
import time
import RPi.GPIO as GPIO
import requests

# Telegram Setup
TOKEN = "8731479116:AAGPTCh5JCaHMQxYm6N_UkbDGv39jJ-npAo"
CHAT_ID = "7670116989"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

GPIO.setmode(GPIO.BOARD) # Keeps your physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
print("System Ready. Monitoring physical pin 7...")

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        
        # This sends the message to your phone
        payload = {"chat_id": CHAT_ID, "text": "Someone pressed the alert button!"}
        try:
            requests.post(URL, data=payload)
        except Exception as e:
            print(f"Error: {e}")
            
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    
    time.sleep(0.1)
