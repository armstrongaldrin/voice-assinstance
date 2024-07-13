
import smtplib
import pyttsx3

import speech_recognition as recon


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

def send_email(sender_email,sender_password,recipient_email,subject, content):
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['From'] =  sender_email
    msg['To'] = recipient_email
    msg['subject'] = subject
    msg.set_content(content)

    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(sender_email,sender_password)
        server.send_message(msg)

    print("Email sent succesfully")
    talk("Email sent succesfully")

recipient_mapping = {
    "personal" : "bnadish1@gmail.com",
    "akash" : "nadishb@karunya.edu.in"
    #continue


    }

sender_email = "bnadish1@gmail.com"
sender_password = "tyodwmjizawdqayp"


