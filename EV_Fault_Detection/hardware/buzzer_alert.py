import RPi.GPIO as GPIO
from scripts.predict_fault import predict_fault

buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

pred, _ = predict_fault()
GPIO.output(buzzer_pin, pred == 1)
