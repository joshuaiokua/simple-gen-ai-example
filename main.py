import os 
from dotenv import load_dotenv
from openai import OpenAI
import urllib

def main():
    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
    )

    # Save the image from the response to a file
    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, 'image.jpg')

if __name__ == "__main__":
    main()