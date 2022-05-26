from locust import task, TaskSet
from registration import Registration
from application import ApplicationFlow
from random import randint
from login import Login
from config import USER_CREDENTAILS
import uuid
import time
import random
import json


class RegistrationTasks(TaskSet):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(RegistrationTasks, self).__init__(*args, **kwargs)
        self.lt_blockskye = Registration(self.user.host, self.client)
        #self.application_page = ApplicationFlow(self.user.host, self.client)
        #self.login_page = Login(self.user.host, self.client)
        # self.token = ''
        # self.cookie = ''
        self.credentials = USER_CREDENTAILS

    def on_start(self):
        # self.user_credentials = random.choice(self.credentials)
        # self.credentials.remove(self.user_credentials)
        #self.login_page.login(self.user_credentials)
        self.register_task()

    # @task(4)
    # def dashboard_task(self):
    #     print("dummy task")
        #self.login_page.visit_dashboard_page()

    @task
    def register_task(self):
        # a = randint(20, 25)
        # time.sleep(a)

        # create profile
        account = 'zeeshan.rana'
        user_email = '{}+{}@arbisoft.com'.format(account, str(uuid.uuid4().node))
        username = 'zrana{}'.format(str(uuid.uuid4().node))
        self.lt_blockskye.register(user_email, username)

        # update profile
        new_user_email = '{}+{}@arbisoft.com'.format(account, str(uuid.uuid4().node))
        new_username = 'zrana{}'.format(str(uuid.uuid4().node))
        self.lt_blockskye.update_profile(username, new_user_email, new_username)

        # get profile
        self.lt_blockskye.get_profile(username)

        # get calendar
        self.lt_blockskye.get_calendar(username)

        # create expense
        response = self.lt_blockskye.create_expense()

        # add ticket data
        responseBody = json.loads(response.text)
        self.lt_blockskye.add_ticket_data(responseBody['expense_approval_id'], responseBody['suvtpNumber']['accountNumber'])
        
        # get expense
        self.lt_blockskye.get_expense(responseBody['expense_approval_id'])

        # delete profile
        self.lt_blockskye.delete_profile(username)

        
        # self.application_page.visit_application_page()
        # self.applicaxtion_page.visit_contact_page()
        # self.application_page.fill_contact_form(user_email, username)
        # self.application_page.fill_education_form()
        # self.application_page.fill_experience_form()
        # self.application_page.fill_cover_form()
        # self.application_page.enroll()

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