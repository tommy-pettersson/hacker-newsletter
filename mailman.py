import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class Mailman:

    def send_mail(articles):

        message = "Subject: Top 10 articles from hacker news 🖥\n\n"

        for article in articles:
            message += f"{article['title']}\n"
            message += f"{article['link']}\n\n"

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get("MY_EMAIL"), password=os.environ.get("MY_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ.get("MY_EMAIL"),
                to_addrs=os.environ.get("RECIEVER_EMAIL"),
                msg=message.encode("utf8")
            )
