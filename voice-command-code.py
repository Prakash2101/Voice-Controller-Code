import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import smtplib
import pyaudio

NAME = "Prakash"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait( )
#speak("Prakash is good")   

def wishMe( ):
    hour= int(datetime.datetime.now().hour)
    print(hour)
    if hour >=0 and hour<12:
        speak("good morning"+NAME)
    elif hour>=12 and hour <18:
        speak("good afternoon"+NAME)
    else:
        speak("good evening"+NAME)
        
speak("Lappy Controller is ready for your help")

wishMe()
def takecommand( ):
    r = sr.Recognizer( )
    with sr.Microphone() as source:
        print("listening.....")
        audio = r.listen(source)
    
        try :
            print("Recognizing...")
            query = r.recognize_google(audio)
            print('user said: {}'.format(query))
        except Exception as e:
            print("say that again please")
            query = None
            if query == None:
                speak('sorry i can not find any task!! thakyou,goodday')
        return query
        
       

#query=takecommand()

while (True):
    #wishMe()
    query=takecommand()
    #time.sleep(0.5)
    if ('wikipedia') and ('open' or 'run')  in query.lower():
        speak("searching on wikipedia")
        query = query.replace("wikipedia"," ")
        results = wikipedia.summary(query, sentences =2)
        speak(results)
    
    elif('run chrome') in query.lower():
        speak("opening chrome browser")
        os.system("chrome")
    elif ('close chrome') in query.lower():
        speak("closing the chrome browser")
        os.system("taskkill /F /IM chrome.exe")
        
    elif ('open' or 'run') and  ('player') in query.lower():
        speak("media player is starting")
        os.system("start wmplayer")
    elif ('close mediaplayer') in query.lower():
        speak("closing the  mediaplayer")
        os.system("taskkill /F /IM wmplayer.exe")
        
    elif ('open' or 'run')and ('notepad') in query.lower():
         speak("notepad is opening")
         os.system("notepad")        
    elif ('close notepad') in query.lower():
        speak("notepad is closing")
        os.system("taskkill /F /IM notepad.exe")
        
    elif ('open' or 'run') and ('youtube') in query.lower():
        webbrowser.open("youtube.com")
    elif ('close youtube') in query.lower():
        speak("youtube is closing")
        os.system("taskkill /F /IM youtube.exe")
           
    elif ('open' or 'run') and(' music')  in query.lower():
        speak('just wait i will paly a song for you')
        sd="C:\\Users\\HP\\Music"
        songs = os.listdir(sd)
        os.startfile(os.path.join(sd, songs[0]))
    elif ('close music') in query.lower():
        speak("music player is closing")
        os.system("taskkill /F /IM Music.exe")
        
    elif ('open' or 'run') and (' task manager') in query.lower():
        speak('task manager is opening')
        os.system('taskmgr')
    elif ('close task manger') in query.lower():
        speak("task manager  is closing")
        os.system("taskkill /F / taskmgr.exe")    
    
    elif ('open' or 'run') and (' camera') in query.lower():
        speak('camera is opening')
        os.system('start microsoft.windows.camera:')
    elif ('close camera') in query.lower():
        speak("camera is closing")
        os.system("taskkill /F /IM Camera.exe")
    elif ' microsoftword'  or 'word' and 'Document' in query.lower():
        speak('microsoftword is opening')
        os.system('winword')
    elif ('open' or 'run') and ('Whatsapp') in query.lower():
        speak('whatsapp is opening')
        os.system( "start chrome   web.whatsapp.com")
    elif ('close whatsapp') in query.lower():
        speak("whatasapp is closing")
        os.system("taskkill /F /IM Whatsapp.exe")
        
    elif ('open' or 'run') and ('facebook') in query.lower():
        speak('facebook is opening')
        os.system("start chrome  facebook.com")
    elif ('close facebook') in query.lower():
        speak("faceook is closing")
        os.system("taskkill /F /IM  Facebook.exe")
        
    elif ( 'open' or 'run' ) and ('gmail') in query.lower():
        speak('googlemail is opening')
        os.system("start chrome  gmail.com")
    elif ('close gmail') in query.lower():
        speak("gmail is closing")
        os.system("taskkill /F /IM gmail.exe")
        
    elif ('open' or 'run') and ('espn') in query.lower():
        speak('espn is opening')
        os.system("chrome  espn.in")
    elif ('close espn') in query.lower():
        speak("espn is closing")
        os.system("taskkill /F /IM chrome.exe")
        
        
    elif ('open' or 'run') and (' github') in query.lower():
        speak('Github is opening')
        os.system("chrome  github.com")
    elif ('close github') in query.lower():
        speak("github is closing")
        os.system("taskkill /F /IM chrome.exe")
    
    elif ('open' or 'run') and ('mentor') in query.lower():
        speak('ok i tell you about your mentor via linkdin profile')
        os.system("chrome  https://www.linkedin.com/in/vimaldaga/")
    elif ('close mentor') in query.lower():
        speak("ok i wil close your mentor profile")
        os.system("taskkill /F /IM chrome.exe")
    
    
    elif ('open' or 'run') and (' iiec rise') in query.lower():
        speak('here is a informaton about indian innovation enterprenureship community')
        os.system("chrome  https://www.linkedin.com/company/indian-innovation-entrepreneurship-community/")
    elif ('close iiec rise') in query.lower():
        speak("ok i will close iiec rise ")
        os.system("taskkill /F /IM chrome.exe")
        
    elif('open' or 'run') and ('stackoverflow') in query.lower():
        speak('stackoverflow  is opening')
        os.system("chrome  stackoverflow.com")  
    elif ('close  stackoverflow') in query.lower():
        speak("stackoverflow is closing")
        os.system("taskkill /F /IM chrome.exe")  
        
    elif('open' or 'run') and (' gcp cloud') in query.lower():
        speak('gcp cloud  is opening')
        os.system("chrome  console.cloud.google.com")  
    elif ('close gcp cloud') in query.lower():
        speak("gcp cloud  is closing")
        os.system("taskkill /F /IM chrome.exe")  
    
    elif('open' or 'run') and  ('aws cloud') in query.lower():
        speak('aws cloud  is opening')
        os.system("chrome  aws.amazon.com")
    elif ('close  aws') in query.lower():
        speak("aws  is closing")
        os.system("taskkill /F /IM chrome.exe")  
        
    elif ('open' or 'run') and ('google drive') in query.lower():
        speak('google drive  is opening')
        os.system("chrome  drive.google.com")
    elif ('close  google drive') in query.lower():
        speak("google drive is closing")
        os.system("taskkill /F /IM chrome.exe")  
        
    elif 'paint' in query.lower():
        speak('opening paint')
        os.system("mspaint")
    elif ('close paint') in query.lower():
        speak("paint is closing")
        os.system("taskkill /F /IM Paint.exe")
        
    elif 'minikube' in query.lower():
        speak('minikube is opening')
        os.system("E:\\kubernets\\Minikube\\minikube.exe")
    elif ('close  minikube') in query.lower():
        speak("minikube is closing")
        os.system("taskkill /F /IM minikube.exe")
        
    elif 'calculator' in query.lower():
        speak('calculator is opening')
        os.system("calc")
    elif ('close calculator') in query.lower():
        speak("calculator is closing")
        os.system("taskkill /F /IM Calculator.exe")
    
    elif 'configuration' and ' commandprompt'  in query.lower():
        speak('command prompt configuration is opening')
        os.system("cliconfg")
    elif ('close  configuration commandprompt') in query.lower():
        speak("commandprompt configuration  is closing")
        os.system("taskkill /F /IM cliconfg.exe")
        
    elif 'open command prompt' in query.lower():
        speak('command prompt is opening')
        os.system("cmd")
    elif ('close   commandprompt') in query.lower():
        speak("commandprompt  is closing")
        os.system("taskkill /F /IM cmd.exe")
    
    
    elif 'ip address' or 'internet protocal' or 'ip' in query.lower():
        speak('wait i am finding your ip address')
        os.system("ipconfig")
    elif ('close ip address') in query.lower():
        speak("ip address  is closing")
        os.system("taskkill /F /IM cmd.exe")
        
    elif  'stop'  in query.lower( ) :
        print("your most welcome" + NAME)
        speak("your most welcome" + NAME)
        break
    elif 'what you can do for me' in query.lower() or 'operations' in query.lower():
        speak("i can search information on wikipedia and open or close chrome,paint,facebook,whatsapp,espn,command prompt,calculator,aws,gcp cloud,ip address,youtube, github,google drive,music,notepad,taskmanager")
        print("i can search information on wikipedia and open or close chrome,paint,facebook,whatsapp,espn,command prompt,calculator,aws,gcp cloud,ip address,youtube, github,google drive,music,notepad,taskmanager")
    else:
        speak ("sorry i can not perform your task,please check my work by speak what you can do for you")