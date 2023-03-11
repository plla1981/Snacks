**首先感谢选择keyestudio产品,**

**我们将继续为你提供好的产品和服务!**

 

------

**关于keyestudio**

Keyestudio是KEYES Corporation旗下最畅销的品牌，我们的产品包括Arduino开发板，扩展板，传感器模块，树莓派，micro：bit扩展板和智能小车，以及为各种级别的客户设计的完整入门套件，这些入门套件旨在为任何水平的客户学习Arduino知识。

我们所有的产品均符合国际质量标准，并在世界各地的不同市场中得到了极大的赞赏。 

欢迎从我们的官方网站查看更多内容：

http://www.keyestudio.com

------

**获取资料和售后服务**

1. 坦克机器人资料下载地址：
2. 如果发现某些东西丢失或损坏，或者学习套件时遇到一些困难。keyestudio会提供免费和快速的支持，如果您有任何疑问，请给我们发送电子邮件：[service@keyestudio.com](http://m.138.gz.cn/webadmin/~CAmsnCrrNXhTAySKCerrIfWjjZuuWVfI/~/usr/mod_edituser.jsp?;uid=service@keyestudio.com;;clearCache=)
3. 欢迎提出建议和反馈，我们会根据您的反馈不断更新套件和教程，以使其更好。谢谢！

------

**产品安全**

1. 本产品内含细小的零件（螺丝，铜柱），请勿让7岁以下的儿童接触，放在他们拿不到的地方。
2. 本产品包含导电部件(控制板和电子模块），请按照本教程的要求进行操作，不当的操作可能导致过热并且损害零件，请勿触摸并立即断开电路电源。

------

**版权**

keyestudio商标和徽标是KEYES DIY ROBOT co.,LTD的版权,任何人和公司在没有授权的情况下，不得复制，售卖，转卖，keyestudio品牌的产品。如果你有兴趣在当地售卖我们的产品，请联系我们专业的批发销售人员：[fennie@keyestudio.com](http://m.138.gz.cn/webadmin/~CAmsnCrrNXhTAySKCerrIfWjjZuuWVfI/~/usr/mod_edituser.jsp?;uid=fennie@keyestudio.com;;clearCache=)

------





# **体感运动手套智能小车手势控制基于arduino**

![img](./zh_img/new(1).png)



------



- [**体感运动手套智能小车手势控制基于arduino**](#体感运动手套智能小车手势控制基于arduino)
  - [**介绍**](#介绍)
  - [**特点**](#特点)
  - [**参数**](#参数)
  - [**清单**](#清单)
  - [**教程**](#教程)
    - [**安装开发软件和驱动**](#安装开发软件和驱动)
      - [**安装Arduino IDE**](#安装arduino-ide)
      - [**keyestudio NANO PLUS开发板**](#keyestudio-nano-plus开发板)
      - [**安装开发板驱动文件**](#安装开发板驱动文件)
      - [**Arduino IDE设置和工具栏介绍**](#arduino-ide设置和工具栏介绍)
      - [**启动你的第一个程序**](#启动你的第一个程序)
    - [**安装库文件**](#安装库文件)
      - [**什么是arduino库文件 ?**](#什么是arduino库文件-)
      - [**如何安装库文件?**](#如何安装库文件)
    - [**扩展板介绍**](#扩展板介绍)
    - [**MPU6050基础数据**](#mpu6050基础数据)
      - [MPU6050介绍](#mpu6050介绍)
      - [**什么是陀螺仪传感器？**](#什么是陀螺仪传感器)
      - [**什么是加速度传感器？**](#什么是加速度传感器)
      - [**如何获取数据**](#如何获取数据)
      - [**接线图**](#接线图)
      - [**获取数据过程**](#获取数据过程)
        - [**获取传感器ID**](#获取传感器id)
        - [**设置数据量程**](#设置数据量程)
        - [**进行自检**](#进行自检)
        - [**进行校准**](#进行校准)
        - [**初始化**](#初始化)
        - [**判断是否有数据**](#判断是否有数据)
        - [**读取传感器数据**](#读取传感器数据)
        - [**结果**](#结果)
      - [**完整代码**](#完整代码)
      - [**拓展**](#拓展)
    - [**MPU6050姿态获取**](#mpu6050姿态获取)
      - [**姿态介绍**](#姿态介绍)
      - [**如何获取姿态**](#如何获取姿态)
      - [**接线图**](#接线图-1)
      - [**获取姿态过程**](#获取姿态过程)
        - [**转换加速度数据**](#转换加速度数据)
        - [**转换陀螺仪数据**](#转换陀螺仪数据)
        - [**计算积分**](#计算积分)
        - [**将六轴数据转换成四元数**](#将六轴数据转换成四元数)
        - [**四元数转换函数**](#四元数转换函数)
        - [**将四元数转换成欧拉角**](#将四元数转换成欧拉角)
      - [**结果**](#结果-1)
      - [**完整代码**](#完整代码-1)
    - [**蓝牙的发送与接收**](#蓝牙的发送与接收)
      - [**蓝牙模块介绍**](#蓝牙模块介绍)
      - [**相关AT命令详解**](#相关at命令详解)
      - [**接线图**](#接线图-2)
      - [**使用AT命令控制蓝牙**](#使用at命令控制蓝牙)
        - [**控制主机**](#控制主机)
        - [**控制从机**](#控制从机)
      - [**AT指令集**](#at指令集)
      - [**蓝牙主机连接从机**](#蓝牙主机连接从机)
      - [**蓝牙主从机通信**](#蓝牙主从机通信)
    - [**控制麦克纳姆轮小车**](#控制麦克纳姆轮小车)
      - [**手势角度**](#手势角度)
      - [**手势角度代码**](#手势角度代码)
      - [**控制小车代码**](#控制小车代码)
  - [**参考链接**](#参考链接)
  - [**附录**：安装步骤](#附录安装步骤)

------



## **介绍**

这是一款基于MPU6050的体感运动手套，它是Arduino套件之一，可以识别多种不同方向的手势角度。与传统的按键和滑动等操作方式相比，手势识别控制具有更大的自由度，让你可以随心所欲地操控你的设备。

通过蓝牙无线模块，可以与麦克纳姆轮小车、机械臂和双足机器人进行蓝牙连接，简单手势，即可实现隔空手势操作，控制小车的前进、机械臂的夹爪和机器人的行走等动作。 

安装简单易行，只需将几个模块拼接在一起，即可组成体感运动手套。此外，通过附在手套上的扩展板，可以安装更多模块，以创造出更多功能的体感手套，让你可以更轻松地操控你的设备。 

为了让您更好地体验手势控制带来的智能与便利，我们为您准备了几节Arduino C语言课程，从点亮一颗LED灯开始，循序渐进，到动手做手势控制，让你可以轻松上手，轻松掌握技术。

------



## **特点**

这款手套套件具有以下优点：

1.功能强大：能够识别多种不同的方向；

2.组装简单：只需几个简单的步骤即可完成，无需焊接电路；

3.扩展性强：附在手套上的扩展板，预留了常用的接口，可外扩其他传感器；

4.学习基础编程：使用Arduino IDE的C语言编程，可以接触底层代码。

------



## **参数**

工作电压：5V

电池电压：9V

最大输出电流：≤20mA（9V电池）

最大耗散功率：≤0.18W

蓝牙通信距离：40M（空旷地区）

蓝牙工作频率：2.4GHz ISM频段

工作温度：–10至+65摄氏度

------



## **清单**

当收到这个产品时，请根据附件7中的清单进行清点，以确保所有配件完整无损。如果发现有缺失的配件，请立即联系我们的销售人员。

| 序号 |           图片            |                             规格                             | 倍用量 |
| :--: | :-----------------------: | :----------------------------------------------------------: | :----: |
|  1   | ![img](zh_img/new(2).png) |         Keyestudio MPU6050陀螺仪与加速度计模块(直针)         |   1    |
|  2   | ![img](zh_img/new(3).png) | Keyestudio开发板 Keyestudio NANO PLUS 开发板 兼容ARDUINO NANO 黑色环保 |   1    |
|  3   | ![img](zh_img/new(4).png) |         DX-BT24 V5.1 BLE蓝牙模块 主机 上电不打印数据         |   1    |
|  4   | ![img](zh_img/new(5).png) |         Keyestudio NANO 体感运动手套扩展板 黑色环保          |   1    |
|  5   | ![img](zh_img/new(6).png) | FY672 M码 半指手套 背部塑胶 手背内侧：聚酯纤维+海绵+鸟眼布 防滑 手心内侧：符合保暖绒 黑色 |   1    |
|  6   | ![img](zh_img/new(7).png) |              USB2.0对TYPE C 白色 L:1M OD：4.0MM              |   1    |

如需完整安装步骤，请点击跳转至第7节[附录：安装步骤](#附录安装步骤)。

------



## **教程**

万事俱备，现在我们正式进入体感运动手套的教程。来感受代码操作硬件的乐趣。

<span style="color: rgb(255, 0, 0);">注意：扩展板上标注的G、GND表示电源负极，可连接传感器的G、GND、—等负极接口；标注的V、VCC为电源正极（此扩展板上的电源为5V），可连接传感器的V、VCC、+ 等5V电源接口。</span>

------



### **安装开发软件和驱动**

#### **安装Arduino IDE**

我们先到Arduino官方的网站（https://www.arduino.cc/），下载最新版本的arduino开发软件，进入网站之后点击界面上的SOFTWARE,如下图：

![img](zh_img/new(8).png)

------



Arduino 软件有很多版本，有wodows,mac linux系统的（如下图），而且还有过去老的版本，你只需要下载一个适合系统的版本即可。

![img](zh_img/new(9).png)

------



这里我们以Windows系统的为例给大家介绍下载和安装的步骤。Windows系统的也有两个版本，一个版本是安装版的，一个是下载版的不用安装，直接下载文件到电脑，解压缩就可以用了。

![img](zh_img/new(10).png)

一般情况下，我们点击JUST DOWNLOAD就可以下载了，当然，如果你愿意，你可以选择小小的赞助一下，以帮助伟大的Arduino 开源事业。

------



#### **keyestudio NANO PLUS开发板**

在开始所有的项目之前，我们首先要了解下面这片keyestudio NANO开发板，是这个项目的核心开发板。

![img](zh_img/new(11).png)

Keyestudio NANO PLUS的处理器核心是ATMEGA328P-AU。和官网的ARDUINO NANO对比，Keyestudio NANO PLUS使用的USB转串口芯片为CH340G，安装的驱动文件不一样，其他的使用方法完全一样。

它同时具有14路数字输入/输出口（其中6路可作为PWM输出），8路模拟输入，1个16MHz晶体振荡器，1个Type-C USB接口，1个ICSP接口和一个复位按钮。

其中ICSP接口是用来给ATMEGA328P-AU烧录固件，由于这个该芯片我们在出厂前都以烧录好固件，所以一般不用。使用时我们可以利用Type-C USB线供电，，还可以利用排母接口VIN GND（DC 7-12V）供电。

![img](zh_img/new(12).png)

![img](zh_img/new(13).png)

​	它包含支持微控制器所需的一切，可以通过连接排针Vin 和GND（DC 7-12V)接口和USB电源即可启动。接口说明：

| 编号 |           名称           |                             描述                             |
| :--: | :----------------------: | :----------------------------------------------------------: |
|  1   |       ICSP Headers       | 一个由MOSI、MISO、SCK、RESET、VCC和GND组成的的微型编程头，它通常被称为SPI（串行外设接口）。连接电脑时，可以给ATMEGA328P-AU烧录固件。 |
|  2   |   LED indicator（RX）    |         控制板进行串口通信，接收到信息时，RX灯闪烁。         |
|  3   |   LED indicator（TX）    |          控制板进行串口通信，发送信息时，TX灯闪烁。          |
|  4   |   LED indicator（POW）   |              控制板运作时，LED亮起，否则熄灭。               |
|  5   |    LED indicator（L）    |     当D13引脚为高电平时，LED亮起，为低电平时，LED熄灭。      |
|  6   | RX0（D0）TX1（D1）D2-D13 | 有14个数字I/O引脚（D0-D13）其中6个提供PWM（脉宽调制）输出，这些引脚可配置为数字输入引脚，用于读取逻辑值（0或1）。 |
|  7   |           RST            |             可外接按键，和ResetButton功能一样。              |
|  8   |      ATMEGA328P-AU       | 微控制器，你可以假设它作为板的大脑，微控制器是ATMEL公司的。有关该IC的结构和功能的更多详细信息，请参阅数据表。 |
|  9   |         MINI USB         | 利用mini USB线连接到电脑USB端口，可以给控制板供电，还可以给控制板上传程序。 |
|  10  |           3V3            |                     提供 3.3V 输出电压。                     |
|  11  |           REF            | 代表模拟参考。它用于设置外部参考电压（0至5伏之间）作为模拟输入引脚的上限。 |
|  12  |          A0-A7           |                      8个模拟引脚A0-A7。                      |
|  13  |            5V            |                      5V 输入输出电压。                       |
|  14  |           GND            |                       电源负极，接地。                       |
|  15  |           VIN            |             外部输入DC 7-12V电压，给控制板供电。             |
|  16  |       Reset Button       |                     可以重置你的控制板。                     |
|  17  |          CH340G          |         USB转串口芯片，将电脑USB信号转化成串口信号。         |
|  18  |         AMS1117          |  它将外部输入的DC 7-12V电压转化成DC 5V电压，给主控板供电。   |

------



#### **安装开发板驱动文件**

安装Arduino IDE后，我们就开始安装驱动。将控制板用USB线连接在电脑上后，如果是Windows10系统电脑，电脑会自动安装驱动。如果是其他系统电脑，如Windows7系统电脑，需要手动安装驱动。

控制板的USB转串口芯片为CH340G我们需要安装这芯片的驱动，驱动为usb_ch341_3.1.2009.06。第一次将控制板连接电脑时，点击计算机--属性--设备管理器，显示如下图。

![img](zh_img/new(14).png)

------



点击USB Serial后，点击“更新驱动程序”，开始安装驱动，如下图。

![img](zh_img/new(15).png)

------



进入下图，选择浏览我的电脑以查找驱动程序。

![img](zh_img/new(16).png)

------



在电脑中找到usb_ch341_3.1.2009.06文件夹。

![img](zh_img/new(17).png)

------



安装驱动完成，出现下图点击关闭，之后就会出现串口号了。

![img](zh_img/new(18).png)

------



这样驱动就装好了。点击计算机--属性--设备管理器，我们可看见如下图。

![img](zh_img/new(19).png)

------



#### **Arduino IDE设置和工具栏介绍**

装好了开发板的驱动，我们下面了解Arduino软件的使用，首先我们打开Arduino IDE软件。

![img](zh_img/new(20).png)

------



选择正确的Arduino板，与连接到计算机的电路板相匹配。转到Tools→Board，选择Arduino NANO。

![img](zh_img/new(21).png)

------



然后再选择正确的COM口（安装驱动成功后，可看到对应COM口），这样就算连接成功了。

![img](zh_img/new(22).png)

------



#### **启动你的第一个程序**

上面我们学习了怎么下载软件和安装开发板的驱动，那下面我们就开始正式开始第一个程序，打开文件选择例子，选择第一个文件BASIC里面的BLINK程序。

![img](zh_img/new(23).png)

------



按照前面方法设置板和COM口，IDE右下角显示对应板和COM口。点击左上角的“√”图标开始编译程序，检查错误，也可以点击“→”一键编译并上传到开发板。

![img](zh_img/new(24).png)

------



上传成功如下图。

![img](zh_img/new(25).png)

程序上传成功，板载的LED灯亮一秒钟，灭一秒钟，恭喜你的第一个程序完成了。Arduino编程语言可以分为三个主要部分：函数、值（变量和常量）和结构。具体参考请查看Arduino官网教程https://www.arduino.cc/reference/en/

------



### **安装库文件**

在开始课程之前我们还需要安装课程里面代码需要的Arduino库文件。

#### **什么是arduino库文件 ?**

库是代码的集合，使您可以轻松地连接到传感器、显示器、模块等。

例如，内置的LiquidCrystal库使与字符LCD显示器的通话变得容易，Internet上有数百个其他库可供下载。参考中列出了内置库和手动添加的库。 

------



#### **如何安装库文件?**

在这里，我们将为您介绍最简单的添加库的方法。首先，依次点击右上角的Skerch>Include Library>Add .Zip Library...


![img](zh_img/new(26).png)

------



再选择文件中，找到自己需要的库压缩包.zip格式，点击确定即可添加成功，添加成功后消息栏会显示“Library installed”。

![img](zh_img/new(27).png)

更多教程与产品，请访问本公司官网https://www.keyestudio.com/

------



### **扩展板介绍**

该体感运动手套扩展板基于ArduinoNANO开发，可安装9V电池，独立供电，不需要外接电源；板上配有常用的UART和I2C通信接口，以及两个按钮（D7，D8），ArduinoNANO的其他引脚也全部通过排针引出，可外接传感器。在扩展板上安装MPU6050模块和BT24蓝牙模块，即可组装成完整的体感运动手套。

![img](zh_img/new(28).png)

------



该原理图如下：

![img](zh_img/new(29).png)

------



###  **MPU6050基础数据**

####  MPU6050介绍

MPU6050是一款六轴运动处理器，它包括一个3轴陀螺仪和一个3轴加速度计，这两个传感器集成在一个芯片上，可以检测静态和动态的物体运动状态，包括角速度、角度和加速度。

------

MPU6050内部集成了一个16位ADC，它可以同时读取6轴的数据，从而实现对角速度和角度的测量，也可以从中推算出物体的加速度信息。MPU6050还拥有一个内置的温度传感器，可以用来测量芯片的温度，有助于在运行过程中对传感器的温度进行监测。

------

此外，MPU6050还集成了一个快速的DMP（Digital Motion Processor），可以帮助处理陀螺仪和加速度计的原始数据，从而获取物体的运动状态。

![img](zh_img/new(30).png)

------



典型电路图为：

![img](zh_img/new(31).png)

| 编号 | 名称 |                           描述                            |
| :--: | :--: | :-------------------------------------------------------: |
|  1   | GND  |                     负极接口（0V）。                      |
|  2   | VCC  |                正极接口（兼容3.3V、5V）。                 |
|  3   | SDA  |            I2C数据线，连接MCU，用来传输数据。             |
|  4   | SCL  |          I2C时钟线，连接MCU，用来同步数据传输。           |
|  5   | XDA  |       I2C数据线，连接外部扩展传感器，用来传输数据。       |
|  6   | XCL  |     I2C时钟线，连接外部扩展传感器，用来同步数据传输。     |
|  7   | AD0  | I2C从属地址，高电平时，传感器地址为0x69，低电平时为0x68。 |
|  8   | INT  |         外部中断引脚，检测MPU6050的内部中断时间。         |

- 操作电压：3.3V、5V

- 静态电流：5μA

- 旋转电流：3mA

- 最大旋转速度：2000°/s

- 加速度范围：±2g，±4g，±8g，±16g

- 温度范围：–10至+65摄氏度

**详细参数，请查看芯片数据手册。**

------



#### **什么是陀螺仪传感器？**

陀螺仪，又称回转角速率计，是一种测量旋转速度的仪器。

------

它的物理原理是利用陀螺效应，即物体在旋转运动时，会产生一个与旋转方向垂直的力，这种力叫做离心力。陀螺仪就是利用这种离心力来测量物体的旋转速度。陀螺仪一般由测量陀螺力的磁阻器、放大及调整电路、输出电路等组成。 陀螺仪可以用于测量汽车行驶方向、航空器姿态角、精密仪器控制系统等，它们可以精确测量物体的旋转速度，从而帮助用户获得准确的信息。

![img](zh_img/new(32).png)

------



#### **什么是加速度传感器？**

通过测量由重力引发的加速度，可以计算出设备相对于水平面的倾斜角度。分析动态加速度，可以确定设备的移动方式。

然而，开始时，光测量倾角和加速度可能看起来似乎没有什么用处。但是，工程师们已经想出了许多方法来获取更多有用的信息。 加速度传感器可以帮助机器人了解它所处的环境。它正在攀登吗？或者正在下坡？或者倒地了没有？或者对于飞行机器人来说，控制姿态也是至关重要的。而且，你还需要确保机器人没有携带炸弹前往人群密集处。一个熟练的程序员可以使用加速度传感器来回答所有上述问题。加速度传感器甚至可以用来分析发动机的振动。

***MPU6050中使用陀螺仪传感器测量角度，并使用加速度传感器测量加速度。接下来我们就来获取它的加速度和陀螺仪数据等基础数据。***

------



#### **如何获取数据**

MPU-6050使用I2C串行通信协议来获取数据。什么是I2C串行通信协议？

I2C通信协议是Inter-Integrated Circuit（IIC）的缩写，也叫作两线制或TWI（Two-Wire Interface），是一种通用的主从式的两线总线通信协议，它是由Philips Semiconductor公司开发的（现在被美国NXP半导体公司收购）。

其最大的优点是只需要两根线就可以完成数据的传输，对于系统线路的繁琐也减少了很多，这种总线可以并行联结127个节点，并且支持多主机，从机一般不需要外接电源，因为I2C总线可以把电源传输到从机。如下图。

![img](zh_img/new(33).png)

------



I2C总线具有两根线，分别为SCL（Serial Clock）和SDA（Serial Data），SCL线负责时钟信号，SDA线负责数据传输。在I2C总线中，只有主机可以控制时钟信号，节点只能接受时钟信号，主机控制所有的数据传输，从机只能接受数据。

I2C总线的数据传输采用8位数据传输的方式，通常一个字节的数据传输是由9个时钟信号组成，8个时钟信号传输数据，最后一个时钟信号用于传输结束的标志。同时，I2C总线也支持多字节的数据传输，不断重复上述过程，即可完成多字节的数据传输。

------

I2C协议的基本组成部分包括以下内容：

- 起始信号：在发送数据之前，发送方必须发送起始信号，以告知接收方，要发送数据了。

- 地址码：地址码用于告知接收方，要发送的数据是给谁的。

- 数据：数据按照位传输，每次传输一个字节的数据。 

- 停止信号：发送完数据后，发送方必须发送停止信号，以告知接收方，数据发送完毕。

**串口协议时序如下：**

**（具体通信协议请移步官网https://www.nxp.com/）**

![img](zh_img/new(34).png)

![img](zh_img/new(35).png)

Arduino提供了一个名为Wire.h的I2C协议集成库，可以通过调用其函数实现I2C通信，从而实现与I2C/TWI设备的通信。具体库介绍参考官网链接

https://www.arduino.cc/reference/en/language/functions/communication/wire/

------



#### **接线图**

将Arduino Nano 主板接到扩展板上，再把MPU6050接到扩展板上的I2C接口上即可。

![img](zh_img/new(36).png)

再将Arduino Nano用USB线连接电脑，打开Arduino IDE。

------



#### **获取数据过程**

##### **获取传感器ID**

要判断是否与MPU6050通信成功，需要获取到MPU6050的内部ID，并与数据手册上的ID（0x68）进行比较。

**代码如下：**

```c++
//获取到MPU6050传感器的ID值

uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050); 
```

------



#####  **设置数据量程**

获取到正确ID后，设置加速度和陀螺仪的量程，通过寄存器手册可知：

加速度分辨率：

![img](zh_img/new(37).png)

陀螺仪分辨率：

![img](zh_img/new(38).png)

**代码如下：**

```c++
//量程如下：
// GFS_250DPS:250 DPS (0x00), GFS_500DPS:500 DPS (0x01)
// GFS_1000DPS:1000 DPS (0x10), GFS_2000DPS:2000 DPS (0x11)
// AFS_2G:2 Gs (0x00), AFS_4G: 4 Gs (0x01)
// AFS_8G:8 Gs (0x10), AFS_16G:16 Gs  (0x11)
//设置MPU6050传感器的量程。

mpu.settings(AFS_2G, GFS_250DPS);
```

------



##### **进行自检**

运行自检程序，目的是确保设备在正常运行状态下，能够提供精准的数据和有效的输出。

**代码如下：**

```c++
//[在step()中使用] MPU6050进行自检，并把加速度和陀螺仪的三轴数据，存放在SelfTest[6]中。
//加速度自检时量程应设置为8g，陀螺仪自检时量程应设置为250dps。
// 自我检测值存放容器

float SelfTest[6];        

// MPU6050进行自检

mpu.MPU6050SelfTest(SelfTest); 
```

------



#####   **进行校准**

运行校准程序，由于陀螺仪和加速度计的结构和构造都是固定的，产品在出厂后，它们的读数可能会受到温度，湿度，振动和外界磁场的影响，因此需要校准来确保精确的测量。

**代码如下：**

```c++
//[在step()中使用] 校准陀螺仪和加速度计，在偏置寄存器中加载偏置值,并把数据存放在gyroBias[3]和accelBias[3]中。

float gyroBias[3] = {0, 0, 0}; // 陀螺仪和加速度计的偏差校正

float accelBias[3] = {0, 0, 0};

mpu.calibrateMPU6050(gyroBias, accelBias);
```

------



##### **初始化**

进行最终的初始化，关闭中断、关闭 AUX IIC 接口、禁止 FIFO、设置陀螺仪采样率和设置数字低通滤波器（DLPF）等。此外，还可以通过初始化过程来校准传感器，以确保其正确的工作。

**代码如下：**

```c++
//[在step()中使用] 初始化MPU6050

mpu.initMPU6050();
```

------



#####  **判断是否有数据**

初始化完成后，进行循环的获取传感器的数据，首先要判断数据是否准备好。

**代码如下：**

```c++
//判断数据是否准备就绪

if(mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01)
{
    
}
```

------



##### **读取传感器数据**

读取加速度、陀螺仪和温度计的数据。

**代码如下：**

```c++
//读取加速度、陀螺仪和温度的初始值

int16_t accelCount[3];      // 存储16位有符号的加速器传感器输出

int16_t gyroCount[3];      // 存储16位有符号的陀螺仪传感器输出

int16_t tempCount;        // 存储真实的内部芯片温度

 

// 读取加速度的初始值

mpu.readAccelData(accelCount);

// 读取陀螺仪的初始值

mpu.readGyroData(gyroCount);

//读取温度计的初始值

tempCount = mpu.readTempData();
```

------



##### **结果**

将扩展板平稳放在桌面上，按住Arduino NANO主板上的复位按钮，进行复位，越平衡，MPU6050获取的基础数据也越准确。打开Arduino IDE的串口监视器，可以看到获取的角速度、陀螺仪和温度等基础数据，每0.5秒刷新一次数据。

![img](zh_img/new(39).png)

 

1. MPU6050的初始化过程，大约需要3秒，只初始化一次，初始化时，请将扩展板和MPU6050传感器保持在水平位置。
2. MPU6050传感器的初始加速度数据。
3. MPU6050传感器的初始陀螺仪数据。
4. MPU6050传感器的初始温度计数据。

------



#### **完整代码**

**代码请查看资料中提供的lesson_1_1文件夹。**

[lesson_1_1.ino]:

```c++
#include <MPU6050.h>


MPU6050lib mpu;


int16_t accelCount[3];      // 存储16位有符号的加速器传感器输出

int16_t gyroCount[3];      // 存储16位有符号的陀螺仪传感器输出

int16_t tempCount;        // 存储真实的内部芯片温度

float gyroBias[3] = {0, 0, 0}; // 陀螺仪和加速度计的偏差校正

float accelBias[3] = {0, 0, 0};

float SelfTest[6];        // 自我检测值存放容器


void setup()

{

 Wire.begin();

 Serial.begin(9600);

 // Read the WHO_AM_I register, this is a good test of communication

 // Read WHO_AM_I register for MPU-6050

 uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050);  

 Serial.print("I AM ");

 Serial.print(c, HEX);

 //进行自检时，应设置为最小量程

   // Possible gyro scales (and their register bit settings) are: 

   // 250 DPS (0x00), 500 DPS (0x01), 1000 DPS (0x10), and 2000 DPS  (0x11).

   // Possible accelerometer scales (and their register bit settings) are:

   // 2 Gs (0x00), 4 Gs (0x01), 8 Gs (0x10), and 16 Gs  (0x11).

 mpu.settings(AFS_8G, GFS_250DPS);

 // WHO_AM_I should always be 0x68 //MPU6050版本1地址：0x68，2地址：0x98

 if (c == 0x68 || c == 0x98) {

  Serial.println("MPU6050 is online...");

  // Start by performing self test

  mpu.MPU6050SelfTest(SelfTest);


  if (SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f 

  && SelfTest[5] < 1.0f) {

   Serial.println("Pass Selftest!");

   // Calibrate gyro and accelerometers, load biases in bias registers

   mpu.calibrateMPU6050(gyroBias, accelBias);

   mpu.settings(AFS_2G, GFS_250DPS);

   mpu.initMPU6050();

   // Initialize device for active mode read of acclerometer, gyroscope, and temperature

   Serial.println("MPU6050 initialized for active data mode...."); 

  }

  else{

   Serial.print("Could not connect to MPU6050: 0x");

   Serial.println(c, HEX);

   // Loop forever if communication doesn't happen

   while (1) ; 

  }

 }

}


void loop()

{

 // If data ready bit set, all data registers have new data

 // check if data ready interrupt

 if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) {

  // Read the x/y/z adc values

  mpu.readAccelData(accelCount);

  // Read the x/y/z adc values

  mpu.readGyroData(gyroCount);

  Serial.println("--------");

  Serial.print("Accel X:");

  Serial.println(accelCount[0]);

  Serial.print("Accel Y:");

  Serial.println(accelCount[1]);

  Serial.print("Accel Z:");

  Serial.println(accelCount[2]);

  Serial.println("--------");

  Serial.print("Gyro X:");

  Serial.println(gyroCount[0]);

  Serial.print("Gyro Y:");

  Serial.println(gyroCount[1]);

  Serial.print("Gyro Z:");

  Serial.println(gyroCount[2]);

  Serial.println("--------");

  // Read the x/y/z adc values

  tempCount = mpu.readTempData();

  // Temperature in degrees Centigrade

  Serial.print("Initial TEMP values:");

  Serial.println(tempCount);

  Serial.println("--------");

  delay(500);

 }

}
```

------



#### **拓展**

MPU6050的初始温度数据不能作为我们日常使用的数据，因此应该把它转换成我们常用的单位来查看。接下来我们运用公式，把他转换成我们常用数据。

转换公式：


$$
Temperature in degrees C = (TEMP_OUT Register Value as a signed quantity)/340 + 36.53
$$



**具体操作，请查看芯片数据手册。**

**代码请查看资料中提供的lesson_1_2文件夹。**

[lesson_1_2.ino]:

```c++
#include <MPU6050.h>

MPU6050lib mpu;

int16_t tempCount;        // 存储真实的内部芯片温度

float temperature;        // 存储实际的温度，单位为摄氏度

float gyroBias[3] = {0, 0, 0}; // 陀螺仪和加速度计的偏差校正

float accelBias[3] = {0, 0, 0};

float SelfTest[6];        // 自我检测值存放容器

 
void setup()

{

     Wire.begin();

     Serial.begin(9600);

     // Read the WHO_AM_I register, this is a good test of communication

     // Read WHO_AM_I register for MPU-6050

     uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050);  

     Serial.print("I AM ");

     Serial.print(c, HEX);

     //进行自检时，应设置为最小量程

	// Possible gyro scales (and their register bit settings) are: 

	// 250 DPS (0x00), 500 DPS (0x01), 1000 DPS (0x10), and 2000 DPS  (0x11).

	// Possible accelerometer scales (and their register bit settings) are:

	// 2 Gs (0x00), 4 Gs (0x01), 8 Gs (0x10), and 16 Gs  (0x11).

	mpu.settings(AFS_8G, GFS_250DPS);

 	// WHO_AM_I should always be 0x68 //MPU6050版本1地址：0x68，2地址：0x98

 	if (c == 0x68 || c == 0x98) {

  		Serial.println("MPU6050 is online...");

  		// Start by performing self test

  		mpu.MPU6050SelfTest(SelfTest);

  		if (SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f 

  		&& SelfTest[5] < 1.0f) {

   			Serial.println("Pass Selftest!");

   			// Calibrate gyro and accelerometers, load biases in bias registers

   			mpu.calibrateMPU6050(gyroBias, accelBias);

   			mpu.settings(AFS_2G, GFS_250DPS);

   			mpu.initMPU6050();

   			// Initialize device for active mode read of acclerometer, gyroscope, and temperature

   			Serial.println("MPU6050 initialized for active data mode...."); 

    	}
		else{

			Serial.print("Could not connect to MPU6050: 0x");

			Serial.println(c, HEX);

			// Loop forever if communication doesn't happen

			while (1) ; 

        }
	}
}

 
void loop()

{

     // If data ready bit set, all data registers have new data

     // check if data ready interrupt

     if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) {

         tempCount = mpu.readTempData(); // Read the x/y/z adc values

  		temperature = ((float) tempCount) / 340. + 36.53; // Temperature in degrees Centigrade

	 }

 
 	Serial.println("--------");

 	// Temperature in degrees Centigrade

	Serial.print("TEMP values:");
	
	Serial.println(temperature);

 	Serial.println("--------");

	delay(500);

}
```

------



显示效果：转换成实际温度值。

![img](zh_img/new(40).png)

------



### **MPU6050姿态获取**

我们已经从MPU6050获得了数据，现在我们将加速度和陀螺仪的数据进行姿态融合解算。

在姿态融合解算中，一般使用四元数表示姿态，因为欧拉角会出现万向节死锁问题，而且运算复杂。四元数由三个实数和一个虚数组成，处理完毕后可以转换成欧拉角。从而获得准确的旋转信息，可以更准确地控制无人机，移动机器人或者其他的驱动器。

------



####  **姿态介绍**

MPU6050 可以用来测量物体的姿态。可以提供三个角度的测量：滚动（roll），俯仰（pitch）和偏航（yaw）。也可以提供物体的加速度，通过计算得到物体的速度和位置信息。

他的三轴如下：

![img](zh_img/new(41).png)

 

对应的欧拉角是一种表示物体在三维空间的旋转的角度的称呼，它的坐标轴可以任意调整。

欧拉角由三个角度组成，分别是滚转角（Roll），俯仰角（Pitch）和偏航角（Yaw)。

其中：

|   滚转角（Roll）    |  以 x轴为旋转轴的旋转角度   |
| :-----------------: | :-------------------------: |
| **俯仰角（Pitch）** | **以y轴为旋转轴的旋转角度** |
|  **偏航角（Yaw)**   | **以z轴为旋转轴的旋转角度** |

 

![img](zh_img/new(42).png)

 

在获取偏航角（Yaw)时，由于MPU6050内部的陀螺仪会自动校准，它会自动把自己的角度设置为零度，这会导致偏航角（Yaw)零飘。零飘是指检测到的数据会发生偶然的小波动，比如传感器的值会自动发生偶然的小变化。即使是经过优良的算法后，依然会产生零飘，这受限于硬件，解决方式：添加磁力计来校准MPU6050。

<span style="color: rgb(255, 0, 0);">所以在以下教学和应用中，我们主要使用翻滚角（Roll）和俯仰角（Pitch）作为主要内容。</span>

------



#### **如何获取姿态**

利用加速度和陀螺仪六轴基础数据，经过滤波算法，减少误差后，转换成四元数，之后再从四元数转换成欧拉角，来表示具体的姿态数据。

------

**获取四元数有两种方法：**

1. **利用MPU6050自带的数字运动器，也就是DMP，并且MPU的官方团队提供了一个嵌入式运动驱动库，可以直接输出姿态解算的四元数。**
2. **Sebastian Madgwick的高效定位滤波器。**

------

本次教程中使用高效定位滤波器是一种用于惯性/磁传感器阵列的无模型状态估计算法，来估计系统的姿态（Sebastian Madgwick是来自英国的一位博士后，他撰写了一篇名为“高效惯性/磁传感器阵列的定向滤波器”的文章，也就是此处的高效定位滤波器算法），四元数滤波算法的性能比肩卡尔曼滤波算法，但计算强度却小很多，以至于能在Arduino Pro Mini开发板上以8MHz的速度运行。该算法将变化的角度表示为一个四元数，有效过滤掉传感器的噪声，并减少定位误差。

高效定位滤波器使用下面的公式来估计姿态：



$$
(Δφ = qt * qt-1)
$$


$$
qt+1 = qt + (1/α) * Δφ
$$



Δφ是四元数之间的差值，表示两个四元数之间的夹角变化。qt是当前的四元数，表示当前的姿态，qt-1是上一次读取的四元数，表示上一次姿态，α是一个可调的调节参数，控制过滤器的敏感度，qt+1是下一次的四元数，是根据当前的四元数和差值计算出来的，表示下一次姿态。

------



#### **接线图**

![img](zh_img/new(43).png)

 

和5.3.5步骤获取MPU6050基础数据的教程一样，请把MPU6050安装在扩展板上，再用USB线连接电脑即可。

------



####  **获取姿态过程**

##### **转换加速度数据**

首先把加速度计的基础数据转换成实际数据。

其中加速度的计算公式为：



$$
加速度=\frac{加速度原始数据}{数据分辨}单位(m/s^2)
$$



***比如我们设置量程为±2g，那么通过ADC采集电压的值来输出加速度值，而数据寄存器是16位且最高一位为符号位，即ADC读取的值位±32768对应±2g，1g对应的ADC值为+32768/2，即16384LSB/g为数据分辨率同样可得±4g，数据分辨率为+32768/4=8192LSB/g。***



**代码如下：**

```c++
mpu.readAccelData(accelCount); //读取x/y/z adc值 Read the x/y/z adc values

aRes = mpu.getAres();

//现在我们将加速度值计算为实际的g Now we'll calculate the accleration value into actual g's	

ax = (float)accelCount[0] * aRes; //得到实际的g值，这取决于所设置的比例 get actual g value, this depends on scale being set

ay = (float)accelCount[1] * aRes;

az = (float)accelCount[2] * aRes;
```

------



##### **转换陀螺仪数据**

把陀螺仪的基础数据转换成实际数据。

其中角速度的计算公式为：



$$
角速度=\frac{角速度原始值}{数据分辨率}单位(°/s)
$$



***ADC输出范围为±32768，比如我们选中测量范围为±2000°/s，ADC读取的原始值为300，数据分辨率就是32768/2000=16.384LSB/(°/s)，那么转换为角速度就是300/16.384=18.3105(°/s)。***



**代码如下：**

```c++
mpu.readGyroData(gyroCount);    //读取x/y/z adc值 Read the x/y/z adc values

gRes = mpu.getGres();       //获取转换值


//计算陀螺值为实际度每秒 Calculate the gyro value into actual degrees per second

gyrox = (float)gyroCount[0] * gRes; //获得实际的陀螺值，这取决于刻度被设置 get actual gyro value, this depends on scale being set

gyroy = (float)gyroCount[1] * gRes;

gyroz = (float)gyroCount[2] * gRes;
```

------



##### **计算积分**

获取时间，用于计算积分区间，用于转换成四元数。



**代码如下：**

```c++
//获取系统当前微秒时间

 Now = micros();

 //按自上次过滤器更新以来经过的时间设置集成时间 set integration time by time elapsed since last filter update

 deltat = ((Now - lastUpdate) / 1000000.0f);

 lastUpdate = Now;

 if(lastUpdate - firstUpdate > 10000000uL) {

      beta = 0.041; //稳定后降低滤波器增益 decrease filter gain after stabilized

      zeta = 0.015; //稳定后增加陀螺偏压漂移增益 increase gyro bias drift gain after stabilized

 }
```

------



#####  **将六轴数据转换成四元数**

将加速度计数据和陀螺仪数据进行四元数的转换，陀螺仪每个轴的数据，都需要转换成弧度，再进行转换，其中gyrox * PI / 180.0f表示将gyrox的角度转换为弧度。因为弧度是一个角度的度量，而角度是一个弧度的度量，所以根据比例关系，gyrox * PI / 180.0f就是将gyrox的角度转换为弧度。



**代码如下：**

```c++
// 陀螺仪数据转换为弧度

gyrox = gyrox  * PI / 180.0f;

gyroy = gyroy * PI / 180.0f;

gyroz = gyroz * PI / 180.0f;

// 四元数转换函数

MadgwickQuaternionUpdate(ax, ay, az, gyrox, gyroy, gyroz);
```

------



##### **四元数转换函数**

四元数滤波器计算函数。先定义所需变量，包括偏差，辅助运算值、模和Jacobian矩阵值等。

1.先计算加速度的模长，即求加速度向量的模，模长是向量的长度。模长由下面的公式计算：


$$
norm = sqrt(ax * ax + ay * ay + az * az)
$$


*其中ax、ay和az分别表示x、y和z轴上的加速度。*

2.计算雅克比矩阵。

3.通过矩阵乘法实现梯度的计算。

4.将梯度归一化。

5.计算估计陀螺仪偏差。

6.计算和消除陀螺仪偏差。

7.计算四元数的导数。

8.然后积分估计四元数的导数。

9.最后进行四元数归一化。



**代码如下：**

```c++
// Implementation of Sebastian Madgwick's "...efficient orientation filter for... inertial/magnetic sensor arrays"

// which fuses acceleration and rotation rate to produce a quaternion-based estimate of relative

// device orientation -- which can be converted to yaw, pitch, and roll. Useful for stabilizing quadcopters, etc.

// The performance of the orientation filter is at least as good as conventional Kalman-based filtering algorithms

// but is much less computationally intensive---it can be performed on a 3.3 V Pro Mini operating at 8 MHz!

void MadgwickQuaternionUpdate(float ax, float ay, float az, float gyrox, float gyroy, float gyroz)

{

	//为便于阅读，简称局部变量 short name local variable for readability

	float q1 = q[0], q2 = q[1], q3 = q[2], q4 = q[3]; 

	//向量范数,模 vector norm    

	float norm;

	//目标功能元素 objetive funcyion elements

	float f1, f2, f3;

	//目标函数雅可比矩阵 objective function Jacobian elements

	float J_11or24, J_12or23, J_13or22, J_14or21, J_32, J_33; 

	float qDot1, qDot2, qDot3, qDot4;

	float hatDot1, hatDot2, hatDot3, hatDot4;

	//陀螺偏压误差 gyro bias error

	float gerrx, gerry, gerrz, gbiasx, gbiasy, gbiasz;

	//辅助变量避免重复运算 Auxiliary variables to avoid repeated arithmetic

	float _halfq1 = 0.5f * q1;
	
	float _halfq2 = 0.5f * q2;

	float _halfq3 = 0.5f * q3;

	float _halfq4 = 0.5f * q4;

	float _2q1 = 2.0f * q1;

	float _2q2 = 2.0f * q2;

	float _2q3 = 2.0f * q3;

	float _2q4 = 2.0f * q4;

	float _2q1q3 = 2.0f * q1 * q3;

	float _2q3q4 = 2.0f * q3 * q4;

 
	//规范化加速度计测量 Normalise accelerometer measurement

	norm = sqrt(ax * ax + ay * ay + az * az);

	if (norm == 0.0f) return; // handle NaN

	norm = 1.0f/norm;

	ax *= norm;

	ay *= norm;

	az *= norm;

 
	//计算目标函数和雅可比矩阵 Compute the objective function and Jacobian

	f1 = _2q2 * q4 - _2q1 * q3 - ax;

	f2 = _2q1 * q2 + _2q3 * q4 - ay;

	f3 = 1.0f - _2q2 * q2 - _2q3 * q3 - az;

	J_11or24 = _2q3;

	J_12or23 = _2q4;

	J_13or22 = _2q1;

	J_14or21 = _2q2;

	J_32 = 2.0f * J_14or21;

	J_33 = 2.0f * J_11or24;


	//计算梯度(矩阵乘法) Compute the gradient (matrix multiplication)

	hatDot1 = J_14or21 * f2 - J_11or24 * f1;

	hatDot2 = J_12or23 * f1 + J_13or22 * f2 - J_32 * f3;

	hatDot3 = J_12or23 * f2 - J_33 *f3 - J_13or22 * f1;

	hatDot4 = J_14or21 * f1 + J_11or24 * f2;

 
	//将梯度归一化 Normalize the gradient

	norm = sqrt(hatDot1 * hatDot1 + hatDot2 * hatDot2 + hatDot3 * hatDot3 + hatDot4 * hatDot4);

	hatDot1 /= norm;

	hatDot2 /= norm;

	hatDot3 /= norm;

	hatDot4 /= norm;

 
	//计算估计陀螺仪偏差 Compute estimated gyroscope biases

	gerrx = _2q1 * hatDot2 - _2q2 * hatDot1 - _2q3 * hatDot4 + _2q4 * hatDot3;

	gerry = _2q1 * hatDot3 + _2q2 * hatDot4 - _2q3 * hatDot1 - _2q4 * hatDot2;

	gerrz = _2q1 * hatDot4 - _2q2 * hatDot3 + _2q3 * hatDot2 - _2q4 * hatDot1;

 
	//计算和消除陀螺仪偏差 Compute and remove gyroscope biases

	gbiasx += gerrx * deltat * zeta;

	gbiasy += gerry * deltat * zeta;

	gbiasz += gerrz * deltat * zeta;

	gyrox -= gbiasx;

	gyroy -= gbiasy;

	gyroz -= gbiasz;

 
	// 计算四元数的导数 Compute the quaternion derivative

	qDot1 = -_halfq2 * gyrox - _halfq3 * gyroy - _halfq4 * gyroz;

	qDot2 =  _halfq1 * gyrox + _halfq3 * gyroz - _halfq4 * gyroy;

	qDot3 =  _halfq1 * gyroy - _halfq2 * gyroz + _halfq4 * gyrox;

	qDot4 =  _halfq1 * gyroz + _halfq2 * gyroy - _halfq3 * gyrox;

 
	// 计算，然后积分估计四元数的导数 Compute then integrate estimated quaternion derivative

	q1 += (qDot1 -(beta * hatDot1)) * deltat;

	q2 += (qDot2 -(beta * hatDot2)) * deltat;

	q3 += (qDot3 -(beta * hatDot3)) * deltat;

	q4 += (qDot4 -(beta * hatDot4)) * deltat;

 
	// 四元数归一化 Normalize the quaternion

	norm = sqrt(q1 * q1 + q2 * q2 + q3 * q3 + q4 * q4);   // 标准化四元数 normalise quaternion

	norm = 1.0f/norm;

	q[0] = q1 * norm;

	q[1] = q2 * norm;

	q[2] = q3 * norm;

	q[3] = q4 * norm;

}
```

------



##### **将四元数转换成欧拉角**

将四元数转换成最后的欧拉角，公式为：



$$
Yaw(z) = atan2(2*(w*z+x*y), 1-2*(z^2+x^2))
$$

$$
Pitch(y) = asin(2*(w*y-z*x))
$$

$$
Roll(x) = atan2(2*(w*x+y*z), 1-2*(x^2+y^2))
$$



**代码如下：**

```c++
yaw = atan2(2.0f * (q[1] * q[2] + q[0] * q[3]), q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]);

pitch = -asin(2.0f * (q[1] * q[3] - q[0] * q[2]));

roll  = atan2(2.0f * (q[0] * q[1] + q[2] * q[3]), q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]);


pitch *= 180.0f / PI;

yaw  *= 180.0f / PI;

roll  *= 180.0f / PI;
```

------



#### **结果**

将完整代码下载到Arduino NANO中，确保MPU6050传感器保持水平，按NANO主板的复位按键，等待3-5秒，打开串口，即可查看信息。

![img](zh_img/new(44).png)

 

其中：

1. 获取到MPU6050的ID：0x68

2. 进行自检，并打印出自检值。

3. 进行校准，打印出校准值，传感器进行初始化。

4. 获取到的加速度和陀螺仪数据，还有转换后的四元数数据。

5. 转换后的欧拉角数据。

6. XYZ三轴加速度、陀螺仪和欧拉角数据。


------



####  **完整代码**

**代码请查看资料中提供的lesson_2_1文件夹。**

[lesson_2_1.ino]:

```c++
#include "MPU6050.h"

MPU6050lib mpu;


float aRes, gRes;        //传感器的每个LSB的刻度分辨率 scale resolutions per LSB for the sensors

int16_t accelCount[3];      //存储16位符号加速度计传感器输出 Stores the 16-bit signed accelerometer sensor output

int16_t gyroCount[3];      //存储16位符号陀螺传感器输出 Stores the 16-bit signed gyro sensor output

float ax, ay, az;        //在g中存储真正的加速度值 Stores the real accel value in g's

float gyrox, gyroy, gyroz;    //存储真实的陀螺仪值，单位为度/秒 Stores the real gyro value in degrees per seconds

float gyroBias[3] = {0, 0, 0};

float accelBias[3] = {0, 0, 0}; //陀螺仪和加速度计的偏差校正 Bias corrections for gyro and accelerometer

int16_t tempCount;        //存储真正的内部芯片温度摄氏度 Stores the real internal chip temperature in degrees Celsius

float temperature;

float SelfTest[6];

float q[4] = {1.0f, 0.0f, 0.0f, 0.0f};// vector to hold quaternion

float pitch, yaw, roll;

//6自由度传感器融合计算参数 parameters for 6 DoF sensor fusion calculations

float GyroMeasError = PI * (40.0f / 180.0f);    // 陀螺仪测量误差以拉德/秒为单位(从60度/秒开始)，然后在~10秒后减小到3gyroscope measurement error in rads/s (start at 60 deg/s), then reduce after ~10 s to 3

float beta = sqrt(3.0f / 4.0f) * GyroMeasError;  // 计算β compute beta

float GyroMeasDrift = PI * (2.0f / 180.0f);    // 陀螺仪测量漂移(rad/s/s)(从0.0度/s/s开始)gyroscope measurement drift in rad/s/s (start at 0.0 deg/s/s)

float zeta = sqrt(3.0f / 4.0f) * GyroMeasDrift;  // 计算zeta, Madgwick格式中的另一个自由参数通常设置为一个小值或零值compute zeta, the other free parameter in the Madgwick scheme usually set to a small or zero value

float deltat = 0.0f;                // 两种滤波方案的积分区间integration interval for both filter schemes

uint32_t lastUpdate = 0, firstUpdate = 0;     // 用于计算积分区间used to calculate integration interval

uint32_t Now = 0;                 // 用于计算积分区间used to calculate integration interval

 

void setup()

{

 Wire.begin();

 Serial.begin(9600);


 // Read the WHO_AM_I register, this is a good test of communication

 uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050); // Read WHO_AM_I register for MPU-6050

 Serial.print("I AM ");

 Serial.println(c, HEX);


 mpu.settings(AFS_8G, GFS_250DPS);

 if (c == 0x68) //WHO_AM_I应该总是0x68 WHO_AM_I should always be 0x68

 {

  Serial.println("MPU6050 is online...");

  //从执行自检和报告值开始 Start by performing self test and reporting values

  mpu.MPU6050SelfTest(SelfTest); 

  Serial.print("x-axis self test: acceleration trim within : "); Serial.print(SelfTest[0],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: acceleration trim within : "); Serial.print(SelfTest[1],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: acceleration trim within : "); Serial.print(SelfTest[2],1); Serial.println("% of factory value");

  Serial.print("x-axis self test: gyration trim within : "); Serial.print(SelfTest[3],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: gyration trim within : "); Serial.print(SelfTest[4],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: gyration trim within : "); Serial.print(SelfTest[5],1); Serial.println("% of factory value");

 

  if (SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f && SelfTest[5] < 1.0f) {

   Serial.println("Pass Selftest!");

   //校准陀螺和加速度计，在偏置寄存器中加载偏置 Calibrate gyro and accelerometers, load biases in bias registers

   mpu.calibrateMPU6050(gyroBias, accelBias); 

   Serial.println("MPU6050 bias");

   Serial.println(" x\t  y\t  z  ");

   Serial.print((int)(1000 * accelBias[0])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[1])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[2]));

   Serial.println(" mg");

 
   Serial.print(gyroBias[0], 1); Serial.print('\t');

   Serial.print(gyroBias[1], 1); Serial.print('\t');

   Serial.print(gyroBias[2], 1);

   Serial.println(" o/s");


   mpu.settings(AFS_2G, GFS_250DPS);

   mpu.initMPU6050(); 

   //初始化设备的主动模式读数的加速度计、陀螺仪和温度 Initialize device for active mode read of acclerometer, gyroscope, and temperature


   Serial.println("MPU6050 initialized for active data mode...."); 

  }

 }

 else

 {

  Serial.print("Could not connect to MPU6050: 0x");

  Serial.println(c, HEX);

  while(1); //如果通信没有发生，则永远循环 Loop forever if communication doesn't happen

 }

}

 

void loop()

{

 //如果设置了数据就绪位，则所有数据寄存器都有新数据 If data ready bit set, all data registers have new data

 if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) { //检查数据是否准备 check if data ready interrupt

  mpu.readAccelData(accelCount);   //读取x/y/z adc值 Read the x/y/z adc values

  aRes = mpu.getAres();       //获取转换值


  //现在我们将加速度值计算为实际的g Now we'll calculate the accleration value into actual g's

  ax = (float)accelCount[0] * aRes; //得到实际的g值，这取决于所设置的比例 get actual g value, this depends on scale being set

  ay = (float)accelCount[1] * aRes;

  az = (float)accelCount[2] * aRes;


  mpu.readGyroData(gyroCount);    //读取x/y/z adc值 Read the x/y/z adc values

  gRes = mpu.getGres();       //获取转换值

 
  //计算陀螺值为实际度每秒 Calculate the gyro value into actual degrees per second

  gyrox = (float)gyroCount[0] * gRes; //获得实际的陀螺值，这取决于刻度被设置 get actual gyro value, this depends on scale being set

  gyroy = (float)gyroCount[1] * gRes;

  gyroz = (float)gyroCount[2] * gRes;


  tempCount = mpu.readTempData(); //读取x/y/z adc值 Read the x/y/z adc values

  temperature = ((float) tempCount) / 340. + 36.53; //温度(摄氏度) Temperature in degrees Centigrade

 }

 //获取系统当前微秒时间

 Now = micros();

 //按自上次过滤器更新以来经过的时间设置集成时间 set integration time by time elapsed since last filter update

 deltat = ((Now - lastUpdate) / 1000000.0f);

 lastUpdate = Now;

 if(lastUpdate - firstUpdate > 10000000uL) {

  beta = 0.041; //稳定后降低滤波器增益 decrease filter gain after stabilized

  zeta = 0.015; //稳定后增加陀螺偏压漂移增益 increase gyro bias drift gain after stabilized

 }

 // 陀螺仪数据转换为弧度

 gyrox = gyrox  * PI / 180.0f;

 gyroy = gyroy * PI / 180.0f;

 gyroz = gyroz * PI / 180.0f;

 // 四元素转换函数

 MadgwickQuaternionUpdate(ax, ay, az, gyrox, gyroy, gyroz);


 Serial.println("--------------------");

 Serial.print("ax:"); Serial.print((int)1000*ax);

 Serial.print("ay:"); Serial.print((int)1000*ay);

 Serial.print("az:"); Serial.print((int)1000*az); Serial.println(" mg");
 

 Serial.println("  ");

 Serial.print("gyrox:"); Serial.print( gyrox, 1);

 Serial.print("gyroy:"); Serial.print( gyroy, 1);

 Serial.print("gyroz:"); Serial.print( gyroz, 1); Serial.println(" deg/s");


 Serial.println("  ");

 Serial.print(" q0 = "); Serial.print(q[0]);

 Serial.print(" qx = "); Serial.print(q[1]);

 Serial.print(" qy = "); Serial.print(q[2]);

 Serial.print(" qz = "); Serial.println(q[3]);

 Serial.println("--------------------");


 // Define output variables from updated quaternion---these are Tait-Bryan angles, commonly used in aircraft orientation.

 // In this coordinate system, the positive z-axis is down toward Earth.

 // Yaw is the angle between Sensor x-axis and Earth magnetic North (or true North if corrected for local declination, looking down on the sensor positive yaw is counterclockwise.

 // Pitch is angle between sensor x-axis and Earth ground plane, toward the Earth is positive, up toward the sky is negative.

 // Roll is angle between sensor y-axis and Earth ground plane, y-axis up is positive roll.

 // These arise from the definition of the homogeneous rotation matrix constructed from quaternions.

 // Tait-Bryan angles as well as Euler angles are non-commutative; that is, the get the correct orientation the rotations must be

 // applied in the correct order which for this configuration is yaw, pitch, and then roll.

 yaw  = atan2(2.0f * (q[1] * q[2] + q[0] * q[3]), q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]);

 pitch = -asin(2.0f * (q[1] * q[3] - q[0] * q[2]));

 roll  = atan2(2.0f * (q[0] * q[1] + q[2] * q[3]), q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]);


 pitch *= 180.0f / PI;

 yaw  *= 180.0f / PI;

 roll  *= 180.0f / PI;

 
 Serial.println("--------------------");

 // Serial.println("Yaw\t Pitch\t Roll: ");

 Serial.print("Yaw:");

 Serial.print(yaw, 2);

 Serial.print("°");

 Serial.print("\tPitch:");

 Serial.print(pitch, 2);

 Serial.print("°");

 Serial.print("\tRoll:");

 Serial.print(roll, 2);

 Serial.println("°");

 Serial.println("--------------------");


 Serial.println(" x\t  y\t  z  ");


 Serial.print((int)(1000 * ax)); Serial.print('\t');

 Serial.print((int)(1000 * ay)); Serial.print('\t');

 Serial.print((int)(1000 * az));

 Serial.println(" mg");

 Serial.println("  ");

 Serial.print((int)(gyrox)); Serial.print('\t');

 Serial.print((int)(gyroy)); Serial.print('\t');

 Serial.print((int)(gyroz));

 Serial.println(" o/s");

 Serial.println("  ");

 Serial.print((int)(yaw)); Serial.print('\t');

 Serial.print((int)(pitch)); Serial.print('\t');

 Serial.print((int)(roll));

 Serial.println(" ypr");

 Serial.println("--------------------");


 delay(100);

}


// Implementation of Sebastian Madgwick's "...efficient orientation filter for... inertial/magnetic sensor arrays"

// which fuses acceleration and rotation rate to produce a quaternion-based estimate of relative

// device orientation -- which can be converted to yaw, pitch, and roll. Useful for stabilizing quadcopters, etc.

// The performance of the orientation filter is at least as good as conventional Kalman-based filtering algorithms

// but is much less computationally intensive---it can be performed on a 3.3 V Pro Mini operating at 8 MHz!

void MadgwickQuaternionUpdate(float ax, float ay, float az, float gyrox, float gyroy, float gyroz)

{

 float q1 = q[0], q2 = q[1], q3 = q[2], q4 = q[3];     //为便于阅读，简称局部变量 short name local variable for readability

 float norm;                        //向量范数 vector norm

 float f1, f2, f3;                     //目标功能元素 objetive funcyion elements

 float J_11or24, J_12or23, J_13or22, J_14or21, J_32, J_33; //目标函数雅可比矩阵 objective function Jacobian elements

 float qDot1, qDot2, qDot3, qDot4;

 float hatDot1, hatDot2, hatDot3, hatDot4;

 float gerrx, gerry, gerrz, gbiasx, gbiasy, gbiasz;     //陀螺偏压误差 gyro bias error
 

 //辅助变量避免重复运算 Auxiliary variables to avoid repeated arithmetic

 float _halfq1 = 0.5f * q1;

 float _halfq2 = 0.5f * q2;

 float _halfq3 = 0.5f * q3;

 float _halfq4 = 0.5f * q4;

 float _2q1 = 2.0f * q1;

 float _2q2 = 2.0f * q2;

 float _2q3 = 2.0f * q3;

 float _2q4 = 2.0f * q4;

 float _2q1q3 = 2.0f * q1 * q3;

 float _2q3q4 = 2.0f * q3 * q4;


 //规范化加速度计测量 Normalise accelerometer measurement

 norm = sqrt(ax * ax + ay * ay + az * az);

 if (norm == 0.0f) return; // handle NaN

 norm = 1.0f/norm;

 ax *= norm;

 ay *= norm;

 az *= norm;


 //计算目标函数和雅可比矩阵 Compute the objective function and Jacobian

 f1 = _2q2 * q4 - _2q1 * q3 - ax;

 f2 = _2q1 * q2 + _2q3 * q4 - ay;

 f3 = 1.0f - _2q2 * q2 - _2q3 * q3 - az;

 J_11or24 = _2q3;

 J_12or23 = _2q4;

 J_13or22 = _2q1;

 J_14or21 = _2q2;

 J_32 = 2.0f * J_14or21;

 J_33 = 2.0f * J_11or24;

 
 //计算梯度(矩阵乘法) Compute the gradient (matrix multiplication)

 hatDot1 = J_14or21 * f2 - J_11or24 * f1;

 hatDot2 = J_12or23 * f1 + J_13or22 * f2 - J_32 * f3;

 hatDot3 = J_12or23 * f2 - J_33 *f3 - J_13or22 * f1;

 hatDot4 = J_14or21 * f1 + J_11or24 * f2;


 //将梯度归一化 Normalize the gradient

 norm = sqrt(hatDot1 * hatDot1 + hatDot2 * hatDot2 + hatDot3 * hatDot3 + hatDot4 * hatDot4);

 hatDot1 /= norm;

 hatDot2 /= norm;

 hatDot3 /= norm;

 hatDot4 /= norm;
 

 //计算估计陀螺仪偏差 Compute estimated gyroscope biases

 gerrx = _2q1 * hatDot2 - _2q2 * hatDot1 - _2q3 * hatDot4 + _2q4 * hatDot3;

 gerry = _2q1 * hatDot3 + _2q2 * hatDot4 - _2q3 * hatDot1 - _2q4 * hatDot2;

 gerrz = _2q1 * hatDot4 - _2q2 * hatDot3 + _2q3 * hatDot2 - _2q4 * hatDot1;


 //计算和消除陀螺仪偏差 Compute and remove gyroscope biases

 gbiasx += gerrx * deltat * zeta;

 gbiasy += gerry * deltat * zeta;

 gbiasz += gerrz * deltat * zeta;

 gyrox -= gbiasx;

 gyroy -= gbiasy;

 gyroz -= gbiasz;
 

 //计算四元数的导数 Compute the quaternion derivative

 qDot1 = -_halfq2 * gyrox - _halfq3 * gyroy - _halfq4 * gyroz;

 qDot2 =  _halfq1 * gyrox + _halfq3 * gyroz - _halfq4 * gyroy;

 qDot3 =  _halfq1 * gyroy - _halfq2 * gyroz + _halfq4 * gyrox;

 qDot4 =  _halfq1 * gyroz + _halfq2 * gyroy - _halfq3 * gyrox;

 //计算，然后积分估计四元数的导数 Compute then integrate estimated quaternion derivative

 q1 += (qDot1 -(beta * hatDot1)) * deltat;

 q2 += (qDot2 -(beta * hatDot2)) * deltat;

 q3 += (qDot3 -(beta * hatDot3)) * deltat;

 q4 += (qDot4 -(beta * hatDot4)) * deltat;

 //四元数归一化 Normalize the quaternion

 norm = sqrt(q1 * q1 + q2 * q2 + q3 * q3 + q4 * q4);   // 标准化四元数 normalise quaternion

 norm = 1.0f/norm;

 q[0] = q1 * norm;

 q[1] = q2 * norm;

 q[2] = q3 * norm;

 q[3] = q4 * norm;

}
```

------



### **蓝牙的发送与接收**

#### **蓝牙模块介绍**

BT24蓝牙主机模块（直针）：

 

![img](zh_img/new(45).png)

 

BT24蓝牙从机模块（弯针）：

![img](zh_img/new(46).png)

 

DX-BT24蓝牙模块是深圳大夏龙雀科技有限公司专为智能无线数据传输而打造，采用DIALOG 14531芯片，遵循蓝牙BLE5.1规范，支持AT指令，具有调整串口波特率、设备名称等参数的灵活性，使用UART进行通信，优势是成本低、功耗低、接收灵敏度高。

------

**特点：**

- DIALOG14531主控芯片

- 蓝牙BLE5.1协议

- 功耗可低至2 uA

- 从模块可视距离90M、主模块可视距离20M

- 传输速率10K Bytes/s

- UART通信

- 可选择iBeacon模式程序

- 可选择直驱模式程序、可选择单主模式程序

- 可选择一主多从模式程序

------

**简易电路图：**

![img](zh_img/new(47).png)

------

蓝牙工作模式：

|     模式     |                             功能                             |
| :----------: | :----------------------------------------------------------: |
| 正常工作模式 |              所有功能和外设接口都可以正常使用。              |
|  低功耗模式  | 未连接状态下，仅开启广播，所有外设接口都关闭。连接状态下，所有功能和外设接口都可以正常使用。 |
|   冬眠模式   | 模块所有运行的 RAM块全部关闭，仅保留芯片内部的滴答时钟用于唤醒，广播和所有外设接口都关闭。 |

------

UART接口：模块串口默认参数：9600bps/8/n/1（波特率/数据位/无校验/停止位）。

|     参数     |                              值                              |
| :----------: | :----------------------------------------------------------: |
|    波特率    | 最低：2400baud（≤1%Error）标准：9600baud（≤1%Error）最大：115200baud（≤1%Error） |
|   奇偶校验   |                          无，奇或偶                          |
| 停止位的数量 |                             1/2                              |
| 每通道的位数 |                              8                               |

------

**关于如何控制蓝牙：**使用AT指令来控制蓝牙。AT指令是一组用于控制通用蓝牙模块行为的指令集。它由AT功能和AT参数组成，并以AT开头。AT功能被用来控制蓝牙模块的行为，如连接和断开连接，搜索和配对设备，设置蓝牙模块的参数，发送和接收数据等，而AT参数用于指定AT功能的相关信息，例如设置蓝牙设备的配对码，连接地址，连接时间间隔，发送数据的长度等。

------

**AT命令模式和透传模式：**

- AT命令模式：模块在未连接上其他从设备的情况下，即为命令模式，可以响应命令。
- 透传模式：模块连接上其他设备后，即为透传模式，此时可以开始传输数据。

------

**关于蓝牙设备之间的连接：**设备地址（MAC地址）是用来唯一识别一个物理设备的，对设备地址而言，一个重要的特性，就是唯一性（或者说一定范围内的唯一性），通俗的说，就是蓝牙的身份证，通过此地址来找到此设备。

------

一个BLE设备，可以使用两种类型的地址（一个BLE设备可以同时具备两种地址）：

**Public Device Address（公共设备地址）**和**Random Device Address（随机设备地址）**。

而Random Device Address又分为Static Device Address（静态设备地址）和Private Device Address（私密设备地址）两类。其中Private Device Address又可以分为Non-resolvable Private Address（不可解析私密地址）和Resolvable Private  Address（可解析私密地址）。

![img](zh_img/new(48).png)

 

------

**公共设备地址**（**Public Device Address**）：对经典蓝牙（BR/EDR）来说，其设备地址是一个48bits（6字节）的数字，称作“48-bit universal LAN MAC address”（和电脑的MAC地址一样）。正常情况下，该地址需要向IEEE申请购买。通过付费，来保证地址的唯一性。这种地址分配的方式，在BLE中也保留了下来，也就是Public Device Address（公共设备地址）。

------

**静态设备地址**（**Static Device Address**）：即设备地址不是固定分配的，而是在设备启动后随机生成的。

在下面的教程中，我们会用到主设备和从设备两个蓝牙模块，让两个模块进行无线通信。我们需要使用AT指令，来控制两个蓝牙模块进行通信。

------



#### **相关AT命令详解**

AT指令是计算机通过串口与蓝牙设备进行交互的一种文本型命令。它们可以用于询问蓝牙设备的状态，查询设备的功能，配置设备的参数，控制蓝牙的连接状态等等。我们可以通过USB转串口与蓝牙模块进行连接，对蓝牙模块进行操作。

------

**发送给蓝牙的AT命令的格式说明：**

**AT+Command<param1,param2,param3> <CR><CF>**

- 所有的指令以AT开头，<CR><LF>结束，在本文档中表现命令和响应的表格中，省略了<CR><LF>，仅显示命令和响应。

- 所有AT命令字符都为大写。

- <>内为可选内容，如果命令中有多个参数，以逗号“，”隔开，实际命令中不包含尖括号。<CR>为回车字符\r，十六进制为OXOD。

- <LF>为换行字符\n，十六进制为OXOA。

- 指令执行成功，返回相应命令以OK结束，失败返回EEROR=<>， “<>”内容为对应错误码

------

**从蓝牙接受回应AT命令的格式说明：**

**+Indication<=param1,param2,param3><CR><CF>**

- 回应指令以加号“+”开头，<CR><CF>结束

- 等于“=”后面为回应参数

- 如果回应参数中有多个参数，会以逗号”，”隔开

------

**AT命令举例说明：**

**举例：**修改蓝牙设备名称为1234

- 发送：AT+NAME1234

- 返回：+NAME=1234

​					OK

更详细的AT命令请参考[5.5.5AT指令集](#_AT指令集)和附带资料提供的数据手册。

------



#### **接线图**

我们使用USB转串口模块，与蓝牙模块进行通信，实现对蓝牙的AT命令控制。<span style="color: rgb(255, 0, 0);">注意：主机模块和从机模块的安装方法一致。</span>

此处我使用的是本公司的USB转串口模块Keyestudio FTDI(original chips) Basic Program。

USB转串口模块链接：https://www.keyestudio.com/search/?Keyword=ks0277

![img](zh_img/new(49).png)

引脚连接表：

| USB转串口模块 | 蓝牙主机&蓝牙从机 |
| :-----------: | :---------------: |
|      RX       |        TX         |
|      TX       |        RX         |
|      VCC      |        VCC        |
|      GND      |        GND        |

------



#### **使用AT命令控制蓝牙**

蓝牙模式在未连接上其他从设备的情况下，即为AT命令模式，可以响应AT命令。***\*请注意：所有AT指令都必须是大写字母！\****

#####  **控制主机**

我们在ArduinoIDE中，新建一个空白的项目，选择对应的串口。

![img](zh_img/new(50).png)

 

------



设置波特率为9600（蓝牙主机模块默认为9600），在输入框输入AT，然后回车发送命令，此时，如果蓝牙模块接收到了命令，会返回OK，说明你的命令已经可以被他接收了。

![img](zh_img/new(51).png)

------

 

***AT指令：查询版本号。***在ArduinoIDE输入框输入AT+VERSION，会回应蓝牙模块软件版本号。

![img](zh_img/new(51).png)

------

 

***AT指令：更改蓝牙名称。***在ArduinoIDE输入框输入AT+NAMEBT24 Master，蓝牙模块会修改为BT24 Master，并返回蓝牙名称，单独查询蓝牙名称的AT指令为AT+NAME。

![img](zh_img/new(52).png)

------



|  编号  |  1   |  2   |  3   |   4   |   5   |   6   |   7    | 默认值 |
| :----: | :--: | :--: | :--: | :---: | :---: | :---: | :----: | :----: |
| 波特率 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 |  9600  |

***AT指令：设置波特率。***在输入框输入AT+BAUD7，此时波特率已被设置为115200，与其他蓝牙或者手机等通信设备，进行通信时，其波特率也要设置为115200。

![img](zh_img/new(53).png)

------

 

***AT指令：设置模块的搜索模式。***设置相应的模式，蓝牙主机才能搜索到对应模式的从设备。

| 编号 |           功能           |   指令   |                             说明                             |
| :--: | :----------------------: | :------: | :----------------------------------------------------------: |
|  1   |     查询模块搜索模式     | AT+MODE  |                  查询蓝牙模块现在的搜索模式                  |
|  2   | 普通模式（系统默认模式） | AT+MODE0 | 普通模式:可以搜索到周边所有BLE蓝牙设备。(注:只能连接BT24系列的从模块，其他设备连接不上。) |
|  3   |       过滤厂商模式       | AT+MODE1 | 过滤厂商信息:只能搜索到广播包中带有我司厂商（BT24系列）信息的模块。 |
|  4   |         配对模式         | AT+MODE2 |          配对模式:只能搜索到开启配对模式的从设备。           |
|  5   |   获取IBEACON信息模式    | AT+MODE3 | 获取IBEACON信息模式:打开该模式后，可以通过扫描，获取周边IBeacon广播包信息。 |

例如：查询当前的搜索模式。在输入框输入AT+MODE，即可查询当前模块的搜索模式。

![img](zh_img/new(54).png)

 

更多命令介绍，请查看[5.6.5](#AT指令集)的AT指令集，和附带的DX-BT24系列数据手册。

------



#####  **控制从机**

![img](zh_img/new(56).png)

 

本次使用的从机设备为本公司的BT24蓝牙模块，如下。***\*注意：仅做教程使用，包装中不附带此蓝牙模块产品，如有需要，请单独下单。\****

链接：

https://www.keyestudio.com/products/keyestudio-wireless-data-transmission-dailog-14531-chip-dx-bt24-v51-bluetooth-module-

 

蓝牙从机模块的AT指令通信使用教程，和主机的相同，区别在于AT指令略有不同。

我们按照主机的操作方式，打开ArduinoIDE，选定串口和波特率，发送AT来进行通信测试，成功则返回OK。

![img](zh_img/new(57).png)

------

 

**AT指令：查询版本号**。在ArduinoIDE输入框输入AT+VERSION，会回应蓝牙模块软件版本号。

![img](zh_img/new(58).png)

------

 

**AT指令：蓝牙名称的查询和更改**。先查询蓝牙名称，在输入框里输入AT+NAME。

更改从蓝牙名称，例如：输入AT+NAMEBT24 Slave，把蓝牙名称改为BT24 Slave。

![img](zh_img/new(59).png)

------

 

**AT指令：查询设备MAC地址（只有从设备有此AT指令）**。在输入框输入AT+LADDR，即可返回设备的MAC地址，主机想要和从机连接时，正是用此地址来连接从机。

![img](zh_img/new(60).png)

------



#### **AT指令集**

适用于BT24系列蓝牙主从模块。

链接：https://www.keyestudio.com/search/?Keyword=bt-24

***\*注意：只有主机蓝牙模块才能查询和设置模式（MODE），只有从机蓝牙模块才能查询MAC地址。设置完指令后需重启蓝牙模块以生效，以下为主机AT指令集。\****

| 编号 |       功能       |        指令         |                             响应                             |                             说明                             |
| :--: | :--------------: | :-----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  1   |     测试指令     |         AT          |                              OK                              |                         用于测试串口                         |
|  2   |    查询版本号    |     AT+VERSION      |                     +VERSION=\<version>                      |  \<version >软件版本号依据不同的模块与定制需求版本会有区别   |
|  3   |  查询 MAC 地址   |      AT+LADDR       |                       +LADDR=\<laddr>                        |                   \<laddr>蓝牙 MAC 地址码                    |
|  4   |    查询蓝牙名    |       AT+NAME       |                        +NAME=\<name>                         |        \<name>蓝牙名，最长为 28 个字节默认名称：BT24         |
|  5   |    设置蓝牙名    |   AT+NAME\<name>    |                       +NAME=\<name>OK                        |                                                              |
|  6   |  查询串口停止位  |       AT+STOP       |                        +STOP=\<param>                        |         \<param>序号0：1 停止位1：2 停止位,默认值：0         |
|  7   |  设置串口停止位  |   AT+STOP\<param>   |                       +STOP=\<param>OK                       |                                                              |
|  8   |  查询串口校验位  |       AT+PARI       |                        +PARI=\<param>                        |          \<param>序号0：无校验 1：奇校验 2：偶校验           |
|  9   |  设置串口校验位  |       AT+PARI       |                  +PARI=\<param>查询波特率OK                  |                                                              |
|  10  |    查询波特率    |       AT+BAUD       |                        +BAUD=\<baud>                         | \<baud>波特率对应序号1:24005: 384002:48006: 576003:96007:1152004: 19200 默认值：3(9600) |
|  11  |    设置波特率    |   AT+BAUD\<baud>    |                       +BAUD=\<baud>OK                        |                                                              |
|  12  | 查询模块搜索模式 |       AT+MODE       |                        + MODE\<Param>                        | \<param>(0、1、2、3)0：普通模式1：过滤厂商信息2：配对模式3：获取 IBEACON 信息模式,默认值：0 |
|  13  | 设置模块搜索模式 |   AT+MODE\<Param>   |                       + MODE\<Param>OK                       |                                                              |
|  14  |     断开连接     |       AT+DISC       |                                                              |                                                              |
|  15  |     软件重启     |      AT+RESET       |                       +RESETOKPower On                       |                                                              |
|  16  |   恢复出厂设置   |     AT+DEFAULT      |                      +DEFAULTOKPower On                      |                                                              |
|  17  | 查询过滤信号强度 |     AT+SCANRSSI     |                       +SCANRSSI\<rssi>                       |          < rssi>信号强度 1-100(十进制),默认值：100           |
|  18  | 设置过滤信号强度 | AT+SCANRSSI\<rssi>  |                              OK                              |                                                              |
|  19  | 查询搜索时间长度 |     AT+TIMEINQ      |                       +TIMEINQ\<time>                        |             \<time>时间(1-200) *100ms,默认值：10             |
|  20  | 设置搜索时间长度 |  AT+TIMEINQ\<time>  |                              OK                              |                                                              |
|  21  |   连接蓝牙设备   |   AT+CONN\<param>   |            +Connecting>>\<mac>+Connected>>\<mac>             |                   \<param>序号\<mac>地址码                   |
|  22  |   搜索蓝牙设备   |       AT+INQ        | OK+INQS+INQ:\<param>,\<mac>,\<rssi>,\<name>+INQ:\<param>,\<mac>,\<rssi>,\<name>……+INQEDevices Found \<x> | \<param>序号\<mac>地址码\<rssi>信号值\<name>设置名称\<x>个数(最大为 8) |
|  23  |   连接蓝牙设备   |    AT+CONA\<mac>    |            +Connecting>>\<mac>+Connected>>\<mac>             |                         \<mac>地址码                         |
|  24  | 查询绑定蓝牙地址 |       AT+BIND       |                         +BAND\<mac>                          |                         \<mac>地址码                         |
|  25  | 设置绑定蓝牙地址 |    AT+BIND\<mac>    |                              OK                              |                                                              |
|  26  | 查询模块连接模式 |     AT+AUTOCONN     |                      +AUTOCONN\<param>                       |            \<param>(0、1)0：关闭1：打开,默认值：0            |
|  27  | 设置模块连接模式 | AT+AUTOCONN\<param> |                              OK                              |                                                              |
|  28  |   清除连接记忆   |      AT+CLEAR       |                              OK                              |                                                              |

------

错误码一览表：

| 编号 | 返回值 | 错误信息说明 |
| :--: | :----: | :----------: |
|  1   |  101   | 参数长度错误 |
|  2   |  102   | 参数格式错误 |
|  3   |  103   | 参数数据异常 |
|  4   |  104   |   指令错误   |

------



#### **蓝牙主机连接从机**

蓝牙主机与蓝牙从机设备之间的配对，需要AT指令进行连接，两个蓝牙设置好后，上电即可自动连接。

------

操作步骤为：

1. 蓝牙主机和从机设备都需要设置相同的波特率。设置主机与从机设备的波特率AT指令一致，先设置好主设备，再设置从设备（此处将两个设备设置的波特率为115200，蓝牙模块默认为9600），然后使用RESET将蓝牙设备重启。

​	AT指令1：**AT+BAUD7**

​	AT指令2：**AT+RESET**

![img](zh_img/new(61).png)

 

------



2. 将主模块模式设置为模式2，发送**AT+MODE2**，然后再将模块设置为自动连接，即发送**AT+AUTOCONN1**。

![img](zh_img/new(62).png)

 

![img](zh_img/new(63).png)

 

 

------



3. 让从模块进入配对模式，发送配对模式指令：**AT+SEADV534d4152542d00**，让模块进入到配对模式。如需退出配对模式，发送**AT+CLEARADV**进行清除。

![img](zh_img/new(64).png)

 

4. 把主机和从机两个蓝牙模块上电，主机模块会连接上从模块，主模块将对从模块蓝牙地址码进行绑定，即使掉电或者断开后，主模块还会自动连接该从模块。

​	如需清除绑定，发送**AT+CLEAR**或者使用按键进行清除。

![img](zh_img/new(65).png)

​	两个主从蓝牙设备联机后，主设备上的LED灯会持续亮，而从模块上的LED灯，每个3秒左右会闪烁一次。根据以上操作，两主从设备的蓝牙模块，就可以进			行无线数据的传输。

------



#### **蓝牙主从机通信**

我们用主机给从机蓝牙模块进行发送信息。

1. 首先我们将主机蓝牙模块，安装在扩展板上，给ArduinoNANO烧录测试代码。***\*注意：烧录代码时，请取下蓝牙模块，烧录完后，再安装蓝牙模块。\****

​	代码请查看资料中提供的lesson_3_1文件夹。

​	代码如下：

[lesson_3_1.ino]:

```c++
void setup() {

Serial.begin(115200);//初始化串口，之前把蓝牙的波特率设置为115200

}

void loop() {

Serial.println("A");

delay(500);

Serial.println("B");

delay(500);

}
```

------



2. 我们先使用USB转串口模块，将从机蓝牙模块与电脑连接，选择正确的串口号，设置波特率为115200，此时从机可以接收到信息，看到串口每隔0.5秒循环交替打印“A”和“B”。

![img](zh_img/new(66).png)

 

------



### **控制麦克纳姆轮小车**

现在我们进入实战阶段，我们用体感智能手套的姿态，来控制小车。例如：我们将手往上抬，来控制小车的前进，往下抬控制来控制小车的后退等等。体感运动手套完整的安装教程，请查看附录：安装步骤。

麦克纳姆轮小车链接：

https://www.keyestudio.com/search/?Keyword=mecanum

![img](zh_img/new(67).png)

 

当然，他不仅可以控制小车，而且还可以与我们公司的其他产品搭配使用，比如坦克车、智能房车和Beetlebot小车，通过手势来控制他们。

坦克车、智能房车和Beetlebot小车等链接：

https://www.keyestudio.com/search/?&Keyword=car&Sort=4d&page=1

![img](zh_img/new(68).png)

 

------



#### **手势角度**

注意：由于体感运动手套仅配备了MPU6050，偏航角（Yaw)会出现零飘，数据不准确。所以在教程中，只获取翻滚(roll)、俯仰(pitch)两个角度，***\*如需获取完整的三轴角度，请搭配磁力计来校准MPU6050。\****

根据我们所安装的体感运动手套，我们先了解整体的方向。手指朝前，手掌左右翻滚，这是在绕Y轴运动。手不移动的情况下为0°，手往左边向下滚动为负数（-180°），往右向下滚动则为正数（+180°）。

![img](zh_img/new(69).png)

 

------

手指朝前，以手掌心为中心，手上下移动，这是在绕X轴旋转。手不移动的情况下为0°，手往上抬为正数（+180°），手往下放为负数（-180°）。

![img](zh_img/new(70).png)

 

------



#### **手势角度代码**

我们先预设几个手势动作，左翻滚、右翻滚、上抬和下压这四个动作，给它们都定一个角度范围，当手势动作到达了这个范围值，即可判定为某个特定动作。

1. 水平：X和Y轴大于-40°，并且小于40°，设定为手水平平衡放着。

2. 左翻滚：以Y轴为参考轴，设定-40~-90°为左翻滚的范围。

3. 右翻滚：以Y轴为参考轴，设定40~90°为右翻滚的范围。

4. 上抬手：以X轴为参考轴，设定40~90°为上抬手的范围。

5. 下放手：以X轴为参考轴，设定-40~-90°为下放手的范围。

可自行修改范围，具体实现代码，请查看资料中提供的lesson_4_1文件夹。***\*注意：烧录代码时，请取下蓝牙模块，烧录完后，再安装蓝牙模块。\****

烧录完代码后打开串口，即可看到手势数据。

![img](zh_img/new(71).png)

 

代码如下：

[lesson_4_1.ino]:

```c++
#include "MPU6050.h"

MPU6050lib mpu;

 

float aRes, gRes;        //传感器的每个LSB的刻度分辨率 scale resolutions per LSB for the sensors

int16_t accelCount[3];      //存储16位符号加速度计传感器输出 Stores the 16-bit signed accelerometer sensor output

int16_t gyroCount[3];      //存储16位符号陀螺传感器输出 Stores the 16-bit signed gyro sensor output

float ax, ay, az;        //在g中存储真正的加速度值 Stores the real accel value in g's

float gyrox, gyroy, gyroz;    //存储真实的陀螺仪值，单位为度/秒 Stores the real gyro value in degrees per seconds

float gyroBias[3] = {0, 0, 0};

float accelBias[3] = {0, 0, 0}; //陀螺仪和加速度计的偏差校正 Bias corrections for gyro and accelerometer

int16_t tempCount;        //存储真正的内部芯片温度摄氏度 Stores the real internal chip temperature in degrees Celsius

float temperature;

float SelfTest[6];

float q[4] = {1.0f, 0.0f, 0.0f, 0.0f};// vector to hold quaternion

float pitch, yaw, roll;

//6自由度传感器融合计算参数 parameters for 6 DoF sensor fusion calculations

float GyroMeasError = PI * (40.0f / 180.0f);    // 陀螺仪测量误差以拉德/秒为单位(从60度/秒开始)，然后在~10秒后减小到3gyroscope measurement error in rads/s (start at 60 deg/s), then reduce after ~10 s to 3

float beta = sqrt(3.0f / 4.0f) * GyroMeasError;  // 计算β compute beta

float GyroMeasDrift = PI * (2.0f / 180.0f);    // 陀螺仪测量漂移(rad/s/s)(从0.0度/s/s开始)gyroscope measurement drift in rad/s/s (start at 0.0 deg/s/s)

float zeta = sqrt(3.0f / 4.0f) * GyroMeasDrift;  // 计算zeta, Madgwick格式中的另一个自由参数通常设置为一个小值或零值compute zeta, the other free parameter in the Madgwick scheme usually set to a small or zero value

float deltat = 0.0f;                // 两种滤波方案的积分区间integration interval for both filter schemes

uint32_t lastUpdate = 0, firstUpdate = 0;     // 用于计算积分区间used to calculate integration interval

uint32_t Now = 0;                 // 用于计算积分区间used to calculate integration interval

 

void setup()

{

 Wire.begin();

 Serial.begin(9600);

 

 // Read the WHO_AM_I register, this is a good test of communication

 uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050); // Read WHO_AM_I register for MPU-6050

 Serial.print("I AM ");

 Serial.println(c, HEX);

 

 mpu.settings(AFS_8G, GFS_250DPS);

 if (c == 0x68) //WHO_AM_I应该总是0x68 WHO_AM_I should always be 0x68

 {

  Serial.println("MPU6050 is online...");

  //从执行自检和报告值开始 Start by performing self test and reporting values

  mpu.MPU6050SelfTest(SelfTest); 

  Serial.print("x-axis self test: acceleration trim within : "); Serial.print(SelfTest[0],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: acceleration trim within : "); Serial.print(SelfTest[1],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: acceleration trim within : "); Serial.print(SelfTest[2],1); Serial.println("% of factory value");

  Serial.print("x-axis self test: gyration trim within : "); Serial.print(SelfTest[3],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: gyration trim within : "); Serial.print(SelfTest[4],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: gyration trim within : "); Serial.print(SelfTest[5],1); Serial.println("% of factory value");

 

  if (SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f && SelfTest[5] < 1.0f) {

   Serial.println("Pass Selftest!");

   //校准陀螺和加速度计，在偏置寄存器中加载偏置 Calibrate gyro and accelerometers, load biases in bias registers

   mpu.calibrateMPU6050(gyroBias, accelBias); 

   Serial.println("MPU6050 bias");

   Serial.println(" x\t  y\t  z  ");

   Serial.print((int)(1000 * accelBias[0])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[1])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[2]));

   Serial.println(" mg");

 

   Serial.print(gyroBias[0], 1); Serial.print('\t');

   Serial.print(gyroBias[1], 1); Serial.print('\t');

   Serial.print(gyroBias[2], 1);

   Serial.println(" o/s");

 

   mpu.settings(AFS_2G, GFS_250DPS);

   mpu.initMPU6050(); 

   //初始化设备的主动模式读数 加速度计，陀螺仪，和温度 Initialize device for active mode read of acclerometer, gyroscope, and temperature

   Serial.println("MPU6050 initialized for active data mode...."); 

  }

 }

 else

 {

  Serial.print("Could not connect to MPU6050: 0x");

  Serial.println(c, HEX);

  while(1); //如果通信没有发生，则永远循环 Loop forever if communication doesn't happen

 }

}
 

void loop()

{

 //如果设置了数据就绪位，则所有数据寄存器都有新数据 If data ready bit set, all data registers have new data

 if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) { //检查数据是否准备 check if data ready interrupt

  mpu.readAccelData(accelCount);   //读取x/y/z adc值 Read the x/y/z adc values

  aRes = mpu.getAres();       //获取转换值


  //现在我们将加速度值计算为实际的g Now we'll calculate the accleration value into actual g's

  ax = (float)accelCount[0] * aRes; //得到实际的g值，这取决于所设置的比例 get actual g value, this depends on scale being set

  ay = (float)accelCount[1] * aRes;

  az = (float)accelCount[2] * aRes;


  mpu.readGyroData(gyroCount);    //读取x/y/z adc值 Read the x/y/z adc values

  gRes = mpu.getGres();       //获取转换值


  //计算陀螺值为实际度每秒 Calculate the gyro value into actual degrees per second

  gyrox = (float)gyroCount[0] * gRes; //获得实际的陀螺值，这取决于刻度被设置 get actual gyro value, this depends on scale being set

  gyroy = (float)gyroCount[1] * gRes;

  gyroz = (float)gyroCount[2] * gRes;


  tempCount = mpu.readTempData(); //读取x/y/z adc值 Read the x/y/z adc values

  temperature = ((float) tempCount) / 340. + 36.53; //温度(摄氏度) Temperature in degrees Centigrade

 }

 //获取系统当前微秒时间

 Now = micros();

 //按自上次过滤器更新以来经过的时间设置集成时间 set integration time by time elapsed since last filter update

 deltat = ((Now - lastUpdate) / 1000000.0f);

 lastUpdate = Now;

 if(lastUpdate - firstUpdate > 10000000uL) {

  beta = 0.041; //稳定后降低滤波器增益 decrease filter gain after stabilized

  zeta = 0.015; //稳定后增加陀螺偏压漂移增益 increase gyro bias drift gain after stabilized

 }

 // 陀螺仪数据转换为弧度

 gyrox = gyrox  * PI / 180.0f;

 gyroy = gyroy * PI / 180.0f;

 gyroz = gyroz * PI / 180.0f;

 // 四元素转换函数

 MadgwickQuaternionUpdate(ax, ay, az, gyrox, gyroy, gyroz);


 // Define output variables from updated quaternion---these are Tait-Bryan angles, commonly used in aircraft orientation.

 // In this coordinate system, the positive z-axis is down toward Earth.

 // Yaw is the angle between Sensor x-axis and Earth magnetic North (or true North if corrected for local declination, looking down on the sensor positive yaw is counterclockwise.

 // Pitch is angle between sensor x-axis and Earth ground plane, toward the Earth is positive, up toward the sky is negative.

 // Roll is angle between sensor y-axis and Earth ground plane, y-axis up is positive roll.

 // These arise from the definition of the homogeneous rotation matrix constructed from quaternions.

 // Tait-Bryan angles as well as Euler angles are non-commutative; that is, the get the correct orientation the rotations must be

 // applied in the correct order which for this configuration is yaw, pitch, and then roll.

 yaw  = atan2(2.0f * (q[1] * q[2] + q[0] * q[3]), q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]);

 pitch = -asin(2.0f * (q[1] * q[3] - q[0] * q[2]));

 roll  = atan2(2.0f * (q[0] * q[1] + q[2] * q[3]), q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]);


 pitch *= 180.0f / PI;

 yaw  *= 180.0f / PI;

 roll  *= 180.0f / PI;

 
 if(40 >= pitch && pitch >= -40 

 && 40 >= roll && roll >= -40){

  Serial.println("Gestures:Horizontal");

 }

 else if (-40 >= pitch && pitch >= -90

 && 40 >= roll && roll >= -40){

  Serial.println("Gestures:Hand to the left");   

 }

 else if (90 >= pitch && pitch >= 40

 && 40 >= roll && roll >= -40){

  Serial.println("Gestures:Hand to the right");   

 }

 else if (-40 >= roll && roll >= -90

 && 40 >= pitch && pitch >= -40){

  Serial.println("Gestures:Hand down");   

 }

 else if (90 >= roll && roll >= 40

 && 40 >= pitch && pitch >= -40){

  Serial.println("Gestures:Hand up");   

 }

 delay(100);

}


// Implementation of Sebastian Madgwick's "...efficient orientation filter for... inertial/magnetic sensor arrays"

// (see http://www.x-io.co.uk/category/open-source/ for examples and more details)

// which fuses acceleration and rotation rate to produce a quaternion-based estimate of relative

// device orientation -- which can be converted to yaw, pitch, and roll. Useful for stabilizing quadcopters, etc.

// The performance of the orientation filter is at least as good as conventional Kalman-based filtering algorithms

// but is much less computationally intensive---it can be performed on a 3.3 V Pro Mini operating at 8 MHz!

void MadgwickQuaternionUpdate(float ax, float ay, float az, float gyrox, float gyroy, float gyroz)

{

 float q1 = q[0], q2 = q[1], q3 = q[2], q4 = q[3];     //为便于阅读，简称局部变量 short name local variable for readability

 float norm;                        //向量范数 vector norm

 float f1, f2, f3;                     //目标功能元素 objetive funcyion elements

 float J_11or24, J_12or23, J_13or22, J_14or21, J_32, J_33; //目标函数雅可比矩阵 objective function Jacobian elements

 float qDot1, qDot2, qDot3, qDot4;

 float hatDot1, hatDot2, hatDot3, hatDot4;

 float gerrx, gerry, gerrz, gbiasx, gbiasy, gbiasz;     //陀螺偏压误差 gyro bias error


 //辅助变量避免重复运算 Auxiliary variables to avoid repeated arithmetic

 float _halfq1 = 0.5f * q1;

 float _halfq2 = 0.5f * q2;

 float _halfq3 = 0.5f * q3;

 float _halfq4 = 0.5f * q4;

 float _2q1 = 2.0f * q1;

 float _2q2 = 2.0f * q2;

 float _2q3 = 2.0f * q3;

 float _2q4 = 2.0f * q4;

 float _2q1q3 = 2.0f * q1 * q3;

 float _2q3q4 = 2.0f * q3 * q4;


 //规范化加速度计测量 Normalise accelerometer measurement

 norm = sqrt(ax * ax + ay * ay + az * az);

 if (norm == 0.0f) return; // handle NaN

 norm = 1.0f/norm;

 ax *= norm;

 ay *= norm;

 az *= norm;


 //计算目标函数和雅可比矩阵 Compute the objective function and Jacobian

 f1 = _2q2 * q4 - _2q1 * q3 - ax;

 f2 = _2q1 * q2 + _2q3 * q4 - ay;

 f3 = 1.0f - _2q2 * q2 - _2q3 * q3 - az;

 J_11or24 = _2q3;

 J_12or23 = _2q4;

 J_13or22 = _2q1;

 J_14or21 = _2q2;

 J_32 = 2.0f * J_14or21;

 J_33 = 2.0f * J_11or24;


 //计算梯度(矩阵乘法) Compute the gradient (matrix multiplication)

 hatDot1 = J_14or21 * f2 - J_11or24 * f1;

 hatDot2 = J_12or23 * f1 + J_13or22 * f2 - J_32 * f3;

 hatDot3 = J_12or23 * f2 - J_33 *f3 - J_13or22 * f1;

 hatDot4 = J_14or21 * f1 + J_11or24 * f2;


 //将梯度归一化 Normalize the gradient

 norm = sqrt(hatDot1 * hatDot1 + hatDot2 * hatDot2 + hatDot3 * hatDot3 + hatDot4 * hatDot4);

 hatDot1 /= norm;

 hatDot2 /= norm;

 hatDot3 /= norm;

 hatDot4 /= norm;


 //计算估计陀螺仪偏差 Compute estimated gyroscope biases

 gerrx = _2q1 * hatDot2 - _2q2 * hatDot1 - _2q3 * hatDot4 + _2q4 * hatDot3;

 gerry = _2q1 * hatDot3 + _2q2 * hatDot4 - _2q3 * hatDot1 - _2q4 * hatDot2;

 gerrz = _2q1 * hatDot4 - _2q2 * hatDot3 + _2q3 * hatDot2 - _2q4 * hatDot1;
 

 //计算和消除陀螺仪偏差 Compute and remove gyroscope biases

 gbiasx += gerrx * deltat * zeta;

 gbiasy += gerry * deltat * zeta;

 gbiasz += gerrz * deltat * zeta;

 gyrox -= gbiasx;

 gyroy -= gbiasy;

 gyroz -= gbiasz;
 

 //计算四元数的导数 Compute the quaternion derivative

 qDot1 = -_halfq2 * gyrox - _halfq3 * gyroy - _halfq4 * gyroz;

 qDot2 =  _halfq1 * gyrox + _halfq3 * gyroz - _halfq4 * gyroy;

 qDot3 =  _halfq1 * gyroy - _halfq2 * gyroz + _halfq4 * gyrox;

 qDot4 =  _halfq1 * gyroz + _halfq2 * gyroy - _halfq3 * gyrox;


 //计算，然后积分估计四元数的导数 Compute then integrate estimated quaternion derivative

 q1 += (qDot1 -(beta * hatDot1)) * deltat;

 q2 += (qDot2 -(beta * hatDot2)) * deltat;

 q3 += (qDot3 -(beta * hatDot3)) * deltat;

 q4 += (qDot4 -(beta * hatDot4)) * deltat;

 
 //四元数归一化 Normalize the quaternion

 norm = sqrt(q1 * q1 + q2 * q2 + q3 * q3 + q4 * q4);   // 标准化四元数 normalise quaternion

 norm = 1.0f/norm;

 q[0] = q1 * norm;

 q[1] = q2 * norm;

 q[2] = q3 * norm;

 q[3] = q4 * norm;

}
```

------



#### **控制小车代码**

接下来，我们来完成体感手套控制麦克纳姆轮的代码。

![img](zh_img/new(72).png)

 

------

基于麦克纳姆轮技术的全方位的小车，可以实现前行、横移、[斜行](https://baike.baidu.com/item/斜行/5135999?fromModule=lemma_inlink)、旋转及其组合等运动方式。这种全方位移动方式是基于一个有许多位于[机轮](https://baike.baidu.com/item/机轮/5308297?fromModule=lemma_inlink)周边的[轮轴](https://baike.baidu.com/item/轮轴/1872661?fromModule=lemma_inlink)的中心轮的原理上，这些成角度的周边轮轴把一部分的机轮转向力转化到一个机轮[法向力](https://baike.baidu.com/item/法向力/9444144?fromModule=lemma_inlink)上面。

![img](zh_img/new(73).png)

 

 麦克纳姆轮小车链接：https://www.keyestudio.com/search/?Keyword=mecanum

 

麦克纳姆轮小车四个电机单独工作，具有多方位运动，其灵活性使得它可以轻松适应不同的环境和条件。

 

![img](zh_img/new(74).png)

 

使用体感智能手套控制小车时，需要与小车上的蓝牙进行配对，通过AT指令，使主机和从机蓝牙模块相连接，此时，我们的体感手套就是主机，小车就是从机。

------

操作主机蓝牙模块的AT指令：

- AT指令1：***AT+BAUD7*** 设置蓝牙的波特率为115200，也可以设置其他波特率

- AT指令2：**AT+RESET** 重启蓝牙

- AT指令3：**AT+RESET** 设置为模式2，打开配对模式

- AT指令4：**AT+AUTOCONN1** 设置成上电自动配对连接

------

操作从机蓝牙模块的AT指令：

​	AT指令：**AT+SEADV534d4152542d00** 让从机进入配对模式，上电自动连接

具体步骤，可参照[5.6.6 蓝牙主机连接从机](#蓝牙主机连接从机)。

------

我们还需要定义不同的动作姿态对应的功能，如左倾斜≥-40°表示左转，右倾斜≥40°表示右转等，扩展板上还带有两个按键，可通过按键，切换对小车的功能控制。

------

主机端体感运动手套的定义：（可根据自己的需求，设定角度和对应的功能）

第一种手势：

|     手势     |         欧拉角数值          |             功能             |
| :----------: | :-------------------------: | :--------------------------: |
| 上抬手40~60° |       -40°≥pitch≥-60°       | Serial.print("a")；发送a前进 |
| 下放手40~60° |        40°≥pitch≥60°        | Serial.print("c")；发送c后退 |
| 左翻滚40~60° |       -40°≥roll≥-60°        | Serial.print("b")；发送b左转 |
| 右翻滚40~60° |        40°≥roll≥60°         | Serial.print("d")；发送d右转 |
|   水平不动   | 40°≥pitch≥-40°40°≥roll≥-40° | Serial.print("s")；发送s停止 |

------

第二种手势：

|    欧拉角数值    |     手势      |              功能              |
| :--------------: | :-----------: | :----------------------------: |
| -60°≥pitch≥-120° | 上抬手60~120° | Serial.print("f")；发送f左漂移 |
|  60°≥pitch≥120°  | 下放手60~120° | Serial.print("e")；发送e右漂移 |
| -60°≥roll≥-120°  | 左翻滚60~120° |  Serial.print("k")；发送k左移  |
|  60°≥roll≥120°   | 右翻滚60~120° |  Serial.print("h")；发送h右移  |

------

第三种按键功能：

- D7按键被按时开七彩灯，再按一次为关七彩灯，

  - 代码：Serial.print("t")；//开


  - 代码：Serial.print("u")；//关




- 
  D8按键被按时开RGB灯，再按一次为关RGB灯

  - 代码：Serial.print("m")；//开


  - 代码：Serial.print("o")；//关


------

从机麦克纳姆轮小车的接口：(可根据接口，自定义手势的功能)

| 接收命令 |       功能       |
| :------: | :--------------: |
|    s     |       停止       |
|    a     |       前进       |
|    c     |       后退       |
|    b     |       左转       |
|    d     |       右转       |
|    k     |       左移       |
|    h     |       右移       |
|    l     |      左上移      |
|    j     |      左下移      |
|    g     |      右上移      |
|    i     |      右下移      |
|    e     |       漂移       |
|    f     |       漂移       |
|    p     |       循迹       |
|    q     |       跟随       |
|    r     |       避障       |
|    t     |     开七彩灯     |
|    u     |     关七彩灯     |
|    m     | 切换2812灯珠颜色 |
|    o     |   关闭2812灯珠   |
|    n     | 切换2812灯珠颜色 |
| x+0~255  |  设置M1电机速度  |
| v+0~255  |  设置M2电机速度  |
| w+0~255  |  设置M3电机速度  |
| y+0~255  |  设置M4电机速度  |

 

具体实现代码，请查看资料中提供的lesson_4_2文件夹。

代码如下：

[lesson_4_2.ino]:

```c++
#include "Wire.h"

#include "MPU6050.h"


MPU6050lib mpu;


float aRes, gRes;        //传感器的每个LSB的刻度分辨率 scale resolutions per LSB for the sensors

int16_t accelCount[3];      //存储16位符号加速度计传感器输出 Stores the 16-bit signed accelerometer sensor output

int16_t gyroCount[3];      //存储16位符号陀螺传感器输出 Stores the 16-bit signed gyro sensor output

float SelfTest[6];

float gyroBias[3] = {0, 0, 0};

float accelBias[3] = {0, 0, 0}; //陀螺仪和加速度计的偏差校正 Bias corrections for gyro and accelerometer

float q[4] = {1.0f, 0.0f, 0.0f, 0.0f};// vector to hold quaternion

float pitch, yaw, roll;

//6自由度传感器融合计算参数 parameters for 6 DoF sensor fusion calculations

float GyroMeasError = PI * (40.0f / 180.0f);    // 陀螺仪测量误差以拉德/秒为单位(从60度/秒开始)，然后在~10秒后减小到3gyroscope measurement error in rads/s (start at 60 deg/s), then reduce after ~10 s to 3

float beta = sqrt(3.0f / 4.0f) * GyroMeasError;  // 计算β compute beta

float GyroMeasDrift = PI * (2.0f / 180.0f);    // 陀螺仪测量漂移(rad/s/s)(从0.0度/s/s开始)gyroscope measurement drift in rad/s/s (start at 0.0 deg/s/s)

float zeta = sqrt(3.0f / 4.0f) * GyroMeasDrift;  // 计算zeta, Madgwick格式中的另一个自由参数通常设置为一个小值或零值compute zeta, the other free parameter in the Madgwick scheme usually set to a small or zero value

float deltat = 0.0f;                // 两种滤波方案的积分区间integration interval for both filter schemes

uint32_t lastUpdate = 0, firstUpdate = 0;     // 用于计算积分区间used to calculate integration interval

uint32_t Now = 0;                 // 用于计算积分区间used to calculate integration interval

double ax,ay,az; //滤波器的输出

double gyrox,gyroy,gyroz; //滤波器的输出

int btnA = 7; //定义两个按钮

int btnB = 8;

int btnAv = 0;  //获取两个按钮的值

int btnBv = 0;

 

void setup()

{

 Wire.begin();

 Serial.begin(115200);


 uint8_t c = mpu.readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050);  // Read WHO_AM_I register for MPU-6050

 Serial.print("I AM ");

 Serial.println(c, HEX);

 mpu.settings(AFS_8G, GFS_250DPS);

 if (c == 0x68) //WHO_AM_I应该总是0x68 WHO_AM_I should always be 0x68

 {

  Serial.println("MPU6050 is online...");

  //从执行自检和报告值开始 Start by performing self test and reporting values

  mpu.MPU6050SelfTest(SelfTest); 

  Serial.print("x-axis self test: acceleration trim within : "); Serial.print(SelfTest[0],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: acceleration trim within : "); Serial.print(SelfTest[1],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: acceleration trim within : "); Serial.print(SelfTest[2],1); Serial.println("% of factory value");

  Serial.print("x-axis self test: gyration trim within : "); Serial.print(SelfTest[3],1); Serial.println("% of factory value");

  Serial.print("y-axis self test: gyration trim within : "); Serial.print(SelfTest[4],1); Serial.println("% of factory value");

  Serial.print("z-axis self test: gyration trim within : "); Serial.print(SelfTest[5],1); Serial.println("% of factory value");

 

  if (SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f && SelfTest[5] < 1.0f) {

   Serial.println("Pass Selftest!");

   //校准陀螺和加速度计，在偏置寄存器中加载偏置 Calibrate gyro and accelerometers, load biases in bias registers

   mpu.calibrateMPU6050(gyroBias, accelBias); 

   Serial.println("MPU6050 bias");

   Serial.println(" x\t  y\t  z  ");

   Serial.print((int)(1000 * accelBias[0])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[1])); Serial.print('\t');

   Serial.print((int)(1000 * accelBias[2]));

   Serial.println(" mg");

 

   Serial.print(gyroBias[0], 1); Serial.print('\t');

   Serial.print(gyroBias[1], 1); Serial.print('\t');

   Serial.print(gyroBias[2], 1);

   Serial.println(" o/s");

 

   mpu.settings(AFS_8G, GFS_2000DPS);

   mpu.initMPU6050(); 

   //初始化设备的主动模式读数 加速度计，陀螺仪，和温度 Initialize device for active mode read of acclerometer, gyroscope, and temperature

   Serial.println("MPU6050 initialized for active data mode...."); 

  }

 }

 else

 {

  Serial.print("Could not connect to MPU6050: 0x");

  Serial.println(c, HEX);

  while(1); //如果通信没有发生，则永远循环 Loop forever if communication doesn't happen

 }

 for(int i = 0; i < 300;i++){

  if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) { //检查数据是否准备 check if data ready interrupt

   mpu.readAccelData(accelCount);   //读取x/y/z adc值 Read the x/y/z adc values

   mpu.readGyroData(gyroCount);    //读取x/y/z adc值 Read the x/y/z adc values

  }

 }

}

 

void loop()

{

 //如果设置了数据就绪位，则所有数据寄存器都有新数据 If data ready bit set, all data registers have new data

 if (mpu.readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) { //检查数据是否准备 check if data ready interrupt

  mpu.readAccelData(accelCount);   //读取x/y/z adc值 Read the x/y/z adc values

  // Kalman_Filter(accelCount[0],accelCount[1],accelCount[2]);

  //现在我们将加速度值计算为实际的g Now we'll calculate the accleration value into actual g's

  aRes = mpu.getAres();//获取转换值

  ax = (float)accelCount[0] * aRes; //得到实际的g值，这取决于所设置的比例 get actual g value, this depends on scale being set

  ay = (float)accelCount[1] * aRes;

  az = (float)accelCount[2] * aRes;

 

  mpu.readGyroData(gyroCount);    //读取x/y/z adc值 Read the x/y/z adc values

  // Kalman_Filter(gyroCount[0],gyroCount[1],gyroCount[2]);

  gRes = mpu.getGres();       //获取转换值

  //计算陀螺值为实际度每秒 Calculate the gyro value into actual degrees per second

  gyrox = (float)gyroCount[0] * gRes;//获得实际的陀螺值，这取决于刻度被设置 get actual gyro value, this depends on scale being set

  gyroy = (float)gyroCount[1] * gRes;

  gyroz = (float)gyroCount[2] * gRes;


 }

 //获取系统当前微秒时间

 Now = micros();

 //按自上次过滤器更新以来经过的时间设置集成时间 set integration time by time elapsed since last filter update

 deltat = ((Now - lastUpdate) / 1000000.0f);

 lastUpdate = Now;

 if(lastUpdate - firstUpdate > 10000000uL) {

  beta = 0.041; //稳定后降低滤波器增益 decrease filter gain after stabilized

  zeta = 0.015; //稳定后增加陀螺偏压漂移增益 increase gyro bias drift gain after stabilized

 }

 // 陀螺仪数据转换为弧度

 gyrox = gyrox  * PI / 180.0f;

 gyroy = gyroy * PI / 180.0f;

 gyroz = gyroz * PI / 180.0f;

 // 四元素转换函数

 MadgwickQuaternionUpdate(ax, ay, az, gyrox, gyroy, gyroz);


 // yaw  = atan2(2.0f * (q[1] * q[2] + q[0] * q[3]), q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]);

 pitch = -asin(2.0f * (q[1] * q[3] - q[0] * q[2]));

 roll  = atan2(2.0f * (q[0] * q[1] + q[2] * q[3]), q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]);


 pitch *= 180.0f / PI;

 yaw  *= 180.0f / PI;

 roll  *= 180.0f / PI;


 //按钮A

 if(!digitalRead(btnA))

 {

  delay(100);

  if(!digitalRead(btnA))

  {

   btnAv = ~btnAv;

  }

 }

 //按钮B

 if(!digitalRead(btnB))

 {

  delay(100);

  if(!digitalRead(btnB))

  {

   btnBv = ~btnBv;

  }

 }

 // Serial.print("roll:");Serial.println(roll);

 // Serial.print("pitch:");Serial.println(pitch);


 if(btnAv == -1) Serial.println("t");//控制麦伦车：开七彩灯

 else Serial.print("u");//控制麦伦车：关七彩灯

 if(btnBv == -1) Serial.println("m");//控制麦伦车：切换2812灯珠颜色

 else Serial.print("o");//控制麦伦车：关闭2812灯珠


 if(40 >= pitch && pitch >= -40 

 && 40 >= roll && roll >= -40){

  Serial.print("s");//控制麦伦车：停止

 }

 else if (-40 >= pitch && pitch >= -60

 && 40 >= roll && roll >= -40){

  Serial.print("b");//控制麦伦车：左转

 }

 else if(-60 >= pitch && pitch >= -120

 && 40 >= roll && roll >= -40){

  Serial.print("k");//控制麦伦车：左移

 }

 else if (60>= pitch && pitch >= 40

 && 40 >= roll && roll >= -40){

  Serial.print("d");//控制麦伦车：右转

 }

 else if(120 >= pitch && pitch >= 60

 && 40 >= roll && roll >= -40){

  Serial.print("h");//控制麦伦车：右移

 }

 else if (-40 >= roll && roll >= -60

 && 40 >= pitch && pitch >= -40){

  Serial.print("c");//控制麦伦车：后退

 }

 else if(-60 >= roll && roll >= -120

 && 40 >= pitch && pitch >= -40){

  Serial.print("f");//控制麦伦车：漂移

 }

 else if (60 >= roll && roll >= 40

 && 40 >= pitch && pitch >= -40){

  Serial.print("a");//控制麦伦车：前进

 }

 else if(120 >= roll && roll >= 60

 && 40 >= pitch && pitch >= -40){

  Serial.print("e");//控制麦伦车：漂移

 }

 delay(10);

}


// Implementation of Sebastian Madgwick's "...efficient orientation filter for... inertial/magnetic sensor arrays"

// which fuses acceleration and rotation rate to produce a quaternion-based estimate of relative

// device orientation -- which can be converted to yaw, pitch, and roll. Useful for stabilizing quadcopters, etc.

// The performance of the orientation filter is at least as good as conventional Kalman-based filtering algorithms

// but is much less computationally intensive---it can be performed on a 3.3 V Pro Mini operating at 8 MHz!

void MadgwickQuaternionUpdate(float ax, float ay, float az, float gyrox, float gyroy, float gyroz)

{

 float q1 = q[0], q2 = q[1], q3 = q[2], q4 = q[3];     //为便于阅读，简称局部变量 short name local variable for readability

 float norm;                        //向量范数 vector norm

 float f1, f2, f3;                     //目标功能元素 objetive funcyion elements

 float J_11or24, J_12or23, J_13or22, J_14or21, J_32, J_33; //目标函数雅可比矩阵 objective function Jacobian elements

 float qDot1, qDot2, qDot3, qDot4;

 float hatDot1, hatDot2, hatDot3, hatDot4;

 float gerrx, gerry, gerrz, gbiasx, gbiasy, gbiasz;     //陀螺偏压误差 gyro bias error


 //辅助变量避免重复运算 Auxiliary variables to avoid repeated arithmetic

 float _halfq1 = 0.5f * q1;

 float _halfq2 = 0.5f * q2;

 float _halfq3 = 0.5f * q3;

 float _halfq4 = 0.5f * q4;

 float _2q1 = 2.0f * q1;

 float _2q2 = 2.0f * q2;

 float _2q3 = 2.0f * q3;

 float _2q4 = 2.0f * q4;

 float _2q1q3 = 2.0f * q1 * q3;

 float _2q3q4 = 2.0f * q3 * q4;


 //规范化加速度计测量 Normalise accelerometer measurement

 norm = sqrt(ax * ax + ay * ay + az * az);

 if (norm == 0.0f) return; // handle NaN

 norm = 1.0f/norm;

 ax *= norm;

 ay *= norm;

 az *= norm;


 //计算目标函数和雅可比矩阵 Compute the objective function and Jacobian

 f1 = _2q2 * q4 - _2q1 * q3 - ax;

 f2 = _2q1 * q2 + _2q3 * q4 - ay;

 f3 = 1.0f - _2q2 * q2 - _2q3 * q3 - az;

 J_11or24 = _2q3;

 J_12or23 = _2q4;

 J_13or22 = _2q1;

 J_14or21 = _2q2;

 J_32 = 2.0f * J_14or21;

 J_33 = 2.0f * J_11or24;

 
 //计算梯度(矩阵乘法) Compute the gradient (matrix multiplication)

 hatDot1 = J_14or21 * f2 - J_11or24 * f1;

 hatDot2 = J_12or23 * f1 + J_13or22 * f2 - J_32 * f3;

 hatDot3 = J_12or23 * f2 - J_33 *f3 - J_13or22 * f1;

 hatDot4 = J_14or21 * f1 + J_11or24 * f2;


 //将梯度归一化 Normalize the gradient

 norm = sqrt(hatDot1 * hatDot1 + hatDot2 * hatDot2 + hatDot3 * hatDot3 + hatDot4 * hatDot4);

 hatDot1 /= norm;

 hatDot2 /= norm;

 hatDot3 /= norm;

 hatDot4 /= norm;
 

 //计算估计陀螺仪偏差 Compute estimated gyroscope biases

 gerrx = _2q1 * hatDot2 - _2q2 * hatDot1 - _2q3 * hatDot4 + _2q4 * hatDot3;

 gerry = _2q1 * hatDot3 + _2q2 * hatDot4 - _2q3 * hatDot1 - _2q4 * hatDot2;

 gerrz = _2q1 * hatDot4 - _2q2 * hatDot3 + _2q3 * hatDot2 - _2q4 * hatDot1;


 //计算和消除陀螺仪偏差 Compute and remove gyroscope biases

 gbiasx += gerrx * deltat * zeta;

 gbiasy += gerry * deltat * zeta;

 gbiasz += gerrz * deltat * zeta;

 gyrox -= gbiasx;

 gyroy -= gbiasy;

 gyroz -= gbiasz;


 //计算四元数的导数 Compute the quaternion derivative

 qDot1 = -_halfq2 * gyrox - _halfq3 * gyroy - _halfq4 * gyroz;

 qDot2 =  _halfq1 * gyrox + _halfq3 * gyroz - _halfq4 * gyroy;

 qDot3 =  _halfq1 * gyroy - _halfq2 * gyroz + _halfq4 * gyrox;

 qDot4 =  _halfq1 * gyroz + _halfq2 * gyroy - _halfq3 * gyrox;


 //计算，然后积分估计四元数的导数 Compute then integrate estimated quaternion derivative

 q1 += (qDot1 -(beta * hatDot1)) * deltat;

 q2 += (qDot2 -(beta * hatDot2)) * deltat;

 q3 += (qDot3 -(beta * hatDot3)) * deltat;

 q4 += (qDot4 -(beta * hatDot4)) * deltat;


 //四元数归一化 Normalize the quaternion

 norm = sqrt(q1 * q1 + q2 * q2 + q3 * q3 + q4 * q4);   // 标准化四元数 normalise quaternion

 norm = 1.0f/norm;

 q[0] = q1 * norm;

 q[1] = q2 * norm;

 q[2] = q3 * norm;

 q[3] = q4 * norm;

}
```

------



## **参考链接**

我们公司网址为：

https://www.keyestudio.com/

麦克纳姆轮小车链接：

https://www.keyestudio.com/search/?Keyword=mecanum

USB转串口模块链接：

https://www.keyestudio.com/search/?Keyword=ks0277

蓝牙从机模块链接：

https://www.keyestudio.com/products/keyestudio-wireless-data-transmission-dailog-14531-chip-dx-bt24-v51-bluetooth-module-

MPU6050数据手册网址：

https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf

https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf

Arduino官网网址：

https://www.arduino.cc/

 

------



## **附录**：安装步骤

 

| 步骤  |         图示          |                             说明                             |
| :---: | :-------------------: | :----------------------------------------------------------: |
| 步骤1 | ![img](zh_img/new(75).png) |                     清单（不包含9V电池）                     |
| 步骤2 | ![img](zh_img/new(76).png) | 首先把ArduinoNANO主板安装在扩展板上，USB接口的朝向，根据扩展板上的箭头指示安装。再把蓝牙安装在扩展板上的串口接口 |
| 步骤3 | ![img](zh_img/new(77).png) |    引脚位置如下：(GND--GND) (VCC--VCC) (TX--RX) (RX--TX)     |
| 步骤4 | ![img](zh_img/new(78).png) |             再把MPU6050模块安装在扩展板上的接口              |
| 步骤5 | ![img](zh_img/new(79).png) |  引脚位置如下：(GND--GND) (VCC--VCC) (SDA--SDA) (SCL--SCL)   |
| 步骤6 | ![img](zh_img/new(80).png) | 把扩展板背部的泡棉双面胶撕开，贴在手套（左右手都行）的背部，用手按压扩展板，以让他沾在手套上更稳固。即可完成所有步骤安装。 |
| 步骤7 | ![img](zh_img/new(81).png) |                             成品                             |

------

