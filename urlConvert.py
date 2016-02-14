# 真实地址 迅雷 QQ旋风 快车地址转换
# 2016-02-13 11:19:26
# 1.1
# 修复了ftp协议识别错误的bug
def hex2bin(hexChar):
	"""
	将一个16进制的字符转换为一个4bit的二进制
	不足4bit前面补0
	# 输入	一个字符，含义为一个16进制数
	# 输出	4bit01字符串，含义为4bit二进制数
	"""
	tempString = str(bin(int(hexChar, 16)))
	tempBinString = tempString[2: 6]
	resultBinString = ''
	stringLength = 4 - len(tempBinString)
	if stringLength == 0:
		pass
	elif stringLength == 1:
		resultBinString += '0'
	elif stringLength == 2:
		resultBinString += '00'
	elif stringLength == 3:
		resultBinString += '000'
	elif stringLength == 4:
		resultBinString += '0000'
	resultBinString += tempBinString
	return resultBinString
def hexStr2binStr(hexString):
	"""
	将一个16进制的字符串转换为一个二进制字符串
	其中每个16进制数转换为4bit的二进制
	不足4bit前面补0
	# 输入	一个字符串，含义为16进制数序列
	# 输出	一个字符串，含义为输入对应的二进制序列
	"""
	resultBinStr = ''
	for x in range(0,len(hexString)):
		resultBinStr += hex2bin(hexString[x])
	return resultBinStr
def binStr2Base64(binString):
	"""
	将二进制字符串转换为Base64编码的字符串
	其中binString的长度必须为偶数
	# 输入	一个字符串，含义为二进制序列
	# 输出	一个字符串，含义为输入对应的Base64编码
	"""
	Base64List = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','=']
	resultBase64 = ''
	lastNum = len(binString) % 6
	if lastNum == 0:
		pass
	elif lastNum == 2:
		binString += '0000'
	elif lastNum == 4:
		binString += '00'
	else:
		print("binString的长度不为偶数!")
		return False
	for x in range(0,len(binString)//6):
		resultBase64 += Base64List[int(binString[x * 6: x * 6 + 6], 2)]
	if lastNum == 0:
		pass
	elif lastNum == 2:
		resultBase64 += '=='
	elif lastNum == 4:
		resultBase64 += '='
	return resultBase64
def char2Hex(char):
	"""
	将一个字符对应的ANSCII转换为对应的16进制
	每个字符对应2位的16进制数
	# 输入	一个字符
	# 输出	一个16进制数
	"""
	charASCII = ord(char)
	hexChar = hex(charASCII)
	return hexChar
def str2Hex(Str):
	"""
	将字符串转换为16进制序列
	每个字符对应2位的16进制数
	# 输入	字符串
	# 输出	16进制序列
	"""
	hexStr = ''
	for x in range(0, len(Str)):
		hexStr += str(char2Hex(Str[x]))[2: 4]
	return hexStr
def qqxf(url):
	"""
	将真实地址转换为QQ旋风地址
	# 输入	真实地址
	# 输出	QQ旋风地址
	"""
	return 'qqdl://' + binStr2Base64(hexStr2binStr(str2Hex(url)))
def thunder(url):
	"""
	将真实地址转换为迅雷地址
	# 输入	真实地址
	# 输出	迅雷地址
	"""
	return 'thunder://' + binStr2Base64(hexStr2binStr(str2Hex('AA' + url + 'ZZ')))
def flashget(url):
	"""
	将真实地址转换为快车地址
	# 输入	真实地址
	# 输出	快车地址
	"""
	return 'flashget://' + binStr2Base64(hexStr2binStr(str2Hex('[FLASHGET]' + url + '[FLASHGET]')))
def dec2Bin(dec):
	"""
	将十进制数转换为对应的6bit二进制
	# 输入	0~63十进制数
	# 输出	6bit二进制数
	"""
	binValue = bin(dec)
	binValue = binValue[2:]
	zeroStr = ''
	for x in range(1, 6 - len(binValue) + 1):
		zeroStr += '0'
	return zeroStr + binValue
def base642BinStr(base64Str):
	"""
	将Base64编码的字符串转换为二进制字符串
	# 输入	Base64编码的字符串
	# 输出	二进制字符串
	"""
	if base64Str[-1] != '=':
		equalSignNum = 0
	elif base64Str[-2] == '=':
		equalSignNum = 2
		base64Str = base64Str[: -2]
	else:
		equalSignNum = 1
		base64Str = base64Str[: -1]
	decList = []
	Base64List = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','=']
	for x in range(0, len(base64Str)):
		decList.append(Base64List.index(base64Str[x]))
	binList = ''
	for x in range(0, len(decList)):
		binList += str(dec2Bin(decList[x]))
	if equalSignNum == 1:
		binList = binList[: -2]
	elif equalSignNum == 2:
		binList = binList[: -4]
	return binList
def binStr2DecList(binStr):
	"""
	将二进制序列以8个一组转换为十进制数组
	# 输入	二进制序列
	# 输出	十进制数组
	"""
	if len(binStr) % 8 != 0:
		print("binStr length error!")
		return False
	decList = []
	for x in range(0, int(len(binStr) / 8)):
		tempBinNum = binStr[x * 8: x * 8 + 8]
		decList.append(int(tempBinNum, 2))
	return decList
def decList2Str(decList):
	"""
	十进制数组转换为对应ANSCII的字符串
	# 输入	十进制数组
	# 输出	字符数组
	"""
	Str = ''
	for x in range(0, len(decList)):
		Str += chr(decList[x])
	return Str
def base642Str(base64Str):
	"""
	将Base64编码的字符串转换为字符串
	# 输入	Base64编码的字符串
	# 输出	字符串
	"""
	return decList2Str(binStr2DecList(base642BinStr(base64Str)))
def urlConvert(url):
	"""
	将任意地址转换为真实地址
	# 输入	任意地址
	# 输出	真实地址
	"""
	if url[0: 7] == 'qqdl://':
		base64Str = url[7:]
		trueUrl = base642Str(base64Str)
	elif url[0: 10] == 'thunder://':
		base64Str = url[10:]
		trueUrl = base642Str(base64Str)
		trueUrl = trueUrl[2:]
		trueUrl = trueUrl[:-2]
	elif url[0: 11] == 'flashget://':
		base64Str = url[11:]
		trueUrl = base642Str(base64Str)
		trueUrl = trueUrl[10:]
		trueUrl = trueUrl[:-10]
	else:
		trueUrl = url
	return trueUrl
def outputUrl(url):
	"""
	将真实地址转换为任意地址并输出
	# 输入	真实地址
	# 输出	将任意地址打印
	"""
	trueUrl = urlConvert(url)
	print("真实-> " + trueUrl)
	print("旋风-> " + qqxf(trueUrl))
	print("迅雷-> " + thunder(trueUrl))
	print("快车-> " + flashget(trueUrl))
inputURL = input("URL:-> ")
outputUrl(inputURL)