# py_servo

publisherで1sec毎に500-2500(100刻み)のint値を"servo_topic"にpublishする

subscriberでは、"servo_topic"の値を読んで指定したGPIOにパルス(矩形波)をpigpioを使って生成する
(pigpiodが稼働していること)

SG90などのマイクロサーボに負荷を掛けないのであればVDD,GND,PWM(GPIO)にサーボモーターを接続すると動作するはず

|RaspberryPi|SG90|
|--|--|
|3.3V|Vcc(Red)|
|GND|GND(Brown)|
|GPIO18(12)|PWM(Orange)|



```bash
ros2 pkg create --build-type ament_python py_servo
colcon build --packages-select py_servo
cd raspi_ws
. install/setup.bash
ros2 run py_servo talker
ros2 run py_servo listener
```
