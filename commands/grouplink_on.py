def enable_grouplink(line, chat_id):
    try:
        group = line.getChats(chat_id)  
        print(group) 
        
        if group:
            if hasattr(group, 'preventedJoinByTicket'):
                print(f"preventedJoinByTicket: {group.preventedJoinByTicket}")
                if not group.preventedJoinByTicket:
                    line.sendMessage(chat_id, "Group link is already on.")
                else:
                    group.preventedJoinByTicket = False
                    line.updateGroup(group)
                    line.sendMessage(chat_id, "Group link is now enabled.")
            else:
                line.sendMessage(chat_id, "This group does not support enabling the group link.")
    except Exception as e:
        print(f"Error enabling group link: {e}")  
