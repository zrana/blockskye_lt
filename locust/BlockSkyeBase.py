
class BlockSkyeBase(object):
    """
    Base class for page objects.
    """

    def __init__(self, hostname, client):
        """
        Initialize the client.
        :param hostname: The hostname of the test server
        :param client: The test client used by locust.
        """
        self.hostname = hostname
        self.client = client
        # self.client.auth = BASIC_AUTH_CREDENTIALS

        # self.default_headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Connection': 'keep-alive',
        # }