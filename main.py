from importlib_metadata import files

from utils import parse_github_url
from github_fetcher import fetch_repo   
from chunker import chunk_files
from vector_store import create_Vector_store
from retriver import retriver_docs
from dotenv import load_dotenv
from langchain.messages import HumanMessage,SystemMessage,AIMessage
from q_Engine import query
load_dotenv()



def main():
    """
    Entry point to test the repo fetching
    
    """
    github_url = "https://github.com/hdRutvik114/Calculator-.git"
    
    owner,repo =parse_github_url(github_url)
    print(f"fetching repo: {owner}/{repo}")
    
    files=fetch_repo(owner,repo)
    
    # print(f"Total files fetched:{len(files)}")
    # print("what files were fetched:", [file['path'] for file in files])
    
    # print first few files TO VERIFY 
    # for file in files[:5]:
    #     print(f"File: {file['path']}, Content Length: {len(file['content'])}")
    #     print("Content preview:",file['content'][:100])  # print first 100 chars of content     
    #     print("-"*50)
        


    chunks,metadatas=chunk_files(files)
    # print(f"Total chunks created: {len(chunks)}")
    # print("what are the first few chunks:", chunks[:3])
    # print("what are the corresponding metadatas:",         metadatas[:3])
        
    vectore_store=create_Vector_store(chunks,metadatas)
    
    print("vectore_store created")
    print("-"*15)
    # question="calculator"
    # docs=retriver_docs(vectore_store,question)
    # print("\nTop RelevantChunks:\n")
    # # print(docs)
    # print("\nTop RelevantChunks:\n")

    
 
    # print("\n=== RAW DOCS ===\n ")
             
    messages=[SystemMessage(content="Your a good coder ")]
    
    
    while True:
        userinput=input("User: ")
        if userinput.lower() in ["exit", "quit", "stop", "done"]:
            print("Goodbye 👋")
            break
        print("You : ",userinput)
        messages.append(HumanMessage(content=userinput))
        docs = retriver_docs(vectore_store, userinput)
        check=query(userinput,docs,messages)
        messages.append(AIMessage(content=check))
        print("Ai : ",check)
        print("-"*10)
        
        
        
        
        
        
                
    # for i, doc in enumerate(docs ):
    #     print(f"\n--- Document {i+1}  ---")
         
    #     # show full metadata  safely
    #     print("Metadata:", doc.metadata )
         
    #     # show full content (or partial if too long )
    #     print("Content:\n", doc.page_content )
    
    # print("\n\n")
    # print("="*10)
    # gotcha=query(question,docs)
    # print(gotcha)
    
        
if __name__ == "__main__":
    main()
    