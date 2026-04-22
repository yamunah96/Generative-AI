def chunk_text(text,chunk_size=100):
    words= text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words),chunk_size)]


# print(chunk_text("This is a sample text to demonstrate how to chunk text into smaller pieces.", chunk_size=5))