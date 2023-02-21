import streamlit as st 
import pandas as pd 
import numpy as np
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate


#image = Image.open('C:/Users/aswin/Downloads/download.jpg')

#st.image(image, caption='AmplifAI Logo')
api_Key="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"
def model(template,q1):
    count1=0
    x=st.text_input("Your Response")
    if x !="" :
        count1+=1
        x= "Agent: "+x 
        
    if count1==1:
    
        prompt_template = PromptTemplate(input_variables=["chat_history","question"], template=template)
        memory = ConversationBufferMemory(memory_key="chat_history")
        
        llm_chain = LLMChain(
            llm=OpenAI(openai_api_key=api_Key),
            prompt=prompt_template,
            verbose=True,
            memory=memory,
        )
        
        r=llm_chain.predict(question=x)
        print("First output: ")
        print(r)
        
        st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
        st.write(r)
        count1+=1
    
    
    
    if count1==2:
        st.write(q1)
        st.write("Agent: ")
        y=st.text_input("Your Response",key = "text2")
        
        if y !="" :
            count1+=1
            y= "Agent: "+y
            
    if count1==3:
        print("Second Output: ")
        
        result = llm_chain.predict(question=q1+y)
        print("Second Output: ")
        print(result)
        st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
        st.write(result)
    


count=0

st.title("AmplifAI ChatPro")


st.subheader("How would you respond to the following customer?")
x=st.selectbox("Select a scenario :",("","Billing Issue","Check Order Status","Military Discount"))


if x=="Billing Issue":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for an angry customer that is having billing issues.
        Customer:  Hello, you guys keep billing me incorrectly and I have called multiple times and its not fixed.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for an angry customer that is having billing issues.")
        st.write("Customer:  Hello, you guys keep billing me incorrectly and I have called multiple times and its not fixed.\nAgent:")
        q1="Customer: I have been on the call for more than an hour. "
        model(template,q1)
        
        #Getting the first input
# =============================================================================
#         x=st.text_input("Your Response")
#         if x !="" :
#             count+=1
#             x= "Agent: "+x    
#         
#         if count==1:
#         
#             prompt_template = PromptTemplate(input_variables=["chat_history","question"], template=template)
#             memory = ConversationBufferMemory(memory_key="chat_history")
#             
#             llm_chain = LLMChain(
#                 llm=OpenAI(openai_api_key="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"),
#                 prompt=prompt_template,
#                 verbose=True,
#                 memory=memory,
#             )
#             
#             t="I am sorry for the inconvinence"
#             r=llm_chain.predict(question=x)
#             print("First output: ")
#             print(r)
#             
#             st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
#             st.write(r)
#             count+=1
#         
#         
#         
#         if count==2:
#             st.write("Customer: I have been on the call for a long time probably an hour.")
#             st.write("Agent: ")
#             y=st.text_input("Your Response",key = "text2")
#             
#             if y !="" :
#                 count+=1
#                 y= "Agent: "+y
#                 
#         if count==3:
#             print("Second Output: ")
#             
#             result = llm_chain.predict(question="Customer: I have been on the call for more than an hour. "+y)
#             print("Second Output: ")
#             print(result)
#             st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
#             st.write(result)
# =============================================================================
            
if x=="Military Discount":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer enquiring about military discount.
        Customer:  Hello, I wanted to check with you guys about military discount.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer enquiring about military discount.")
        st.write("Customer:  Hello, I wanted to check with you guys about military discount.")
        st.write("Agent: ")
        q1="Customer: How much discount do you provide as a part of military discount?"
        model(template,q1)
        #Getting the first input
# =============================================================================
#         x=st.text_input("Your Response")
#         if x !="" :
#             count+=1
#             x= "Agent: "+x    
#         
#         if count==1:
#         
#             prompt_template = PromptTemplate(input_variables=["chat_history","question"], template=template)
#             memory = ConversationBufferMemory(memory_key="chat_history")
#             
#             llm_chain = LLMChain(
#                 llm=OpenAI(openai_api_key="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"),
#                 prompt=prompt_template,
#                 verbose=True,
#                 memory=memory,
#             )
#             
#             t="I am sorry for the inconvinence"
#             r=llm_chain.predict(question=x)
#             print("First output: ")
#             print(r)
#             
#             st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
#             st.write(r)
#             count+=1
#         
#         
#         
#         if count==2:
#             st.write("Customer: How much discount do you provide as a part of military discount?")
#             st.write("Agent: ")
#             y=st.text_input("Your Response",key = "text2")
#             
#             if y !="" :
#                 count+=1
#                 y= "Agent: "+y
#                 
#         if count==3:
#             print("Second Output: ")
#             
#             result = llm_chain.predict(question="Customer: How much discount do you provide as a part of military discount? "+y)
#             print("Second Output: ")
#             print(result)
#             st.write("AmplifAI Nexa: The following can be a better way of responding to this situation.")
#             st.write(result)
# =============================================================================
            
            

if x=="Check Order Status":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who wants to check the order status.
        Customer:  Hello, I want to check the status of my order.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who wants to check the order status.")
        st.write("Customer:  Hello, I want to check the status of my order.")
        st.write("Agent: ")
        q1="Customer: Can you tell me when it will be delivered."
        model(template,q1)




