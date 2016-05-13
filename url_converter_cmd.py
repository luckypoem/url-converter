import url_converter_lib
inputURL = input("URL:-> ")
# 接收用户输入地址
if len(inputURL) == 0:
    pass
else:
    trueUrl = url_converter_lib.urlConvert(inputURL)
    # 计算真实地址
    if trueUrl == 0:
    # 无法正确转换用户输入的地址
        print('输入地址有误, 无法转换')
    else:
        print("真实-> " + trueUrl.decode('utf-8'))
        print("旋风-> " + url_converter_lib.qqxf(trueUrl).decode('utf-8'))
        print("迅雷-> " + url_converter_lib.thunder(trueUrl).decode('utf-8'))
        print("快车-> " + url_converter_lib.flashget(trueUrl).decode('utf-8'))
