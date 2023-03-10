import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import pigpio
SENSOR_PIN=18 # GPIO18(no.12)

class SensorPublisher(Node):
  def __init__(self):
    super().__init__("sensor_publisher")
    self.init_sensor()
    self.publisher_ = self.create_publisher(Bool, "sensor_topic", 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)

  def timer_callback(self):
    input_msg = Bool(data=self.sensor_input())
    self.publisher_.publish(input_msg)
    self.get_logger().info("Publishing, [%s]"%(input_msg))

  def init_sensor(self):
    self.pi = pigpio.pi()
    self.pi.set_mode(SENSOR_PIN, pigpio.INPUT)
    self.pi.set_pull_up_down(SENSOR_PIN, pigpio.PUD_UP)
  
  def sensor_input(self):
    if self.pi.read(SENSOR_PIN) == 1:
      return True
    else:
      return False

def main(args=None):
  try:
    rclpy.init(args=args)
    sensor_publisher = SensorPublisher()
    rclpy.spin(sensor_publisher)
  except KeyboardInterrupt:
    pass
  finally:
    sensor_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
