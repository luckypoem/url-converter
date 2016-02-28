# 真实地址 迅雷 QQ旋风 快车地址转换
# 2016-02-28 11:03:44
# 2.0
# 使用Python库函数进行base64编码解码，使用utf-8进行字符串编码，进而增加了对中文的支持
import base64
def qqxf(url):
	"""
	将真实地址转换为QQ旋风地址
	# 输入	真实地址
	# 输出	QQ旋风地址
	"""
	return b'qqdl://' + base64.b64encode(url)
def thunder(url):
	"""
	将真实地址转换为迅雷地址
	# 输入	真实地址
	# 输出	迅雷地址
	"""
	return b'thunder://' + base64.b64encode(b'AA' + url + b'ZZ')
def flashget(url):
	"""
	将真实地址转换为快车地址
	# 输入	真实地址
	# 输出	快车地址
	"""
	return b'flashget://' + base64.b64encode(b'[FLASHGET]' + url + b'[FLASHGET]')
def urlConvert(url):
	"""
	将任意地址转换为真实地址
	# 输入	任意地址
	# 输出	真实地址
	"""
	if url[0: 7] == 'qqdl://':
		base64Str = url[7:]
		trueUrl = base64.b64decode(base64Str)
	elif url[0: 10] == 'thunder://':
		base64Str = url[10:]
		trueUrl = base64.b64decode(base64Str)
		trueUrl = trueUrl[2:]
		trueUrl = trueUrl[:-2]
	elif url[0: 11] == 'flashget://':
		base64Str = url[11:]
		trueUrl = base64.b64decode(base64Str)
		trueUrl = trueUrl[10:]
		trueUrl = trueUrl[:-10]
	else:
		trueUrl = url.encode('utf-8')
	return trueUrl
def outputUrl(url):
	"""
	将真实地址转换为任意地址并输出
	# 输入	真实地址
	# 输出	将任意地址打印
	"""
	trueUrl = urlConvert(url)
	print("真实-> " + trueUrl.decode('utf-8'))
	print("旋风-> " + qqxf(trueUrl).decode('utf-8'))
	print("迅雷-> " + thunder(trueUrl).decode('utf-8'))
	print("快车-> " + flashget(trueUrl).decode('utf-8'))
print('欢迎使用「真实地址 迅雷 QQ旋风 快车地址转换」2.0版本, 支持中文喽！')
print('详情请访问主页: https://github.com/note286/urlConvert')
inputURL = input("URL:-> ")
outputUrl(inputURL)