# 真实地址 迅雷 QQ旋风 快车地址转换
# 2016-03-15 22:21:03
# 2.1
# 增加了对中文 GBK 编码的识别
import base64
def qqxf(url):
	"""
	将真实地址转换为QQ旋风地址
	# 输入	真实地址
	# 输出	QQ旋风地址
	"""
	return b'qqdl://' + base64.b64encode(url.encode('utf-8'))
def thunder(url):
	"""
	将真实地址转换为迅雷地址
	# 输入	真实地址
	# 输出	迅雷地址
	"""
	return b'thunder://' + base64.b64encode(b'AA' + url.encode('utf-8') + b'ZZ')
def flashget(url):
	"""
	将真实地址转换为快车地址
	# 输入	真实地址
	# 输出	快车地址
	"""
	return b'flashget://' + base64.b64encode(b'[FLASHGET]' + url.encode('utf-8') + b'[FLASHGET]')
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

	# 识别编码编码是utf-8还是gbk, 然后将其对应的字符串赋值给trueUrlUtf_8
	trueUrl = urlConvert(url)
	try:
		trueUrl.decode('utf-8')
	except UnicodeDecodeError as e:
		trueUrlUtf_8 = trueUrl.decode('gbk')
	else:
		trueUrlUtf_8 = trueUrl.decode('utf-8')
	finally:
		pass

	# 在qqxf(), thunder(), flashget()中均采用utf-8对字符串进行编码

	print("真实-> " + trueUrlUtf_8)
	print("旋风-> " + qqxf(trueUrlUtf_8).decode('utf-8'))
	print("迅雷-> " + thunder(trueUrlUtf_8).decode('utf-8'))
	print("快车-> " + flashget(trueUrlUtf_8).decode('utf-8'))
print('欢迎使用「真实地址 迅雷 QQ旋风 快车地址转换」2.1版本, 支持中文喽！(可识别 utf-8 和 GBK 编码)')
print('详情请访问主页: https://github.com/note286/urlConvert')
inputURL = input("URL:-> ")
outputUrl(inputURL)