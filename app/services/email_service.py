import resend
from flask import current_app


def send_password_reset_link(email, reset_url):
    resend.api_key = current_app.config["RESEND_API_KEY"]
    resend.Emails.send(
        {
            "from": "FinTrack <onboarding@resend.dev>",
            "to": [email],
            "subject": "Reset your FinTrack password",
            "html": f"""
            <h2>Reset your password</h2>

            <p>
                We received a request to reset your FinTrack account password.
            </p>

            <p>
                Click the button below to create a new password:
            </p>

            <p>
                <a href="{reset_url}">
                    Reset Password
                </a>
            </p>

            <p>
                This link will expire in 10 minutes.
            </p>

            <p>
                If you did not request this, you can safely ignore
                this email.
            </p>
        """,
        }
    )


def send_Welcome(email,user):
    resend.api_key = current_app.config["RESEND_API_KEY"]
    resend.Emails.send(
        {
           "from": "FinTrack <onboarding@resend.dev>",
            "to": [email],
            "subject": "Welcome to FinTrack!",
            "html": f"""
                <h1>A warm greating from Xitiz</h1>
                <h2>Welcome {user} To FinTrack</h2>
                <p>
                    Your FinTrack account has been successfully created.
                </p>

                <p>
                    You can now start tracking your income, expenses,
                    and financial accounts.
                </p>

                <p>
                    Thanks for joining FinTrack!
                </p>
            """,
        }
    )
