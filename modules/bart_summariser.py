from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

# Load model and tokenizer
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Create summarization pipeline
summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

# Some long text, each element is a large string from a <= 20 minute audio chunk
#text_from_audio_chunks = []


def summarise_text_from_audio_chunks(text_from_audio_chunks, max_tokens):
    
    print("\nStarting BART summarisation...")
    
    # limited array where each element is capped at 1000 tokens for the bart model to summarise
    token_limited_text = []

    for index, chunk in enumerate(text_from_audio_chunks):
        print(f'summarising chunk #{index}')
        # break up each element string into new array and build back up
        words = chunk.split(" ")
        s = ""
        
        for word in words:
            s += f'{word} '
            tokens = tokenizer.encode(s, return_tensors='pt')
            if tokens.shape[1] >= max_tokens:  # Check number of tokens instead of words (1024 max for bart)
                token_limited_text.append(s.strip())  # Remove trailing space
                s = ""
                
        if s:  # Append remaining words if less than 1000 tokens 
            token_limited_text.append(s.strip())

    summary_string = ""

    for chunk in token_limited_text:
        summary = summarizer(chunk, do_sample=False)
        summary_string += (summary[0]['summary_text'])

    #print(summary_string)
    print("BART summarisations complete")
    return summary_string
