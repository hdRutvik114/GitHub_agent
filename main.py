from utils import parse_github_url
from github_fetcher import fetch_repo   
from chunker import chunk_files
from vector_store import create_Vector_store
from retriver import retriver_docs
from dotenv import load_dotenv
load_dotenv()
def main():
    """
    Entry point to test the repo fetching
    
    """
    github_url = "https://github.com/hdRutvik114/BOOKS_open.git"
    
    owner,repo =parse_github_url(github_url)
    print(f"fetching repo: {owner}/{repo}")
    
    files=fetch_repo(owner,repo)
    
    print(f"Total files fetched:{len(files)}")
    print("what files were fetched:", [file['path'] for file in files])
    
    # print first few files TO VERIFY 
    for file in files[:5]:
        print(f"File: {file['path']}, Content Length: {len(file['content'])}")
        print("Content preview:",file['content'][:100])  # print first 100 chars of content     
        print("-"*50)
        


        chunks,metadatas=chunk_files(files)
        print(f"Total chunks created: {len(chunks)}")
        print("what are the first few chunks:", chunks[:3])
        print("what are the corresponding metadatas:",         metadatas[:3])
        
    vectore_store=create_Vector_stre(chunks,metadatas)
    
    print("vectore_store created")
    print("-"*10)
    question="who is rutvik"
    docs=retriver_doc(vectore_store,question)
    print("\nTop RelevantChunks:\n")
    # print(docs)
    print("\nTop RelevantChunks:\n")

    for i, doc in enumerate(docs):
        print(f"\n--- Chunk {i+1} ---")
        print("Source:", doc.metadata  ["source"])
        print("Content preview:", doc. page_content[:20])
        
        
if __name__ == "__main__":
    main()
    