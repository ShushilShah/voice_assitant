import speech_recognition as sr
import pyttsx3
import datetime
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI
from dotenv import load_dotenv
# Set up the speech recognizer
recognizer = sr.Recognizer()

# Set up the text-to-speech engine
engine = pyttsx3.init()

engine.setProperty('rate', 105)

load_dotenv()
# connecting to sql database
db = SQLDatabase.from_uri("sqlite:///content.db")

# creating chain to interact with database
llm = OpenAI(temperature=0)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


# Implement voice input and processing

# engine.say("Hello!, My name is Talker.")
# engine.runAndWait()


def process_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)

        # Generate a response based on the voice input
        response = generate_response(query)
        print("Assistant:", response)

        # Implement voice output using the text-to-speech engine
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

# Generate a response based on the user query


# def generate_response(query):
#     predefined_responses = {
#         "hello": "Hello! How can I assist you?",
#         "name": "My name is talker",
#         "age": "Your age is 23 years",
#         "capital": "Kathmandu",
#         "datascience": " Data science is the study of data and its behavoir",
#         "weather": "The weather today is sunny.",
#         "time": "The current time which is  {}".format(datetime.datetime.now().strftime("%H:%M")),
#         # Add more queries and responses as needed
#     }

#     if query.lower() in predefined_responses:
#         return predefined_responses[query.lower()]
#     else:
#         return "I'm sorry, I don't have a response for that query."

def generate_response(query):
    result = handle_user_query(query)
    return result

# Handle user query and execute SQL queries on the database


def handle_user_query(query):
    try:
        result = db_chain.run(query)
        return result
    except Exception as e:
        print("Error:", str(e))
        return "I'm sorry, there was an error processing your query."


# Call the function to start processing voice input
process_voice_input()
