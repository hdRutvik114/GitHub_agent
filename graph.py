from typing import TypedDict

from langgraph.graph import StateGraph,START,END
from q_Engine import query
from retriver import retriver_docs



# ----State------
class Graph(TypedDict):
    question : str
    docs : list
    answer :str
    vectore_store : object
    

# Node1 

def retrive_node(state):
    docs = retriver_docs(state['vectore_store'],state['question'])
    
    return {"docs" : docs}

def qa_node(state):
    ans= query(state['question'],state['docs'])
    return {'answer':ans}


chat=StateGraph(Graph)
chat.add_node("retrive",retrive_node)
chat.add_node("question_asking",qa_node)

chat.add_edge(START,"retrive")
chat.add_edge("retrive","question-asking")
chat.add_edge("question_asking",END)

workflow=chat.compile()
print(workflow)



     
    

    
    

    