# ChatbotV1

A simple, menu-driven chatbot built with Python.

This project is part of my journey learning Python, including modules, functions, exception handling, and saving data using JSON.

## Features

* Random greetings
* Random cheese-related responses
* Random jokes
* Random weather responses
* Saves chat history to a JSON file
* Loads previously saved chat history
* Handles invalid menu input

## Project Structure

CHATBOTV1/
├── main/
│   ├── __init__.py
│   └── chatbot.py
├── options/
│   ├── __init__.py
│   ├── greeting.py
│   ├── jokes.py
│   ├── wheather.py
│   └── cheese.py
├── .gitignore
└── README.md

The `chatbot_history.json` file is generated when the program saves its history.

## How to Run

Make sure Python is installed.

Open a terminal in the directory containing the `CHATBOTV1` folder and run:

bash
python -m CHATBOTV1.main.chatbot

## Purpose

This project is a learning exercise to practise Python programming, organising code into modules, handling user input, and working with files.

## Future Improvements

* Add more chatbot responses
* Improve error handling
* Add a command to view previous chat history
* Expand the chatbot's conversational abilities

---
