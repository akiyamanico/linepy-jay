import json
from social_tools.whatsappMentionFunction import send_whatsapp_message, load_whatsapp_number

def process_mention(line, msg, text):
    chat_id = msg.to
    sender_id = msg._from
    whatsapp_number = load_whatsapp_number()


    if msg.contentType == 0 and "@" in text:
        mentions_data = msg.contentMetadata.get('MENTION')

        if mentions_data:
            try:
                mentions_info = json.loads(mentions_data)  

                mentionees = mentions_info.get("MENTIONEES", [])
                if mentionees:
                    for mention in mentionees:
                        mention_id = mention.get('M')  
                        if mention_id != line.profile.mid:
                            continue
                        if mention_id:  
                            chats = line.getChats([chat_id]).chats
                            chat_info = chats[0]
                            group_name = chat_info.chatName if chat_info else "Unknown Group"
                            sender_contact = line.getContact(sender_id)
                            sender_name = sender_contact.displayName if sender_contact else "Unknown Sender"

                            if whatsapp_number:
                                send_whatsapp_message(
                                    f"You were mentioned in the group: '{group_name}' with messages: '{text}' by: '{sender_name}'",
                                    whatsapp_number
                                )
            except json.JSONDecodeError:
                print("[DEBUG] Failed to decode mentions data.")
