from .variables import username,password
import time
import os
import requests
from django.shortcuts import render,HttpResponse
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR,HTTP_504_GATEWAY_TIMEOUT,HTTP_200_OK

# Create your views here.
def create_environment_variables():
    os.environ['MOVIE_API_USERNAME']=username 
    os.environ['MOVIE_API_PASSWORD']=password

def login_details():
    url='https://demo.credy.in/api/v1/maya/movies/'

    api_username=os.environ['MOVIE_API_USERNAME']
    api_password=os.environ['MOVIE_API_PASSWORD']
    
    headers={username:api_username,
             password:api_password}
    
    return url,headers

def check_response(response,url,headers):
    retry=1
    max_retries=5
    print("here")
    while(retry!=max_retries):
        print(f"error with status code={response.status_code} occured")
        time.sleep(2)
        response=requests.get(url=url,headers=headers)
        print(response.status_code)
        if(response.status_code==HTTP_200_OK):
            
            retry=max_retries
        else:
            print(f"retries ={retry}")
            retry+=1
    return response.text

def movies_api(request):
    url,headers=login_details()
    
    if(request.method=='GET'):
        retry=0
        response=requests.get(url=url,headers=headers)
        response_text=response.text
        if(response.status_code==HTTP_500_INTERNAL_SERVER_ERROR or response.status_code==HTTP_504_GATEWAY_TIMEOUT):
            response_text=check_response(response=response,url=url,headers=headers)
        return(HttpResponse(response_text))

def get_more_movies(request,id):

    url,headers=login_details()
    if(id>1):
        url=url+f"?page={id}"

    if(request.method=='GET'):
        response=requests.get(url=url,headers=headers)
        response_text=response.text
        if(response.status_code==HTTP_500_INTERNAL_SERVER_ERROR or response.status_code==HTTP_504_GATEWAY_TIMEOUT):
            response_text=check_response(response=response,url=url,headers=headers)

        return(HttpResponse(response_text))
                           
