"""
POST requests
"""

from appConfig.app import app
from baseModel.models import Mailer
import resend
import os

@app.post('/sending/', response_model=Mailer)
def sendMail(mailer: Mailer):
	resend.api_key = os.environ["RESEND_API"]
	params = {
			"from": "Acme <onboarding@resend.dev>",
			"to": [f"{mailer.email}"],
			"subject": "Feedback from portfolio",
			"html": f"<strong>H!, {mailer.name} ✌️ <br />{mailer.message} <br /><img src='https://www.thedrive.com/uploads/2022/12/13/22C0387_051.jpg?auto=webp&crop=16%3A9&auto=webp&optimize=high&quality=70&width=1440' width='100px' alt='image'></img></strong>",
	}
	email = resend.Emails.send(params)
	return mailer
