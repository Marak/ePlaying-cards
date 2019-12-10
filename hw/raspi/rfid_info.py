from time import sleep
import sys
from mfrc522 import SimpleMFRC522

# Create instance of reader library
reader = SimpleMFRC522()

def get_card():
    id_card = None
    try:
        print("Hold a tag near the reader")
        id, text = reader.read()
        sleep(5)
        id_card = id
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
    return id_card
