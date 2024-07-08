#encoding=UTF-8
import rosbag
import pandas as pd
import numpy as np

def extract_odometry_data(bag_file_path, topic_name):
    data = []
    with rosbag.Bag(bag_file_path) as bag:
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
            if topic == topic_name:
                # 将线性速度和角速度的数据添加到列表中
                data.append([
                    msg.twist.linear.x,
                    msg.twist.linear.y,
                    msg.twist.linear.z,
                    msg.twist.angular.x,
                    msg.twist.angular.y,
                    msg.twist.angular.z
                ])

    return np.array(data)

def save_to_excel(data, file_name):
    # 将数据转换为DataFrame，并指定列名
    df = pd.DataFrame(data, columns=['linear_x', 'linear_y', 'linear_z', 'angular_x', 'angular_y', 'angular_z'])
    # 将DataFrame保存到Excel文件
    df.to_excel(file_name, index=False)


if __name__ == '__main__':
    bag_file_path = '/home/nrc/20240507data/lichengji_cheku.bag'  # 替换为你的rosbag文件路径
    topic_name = '/odom1'  # 替换为你的TwistStamped话题名称
    output_file_name = 'odometry_data.xlsx'  # 输出的Excel文件名

    data = extract_odometry_data(bag_file_path, topic_name)
    save_to_excel(data, output_file_name)
