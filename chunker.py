from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_files(files):
   """
    Convert full file contents into smaller chunks.

    Why?
    - LLMs can't handle large files directly
    - Smaller chunks improve retrieval accuracy

    Input:
    - files: list of { path, content }

    Output:
    - chunks: list of text chunks
    - metadatas: list of metadata (file source)
   """
   
   splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
   
   chunks=[]
   metadatas=[]
   
   for file in files:
       content=file['content']
       path=file['path']
       
       if not content or len(content.strip())==0:
           continue  # skip empty files

       file_chunks=splitter.split_text(content)
       chunks.extend(file_chunks)
       metadatas.extend([{'file_path': path} for _ in file_chunks])
       
       return chunks, metadatas