import http.cookiejar

cookiejar = http.cookiejar.FileCookieJar('123',delayload=True)
print(cookiejar.filename)