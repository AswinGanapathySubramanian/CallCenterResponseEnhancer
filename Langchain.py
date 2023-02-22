import streamlit as st 
import pandas as pd 
import numpy as np
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate
import os
#from dotenv import load_dotenv
#load_dotenv()
#image = Image.open('C:/Users/aswin/Downloads/download.jpg')

#st.image(image, caption='AmplifAI Logo')

api_Key=os.getenv("api_Key")
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
x=st.selectbox("Select a scenario :",("","Issue with Order","Order Confirmation","Career Resources","Haven't Received Order","Billing Issue","Check Order Status","Military Discount","Check Product Availability","Order Cancellations","Ask About Shipping or Pick up","File a Complaint","Refund Questions","Request Price Match"))


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

if x=="Check Product Availability":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who wants to check product availability.
        Customer:  Hello, I wanted to check with you guys about the availability of the product.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who wants to check product availability.")
        st.write("Customer:  I wanted to check with you guys about the availability of the product.")
        st.write("Agent: ")
        q1="Customer: How can I order the product. "
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
        q1="Customer: My order number is 01234567. Can you tell me when it will be delivered."
        model(template,q1)

if x=="Order Cancellations":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who wants to cancel their order.
        Customer:  Hello, I want to cancel my order.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who wants to check the order status.")
        st.write("Customer:  Hello, I want to cancel my order.")
        st.write("Agent: ")
        q1="Customer: My order number is 01234567. Can you tell me when will I get the refund."
        model(template,q1)


if x=="Haven't Received Order":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who haven't received their order.
        Customer:  Hello, I haven't received my order yet.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who haven't received their order.")
        st.write("Customer:  Hello, I haven't received my order yet.")
        st.write("Agent: ")
        q1="Customer: My order number is 01234567. Can you tell me when will I get my order."
        model(template,q1)


if x=="Ask About Shipping or Pick up":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer has queries about shipping and pick up.
        Customer:  Hello, I want know about the shipping and pick up.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has queries about shipping and pick up.")
        st.write("Customer:  Hello, I want to know about shipping and pick up.")
        st.write("Agent: ")
        q1="Customer: What is the cost for shipping and pick up."
        model(template,q1)

if x=="Career Resources":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer has queries about Career Resources.
        Customer:  Hello, I want know about the Career Resources.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has queries about Career Resources.")
        st.write("Customer:  Hello, I want to know about Career Resources.")
        st.write("Agent: ")
        q1="Customer: How can I apply to the call center specialist position."
        model(template,q1)

if x=="Order Confirmation":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer has queries about Order Confirmation.
        Customer:  Hello, I want know whether my order is confirmed or not, I haven't received my order confirmation but payment got debitted from my card.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has queries about Order Confirmation.")
        st.write("Customer:  Hello, I want know whether my order is confirmed or not, I haven't received my order confirmation but payment got debitted from my card.")
        st.write("Agent: ")
        q1="Customer: My order number is 09876554. Will I be receiving a order confirmation mail now."
        model(template,q1)

if x=="Issue with Order":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer has issues with order.
        Customer:  Hello, I ordered a toaster but got a blender.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has issues with order.")
        st.write("Customer:  Hello, I ordered a toaster but got a blender.")
        st.write("Agent: ")
        q1="Customer: My order number is 1234576 and I want a toaster and not a blender."
        model(template,q1)


if x=="File a Complaint":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for an angry customer who wants to file a complaint.
        Customer:  Hello, I would like to file a complaint.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for an angry customer who wants to file a complaint.")
        st.write("Customer:  Hello, I would like to file a complaint.")
        st.write("Agent: ")
        q1="Customer: I didn't receive the item I ordered."
        model(template,q1)


if x=="Refund Questions":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who has questions regarding refund.
        Customer:  Hello, I would like to know about my refund status.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has questions regarding refund.")
        st.write("Customer:  Hello, I would like to know about my refund status.")
        st.write("Agent: ")
        q1="Customer: My member id is axg16273. It's been 5 business days but I haven't received my refund yet."
        model(template,q1)

if x=="Request Price Match":
        
        template = """You are a agent in a call center. Given the response of the agent, it is your job to write a better response.
        Scenario: Lets do a quick role play for a customer who has questions regarding price match.
        Customer:  Hello, I would found a better deal on the car on carvanna will you guys do a price match.{chat_history}
        {question}
        AI:
        """
        st.write("Scenario: Lets do a quick role play for a customer who has questions regarding price match.")
        st.write("Customer: Hello, I would found a better deal on the car on carvanna will you guys do a price match.")
        st.write("Agent: ")
        q1="Customer: It's a 2021 honda accord for $29000."
        model(template,q1)