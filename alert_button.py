
import time
import RPi.GPIO as GPIO
import requests


TOKEN: “8780387298:AAE4lDtkcighsE6Md"
CHAT_ID = "603950****"


def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot8780387298:AAE4lDtkcighsE6Md_ID6uuNOMHMmA/sendmessage"
    payload = {"603950669": CHAT_ID, "text": text}
    try:
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        print(f"Connection Error: {e}")


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

print("System is running!")


try:
    while True:

        if GPIO.input(7) == GPIO.HIGH:
            if not button_pressed:
                print("Button Pressed! Sending Telegram...")
                send_telegram_msg (“ someone pushed the button")
                button_pressed = True
        else:

            button_pressed = False

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting the program. Have a nice day!")
    GPIO.cleanup()
