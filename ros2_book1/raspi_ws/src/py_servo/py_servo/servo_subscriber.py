import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

import pigpio
SERVO_PIN = 22
pi = pigpio.pi()

class ServoSubscriber(Node):
  def __init__(self):
    super().__init__("servo_subscriber")
    self.subscription = self.create_subscription(
      Int16,
      "servo_topic",
      self.listener_callback,
      10)
    self.subscription

  def listener_callback(self, msg):
    self.get_logger().info("Subscribed [%d]"%(msg.data))
    p_width = msg.data
    pi.set_servo_pulsewidth(SERVO_PIN, p_width)

def main(args=None):
  try:
    rclpy.init(args=args)
    servo_subscripber = ServoSubscriber()
    rclpy.spin(servo_subscripber)
  except KeyboardInterrupt:
    pass
  finally:
    servo_subscripber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
  