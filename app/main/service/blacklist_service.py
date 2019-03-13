from app.main import db
from app.main.model.blacklist import BlacklistToken


def save_token(token)
	blacklist_token = BlacklistToken(token=token)
	try:
		#insert token
		db.session.add(blacklist_token)
		db.session.commit()
		response_object = {
			'status' : 'success'
			'message' : 'Logged out successfully.'
		}
		return response_object, 200
	except Exception as e:
		response_object = {
			'status' : 'fail'
			'message' : e
		}
		return response_object, 200