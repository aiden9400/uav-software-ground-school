import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class TestPublisher(Node):
    def __init__(self, period: int):
        super.__init__('test publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(period, self.timer_callback)
        self.cycles = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Cycles since start: %d' % self.cycles
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.cycles += 1

def main(args = None):
    rclpy.init(args = args)
    test_publisher = TestPublisher(1)
    rclpy.spin(test_publisher)

    test_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()