import requests
import time
from random import randint

class Test(object):
    """
    Base class for page objects.
    """

    def __init__(self):
        """
        Initialize the Task set.
        """
        super(Test, self).__init__()
        self.session = requests.Session()
        self.hostname = "https://courses.omnipreneurshipacademy.com"

    def login(self):
        a = randint(5, 10)
        print(a)
        time.sleep(a)



ab = Test()
#ab.login()
ab.login()

