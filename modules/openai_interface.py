import openai
import os
from dotenv import load_dotenv

# load key and pass it to openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_revision_questions(summary, output_filename):
    
    #summary = "Today we will be talking about a different type of strategy. We are looking into problems that can be represented in a state space. While we are searching for a solution, we are building a search tree that represents all the states, all the nodes that we are visiting on that graph. And also, it keeps track of the frontier. We're looking into a search algorithm.The cost associated to each arc is proportion to the length of that arc, okay? So we know that straight line represents the shortest path, right? So green, blue, red would be the optimal path. If you use uniform cost search, it will not go to the blue line. It will try to first explore all the states which are easier and faster to reach.Heuristics are criteria, or you can implement it as a method or principle, deciding which among several alternative course actions are most promising. For every problem, you will need to think what kind of function can tell you whether you're going in the right direction. Informed search strategies, basically, you need to go a little bit beyond that definition.The first algorithm we'll be looking at, it's called greedy best-first search, or just greedy search. This is because, basically, this algorithm solely relies on the heuristic. It ignores all the information about the path cost. So the idea is that we are selecting the path whose end is closest to the gold.So we have this graph. And we can try to perform it. So if we will look at this graph again, we are starting with all 103. So what we have, we have TS, B3, and O109. TS gives us, right there, 23. B3 gives us 17. O109 gives us 24. So out of all of them, I think B3 is the closest.In the next lecture, we will be talking about a different algorithm, which also is an informed search strategy. We do have something that kind of adds to the greedy search, which helps us to have kind of like a better algorithm if we need to find an optimal solution. So I think that's the end of this lecture. It's pretty short.You will also need to go and complete exercise in the Jupyter Notebook. Why is it important? Because soon I will be releasing your assignment, and if you're doing this now, then you're all prepared to start doing your assignment. I also want to remind then that you can attend also undergrads tutorials if you experiencing problems."
    
    print("GPT-4 working on report...")
    
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a assistant who converts an abridged version of a lecture recording into revision and exercise questions to assist with learning. Firstly, give an overview of the lecture, identifying the key points. Then, at the top, include the questions and exercises, and at the bottom include some model answers. Aim to have at least 10 revision questions, but provide as many as possible while maintaining good quality."},
        {"role": "user", "content": summary}
    ]
    )
    #print(completion.choices[0].message["content"])
    
    with open(f'revision_{output_filename}.txt','a') as file_output:
        file_output.write(completion.choices[0].message["content"])


def transcribe(output_filename):
    # init transcript string which we will append to for each chuncked audio file
    transcriptions = []

    # fetch files from dir (default audio_chunks)
    files = fetch_audio_chunks(filename_search=output_filename)

    for file in files:
        audio_file= open(f'audio_chunks/{file}', "rb")
        print(f'Transcribing {file}...')
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        transcriptions.append(transcript["text"])
    print('All transcriptions done')
    

    with open(f'full_trancript_{output_filename}.txt','a') as file:
        for text_chunk in transcriptions:
            file.write(text_chunk)

    return transcriptions

def fetch_audio_chunks(filename_search, path = 'audio_chunks'):
    chunked_audio_files = [file for file in os.listdir(path) if file.endswith('.mp3') and filename_search in file]
    chunked_audio_files.sort()
    return chunked_audio_files

if __name__ == '__main__':
    transcribe()