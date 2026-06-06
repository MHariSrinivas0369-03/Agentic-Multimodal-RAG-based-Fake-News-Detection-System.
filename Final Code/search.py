from serpapi.google_search import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def google_search(query):

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    evidence = []

    if "organic_results" in results:
        for r in results["organic_results"][:5]:

            title = r.get("title","")
            snippet = r.get("snippet","")
            link = r.get("link","")

            text = f"{title} - {snippet} ({link})"
            evidence.append(text)

    return evidence