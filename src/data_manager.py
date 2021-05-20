from src import models

def first_user(session):
	return session.query(models.User).first()
