"""
models configuration
"""

from pydantic import BaseModel


class Mailer(BaseModel):
	name: str
	email: str
	message: str
