#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Vector3

class IMUConverter:
    def __init__(self):
        rospy.init_node('imu_converter', anonymous=True)
        rospy.Subscriber("/imu", Imu, self.callback)
        self.pub = rospy.Publisher('/euler', Vector3, queue_size=10)

    def callback(self, data):
        quaternion = (
            data.orientation.x,
            data.orientation.y,
            data.orientation.z,
            data.orientation.w
        )
        euler = euler_from_quaternion(quaternion)
        euler_msg = Vector3()
        euler_msg.x = euler[0]
        euler_msg.y = euler[1]
        euler_msg.z = euler[2]
        self.pub.publish(euler_msg)

    def start(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        converter = IMUConverter()
        converter.start()
    except rospy.ROSInterruptException:
        pass
