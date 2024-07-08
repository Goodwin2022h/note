import serial
import pynmea2
import rospy
from sensor_msgs.msg import NavSatFix

def parse_nmea_data(nmea_sentence):
    try:
        msg = pynmea2.parse(nmea_sentence)
        if isinstance(msg, pynmea2.types.talker.GGA):
            navsatfix_msg = NavSatFix()
            navsatfix_msg.latitude = msg.latitude
            navsatfix_msg.longitude = msg.longitude
            navsatfix_msg.altitude = msg.altitude
            navsatfix_msg.header.stamp = rospy.Time.now()
            navsatfix_msg.status.service = NavSatFix.SERVICE_GPS
            navsatfix_msg.status.status = NavSatFix.STATUS_FIX

            # 添加更多字段
            navsatfix_msg.status.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
            navsatfix_msg.status.position_covariance[0] = msg.horizontal_dil
            navsatfix_msg.status.position_covariance[4] = msg.horizontal_dil
            navsatfix_msg.status.position_covariance[8] = msg.vertical_dil

            navsatfix_msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
            navsatfix_msg.position_covariance[0] = msg.horizontal_dil
            navsatfix_msg.position_covariance[4] = msg.horizontal_dil
            navsatfix_msg.position_covariance[8] = msg.vertical_dil

            return navsatfix_msg
    except pynmea2.ParseError as e:
        print(f"Error parsing NMEA data: {e}")
    return None

def main():
    # 初始化ROS节点
    rospy.init_node('gps_reader', anonymous=True)

    # 配置串口
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    # 创建NavSatFix发布者
    pub = rospy.Publisher('/gps/fix', NavSatFix, queue_size=10)

    while not rospy.is_shutdown():
        try:
            # 从串口读取一行NMEA数据
            nmea_data = ser.readline().decode('utf-8').strip()

            # 解析NMEA数据并发布NavSatFix消息
            navsatfix_msg = parse_nmea_data(nmea_data)
            if navsatfix_msg:
                pub.publish(navsatfix_msg)

        except serial.SerialException as e:
            print(f"Serial port error: {e}")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass