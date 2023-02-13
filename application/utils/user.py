class User():
    def validate_token(token):
        from application import app
        import requests
        import os

        response = None

        if not token:
            app.logger.error(f'token is {token}')
            raise Exception('Not found token')
            return response

        start_with_bearer = token.startswith('Bearer ')

        if not start_with_bearer:
            app.logger.error(f'token not start with Bearer {token}')
            raise Exception('Not found token')
            return response

        token = token[7:]

        # Search token profile
        try:
            url = os.getenv('USER_MANAGMENT_URL')

            headers = {
                'Authorization': f'Bearer {token}'
            }

            response = requests.request("GET", url, headers=headers)
            if response.status_code != 200:
                raise Exception('invalid token')
            response = response.json()

        except Exception as e:
            app.logger.error(f'Cant reach MS {e}')
            raise Exception('Server error')
            return response

        if not response:
            app.logger.error(f'User not found {token}')
            raise Exception('Not found token')

        return response
