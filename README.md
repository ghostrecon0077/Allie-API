# Allie-API
API for a Discord AI to make it work anywhere using FastAPI
# 🧠 Allie Protocol API

**Developer:** Marineo — Creator of Marra Discord Bot

A **memory‑aware AI chat API** built with FastAPI. Allie remembers context across messages, responds via OpenRouter, and is structured for extensibility and integration.
Run the API:
1) In the Bash or Terminal in the root folder type : uvicorn app.main:app --reload
2) Then go to : http://localhost:8000/docs

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🎯 `/chat` endpoint | Accepts JSON `{"user_id","message"}` and returns contextual AI response |
| 🗃 SQLite memory storage | Saves user & assistant messages per session |
| 🔄 Contextual history | Includes last 6 messages in prompts for continuity |
| 🔒 Secure key management | Uses `.env` for OpenRouter API key |
| 🧩 Modular design | Clean architecture with `config`, `database`, `memory`, and `router` modules |
| 📄 Interactive docs | Self-documenting with Swagger via `/docs` |
| 🌐 OpenRouter integration | Supports GPT‑3.5, DeepSeek, Mixtral, etc. |

---

## 💻 Tech Stack

- **FastAPI** – Python web framework  
- **Uvicorn** – ASGI server  
- **SQLite** – Lightweight DB for memory  
- **Pydantic** – Input validation  
- **python-dotenv** – Secure config handling  
- **httpx** – Async HTTP client for OpenRouter

---

## 🛠 Getting Started

### Prerequisites
- Python 3.9+
- OpenRouter API key (get one at [https://openrouter.ai](https://openrouter.ai))
----
✨ Future Roadmap
🔐 API token validation
🧼 POST /forget endpoint to reset user memory
🐳 Docker support
🔍 Redis caching (optional)
📊 Usage tracking
----
🧠 Skills Highlighted
✅ Python Backend Development
✅ FastAPI REST Architecture
✅ Async programming (httpx + FastAPI)
✅ SQLAlchemy ORM + SQLite
✅ Secure key handling with dotenv
✅ OpenRouter API integration
✅ Modular codebase for scalability
✅ Swagger UI auto-documentation
----
👤 Author
Marineo
AI Developer, Discord Bot Engineer, System Integrator
GitHub: github.com/ghostrecon0077

