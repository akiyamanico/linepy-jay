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


#basically get_siders required a client which supported to get lastReadMessage
#because we are using windows as a client in thrift so these lines of get_siders is very useless
def get_siders(line, chat_id):
    try:
        last_read_message_id = line.getLastReadMessageIds(chat_id)
        
        if last_read_message_id:
            read_members = line.getReadMemberIds(chat_id, last_read_message_id)
            
            if read_members:
                members = [line.getContact(mid).displayName for mid in read_members]
                siders_message = "Orang yang sudah melihat pesan terakhir:\n" + "\n".join(members)
            else:
                siders_message = "Tidak ada yang telah melihat pesan terakhir."
            
            broadcast_group = get_broadcast_group()
            if broadcast_group:
                line.sendMessage(broadcast_group, siders_message)
            else:
                line.sendMessage(chat_id, siders_message)
        else:
            line.sendMessage(chat_id, "Tidak dapat menemukan ID pesan terakhir.")
    except Exception as e:
        print(f"Error fetching siders: {e}")