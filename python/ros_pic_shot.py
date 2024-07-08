import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


i=0
def img_callback(data):
    # print("into callback\n")
    global bridge
    bridge=CvBridge()
    global cv_image
    cv_image=bridge.imgmsg_to_cv2(data,"bgr8")
    cv2.imshow("img",cv_image)
    key=cv2.waitKey(1)
    key_callback(key)

def key_callback(key):
    if key==ord('s'):
	global i
        cv2.imwrite("savedpic_"+str(i)+".png",cv_image)
	i=i+1
        print("saving picture "+str(i)"!\n")
def img_sub():
    # print("into sub\n")
    rospy.init_node("img_sub",anonymous=True)
    bridge=CvBridge()
    rospy.Subscriber('/camera/left/image_raw',Image,img_callback)
    rospy.spin()

if __name__=='__main__':
    try:

        # print("into main\n")
        img_sub()
	
    except rospy.ROSInternalException:
        pass
