from flask import request
from flask_restplus import Resource

from ..util.dto import DistCenterDto
from ..util.decorator import token_required, admin_token_required
from ..service.distcenter_service import save_new_dcenter, get_all_dcenters, get_a_dcenter, update_dcenter, delete_dcenter

api = DistCenterDto.api
_dcenter = DistCenterDto.distcenter
parser = DistCenterDto.parser


@api.route('/')
class DCenterList(Resource):
	@api.doc('list_of_registered_distribution_centers')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dcenter, envelope='data')
	def get(self):
		return get_all_dcenters()
  
	@api.response(201, 'Center successfully created.')
	@api.doc('add a new distribution center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def post(self):
		data = request.form
		return save_new_dcenter(data=data)


@api.route('/<id>')
@api.param('id', 'The Distribution Center ID')
@api.response(404, 'Distribution Center not found.')
class DistCenter(Resource):
	@api.doc('get a distribution center')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dcenter)
	def get(self, id):
		dcenter = get_a_dcenter(id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('delete a distsribution center')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def delete(self, id):
		dcenter = delete_dcenter(id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('update a distribution center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self, id):
		data = request.form
		dcenter = update_dcenter(id=id, data=data)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter