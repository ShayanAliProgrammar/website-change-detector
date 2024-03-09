# Website Change detector

This Python script sends email notifications whenever it detects a change to the content of the URLs it is configured to monitor. The script makes use of queries for HTTP queries and BeautifulSoup for site scraping. The list named `urls_to_monitor` contains the URLs that are being watched.

## Get Started:

1. Make a repository clone.

   In a shell, type `git clone https://github.com/your-username/website-change-detector.git`.

2. **Set Up Requirements.**

   ```bash
   pip install -r requirements.txt
   ```

3. If you have not previously, activated two-step verification for your Google Account at [https://myaccount.google.com/u/1/security](/u/1/security/myaccount.google.com).

4. **Create Password for App:**

   - Go to the "App passwords" area at [https://myaccount.google.com/u/1/apppasswords](https://myaccount.google.com/u/1/apppasswords) after turning on [Two-Step Verification](https://google.com/myaccount/u/1/apppasswords).
   - Give your program a name (Website Change Detector, for example).
   - Select "Create" from the menu.
   - An app password will be generated by Google. Make a note of the password.

5. **Edit the file `env.py`:**
   - There will be a file called `env.py` in the root of your project.
   - Replace "insert the password here that you copied" with the app password and add this code:

     ```python
     # env.py

     # App password generated for Gmail
     password = ""
     ```

6. **Set Up URLs for Monitoring:**

   - Start `main.py`.
   - In the `urls_to_monitor` list, add the URLs you wish to keep an eye on.

7. Execute the script by typing `python main.py`

## Remark:

- Paste the app password into the `password` variable in the `env.py` file, enclosing it in quotes.
- Make sure the app password is stored securely and is not accessible to the public in the `env.py` file.

Please feel free to modify the script to suit your needs and use case.
