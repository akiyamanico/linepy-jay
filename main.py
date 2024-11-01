from linepy import *
import time
from commands import hello, kick, kickall, grouplink_on, grouplink_off, quiz
from social_tools.instagramMediaDownloader import handle_instagram_links
from dotenv import load_dotenv
from commands.response_time import test_response_time
import os
from commands.ai import generate_image
from commands.group_commands import *


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


def message_handler(op):
    global broadcast_group_id
    msg = op.message
    text = msg.text
    
    if text is None:
        return
    
    text = text.lower()

    chat_id = msg.to
    
    if text == "hi":
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
        print(image_url)
        if image_url:
            line.sendMessage(chat_id, image_url) 
        else:
            line.sendMessage(chat_id, "Not enough credit.")
            
    elif text == "test response":
        test_response_time(line, chat_id)

    elif text == "set this groupbroadcast":
        set_group_broadcast(line, chat_id)

    elif text.startswith("broadcast message "):
        broadcast_message_text = text.replace("broadcast message ", "", 1).strip()
        broadcast_message(line, broadcast_message_text)

    elif text == "list sider":
        get_siders(line, chat_id)
        print(get_siders)

    handle_instagram_links(line, chat_id, text)  

def main():
    oepoll = OEPoll(line)
    print("Secure bot is running with E2EE and Letter Sealing...")

    while True:
        try:    
            ops = oepoll.singleTrace(count=50)
            for op in ops:
                if op.type == 25:  
                    message_handler(op)
                oepoll.setRevision(op.revision)
        except EOFError:
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
