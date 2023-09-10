#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# Callback function for the "control_nav" topic
def control_nav_callback(data):
    if data.data == "start":
        # 노드를 다시 시작
        rospy.loginfo("Starting 'set_initial_and_send_goal' node")
        rospy.init_node('set_initial_and_send_goal', anonymous=True)
    elif data.data == "end":
        # 노드를 중단
        rospy.loginfo("Stopping 'set_initial_and_send_goal' node")
        rospy.signal_shutdown("Shutdown by user")

if __name__ == '__main__':
    rospy.init_node('route_moving', anonymous=True)

    # Subscribe to the "control_nav" topic
    rospy.Subscriber('control_nav', String, control_nav_callback)

    rospy.spin()