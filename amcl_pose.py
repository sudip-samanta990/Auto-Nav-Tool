#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped



def callback(data):
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    with open('pose.txt','w') as f:
        f.write("%f, %f" %(x,y))
    
    
    
def pose():
    rospy.init_node('listen_pose', anonymous=True)
    rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callback)
    rospy.spin()
    
	
if __name__ == '__main__':
    pose()
