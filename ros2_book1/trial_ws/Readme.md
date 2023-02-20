# Dockerでtrial_wsを実行

```bash
> cd trial_ws
> docker compose up -d
```

## trial_topic_pi

```bash
> cd trial_ws
> docker exec -it -u $(id -u):$(id -g) ros2-realsense-container bash
$ cd /home/work/trial_ws
$ colcon build --symlink-install --cmake-clean-cache
$ . install/setup.bash

$ ros2 run trial_topic_pi publisher

2023-02-13 06:41:00.485 [RTPS_TRANSPORT_SHM Error] Failed to create segment e860055311bb4e07: Permission denied -> Function compute_per_allocation_extra_size
2023-02-13 06:41:00.485 [RTPS_MSG_OUT Error] Permission denied -> Function init
[INFO] [1676270462.363545389] [trial_publisher]: Publising Pi, -1.2246467991473532e-16
[INFO] [1676270463.189465554] [trial_publisher]: Publising Pi, 1.2246467991473532e-16
[INFO] [1676270464.191325984] [trial_publisher]: Publising Pi, 1.299038105676658

$ ros2 run trial_topic_pi subscriber

2023-02-13 06:41:23.635 [RTPS_TRANSPORT_SHM Error] Failed to create segment ed1f1859162cab76: Permission denied -> Function compute_per_allocation_extra_size
2023-02-13 06:41:23.635 [RTPS_MSG_OUT Error] Permission denied -> Function init
[INFO] [1676270485.183826019] [trial_publisher]: Publising Pi, 3.105828541230249
[INFO] [1676270486.179176678] [trial_publisher]: Publising Pi, 3.108623589560685
[INFO] [1676270487.178188914] [trial_publisher]: Publising Pi, 3.111103635738251
```

> トラブルシューティング

WSL2 + dockerコンテナ内のROS2で`ros2 run`したときに下記のエラーが出た

```bash
[RTPS_TRANSPORT_SHM Error] Failed to create segment e860055311bb4e07: Permission denied -> Function compute_per_allocation_extra_size
[RTPS_MSG_OUT Error] Permission denied -> Function init
```

DDS通信？で/dev/shmでマウントされた領域を共有メモリとして利用するっぽいが、
WSL2ではマウントされない。(docker-compose.ymlでshm_size指定してもダメ)

ただし`docker run`で以下のように指定すると`/dev/shm`が生成されるので、WSL2ではこれでやるしかない。

```bash
docker run .. --shm-size=512m ...
```

