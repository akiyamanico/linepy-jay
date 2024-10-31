import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1, 
            size="1024x1024" 
        )
      
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None
