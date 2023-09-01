#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

initpose_msg = PoseWithCovarianceStamped()

def amcl_pose_callback(msg):
    # amcl_pose 토픽에서 수신한 메시지를 initialpose 토픽으로 퍼블리시
    global initpose_msg

    # amcl_pose 메시지로부터 위치와 방향 정보 추출
    position_x = msg.pose.pose.position.x
    position_y = msg.pose.pose.position.y
    orientation_x = msg.pose.pose.orientation.x
    orientation_y = msg.pose.pose.orientation.y
    orientation_z = msg.pose.pose.orientation.z
    orientation_w = msg.pose.pose.orientation.w

    # initpose_msg에 값 할당
    initpose_msg.header.frame_id = "map"
    initpose_msg.pose.pose.position.x = position_x
    initpose_msg.pose.pose.position.y = position_y
    initpose_msg.pose.pose.orientation.x = orientation_x
    initpose_msg.pose.pose.orientation.y = orientation_y
    initpose_msg.pose.pose.orientation.z = orientation_z
    initpose_msg.pose.pose.orientation.w = orientation_w
    initialpose_pub.publish(msg)

rospy.init_node("amcl_pose_to_initialpose")

# initialpose 토픽에 메시지를 퍼블리시하기 위한 퍼블리셔 생성
initialpose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)


# amcl_pose 토픽에서 메시지를 구독하고, 수신할 때마다 amcl_pose_callback 함수 호출
rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, amcl_pose_callback)

rospy.spin()