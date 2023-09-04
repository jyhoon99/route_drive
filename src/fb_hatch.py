#!/usr/bin/env python

# 키보드로 해치제어 

import rospy
from std_msgs.msg import String
from hatch.msg import Message

def main():
    rospy.init_node("Publisher_node")
    pub = rospy.Publisher("topic", Message, queue_size=10)
    rate = rospy.Rate(10)
    work = Message()

    while not rospy.is_shutdown():
        # 키보드 입력 받기
        key = input()

        if key == 'f':
            work.mode = 1
        elif key == 'g':
            work.mode = 2
        elif key == 'h':
            work.mode = 3

        pub.publish(work)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass