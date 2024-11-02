def send_help(line, to):
    try:
        line.sendMessage(
            to,
            (
                "𝐤𝐢𝐜𝐤𝐚𝐥𝐥 - Kicking all members (lol, faggot) - idk if this was working or not but yes you can try it DWYOR!\n\n"
                "𝐤𝐢𝐜𝐤 @𝐌𝐞𝐦𝐛𝐞𝐫 - Kicking a member\n\n"
                "𝐬𝐭𝐚𝐫𝐭 𝐪𝐮𝐢𝐳 - Starting a quiz (currently in development)\n\n"
                "𝐥𝐢𝐬𝐭 𝐬𝐢𝐝𝐞𝐫 - Seeing the sider list (currently in development)\n\n"
                "𝐬𝐭𝐨𝐩 𝐪𝐮𝐢𝐳 - Stopping a quiz (currently in development)\n\n"
                "𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐢𝐦𝐚𝐠𝐞 *𝐤𝐞𝐲𝐰𝐨𝐫𝐝* - Generating a picture by AI (currently in development - need donations)\n\n"
                "𝐭𝐞𝐬𝐭 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 - Testing the response time of this bot\n\n"
                "𝐬𝐞𝐭 𝐭𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 - Setting up your group for monitoring people from another group\n\n"
                "𝐚𝐝𝐝 𝐰𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐘𝐨𝐮𝐫𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩𝐍𝐮𝐦𝐛𝐞𝐫 - Use your WhatsApp number for notifications (mention notification is working now but the whole of them are currently in development)\n\n"
                "If a media platform link is attached, it will automatically download to our server and handle the upload to the chat."
            )
        )
    except Exception as e:
        pass
