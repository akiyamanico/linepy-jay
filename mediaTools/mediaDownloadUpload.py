import os
import yt_dlp
import random
import string

def generate_random_filename(length=4):
    """Generate a random filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def download_video(url):
    output_folder = 'downloads'  
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    random_filename = generate_random_filename() 

    ydl_opts = {
        'format': 'bestvideo[ext=mp4][vcodec=avc1.64001F]+bestaudio[ext=m4a]/best[ext=mp4]',  
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4', 
        }],
        'outtmpl': os.path.join(output_folder, f'{random_filename}.%(ext)s'), 
        'quiet': True,
        'postprocessor_args': [
            '-b:v', '10M', 
            '-c:v', 'libx264', 
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = os.path.join(output_folder, f"{random_filename}.mp4") 
    
    return video_file

def upload_video(line, chat_id, video_path):
    try:
        line.sendVideo(chat_id, video_path) 
        print(f"Uploaded video: {video_path}")
    finally:
        if os.path.exists(video_path):
            os.remove(video_path)  
            print(f"Deleted file: {video_path}")
