import requests
import os

def download_media(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            content = response.text
        
            if 'og:image' in content:
                media_url = content.split('og:image" content="')[1].split('"')[0]  
                file_path = download_file(media_url, 'temp_image.jpg')
                return file_path
            elif 'og:video' in content:
                media_url = content.split('og:video" content="')[1].split('"')[0]  
                file_path = download_file(media_url, 'temp_video.mp4')
                return file_path
            else:
                print("No media found in the provided link.")
                return None
        else:
            print(f"Failed to fetch the page, status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading media: {e}")
        return None

def download_file(media_url, file_name):
    try:
        media_response = requests.get(media_url)
        if media_response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(media_response.content)
            return file_name
        else:
            print(f"Failed to download media file, status code: {media_response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading media file: {e}")
        return None

def upload_media(line, chat_id, media_path):
    try:
        if media_path.endswith('.mp4'):
            line.sendVideo(chat_id, media_path)  
        else:
            line.sendImage(chat_id, media_path) 
        os.remove(media_path)  
    except Exception as e:
        print(f"Error uploading media: {e}")

def handle_instagram_links(line, chat_id, text):
    # Extract links from the text
    words = text.split()
    for word in words:
        if "instagram.com" in word:
            media_path = download_media(word) 
            if media_path:
                upload_media(line, chat_id, media_path)
