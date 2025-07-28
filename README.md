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
