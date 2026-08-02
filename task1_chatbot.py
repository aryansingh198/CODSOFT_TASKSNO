"""
CODSOFT - Artificial Intelligence Internship
TASK 1: CHATBOT WITH RULE-BASED RESPONSES

A simple rule-based chatbot that uses pattern matching (if-else / keyword
matching) to understand user input and respond accordingly. This is a
classic introduction to NLP and conversation flow, without any ML model.
"""

import re
import random
from datetime import datetime


class RuleBasedChatbot:
    def __init__(self, name="CodBot"):
        self.name = name
        # Each rule = (regex pattern, list of possible responses)
        self.rules = [
            (r"\b(hi|hello|hey|hola)\b", [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Good to see you."
            ]),
            (r"\bhow are you\b", [
                "I'm just a bunch of if-else statements, but I'm doing great!",
                "Running smoothly, thanks for asking!"
            ]),
            (r"\byour name\b", [
                f"I'm {self.name}, your friendly rule-based chatbot."
            ]),
            (r"\b(time)\b", [
                lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}."
            ]),
            (r"\b(date|today)\b", [
                lambda: f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."
            ]),
            (r"\b(bye|goodbye|exit|quit)\b", [
                "Goodbye! Have a great day!",
                "See you soon!"
            ]),
            (r"\b(thanks|thank you)\b", [
                "You're welcome!",
                "Anytime!"
            ]),
            (r"\b(help|what can you do)\b", [
                "I can chat about greetings, tell you the time/date, "
                "and respond to simple questions. Try asking me something!"
            ]),
            (r"\b(codsoft)\b", [
                "CodSoft is a tech education & software development platform "
                "offering virtual internships and AI-driven career tools."
            ]),
            (r"\b(weather)\b", [
                "I can't check live weather (no internet access), "
                "but I hope it's sunny where you are!"
            ]),
        ]

        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more.",
            "Hmm, I don't have a rule for that yet.",
            "Can you elaborate a bit more?"
        ]

    def get_response(self, user_input: str) -> str:
        text = user_input.lower().strip()

        for pattern, responses in self.rules:
            if re.search(pattern, text):
                choice = random.choice(responses)
                # Support responses that are callables (e.g. dynamic time/date)
                return choice() if callable(choice) else choice

        return random.choice(self.default_responses)

    def chat(self):
        print(f"{self.name}: Hi! I'm {self.name}. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if not user_input.strip():
                continue
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")
            if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
                break


if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.chat()
