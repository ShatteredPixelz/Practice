
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + '%s', data.data)

def commandlineprint():

    rospy.init_node('commandlineprint', anonymous=True)
    
    rospy.Subscriber('caelinsfury', String, callback)
#keeps it going while program is running
    rospy.spin()

if __name__ == '__main__':
    commandlineprint()