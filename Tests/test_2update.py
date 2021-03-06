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


update_resource = "https://jsonplaceholder.typicode.com/posts/8"
t = headers()
received_headers = t.headers_dictionary()

class test_update_api(unittest.TestCase): 

    def test_updateExisting_user(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/update.json") as json_file:
            json_data = json.load(json_file)
                    
                    
            payload = json_data['data'][0]["payload1"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('PUT', update_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)   

            #validate response time
            responseTime = response.elapsed.total_seconds()
            print(response.elapsed.total_seconds())
            assert responseTime <= 2

            assert json_data["title"] == "xyz"
            assert json_data["body"] == "testing"
            assert json_data["userId"] == "101"
            assert json_data["id"] == 8
            assert response.status_code == 200

    def test_update_user_empty_value(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/update.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data['data'][1]["payload2"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('PUT', update_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code != 200
           
            if response.status_code == 200 :
                print("Error: User should not allow to update empty key values")
            else:
                print("Pass: Not able to update user with empty values in request body")


            
    def test_different_type_in_request(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/update.json") as json_file:
            json_data = json.load(json_file)
                
                
            payload = json_data["data"][2]["payload3"]["request_body"]
            request_body = json.dumps(payload)
            response = requests.request('PUT', update_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     
           
            assert response.status_code != 200
            
            if response.status_code == 200 :
                print("Error: If passing null/boolean,integer in json values still gives response")
            else:
                print("Pass: Not able to update user with invalid request body")



    def test_empty_request(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/update.json") as json_file:
            json_data = json.load(json_file)
                    
                    
            response = requests.request('PUT', update_resource, data="", headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code != 200
            

            if response.status_code == 200 :
                print("Error: update user with empty payload")
            else:
                print("Pass: Not able to create user with empty paload")

                

    def test_invalid_json_body(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/update.json") as json_file:
            json_data = json.load(json_file)
                    
            payload1 = json_data["data"][3]["payload4"]["request_body"]
            request_body = json.dumps(payload1)
                    
            response = requests.request('PUT', update_resource, data=request_body, headers=received_headers)
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
