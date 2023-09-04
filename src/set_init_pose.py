#! /usr/bin/env python

# 초기위치 설정 - rviz상 모델 이동

import rospy
from geometry_msgs.msg import PoseWithCovariance
initpose_msg = PoseWithCovarianceStamped()
initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map"
initpose_msg.pose.pose.position.x = 0.7271415659708295
initpose_msg.pose.pose.position.y = -0.7981304936623433
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = 0.769978405623212
initpose_msg.pose.pose.orientation.w = 0.6380699451266582
initpose_msg.pose.covariance=[0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
rospy.sleep(1)

rospy.loginfo ("Setting initial pose")
pub.publish(initpose_msg)




rospy.loginfo ("Initial pose SET")

rospy.spin()

