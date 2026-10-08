# Hangman

A simple command-line Hangman game that fetches a random word from an API.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/HTTP-Requests-2CA5E0?style=for-the-badge)](https://requests.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 🛠️ Tech Stack

- **Python** — game logic
- **Requests** — fetching a random word from the API

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Daivyway/Hangman.git
cd Hangman
```

### Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependency

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python game.py
```

## 🎮 How to Play

Enter one letter at a time to guess the hidden word. Guess all the letters before the hangman is fully drawn to win!

If the API is unavailable, the game uses `hangman` as the default word.

## 📖 Documentation

- [Requests](https://requests.readthedocs.io/)
- [Random Word API](https://random-word-api.herokuapp.com/home)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 💻 Code. Learn. Build. Repeat.

</div>
