import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

# https://mkx99.wiki.fc2.com/wiki/pigpio%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%9C%E3%83%A2%E3%83%BC%E3%82%BF%E3%82%92%E5%8B%95%E3%81%8B%E3%81%99
# pigpio.set_servo_pulsewidth()に渡す値を生成する
# 500-2500の範囲で、500:反時計回り最大、1500:中央、2500:時計回り最大
# サーボによって異なるので要調整

class ServoPublisher(Node):
  def __init__(self):
    super().__init__("servo_publisher")
    self.publisher_ = self.create_publisher(Int16, "servo_topic", 10)
    timer_period = 3
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 500

  def timer_callback(self):
    msg = Int16()
    msg.data = self.i
    self.publisher_.publish(msg)
    self.get_logger().info("Publishing, [%d]"%(msg.data))
    if self.i == 2500:
      self.i = 500
    else:
      self.i += 100

def main(args=None):
  try:
    rclpy.init(args=args)
    servo_publisher = ServoPublisher()
    rclpy.spin(servo_publisher)
  except KeyboardInterrupt:
    pass
  finally:
    servo_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
