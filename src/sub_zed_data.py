#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
import struct

def callback(data):
    rospy.loginfo("Received PointCloud2 message:")
    rospy.loginfo("Data:")

    # Extract x, y, z coordinates from the data array
    data_array = struct.unpack('<{}B'.format(len(data.data)), data.data)
    x_bytes = data_array[0:4]
    y_bytes = data_array[4:8]
    z_bytes = data_array[8:12]

    x = struct.unpack('<f', bytes(x_bytes))[0]
    y = struct.unpack('<f', bytes(y_bytes))[0]
    z = struct.unpack('<f', bytes(z_bytes))[0]

    rospy.loginfo("  x: %.2f, y: %.2f, z: %.2f", x, y, z)

def listener():
    rospy.init_node('point_cloud_listener', anonymous=True)
    rospy.Subscriber("your_point_cloud_topic_name_here", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()