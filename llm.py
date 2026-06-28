import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_news(news):

    # Limit articles to reduce token usage
    news = news[:25]

    headlines = ""

    for article in news:
        headlines += f"""
Title: {article['title']}
Summary: {article.get('summary', '')}
Link: {article['link']}

"""

    prompt = f"""
You are an expert Technology News Editor.

Below are today's technology news articles.

{headlines}

Your tasks:

1. Remove duplicate or similar news.
2. Choose the Top 5 most important technology stories.
3. Write a simple English summary (3 lines).
4. Translate each summary into natural Tamil.
5. Return the result in this format:

🚀 Title

🇬🇧 English Summary:
...

🇮🇳 Tamil:
...

🔗 Link:
...

Only return the final answer.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            print(f"Attempt {attempt+1} failed")
            print(e)
            time.sleep(5)

    return "❌ Gemini API is busy. Try again later."