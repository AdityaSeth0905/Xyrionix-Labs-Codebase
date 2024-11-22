from fastapi import FastAPI
from pydantic import BaseModel
import random

# Define the FastAPI app
app = FastAPI()

# Create a Chatbot class
class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello! How can I help you?", "Hey, how can I assist you today?"],
            "how are you": ["I'm just a bot, but I'm doing well, thank you!", "I'm doing great, how about you?"],
            "product": ["Our product is a fire early warning and suppression system.", "We provide advanced fire detection and prevention solutions."],
            "thanks": ["You're welcome!", "Glad I could help!"],
            "bye": ["Goodbye! Have a great day.", "See you later!", "Bye, stay safe!"]
        }
    
    def get_response(self, user_input: str):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "Sorry, I didn't understand that. Can you ask something else?"

# Initialize chatbot
chatbot = Chatbot()

# Define the input and output models
class UserInput(BaseModel):
    message: str

# API endpoint to get chatbot response
@app.post("/chat/")
async def chat(user_input: UserInput):
    response = chatbot.get_response(user_input.message)
    return {"response": response}
