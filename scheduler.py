from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_news_agent

scheduler = BlockingScheduler()

# Runs every day at 8:00 AM
scheduler.add_job(
    run_news_agent,
    trigger="cron",
    hour=8,
    minute=0
)

print("AI News Agent started...")
scheduler.start()