"""
GET requests
"""

from appConfig.app import app
from uiData.data import data

@app.get('/menu_links/')
def getMenuLinks():
	return data['menu_links']

@app.get('/projects/')
def getProjects():
	return data['projects']
