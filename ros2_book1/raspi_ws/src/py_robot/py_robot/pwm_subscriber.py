import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import pigpio

PWM_PIN = 22
pi = pigpio.pi()

class PwmSubscriber(Node):
  def __init__(self):
    super().__init__("pwm_subscriber")
    self.subscription = self.create_subscription(
      Int16,
      "pwm_topic",
      self.listener_callback,
      10)
    self.subscription

  def listener_callback(self, msg):
    self.get_logger().info("Subscribed [%d]"%(msg.data))
    p_width = msg.data
    pi.set_pwm_pulsewidth(PWM_PIN, p_width)

def main(args=None):
  try:
    rclpy.init(args=args)
    pwm_subscripber = PwmSubscriber()
    rclpy.spin(pwm_subscripber)
  except KeyboardInterrupt:
    pass
  finally:
    pwm_subscripber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
  