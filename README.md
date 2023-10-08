# Open Relay Check Script

## Overview

This Python script is designed to test if an SMTP server is configured as an open relay. Open relays are considered a security risk as they allow anyone on the Internet to send email through your server. This can lead to your server being blacklisted by spam filters.

## Requirements

- Python 3.x
- smtplib library (usually comes pre-installed with Python)

## Usage

1. Open a terminal window.
2. Navigate to the directory where open-relay-check.py is located.
3. Run the script using Python 3:

    python3 open-relay-check.py

## Output

The script will attempt to send an email through the SMTP server without authenticating. If the server allows the email to be sent, it is an open relay. If the server blocks the attempt, it is not an open relay.

### Example Output

If the server does not allow open relay, you will see:

Server doesn't allow open relay. Error: {'example@example.com': (454, b'4.7.1 <example@example.com>: Relay access denied')}

## Customization

You can customize the script by modifying the following variables:

- SMTP_SERVER: The address of the SMTP server you want to test.
- SMTP_PORT: The port number to use for the SMTP server.
- FROM_EMAIL: The email address that will be used as the sender.
- TO_EMAIL: The email address that will be used as the recipient.

## Debugging

To enable debug output, uncomment the line:

server.set_debuglevel(1)

This will print the SMTP conversation to the console, which can be useful for troubleshooting.
