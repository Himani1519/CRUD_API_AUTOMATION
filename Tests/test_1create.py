import unittest
import requests
from headers import headers
import json
import random
import csv
import os.path
from time import gmtime, strftime
import glob
import pandas as pd
from datetime import datetime
import time
import pytest


create_resource = "https://jsonplaceholder.typicode.com/posts"
t = headers()
received_headers = t.headers_dictionary()

class test_create_api(unittest.TestCase): 

    def test_create_user(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data['data'][0]["payload1"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            assert response.status_code == 201
            #validate response time
            responseTime = response.elapsed.total_seconds()
            print(response.elapsed.total_seconds())
            assert responseTime <= 2

            if response.status_code == 201 :
                print("User created successfully")
            else:
                print("Failed to create user")

    def test_exiting_user(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data['data'][0]["payload1"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code != 201
            

            if response.status_code == 201 :
                print("Error creates Existing user")
            else:
                print("Pass user is not able to create existing user")

                



    def test_empty_value(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data['data'][1]["payload2"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code != 201
           
            if response.status_code == 201 :
                print("Error: User creates with empty key values")
            else:
                print("Pass: Not able to create user with empty values in request body")


            
    def test_different_type_in_request(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data["data"][2]["payload3"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     
           
            assert response.status_code != 201
            
            if response.status_code == 201 :
                print("Error: If passing null/boolean,integer in json values still gives response")
            else:
                print("Pass: Not able to create user with invalid request body")



    def test_empty_request(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                    
                    
            response = requests.request('POST', create_resource, data="", headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code != 201
            

            if response.status_code == 201 :
                print("Error: Create user with empty payload")
            else:
                print("Pass: Not able to create user with empty paload")

                

    def test_invalid_json_body(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/create.json") as json_file:
            json_data = json.load(json_file)
                    
            payload1 = json_data["data"][3]["payload4"]["request_body"]
            request_body = json.dumps(payload1)
                    
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     
            
            assert response.status_code == 400
            

            if response.status_code == 400 :
                print("Pass: If user pass invalid json body its giving 400 bad request")
            else:
                print("Error:: It should not give 500 intrrnal server error  ")




        




             
               
                
if __name__ == '__main__':
    unittest.main()
