import json
from social_tools.whatsappMention import send_whatsapp_message, load_whatsapp_number

            
def process_mention(line, msg, text):
    chat_id = msg.to
    sender_id = msg._from
    whatsapp_number = load_whatsapp_number()

    print(f"[DEBUG] Received message: {text}")
    print(f"[DEBUG] Sender ID: {sender_id}, Chat ID: {chat_id}")

    if msg.contentType == 0 and "@" in text:
        mentions_data = msg.contentMetadata.get('MENTION')

        print(f"[DEBUG] Mentions data: {mentions_data}")

        if mentions_data:
            try:
                mentions_info = json.loads(mentions_data)  # Parse JSON

                mentionees = mentions_info.get("MENTIONEES", [])
                if mentionees:
                    for mention in mentionees:
                        mention_id = mention.get('M')  
                        if mention_id:  
                            group_info = line.getGroup(chat_id)
                            group_name = group_info.name if group_info else "Unknown Group"
                            sender_contact = line.getContact(sender_id)
                            sender_name = sender_contact.displayName if sender_contact else "Unknown Sender"

                            if whatsapp_number:
                                send_whatsapp_message(
                                    f"You were mentioned in the group: '{group_name}' with messages: '{text}' by: '{sender_name}'",
                                    whatsapp_number
                                )
                                print("[DEBUG] WhatsApp notification sent.")
                            else:
                                print("[DEBUG] No WhatsApp number set, skipping notification.")
                else:
                    print("[DEBUG] No valid mentionees found in the mentions data.")
            except json.JSONDecodeError:
                print("[DEBUG] Failed to decode mentions data.")
        else:
            print("[DEBUG] No mentions data found.")
    else:
        print("[DEBUG] Message does not contain mentions.")