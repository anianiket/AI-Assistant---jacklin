import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import requests
import subprocess
import pyautogui
import random
from selenium import webdriver
import bs4
from playsound import playsound
from googletrans import Translator
from gtts import gTTS

print("Initializing Jacklin")
master = "sir"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):  # this function will speak the given text
    engine.say(text)
    engine.runAndWait()


def wishMe():  # This function will wish you as per the time
    hour = datetime.datetime.now().hour
    print(time.ctime())

    if hour >= 0 and hour < 12:
        speak("good morning..." + master + "..." + "how may i help you...")
    elif hour >= 12 and hour < 18:
        speak("good afternoon..." + master + "..." + "how may i help you...")
    else:
        speak("good evening..." + master + "..." + "how may i help you...")


# this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("listening_2.mp3")
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        query = query.lower().strip()

    except Exception as e:
        playsound("error.mp3")
        print("Say that again please\n")
        query = "None"

    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Testcase0000001@gmail.com', 'Test@0987654321')
    server.sendmail("Testcase0000001@gmail.com", to, content)
    server.close()


remind_speech = []  # this will save the reminder as texts


def main_fun(query):
    if query == "None":
        pass

    elif 'wikipedia' in query:
        playsound("recognizing.mp3")
        speak("searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        playsound("recognizing.mp3")
        url = "youtube.com"
        chrome_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif 'google' in query:
        playsound("recognizing.mp3")
        url = "google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query:
        playsound("recognizing.mp3")
        songs_dir = "C:\\Users\\suman\\Downloads\\music"
        songs = os.listdir(songs_dir)
        print(songs)
        length = len(songs)
        os.startfile(os.path.join(songs_dir, songs[random.randrange(0, length - 1)]))

    elif 'the time' in query:
        playsound("recognizing.mp3")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{master} the time is {strTime}")
        speak(f"{master} the time is {strTime}")

    elif 'open code' in query:
        playsound("recognizing.mp3")
        code_path = "C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
        subprocess.Popen(code_path)
        speak("opening dev c++")

    elif 'email to' in query:
        playsound("recognizing.mp3")
        try:
            speak("what should i send")
            message = takeCommand()
            content = "Subject: {}\n\n{}".format(datetime.datetime.now(), message)
            to = "sumantnetflix2000@gmail.com"
            sendmail(to, content)
            speak("email sent succesfully")
        except:
            speak("some error occured!")

    elif "weather in" in query:
        playsound("recognizing.mp3")
        api_key = "b5e6bdcb22ca5e0201127e4df05fe6a3"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = query.lower().split()[-1]
        print(city_name)
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        print(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
            speak(
                f"The temperature in {city_name} is {current_temperature}, humidity is {current_humidiy} and atmospheric pressure is {current_pressure}")
            time.sleep(5)
        else:
            print(" City Not Found ")

    elif 'search' in query:
        playsound("recognizing.mp3")
        speak("what do you want to search for?")
        search = takeCommand()
        try:
            url = 'https://www.google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Here is what i found for' + search)
        except:
            print("error\n")

    elif 'find location' in query:
        playsound("recognizing.mp3")
        speak("what is the location?")
        location = takeCommand()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
        speak('Here is your location:' + location)

    elif 'search in youtube' in query:
        playsound("recognizing.mp3")
        speak("what do you want to search for?")
        search = takeCommand()
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get('https://youtube.com')
        searchbox = driver.find_element_by_xpath('//*[@id="search"]')
        searchbox.send_keys(search)
        searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        searchbutton.click()

    elif 'desktop apps' in query:
        playsound("recognizing.mp3")
        speak("which app you want to open?")
        app = takeCommand()
        if 'calculator' in app:
            subprocess.Popen("calc.exe")
            speak("Opened!")

        elif 'notepad' in app:
            subprocess.Popen("notepad.exe")
            speak("Opened!")

        elif 'task manager' in app:
            subprocess.Popen("taskmgr.exe")
            speak("Opened!")

        elif 'control panel' in app:
            subprocess.Popen("control.exe")
            speak("Opened!")

        else:
            speak("not found what you are looking for!")

    elif 'calculate' in query:
        playsound("recognizing.mp3")
        speak("what do you want to calculate?")
        exp = takeCommand()
        opr = str(exp).split(" ")[1]

        if opr == '+' or opr == 'plus' or opr == 'add':
            ans = int(exp.split(" ")[0]) + int(exp.split(" ")[2])
            print(ans)
            speak(ans)
        elif opr == '-' or opr == 'minus' or opr == 'subtract':
            ans = int(exp.split(" ")[0]) - int(exp.split(" ")[2])
            print(ans)
            speak(ans)
        elif opr == '*' or opr == 'multiply' or opr == 'into':
            ans = int(exp.split(" ")[0]) * int(exp.split(" ")[2])
            print(ans)
            speak(ans)
        elif opr == '/' or opr == 'divide' or opr == 'by':
            ans = int(exp.split(" ")[0]) / int(exp.split(" ")[2])
            print(ans)
            speak(ans)
        else:
            speak("Wrong Operator")

    elif 'set reminder' in query:
        playsound("recognizing.mp3")
        speak("what you want me to remind?")
        remind_speech.append(takeCommand())
        speak("alright i will remind you!")

    elif 'tell reminder' in query:
        playsound("recognizing.mp3")
        if len(remind_speech) > 0:
            speak("here's your reminder!")
            for i in remind_speech:
                print(i, sep="  ", end="")
                speak(i)
            print()
        else:
            speak("you have no reminder")

    elif 'write in notepad' in query:
        playsound("recognizing.mp3")
        speak("what you want me to write")
        text = takeCommand()
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, 'w') as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])
        speak("done sir")

    elif 'scroll down' in query:
        playsound("recognizing.mp3")
        pyautogui.scroll(-200)

    elif 'scroll up' in query:
        playsound("recognizing.mp3")
        pyautogui.scroll(200)

    elif 'click now' in query:
        playsound("recognizing.mp3")
        pyautogui.click()

    elif 'move right' in query:
        playsound("recognizing.mp3")
        pyautogui.moveRel(50, 0, duration=0.2)

    elif 'move left' in query:
        playsound("recognizing.mp3")
        pyautogui.moveRel(-50, 0, duration=0.2)

    elif 'move up' in query:
        playsound("recognizing.mp3")
        pyautogui.moveRel(0, -50, duration=0.2)

    elif 'move down' in query:
        playsound("recognizing.mp3")
        pyautogui.moveRel(0, 50, duration=0.2)

    elif 'take screenshot' in query:
        playsound("recognizing.mp3")
        img = pyautogui.screenshot()
        date = datetime.datetime.now()
        save_path = "img-" + str(date).replace(":", "-") + ".png"
        img.save(save_path)
        speak("done")

    elif 'double click' in query:
        playsound("recognizing.mp3")
        pyautogui.doubleClick()

    elif 'open website' in query:
        playsound("recognizing.mp3")
        search = query.lower().replace('open website ', "")
        url = "https://www." + search
        webbrowser.open(url)

    elif 'coronavirus cases' in query:
        playsound("recognizing.mp3")
        r = requests.get("https://www.worldometers.info/coronavirus/country/india/")
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        val = []
        for d in soup.find_all('div', class_="maincounter-number"):
            val.append(d.find('span').text)

        print("total cases: ", val[0])
        speak(f"total cases are {val[0]}")

        print("Deaths: ", val[1])
        speak(f"deaths are {val[1]}")

        print("Recovered: ", val[2])
        speak(f"recovered are {val[2]}")

    elif 'news' in query:
        playsound("recognizing.mp3")
        page = requests.get("https://timesofindia.indiatimes.com/us")
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        i = 0
        for a in soup.find_all("figcaption"):
            if i == 10:
                break
            else:
                print(a.text)
                speak(a.text)
                print()
                i = i + 1

    elif 'translate' in query:
        playsound("recognizing.mp3")
        dict_lang = {'hindi': 'hi', 'kannada': 'kn', 'tamil': 'ta', 'telugu': 'te', 'gujarati': 'gu', 'marathi': 'mr'}
        speak("what you want me to translate?")
        sentence = takeCommand()
        speak("In which language you want me to translate?")
        lang = takeCommand().lower()
        if dict_lang.get(lang, 0):
            print("translating:", sentence)
            speak(f"translating {sentence}")
            translator = Translator()
            result = translator.translate(sentence, src="en", dest=dict_lang.get(lang))
            print(result.text)
            hindi = result.text
            obj = gTTS(text=hindi, slow=False, lang=dict_lang.get(lang, 'hi'))
            obj.save('hindi.mp3')
            playsound('hindi.mp3')
        else:
            speak("sorry..I dont know that language.")

    elif 'play in youtube' in query:
        playsound("recognizing.mp3")
        speak("what you want me to play from youtube?")
        search = takeCommand()
        search = search.strip().replace(" ", "+")
        api_key = "AIzaSyDAeBfUvjZZsc4Wx52CkvNjFLO_ps3Wgm8"
        from googleapiclient.discovery import build
        youtube = build('youtube', 'v3', developerKey=api_key)
        type(youtube)
        req = youtube.search().list(q=search, part='snippet', type='video', maxResults=1)
        res = req.execute()
        id = res['items'][0]['id']['videoId']
        webbrowser.open("http://www.youtube.com/watch?v=" + id)


    elif 'coding' in query:
        playsound("recognizing.mp3")
        keys = {'enter': '\n', 'space': ' ', 'round bracket': '(', 'curly bracket': '{', 'square bracket': '[',
                'backspace': 'backspace', 'down': 'down', 'up': 'up',
                'left': 'left', 'right': 'right', 'inverted,': '"', 'single,': ',', ',': ',', 'colon': ':',
                'semi colon': ';',
                'comment': '#', 'not': '!', 'plus': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.py"
        print(file_name)
        while True:
            with open(file_name, 'w') as f:
                subprocess.Popen(["C:\\Users\\suman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", file_name])
            query = takeCommand()
            if 'press' in query:
                playsound("recognizing.mp3")
                query = query.replace("press ", "")
                if query in keys:
                    pyautogui.press(keys.get(query))
                else:
                    pyautogui.typewrite('press ' + query)

            elif 'type' in query:
                playsound("recognizing.mp3")
                query = query.replace('type ', "")
                pyautogui.typewrite(query)

            elif 'format' in query:
                playsound("recognizing.mp3")
                pyautogui.hotkey('shift', 'alt', 'f')

            elif 'save' in query:
                playsound("recognizing.mp3")
                pyautogui.hotkey('ctrl', 's')

            elif 'run' in query:
                playsound("recognizing.mp3")
                pyautogui.hotkey('ctrl', 'c')
                run_button = pyautogui.locateOnScreen('run_photo.png')
                location = pyautogui.center(run_button)
                if not pyautogui.click(location):
                    print("run successfull")
                else:
                    print("error")

            elif 'scroll down' in query:
                playsound("recognizing.mp3")
                pyautogui.scroll(-200)

            elif 'scroll up' in query:
                playsound("recognizing.mp3")
                pyautogui.scroll(200)

            elif 'click now' in query:
                playsound("recognizing.mp3")
                pyautogui.click()

            elif 'move right' in query:
                playsound("recognizing.mp3")
                pyautogui.moveRel(50, 0, duration=0.2)

            elif 'move left' in query:
                playsound("recognizing.mp3")
                pyautogui.moveRel(-50, 0, duration=0.2)

            elif 'move up' in query:
                playsound("recognizing.mp3")
                pyautogui.moveRel(0, -50, duration=0.2)

            elif 'move down' in query:
                playsound("recognizing.mp3")
                pyautogui.moveRel(0, 50, duration=0.2)

            elif 'quit' in query:
                playsound("recogizing.mp3")
                cut_button = pyautogui.locateOnScreen('cut_code.png')
                location = pyautogui.center(cut_button)
                if not pyautogui.click(location):
                    print("quit successfull")
                else:
                    print("error")
                    playsound("error.mp3")
                break

    elif 'close current window' in query:
        playsound("recogizing.mp3")
        pyautogui.hotkey('ctrl','alt','f4')

    elif 'close current tab' in query:
        playsound("recogizing.mp3")
        pyautogui.hotkey('ctrl','w')

    elif 'move to another window' in query:
        playsound("recogizing.mp3")
        pass

    elif 'who are you' in query:
        playsound("recognizing.mp3")
        speak("I am jacklin.. built to serve humanity!")

    else:
        playsound("error.mp3")
        speak("I didn't get that one")


def checkInternet():
    url = "https://www.facebook.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


# main program starts here..
if __name__ == "__main__":
    speak("Initializing Jacklin.")
    wishMe()
    if checkInternet():
        while True:
            query = takeCommand()
            if "ok jack" in query:
                playsound("listening.mp3")
                while True:
                    query = takeCommand()
                    if 'quit' in query:
                        speak("bye sir")
                        break
                    else:
                        try:
                            main_fun(query)
                        except:
                            playsound("error.mp3")
                            print("error\n")
                            speak("error")
    else:
        print("No internet connection!")
        speak("No internet connection!")
