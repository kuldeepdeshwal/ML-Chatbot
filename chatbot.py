import nltk
import re
from nltk.chat.util import Chat, reflections
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
import random

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'Howdy!']),
    (r'how are you?', ['I\'m good, thank you!', 'I\'m doing well, thanks for asking. How about you?', 'Fantastic! How are you?']),
    (r'what is your name?', ['You can call me Jarvis.', 'I go by the name Jarvis.', 'Jarvis at your service!']),
    (r'(.*) your name?', ['You can call me Jarvis.', 'I go by the name Jarvis.', 'I am known as Jarvis.']),
    (r'good morning|good afternoon|good evening', ['Good morning!', 'Good afternoon!', 'Good evening!', 'Hope you are having a wonderful day!']),
    (r'goodbye|bye|see you later', ['Goodbye!', 'See you later!', 'Have a great day!', 'Take care!']),
    (r'introduce yourself', ['I\'m Jarvis, nice to meet you!', 'Hi, I\'m Jarvis.', 'Greetings! I am Jarvis, your friendly assistant.']),
    (r'what time is it?', ['I don\'t have access to real-time information, but you can check your device for the current time.', 'Unfortunately, I can\'t provide real-time information.']),
    (r'what day is it?', ['I don\'t have access to real-time information, but you can check your device for the current day.', 'I\'m not able to provide real-time information at the moment.']),
    (r'what is the date?', ['I don\'t have access to real-time information, but you can check your device for the current date.', 'I can\'t provide real-time information, sorry!']),
    (r'tell me a joke', ['Why was the math book sad? Because it had too many problems.', 'Why did the computer go to the doctor? It had a virus!', 'Why don\'t programmers like nature? It has too many bugs.']),
    (r'how is the weather', ['I don\'t have access to real-time weather information, but you can check your device for the current weather.', 'I\'m not able to provide real-time weather information.']),
    (r'do you like (.*)', ['I\'m just a language model, I don\'t have personal preferences.', 'I don\'t have feelings or emotions, but I can tell you about the topic.']),
    (r'what is a design pattern?', ['A design pattern is a repeatable and optimized solution approach frequently used in the software development process.', 'It offers solutions to problems encountered during the software development process.']),
    (r'types of design patterns', ['There are three types of design patterns: Creational, Structural, and Behavioral.', 'Creational patterns address problems related to the creation of objects, Structural patterns organize the relationships between objects, and Behavioral patterns regulate the behavior and interactions of objects.']),
    (r'example of creational design pattern', ['The Singleton pattern is an example of a Creational design pattern.', 'It ensures that only one instance of a class is created.']),
    (r'example of structural design pattern', ['The Adapter pattern is an example of a Structural design pattern.', 'It allows two incompatible objects to work together.']),
    (r'example of behavioral design pattern', ['The Observer pattern is an example of a Behavioral design pattern.', 'It defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.']),
    (r'what is machine learning?', ['Machine learning is a subset of artificial intelligence that involves training models on data to make predictions or take actions.', 'It\'s a way to enable computers to learn from experience and improve their performance over time.']),
    (r'what is natural language processing?', ['Natural language processing is a field of study focused on the interaction between computers and human language.', 'It involves developing algorithms and models that can understand, interpret, and generate human language.']),
    (r'what is deep learning?', ['Deep learning is a subset of machine learning that involves using neural networks to analyze and interpret data.', 'It\'s a way to enable computers to learn complex patterns and relationships in data.']),
    (r'how are you doing today?', ['I\'m doing well, thanks for asking!', 'I\'m just a language model, I don\'t have feelings or emotions, but I\'m here to help you!']),
    (r'what do you like to do?', ['I\'m just a language model, I don\'t have personal preferences, but I love assisting you!', 'I can assist with a wide range of tasks, from answering questions to generating text.']),
    (r'tell me a story', ['Once upon a time, there was a language model named Jarvis...', 'I can generate a story for you, but it might not be as interesting as a human-written one.']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Training data for the ML model
train_data = [
    ('What is machine learning?', 'Machine learning is a subset of artificial intelligence...'),
    ('What is natural language processing?', 'Natural language processing is a field of study focused on...'),
    ('What is deep learning?', 'Deep learning is a subset of machine learning that involves...'),
    #... (more training data)
]

# Vectorizer and model pipeline
pipeline = make_pipeline(CountVectorizer(), MultinomialNB())
X_train = [x[0] for x in train_data]
y_train = [x[1] for x in train_data]
pipeline.fit(X_train, y_train)

# Function to generate a response
def respond(user_input):
    if any(re.search(pattern[0], user_input, re.IGNORECASE) for pattern in patterns):
        return chatbot.respond(user_input)
    else:
        vectorized_input = [user_input]
        predicted_response = pipeline.predict(vectorized_input)
        return predicted_response[0]

# Start the conversation
print("Hello! I'm Jarvis. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
        print("Jarvis: Goodbye! Have a great day!")
        break
    response = respond(user_input)
    print("Jarvis:", response)
