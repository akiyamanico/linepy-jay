def disable_grouplink(line, chat_id):
    try:
        group = line.getChats(chat_id)  
        print(group) 
        
        if group:
            if hasattr(group, 'preventedJoinByTicket'):
                print(f"preventedJoinByTicket: {group.preventedJoinByTicket}")
                if group.preventedJoinByTicket:
                    line.sendMessage(chat_id, "Group link is already off.")
                else:
                    group.preventedJoinByTicket = True  
                    line.updateGroup(group)
                    print("Updating group to disable join by link...") 
                    line.sendMessage(chat_id, "Group link is now disabled.")
            else:
                line.sendMessage(chat_id, "This group does not support disabling the group link.")
    except Exception as e:
        print(f"Error disabling group link: {e}")  
