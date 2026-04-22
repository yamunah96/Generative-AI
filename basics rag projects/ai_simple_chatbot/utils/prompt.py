def my_prompt(context_chunks,query):
    #  what is transformer (chunks) + actual query
    context="\n\n".join(context_chunks)
    return f"""use the context below to answer the question"
        Context:
        {context}

        Question
        {query}

        Answer: """