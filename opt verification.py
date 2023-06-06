import random
import smtplib
from tkinter import *
from tkinter import messagebox

# Generate random OTP
def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

# Send OTP via Gmail
def send_otp(email, otp):
    gmail_user = 'cbsravani0204@gmail.com'
    gmail_password = 'yaplfnydfxdsohxv'

    sent_from = gmail_user
    to = 'saipreethicsm@gmail.com'
    subject = 'OTP Verification'
    body = f'Your OTP is: {otp}'

    email_text = f"From: {sent_from}\nTo: {', '.join(to)}\nSubject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return True
    except:
        return False

# Verify OTP
def verify_otp():
    user_otp = otp_entry.get()

    if user_otp == str(otp):
        messagebox.showinfo("Success", "OTP verification successful!")
    else:
        messagebox.showerror("Error", "OTP verification failed!")

# Generate and send OTP when button is clicked
def send_otp_clicked():
    email = email_entry.get()

    global otp
    otp = generate_otp()

    if send_otp(email, otp):
        messagebox.showinfo("Success", "OTP sent successfully!")
    else:
        messagebox.showerror("Error", "Failed to send OTP!")

# Create UI
root = Tk()
root.title("OTP Verification")

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

otp_button = Button(root, text="Send OTP", command=send_otp_clicked)
otp_button.pack()

otp_label = Label(root, text="OTP:")
otp_label.pack()
otp_entry = Entry(root)
otp_entry.pack()

verify_button = Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

root.mainloop()