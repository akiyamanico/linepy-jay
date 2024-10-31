def kick_member(line, msg, text):
    print(text)
    print(msg)
    print(line)
    try:
        
        if 'MENTION' in msg.contentMetadata.keys():
            mentionees = eval(msg.contentMetadata['MENTION'])['MENTIONEES']
            if mentionees:
                member_mid = mentionees[0]['M']  
                if hasattr(line, 'kickoutFromGroup'):
                    line.kickoutFromGroup(msg.to, [member_mid])
                    print("tertendang")
                else:
                    line.sendMessage(msg.to, "udah di ganti commandnya berarti lol -bot")
                    print("lololol")
            else:
                line.sendMessage(msg.to, "Bener ga?")
                print("error")
        else:
            line.sendMessage(msg.to, "Mention dulu")
    except Exception as e:
        line.sendMessage(msg.to, f"Error: {e}")
        print(e)
