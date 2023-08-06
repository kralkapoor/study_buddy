from pydub import AudioSegment

def chunk_audio(file_name):
    
    print('Loading mp3 file for chunking...')
    audio = AudioSegment.from_file(f'{file_name}.mp3', format="mp3")
    length_audio = len(audio)
    print('Done\n')
    
    one_minute = 1000 * 60
    twenty_minutes = one_minute * 20
    
    start = 0  # in miliseconds
    end = twenty_minutes  # also in miliseconds
    i = 1
    
    while start < length_audio:
        print(f'Chunking part {i}...')
        chunk = audio[start:end]
        chunk.export(f"audio_chunks/{i}_{file_name}.mp3", format="mp3")
        print(f'Part {i} done\n')
        
        i += 1
        start += twenty_minutes
        end += twenty_minutes

    print("Audio chunking completed")
    
if __name__ == '__main__':
    pass
