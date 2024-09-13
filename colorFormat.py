

#   
#        TFT 屏幕颜色转换器 -- RGB 565
#            乐乐龙果冻（gxdung）
#   是只混兽圈的龙龙ww 欢迎关注B站/抖音/小红书
#
#   有任何问题请通过 GitHub Issue 或 B站私信 反馈
#     GitHub：https://github.com/gxdung
#---------------------------------------------


#  1、颜色输入
rgbclr = "(28,28,30)"     #  RGB值
hexclr = "#ffffff"         #  十六进制颜色

#  2、模式选择
#  0:RGB转RGB565  1:Hex转RGB565  2:RGB转Hex  3:Hex转RGB
mode = 0        

def start():
    global rgbclr # 全局变量声明

    # 去除 RGB 值括号
    rgbclr = rgbclr.replace('(','',-1)
    rgbclr = rgbclr.replace(')','',-1)

    print("\n ------------  TFT 屏幕颜色转换器 （GitHub：gxdung 乐乐龙果冻）  ----------- \n")

def ends():
    print("\n ----------------------------  程序运行完毕  ------------------------------- \n")
    exit()

# 模块：RGB 转 16进制
def RGB2Hex(rgb):
    RGB = rgb.split(',')            # 将RGB格式划分开来
    color = '#'
    for i in RGB:
        num = int(i) 
        # 将R、G、B分别转化为16进制拼接转换并大写 hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color

# 模块：16进制 转 RGB
def Hex2RGB(hex):
    r = int(hex[1:3],16)
    g = int(hex[3:5],16)
    b = int(hex[5:7], 16)
    rgb = str(r)+','+str(g)+','+str(b)
    return rgb

# 模块：二进制补码（字符串格式）
def bin2str(bin1):
    if len(bin1) < 8:
        Str = ""
        i = 0
        while i < 8 - len(bin1):
            Str = Str + "0"
            i += 1
    else:
        Str = ""
    return str(Str) + str(bin1)

def RGB565(rgb):
    global rgbclr
    RGB = list(rgb.split(','))
    r,g,b = str(bin(int(RGB[0]))),str(bin(int(RGB[1]))),str(bin(int(RGB[2])))
    r,g,b = r.replace('0b','',-1),g.replace('0b','',-1),b.replace('0b','',-1)
    r,g,b = bin2str(r),bin2str(g),bin2str(b)
    r,g,b = r[0:5],g[0:6],b[0:5]
    rgb565 = r+g+b
    rgb565 = hex(int(rgb565,2)).upper()
    return rgb565
    
#  3、判断模式
def modes():
    if mode == 0:
        print(" -- 当前模式：RGB 转 RGB565 \n")
        print(" -- 输出：" + str(RGB565(rgbclr)))
    elif mode == 1:
        print(" -- 当前模式：Hex 转 RGB565 \n")
        print(" -- 输出：" + str(RGB565(Hex2RGB(hexclr))))
    elif mode == 2:
        print(" -- 当前模式：RGB 转 Hex \n")
        print(" -- 输出：" + str(RGB2Hex(rgbclr)))
    else:
        print(" -- 当前模式：Hex 转 RGB \n")
        print(" -- 输出：" + str(Hex2RGB(hexclr)))

start()
modes()
ends()