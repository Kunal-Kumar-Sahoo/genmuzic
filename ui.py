import streamlit as st
from music_generator import MusicGenerator
import base64
import os


class MusicGeneratorUI:
    def __init__(self):
        self.music_generator = MusicGenerator()

    def get_binary_file_downloader_html(self, binary_file, file_label='File'):
        with open(binary_file, 'rb') as file:
            data = file.read()

        binary_string = base64.b64encode(data).decode()
        return f'''<a href="data:application/octet-stream;base64,{binary_string}" 
        download={os.path.basename(binary_file)}>
            Download {file_label}
        </a>
        '''
    
    def run(self):
        st.set_page_config(
            page_icon=':musical_note:',
            page_title='GenMuzic'
        )

        st.title('GenMuzic: Text2Music App built using AudioCraft/MusicGen')

        text_area = st.text_area('Enter your music description...')
        time_slider = st.slider('Select time duration (in seconds)', 2, 30, 10)

        audio_dir = './audio_output'
        os.makedirs(audio_dir, exist_ok=True)

        if text_area and time_slider:
            st.json({
                'Your Description': text_area,
                'Selected Time Duration (in seconds)': time_slider
            })

            st.subheader('Generated music')

            music_tensors = self.music_generator.generate_music_tensors(text_area, time_slider)
            audio_file_path = self.music_generator.save_audio(music_tensors, audio_dir)
            audio_file = open(audio_file_path, 'rb')
            audio_bytes = audio_file.read()

            st.audio(audio_bytes)
            st.markdown(
                self.get_binary_file_downloader_html(audio_file_path, 'Audio'),
                unsafe_allow_html=True
            )

        st.sidebar.title('Previous Work Samples')
        sample_files = os.listdir(audio_dir)
        for i, sample_file in enumerate(sample_files):
            st.sidebar.audio(os.path.join(audio_dir, sample_file), f'Sample {i+1}')

        # st.footer('Made with :heart: by [Kunal Kumar Sahoo](https://github.com/Kunal-Kumar-Sahoo)')
