# app/router.py

import httpx
from app.config import OPENROUTER_API_KEY, REFERER_HEADER, TITLE_HEADER

# 🌐 Send user message + context to OpenRouter and return reply
async def get_openrouter_response(user_message: str, context: list) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": REFERER_HEADER,
        "X-Title": TITLE_HEADER,
        "Content-Type": "application/json"
    }

    messages = context + [{"role": "user", "content": user_message}]
    
    payload = {
        "model": "openrouter/auto",  # or use "mistralai/mixtral-8x7b", etc.
        "messages": messages
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code != 200:
        return f"[OpenRouter Error] {response.status_code}: {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]
