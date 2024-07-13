import speech_recognition as recon
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests, json

apiKey = "3825af9e74068a9af623c519e82fe299"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="




 
listener = recon.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()




def input_instruction():
    global instruction
    try:
        with recon.Microphone() as origin:
            print("Listening")
            listener.adjust_for_ambient_noise(origin,duration=1)
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "dax" in instruction:
                instruction = instruction.replace('dax', " ")
                print(instruction)
    
    except:
        pass
    return instruction
def play_dex():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        songs = instruction.replace('play',"")
        talk("playing"+ songs)
        pywhatkit.playonyt(songs)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk("Current time"+time)
        print(time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Todays Date"+date)

    elif "what is my name" in instruction:
        name = "Nadish"
        talk(name)
        print(name)
    elif "what is your name" in instruction:
        talk("I am dex, How can I help you?")
    elif "what's your name" in instruction:
        talk("I am dex, How can I help you?")
    elif "husband" in instruction:
        talk("akash")
        print("akash")
    elif "who is " in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        talk(info)
        print(info)
    elif "hello" in instruction:

        
        talk("hi I am dex, how can I help you")
        print("hi I am dex, how can I help you")
    elif "send email" in instruction:
            print("To whom do I send the email")
            talk("To whom do I send the email")

            recipient_name = input_instruction().lower()
            from sendemail import recipient_mapping
            recipient_email = recipient_mapping.get(recipient_name)

            if recipient_email:
                print("what is the subject of email ")
                talk("what is the subject of email ")

                subject = input_instruction().lower()
                from sendemail import send_email
                from sendemail import sender_email
                from sendemail import sender_password

                print("what is the message")
                talk("what is the message")

                content = input_instruction().lower()

                send_email(sender_email, sender_password, recipient_email,subject,content)

            else:
                print("Sorry I am not able to send email")
                talk("Sorry I am not able to send email")
    elif "youtube" in instruction:
        talk("opening youtube")
        
        webbrowser.open("https://www.youtube.com/")
    
    elif "gmail" in instruction:
        talk("opening gmail")
        
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    
    elif "map" in instruction:
        talk("opening map")
        
        webbrowser.open("https://www.google.com/maps")

    elif "weather" in instruction:
        talk("Say your city")
        print("Say your city")
        city = input_instruction().lower()
        print(city)
        CompleteURL = baseURL + city + "&appid=" + apiKey
        response = requests.get(CompleteURL)

        data = response.json()

        print("Current Temperature:",data["main"]["temp"])
        print("Current Temperature feels like:",data["main"]["feels_like"])
        print("Maximun Temperature:",data["main"]["temp_max"])
        print("Minimun Temperature:",data["main"]["temp_min"])

       
    else:
        talk("please repeat")

play_dex()





