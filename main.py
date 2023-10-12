import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random



# def weather(query):

chatstr = ""
def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr = f"saurabh_sharma: {query}\n carlo: "

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chatstr,
        temperature=0.7,
        max_tokens=256,
    )

    assistant_response = response.choices[0].text.strip()
    print(assistant_response)
    say(assistant_response)
    chatstr += f"{assistant_response}\n"
    return assistant_response

    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    #
    # with open(f"Openai/{''.join(message.split('intelligence')[1:])}-{random.randint(1, 6572853)}.txt", "w") as f:
    #     f.write(text)


def ai(message):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {message}\n####################################\n\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=256,
    )

    assistant_response = response.choices[0].text.strip()
    print(assistant_response)
    text += assistant_response

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(message.split('intelligence')[1:])}-{random.randint(1, 6572853)}.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognising....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            return query
        except Exception as e:
            print("Recognition error:", e)
            return "I am sorry please repeat."


if __name__ == '__main__':
    print('WELCOME')
    say("Hello I am Carlo, how may I help you")
    while True:
        print("listening....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ['wikipedia', 'https://www.wikipedia.org/'],
                 ['microsoft', 'https://www.microsoft.com/en-in'],
                 ['github', 'https://github.com/'], ['google', 'https://www.google.com/'],
                 ['linkedin', 'https://in.linkedin.com/']]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]}, sir...")
                webbrowser.open(site[1])
        if "music" in query.lower():
            musicPath = "/Users/gauravsharma/downloads/tvari-hawaii-vacation-159069.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        elif "open" in query.lower():
            app_name = query.lower().replace("open", "").strip()
            os.system(f"open -a '{app_name}.app'")

        elif "using artificial intelligence" in query.lower():
            ai(message=query)

        if any(keyword in query.lower() for keyword in ["bye", "quit", "exit", "goodbye"]):

            say("Bye, sir")



            break


        else:
            chat(query)

