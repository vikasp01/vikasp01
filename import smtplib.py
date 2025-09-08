from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
import smtplib
from email.mime.text import MIMEText

def send_scheduled_email():
    """Sends a scheduled email."""
    # Email details
    sender_email = "journeywithvikas0108@gmail.com"  # Replace with your email
    sender_password = "qtaq xjyh nnsp unrt"  # Replace with your password or App Password
    receiver_email = "vikasp01082000@gmail.com"  # Replace with recipient email
    subject = "Test Email from Colab"
    body = "This is a test email sent from Google Colab using Python's smtplib."

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Connect to the SMTP server and send the email
    try:
        # For Gmail, the SMTP server is smtp.gmail.com and the port is 587 (for TLS) or 465 (for SSL)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Instantiate the BackgroundScheduler
scheduler = BackgroundScheduler()

# Add the email sending job with a CronTrigger
# This schedules the email to be sent at 8:20 AM UTC on the 7th day of every month.
scheduler.add_job(send_scheduled_email, CronTrigger(minute='45', hour='8', day='7', month='*', year='*'))

print("Scheduler started. Emails will be sent according to the schedule.")

# Start the scheduler
scheduler.start()

# Keep the notebook alive
try:
    while True:
        time.sleep(2)  # Sleep to allow the scheduler to run in the background
except (KeyboardInterrupt, SystemExit):
    # Shut down the scheduler when the script is interrupted
    scheduler.shutdown()