import dotenv
import scrape_web
import send_email


def start():
    dotenv.load_dotenv(dotenv_path='/Users/jenya/Desktop/becoming_full_stack/python/my_projects/scrape_and_send_news_meneame/.env')
    return send_email.email(scrape_web.scrape_news())


if __name__ == '__main__':
    start()

