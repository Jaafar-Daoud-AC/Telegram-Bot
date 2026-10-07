<div align="center">

# 🤖 Telegram Bot: Gold, Dollar & Tools

**My first Telegram bot — the project where I learned how to build Telegram bots from scratch**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)
![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-telebot-blue)
![Status](https://img.shields.io/badge/Status-Learning%20Project-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

[🇬🇧 English](README.en.md) · [🇸🇦 العربية](README.md)

</div>

---

## 📖 About

This is **the first Telegram bot I ever built**. I created it while learning how to develop Telegram bots with **Python** and the **pyTelegramBotAPI** library.

The bot offers a few simple, practical services right inside the chat:

- Gold prices in Egypt by karat.
- US dollar exchange rates against several currencies.
- A quick calculator.
- A ratio-to-decibel (dB) converter.

> 💡 **Note:** This is primarily a learning project, built to practice the core concepts of bot development in a clean, organized way.

---

## ✨ Features

| Command | Description | Example |
|---------|-------------|---------|
| `/start` or `/help` | Welcome message and command list | `/help` |
| `/gold` | Gold prices in Egypt (24, 21, 18, 14, 10 karat), sell and buy | `/gold` |
| `/dollar` | 1 USD against SYP, EGP, TRY and EUR | `/dollar` |
| `/calc` | Basic calculator | `/calc 5*(2+3)` |
| `/db` | Convert a ratio to decibels (power and voltage) | `/db 100` |

### Extras

- 💬 **Plain-text replies:** typing "ذهب", "دولار", "gold" or "dollar" works without a command.
- ⚡ **Caching:** results are cached for 10 minutes so the sources aren't hit on every message.
- 🛡️ **Error handling:** clear messages when fetching fails or the input is invalid.
- 🔒 **Safer calculator:** only digits and `+ - * / % ( )` are accepted; exponents and long expressions are rejected.
- 🔑 **Token safety:** the token lives in a `.env` file that is never pushed to GitHub.
- 📋 **Command menu:** commands appear in Telegram's menu via `set_my_commands`.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) | Building the bot and handling messages/commands |
| [python-decouple](https://github.com/HBNetwork/python-decouple) | Reading secrets from `.env` |
| [requests](https://requests.readthedocs.io/) | HTTP requests |
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) + [lxml](https://lxml.de/) | Parsing the web page to extract gold prices |

**Data sources:**

- Gold: [masrawy.com/gold](https://www.masrawy.com/gold)
- Currencies: [open.er-api.com](https://open.er-api.com)

---

## 📁 Project Structure

```
pot_telegram/
├── bot_telegram.py    # Entry point: bot setup, commands and message handlers
├── gold.py            # Gold prices via web scraping
├── dollar.py          # Exchange rates via API
├── tools.py           # Calculator and decibel converter
├── requirements.txt   # Dependencies
├── .env.example       # Example environment file
├── .gitignore         # Files excluded from Git
└── README.md
```

Each feature lives in its own module to keep the code organized and easy to change.

---

## 🚀 Getting Started

### 1) Requirements

- Python 3.8 or newer
- A Telegram account and a bot token from [@BotFather](https://t.me/BotFather)

### 2) Clone

```bash
git clone https://github.com/YOUR_USERNAME/pot_telegram.git
cd pot_telegram
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure the token

Copy the example file and create your `.env`:

```bash
cp .env.example .env
```

Then open it and add your token:

```env
BOT_TOKEN=your_token_here
```

### 5) Run

```bash
python bot_telegram.py
```

Open the bot in Telegram and send `/start` 🎉

---

## 💬 Usage Examples

```
/gold
→ Gold prices in Egypt (EGP)
  Karat 24 : sell ... | buy ...
  ...

/dollar
→ Price of 1 USD:
  Egyptian Pound : ...
  ...

/calc 5*(2+3)
→ 5*(2+3) = 25

/db 100
→ Ratio 100
  Power:   10 log10(P2/P1) = 20.0 dB
  Voltage: 20 log10(V2/V1) = 40.0 dB
```

*(Bot replies are in Arabic.)*

---

## 🎓 What I Learned

As my first bot, this project taught me the fundamentals:

- Creating a bot with **BotFather** and getting a token.
- Handling commands and messages with **message handlers**.
- Keeping the bot running with **polling** (`infinity_polling`).
- Registering the command menu with `set_my_commands`.
- Extracting data from websites with **web scraping** and **regular expressions**.
- Consuming a **REST API** and parsing JSON.
- Using **caching** to cut down requests and speed up replies.
- **Input validation** and **exception handling** (`try / except`).
- Protecting secrets with environment variables (`.env`) and `.gitignore`.
- Splitting a project into independent **modules**.

---

## 🗺️ Roadmap

- [ ] Inline keyboard buttons.
- [ ] Silver prices and more currencies.
- [ ] Let users choose their currency.
- [ ] Logging.
- [ ] Deploy to a server (VPS / Docker).
- [ ] Additional languages.

---

## ⚠️ Notes

- Gold prices are parsed from the page text, so if masrawy.com changes its layout, `gold.py` may need a small update.
- Dollar rates are official rates from the listed source and may differ from the street market.
- Prices are for information only and are not financial advice.

---

## 🤝 Contributing

This project is at an early stage, and feedback that helps me learn is welcome. Feel free to open an **Issue** or submit a **Pull Request**.

---

## 📄 License

Released under the **MIT** License.

---

## 👤 Author

**Jaafar Dawood** (جعفر داؤد)

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

<div align="center">

⭐ If you like this project, consider giving it a star!

</div>
