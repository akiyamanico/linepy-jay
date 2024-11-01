import requests
import os

whatsapp_number_file = "whatsapp_number.txt" #this is where the whatsapp number is saved

def send_whatsapp_message(message, whatsapp_number):
    url = "" #api url
    api_key = "" #api key

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
