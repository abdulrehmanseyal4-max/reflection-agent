from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a strict Twitter content reviewer. Your job is to critique the tweet."
            "Identify weaknesses, unclear sentences, missing hooks, and ways to increase virality."
            "Keep critique short, clear, and actionable. DO NOT rewrite the tweet."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional Twitter tech influencer assistant."
            "Your job is to write the best possible improved version of the user's tweet."
            "If the last message starts with 'Critique:', revise your previous output accordingly."
            "Do NOT ask the user questions. Do NOT refuse. Just generate the improved tweet."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOllama(model="llama3.1:latest", stream=False)

reflect_chain = reflection_prompt | llm
generate_chain = generation_prompt | llm
