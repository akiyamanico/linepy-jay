def enable_grouplink(line, chat_id):
    try:
        group = line.getGroup(chat_id)
        print(group)
        
        if group:
            print(f"preventedJoinByTicket: {group.preventedJoinByTicket}")
            if not group.preventedJoinByTicket:
                line.sendMessage(chat_id, "Group link is already on.")
            else:
                group.preventedJoinByTicket = False
                line.updateGroup(group)
                print("Updating group to enable join by link...") 
                line.sendMessage(chat_id, "Group link is now enabled.")
    except Exception as e:
        print(f"Error enabling group link: {e}")  # Logging the exception
