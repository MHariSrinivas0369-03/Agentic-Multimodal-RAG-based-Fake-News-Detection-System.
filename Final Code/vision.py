import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_image(image_file):
    # Open the uploaded file directly with PIL
    img = Image.open(image_file)

    # Use the Flash model which supports multimodal input
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content([
        "Describe what is happening in this image.",
        img
    ])

    return response.text