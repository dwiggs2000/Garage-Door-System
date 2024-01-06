import RPi.GPIO as GPIO
import time
import picamera import Picamera
import smtplib

from email.mime.multipart import MIMultiplart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

DIR = './Database/'

FILE_PREFIX = 'image'
sender = 'finalproject@gmail.com'

spass = 'io54321'
reciever = 'trey_tebbe@hotmail.com'




def send_mail():

    print("sending mail")
    if not os.path.exists(DIR):
        os.makedirs(DIR)

    files = sorted(glob.glob(os.path.join(DIR,FILE_PREFIX + '[O-9][O-9][O-9]')))

    count = 0
    if len(files) > 0:
        count = int(files[-1][-7:-4])+1

        filename = os.path.join(DIR,FILE_PREFIX + '%03d.jpg' % count)

        with picamera.PiCamera() as camera:

        pic = camera.capture(filename)

    msg = MIMEmultipart(
    msg["From"] = sender
    msg["to"] = reciever
    msg["subject"] = "keypad code entered"
    body = "picture code entered"
    body = "picture attached:"

    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())

    encoders.encode_base64(part)
    part.add_header('Contenet-Disposition', 'attachment'; 'filename=%s', % filename)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.login(sender,password)
    text = msg.as_string()
    server.sendmail(sender,reciever,text)
    )
    
L1 = 25
L2 = 8
L3 = 7
L4 = 1

C1 = 12
C2 = 16
C3 = 20
C4 = 21

input = []

code = ["1","2","3","4"]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)



GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 0):
        input.append(characters[0])

        print(characters[0])

    if(GPIO.input(C2) == 1):
        input.append(characters[1])

        print(characters[1])

    if(GPIO.input(C3) == 2):

        input.append(characters[2])

        print(characters[2])
        
    if(GPIO.input(C4) == 3):

        input.append(characters[3])

        print(characters[3])

    GPIO.output(line, GPIO.LOW)

try:
    while True:
      
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        if(len(input)==4):

            if(input == code):
                print("Code Accepted")
                send_mail()
            else: 
                print("Incorrect code")
