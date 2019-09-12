#!/usr/bin/env python
# coding=utf-8

import requests,json
import time
# import redis


def request_decorator(fun):
    def wraper():
        try:
            res=fun()
        except requests.exceptions.ConnectTimeout:
            print("request time out!")
#            res=json.load("{error:ddConnect timeout}")
        except requests.exceptions.ReadTimeout:
            print("request readtimeout!")
        except requests.exceptions.ConnectionError:
            print("request ConnectionError!")
        except requests.exceptions.ProxyError:
            print("request ProxyError")
        except requests.exceptions.ConnectionError:
            print("request Connection Error!")
        except Exception as e:
            print("request Error!")
            

def toJsonWrapper(func):
    try:
        res=func()
    except Exception as e:
        print(e)

def jsonToStr(func):
    try:
        res=func()
    except Exception as e:
        print(e)
    return res


class Fetcher:
    def __init__(self):
        fetcher=requests
    
    @request_decorator
    def fetch_one_by_get(self,url):
        self.fetcher.get(url)

    
    @request_decorator
    def fetch_one_by_post(self,url,body):
        self.fetcher.post(url,body)

    #make it become multi thread
    def fetch_batch_by_get(self,url_li):
        res={"method":"GET","total":0,"url_list":{}}
        for i in range(len(url_li)):
            k=url_li[i]
            r=fetch_one_by_get(k)
            res["url_list"][k]=v
    return res

    def fetch_batch_by_post(self，url_li,body):
        res={"body":body,"method":"POST","total":0,"url_list":{}}
        for i in range(len(url_li)):
            k=url_li[i]
            v=fetch_one_by_post（key,body）
            res["url_list"][key]=v
        retrun res


