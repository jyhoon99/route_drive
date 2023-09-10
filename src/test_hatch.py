import rospy
from std_msgs.msg import Int32
from hatch.msg import Message

def main():
    rospy.init_node("combined_pub")
    
    # Publishers
    linear_pub = rospy.Publisher("linear", Int32, queue_size=10)
    hatch_pub = rospy.Publisher("topic", Message, queue_size=10)
    
    rospy.loginfo("Publishing to topics linear and topic...")
    
    rate = rospy.Rate(10)  # 10 Hz
    
    msg = Int32()
    work = Message()

    while not rospy.is_shutdown():
        ch = input("Enter 'o', 'p' for linear, 'f', 'g', or 'h' for hatch: ")

        if ch.lower() in ['o', 'p']:
            if ch.lower() == 'o':
              msg.data = 1900  
            elif ch.lower() == 'p':
              msg.data = 1035  

            rospy.loginfo("Published linear message: %d", msg.data)
            linear_pub.publish(msg)
        elif ch.lower() in ['f', 'g', 'h']:
            if ch.lower() == 'f':
                work.mode = 1
            elif ch.lower() == 'g':
                work.mode = 2
            elif ch.lower() == 'h':
                work.mode = 3

            rospy.loginfo("Published topic message: %d", work.mode)
            hatch_pub.publish(work)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
