# girlfriend_chatbot.py

import random

# Predefined responses
greetings = ["Hey babe! 😘", "Hi honey! ❤️", "Hello cutie! 🥰"]
how_are_you = ["I'm great, thinking about you! 💕", "Feeling awesome! How about you?", "I'm good, miss you! 😘"]
compliments = ["You're amazing 😍", "I love your smile 😊", "You are my favorite person ❤️"]
goodbyes = ["Bye love! 😘", "Talk soon, cutie! ❤️", "Missing you already 😢"]

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(greetings)
    elif "how are you" in user_input:
        return random.choice(how_are_you)
    elif any(word in user_input for word in ["love me", "i love you", "miss me"]):
        return random.choice(compliments)
    elif any(word in user_input for word in ["bye", "see you", "good night"]):
        return random.choice(goodbyes)
    else:
        return "Aww, tell me more 😘"

def main():
    print("💖 Girlfriend Chatbot 💖")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Bye cutie! 😘")
            break
        
        response = chatbot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
