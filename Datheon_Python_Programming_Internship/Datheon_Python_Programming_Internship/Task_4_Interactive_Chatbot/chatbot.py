
import datetime
import json
import random
import re


FAQ_FILE = "sample_faq.json"


def load_faqs():
    """Load greetings and FAQs from the JSON dataset."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("greetings", []), data.get("faqs", [])

    except FileNotFoundError:
        print("Warning: FAQ dataset not found.")
        return [], []

    except json.JSONDecodeError:
        print("Warning: FAQ dataset contains invalid JSON.")
        return [], []


def normalize_input(user_input):
    """Normalize user input for matching."""
    return re.sub(r"\s+", " ", user_input.lower().strip())


def get_greeting():
    """Return a friendly greeting."""
    greetings = [
        "Hello!",
        "Hi there!",
        "Welcome!",
        "Hey there!"
    ]
    return random.choice(greetings)


def find_faq_response(message, faqs):
    """Find a matching FAQ using keywords and regular expressions."""

    message = normalize_input(message)

    for faq in faqs:
        question = faq.get("question", "").lower()
        answer = faq.get("answer", "")

        # Match important keywords from the FAQ question
        keywords = re.findall(r"\b[a-zA-Z]{4,}\b", question)

        matched_keywords = sum(
            1 for keyword in keywords if keyword in message
        )

        if matched_keywords >= 2:
            return answer

        # Match the full question when possible
        if question.rstrip("?") in message:
            return answer

    return None


def get_response(user_input, user_name, greetings, faqs):
    """Recognize user intent and return a suitable response."""

    message = normalize_input(user_input)

    # Exit intent
    if re.fullmatch(r"(bye|goodbye|exit|quit|stop)", message):
        return (
            "Thank you for chatting with us, {}! "
            "Have a wonderful day. Goodbye!".format(user_name),
            True
        )

    # Help intent
    if re.search(r"\b(help|commands|what can you do)\b", message):
        return (
            "Welcome to the Customer Support Assistant!\n"
            "You can ask me about:\n"
            "  • Business hours\n"
            "  • Internship project submission\n"
            "  • Certificate processing time\n"
            "  • Available FAQs\n"
            "  • General greetings\n"
            "  • Type 'bye' or 'exit' to end the chat",
            False
        )

    # Greeting intent
    if any(re.search(r"\b" + re.escape(greeting) + r"\b", message)
           for greeting in greetings):
        return (
            "{} {}! Welcome to our customer support assistant. "
            "How can I help you today?".format(get_greeting(), user_name),
            False
        )

    # Business hours intent
    if re.search(
        r"\b(hours|opening|closing|open|closed|working hours|business hours)\b",
        message
    ):
        response = find_faq_response(
            "hours of operation", faqs
        )
        if response:
            return response, False

    # Internship project submission intent
    if re.search(
        r"\b(submit|submission|upload|turn in)\b", message
    ) and re.search(
        r"\b(project|internship|github|repository|repo)\b", message
    ):
        response = find_faq_response(
            "submit internship project", faqs
        )
        if response:
            return response, False

    # Certificate intent
    if re.search(
        r"\b(certificate|certification|completion certificate)\b",
        message
    ):
        response = find_faq_response(
            "receive certificate", faqs
        )
        if response:
            return response, False

    # General FAQ matching
    faq_response = find_faq_response(message, faqs)
    if faq_response:
        return faq_response, False

    # Chatbot identity
    if re.search(r"\b(who are you|what are you|your name)\b", message):
        return (
            "I'm a rule-based customer support assistant developed "
            "using Python. I help answer common questions using "
            "keywords, regular expressions, and an FAQ dataset.",
            False
        )

    # Time and date
    if re.search(r"\b(time|current time)\b", message):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return "The current time is {}.".format(current_time), False

    if re.search(r"\b(date|today|today's date)\b", message):
        current_date = datetime.datetime.now().strftime(
            "%A, %d %B %Y"
        )
        return "Today is {}.".format(current_date), False

    # Joke intent
    if re.search(r"\b(joke|funny|laugh)\b", message):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "Why was the Python programmer confused? Because they couldn't C!"
        ]
        return random.choice(jokes), False

    # Motivation intent
    if re.search(r"\b(motivate|motivation|inspire)\b", message):
        quotes = [
            "Believe in yourself. Every small step brings you closer to your goal!",
            "Mistakes are proof that you are learning. Keep going!",
            "Great things take time. Trust your journey!"
        ]
        return random.choice(quotes), False

    # Thank-you intent
    if re.search(r"\b(thank you|thanks)\b", message):
        return "You're welcome, {}! I'm happy to help.".format(user_name), False

    # Casual conversation
    if re.search(r"\b(how are you|how are you doing)\b", message):
        return "I'm doing well and ready to help! How are you?", False

    if re.search(r"\b(i am|i'm|im)\b", message):
        return "Nice to know! How can I assist you today?", False

    # Fallback response
    fallback_responses = [
        "I'm sorry, I couldn't find an answer to that. "
        "Please try asking in a different way.",
        "I don't have information about that yet. "
        "Type 'help' to see what I can assist with.",
        "Could you please rephrase your question?"
    ]

    return random.choice(fallback_responses), False


def main():
    """Start the interactive customer support chatbot."""

    greetings, faqs = load_faqs()

    print("=" * 55)
    print("       DATHEON CUSTOMER SUPPORT CHATBOT")
    print("=" * 55)

    user_name = input("Welcome! What should I call you? ").strip()

    if not user_name:
        user_name = "Friend"

    user_name = user_name.title()

    print("\n{} {}!".format(get_greeting(), user_name))
    print("I'm here to help with your questions.")
    print("Type 'help' to view available features.")
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("{}: ".format(user_name)).strip()

            if not user_input:
                print("Assistant: Please enter a question.\n")
                continue

            response, should_exit = get_response(
                user_input, user_name, greetings, faqs
            )

            print("Assistant: {}\n".format(response))

            if should_exit:
                break

        except KeyboardInterrupt:
            print(
                "\nAssistant: Goodbye, {}! "
                "Thank you for chatting with us.".format(user_name)
            )
            break


if __name__ == "__main__":
    main()
