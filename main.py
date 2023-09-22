import os
import shutil
import subprocess
import json
from audiosr import build_model, super_resolution, save_wave

def get_sample_rate(file_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'a:0',
        '-show_entries', 'stream=sample_rate',
        '-of', 'json',
        file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = json.loads(result.stdout)
    return int(output['streams'][0]['sample_rate'])

datasets_path = './datasets/'
speakers = [d for d in os.listdir(datasets_path) if os.path.isdir(os.path.join(datasets_path, d))]
audiosr = build_model(model_name='speech', device="auto")

for speaker in speakers:
    folder_path = os.path.join(datasets_path, speaker)
    source_wavs_folder = os.path.join(folder_path, 'source_wavs')
    if not os.path.exists(source_wavs_folder):
        os.makedirs(source_wavs_folder)

    files = os.listdir(folder_path)

    for file in files:
        input_path = os.path.join(folder_path, file)
        base_name, _ = os.path.splitext(file)
        wav_file_name = f"{base_name}.wav"
        wav_path = os.path.join(folder_path, wav_file_name)
        
        if file.endswith('.mp3'):
            try:
                sample_rate = get_sample_rate(input_path)
                subprocess.run(["ffmpeg", "-i", input_path, "-ar", str(sample_rate), "-ac", "1", wav_path], check=True)
                os.remove(input_path)
            except subprocess.CalledProcessError as e:
                print(f"Error occurred while converting {input_path} to WAV: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        
        if file.endswith('.wav') or file.endswith('.mp3'):
            shutil.move(wav_path, os.path.join(source_wavs_folder, wav_file_name))

for speaker in speakers:
    folder_path = os.path.join(datasets_path, speaker)
    wavs_folder = os.path.join(folder_path, 'wavs')
    source_wavs_folder = os.path.join(folder_path, 'source_wavs')
    if not os.path.exists(wavs_folder):
        os.makedirs(wavs_folder)

    source_wavs_files = os.listdir(source_wavs_folder)

    for file in source_wavs_files:
        if file.endswith('.wav'):
            input_path = os.path.join(source_wavs_folder, file)
            save_path = os.path.join(wavs_folder)
            try:
                waveform = super_resolution(
                    audiosr,
                    input_path,
                    seed=42,
                    guidance_scale=3.5,
                    ddim_steps=50,
                    latent_t_per_second=12.8
                )
                base_name, _ = os.path.splitext(file)
                save_wave(waveform, save_path, name=base_name, samplerate=48000)
            except Exception as e:
                print(f"An error occurred: {e}")
