import agent
import os
from agent import Agent
from dotenv import load_dotenv
from flask import Flask, request

# Load default environment variables (.env)
load_dotenv()

AGENT_NAME = os.getenv("AGENT_NAME", "my-agent")

agent = Agent(AGENT_NAME)

# Creates Pinecone Index
agent.createIndex()

app = Flask(__name__)

print("Talk to the AI!")

@app.route("/", methods=['POST'])
def default_action():
    request_keys = request.form.keys()
    print(request_keys)
    agent_response = agent.action(request.form.request_keys[0])
    return agent_response
    
if __name__ == "__main__":
    app.run()
