#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped

# Callbacks definition
def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    elif status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    elif status == 4:
        rospy.loginfo("Goal aborted")

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    pass  # You can process feedback here if needed

rospy.init_node('set_initial_and_send_goal', anonymous=True)

# Setting initial pose
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped)
initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map"
initpose_msg.pose.pose.position.x = 0.6820064710401897
initpose_msg.pose.pose.position.y = -0.8350903784964886
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = 0.7535606279892368
initpose_msg.pose.pose.orientation.w = 0.6573784145714453
rospy.sleep(1)
rospy.loginfo("Setting initial pose")
pub.publish(initpose_msg)
rospy.loginfo("Initial pose SET")

# Initializing navigation client
navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
navclient.wait_for_server()

# First navigation goal
goal1 = MoveBaseGoal()
goal1.target_pose.header.frame_id = "map"
goal1.target_pose.header.stamp = rospy.Time.now()
goal1.target_pose.pose.position.x = 0.2451502756175426
goal1.target_pose.pose.position.y = 0.3624416731753185
goal1.target_pose.pose.position.z = 0.0
goal1.target_pose.pose.orientation.x = 0.0
goal1.target_pose.pose.orientation.y = 0.0
goal1.target_pose.pose.orientation.z = 0.12981034089505658
goal1.target_pose.pose.orientation.w = 0.991538842101866

# Sending first navigation goal
navclient.send_goal(goal1, done_cb=done_cb, active_cb=active_cb, feedback_cb=feedback_cb)
navclient.wait_for_result()

# Second navigation goal
goal2 = MoveBaseGoal()
goal2.target_pose.header.frame_id = "map"
goal2.target_pose.header.stamp = rospy.Time.now()
goal2.target_pose.pose.position.x = 1.797328513758231
goal2.target_pose.pose.position.y = 0.8350818575783361
goal2.target_pose.pose.position.z = 0.0
goal2.target_pose.pose.orientation.x = 0.0
goal2.target_pose.pose.orientation.y = 0.0
goal2.target_pose.pose.orientation.z = -0.6539524516548954
goal2.target_pose.pose.orientation.w = 0.7565356508285328

# Sending second navigation goal
navclient.send_goal(goal2, done_cb=done_cb, active_cb=active_cb, feedback_cb=feedback_cb)
navclient.wait_for_result()

# Third navigation goal
goal3 = MoveBaseGoal()
goal3.target_pose.header.frame_id = "map"
goal3.target_pose.header.stamp = rospy.Time.now()
goal3.target_pose.pose.position.x = 1.8875419083290896
goal3.target_pose.pose.position.y = -0.17368427559503785
goal3.target_pose.pose.position.z = 0.0
goal3.target_pose.pose.orientation.x = 0.0
goal3.target_pose.pose.orientation.y = 0.0
goal3.target_pose.pose.orientation.z = -0.6775392315479872
goal3.target_pose.pose.orientation.w = 0.7354866346259209

# Sending third navigation goal
navclient.send_goal(goal3, done_cb=done_cb, active_cb=active_cb, feedback_cb=feedback_cb)
navclient.wait_for_result()

rospy.spin()