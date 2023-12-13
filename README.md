# Website Change Detector

This Python script monitors specified URLs for any changes in their content and sends email notifications when a change is detected. The script uses BeautifulSoup for web scraping and Requests for HTTP requests. The monitored URLs are stored in the `urls_to_monitor` list.

## Features:

- **Change Detection:** The script compares the current content of a website with the previously stored version and sends an email notification if any changes are detected.

- **Email Notification:** Notifications are sent via email using the SMTP protocol. Gmail is configured for sending emails. The email content includes a message indicating the change and the URL of the modified website.

- **File Storage:** The script stores the HTML content of the monitored websites in separate files, using a naming convention based on the URL to avoid conflicts.

## How to Use:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Enable 2-Step Verification for your Google Account if not already enabled: [https://myaccount.google.com/u/1/security](https://myaccount.google.com/u/1/security).
4. After enabling 2-Step Verification, go to the "App passwords" section: [https://myaccount.google.com/u/1/apppasswords](https://myaccount.google.com/u/1/apppasswords).
5. Enter a name for your app (e.g., "Website Change Detector").
6. Click on the "Create" button.
7. Google will generate app password. **Copy that password**.
8. Create a new file in the root of your project called `env.py` and add the following code to it, replacing `"paste the password here that you copied"` with the actual app password:

   ```python
   # env.py

   # App password generated for Gmail
   password = "paste the password here that you copied"
   ```

9. Add the URLs you want to monitor to the `urls_to_monitor` list in `main.py`.
10. Run the script: `python main.py`.

## Note:

- Ensure the `env.py` file containing the app password is available and secure.
- This script is designed to run continuously, checking for changes every hour (`time.sleep(3600)`).

Feel free to customize the script based on your specific requirements and use case.
