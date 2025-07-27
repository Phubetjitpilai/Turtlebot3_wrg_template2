#!/usr/bin/env python3
from std_msgs.msg import Bool
from std_msgs.msg import Empty
from rclpy.node import Node 
import rclpy

class DetectionNode(Node):
    # เรียก rclpy.init() ก่อนที่จะสร้าง node
    def __init__(self):
        super().__init__('detection_node')
        # รอรับสัญญาณจาก Node nav ว่าไปถึง waypoint แล้ว
        self.waypoint_sub = self.create_subscription(Empty, '/waypoint_reached', self.on_waypoint_reached, 10)
        # รอรับสัญญาณจาก Node nav ว่าจบการทำงาน แล้ว
        self.task_done_sub = self.create_subscription(Empty, '/task_completed', self.on_task_completed, 10)
        # ส่งสัญญาณ ไป node อื่น เพื่อดำเนินการต่อไป
        self.camera_to_servo_pub = self.create_publisher(Bool, '/person_detected', 10)
        self.camera_to_nav_pub = self.create_publisher(Empty, '/person_no_detected', 10)
        self.person_detected = False

    def on_waypoint_reached(self, msg):
        # เมื่อได้รับข้อความจาก Node 1 (waypoint_reached) จะเริ่มการทำงาน
        self.get_logger().info("Waypoint reached, starting person detection...")
        self.person_detected = self.detect_person()  # # ฟังก์ชันตรวจจับบุคคล
        detection_msg = Bool()
        detection_msg.data = self.person_detected
        if not self.person_detected:
            self.get_logger().info("No person detected.")
            self.camera_to_nav_pub.publish(Empty())
        else:
            self.get_logger().info("person detected.")
            self.camera_to_servo_pub.publish(detection_msg)

    #หยุด spin
    def on_task_completed(self, msg):
        self.get_logger().info("shutdown node Detection...")
        self.destroy_node()  
        rclpy.shutdown()


    def detect_person(self): #เขียน code ตรงนี้
        # Fake detection: ทุกครั้งที่เรียกฟังก์ชันนี้จะ return ว่ามีคน
        return False  # แสดงว่ามีคนเจอทุกรอบ


def main(args=None):
    rclpy.init(args=args)
    node = DetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
