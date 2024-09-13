
#   
#                  Arduino U8G2 字库生成器    
#                  作者：乐乐龙果冻（gxdung）
#            是只混兽圈的龙龙ww 欢迎关注B站/抖音/小红书
#
#         有任何问题请通过 GitHub Issue 或 B站私信 反馈
#            GitHub：https://github.com/gxdung
#
#--------------------------------------------------------------------------
#    本工程系 Gitee 平台 @gastonfeng 的 u8g2_fontmaker 重构项目
#    您可以通过本工具生成 Map、BDF 文件来创建属于您自己的 U8g2 字体字库
#
#    项目参考
#    1、bdfconv 命令行生成器：https://stncrn.github.io/u8g2-unifont-helper/
#    2、u8g2：https://github.com/olikraus/u8g2
#    3、u8g2 字体懒人脚本工具：https://gitee.com/kaikong/u8g2_fontmaker/tree/main


#  0、项目依赖，请检查以下模块是否存在 （通过 pip install 命令安装）
import os, re, pathlib, subprocess, shutil, chardet

#  1、设置字体名称与大小 (拷贝字体到 /font 文件夹下)
FontFile  = "1.ttf"    # 字体文件名
FontName  = "1"          # 字体名称
FontSizes = [14]                # 字体大小

#  2、依赖文件与路径配置
MapArray = ["chinese1", "chinese2", "chinese3", "gb2312", "gb2312a", "gb2312b"]
Folders  = ["bdf", "font", "output", "map", "core", "custom"]

path = pathlib.Path(__file__).parent.resolve()
bdfUrl  = str(path / Folders[0])
fontUrl = str(path / Folders[1])
codeUrl = str(path / Folders[2])
mapUrl  = str(path / Folders[3])
toolUrl = str(path / Folders[4])
customUrl = str(path / Folders[5])

ver = "1.0.2 (240913)"

#  3、工作模式：请配置 MapStatus 变量
#  0：自定义字库 txt格式   1：预设字库
#  无自定义 map 字库时，请选择 0

MapStatus = 0 

# 字库文件名
# 预设字库 ["chinese1", "chinese2", "chinese3", "gb2312", "gb2312a", "gb2312b"]
MapName   = "furry"     


#  4、工具函数
#  a. 控制台输出字体颜色
class color: 
    PURPLE = '\033[95m' 
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    HIGHLIGHT ='\033[1m'

#  b. 版本号输出
def version():
    print("\n - 当前版本：Ver " + ver + "\n")

#  c. 文件操作类函数
def openFile(url):
    return open(url, "r", encoding='utf8')

def IsFolder():
    count = len(Folders)   # 数组元素个数
    i = 0               # 计数器

    for folder in Folders:
        url = path / folder
        if not url.exists():
            os.mkdir(url)
            print(f"{color.YELLOW} - a. 目录检查：未通过，但已创建 {folder} 文件夹 {color.END}")
        i += 1

    if i == count:
        print(f"{color.GREEN} - a. 目录检查：通过 ({i}/{count}){color.END}")

def IsFiles():
    Fonts = [FontFile]
    fontnum = len(Fonts)     # 字体文件个数
    mapnum = len(MapArray)   # map文件个数
    const = 0                # 计数器

    for file in Fonts:
        const += 1
        if os.path.exists(fontUrl + "\\" + file) == 1:
            if(const == fontnum):
                print(f"{color.GREEN} - b. 字体文件检查：通过 ({str(const)}/{str(fontnum)}) {color.END}")

        else:
            print(f"{color.RED} - b. 字体文件检查：不存在 ( {file} ) {color.END}")
            Finish()

    const = 0
    for maps in MapArray:
        const += 1
        if os.path.exists(mapUrl + "\\" + maps + ".map") == 1:
            if(const == mapnum):
                print(f"{color.GREEN} - c. 字库文件检查：通过 ({str(const)}/{str(mapnum)}) {color.END}")

        else:
            print(f"{color.RED} - c. 字库文件检查：异常 {maps}.map ({str(const)}/{str(mapnum)}) {color.END}")
            Finish()
    const = 0

def checkMap():
    if MapStatus == 0 :
        if os.path.exists(str(f'{customUrl}\\{MapName}.txt')) == 1:
            print(f'{color.GREEN} - e. 自定义字库 (TXT) 存在 {color.END}')
        else:
            print(f'{color.RED} - e. 自定义字库 (TXT) 不存在, 请检查 {color.END}')
            Finish()

    elif MapStatus == 1 :
        if os.path.exists(str(f'{mapUrl}\\{MapName}.map')) == 1:
            print(f'{color.GREEN} - e. 预设字库 (Map) 存在 {color.END}')
        else:
            print(f'{color.RED} - e. 预设字库 (Map) 不存在, 请检查 {color.END}')
            Finish()


def Depend():
    tool = ["bdfconv.exe", "header1.txt", "header2.txt", "otf2bdf.exe"]
    const = 0
    for tools in tool:
        if os.path.exists(toolUrl + "\\" + tools) == 1:
            const += 1
            if (const == len(tool)):
                print(f"{color.GREEN} - d. 项目依赖文件：存在 ( {str(const)}/{str(len(tool))} ) {color.END}")
        else:
            print(f"{color.RED} - d. 项目依赖文件：不存在, 请检查 ( {tools} ) {color.END}")
            Finish()


#  d. 程序开始/结束
def Start():
    print(f"{color.BOLD} \n ------------  Arduino U8g2 字库生成器 (GitHub: @gxdung 乐乐龙果冻)  ----------- {color.END}")
    version()
    IsFolder()
    IsFiles()

def Finish():
    print("\n ---------------------------------- 执行完毕 ----------------------------------- ")
    print(f"{color.BOLD} \n ------------  Arduino U8g2 字库生成器 (GitHub: @gxdung 乐乐龙果冻)  ----------- \n {color.END}")
    exit()

#  e. TTF 转换成 BDF 字库
def createBDF():
    print(f"{color.BOLD}{color.BLUE}\n ------ j. 开始转换BDF文件 ( CMD 命令行 ) ------{color.END}")

    # OTF2BDF工具 CMD 命令说明
    # -r 设置水平与垂直分辨率  -p 设置所需的像素大小  -o 输出文件

    count = 0

    for px in FontSizes:
        msgl = []  # CMD 控制台输出    
        count += 1 

        # CMD 命令
        cmd1 = str(f"cd {str(toolUrl)}")
        cmd2 = str(f"otf2bdf -r 100 -p {px} -o {FontName}_{px}.bdf {fontUrl}\\{FontFile}")
        print(f"{color.CYAN} - 执行: {color.END} {cmd1} \n{color.CYAN} - 执行: {color.END} {cmd2}")

        # CMD 调用
        cmd = subprocess.Popen( str(f"{cmd1}&&{cmd2}"), shell=True, stdout=subprocess.PIPE)
        msg = cmd.stdout.readline().decode(encoding="gbk")
        msgl.append(msg)

        cmd.wait()
        cmd.stdout.close()
        if(msg==""):
            print(f"\n{color.GREEN} - 命令行成功执行: 已生成 {str(px)}px 字库{color.END} ({str(count)}/{str(len(FontSizes))})")
            shutil.move(str(toolUrl) + "\\" + str(FontName) +"_" + str(px)+".bdf", str(bdfUrl) + "\\" + str(FontName) +"_" + str(px)+".bdf") # 移动文件
            
            count = 0
            print(f"{color.BOLD}{color.GREEN} - BDF 字库文件成功生成 {color.END}")

        else:
            print(f"{color.RED} - 命令行执行异常: {msgl[0]} ({str(count)}/){str(len(FontSizes))} {color.END}")
            print(f"{color.BOLD}{color.RED} - BDF 字库文件生成失败 {color.END}")
            Finish()



#  f. 生成 C 源代码
def sourceCode():
    print(f"{color.BOLD}{color.PURPLE}\n ------ k. 开始生成 C 语言源文件 ------{color.END}")

    count = 0  # 计数器
    for px in FontSizes:
        count += 1
        msgl = []  # CMD 控制台输出

        # bdfconv 命令行说明
        # -b <n> 字体构建模式，0：比例，1：公共高度，2：等宽，3：8的倍数
        # -f <n> 字体格式，0：ucglib 字体，1：u8g2 字体，2：u8g2 未压缩的8x8 字体（强制-b 3）
        # -M 'mapfile' 从文件 'mapfile' 读取 Unicode ASCII 映射
        # -o <file> C 输出文件
        # -n <name> C 标识符（字体名称）
        # 其他说明：https://clz.me/u8g2-bdfconv/

        cmd1 = str(f"cd {str(toolUrl)}")
        cmd2 = str(f"bdfconv -b 0 -f 1 -M {str(mapUrl)}\\{str(MapName)}.map -n {str(FontName)}_{str(px)} -o {str(codeUrl)}\\{str(FontName)}_{str(px)}.c {str(bdfUrl)}\\{str(FontName)}_{str(px)}.bdf")

        if MapStatus == 0:
            cmd2 = str(f"bdfconv -b 0 -f 1 -M {str(customUrl)}\\{str(MapName)}.map -n {str(FontName)}_{str(px)} -o {str(codeUrl)}\\{str(FontName)}_{str(px)}.c {str(bdfUrl)}\\{str(FontName)}_{str(px)}.bdf")
        
        print(f"{color.CYAN} - 执行: {color.END} {cmd1} \n{color.CYAN} - 执行: {color.END} {cmd2}")

        # CMD 调用
        cmd = subprocess.Popen(cmd1+"&&"+cmd2, shell=True, stdout=subprocess.PIPE)
        msg = cmd.stdout.readline().decode(encoding="gbk")
        msgl.append(msg)

        cmd.wait()
        cmd.stdout.close()

        if(msg == ""):
            print(f"{color.GREEN} - 命令行成功执行: 已生成 {str(px)}px C 文件 {color.END}({str(count)}/{str(len(FontSizes))})\n")
        else:
            print(f"{color.RED} - 命令行执行异常: {str(msgl[0])} ({str(count)}/{str(len(FontSizes))}{color.END}\n")

    count = 0

#  g. 操作 C 源代码
def editCode():
    print(f"{color.BOLD}{color.BLUE}\n ------ l. 开始处理 C 语言源文件 ------{color.END}")
    count = 0  # 计数器
    error = 0
    for px in FontSizes:
        count += 1
        cpath = str(f'{codeUrl}\\{FontName}_{px}.c')

        if os.path.exists(cpath) == 1:
            cfile = open(cpath, "r+", encoding="utf-8", errors="ignore")
            cdata = cfile.read()
            cfile.close()

            cfile = open(cpath, "w+", encoding="utf-8")
            cfile.seek(0, 0)
            headcode = str(f'\n #include "{FontName}_{px}.h"')
            cfile.write(str(f'{headcode}\n\n{str(cdata)}'))
            cfile.close()
            print(f"{color.GREEN} - 已处理: {str(px)}px C 文件 {color.END}({str(count)}/{str(len(FontSizes))})")
        else:
            print(f"{color.RED} - 文件不存在: {str(px)}px C 文件 {color.END}({str(count)}/{str(len(FontSizes))})")
            error += 1
    
    if error > 0:
        print(f"{color.BOLD}{color.YELLOW} - Warning: C 语言源文件写入失败或不存在 ({str(error)}/{str(len(FontSizes))}) {color.END}\n")
        Finish()
    else:
        print(f"{color.BOLD}{color.GREEN} - Success: C 语言源文件处理完成 {color.END}\n")

#  h. 生成 Header 文件
def headerCode():
    print(f"{color.BOLD}{color.CYAN} ------ m. 开始处理 Header 文件 ------{color.END}")
    count = 0  # 计数器
    head1 = openFile(str(f"{toolUrl}\\header1.txt"))
    head2 = openFile(str(f"{toolUrl}\\header2.txt"))

    h1 = head1.read()
    h2 = head2.read()
    head1.close()
    head2.close()

    for px in FontSizes:
        count += 1
        fontname = str(f"{str(FontName)}_{str(px)}")
        codeTemp = str(f"#ifndef _{fontname.upper()}_H")
        codeTemp = codeTemp + str(f"\n#define _{fontname.upper()}_H")
        codeTemp = codeTemp + str(f"\n{h1}")
        codeTemp = codeTemp + str(f'\n extern const uint8_t {fontname} [] U8G2_FONT_SECTION("{fontname}");')
        codeTemp = codeTemp + str(f"\n\n{h2}")

        headerTemp = open(str(f'{codeUrl}\\{fontname}.h'), "w", encoding='utf-8')
        headerTemp.write(codeTemp)
        headerTemp.close()

        print(f'{color.GREEN} - 已生成 C Header 文件 ({str(count)}/{str(len(FontSizes))}){color.END}')

    print(f'\n{color.GREEN}{color.BOLD} - 自定义字库已生成，请将 {color.END}OutPut {color.GREEN}{color.BOLD}文件夹内的字库上传至开发板进行调试。{color.END}')
    print(f'{color.YELLOW}{color.BOLD} - 请注意：中文字体可能存在大小不一致，目前无方案解决该问题。请尝试控制单个汉字的位置。{color.END}')

#  i. UTF-8 转 Unicode
def utf8ToUnicode(str):
    Word,Uni,word1=[],[],[]
    for word in str:
        Word.append(word)
        # 正则表达式 匹配A-Z a-z 0-9 特殊符号 空格 换行符
        r = re.compile(r'^[a-zA-Z0-9\x21-\x7e\s\n]') 
    for word in Word:
        result = r.match(word)
        if result != None:
            temp = result.group()
            word1.append(temp)
            temp = hex(ord(word))[2:]
            temp = "\\u00" + temp
            Uni.append(temp)
        else:
            temp = word.encode('unicode_escape')
            Uni.append(temp)
    print(color.HIGHLIGHT + color.PURPLE + '\n - f. 自定义字库 (TXT) 内容 -----------------------------------------------------' + color.END)
    print(Word)
    print(color.HIGHLIGHT + color.CYAN + '\n - g. 原始 Unicode 内容 ---------------------------------------------------------' + color.END)
    print(Uni)
    return(Uni)

#  j. 子程序：TXT 转换成 MAP 文件
def textToMap():
    text = openFile(str(f'{customUrl}\\{MapName}.txt'))
    data = str(text.read())

    # 生成原始 Unicode 内容
    unicode = utf8ToUnicode(data)
    text.close()

    # 生成临时文件 写入后再进行预处理
    tempText = open(str(f'{customUrl}\\temp.txt'), "w", encoding = 'UTF-8')
    tempText.write(str(unicode).replace('\\\\u','\\u',-1))
    tempText.close()
    tempText = open(str(f'{customUrl}\\temp.txt'), "r", encoding = 'UTF-8')
    tempText = str(tempText.read())

    # 预处理 Unicode
    tempText = tempText.replace('[','',-1).replace(']','',-1).replace('b\'\\u','\\u',-1).replace('\'','',-1).replace(' ','',-1).replace('\\u','$',-1)
    
    print(f'{color.HIGHLIGHT}{color.YELLOW}\n - h. 处理后 Unicode 内容 -------------------------------------------------------{color.END}')
    print(f'32-128, {tempText.upper()}')

    os.remove(str(f'{customUrl}\\temp.txt'))

    text = open(str(f'{customUrl}\\{MapName}.map'), "w", encoding = 'UTF-8')
    text.write(str(f'32-128, {tempText.upper()}'))
    text.close()
    
    print(f'{color.HIGHLIGHT}{color.GREEN}\n - i. 自定义字库 (MAP): 已生成{color.END} \n')

#  k. 生成字体文件
def handler():
    if MapStatus == 0:
        print(f'\n -----------------------{color.BLUE} 当前模式：0、自定义字库 (TXT) {color.END}--------------------------\n')
        checkMap()
        textToMap()
        createBDF()
        sourceCode()
        editCode()
        headerCode()
    
    if MapStatus == 1:
        print(f'\n -----------------------{color.BLUE} 当前模式：1、预设字库 (MAP) {color.END}--------------------------\n')
        checkMap()
        createBDF()
        sourceCode()
        editCode()
        headerCode()

Start()
handler()
Finish()
