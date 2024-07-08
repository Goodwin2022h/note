
import rosbag
from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry

def twist_stamped_to_odometry(twist_stamped_msg):
    odometry_msg = Odometry()
    odometry_msg.header = twist_stamped_msg.header
    odometry_msg.child_frame_id = "base_link"  # 根据实际情况调整
    # 由于TwistStamped不包含位置信息，这里的位置信息设置为0
    odometry_msg.pose.pose.position.x = 0.0
    odometry_msg.pose.pose.position.y = 0.0
    odometry_msg.pose.pose.position.z = 0.0
    # 假设协方差矩阵为单位矩阵，实际应用中应根据情况调整
    odometry_msg.pose.covariance = [0.0] * 36
    odometry_msg.pose.covariance[0] = 1.0
    odometry_msg.pose.covariance[7] = 1.0
    odometry_msg.pose.covariance[35] = 1.0
    odometry_msg.twist.twist = twist_stamped_msg.twist
    return odometry_msg

def convert_bag(input_bag_path, output_bag_path, twist_stamped_topic, odometry_topic):
    with rosbag.Bag(output_bag_path, 'w') as outbag:
        # 读取输入的ROS bag文件
        with rosbag.Bag(input_bag_path) as inbag:
            for topic, msg, t in inbag.read_messages():
                if topic == twist_stamped_topic:
                    # 将TwistStamped消息转换为Odometry消息
                    odometry_msg = twist_stamped_to_odometry(msg)
                    # 将Odometry消息写入新的ROS bag文件
                    outbag.write(odometry_topic, odometry_msg, t)
                else:
                    # 其他话题的消息保持不变，直接写入新的ROS bag文件
                    outbag.write(topic, msg, t)

if __name__ == '__main__':
    input_bag_path = '/home/nrc/20240507data/lichengji_cheku.bag'  # 替换为你的输入ROS bag文件路径
    output_bag_path = '/home/nrc/20240507data/lichengji_cheku_odo.bag'  # 输出的ROS bag文件路径
    twist_stamped_topic = '/odom1'  # 替换为你的TwistStamped话题名称
    odometry_topic = '/odom2'  # 新的Odometry话题名称

    convert_bag(input_bag_path, output_bag_path, twist_stamped_topic, odometry_topic)
