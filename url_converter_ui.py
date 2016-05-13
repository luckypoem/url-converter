import tkinter
import url_converter_lib
root = tkinter.Tk()
# 新建根窗口
root.title('url-converter')
# 设置窗口标题

def convert():
    url_qqxf_output.delete(1.0, tkinter.END)
    # 清空文本框内容
    url = url_input.get(1.0, tkinter.END)[: -1]
    # 获取用户输入
    
    if len(url) == 0:
    # 如果输入为空, 则直接返回
        return

    url_true = url_converter_lib.urlConvert(url)
    # 计算真实地址
    if url_true == 0:
    # 无法正确转换用户输入的地址
        url_true = '输入不合法'.encode('utf-8')
    else:
    # 能正确地转换用户输入的地址
        url_true_output.delete(1.0, tkinter.END)
        # 清空之前的真实地址内容
        url_true_output.insert(tkinter.END, url_true.decode('utf-8'))
        # 显示真实地址
        
        url_qqxf_output.delete(1.0, tkinter.END)
        # 清空之前的 QQ 旋风地址内容
        url_qqxf_output.insert(tkinter.END, url_converter_lib.qqxf(url_true).decode('utf-8'))
        # 显示 QQ 旋风地址

        url_thunder_output.delete(1.0, tkinter.END)
        # 清空之前的迅雷地址内容
        url_thunder_output.insert(tkinter.END, url_converter_lib.thunder(url_true).decode('utf-8'))
        # 显示迅雷地址

        url_flashget_output.delete(1.0, tkinter.END)
        # 清空之前的快车地址内容
        url_flashget_output.insert(tkinter.END, url_converter_lib.flashget(url_true).decode('utf-8'))
        # 显示快车地址

def clear():
    url_input.delete(1.0, tkinter.END)
    url_true_output.delete(1.0, tkinter.END)
    url_qqxf_output.delete(1.0, tkinter.END)
    url_thunder_output.delete(1.0, tkinter.END)
    url_flashget_output.delete(1.0, tkinter.END)
        
convert_button = tkinter.Button(text='转换', command=convert)
convert_button.grid(row=1, column=1)
# 转换按钮按钮

clear_button = tkinter.Button(text='清空', command=clear)
clear_button.grid(row=1, column=2)
# 清空按钮

quit_button = tkinter.Button(text='退出', command= root.quit)
quit_button.grid(row=1, column=3)
# 退出按钮

url_input_label = tkinter.Label(text='输入')
url_input_label.grid(row=2, column=1)
url_input = tkinter.Text(width=50, height=5)
url_input.grid(row=2, column=2)
# 待转换地址输入

url_true_label = tkinter.Label(text='真实地址')
url_true_label.grid(row=3, column=1)
url_true_output = tkinter.Text(width=50, height=5)
url_true_output.grid(row=3, column=2)
# 真实地址输出

url_qqxf_label = tkinter.Label(text='QQ 旋风地址')
url_qqxf_label.grid(row=4, column=1)
url_qqxf_output = tkinter.Text(width=50, height=5)
url_qqxf_output.grid(row=4, column=2)
# QQ 旋风地址输出

url_thunder_label = tkinter.Label(text='迅雷地址')
url_thunder_label.grid(row=5, column=1)
url_thunder_output = tkinter.Text(width=50, height=5)
url_thunder_output.grid(row=5, column=2)
# 迅雷地址输出

url_flashget_label = tkinter.Label(text='快车地址')
url_flashget_label.grid(row=6, column=1)
url_flashget_output = tkinter.Text(width=50, height=5)
url_flashget_output.grid(row=6, column=2)
# 快车地址输出

tkinter.mainloop()
# 进入主事件循环
