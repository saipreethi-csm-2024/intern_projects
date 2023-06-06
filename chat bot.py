import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Create a chatbot using the nltk library
pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot",]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it",]
    ],
    [
        r"quit|Bye",
        ["Bye! Take care.", "Goodbye!"]
    ],
     [
        r"what do you mean by AI?",
        ["AI stands for Artificial Intelligence.AI is a field of computer science that focuses on creating machines that can perform tasks that would require human intelligence to complete."]
    ],
     [
        r"Hey",
        ["Hey!What's up?","Hey!How can I help you?"]
    ],
]

chatbot = Chat(pairs, reflections)

# Function to get the chatbot's response
def get_bot_response(message):
    return chatbot.respond(message)

# Create the GUI
def send_message(event=None):
    message = user_input.get()
    if message.strip() == "":
        return
    chat_window.configure(state="normal")
    chat_window.insert(tk.END, "You: " + message + "\n")
    chat_window.configure(state="disabled")
    chat_window.yview(tk.END)
    
    bot_response = get_bot_response(message)
    chat_window.configure(state="normal")
    chat_window.insert(tk.END, "ChatBot: " + bot_response + "\n")
    chat_window.configure(state="disabled")
    chat_window.yview(tk.END)
    
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("ChatBot")

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, state="disabled", height=20, width=50,bg="cyan")
chat_window.grid(row=0, column=0, padx=10, pady=10)

# Create the user input field
user_input = tk.Entry(root, width=50)
user_input.grid(row=1, column=0, padx=10, pady=10)
user_input.bind("<Return>", send_message)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()