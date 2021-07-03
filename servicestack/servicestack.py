import json
import os
import pathlib
import platform
import dataclasses

from marshmallow.fields import Method
from servicestack.client_dtos import IDelete, IGet, IPatch, IPost, IPut, IReturn, IReturnVoid

from typing import TypeVar, Generic, Optional, Dict, List, Tuple, get_args, Any
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, Undefined
from urllib.parse import urljoin, urlencode, quote_plus
import inspect
import typing
import requests


def dump(obj):
  print("")
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))
  print("")

def _resolve_response_type(request):
    if (isinstance(request, IReturn)):
        for cls in request.__orig_bases__:
            if (hasattr(cls,'__args__')):
                return cls.__args__[0]
    if (isinstance(request, IReturnVoid)):
        return type(None)
    return None

def _resolve_http_method(request):
    if (isinstance(request, IGet)):
        return "GET"
    if (isinstance(request, IPost)):
        return "POST"
    if (isinstance(request, IPut)):
        return "PUT"
    if (isinstance(request, IPatch)):
        return "PATCH"
    if (isinstance(request, IDelete)):
        return "DELETE"
    return "POST"

def nameof(instance):
    return type(instance).__name__

def qsvalue(arg):
    if (not arg): return ""
    if (arg is str):
        return urlencode(arg,quote_via=quote_plus)
    return arg

def append_query_string(url:str, args:dict[str,Any]):
    if (args):
        for key in args:
            val = args[key]
            if (val is None): continue
            url += '&' if '?' in url else '?'
            url += key + '=' + qsvalue(val)
    return url

def has_request_body(method:str):
    return not (method == "GET" or method == "DELETE" or method == "HEAD" or method == "OPTIONS")

@dataclass
class SendContext:
    url: str = None
    request: IReturn = None
    method: str = None
    params: dict[str,str] = None
    headers: dict[str,str] = None
    response_as: type = None

class JsonServiceClient:
    base_url: str = None
    reply_base_url: str = None
    oneway_base_url: str = None
    headers: dict[str,str] = None
    bearer_token: str = None
    username: str = None
    password: str = None

    def __init__(self,base_url):
        if (not base_url):
            raise TypeError(f"base_url is required")
        self.base_url = base_url
        self.reply_base_url = urljoin(base_url,'json/reply') + "/"
        self.oneway_base_url = urljoin(base_url,'json/oneway') + "/"
        self.headers = { 'Accept': 'application/json' }

    def create_url_from_dto(self, method:str, request:Any):
        url = urljoin(self.reply_base_url, nameof(request))
        if (not has_request_body(method)):
            url = append_query_string(url, request.__dict__)
        return url

    def get(self,request,args=None):
        return self.send(request,"GET",args)

    def send(self,request,method,args=None):
        if (not isinstance(request, IReturn) and not isinstance(request, IReturnVoid)):
            raise TypeError(f"'{nameof(request)}' does not implement IReturn or IReturnVoid")

        return_type = _resolve_response_type(request)
        if (return_type is None):
            raise TypeError(f"Could not resolve Response Type for '{nameof(request)}'")

        return self.send_request(SendContext(
            request=request,
            method=method or _resolve_http_method(request),
            response_as=return_type))

    def send_request(self,info:SendContext):
        status_code = -1
        
        # try:
        url = info.url
        if (not url):
            url = urljoin(self.reply_base_url, nameof(info.request))
            url = append_query_string(url, info.request.__dict__)
        else:
            url = self.create_url_from_dto(info.method,info.request)

        if (not url):
            raise TypeError

        if (info.params):
            url = append_query_string(url, info.params)

        response = requests.get(url, headers=self.headers)
        json = response.text

        res_dto = info.response_as.schema().loads(json)

        return res_dto

        # except Exception as e:
        #     print(f"ERROR: {e.__class__}")


        
