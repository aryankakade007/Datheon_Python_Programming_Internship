# Datheon Task 4 - Rule-Based Interactive Chatbot

## Project Overview

This project is a rule-based customer support chatbot developed using Python as part of the Datheon Python Programming Internship.

The chatbot provides an interactive terminal experience and answers common customer support questions using keyword matching, regular expressions, and a JSON-based FAQ dataset.

It supports multiple intents, contextual responses, input validation, and graceful exit handling.

## Features

- Interactive terminal-based conversation
- Friendly greetings and personalized user interaction
- Keyword-based and regular-expression intent recognition
- FAQ responses loaded from a JSON dataset
- Business hours information
- Internship project submission guidance
- Certificate processing information
- Help command to display available features
- Current time and date responses
- Random jokes and motivational messages
- Casual conversation support
- Helpful fallback responses for unknown queries
- Empty input validation
- Graceful exit using `bye`, `exit`, `quit`, or `stop`
- Error handling for missing or invalid FAQ data

## Sample FAQ Information

The chatbot can answer questions about:

| Topic | Information |
|---|---|
| Business Hours | Monday to Friday, 9:00 AM to 6:00 PM IST |
| Project Submission | Submit a public GitHub repository link through the Student Workspace |
| Certificate | Reviewed and issued within 3–5 business days after code review |

FAQ responses are stored in `sample_faq.json` and loaded when the chatbot starts.

## Technologies Used

- Python 3
- JSON
- Regular Expressions (`re`)
- `datetime` module
- `random` module

## Requirements

- Python 3.10 or above
- Visual Studio Code or any Python-supported editor

No external libraries, paid APIs, or AI services are required.

## Project Structure

```text
Task_4_Interactive_Chatbot/
│
├── chatbot.py
├── sample_faq.json
└── README.md
```

## How to Run

1. Download or clone the project repository.
2. Open the `Task_4_Interactive_Chatbot` folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python chatbot.py
```

5. Enter your name and start interacting with the chatbot.

## Example Questions

- Hello
- What are your business hours?
- How do I submit my internship project?
- How can I upload my project to GitHub?
- When will I receive my certificate?
- Help
- Tell me a joke
- Motivate me
- What time is it?
- Bye

## Learning Outcomes

- Understanding rule-based chatbot development
- Implementing multi-intent recognition
- Using regular expressions for keyword matching
- Loading FAQ information from JSON
- Creating modular Python functions
- Handling user input and unexpected queries
- Developing an interactive terminal application

## Internship

Developed as **Task 4** of the Datheon Python Programming Internship.

## Author

Janhvi Dalavi