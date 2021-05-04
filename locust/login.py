from ADGBase import ADGBase
from config import PASSWORD


class Login(ADGBase):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(Login, self).__init__(*args, **kwargs)

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """
        if response.status_code not in (200, 201):
            raise Exception(
                'API request failed with following error code: ' +
                str(response.status_code)
            )

    def login(self, username):
        """
        Login user
        """
        get_url = self.hostname + "/login"
        url = self.hostname + '/user_api/v1/account/login_session/'
        response = self.client.get(get_url)
        token = response.cookies['csrftoken']
        params = {
            "email": username,
            "password": PASSWORD
        }
        headers = {
            'Origin': "https://courses.omnipreneurshipacademy.com",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-CSRFToken': token,
            'X-Requested-With': "XMLHttpRequest",
            'Referer': "https://courses.omnipreneurshipacademy.com/login?next=%2F",
            'Connection': 'keep-alive'
        }
        response = self.client.post(url, params, headers=headers)
        return response