import smtplib
from tkinter import Tk, Label, Entry, Text, Button

def send_email():
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")  # Get the text from the Text widget
    to_email = to_entry.get()

    sender_email = "vinayorugonda15@gmail.com"
    sender_password = "Vinay@123"

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg)
        server.quit()
        result_label.config(text="Email sent successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Create the main window
root = Tk()
root.title("Mail Application")

# Create and place GUI components
Label(root, text="To:").grid(row=0, column=0, sticky="e")
to_entry = Entry(root)
to_entry.grid(row=0, column=1, columnspan=2, sticky="we")

Label(root, text="Subject:").grid(row=1, column=0, sticky="e")
subject_entry = Entry(root)
subject_entry.grid(row=1, column=1, columnspan=2, sticky="we")

Label(root, text="Body:").grid(row=2, column=0, sticky="e")
body_text = Text(root, height=5, width=40)
body_text.grid(row=2, column=1, columnspan=2, sticky="we")

send_button = Button(root, text="Send Email", command=send_email)
send_button.grid(row=3, column=1, pady=10)

result_label = Label(root, text="", fg="black")
result_label.grid(row=4, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
