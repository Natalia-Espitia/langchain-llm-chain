import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI assistant."),
    ("user", "Explain the concept of {topic} in simple terms.")
])

# Create chain
chain = prompt | llm | StrOutputParser()

# Run chain
response = chain.invoke({"topic": "Retrieval-Augmented Generation"})

print("\nResponse:\n")
print(response)