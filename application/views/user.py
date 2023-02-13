from flask.views import MethodView
from flask import request


class AsignComic(MethodView):
    def post(self):
        from application import app
        from application.utils.user import User
        from application.utils.comics import Comics
        from application.utils.request import Request
        from application.config.db import mongo

        # Get Bearer Token
        authorization = request.headers.get('Authorization')

        # Validate Token
        try:
            info_user = User.validate_token(authorization)
        except Exception as e:
            response = {
                'code': 400,
                'message': 'Invalid token'
            }
            app.logger.error(f'Invalid token {e}')
            return response, response['code']

        # Params Dict
        status, params_received = Request.get_json(request)
        if not status:
            return params_received, params_received['code']

        # Comics
        comics_list = params_received.get('comics_list', [])

        # Sanitize Comics
        comic_list_cleaned = []
        try:
            for comic_id in comics_list:
                # Only accept integers
                comic_id_int = int(comic_id)

                # Search in MS Comics by id
                result = Comics.search_comic_by_id(id=comic_id_int)
                if not result:
                    raise Exception('Marvel comic not found')
                comic_found = result['comics']
                comic_list_cleaned.append(comic_found)
        except Exception as e:
            response = {
                'code': 400,
                'comic_list': comics_list,
                'message': str(e)
            }
            app.logger.error(f'Comic list {e}')
            return response, response['code']

        # Get users collection
        try:
            user_collection = mongo.db.users
        except Exception as e:
            response = {
                'code': 400,
                'comic_list': comics_list,
                'message': str(e)
            }
            app.logger.error(f'User.ManageUser.get.mongo_error.collection {e}')
            return response, response['code']

        # Save comic list
        dict_to_match = {'access_token': info_user['token']}
        dict_to_update = {
            '$addToSet': {
                'comics_layaway': {
                    '$each': comic_list_cleaned
                    }
                }
            }
        result = user_collection.update_one(dict_to_match, dict_to_update)
        # Check result
        if result.acknowledged and result.modified_count:
            response = {
                'comic_list': comics_list,
                'code': 201,
                'message': 'Comics layawayed'
            }
            app.logger.debug(f'User.Login.post {response}')
        elif result.modified_count == 0:
            response = {
                'code': 200,
                'comic_list': comics_list,
                'message': 'Comics already layawayed'
            }
            app.logger.debug(f'User.Login.post {response}')
        else:
            response = {
                'code': 500,
                'comic_list': comics_list,
                'message': 'Server error'
            }
            app.logger.error(f'User.Login.post {response}')
        return response, response['code']

