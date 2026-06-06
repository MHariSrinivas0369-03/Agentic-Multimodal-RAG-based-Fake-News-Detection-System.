from search import google_search
from vision import analyze_image
from prompts import VERIFY_PROMPT

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def verify_claim(claim, image=None):

    # Step 1: retrieve evidence
    evidence = google_search(claim)
    evidence_text = "\n".join(evidence)

    # Step 2: analyze image
    image_analysis = "No image provided."

    if image is not None:
        image_analysis = analyze_image(image)

    # Step 3: reasoning
    prompt = VERIFY_PROMPT.format(
        claim=claim,
        image_analysis=image_analysis,
        evidence=evidence_text
    )

    # Initialize the model
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Generate the response with a temperature of 0 for deterministic outputs
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(temperature=0.0)
    )

    result = response.text

    return {
        "analysis": result,
        "evidence": evidence,
        "image_analysis": image_analysis
    }