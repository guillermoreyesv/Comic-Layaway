class Comics():
    def search_comic_by_id(id):
        from application import app
        import requests
        import os

        response = None

        if not id:
            app.logger.error(f'id is {id}')
            return response

        # Search comic id
        try:
            url = os.getenv('MARVEL_SEARCH_URL')
            url += f'?id={id}&type=comics'

            response = requests.request("GET", url)
            response = response.json()
            pass
        except Exception as e:
            app.logger.error(f'Cant reach MS {e}')
            return response

        if not response:
            app.logger.error(f'Comic not found {id}')

        return response
