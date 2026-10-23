import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load variables from a local .env file into the environment.
load_dotenv()

# Read the API key from the environment; keep the secret out of the script.
api_key = os.environ["OPENAI_API_KEY"]

# Create a LangChain chat model using the gpt-4o-mini model.
llm = ChatOpenAI(model="gpt-4o-mini")

# Define the request as a human message.
prompt = HumanMessage(
    content=(
        "Give exactly 5 healthy breakfast ideas. "
        "Format them as a numbered list, one line each, with no preamble."
    )
)

# Send the prompt to the model. invoke() returns a message object.
reply = llm.invoke([prompt])

# Print only the reply text, not the full message object and its metadata.
print(reply.content)