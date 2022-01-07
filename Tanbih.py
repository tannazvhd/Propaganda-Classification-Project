from __future__ import print_function
import swagger_client
import requests
import json
from swagger_client.rest import ApiException
from pprint import pprint
###################################################################
# def get_key(text):
#     # create an instance of the API class
#     api_instance = swagger_client.DefaultApi()
#     text = text # str |  (optional)

#     try:
#         api_response = api_instance.article_propaganda_sentences_post(text=text)
#         #pprint(api_response["key"])
#         return api_response["key"]
#     except ApiException as e:
#         print("Exception when calling DefaultApi->article_propaganda_sentences_post: %s\n" % e)

##key = get_key("test this sample") 
#####################################################################

def get_key(text):
    headers = {
        "accept": "application/json",
        "Content-Type" : "multipart/form-data"
    }
    url = "http://webapi.tanbih.org/article/propaganda/sentences"

    response = requests.post(url, headers=headers, data= text)
    result = response.json()
    print(result)
 
get_key("test this sample") 
#####################################################################

def propaganda_estimation(key):
    headers = {
        "accept": "application/json",
    }
    url = "http://webapi.tanbih.org/article/propaganda/sentences?key={0}".format(key)

    response = requests.get(url, headers=headers)
    result = response.json()["sentence_propaganda"][0]["confidence"]
    #print(result)
    return result
####################################################################
# test = propaganda_estimation(get_key("test this sample"))
# print(test)
