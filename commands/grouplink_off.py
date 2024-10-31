# commands/grouplink_off.py
def disable_grouplink(line, chat_id):
    try:
        group = line.getGroup(chat_id)
        if group:
            if group.preventedJoinByTicket:
                line.sendMessage(chat_id, "Group link is already off.")
            else:
                group.preventedJoinByTicket = True
                line.updateGroup(group)
                line.sendMessage(chat_id, "Group link is now disabled.")
    except Exception as e:
        pass
