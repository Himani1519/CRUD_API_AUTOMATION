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
fetch_resource = "https://jsonplaceholder.typicode.com/posts"
update_resource = "https://jsonplaceholder.typicode.com/posts/101" 
filtering_resource = "https://jsonplaceholder.typicode.com/posts?userId=1"
delete_resorce = "https://jsonplaceholder.typicode.com/posts/1"
get_user = "https://jsonplaceholder.typicode.com/posts/1"
t = headers()
received_headers = t.headers_dictionary()
#creates user
class test_complete_flow(unittest.TestCase): 

    def test_create_user(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/crud.json") as json_file:
            data = json.load(json_file)
                
                
            payload = data['data'][0]["payload1"]["request_body"]
            title = data['data'][0]["payload1"]["request_body"]["title"]
            body = data['data'][0]["payload1"]["request_body"]["body"]
            userId = data['data'][0]["payload1"]["request_body"]["userId"]
            request_body = json.dumps(payload)
            response = requests.request('POST', create_resource, data=request_body, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(response.json)     

            
            assert response.status_code == 201
            assert json_data["title"] == title
            assert json_data["body"] == body
            assert json_data["userId"] == userId


            if response.status_code == 201 :
                print("User created successfully")
            else:
                print("Failed to create user")

    # validate if user is created
    def test_get_created_user(self):
         with open("/home/himani/Desktop/selenium_python/CRUD/JSON/crud.json") as json_file:
            data = json.load(json_file)
                
                
            title = data['data'][0]["payload1"]["request_body"]["title"]
            body = data['data'][0]["payload1"]["request_body"]["body"]

            response = requests.request('GET', fetch_resource, headers=received_headers)
            data =  response.text                    
            json_data = json.loads(data)
            print(json_data)    

            self.assertTrue(title in json_data)
            self.assertTrue(body in json_data)

    #updte a created user
    def test_update_user(self):
        with open("/home/himani/Desktop/selenium_python/CRUD/JSON/crud.json") as json_file:
            data = json.load(json_file)
                    
            #updating a resorce whose id 101    
            payload = data['data'][1]["payload2"]["request_body"]
            title = data['data'][1]["payload2"]["request_body"]["title"]
            body = data['data'][1]["payload2"]["request_body"]["body"]
            userId = data['data'][1]["payload2"]["request_body"]["userId"]
            request_body = json.dumps(payload)
            response = requests.request('PUT', update_resource, data=request_body, headers=received_headers)
            print(response)
            assert response.status_code == 200

            if response.status_code == 200:
                assert json_data["title"] == title
                assert json_data["body"] == body
                assert json_data["userId"] == userId
                assert json_data["id"] == 101
            else:
                print("Not able to update user with id 101 gives error,",response.status_code)

    # filter the user
    def test_filtering_resource(self):
        response = requests.request('GET', filtering_resource, headers=received_headers)
        data =  response.text                    
        json_data = json.loads(data)
        print(json_data)   
        userId = json_data[0]["userId"]
        assert userId == 1

    #deletes the user
    def test_delete_resorce(self):
        response = requests.request('DELETE', delete_resorce, headers=received_headers)
        data =  response.text                    
        json_data = json.loads(data)
        print(json_data)   
        assert response.status_code == 200

    #check deleted user
    def test_deleted_user(self):

        response = requests.request('GET', get_user, headers=received_headers)
        data =  response.text                    
        json_data = json.loads(data)
        print(json_data)   
        assert json_data == None



          


if __name__ == '__main__':
    unittest.main()