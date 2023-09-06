#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped

# Define the goal positions as an array
goal_positions = [
    {
        'x': 0.0050532572726404434,
        'y': -0.0065163473167238264,
        'z': 0.0,
        'qx': 0.0,
        'qy': 0.0,
        'qz': 0.9999854971906513,
        'qw': 0.005385666937886398
    },
    {
        'x': -1.4849314812542065,
        'y': -1.0723410808727862,
        'z': 0.0,
        'qx': 0.0,
        'qy': 0.0,
        'qz': 0.7002975537695603,
        'qw': 0.7138510602250092
    },
    {
        'x': -1.299856838616526,
        'y': -0.01445918508071406,
        'z': 0.0,
        'qx': 0.0,
        'qy': 0.0,
        'qz': 0.7248938375136363,
        'qw': 0.6888605986226486
    },
    {
        'x': 0.01924784077285243,
        'y': 0.08436867452749593,
        'z': 0.0,
        'qx': 0.0,
        'qy': 0.0,
        'qz': -0.7021836726803337,
        'qw': 0.7119958495814129
    }
]

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

# Function to send navigation goal
def send_navigation_goal(client, x, y, z, qx, qy, qz, qw):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    client.send_goal(goal, done_cb=done_cb, active_cb=active_cb, feedback_cb=feedback_cb)
    client.wait_for_result()

# Function to set initial pose
def set_initial_pose():
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped)
    initpose_msg = PoseWithCovarianceStamped()
    initpose_msg.header.frame_id = "map"
    initpose_msg.pose.pose.position.x = -0.08292758642867278
    initpose_msg.pose.pose.position.y = -0.08516219482204036
    initpose_msg.pose.pose.orientation.x = 0.0
    initpose_msg.pose.pose.orientation.y = 0.0
    initpose_msg.pose.pose.orientation.z = -0.7021836726803337
    initpose_msg.pose.pose.orientation.w = 0.7119958495814129
    rospy.sleep(1)
    rospy.loginfo("Setting initial pose")
    pub.publish(initpose_msg)
    rospy.loginfo("Initial pose SET")

if __name__ == '__main__':
    rospy.init_node('set_initial_and_send_goal', anonymous=True)

    # Setting initial pose
    set_initial_pose()

    # Initializing navigation client
    navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    navclient.wait_for_server()

    # Infinite loop to send navigation goals
    while not rospy.is_shutdown():
        for position in goal_positions:
            send_navigation_goal(
                navclient,
                position['x'],
                position['y'],
                position['z'],
                position['qx'],
                position['qy'],
                position['qz'],
                position['qw']
            )

    rospy.spin()