import urllib
import http.cookiejar
#支持各类cookies操作,代理设置，重定向设置

class browerTab(object):
	"""docstring for browertab"""
	def __init__(self, arg):
		super(browertab, self).__init__()
		self.arg = arg

class cookiesApp(object):
	def __init__(self):
		#初始化CookieJar
		self.cookieJar = http.cookiejar.FileCookieJar()

	#创建cookie对象
	def __makeCookie(self, name, value, domain, path='/'):
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

	#设置Cookie
	def setCookie(self, name, value, domain, path='/', ifpolicy=False):
		if policy:
			return self.cookieJar.set_cookie_if_ok(self.__make_cookie(name,value,domain,path))
		else:
			return self.cookieJar.set_cookie(self.__make_cookie(name,value,domain,path))

	#获取指定Cookie
	def getcookie(self, name=None, domain=None, path=None):
	sendcookie = []
	for cookie in self.cookieJar:
		if name and cookie.name != name:
			continue
		if domain and cookie.domain != domain:
			continue
		if path and cookie.path != path:
			continue
		sendcookie.append(cookie)
	return sendcookie

	#保存Cookie到指定位置
	def save(self, filename, ignore_discard=True, ignore_expires=True):
		return self.cookieJar.save(filename,ignore_discard, ignore_expires)

	#加载指定位置Cookies
	def load(self, filename, ignore_discard=True, ignore_expires=True):
		return self.cookieJar.load(filename,ignore_discard, ignore_expires)

	def clearcookie(self, domain=None, name=None, path=None):
		if domain:
			if name:
				if path:
					self.cookieJar.clear(domain,path,name)
				else:
					cookielist = self.getcookie(domain=domain, name=name)
					for clearcookie in cookielist:
						self.cookieJar.clear(domain,clearcookie.path,name)
			else:
				if path:
					self.cookieJar.clear(domain, path)
				else:
					self.cookieJar.clear(domain)
		else:
			if name:
				if path:
					cookielist = self.getcookie(path=path, name=name)
					for clearcookie in cookielist:
						self.cookieJar.clear(clearcookie.domain,path,name)
				else:
					cookielist = self.getcookie(name=name)
					for clearcookie in cookielist:
						self.cookieJar.clear(clearcookie.domain,clearcookie.path,name)					
			else:
				if path:
					cookielist = self.getcookie(path=path)
					for clearcookie in cookielist:
						self.cookieJar.clear(clearcookie.domain,path,clearcookie.name)						
				else:
					self.cookieJar.clear()
		
class redirectAPP(object):
	"""docstring for redirectAPP"""
	def __init__(self, arg):
		super(redirectAPP, self).__init__()
		self.arg = arg
		

class pythonBrower(object):
	"""docstring for pythonbrower"""
	def __init__(self, arg):
		super(pythonbrower, self).__init__()
		self.arg = arg

	def addHandler(self):


	def cookiesHandler(self):

	def redirectHandler(self):

	def proxyHandler(self):
		