import os

BROADCAST_FILE = 'group_broadcast.txt'

def set_group_broadcast(line, chat_id):

    with open(BROADCAST_FILE, 'w') as file:
        file.write(chat_id)
    line.sendMessage(chat_id, "Group ini telah diset sebagai group broadcast.")

def get_broadcast_group():
    if os.path.exists(BROADCAST_FILE):
        with open(BROADCAST_FILE, 'r') as file:
            return file.read().strip()
    return None

def broadcast_message(line, message):

    broadcast_group = get_broadcast_group()
    if broadcast_group:
        line.sendMessage(broadcast_group, message)
    else:
        print("Tidak ada grup broadcast yang diset.")
        line.sendMessage(broadcast_group, "Tidak ada grup broadcast yang diset.")

def get_siders(line, chat_id, sender_id):
    contact = line.getContact(sender_id)
    sender_name = contact.displayName
    broadcast_group = get_broadcast_group()
    if broadcast_group:
        message = f"{sender_name} telah melihat (atau merespon) pesan terakhir."
        line.sendMessage(broadcast_group, message)
    else:
        line.sendMessage(chat_id, f"{sender_name} telah melihat pesan terakhir.")