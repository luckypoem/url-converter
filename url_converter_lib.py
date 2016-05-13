import base64
def urlConvert(url):
    """将任意地址转换为真实地址
    Arguement:
        url, str, 用户输入的 URL
    Return:
        没有异常: bytes, 对应的真实 URL, 且是 utf-8 编码
        存在异常: int, 0, 由于用户不合法的输入导致
    """
    try:
    # 对于能转化成 str 的输入进行转化
        url = str(url)
    except:
        return 0

    if url[0: 7] == 'qqdl://':
    # QQ 旋风
        base64Str = url[7:]
        # 提取协议后的载荷字符串
        try:
            trueUrl = base64.b64decode(base64Str)
        except:
            return 0
    elif url[0: 10] == 'thunder://':
    # 迅雷
        base64Str = url[10:]
        # 提取协议后的载荷字符串
        try:
            trueUrl = base64.b64decode(base64Str)
        except:
            return 0
        else:
            trueUrl = trueUrl[2:]
            trueUrl = trueUrl[: -2]
    elif url[0: 11] == 'flashget://':
    # 快车
        base64Str = url[11:]
        # 提取协议后的载荷字符串
        try:
            trueUrl = base64.b64decode(base64Str)
        except:
            return 0
        else:
            trueUrl = trueUrl[10:]
            trueUrl = trueUrl[: -10]
    else:
        trueUrl = url.encode('utf-8')
    
    # #
    # 下面的处理是为了防止从非真实地址解析出来的地址不是由 utf-8 编码的 
    try:
    # 尝试使用 utf-8 解码
        trueUrl.decode('utf-8')
    except UnicodeDecodeError:
    # 如果解码不成功则使用 GBK 解码再使用 utf-8 编码
        trueUrl = trueUrl.decode('gbk').encode('utf-8')
    #
    # #

    return trueUrl

def qqxf(url):
    """将真实地址转换为QQ旋风地址
    Arguement:
        bytes, 真实地址
    Return:
        bytes, QQ旋风地址
    """
    return b'qqdl://' + base64.b64encode(url)
def thunder(url):
    """将真实地址转换为迅雷地址
    Arguement:
        bytes, 真实地址
    Return:
        bytes, 迅雷地址
    """
    return b'thunder://' + base64.b64encode(b'AA' + url + b'ZZ')
def flashget(url):
    """将真实地址转换为快车地址
    Arguement:
        bytes, 真实地址
    Return:
        bytes, 快车地址
    """
    return b'flashget://' + base64.b64encode(b'[FLASHGET]' + url + b'[FLASHGET]')
