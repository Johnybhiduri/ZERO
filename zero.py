import speech_recognition as sr
import requests
import os
from dotenv import load_dotenv
import json
import pyttsx3
load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Zero:
    def __init__(self, wake_word, s2TModel = "openai/whisper-base", AIModel = "tiiuae/falcon-7b-instruct"):
        self.wake_word = wake_word
        self.hub_api_key = os.environ['HUB_API_KEY']
        self.s2TModel = s2TModel
        self.AIModel = AIModel

    def audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            recognizer.pause_threshold = 1
            recognizer.energy_threshold = 100
            audio = recognizer.listen(source)

        try:
            audio_bytes = audio.get_wav_data()
            return audio_bytes
        except sr.UnknownValueError:
            print('Sorry, I did not hear your request. Please try again.')
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print("Failed to record try again.")
            return None

    def speechToText(self, audio_bytes):
        headers = {"Authorization": f"Bearer {self.hub_api_key}"}
        API_URL = f"https://api-inference.huggingface.co/models/{self.s2TModel}"
        response = requests.request("POST", API_URL, headers=headers, data=audio_bytes)
        return json.loads(response.content.decode("utf-8"))['text']

    def virtualAssistant(self, text):
        api_url = f"https://api-inference.huggingface.co/models/{self.AIModel}"
        headers = {"Authorization": f"Bearer {self.hub_api_key}"}
        payload = {"inputs": text}
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()[0]["generated_text"][len(text) + 1 :]

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def start(self):
        quit = False
        while not quit:
            command = self.audio()
            if command:
                command_text = self.speechToText(command)
                print(command_text)
            if command_text and self.wake_word.lower() in command_text.lower():
                self.speak('Yes sir!')
                while True:
                    question = self.audio()
                    if question:
                        question_text = self.speechToText(question)
                        print("Question: ", question_text)
                        if "quit" in question_text.strip().lower():
                            quit = True
                            self.speak("Quitting Now!")
                            break
                        elif "sleep" in question_text.strip().lower():
                            self.speak("Sleeping Now!")
                            break
                        response = self.virtualAssistant(question_text)
                        print("Answer: ", response)
                        self.speak(response)
            
            elif command_text and "quit" in command_text.lower():
                self.speak("Quitting Now!")
                break
