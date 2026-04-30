
def retriver_docs(vectorestore,question):
    """
    Retrieve most relevant chunks from the vector database.

    Input:
    - vectorstore: your Chroma DB
    - question: user query

    Output:
    - list of relevant documents (chunks)
    """
    retriver=vectorestore.as_retriever(search_kwarg={"k":3})
    # Perform semantic search
    docs = retriver.invoke(question)
    return docs