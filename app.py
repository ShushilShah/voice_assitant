import speech_recognition as sr
from flask import Flask, render_template, request
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
    terminate = False
    while not terminate:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)

            if query.lower() == "Kill":
                print("Process terminated. Have a nice day")
                terminate = True
                continue

            response = generate_response(query)
            print("Assistant:", response)

        # Generate a response based on the voice input

        # Implement voice output using the text-to-speech engine
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

# Generate a response based on the user query


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
