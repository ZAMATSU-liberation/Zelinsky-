# Zammy Discord AI Bot 🤖

A Discord chatbot powered by Groq + LLaMA 3.1 using `discord.py`.

The bot replies naturally in a casual Delhi/Gen-Z style conversation whenever users mention `zam`.

---

# Features

- AI-powered Discord chatbot
- Uses Groq API with LLaMA 3.1
- Custom personality + slang responses
- Modular cog system
- Moderation support
- Roleplay commands
- Dynamic role changing
- Async architecture using `discord.py`

---

# Tech Stack

- Python
- discord.py
- Groq API
- dotenv
- asyncio

---

# Project Structure

```txt
project/
│
├── main.py
├── .env
├── requirements.txt
│
├── cogs/
│   ├── moderation.py
│   ├── roleplay.py
│   └── role_changing.py
```

---


## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
TOKEN=your_discord_bot_token
groq_api_key=your_groq_api_key
```

---

# Running the Bot

```bash
python main.py
```

If everything works correctly:

```txt
Bot is online as <bot_name>
```

---

# Bot Usage

Mention `zam` in a message:

```txt
zam how are you
```

Example reply:

```txt
mai mast bhai tu bata 😭
```

---

# Commands Prefix

Supported prefixes:

```txt
!
?
zam
```

---

# Required Intents

Enable these intents in the Discord Developer Portal:

- Message Content Intent
- Server Members Intent

Portal:

https://discord.com/developers/applications

---


# Dependencies

Example `requirements.txt`

```txt
discord.py
python-dotenv
groq
```

---

# Future Improvements

- Memory system
- Slash commands
- Voice support
- MongoDB integration
- Conversation history
- Better moderation tools

---

# License

MIT License

---

# Author

Made with chaos and caffeine ☕
