# ArUco Marker Detector

识别ArUco码并输出**位置, 姿态**到MATLAB程序.

## ArUco码

🔗 [在线生成](https://chev.me/arucogen/)

这种二维码叫ArUco码, 码的大小不重要, 重要的是几乘几的, 要在程序使用的marker集合内.

## 环境配置

先将pip换成国内源, 这样下载包的速度会很快: 项目根目录下`config/pip.conf`复制到`%APPDATA%\pip\`文件夹下.

然后在项目根目录下运行`pip install -r config/requirements.txt`按照需要的包.

## 相机校正

💡 标定板大小不重要, 比例重要.

首先打印一张`chboard.pdf`, 然后用要用来识别marker的摄像头录制一段看这张标定板视频`./ChArUcoBoard.mkv`. 编译出`utils/calibrate_camera_charuco.cpp`并运行`./calibrate_camera_charuco -w=5 -h=7 -sl=200 -ml=120 -d=4 -@outfile="charuco_camera_calibration.yaml" -v="../../ChArUcoBoard.mkv"`, 会输出相机参数文件`charuco_camera_calibration.yaml`.

## ArUco码识别

`python detector.py`运行程序, 应当在终端里看到每个marker的rotation, translation, position. 其中坐标已根据图像大小归一化, 左上角为原点.