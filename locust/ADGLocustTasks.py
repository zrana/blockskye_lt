from locust import task, TaskSet
from registration import Registration
from application import ApplicationFlow
from random import randint
from login import Login
from config import USER_CREDENTAILS
import uuid
import time
import random


class RegistrationTasks(TaskSet):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(RegistrationTasks, self).__init__(*args, **kwargs)
        self.register_page = Registration(self.user.host, self.client)
        self.application_page = ApplicationFlow(self.user.host, self.client)
        self.login_page = Login(self.user.host, self.client)
        self.token = ''
        self.cookie = ''
        self.credentials = USER_CREDENTAILS

    def on_start(self):
        self.user_credentials = random.choice(self.credentials)
        self.credentials.remove(self.user_credentials)
        self.login_page.login(self.user_credentials)
        self.register_task()

    @task(4)
    def dashboard_task(self):
        print("dummy task")
        #self.login_page.visit_dashboard_page()
    # @task(15)
    def register_task(self):
        # a = randint(20, 25)
        # time.sleep(a)
        account = 'imran.bashir'
        user_email = '{}+{}@arbisoft.com'.format(account, str(uuid.uuid4().node))
        username = 'ibashir{}'.format(str(uuid.uuid4().node))
        self.register_page.register(user_email, username)
        self.application_page.visit_application_page()
        self.application_page.visit_contact_page()
        self.application_page.fill_contact_form(user_email, username)
        self.application_page.fill_education_form()
        self.application_page.fill_experience_form()
        self.application_page.fill_cover_form()
        self.application_page.enroll()

    # @task(4)
    # def dashboard_task(self):
    #     self.login_page.visit_dashboard_page()
    #
    # @task(3)
    # def application_task(self):
    #     self.login_page.visit_application_page()
    #
    # @task(2)
    # def account_task(self):
    #     self.login_page.visit_account_page()
