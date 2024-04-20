import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, 'camerafeed', 10)
        self.timer_ = self.create_timer(0.1, self.publish_camera_feed)
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(1)

    def publish_camera_feed(self):
        ret, frame = self.capture.read()
        if ret:
            image_message = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(image_message)

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()
    rclpy.spin(camera_publisher)


    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
