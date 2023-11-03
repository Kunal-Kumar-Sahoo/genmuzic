import os, datetime
import torchaudio
from audiocraft.models import MusicGen

class MusicGenerator:
    def __init__(self):
        self.model = None
    
    def load_model(self):
        if self.model is None:
            self.model = MusicGen.get_pretrained(
                'facebook/musicgen-small'
            )
        return self.model
    
    def generate_music_tensors(self, description, duration):
        model = self.load_model()
        model.set_generation_params(
            use_sampling=True,
            top_k=250,
            duration=duration
        )

        output = model.generate(
            descriptions=[description],
            progress=True,
            return_tokens=True
        )

        return output[0]
    
    def save_audio(self, samples, save_path):
        sample_rate = 32000
        os.makedirs(save_path, exist_ok=True)

        assert samples.dim() == 2 or samples.dim() == 3

        samples = samples.detach().cpu()

        if samples.dim() == 2:
            samples = samples[None, ...]
        
        audio_path = ''

        for audio in samples:
            audio_path = os.path.join(save_path, f'audio_{datetime.datetime.now()}.wav')
            torchaudio.save(audio_path, audio, sample_rate)
    
        return audio_path