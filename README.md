# 🗣️ Python Voice Assistant

A simple, offline-friendly voice assistant built with Python. It uses speech recognition and text-to-speech to understand and respond to your voice. No API keys or paid services required — perfect for beginners and personal projects.

---

## ✨ Features

- 👋 Greets you  
- ⏰ Tells the current time  
- ➗ Solves basic math expressions (e.g., "what is 7 times 6")  
- 🌐 Opens websites (e.g., "open google")  
- 😂 Tells random programming jokes  
- 📚 Searches Wikipedia for quick info  
- 🛑 Listens for “stop” or “exit” to end the session  

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

### `requirements.txt` includes:
- SpeechRecognition  
- pyttsx3  
- pyjokes  
- wikipedia  

**Note:**  
- For speech recognition to work, you’ll need a working microphone.  
- On Windows, `pyaudio` may require manual installation. You can use precompiled `.whl` files if needed.  

---

## 🚀 Getting Started

1. Clone this repo or download the code.  
2. Open a terminal in the project folder.  
3. Run the Python file:

```bash
python voice_assistant.py
```

4. Speak a command when prompted!  

---

## 🧠 Example Commands

| Command Example            | What It Does                  |
|---------------------------|-------------------------------|
| `hello`                   | Greets you                    |
| `what is 8 plus 5`        | Solves math and speaks result |
| `open youtube`            | Opens https://youtube.com     |
| `tell me a joke`          | Tells a programming joke       |
| `wikipedia python`        | Gives a short summary          |
| `what time is it`         | Speaks the current time        |
| `exit` or `stop`          | Ends the program               |

---

## 🧩 How It Works

The assistant listens to your voice using `SpeechRecognition`, parses the command, and performs actions like:  
- Calculating math expressions with `eval()`  
- Opening websites with `webbrowser`  
- Speaking responses with `pyttsx3`  
- Searching with the `wikipedia` library  
- Telling jokes with `pyjokes`

---

## 📂 Project Structure

```
voice-assistant/
│
├── voice_assistant.py       # Main program
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🛡 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share it.

---

## 🙌 Contributing

Pull requests are welcome! If you have cool feature ideas — like weather updates, note-taking, or reminders — feel free to fork and improve this project.

---

## ❤️ Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [pyjokes](https://pypi.org/project/pyjokes/)

---

> Made with Python and curiosity ✨
