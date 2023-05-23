from playsound import playsound
import sys
import time
import threading


def typewrite(string):
    for k in string:
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.2)

d = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..",
            "j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.",
            "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----",
            "1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",
             ".":".-.-.-",",":"--..--","?":"..--..","=":"-...-","@":".--.-." }


message = ""

while True:
 n=input("Enter the text:- ")
 nt = n.strip().lower()
 for i in nt:
    if i.isalpha() == True or i.isalnum() == True:
     t = d[i]+" "
     
    elif i == "." or i == "," or i == "?" or i == "=" or i == "@":
     t = d[i]+" "
       
    elif i.isspace() == True:
      t = " / "
      
    message = message + t  
 
 def speaking():
   for c in message:
    if c == ".":
       playsound("D:\SOFTWARES\Python\MY CODES\python\morse code\dot.wav")
    elif c == "-":
       playsound("D:\SOFTWARES\Python\MY CODES\python\morse code\dash.wav")
    elif c == "/" or c == " ":
       time.sleep(0.2) 
 
 threading.Thread(target= speaking).start()
 threading.Thread(target= typewrite(message)).start()

 print()
 message = ""     

