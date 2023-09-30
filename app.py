import os
import base64
import streamlit as st
import numpy as np
import torch
import torchaudio
from audiocraft.models import MusicGen

@st.cache_resource
def load_model():
    return MusicGen.get_pretrained('facebook/musicgen-small')

def generate_music_tensors(description, duration):
    print('Description:', description)
    print('Duration:', duration)
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    with st.spinner('Generating music...'):
        output = model.generate(
            descriptions=[description],
            progress=True,
            return_tokens=True
        )

    return output[0]

def save_audio(samples):
    sample_rate = 32000
    save_path = './audio_output'

    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()

    if samples.dim() == 2:
        samples = samples[None, ...]
    
    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f'audio_{idx}.wav')
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    
    binary_string = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{binary_string}" download={os.path.basename(bin_file)}>Download {file_label}</a>'

st.set_page_config(
    page_icon=':musical_note:',
    page_title='GenMuzic'
)

def main():
    st.title('Text2Music Generation')

    with st.expander('About app'):
        st.write('This is a music generation app built using Meta\'s AudioCraft library (MusicGen). Based on your Natural Langauge description, it can generate music!')
    
    text_area = st.text_area('Enter your description...')
    time_slider = st.slider('Select time duration (s)', 2, 30, 10)

    if text_area and time_slider:
        st.json({
            'Your Description': text_area,
            'Selected Time Duration (in seconds)': time_slider 
        })

        st.subheader('Generated Music')
        music_tensors = generate_music_tensors(text_area, time_slider)
        print('Music tensors:', music_tensors)
        save_music_file = save_audio(music_tensors)
        audio_file_path = './audio_output/audio_0.wav'
        audio_file = open(audio_file_path, 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes)
        st.markdown(get_binary_file_downloader_html(audio_file_path, 'Audio'), unsafe_allow_html=True)

if __name__ == '__main__':
    main()