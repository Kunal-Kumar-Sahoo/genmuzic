import streamlit as st
from music_generator import MusicGenerator
import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class MusicGeneratorUI:
    def __init__(self):
        self.music_generator = MusicGenerator()

    def send_email(self, to_email, subject, message, attachment_path):
        from_email = 'devsmail94@gmail.com'  # Update with your email address
        from_password = 'fkoq yprw jyup fhvr'  # Update with your email password

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
            msg.attach(part)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            return True
        except Exception as e:
            st.error(f"Email could not be sent. Error: {str(e)}")
            return False

    def run(self):
        st.set_page_config(
            page_icon=':musical_note:',
            page_title='GenMuzic'
        )

        st.title('GenMuzic: Text2Music App built using AudioCraft/MusicGen')

        email_address = st.text_input('Enter your email address')
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

            if email_address:
                email_subject = 'Generated Music'
                email_message = 'Here is the generated music you requested.'
                email_sent = self.send_email(email_address, email_subject, email_message, audio_file_path)

                if email_sent:
                    st.success(f"Email sent to {email_address} successfully!")
                else:
                    st.error("Failed to send email. Please check your email configuration.")
            else:
                st.warning('Please enter a valid email address.')

        st.sidebar.title('Previous Work Samples')
        sample_files = os.listdir(audio_dir)
        for i, sample_file in enumerate(sample_files):
            st.sidebar.audio(os.path.join(audio_dir, sample_file), f'Sample {i+1}')

if __name__ == '__main__':
    ui = MusicGeneratorUI()
    ui.run()
