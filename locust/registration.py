from ADGBase import ADGBase


class Registration(ADGBase):

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(Registration, self).__init__(*args, **kwargs)

    def _check_response(self, response):

        print('*** response ***')
        print(response)
        """
        Check whether a response was successful.
        """
        if response.status_code not in 200:
            raise Exception(
                'AddPI request failed with following error code: ' +
                str(response.status_code)
            )

    # def visit_registration_page(self):
    #     url = "https://courses.omnipreneurshipacademy.com/register"
    #     response = self.client.get(url)
    #     token = response.cookies['csrftoken']
    #
    #     headers = {
    #         'Origin': "https://courses.omnipreneurshipacademy.com",
    #         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Referer': self.hostname,
    #         'Connection': 'keep-alive',
    #         'Cookie': "csrftoken={}".format(token)
    #     }
    #
    #     response = self.client.get(url, headers=headers)
    #     self._check_response(response)
    #     return response

    def register(self, email, username):
        url = self.hostname + '/api/v1/profile/create?employee_id=' + username + '&employer_id=1'
        print(url)
        #response = self.client.post(url)
        #token = response.cookies['csrftoken']
        registration_params = {
            "email": email,
            "name": username
        }
        headers = {
            "Authorization": "Bearer 1|JwjHRaWmNLKo6G8PVWo63JaiDasTo4tuYjn70U20",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        print(registration_params)
        print(headers)
        response = self.client.post(url, json=registration_params, headers=headers, name="Create User Profile")
        self._check_response(response)
        return response

    def expense_approval(self):
        url = self.hostname + '/api/v1/expense_approval/create'
        registration_params = {
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
        headers = {
            "Authorization": "Bearer 1|JwjHRaWmNLKo6G8PVWo63JaiDasTo4tuYjn70U20",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        response = self.client.post(url, json=registration_params, headers=headers, name="Expense Approval")
        print('*** response *** 33333 ***')
        print(response.text)
        self._check_response(response)

        return response

    def add_ticket_data(self, response):
        url2 = self.hostname + 'api/v1/test/expense_approval/' + response.data.expense_approval_id

        print(url2)

        registration_params2 = {
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
                        "expenseID": response.data.expense_approval_id,
                        "dateOfIssue": "2022-04-28",
                        "documentNumber": "123456123456",
                        "agencyCode": "10779613",
                        "airlineCarrierCode": "016",
                        "pnrReference":"TEST45",
                        "payments": [{
                            "accountNumber": response.data.suvtpNumber.accountNumber,
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

        headers = {
            "Authorization": "Bearer 1|JwjHRaWmNLKo6G8PVWo63JaiDasTo4tuYjn70U20",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }


        response2 = self.client.put(url2, json=registration_params2, headers=headers, name="Adding Ticket data")
        print('*** response *** 4444444 ***')
        print(response2.text)
        self._check_response(response2)

