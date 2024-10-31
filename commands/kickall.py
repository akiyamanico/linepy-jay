def kick_all_members(line, chat_id):
    try:
        group = line.getGroup(chat_id)
        if group:
            member_mids = [member.mid for member in group.members if member.mid != line.profile.mid]
            if member_mids:
                line.kickoutFromGroup(chat_id, member_mids)
                line.sendMessage(chat_id, "Bye")
            else:
                line.sendMessage(chat_id, "Kosong woi")
    except Exception as e:
        line.sendMessage(chat_id, f"Error ! : {e}")
