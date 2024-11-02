def kick_all_members(line, chat_id):
    try:
        chats = line.getChats([chat_id]).chats
        if chats:
            chat_info = chats[0]
            member_mids = chat_info.extra.groupExtra.memberMids
            if hasattr(line, 'kickoutFromGroup'):
                for member_mid in member_mids:
                    line.kickoutFromGroup(chat_id, [member_mid])
                line.sendMessage(chat_id, "Clear!")
            else:
                line.sendMessage(chat_id, "Error: 'kickoutFromGroup' method not found.")
        else:
            line.sendMessage(chat_id, "Group not found.")
    except Exception as e:
        return


# def kick_all_members(line, chat_id, batch_size=20):
#     try:
#        
#         chats = line.getChats([chat_id]).chats
#         if chats:
#             chat_info = chats[0]

#           
#             member_mids = list(chat_info.extra.groupExtra.memberMids)
            
#          
#             for i in range(0, len(member_mids), batch_size):
#                 batch = member_mids[i:i + batch_size]
#                 if hasattr(line, 'kickoutFromGroup'):
#                     line.kickoutFromGroup(chat_id, batch)  # Kick members in batches
#                 else:
#                     line.sendMessage(chat_id, "Error: 'kickoutFromGroup' method not found.")
#                     return

#             line.sendMessage(chat_id, "Clear!")
#         else:
#             line.sendMessage(chat_id, "Group not found.")
#     except Exception as e:
#         print(f"Error: {e}")
#         line.sendMessage(chat_id, f"Error: {e}")