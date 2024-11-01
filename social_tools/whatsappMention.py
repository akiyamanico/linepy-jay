import requests
import random
import os

whatsapp_number_file = "whatsapp_number.txt" #this is where the whatsapp number is saved

verification_codes = {}

def send_whatsapp_message(message, whatsapp_number):
    url = ""
    api_key = "" 

    payload = {
        "recipient": whatsapp_number,
        "apikey": api_key,
        "text": message
    }

    response = requests.post(url, data=payload) 
    print(f"[DEBUG] WhatsApp API Response: {response.status_code}, {response.text}")
    return response.status_code == 200

def load_whatsapp_number():
    if os.path.exists(whatsapp_number_file):
        with open(whatsapp_number_file, "r") as file:
            number = file.read().strip()
            if number:
                print(f"[DEBUG] WhatsApp number loaded from file: {number}")
                return number
    return None

def save_whatsapp_number(number):
    with open(whatsapp_number_file, "w") as file:
        file.write(number)
        print(f"[DEBUG] WhatsApp number saved to file: {number}")
        
def add_whatsapp_number(line, chat_id, sender_id, text):
    new_number = text.replace("add whatsapp ", "").strip()
    verification_code = random.randint(1000, 9999)
    verification_codes[sender_id] = (new_number, verification_code)

    message = f"Your verification code is: {verification_code}. Please reply with this code to confirm."
    send_whatsapp_message(message, new_number)

    line.sendMessage(chat_id, "A verification code has been sent to your WhatsApp number. Please check and reply with the code.")

def verify_whatsapp_number(line, chat_id, sender_id, text):
    print(f"[DEBUG] Verifying WhatsApp number for sender_id: {sender_id} with input: {text.strip()}")
    if sender_id in verification_codes:
        expected_number, expected_code = verification_codes[sender_id]
        print(f"[DEBUG] Expected code: {expected_code}, Provided code: {text.strip()}")
        if text.strip() == str(expected_code):
            save_whatsapp_number(expected_number)
            line.sendMessage(chat_id, "Your WhatsApp number has been verified and saved.")
            del verification_codes[sender_id]
        else:
            line.sendMessage(chat_id, "Invalid verification code. Please try again.")
    else:
        line.sendMessage(chat_id, "No verification in progress. Please add your WhatsApp number first.")
            
def save_whatsapp_number(number):
    with open(whatsapp_number_file, "w") as file:
        file.write(number)
        print(f"[DEBUG] WhatsApp number saved to file: {number}")
