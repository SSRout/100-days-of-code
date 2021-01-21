import smtplib

#provide your email and password enable less security app on for email
your_email="your email"
paskey="your key"

with smtplib.SMTP("smtp.gmail.com") as con:
    con.starttls()
    con.login(user=your_email,password=paskey)
    con.sendmail(
        from_addr="from email",
        to_addrs="to email",
        msg="subject:<sub> \n\n eom"
    )
