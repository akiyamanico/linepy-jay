# main.py
from linepy import *
import time
from commands import hello, kick, kickall, grouplink_on, grouplink_off, quiz
from dotenv import load_dotenv
from commands.response_time import test_response_time
import os
from commands.ai import generate_image
from commands.group_commands import *
from tools.mention import process_mention  
from social_tools.whatsappMention import send_whatsapp_message, save_whatsapp_number
import random
from mediaTools.mediaDownloadUpload import download_video, upload_video
load_dotenv()

print("Attempting to log in...")

line_email = os.getenv("LINE_EMAIL")
line_password = os.getenv("LINE_PASSWORD")
app_name = os.getenv("LINE_APP_NAME")

line = LINE(line_email, line_password, appName=app_name)
line.server.E2EE_enable = True

line.log('Auth Token: ' + str(line.authToken))
print("Login successful with E2EE and Letter Sealing enabled!")
broadcast_group_id = None
verification_codes = {}

def message_handler(op):
    global broadcast_group_id
    msg = op.message

    if msg is None or not hasattr(msg, 'text'):
        return

    text = msg.text
    if text is None:
        return

    text = text.lower()
    chat_id = msg.to
    sender_id = msg._from
    
    if "instagram.com" in text or "tiktok.com" in text or "youtube.com" in text:
        print(f"Detected video link: {text}")
        video_path = download_video(text)
        upload_video(line, chat_id, video_path)
        
    elif text == "hi":
        hello.send_hello(line, chat_id)

    elif text.startswith("kick @"):
        kick.kick_member(line, msg, text)

    elif text == "kickall":
        kickall.kick_all_members(line, chat_id)

    elif text == "grouplink on":
        grouplink_on.enable_grouplink(line, chat_id)

    elif text == "grouplink off":
        grouplink_off.disable_grouplink(line, chat_id)

    elif text == "start quiz":
        quiz.start_quiz(line, chat_id)

    elif text == "stop quiz":
        quiz.stop_quiz(line, chat_id)

    elif quiz.current_quiz is not None:
        quiz.check_answer(line, text)

    elif text.startswith("generate image "):
        prompt = text.replace("generate image ", "", 1).strip()
        image_url = generate_image(prompt)
        if image_url:
            line.sendMessage(chat_id, image_url)
        else:
            line.sendMessage(chat_id, "Not enough credit.")

    elif text == "test response":
        test_response_time(line, chat_id)

    elif text == "set this groupbroadcast":
        set_group_broadcast(line, chat_id)

    elif text == "list sider":
        get_siders(line, chat_id)
        print(get_siders)

    elif text.startswith("add whatsapp "):
        new_number = text.replace("add whatsapp ", "").strip()
        verification_code = random.randint(1000, 9999)
        verification_codes[sender_id] = (new_number, verification_code)

        message = f"Your verification code is: {verification_code}. Please reply with this code to confirm."
        send_whatsapp_message(message, new_number)
        
        line.sendMessage(chat_id, "A verification code has been sent to your WhatsApp number. Please check and reply with the code.")
        return

    elif sender_id in verification_codes:
        expected_number, expected_code = verification_codes[sender_id]
        if text.strip() == str(expected_code):
            save_whatsapp_number(expected_number)
            line.sendMessage(chat_id, "Your WhatsApp number has been verified and saved.")
            del verification_codes[sender_id]
        else:
            line.sendMessage(chat_id, "Invalid verification code. Please try again.")
        return

    process_mention(line, msg, text)

def main():
    oepoll = OEPoll(line)
    print("Secure bot is running with E2EE and Letter Sealing...")

    while True:
        try:
            ops = oepoll.singleTrace(count=50)
            for op in ops:
                if op.type in [25, 50, 26]:
                    message_handler(op)
                oepoll.setRevision(op.revision)
        except EOFError:
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()