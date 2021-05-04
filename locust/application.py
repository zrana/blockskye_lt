from ADGBase import ADGBase
from bs4 import BeautifulSoup


class ApplicationFlow(ADGBase):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(ApplicationFlow, self).__init__(*args, **kwargs)

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """
        if response.status_code not in (200, 201):
            raise Exception(
                'AddPI request failed with following error code: ' +
                str(response.status_code)
            )

    def visit_application_page(self):
        url = "https://courses.omnipreneurshipacademy.com/application/"
        response = self.client.get(url)
        self._check_response(response)
        return response

    def visit_contact_page(self):
        url = "https://courses.omnipreneurshipacademy.com/application/contact"
        response = self.client.get(url)
        self._check_response(response)
        return response

    def fill_contact_form(self, email, username):
        url = self.hostname + '/application/contact'
        response = self.client.get(url)
        soup = BeautifulSoup(response.text)
        middlewaretoken = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        cookie_dict = self.client.cookies.get_dict()
        edx_jwt_sign = cookie_dict['edx-jwt-cookie-signature']
        edx_jwt_payload = cookie_dict['edx-jwt-cookie-header-payload']
        aws_cors = cookie_dict['AWSALBCORS']
        aws_alb = cookie_dict['AWSALB']
        #is_enterprise = cookie_dict['experiments_is_enterprise']
        lang = cookie_dict['openedx-language-preference']
        info = cookie_dict['edx-user-info']
        login = cookie_dict['edxloggedin']
        sessionid = cookie_dict['sessionid']
        csrftoken = cookie_dict['csrftoken']
        body = {
            "csrfmiddlewaretoken": middlewaretoken,
            "name": username,
            "email": email,
            "city": "Medina",
            "saudi_national": "true",
            "gender": "m",
            "phone_number": "+123435678910",
            "birth_day": "15",
            "birth_month": "6",
            "birth_year": "1990",
            "organization": "",
            "linkedin_url": "",
            "resume": "",
            "delete-file": "No",
        }
        headers = {
            'Origin': 'https://courses.omnipreneurshipacademy.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            'Referer': 'https://courses.omnipreneurshipacademy.com/application/contact',
            'Connection': 'keep-alive',
            'Cookie': "edx-jwt-cookie-signature={}; edx-jwt-cookie-header-payload={}; AWSALBCORS={}; AWSALB={}; openedx-language-preferenc={}; edx-user-info={}; edxloggedin={}; sessionid={}; csrftoken={}".format(
                edx_jwt_sign, edx_jwt_payload, aws_cors, aws_alb, lang, info, login, sessionid, csrftoken),
        }
        resp = self.client.post(url=url, data=body, headers=headers)
        return resp

    def fill_education_form(self):
        url = self.hostname + '/application/education_experience'
        response = self.client.get(url)
        token = response.cookies['csrftoken']
        soup = BeautifulSoup(response.text)
        user_application = soup.find('input', {'name': 'user_application'})['value']
        post_url = self.hostname + '/api/applications/education/'
        education_params = {
            "id": '',
            "user_application": user_application,
            "name_of_school": 'Test',
            "degree": 'AD',
            "area_of_study": "Testing",
            "date_started_month": "6",
            "date_started_year": "2008",
            "date_completed_month": "6",
            "date_completed_year": "2012",
        }
        headers = {
            'Origin': 'https://courses.omnipreneurshipacademy.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            'Referer': 'https://courses.omnipreneurshipacademy.com/application/education_experience',
            'content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection': 'keep-alive',
            'X-CSRFToken': token,
            'X-Requested-With': "XMLHttpRequest",
        }
        resp = self.client.post(url=post_url, data=education_params, headers=headers)
        return resp

    def fill_experience_form(self):
        url = self.hostname + '/application/education_experience'
        response = self.client.get(url)
        token = response.cookies['csrftoken']
        soup = BeautifulSoup(response.text)
        user_application = soup.find('input', {'name': 'user_application'})['value']
        post_url = self.hostname + '/api/applications/work_experience/'
        education_params = {
            "id": '',
            "user_application": user_application,
            "name_of_organization": 'Test',
            "job_position_title": 'SQAE&SSAE',
            "date_started_month": "6",
            "date_started_year": "2008",
            "date_completed_month": "6",
            "date_completed_year": "2012",
            "job_responsibilities": "Load Testing"
        }
        headers = {
            'Origin': 'https://courses.omnipreneurshipacademy.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            'Referer': 'https://courses.omnipreneurshipacademy.com/application/education_experience',
            'content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection': 'keep-alive',
            'X-CSRFToken': token,
            'X-Requested-With': "XMLHttpRequest",
        }
        resp = self.client.post(url=post_url, data=education_params, headers=headers)
        return resp

    def fill_cover_form(self):
        url = self.hostname + '/application/cover_letter'
        response = self.client.get(url)
        token = response.cookies['csrftoken']
        soup = BeautifulSoup(response.text)
        middlewaretoken = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        cookie_dict = self.client.cookies.get_dict()
        edx_jwt_sign = cookie_dict['edx-jwt-cookie-signature']
        edx_jwt_payload = cookie_dict['edx-jwt-cookie-header-payload']
        aws_cors = cookie_dict['AWSALBCORS']
        aws_alb = cookie_dict['AWSALB']
        # is_enterprise = cookie_dict['experiments_is_enterprise']
        lang = cookie_dict['openedx-language-preference']
        info = cookie_dict['edx-user-info']
        login = cookie_dict['edxloggedin']
        sessionid = cookie_dict['sessionid']
        csrftoken = cookie_dict['csrftoken']
        body = {
            "csrfmiddlewaretoken": middlewaretoken,
            "business_line": "22",
            "cover_letter_file": "",
            "cover_letter": "This is cover letter",
            "button_click": "submit",
        }
        headers = {
            'Origin': 'https://courses.omnipreneurshipacademy.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            'Referer': 'https://courses.omnipreneurshipacademy.com/application/contact',
            'Connection': 'keep-alive',
            'Cookie': "edx-jwt-cookie-signature={}; edx-jwt-cookie-header-payload={}; AWSALBCORS={}; AWSALB={}; openedx-language-preferenc={}; edx-user-info={}; edxloggedin={}; sessionid={}; csrftoken={}".format(
                edx_jwt_sign, edx_jwt_payload, aws_cors, aws_alb, lang, info, login, sessionid, csrftoken),
        }
        resp = self.client.post(url=url, data=body, headers=headers)
        return resp

    def enroll(self):
        """
        Enroll user
        """
        get_url = self.hostname + "/courses/course-v1:ADG+ADG01+1/about"
        url = self.hostname + '/change_enrollment'
        response = self.client.get(get_url)
        token = response.cookies['csrftoken']
        params = {
            "course_id": "course-v1:ADG+ADG01+1",
            "enrollment_action": "enroll"
        }
        headers = {
            'Origin': "https://courses.omnipreneurshipacademy.com",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-CSRFToken': token,
            'X-Requested-With': "XMLHttpRequest",
            'Referer': "https://courses.omnipreneurshipacademy.com/courses/course-v1:ADG+ADG01+1/about",
            'Connection': 'keep-alive'
        }
        response = self.client.post(url, params, headers=headers)
        return response
