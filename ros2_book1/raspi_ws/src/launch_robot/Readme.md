# launch_robot

py_robotのランチャー

py_robotのパッケージ内にランチャーを作成することも可能だが、
今回はあえて別のパッケージとしてランチャーを定義した。
このように外部パッケージをランチャーすることも可能。


```bash
ros2 pkg create --build-type ament_python launch_robot
colcon build --packages-select launch_robot
cd raspi_ws
. install/setup.bash
ros2 launch launch_robot robot_system.launch.py
```
