import feedparser

# RSS feeds
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://hnrss.org/frontpage"
]


def get_news():
    news_list = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for article in feed.entries:
            news_list.append({
             "title": article.title,
             "summary": article.summary,
             "link": article.link
            })

    return news_list


from rapidfuzz import fuzz

def remove_similar_duplicates(news, threshold=90):
    unique_news = []

    for article in news:
        is_duplicate = False

        for unique in unique_news:
            similarity = fuzz.ratio(
                article["title"].lower(),
                unique["title"].lower()
            )

            if similarity >= threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            unique_news.append(article)

    return unique_news

if __name__ == "__main__":
    news = get_news()
    news =  remove_similar_duplicates(news)

    print(f"Total unique news: {len(news)}\n")

    for i, article in enumerate(news[:10], start=1):
        print(f"{i}. {article['title']}")
        print(article["link"])
        print("-" * 60)