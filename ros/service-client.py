import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class TestClientAsync(Node):
    def __init__(self):
        super().__init__('test_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec = 1.0):
            self.get_logger().info('service not available; waiting again')
        self.req = AddTwoInts.request

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)

def main(args = None):
    rclpy.init()

    test_client = TestClientAsync()
    future = test_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(test_client, future)
    response = future.result()
    test_client.get_logger().info('Result of add_two_ints: for %d + %d = %d' % (int(sys.argv[1]), int(sys.argv[2]), response.sum))
    
    test_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()