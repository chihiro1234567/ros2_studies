import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class SensorSubscriber(Node):
  def __init__(self):
    super().__init__("sensor_subscriber")
    self.subscription = self.create_subscription(
      Bool,
      "sensor_topic",
      self.listener_callback,
      10)
    self.subscription

  def listener_callback(self, msg):
    self.get_logger().info("Subscribed [%d]"%(msg.data))
    
def main(args=None):
  try:
    rclpy.init(args=args)
    sensor_subscripber = SensorSubscriber()
    rclpy.spin(sensor_subscripber)
  except KeyboardInterrupt:
    pass
  finally:
    sensor_subscripber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
  