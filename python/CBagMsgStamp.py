import rosbag 
import rospy
from rospy import Time

in_bag = '/home/nrc/130/bevlidar2_2024-01-30-15-29-21.bag'
out_bag = '/home/nrc/130/output2.bag'
input_bag = rosbag.Bag(in_bag, "r")
output_bag = rosbag.Bag(out_bag, "w")
# with rosbag.Bag(out_bag, "w"):
#     with rosbag.Bag(in_bag, "r"):
first_flag_odo = True
first_flag_f = True
first_flag_b = True
first_flag_l = True
first_flag_r = True
first_flag_c = True   
t_first_b = Time.from_sec(1)
t_first_c = Time.from_sec(1)
t_first_f = Time.from_sec(1)
t_first_l = Time.from_sec(1)
t_first_r = Time.from_sec(1)
t_first_odo  = Time.from_sec(1)
for topic, msg, t in input_bag.read_messages():
    # print(topic,t)
    if first_flag_odo and topic =='/Odometry':
        t_first_odo = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        first_flag_odo = False
        # print(topic,t1)
        output_bag.write(topic, msg, t)
    elif topic =='/Odometry':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_odo)
        # print(topic,t1)
        output_bag.write(topic, msg, t)

    if first_flag_l and topic =='/camera/left/image_raw':
        t_first_l = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        # print(t,t_first_l)
        first_flag_l = False
        output_bag.write(topic, msg, t)        
    elif topic =='/camera/left/image_raw':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_l)
        output_bag.write(topic, msg, t)
        # print("temp:",t_temp_l)

    if first_flag_r and topic =='/camera/right/image_raw':
        t_first_r = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        first_flag_r = False
        output_bag.write(topic, msg, t)
    elif topic =='/camera/right/image_raw':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_r)
        output_bag.write(topic, msg, t)

    if first_flag_b and topic =='/camera/back/image_raw':
        t_first_b = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        first_flag_b = False
        output_bag.write(topic, msg, t)
    elif topic =='/camera/back/image_raw':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_b)
        output_bag.write(topic, msg, t)
        # print("temp:",t_temp_b)

    if first_flag_f and topic =='/camera/front/image_raw':
        t_first_f = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        first_flag_f = False
        output_bag.write(topic, msg, t)
    elif topic =='/camera/front/image_raw':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_f)
        output_bag.write(topic, msg, t)

    if first_flag_c and topic =='/cloud_registered':
        t_first_c = msg.header.stamp.to_sec()
        msg.header.stamp = Time.from_sec(1)
        first_flag_c = False
        output_bag.write(topic, msg, t)
    elif topic =='/cloud_registered':
        msg.header.stamp = Time.from_sec(msg.header.stamp.to_sec() - t_first_c)    
        output_bag.write(topic, msg, t)           
output_bag.close()
            

