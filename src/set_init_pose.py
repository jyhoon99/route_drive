#! /usr/bin/env python

# 초기위치 설정 - rviz상 모델 이동
import numpy as np
from tf.transformations import euler_from_quaternion
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Float32MultiArray

# ROS 노드 초기화
rospy.init_node('set_init_pose_node', anonymous=True)

# 발행자 생성
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)

initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map"
initpose_msg.pose.pose.position.x = 0.1803995817899704
initpose_msg.pose.pose.position.y = 0.056696951389312744
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = 0
initpose_msg.pose.pose.orientation.w = 0.9999999999999988
rospy.sleep(1)

rospy.loginfo("Setting initial pose")
pub.publish(initpose_msg)
current_x = initpose_msg.pose.pose.position.x
current_y = initpose_msg.pose.pose.position.y
current_orientation = initpose_msg.pose.pose.orientation
(current_roll, current_pitch, current_yaw) = euler_from_quaternion([current_orientation.x, current_orientation.y, current_orientation.z, current_orientation.w])

# 좌측 또는 우측으로 x cm 이동
x_cm = 50  # x cm
x_m = x_cm / 100.0  + -6.93889390390723E-17 # x m로 변환

# 앞쪽으로 z cm 이동
y_cm = 50  # z cm
y_m = y_cm / 100.0 + 0.0165   # z m로 변환

# 새로운 위치 계산
new_x = current_x + (x_m * np.cos(current_yaw) - y_m * np.sin(current_yaw))
new_y = current_y + (x_m * np.sin(current_yaw) + y_m * np.cos(current_yaw))

print("로봇의 중점에서 좌측으로 {} cm, 앞쪽으로 {} cm 떨어진 위치: x={}, y={}".format(x_cm, y_cm, new_x, new_y))





# def callback(data):
#     global x_values, z_values
#     x_values = data.data[0]
#     z_values = data.data[1]

#     # 데이터를 한 번 받은 후에 노드 종료
#     rospy.signal_shutdown("Received data and shutting down")

# rospy.Subscriber("/yolov5/xz_values", Float32MultiArray, callback)

# navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
# navclient.wait_for_server()

# robot_x = 0.1803995817899704
# robot_y = 0.056696951389312744
# robot_z = 0.0
# distance = z_values * 10
# quaternion = (0.0, 0.0, 0.0, 0.9999999999999988)
# offset_from_center = x_values  # 중점에서 객체까지의 거리

# # 쿼터니언 값을 4x4 변환 행렬로 변환
# rotation_matrix = quaternion_matrix(quaternion)

# # 로봇에서 객체까지의 벡터 계산
# object_vector = np.array([0, 0, distance, 1])  # 객체까지의 벡터 (상대적인 위치)

# # 로봇의 쿼터니언을 사용하여 벡터를 좌표계상으로 변환
# object_position = np.dot(rotation_matrix, object_vector)[:3]

# # 객체의 좌표를 로봇의 현재 위치와 offset_from_center를 고려하여 계산
# object_x_absolute = robot_x + object_position[0]
# object_y_absolute = robot_y + object_position[1]
# object_z_absolute = robot_z + object_position[2]

# # offset_from_center를 고려한 위치 계산
# object_x_absolute += offset_from_center * np.cos(quaternion[3])  # 쿼터니언의 w 값은 회전 각도를 나타냄
# object_y_absolute += offset_from_center * np.sin(quaternion[3])

# # First navigation goal
# goal1 = MoveBaseGoal()
# goal1.target_pose.header.frame_id = "map"
# goal1.target_pose.header.stamp = rospy.Time.now()
# goal1.target_pose.pose.position.x = object_x_absolute
# goal1.target_pose.pose.position.y = object_y_absolute
# goal1.target_pose.pose.position.z = object_z_absolute
# goal1.target_pose.pose.orientation.x = 0.0
# goal1.target_pose.pose.orientation.y = 0.0
# goal1.target_pose.pose.orientation.z = 0
# goal1.target_pose.pose.orientation.w = 0.9999999999999988

# Sending first navigation goal
# navclient.send_goal(goal1)
# navclient.wait_for_result()

rospy.loginfo("Initial pose SET")

rospy.spin()