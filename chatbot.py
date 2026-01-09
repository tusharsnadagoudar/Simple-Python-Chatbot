print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, type 'bye' to exit from bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate Me": "Keep Going. Every Bug of your project makes you the best",
}

# Method/Function to get respose of chatbot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. I will learn it soon"
        
# Take user input

while True:
    userInput= input("Please ask your Question:")
    reply= getResponseOfBot(userInput)
    print("Bot response: ", reply)

    if "bye" in userInput.lower():
        break