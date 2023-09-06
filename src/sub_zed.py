#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
import struct

def callback(data):
    rospy.loginfo("Received PointCloud2 message:")
    rospy.loginfo("Header:")
    rospy.loginfo("  Seq: %d", data.header.seq)
    rospy.loginfo("  Stamp: %d.%d", data.header.stamp.secs, data.header.stamp.nsecs)
    rospy.loginfo("  Frame ID: %s", data.header.frame_id)
    rospy.loginfo("Height: %d", data.height)
    rospy.loginfo("Width: %d", data.width)
    rospy.loginfo("Fields:")
    for field in data.fields:
        rospy.loginfo("  Name: %s", field.name)
        rospy.loginfo("  Offset: %d", field.offset)
        rospy.loginfo("  Datatype: %d", field.datatype)
        rospy.loginfo("  Count: %d", field.count)
    rospy.loginfo("Is Bigendian: %s", data.is_bigendian)
    rospy.loginfo("Point Step: %d", data.point_step)
    rospy.loginfo("Row Step: %d", data.row_step)
    rospy.loginfo("Data:")
    ##############################################################################
    data_list = struct.unpack('<{}f'.format(len(data.data) // 4), data.data)
    for i in range(0, len(data_list), 3):
        x = data_list[i]
        y = data_list[i + 1]
        z = data_list[i + 2]
        rospy.loginfo("  x: %.2f, y: %.2f, z: %.2f", x, y, z)
        ##############################################################################
    rospy.loginfo("Is Dense: %s", data.is_dense)

def listener():
    rospy.init_node('point_cloud_listener', anonymous=True)
    rospy.Subscriber("your_point_cloud_topic_name_here", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()