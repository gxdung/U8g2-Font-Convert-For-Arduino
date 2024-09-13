
# Arduino U8G2 自定义字体生成工具
Arduino U8G2 Font Build Tool

本工具将帮助您更快速的创建项目所需的自定义字体


## 1、开始使用
### 重要说明
- 工具运行目录不得包含空格
- 字体名称不得包含中文与空格

### 项目依赖
#### Arduino 依赖
- [Arduino U8g2lib](https://github.com/olikraus/u8g2)
- [GFX Library for Arduino](https://github.com/moononournation/Arduino_GFX)

#### Python 依赖
```cmd
pip install pillow chardet subprocess shutil pathlib
```

### 开发环境
Platform I/O IDE For VS Code
https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide

## 2、Platform I/O 使用方法
### 使用 u8g2 库
```c
/* 引入库文件 */
#include <Arduino.h>
#include <SPI.h>
#include <U8g2lib.h>

/* 引用字体文件（本工具生成的字体文件） */
#include "u8g2_fontname_size_number.h" 
U8G2_FOR_ADAFRUIT_GFX u8g2Fonts;

void setup(){
  display.init();
  display.setRotation(3);    
  u8g2Fonts.begin(display); 
  u8g2Fonts.setFont(u8g2_fontname_size_number);
  u8g2Fonts.drawUTF8(0, 0, "一些文字");
}
```
### 使用 Adafruit GFX 或 Arduino GFX 库
```c
/* ESP32-C3 驱动 ST7789 1.47寸 172*320 IPS 屏幕 */

/*  接线顺序
    IPS / ESP32-C3
    VCC -- 3.3V
    GND -- GND
    DC  -- GPIO 6 
    CS  -- GPIO 7
    SCL -- GPIO 8  (SCK)
    SDA -- GPIO 10 (MOSI)
*/

/* 引入库文件 */
#include <Arduino.h>
#include <Arduino_GFX_Library.h>
#include <U8g2lib.h>
#include <stdio.h>
#include <stdlib.h>

/* 引用字体文件（本工具生成的字体文件） */
#include "PingFang_SC_R_16x16.h"

/* 引脚定义 Arduino_ESP32SPI( DC, CS, SCK/SCL, SDA/MOSI )*/
Arduino_DataBus *bus = new Arduino_ESP32SPI(6,7,8,10);

/* Arduino_ST7789( bus，RST，屏幕旋转90度，IPS屏幕：是，屏幕宽度，屏幕高度，col_offset1，col_rowset1，col_offset2，col_rowset2 */
Arduino_GFX *gfx = new Arduino_ST7789(bus,20,1,true,172,320,34,0,34,0);

void setup(void)
{   
    gfx->begin();
    gfx->fillScreen(0x0000);        /*  背景颜色  */
    gfx->setUTF8Print(true);        /*  启用UTF8 */
    gfx->setTextColor(WHITE);       /*  字体颜色  */
    gfx->setFont(PingFang_SC_R_16); /*  选择字体  */
    gfx->println("乐乐龙果冻");       /*  输出内容  */
}

void loop(){
}

```

## 3、项目参考
- [U8g2 Fontmaker (@gastonfeng)](https://gitee.com/kaikong/u8g2_fontmaker/)
- [U8g2 Issues #710](https://github.com/olikraus/u8g2/issues/710)
- [U8g2_wqy (@larryli) Wiki](https://github.com/larryli/u8g2_wqy/wiki/CustomFont)
