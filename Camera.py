from picamera import PiCamera
from time import sleep

picamera = PiCamera()
timeinbetween = 30

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    for filename in camera.capture_continuous('/home/pi/time-lapse/img{timestamp:%H-%M-%S-%f}.jpg'):
        sleep(timeinbetween)
