from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

def query(question,docs):
    context="\n\n".join([d.page_content for d in docs[:4]])
    parser=StrOutputParser()
    promt=PromptTemplate(
    template="""
    
    Instructions:
    - Answer ONLY using the provided code context
    - Be specific and technical
    - If not found, say: " check for tools ..if no tools then say what it needs to be searched
    "
  
    
    Code Context:
    {context}

    
    Question:
    {question}
    """,input_variables=["context","question","history"])
    chain=promt | llm | parser
    
    
    
    ans=chain.invoke({"context":context,"question":question})
    return ans
    