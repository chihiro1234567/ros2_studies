# py_sensor

publisherで1sec毎にGPIO18(12)のON/OFFの値を読み取って"sensor_topic"にパブリッシュする

subscriberでは、"sensor_topic"の値を読んでコンソールに表示

```bash
ros2 pkg create --build-type ament_python py_sensor
colcon build --packages-select py_sensor
cd raspi_ws
. install/setup.bash

ros2 run py_sensor talker
ros2 run py_sensor listener
```