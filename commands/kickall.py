def kick_all_members(line, chat_id):
    try:
        group = line.getGroup(chat_id)  
        print(group)

        if group:
            member_mids = [member.mid for member in group.members]  
            print(f"Kicking out the following members: {member_mids}")

            if hasattr(line, 'kickoutFromGroup'):
                for member_mid in member_mids:
                    line.kickoutFromGroup(chat_id, [member_mid]) 
                line.sendMessage(chat_id, "Clear!")
            else:
                line.sendMessage(chat_id, "Error!")
        else:
            line.sendMessage(chat_id, "Group not found.")
    except Exception as e:
        line.sendMessage(chat_id, f"Error: {e}")
        print(e)