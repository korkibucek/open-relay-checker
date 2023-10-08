import smtplib


def check_open_relay(server, port, from_email, to_email):
    try:
        server = smtplib.SMTP(server, port)
        server.set_debuglevel(1)
        server.sendmail(from_email, to_email,
                        "Subject: Test Open Relay\n\nThis is a test.")
        print("Server allows open relay.")
    except Exception as e:
        print(f"Server doesn't allow open relay. Error: {e}")
    finally:
        server.quit()


# Replace these variables
SMTP_SERVER = "your-mail-server.com"
SMTP_PORT = 25
FROM_EMAIL = "test@your-domain.com"
TO_EMAIL = "test@external-domain.com"

check_open_relay(SMTP_SERVER, SMTP_PORT, FROM_EMAIL, TO_EMAIL)