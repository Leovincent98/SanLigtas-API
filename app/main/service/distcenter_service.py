
import datetime

from app.main import db
from app.main.model.distcenter import DistCenter


def save_new_dcenter(data):
	dcenter = DistCenter.query.filter_by(address=data['address']).first()
	if not dcenter:
		new_dcenter = DistCenter(
			name=data['name'],
			address=data['address'],
			capacity=data['capacity']
		)
		save_changes(new_dcenter)
		response_object = {
			'status' : 'success',
			'message' : 'distribution center added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Name already used.'
		}
		return response_object, 409


def get_all_dcenters():
	return DistCenter.query.all()

def get_a_dcenter(id):
	return DistCenter.query.filter_by(id=id).first()


def save_changes(data):
	db.session.add(data)
	db.session.commit()

def update_dcenter(id, data):
	dcenter = DistCenter.query.filter_by(id=id).first()
	otherdcenters = DistCenter.query.filter(DistCenter.id != id).all()
	if dcenter:
		check_existing = False
		for x in otherdcenters:
			if x.id == data['address']:
				check_existing = True
		if check_existing:
			dcenter.name=data['name'],
			dcenter.address=data['address'],
			dcenter.capacity=data['capacity']
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'distribution center updated'
			}
			return response_object, 200
		else:
			response_object = {
			'status' : 'fail',
			'message' : 'New Address already used.'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching distribution center found.'
		}
		return response_object, 409


def delete_dcenter(id):
	dcenter = DistCenter.query.filter_by(id=id).first()
	if dcenter:
			db.session.delete(dcenter)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'distribution center deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching distribution center found.'
		}
		return response_object, 409