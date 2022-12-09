# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "seccameraepl445@gmail.com"
email_password = "wmmqojqunhcqxwtb"

# create email
msg = EmailMessage()
msg['Subject'] = "EPL445 Security Camera"
msg['From'] = email_address
msg['To'] = "nvaki001@ucy.ac.cy"
msg.set_content("Hello , we have detected motion")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)