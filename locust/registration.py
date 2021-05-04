from ADGBase import ADGBase


class Registration(ADGBase):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(Registration, self).__init__(*args, **kwargs)

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """
        if response.status_code not in (200, 201):
            raise Exception(
                'AddPI request failed with following error code: ' +
                str(response.status_code)
            )

    def visit_registration_page(self):
        url = "https://courses.omnipreneurshipacademy.com/register"
        response = self.client.get(url)
        token = response.cookies['csrftoken']

        headers = {
            'Origin': "https://courses.omnipreneurshipacademy.com",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': self.hostname,
            'Connection': 'keep-alive',
            'Cookie': "csrftoken={}".format(token)
        }

        response = self.client.get(url, headers=headers)
        self._check_response(response)
        return response

    def register(self, email, username):
        url = self.hostname + '/user_api/v2/account/registration/'
        response = self.client.get(url)
        token = response.cookies['csrftoken']
        registration_params = {
            "email": email,
            "name": "Test User",
            "username": username,
            "password": 'ARbi12.,',
            "level_of_education": "",
            "gender": "",
            "year_of_birth": "",
            "mailing_address": "",
            "goals": "",
            "city": "Medina",
            "is_adg_employee": "true",
            "company": "Petromin",
            "honor_code": "true",
        }
        headers = {
            'Origin': 'https://courses.omnipreneurshipacademy.com',
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-CSRFToken': token,
            'X-Requested-With': "XMLHttpRequest",
            'Referer': '{}register?next=%2F'.format(self.hostname),
            'Content-Length': "213",
            'Connection': 'keep-alive',
            'Cookie': "csrftoken={}".format(token)
        }
        response = self.client.post(url, data=registration_params, headers=headers, name="registration")
        self._check_response(response)
        return response
