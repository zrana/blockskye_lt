from BlockSkyeBase import BlockSkyeBase
import json


class ApplicationFlow(BlockSkyeBase):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(ApplicationFlow, self).__init__(*args, **kwargs)

        self.headers = {
            "Authorization": "Bearer 1|JwjHRaWmNLKo6G8PVWo63JaiDasTo4tuYjn70U20",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """

        if response.status_code != 200:
            raise Exception(
                'AddPI request failed with following error code: ' +
                str(response.status_code)
            )

    def create_profile(self, email, username):

        url = self.hostname + '/api/v1/profile/create?employee_id=' + username + '&employer_id=1'
        registration_params = {
            "email": email,
            "name": username
        }

        response = self.client.post(url, json=registration_params, headers=self.headers, name="Create User Profile")
        self._check_response(response)
        return response

    def update_profile(self, employee_id, new_user_email, new_username):
        url = self.hostname + '/api/v1/profile/update?employee_id=' + employee_id + '&employer_id=1'
        bodyParams = {
            "name": new_username,
            "email": new_user_email
        }
        response = self.client.put(url, json=bodyParams, headers=self.headers, name="Update User Profile")
        self._check_response(response)

        return response

    def get_profile(self, employee_id):
        url = self.hostname + '/api/v1/profile/get?employee_id=' + employee_id + '&employer_id=1'
        response = self.client.get(url, headers=self.headers, name="Get User Profile")
        self._check_response(response)

        return response

    def initial_form_request(self, employee_id):
        url = self.hostname + '/api/v1/expense_approval/checkout_form?employee_id=' + employee_id + '&employer_id=1'
        response = self.client.get(url, headers=self.headers, name="Initial form request")
        self._check_response(response)

        return response

    def wbs_code_lookup(self, employee_id):
        url = self.hostname + '/api/v1/expense_approval/job_codes?employee_id=' + employee_id + '&employer_id=1&search_query=Google'
        response = self.client.get(url, headers=self.headers, name="WBS code lookup")
        self._check_response(response)

        return response

    def delete_profile(self, employee_id):
        url = self.hostname + '/api/v1/profile/delete?employee_id=' + employee_id + '&employer_id=1'
        response = self.client.delete(url, headers=self.headers, name="Delete profile")
        self._check_response(response)

        return response

    def create_expense(self):
        url = self.hostname + '/api/v1/expense_approval/create'
        bodyParams = {
            "employee_id": "00300232877",
            "employer_id": "1",
            "total_amount": 2000,
            "form_of_payment": "BSK",
            "wbs_codes": [
                {
                    "wbs_element": "80124045001",
                    "amount": 2000,
                    "allocation": "100",
                    "tax_status": "taxable",
                    "expense_type": "airfare",
                    "reason": "testing first",
                    "wbsDescription": "testing one",
                    "clientName": "Google",
                    "billingManager": "John",
                    "billingPartner": "Doe",
                    "engagementManager": "Elon",
                    "engagementPartner": "William"
                }
            ]
        }
        response = self.client.post(url, json=bodyParams, headers=self.headers, name="Create Expense")
        self._check_response(response)
        # import pdb
        # pdb.set_trace()
        return response

    def add_ticket_data(self, expense_approval_id, account_number):
        url = self.hostname + '/api/v1/test/expense_approval/' + expense_approval_id
        bodyParams = {
            "airSegments": [
                {
                    "aircraftTypeCode": "37C",
                    "airlineReference": "TEST45",
                    "bookingClass": "F",
                    "carrier": "UA",
                    "departureDateTimeTZ": "2022-07-03T17:05:00-05:00",
                    "origin": "ORD",
                    "flightNumber": 1133,
                    "itemID": 1234567890,
                    "operatingCarrier": "UA",
                    "operatingFlightNumber": 1133,
                    "segmentStatus": "HK",
                    "arrivalDateTimeTZ": "2022-07-04T19:24:00+05:00",
                    "destination": "BOS",
                    "arrivalGate": "5",
                    "departureGate": "2"
                } 
            ],
            "travellers": {
                "firstName": "Usman",
                "lastName": "Chughtai",
                "itemID": 1,
                "passengerType": "government",
                "title": "Mr",
                "emailAddress":"usman.chughtai@blockskye.com",
                "phoneNumber":"+144566543455",
                "employeeID": "00300340746",
                "employer":"PwC"
            },
            "serviceRequests": {
                "itemID": 1,
                "passengerID": 1,
                "requestCode": "0007",
                "requestText": "bacon, black coffee, chilled orange juice, toast, marmalade and scrambled eggs",
                "segmentID": 1,
                "statusCode": "HK"
            },
            "tripID": "ASDF1234",
            "remarks": {
                "remarkCode": "01",
                "remarkText": "top secret"
            },
            "sourceInfo": {
                "agencyID": "KAYAK1",
                "bookingOffice": "KAYAK",
                "creationDate": "05-10-2021",
                
                "sourceReference": "1234ASDF",
                "arranger": {
                    "arrangerEmail": "usman.chughtai@arbisoft.com",
                    "arrangerEmployeeId": "01628315001",
                    "arrangerName": "Mr. Arranger"
                }
            },
            "ticket":{
                "Sale":[{
                        "expenseID": expense_approval_id,
                        "dateOfIssue": "2022-05-28",
                        "documentNumber": "123456123456",
                        "agencyCode": "10779613",
                        "airlineCarrierCode": "016",
                        "payments": [{
                            "accountNumber": account_number,
                            "formOfPaymentAmount": {
                                "amount": 100000,
                                "currency": "USD",
                                "precision": 2
                            }
                        }],
                        "prices": {
                            "baseFareAmount": {
                                "amount": 200000,
                                "currency": "USD",
                                "precision": 2
                            },
                            "ticketDocumentAmount": {
                                "amount": 2000,
                                "currency": "USD",
                                "precision": 2
                            }
                        },
                        "taxes": {
                            "value": {
                                "amount":100,
                                "currency":"USD",
                                "precision":10
                            }
                        },
                        "fees": {
                            "value": {
                                "amount":700,
                                "currency":"USD",
                                "precision":100
                            }
                        },
                        "passenger": {
                            "firstName": "Usman",
                            "lastName": "Chughtai"
                        }
                }]
            }
        }

        with self.client.put(url, json=bodyParams, headers=self.headers, name="Adding Ticket data", catch_response=True) as response:
            if response.status_code == 404:
                response.success()
    
        self._check_response(response)
        return response

    def get_expense(self, expense_approval_id):
        url = self.hostname + '/api/v1/expense/get_expense/' + expense_approval_id

        with self.client.get(url, headers=self.headers, name="Get Expense", catch_response=True) as response:
            if response.status_code == 503:
                response.success()
            while response.status_code == 503:
                with self.client.get(url, headers=self.headers, name="Get Expense", catch_response=True) as response:
                    if response.status_code == 503:
                        response.success()
        
        self._check_response(response)
        return response

    def get_calendar(self, employee_id):
        url = self.hostname + '/api/v1/calendar-integration/status?employee_id=' + employee_id + '&employer_id=1'
        response = self.client.get(url, headers=self.headers, name="Get Calendar Status")
        self._check_response(response)
        return response

