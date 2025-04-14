import smtplib
import traceback
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials import email, password  # Your email and password from a safe file


def send_error_email(subject, plain_message, html_message=None, to_email="pranit.chilbule221@vit.edu"):
    try:
        msg = MIMEMultipart("alternative")
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach plain and HTML versions of the message
        msg.attach(MIMEText(plain_message, 'plain'))
        if html_message:
            msg.attach(MIMEText(html_message, 'html'))

        # Connect to Gmail SMTP server and send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()
        print("✅ Error email sent successfully.")
    except Exception as e:
        print("❌ Failed to send error email:", str(e))


try:
    print("Running main script...")
    1 / 0  # Simulate an error
    print("Script finished without error.")

except Exception as e:
    # Capture full traceback as string
    error_trace = traceback.format_exc()

    # Current timestamp for the error log
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subject = "🚨 URGENT: Error Occurred in Python Script"
    plain_message = f"An error occurred in your Python script:\n\n{error_trace}"

    # Create HTML message with proper error inserted into the log table
    html_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Script Error Log</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                color: #333;
                background-color: #f5f5f5;
            }}
            h1 {{
                color: #c0392b;
                margin-bottom: 20px;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .error-message {{
                background-color: #ffeeee;
                padding: 15px;
                border-left: 5px solid #e74c3c;
                margin-bottom: 20px;
                font-family: monospace;
                white-space: pre-wrap;
            }}
            .log-table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            .log-table th, .log-table td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            .log-table th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            .log-table tr:hover {{
                background-color: #f9f9f9;
            }}
            .timestamp {{
                white-space: nowrap;
            }}
            .error {{
                color: #e74c3c;
                font-weight: bold;
            }}
            .warning {{
                color: #f39c12;
            }}
            .info {{
                color: #3498db;
            }}
            .success {{
                color: #2ecc71;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Script Error Detected</h1>

            <h2>Error Details:</h2>
            <div class="error-message">{error_trace}</div>

            <h2>System Log Data</h2>

            <table class="log-table">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Level</th>
                        <th>Source</th>
                        <th>Message</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="timestamp">{current_time}</td>
                        <td><span class="error">ERROR</span></td>
                        <td>Python Script</td>
                        <td>Division by zero error</td>
                        <td>{str(e)}</td>
                    </tr>
                    <tr>
                        <td class="timestamp">{current_time}</td>
                        <td><span class="info">INFO</span></td>
                        <td>System</td>
                        <td>Script execution started</td>
                        <td>Main process</td>
                    </tr>
                    <tr>
                        <td class="timestamp">{current_time}</td>
                        <td><span class="warning">WARNING</span></td>
                        <td>System</td>
                        <td>Unexpected termination</td>
                        <td>Process terminated due to error</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    # Send the email with both plain text and HTML versions
    send_error_email(subject, plain_message, html_message)