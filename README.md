## การทำงาน คร่าวๆ
package หลักๆ มี 3 ตัว
1. my_robot
   เอาไว้รวมแต่ละ node
   จะมี
   1. nav_to_goal.py เป็น navigation
   2. object_fake_node.py เป็น object detection
   3. servo.py เป็น servo
      
  สมมุติเรา from ... import อะไรมาเพิ่มใน 3 ไฟล์นี้
จะต้องไปเพิ่มที่เรา from ... มาใน package.xml ด้วย 
      
2. my_robot_bringup
    เป็น package ที่มี launch file ไว้รันการทำงานของทุก node ใน my_robot พร้อมกัน

3. my_robot_app
    เป็น package ที่มี master launch file
เอาไว้ run launch file ใน my_robot_bringup และ ใน turtlebot3_navigation2 เพื่อให้แมพขึ้น
ใน launch file ของ package my_robot_app
จะต้องไปตั้งค่า path ของ map เพิ่มเติมเพื่อให้สามารถเปิดแมพได้


## หลักการทำงาน

เมื่อถึงเป้าหมาย nav_to_goal จะส่ง Empty message ผ่าน topic waypoint_reaced
เพื่อบอกให้ object_detection_fake_node.py
ตรวจจับคน และส่งเป็น message true or false
ว่าเจอไหมผ่าน topic person_detected ไปให้ servo.py แล้วพอ servo ทำงานเสร็จจะส่ง empty message ไปให้ nav_to_goal  เพื่อบอกให้ไปจุดต่อไป

กรณี detect ไม่เจอ object_detection_fake_node จะส่ง Empty message ให้ nav_to_goal ให้ไปจุดต่อไปเลย
