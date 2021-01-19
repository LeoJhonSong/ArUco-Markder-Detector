# ArUco Marker Detector

识别ArUco码并输出**位置, 姿态**到MATLAB程序.

## ArUco码

[在线生成](https://chev.me/arucogen/)

## 环境配置

将根目录下`pip.conf`放到`%APPDATA%\pip\`文件夹下

然后在项目根目录下运行`pip install -r requirements.txt`

## 相机校正

我做了

## ArUco码识别

`python detector.py`运行程序, 应当在终端里看到每个marker的rotation, translation, position. 其中坐标已根据图像大小归一化, 左上角为原点.