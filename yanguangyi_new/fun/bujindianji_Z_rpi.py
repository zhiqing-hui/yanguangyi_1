
import RPi.GPIO as GPIO  # 使用GPIO常量, 例如GPIO.HIGH
from fun.general_io import G_IO  # I2C接口和GPIO接口 统一调用库
# from log import debug, log  # 日志
import time
gio = G_IO(GPIO_mode=GPIO.BCM, i2c_index=1, i2c_addr=0x20)
# gio.setup('I1', GPIO.OUT)


IN1 = "I0"
IN2 = "I1"   # 树莓派的物理引脚与驱动模块连接
IN3 = "I2"
IN4 = "I3"
IN5 = "I4"  ###使能开关
# IN6 = 8    ###Z轴限位

def setStep(h1, h2, h3, h4):
    gio.output(IN1, h1)
    gio.output(IN2, h2)
    gio.output(IN3, h3)
    gio.output(IN4, h4)
    gio.output(IN5, 1)


def setup():
    GPIO.setwarnings(False)
    gio.setup(IN1, GPIO.OUT)  # 设置为输出模式
    gio.setup(IN2, GPIO.OUT)
    gio.setup(IN3, GPIO.OUT)
    gio.setup(IN4, GPIO.OUT)
    gio.setup(IN5, GPIO.OUT)





# gio.setmode(GPIO.BOARD)  # 强制定义命名规则



def stop():
    setStep(0, 0, 0, 0)


def forward(delay, steps):  # A-B-C-D-A通电方式
    for i in range(0, steps):
        setStep(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        time.sleep(delay)
        setStep(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        time.sleep(delay)
        setStep(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW)
        time.sleep(delay)
        setStep(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW)
        time.sleep(delay)


def backward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)


def loop():
    setup()
    while True:
        # forward(0.0000001, 1000)  # 旋转1圈 循环512次
        # stop()
        backward(0.00000001, 1000)  # 旋转1圈 循环512次
        time.sleep(1)


def destroy():
    GPIO.cleanup()  # 释放

loop()
# with picamera.PiCamera() as camera:
#     setup()
#     # camera.resolution = (1024,960)
#     # camera.start_recording('1.h264')
#     # camera.wait_recording()
#     backward(0.003, 512)
#     ###反向旋转一圈后暂停
#     # camera.stop_recording()
#     stop()



