from locust import task, TaskSet
from application_flow import ApplicationFlow
import uuid
import json


class RegistrationTasks(TaskSet):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(RegistrationTasks, self).__init__(*args, **kwargs)
        self.lt_blockskye = ApplicationFlow(self.user.host, self.client)
        self.account = 'zeeshan.rana'
        self.username = ''

    def on_start(self):
        # create profile
        user_email = '{}+{}@arbisoft.com'.format(self.account, str(uuid.uuid4().node))
        self.username = 'zrana{}'.format(str(uuid.uuid4().node))
        self.lt_blockskye.create_profile(user_email, self.username)

    @task(4)
    def update_profile(self):
        # update profile
        new_user_email = '{}+{}@arbisoft.com'.format(self.account, str(uuid.uuid4().node))
        new_username = 'zrana{}'.format(str(uuid.uuid4().node))

        self.lt_blockskye.update_profile(self.username, new_user_email, new_username)

    @task(3)
    def get_profile(self):
        # get profile
        self.lt_blockskye.get_profile(self.username)
        # get calendar
        self.lt_blockskye.get_calendar(self.username)

    # @task(2)
    # def delete_profile(self):
    #     # delete profile
    #     self.lt_blockskye.delete_profile(self.username)

    @task(10)
    def create_expense_and_booking(self):
        # create expense
        response = self.lt_blockskye.create_expense()
        # add ticket data
        response_body = json.loads(response.text)
        import time
        time.sleep(6)
        self.lt_blockskye.add_ticket_data(response_body['expense_approval_id'], response_body['suvtpNumber']['accountNumber'])
        # get expense
        #time.sleep(30)
        #self.lt_blockskye.get_expense(response_body['expense_approval_id'])

    # def on_stop(self):
    #     # delete profile
    #     self.lt_blockskye.delete_profile(self.username)