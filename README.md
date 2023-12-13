# Website Change Detector

This Python script monitors specified URLs for any changes in their content and sends email notifications when a change is detected. The script leverages BeautifulSoup for web scraping and Requests for HTTP requests. The monitored URLs are stored in the `urls_to_monitor` list.

## Features:

- **Change Detection:** The script efficiently compares the current content of a website with the previously stored version and triggers an email notification if any changes are detected.

- **Email Notification:** Notifications are dispatched via email using the SMTP protocol, with Gmail configured as the email service provider. The email content includes a detailed message indicating the change and the URL of the modified website.

- **File Storage:** The script intelligently stores the HTML content of the monitored websites in separate files, utilizing a naming convention based on the URL to prevent conflicts.

## How to Use:

1. **Clone the repository.**

   ```bash
   git clone https://github.com/your-username/website-change-detector.git
   ```

2. **Install Dependencies.**

   ```bash
   pip install -r requirements.txt
   ```

3. **Enable Two-Step Verification for your Google Account if not already enabled:**
   [https://myaccount.google.com/u/1/security](https://myaccount.google.com/u/1/security).

4. **Generate App Password:**

   - After enabling Two-Step Verification, navigate to the "App passwords" section: [https://myaccount.google.com/u/1/apppasswords](https://myaccount.google.com/u/1/apppasswords).
   - Enter a name for your app (e.g., "Website Change Detector").
   - Click on the "Create" button.
   - Google will generate an app password. **Copy that password.**

5. **Create `env.py` File:**

   - In the root of your project, create a new file named `env.py`.
   - Add the following code, replacing `"paste the password here that you copied"` with the actual app password:

     ```python
     # env.py

     # App password generated for Gmail
     password = "paste the password here that you copied"
     ```

6. **Configure URLs to Monitor:**

   - Open `main.py`.
   - Add the URLs you want to monitor to the `urls_to_monitor` list.

7. **Run the Script:**
   ```bash
   python main.py
   ```

## Note:

- Ensure the `env.py` file containing the app password is secure and not shared publicly.
- The script is designed to run continuously, checking for changes every hour (`time.sleep(3600)`).

Feel free to customize the script based on your specific requirements and use case.

Make sure to replace `[add your email address here]` and `[add your other email address here]` with your actual email addresses.
