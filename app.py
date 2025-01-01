# Step 1: Import Necessary Libraries
import streamlit as st
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

# Step 2: Define Streamlit Sidebar for API Key Input
st.sidebar.title("Configuration")
groq_api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
submit_key = st.sidebar.button("Submit")

# Step 3: Define Main Streamlit UI
st.title("Simple QA Application")
st.write("Ask a question, and I will answer using the LLM powered by Groq API.")

# Input question from user
user_question = st.text_input("Enter your question here:")

# Step 4: Handle API Key Submission
if submit_key and groq_api_key:
    st.sidebar.success("Groq API key submitted successfully!")
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

    # Step 5: Define Prompt Template
    prompt_template = ChatPromptTemplate.from_template("""
    You are a helpful assistant. Please answer the question below concisely:

    Question: {question}
    Answer:
    """)

    # Step 6: Create QA Chain
    qa_chain = LLMChain(llm=llm, prompt=prompt_template)

        # Step 7: Process Input and Display Output
    if user_question:
        with st.spinner("Thinking..."):
            response = qa_chain.run({"question": user_question})
        st.write("### Answer:")
        st.write(response)



