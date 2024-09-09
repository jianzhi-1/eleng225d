from pydub import AudioSegment
import os

folder_path = './speech_strange'
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for file in file_names:
    audio = AudioSegment.from_file(f"{folder_path}/{file}", format="m4a")
    audio.export(f"{folder_path}/{file.split('.')[0]}.wav", format="wav")
