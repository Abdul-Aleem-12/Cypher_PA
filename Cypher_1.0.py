import pyttsx3
import speech_recognition as sr
import pyautogui
import pywhatkit
import datetime
import os
import pyjokes
import webbrowser
import time
import re
import keyboard



def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print("CYPHER:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=100)  # Increased timeout
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network issue. Please check your connection.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning!"
    elif hour < 18:
        greeting  = "Good afternoon!"
    else:
        greeting = "Good evening!"
    message = f"Welcome back Abdul! {greeting} I am cypher. How can I help you today?"
    speak(message)
e
def open_chrome_and_search(query):
    speak(f"Searching for {query}")
    pywhatkit.search(query)

def play_on_youtube(song):
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def tell_date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {today}")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def open_website(site):
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "chrome": "https://www.google.com"  # Handle "open chrome"
    }
    if site in urls:
        speak(f"Opening {site}")
        webbrowser.open(urls[site])
    else:
        speak(f"I don't recognize {site} as a website, but I can search it.")
        pywhatkit.search(site)
def search_linkedin_profile(name):
    search_query = f"{name} srm site:linkedin.com"
    speak(f"Searching profile")
    pywhatkit.search(search_query)
    time.sleep(3)  # Wait for search results to load

def search_scholar_profile(name):
    search_query = f"{name} AND assistant professor srm site:scholar.google.com"
    speak(f"Searching profile")
    pywhatkit.search(search_query)
    time.sleep(3)  # Wait for search results to load

    # Click first link - Coordinates depend on your screen
    pyautogui.moveTo(292, 396)  # Adjust based on browser search result position
    pyautogui.click()
    speak("Here is the Google Scholar profile I found.")

def automate_chrome():
    speak("Automating Chrome")
    pyautogui.hotkey('win', 'd')
    time.sleep(1)
    pyautogui.moveTo(300, 950)  # Adjust as needed for your screen
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.write('https://www.google.com')
    pyautogui.press('enter')

def cypher():
    wish_user()
    while True:
        
        # command = input("Enter query : ")
        command = take_command()
        if not command:
            continue
        if command == "exit":
            break
        elif "change tab" in command:
            match = re.search(r"tab (to )?(\d+)", command)
            if match:
                tab_number = int(match.group(2))
                if 1 <= tab_number <= 9:
                    pyautogui.hotkey('ctrl', str(tab_number))
                    speak(f"Switched to tab {tab_number}")
                else:
                    speak("I can only switch to tabs 1 through 9.")
            else:
                speak("Please specify a tab number to switch to.")

        elif "search" in command and "linkedin" in command:
            query = re.sub(r"(search|linkedin)", "", command, flags=re.IGNORECASE).strip()
            print(query)
            search_linkedin_profile(query)
        elif "search" in command and ("scholar" in command or "sir" in command or "mam" in command):
            query = re.sub(r"(search|scholar|sir|mam)", "", command, flags=re.IGNORECASE).strip()
            print(query)
            search_scholar_profile(query)
        elif "search" in command:
            query = command.replace("search", "").replace("linkedin","").strip()
            open_chrome_and_search(query)
        elif "close" in command and "tab" in command:
            pyautogui.hotkey('ctrl', 'w')
            speak("Closed the current tab.")

        elif "close window" in command or "exit window" in command:
            pyautogui.hotkey('alt', 'f4')
            speak("Closed the window.")

        elif "play" in command:
            song = command.replace("play", "").strip()
            play_on_youtube(song)

        elif "time" in command or "what time" in command:
            tell_time()

        elif "date" in command or "year" in command or "day" in command:
            tell_date()

        elif "joke" in command:
            tell_joke()

        elif "open" in command:
            site = command.replace("open", "").strip()
            open_website(site)

        elif "chrome automation" in command or "automate chrome" in command:
            automate_chrome()

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye Abdul! Take care.")
            break
        
        else:
            speak("I can search that for you.")
            pywhatkit.search(command)

if __name__ == "__main__":
    cypher()