
response = {
    "hello": "Hi there.",
    "how are you": "I'm fine.",
    "bye": "Goodbye!",
    "thanks": "You're welcome!"
}

while True:
    user = input("Enter the prompt: ").lower()

    if user in response:
        print(response[user])

        if user == "bye":
            break
    else:
        print("I didn't get that.")
      


