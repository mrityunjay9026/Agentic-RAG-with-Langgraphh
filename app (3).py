import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

import streamlit as st
import json

# Load the agent script
def load_agent():
    try:
        with open("agentic_rag.ipynb", "r") as file:
            agent_code = file.read()
        return agent_code
    except FileNotFoundError:
        st.error("Error: agentic_rag.ipynb file not found.")
        return None
    except Exception as e:
        st.error(f"Error loading agent script: {e}")
        return None

st.title("AI Agent Chat Interface")

# User input
user_input = st.text_area("Enter your query:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a query before submitting.")
    else:
        st.info("Processing your query...")
        try:
            # Simulate response
            response = f"Processed query: {user_input}"
            st.success("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error processing query: {e}")

st.sidebar.subheader("About")
st.sidebar.info("This Streamlit app interacts with an AI agent to answer queries.")
