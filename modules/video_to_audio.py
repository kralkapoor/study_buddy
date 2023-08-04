from moviepy.editor import AudioFileClip
import os

def get_file_path():
    name = input("Absolute path to video file: ")
    return name

def convert_mp4_to_mp3(video_filename, audio_filename):
    video_file = AudioFileClip(video_filename)
    video_file.write_audiofile(audio_filename, write_logfile=False)

def move_output(output_filename):
    pass
    #os.replace(output_filename, f'')

def process_video_to_audio():
    input_filename = get_file_path()
    output_filename = f'{input_filename.split(".")[0]}.mp3'
    print(f'Processing {input_filename} to mp3...')
    convert_mp4_to_mp3(input_filename, output_filename)
    print('Video to audio processing complete')
    return output_filename
    
if __name__ == '__main__':
    process_video_to_audio()
