import speech_recognition as sr
import pyttsx3
import datetime
import time

class Alarm:

    def __init__(self):
        self.agent = pyttsx3.init()
        self.r = sr.Recognizer()

    def speak(self, text):
        self.agent.getProperty('voices')
        self.agent.setProperty('rate', 175)
        self.agent.say(text)
        self.agent.runAndWait()
    def userSpeech(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.r.adjust_for_ambient_noise(source)
            self.r.pause_threshold = 1
            self.r.energy_threshold = 100
            audio = self.r.listen(source)

            try:
                print("Recognizing...")
                text = self.r.recognize_google(audio)
                audio_bytes = audio.get_wav_data()
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                return None
            except sr.RequestError as e:
                print(f"Request error: {e}")
                return None


    # Function to set alarm
    def setAlarm(self):
        self.speak("What time would you like to set the alarm for?")
        alarm_time = self.userSpeech()

        if alarm_time:
            try:
                alarm_time_obj = datetime.datetime.strptime(alarm_time, "%I:%M %p")
                current_time = datetime.datetime.now()
                while current_time < alarm_time_obj:
                    current_time = datetime.datetime.now()
                    time.sleep(1)
                print("Time's up! Wake up!")
                self.speak("Time's up! Wake up!")
            except ValueError:
                print("Sorry, I didn't understand the time format.")
                self.speak("Sorry, I didn't understand the time format.")


# Check the above code by this demo model of our alarm
# Note: IT IS NOT THE FINAL VERSION OF THE FUNCTION UPDATES TO BE BRING IN FUTURE:
alarm = Alarm()
if __name__ == "__main__":
    print("Hello! I am your Alarm assistant!")
    alarm.speak("Hello! I am your Alarm assistant")

    while True:
        print("\nSay 'Set Alarm' to set the alarm, or say 'Exit' to quit!")
        alarm.speak("Say 'Set Alarm' to set the alarm, or say 'Exit' to quit!")
        user_input = alarm.userSpeech()

        if user_input:
            if "set alarm" in user_input:
                alarm.setAlarm()
            elif "exit" in user_input:
                print('\nGoodBye!')
                alarm.speak("Goodbye!")
                break
            else:
                print("\nSorry, I didn't understand that command.")
                alarm.speak("Sorry, I didn't understand that command.")

