import dotenv
import scrape_web
import send_email
import os


def start():
    dotenv.load_dotenv(dotenv_path=os.path.join(os.path.abspath(__file__), '.env'))
    return send_email.email(scrape_web.scrape_news())


if __name__ == '__main__':
    start()
