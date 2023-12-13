import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
from env import password  # Make sure the 'env' module with the 'password' variable is available
import ssl
import smtplib
import time

# List of URLs to monitor
urls_to_monitor = ["http://localhost:8000"]

def send_notification(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Continue processing the content
            content = response.text
            soup = BeautifulSoup(content, "html.parser")

            # Replace invalid characters in the URL for the file name
            file_name = f"./website_html_{url.replace(':', '_cln_').replace('/', '_slh_')}.txt"

            try:
                with open(file_name, 'r') as file_content:
                    if file_content.read() != soup.__str__():
                        print('Sending Email...')
                        email_sender = "janishayan10@gmail.com"
                        email_password = password
                        email_receiver = "shayanjaniprogrammar@gmail.com"

                        subject = "Website Change Detection"
                        body = f"""<h1>Hi, there</h1> <p>There is a change for this website page: {url}</p>"""

                        em = EmailMessage()
                        em['From'] = email_sender
                        em['To'] = email_receiver
                        em['Subject'] = subject
                        em.set_content(body)
                        em.set_type('text/html')

                        context = ssl.create_default_context()

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(email_sender, email_password)
                            smtp.sendmail(email_sender, email_receiver, em.as_string())
                            print('Email Sent Successfully 😊')

                        with open(file_name, "w") as file:
                            file.write(soup.__str__())

            except FileNotFoundError:
                with open(file_name, "w") as file:
                    file.write(soup.__str__())

        else:
            print(f"Error: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")

# Run the script in a loop every 1 hour
while True:
    for url in urls_to_monitor:
        send_notification(url)

    # Wait for 1 hour before checking again
    time.sleep(3600)
