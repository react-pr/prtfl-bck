"""
GET requests
"""

from appConfig.app import app
from uiData.data import data

@app.get('/projects/')
def getProjects():
	return data['projects']
