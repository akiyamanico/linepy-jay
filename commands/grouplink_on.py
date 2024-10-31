# commands/grouplink_on.py
def enable_grouplink(line, chat_id):
    try:
        group = line.getGroup(chat_id)
        if group:
            if not group.preventedJoinByTicket:
                line.sendMessage(chat_id, "Group link is already on.")
            else:
                group.preventedJoinByTicket = False
                line.updateGroup(group)
                line.sendMessage(chat_id, "Group link is now enabled.")
    except Exception as e:
        pass
