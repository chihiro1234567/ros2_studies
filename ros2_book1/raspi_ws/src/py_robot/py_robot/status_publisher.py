import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import pigpio
STATUS_PIN=18 # GPIO18(no.12)

class StatusPublisher(Node):
  def __init__(self):
    super().__init__("status_publisher")
    self.init_status()
    
    self.publisher_ = self.create_publisher(Bool, "status_topic", 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)

  def timer_callback(self):
    input_msg = Bool(data=self.status_input())
    self.publisher_.publish(input_msg)
    self.get_logger().info("Publishing, [%d]"%(input_msg))

  def init_status(self):
    self.pi = pigpio.pi()
    self.pi.set_mode(STATUS_PIN, pigpio.INPUT)
    self.pi.set_pull_up_down(STATUS_PIN, pigpio.PUD_UP)
  
  def status_input(self):
    if self.pi.read(STATUS_PIN) == 1:
      return True
    else:
      return False

def main(args=None):
  try:
    rclpy.init(args=args)
    status_publisher = StatusPublisher()
    rclpy.spin(status_publisher)
  except KeyboardInterrupt:
    pass
  finally:
    status_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
  main()
