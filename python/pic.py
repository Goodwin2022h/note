import rosbag
from cv_bridge import CvBridge
import cv2
import os
bridge=CvBridge()
rtk_time=1699412317.974905922
bag=rosbag.Bag('/home/nrc/pukou/pukou_50_2_2023-11-08-10-57-48.bag')
for topic, msg,t in bag.read_messages(topics=['/camera/left/image_raw']):
	if t.to_sec()>=rtk_time-0.01 and t.to_sec()<=rtk_time+0.01:
		cv_image=bridge.imgmsg_to_cv2(msg,"bgr8")
		cv2.imwrite('0.png',cv_image)
bag.close()
