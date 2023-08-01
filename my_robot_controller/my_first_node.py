#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 1
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        if self.counter_ == 1:
            self.get_logger().info("Hello for " + str(self.counter_) + " time")
        else:
            self.get_logger().info("Hello for " + str(self.counter_) + " times")
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()