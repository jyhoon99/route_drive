#! /usr/bin/env python

### 헤더파일 ###
    import rospy
    import actionlib
    from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
    from geometry_msgs.msg import PoseWithCovarianceStamped
    from std_msgs.msg import Int32
    from hatch.msg import Message


### 노드 초기화 ### 
    rospy.init_node("linear_pub")
    rospy.init_node("Publisher_node")


### 퍼블리시 ###
    linear_pub = rospy.Publisher("linear", Int32, queue_size=10)
    hatch_pub = rospy.Publisher("topic", Message, queue_size=10)
    init_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped)

### 서브스크라이브 ###
    zed_sub = rospy.Subscriber("",)
    APP_sub = rospy.Subscriber("",)


### 콜백함수 ###
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

    def topic_callback(msg):
        global object_detected
        # 토픽 메시지를 받았을 때 수행할 동작 정의
        # 객체의 위치까지 이동 + 자세추정
        if msg.object_type == 'A': #배변
            # work.mode = 1
            # delay(5)
            # msg.data = 1900
            # delay(5)
            # msg.data = 1035
            object_detected = None
        elif msg.object_type == 'B': #반려동물
            # work.mode = 2
            # delay(5)
            # work.mode = 3물
            object_detected = None


### 함수 ###
    def set_initial_pose():
        # ROS 노드 초기화
        rospy.init_node('set_init_pose_node', anonymous=True)

        # 발행자 생성
        init_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)

        initpose_msg = PoseWithCovarianceStamped()
        initpose_msg.header.frame_id = "map"
        initpose_msg.pose.pose.position.x = 0.1803995817899704
        initpose_msg.pose.pose.position.y = 0.056696951389312744
        initpose_msg.pose.pose.orientation.x = 0.0
        initpose_msg.pose.pose.orientation.y = 0.0
        initpose_msg.pose.pose.orientation.z = 0
        initpose_msg.pose.pose.orientation.w = 0.9999999999999988
        rospy.sleep(1)

        init_pub.loginfo("Setting initial pose")
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


### 배열 ###
    goal_positions = [
        {
            'x': 1,
            'y': 0,
            'z': 0.0,
            'qx': 0.0,
            'qy': 0.0,
            'qz': -0.7,
            'qw': 0.7
        },
        {
            'x': 1,
            'y': -1.3,
            'z': 0.0,
            'qx': 0.0,
            'qy': 0.0,
            'qz': -1,
            'qw': 0
        },
        {
            'x': 0.3,
            'y': -1.4,
            'z': 0.0,
            'qx': 0.0,
            'qy': 0.0,
            'qz': 0,
            'qw': 1
        },
        {
            'x': 0.1803995817899704,
            'y': 0.056696951389312744,
            'z': 0.0,
            'qx': 0.0,
            'qy': 0.0,
            'qz': 0,
            'qw': 1
        }
    ]


### 메세지 ###
    msg = Int32()
    msg.data = 1900
    msg.data = 1035
    pub.publish(msg)

    work = Message()
    work.mode = 1
    work.mode = 2
    work.mode = 3
    pub.publish(work)





### 메인 ###
if __name__ == '__main__':
    rospy.init_node('set_initial_and_send_goal', anonymous=True)
    rospy.init_node("combined_pub")

    # Setting initial pose
    set_initial_pose()

    # Initializing navigation client
    navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    navclient.wait_for_server()

    while not rospy.is_shutdown():
        if object_detected is None:
            for position in goal_positions:
                # 객체를 인식하지 않은 경우 목표 위치로 이동
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
        else:
            # 객체를 인식한 경우 해당 동작 수행
            topic_callback(object_detected)
            # 동작 수행 후 상태 초기화
            object_detected = None

    rospy.spin()
