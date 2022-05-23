import os
from locust import HttpUser, TaskSet
from BlockSkyeLocustTasks import RegistrationTasks


class BlockSkyeTest(TaskSet):
    """
    Execute Load testscd
    """
    tasks = {
        RegistrationTasks: 1
    }


class BlockSkyeLocust(HttpUser):
    """
    Representation of an HTTP "user".
    Defines how long a simulated user should wait between executing tasks, as
    well as which TaskSet class should define the user's behavior.
    """
    host = 'https://staging.blockskye.com'
    tasks = {BlockSkyeTest: 1}  #globals()[os.getenv('LOCUST_TASK_SET', 'ADGTest')]
    min_wait = 90000
    max_wait = 180000