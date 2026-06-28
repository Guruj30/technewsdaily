from news import get_news, remove_similar_duplicates
from llm import summarize_news
from telegram_bot import send

def run_news_agent():
    news = get_news()
    news = remove_similar_duplicates(news)

    result = summarize_news(news)

    send(result)

if __name__ == "__main__":
    run_news_agent()