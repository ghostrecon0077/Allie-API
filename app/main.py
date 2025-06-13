# app/main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.memory import get_context_for_user, save_message_to_memory
from app.router import get_openrouter_response
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Allie Protocol API", description="Context-aware AI API powered by OpenRouter.ai", version="1.0.0")

# ✅ Define request model
class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat_endpoint(data: ChatRequest):
    user_id = data.user_id
    user_message = data.message

    # 🔄 Retrieve recent memory
    context = get_context_for_user(user_id)

    # 🔁 Call OpenRouter with memory context
    reply = await get_openrouter_response(user_message, context)

    # 💾 Save both user message and AI reply
    save_message_to_memory(user_id, user_message, "user")
    save_message_to_memory(user_id, reply, "assistant")

    return {"reply": reply}
