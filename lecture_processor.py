import modules.video_to_audio as video_to_audio
import modules.audio_chunker as audio_chunker
import modules.openai_interface as openai_interface
import modules.bart_summariser as bart_summariser


if __name__ == '__main__':
    # select video and turn into audio
    output_filename = video_to_audio.process_video_to_audio()
    
    # convert audio in manageable chunks
    audio_chunker.chunk_audio(output_filename)
    
    # using the whisper endpoint, transcribe each audio chunk into text
    transcriptions = openai_interface.transcribe()
    
    # using the bart model, summarise each of the transcription chunks in the transcriptions list
    summary_string = bart_summariser.summarise_text_from_audio_chunks(transcriptions,1000)
    
    # pass the built summary string to gpt-4 to create some revision questions and output to txt file
    openai_interface.create_revision_questions(summary_string)