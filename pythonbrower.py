#2019/08/15 V3.0
import urllib.request
import urllib.parse
import http.cookiejar
import json
import random
import linecache
import re
import gc
import sys
import time
import parsel

class browertab():

	def __init__(self, brower):
		self.brower = brower
		self.url = 'Not url'

	def __repr__(self):
		return '<BrowerTab:'+self.url+'>'

	def post(self , url, data, dataencode=True, headers):
		self.url = url
		request = urllib.request.Request(url=url,headers=headers)
		if dataencode:
			data = urllib.parse.urlencode(data).encode()
		response = self.brower.open(request,data=data)
		self.response = response.read()
		self.headers = response.getheaders()
		return self

	def get(self , url, data,  dataencode=True, headers):
		self.url = url
		if data != None and dataencode:
			data = urllib.parse.urlencode(data)
			requesturl = url+'?'+data
		else:
			requesturl = url
		request = urllib.request.Request(url=requesturl,headers=headers)
		self.response = self.brower.open(request)
		return self

	def getresponse(self, jsondeocde=False):
		try:
			result = self.response.read().decode()
		except:
			try:
				result = self.response.read().decode('gbk')
			except:
				result = self.read().response
		if jsondeocde:
			result = json.loads(result)
		return result

	def getheaders(self):
		return self.response.getheaders()

class Pythonbrower():

	headers = {
		'User-Agent': 'Pythonbrower',
	}

	def __init__(self,ua=False ,randua=True):
		if ua:
			headers['User-Agent'] = ua
		else:
			if randua:
				self.randua(randua)
		self.cj = http.cookiejar.MozillaCookieJar()
		self.cookiehandler = urllib.request.HTTPCookieProcessor(self.cj)
		self.opener = urllib.request.build_opener(self.cookiehandler)

	def __repr__(self):
		return '<Pythonbrower:'+self.headers['User-Agent']+'>'

	def randua(self, randua=True):
		if randua == 'pc':
			f = open('/ua/pc.txt','r', encoding='UTF-8')
			i = -1
			for ua in enumerate(f):
			    i += 1
			self.headers['User-Agent'] = linecache.getline('pc.txt',random.randint(0,i))[:-1]
		elif randua == 'phone':
			f = open('/ua/phone.txt','r', encoding='UTF-8')
			i = -1
			for ua in enumerate(f):
			    i += 1
			self.headers['User-Agent'] = linecache.getline('phone.txt',random.randint(0,i))[:-1]
		elif randua:
			filetxt = random.choice(['/ua/phone','/ua/pc'])+'.txt'
			f = open(filetxt,'r', encoding='UTF-8')
			i = -1
			for ua in enumerate(f):
			    i += 1
			self.headers['User-Agent'] = linecache.getline(filetxt,random.randint(0,i))[:-1]

	def setcookie(self, name, value, domain, path='/'):
		return self.cj.set_cookie(self.__make_cookie(name,value,domain,path))	

	def getcookie(self, name=None, domain=None):
		sendcookie = []
		for cookie in self.cj:
			if name and domain:
				if cookie.name == name and cookie.domain == domain:
					sendcookie.append(cookie)
			elif name and not domain:
				if cookie.name == name:
					sendcookie.append(cookie)
			elif not name and domain:
				if cookie.domain == domain:
					sendcookie.append(cookie)
			else:
				sendcookie.append(cookie)
		return sendcookie

	def savecookie(self, filetxt):
		return self.cj.save(filetxt,ignore_discard=True, ignore_expires=True)

	def loadcookie(self, filetxt):
		return self.cj.load(filetxt,ignore_discard=True, ignore_expires=True)

	def clearcookie(self, domain=None, name=None, path=None):
		if not domain and name:
			clearcookielist = self.getcookie(name=name)
			for clearcookie in clearcookielist:
				if path is None:
					self.cj.clear(clearcookie.domain,clearcookie.path,name)
				else:
					if clearcookie.path == path:
						self.cj.clear(clearcookie.domain,path,name)
		elif domain and name:
			clearcookielist = self.getcookie(name=name,domain=domain)
			for clearcookie in clearcookielist:
				self.cj.clear(clearcookie.domain,clearcookie.path,clearcookie.name)			
		else:
			self.cj.clear(domain,path,name)

	def __make_cookie(self, name, value, domain, path='/'):
	    return http.cookiejar.Cookie(
	        version=0,
	        name=name,
	        value=value,
	        port=None,
	        port_specified=False,
	        domain=domain,
	        domain_specified=True,
	        domain_initial_dot=False,
	        path=path,
	        path_specified=True,
	        secure=False,
	        expires=None,
	        discard=False,
	        comment=None,
	        comment_url=None,
	        rest=None
	    )

	def urlencode(self, data):
		return urllib.parse.quote(data)

	def jsonencode(self, data):
		return json.dumps(data)

	def xpath(self, data, xpath):
		return parsel.Selector(data).xpath(xpath)

class PythonbrowerError(Exception):
    pass