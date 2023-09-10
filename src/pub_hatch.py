#!/usr/bin/env python

import rospy
from hatch.msg import Message 

def main():
    rospy.init_node("Publisher_node")
    pub = rospy.Publisher("topic", Message, queue_size=10)
    rate = rospy.Rate(10)
    work = Message()

    while not rospy.is_shutdown():
        # 키보드 입력 받기
        key = input()  # 수정된 부분: raw_input() -> input()

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




# def main():
#     rospy.init_node("Publisher_node")
#     pub = rospy.Publisher("topic", Message, queue_size=10)
#     rate = rospy.Rate(10)
#     work = Message()

#     while not rospy.is_shutdown():
#         work.mode = 1
#         pub.publish(work)
#         rate.sleep()  # sleep() 함수를 호출할 때 인수를 제거합니다.
        
#         work.mode = 2
#         pub.publish(work)
#         rate.sleep()  # sleep() 함수를 호출할 때 인수를 제거합니다.
        
#         work.mode = 3
#         pub.publish(work)
#         rate.sleep()  # sleep() 함수를 호출할 때 인수를 제거합니다.

# if __name__ == '__main__':
#     try:
#         main()
#     except rospy.ROSInterruptException:
#         pass