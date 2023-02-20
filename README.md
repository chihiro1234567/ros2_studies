# ros2_studies
ROS2の勉強メモとサンプルコード


> 自前でROS2-foxyをインストールしたところ、ラズパイでエラーが発生してしまうケースがあった。
Dockerコンテナ上で実行するのが手っ取り早い。

```bash
> docker pull tiryoh/ros2:foxy-20230205T0228
> docker run -it --rm -v $(pwd):/work tiryoh/ros2:foxy-20230205T0228 bash

$ cd /work
$ colcon build
$ . install/setup.bash
$ ros2 run ...
```

コマンドの実行方法などは各パッケージ内のReadme.mdに記載
