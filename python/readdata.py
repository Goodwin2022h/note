#
# @ 文件名：readdata.py
#
# @ 文件功能描述：将原极DAT数据转换为TXT惯性数据，使用方法，将其放入包含DAT文件的目录，
# @ 会自动搜索目录下的dat文件并转换为TXT， python3 readdata.py --dir 指定的目录
#
# @ 创建日期：2022年8月3日
#
# @ 创建人：南京航空航天大学导航研究中心 袁诚
#
# @ 修改标识：2022年9月1日 V1.1
#
# @ 修改描述：增加时间戳判断，由于存在时间戳判断和帧头重复的问题，所以加入了连续时间戳判断
#           此外，增加了参数，可以指定目录
#
# @ 修改日期：


import os
# import pandas as pd
import math
import struct


def get_full_filelist(base_dir='.', target_ext='') -> list:
    fname_list = []
    # 用于记录文件名的列表

    for fname in os.listdir(base_dir):
        # 逐个检查指定目录
        path = os.path.join(base_dir, fname)
        # 把文件名和所在目录名连接起来
        if os.path.isfile(path):
            # 判断是否是“文件”类型
            fname_main, fname_ext = os.path.splitext(fname)
            # 把文件名和后缀切分开
            if fname_ext == target_ext or target_ext == '':
                # 判断是否指定的后缀名
                fname_list.append(path)
                # 将符合条件的文件全路径名加入列表
        elif os.path.isdir(path):
            # 判断是否是“目录”类型
            temp_list = get_full_filelist(path, target_ext)
            # 递归调用查找子目录
            fname_list = fname_list + temp_list
            # 将递归调用返回的文件名列表合并
        else:
            pass

    return fname_list  # 返回查到的文件名列表


def conver_dat_to_txt(input_name=''):
    file = open(input_name, 'rb')  # 读取文件
    hex_list = ("{:02X}".format(int(c)) for c in file.read())
    file.close()

    file_name_str = input_name + '_to_txt.txt'
    output_file = open(file_name_str, 'w+')

    print(f"Now is open {input_name} and convert to {file_name_str}")
    tsF = "{:.07f}"  # 保留7位小数

    buflist = list(hex_list)  # 用列表保存信息，方便后续操作
    # index_num = '{:d}'.format(int(('0x'+''.join(buflist[12:16])),16))  # 此处提取想要的文本信息\

    index = 0
    data_imu, data_imu_old = [], []
    for i in range(0, len(buflist) - 1):
        # for i in range(0, 400, 2):

        if buflist[i] == 'AA' and buflist[i + 1] == '55' and i + 66 < len(buflist):
            str_imu_id = buflist[i + 5] + buflist[i + 4]  # ID值
            # data_imu.append(str_imu_id)

            imu_length = int(buflist[i + 5], 16) * 16 * 16 + int(buflist[i + 4], 16)
            # data_imu.append(imu_length)

            imu_time = int(buflist[i + 9], 16) * math.pow(16, 6) + int(buflist[i + 8], 16) * math.pow(16, 4) + int(
                buflist[i + 7], 16) * math.pow(16, 2) + int(buflist[i + 6], 16)
            data_imu.append(imu_time)

            # imu_error_code = int(buflist[i+13],16) * math.pow(16,6) + int(buflist[i+12],16) * math.pow(16,4) + int(buflist[i+11],16) * math.pow(16,2) + int(buflist[i+10],16)
            # data_imu.append(imu_error_code)
            # print(f"errorcode is {imu_error_code}")

            str_imu_device_number = buflist[i + 13] + buflist[i + 12] + buflist[i + 11] + buflist[i + 10]
            imu_device_number = struct.unpack('!f', bytes.fromhex(str_imu_device_number))[0]
            data_imu.append(imu_device_number)

            str_imu_pitch = buflist[i + 17] + buflist[i + 16] + buflist[i + 15] + buflist[i + 14]
            imu_pitch = struct.unpack('!f', bytes.fromhex(str_imu_pitch))[0]
            data_imu.append(imu_pitch)

            str_imu_roll = buflist[i + 21] + buflist[i + 20] + buflist[i + 19] + buflist[i + 18]
            imu_roll = struct.unpack('!f', bytes.fromhex(str_imu_roll))[0]
            data_imu.append(imu_roll)

            str_imu_accx = buflist[i + 25] + buflist[i + 24] + buflist[i + 23] + buflist[i + 22]
            imu_accx = struct.unpack('!f', bytes.fromhex(str_imu_accx))[0]
            data_imu.append(imu_accx)

            str_imu_accy = buflist[i + 29] + buflist[i + 28] + buflist[i + 27] + buflist[i + 26]
            imu_accy = struct.unpack('!f', bytes.fromhex(str_imu_accy))[0]

            str_imu_accz = buflist[i + 33] + buflist[i + 32] + buflist[i + 31] + buflist[i + 30]
            imu_accz = struct.unpack('!f', bytes.fromhex(str_imu_accz))[0]

            str_imu_gyrox = buflist[i + 37] + buflist[i + 36] + buflist[i + 35] + buflist[i + 34]
            imu_gyrox = struct.unpack('!f', bytes.fromhex(str_imu_gyrox))[0]

            str_imu_gyroy = buflist[i + 41] + buflist[i + 40] + buflist[i + 39] + buflist[i + 38]
            imu_gyroy = struct.unpack('!f', bytes.fromhex(str_imu_gyroy))[0]

            str_imu_gyroz = buflist[i + 45] + buflist[i + 44] + buflist[i + 43] + buflist[i + 42]
            imu_gyroz = struct.unpack('!f', bytes.fromhex(str_imu_gyroz))[0]

            str_imu_temp = buflist[i + 49] + buflist[i + 48] + buflist[i + 47] + buflist[i + 46]
            imu_temp = struct.unpack('!f', bytes.fromhex(str_imu_temp))[0]

            str_imu_mx = buflist[i + 53] + buflist[i + 52] + buflist[i + 51] + buflist[i + 50]
            imu_mx = struct.unpack('!f', bytes.fromhex(str_imu_mx))[0]

            str_imu_my = buflist[i + 57] + buflist[i + 56] + buflist[i + 55] + buflist[i + 54]
            imu_my = struct.unpack('!f', bytes.fromhex(str_imu_my))[0]

            str_imu_mz = buflist[i + 61] + buflist[i + 60] + buflist[i + 59] + buflist[i + 58]
            imu_mz = struct.unpack('!f', bytes.fromhex(str_imu_mz))[0]

            # print('\n we got a frame in', i, i - index)
            # print(f"id is {str_imu_id}")
            # print(f"length is {imu_length}")
            # print(f"time is {imu_time}")
            # print(f"bmp280_data is {bmp280_data}")
            # print(f"imu_accx is {imu_accx}")
            # print(f"imu_accy is {imu_accy}")
            # print(f"imu_accz is {imu_accz}")
            # print(f"imu_gyrox is {imu_gyrox}")
            # print(f"imu_gyroy is {imu_gyroy}")
            # print(f"imu_gyroz is {imu_gyroz}")
            # print(f"imu_temp is {imu_temp}")
            # print(f"imu_roll is {imu_roll}")
            # print(f"imu_roll is {imu_mx}")
            # print(f"imu_roll is {imu_my}")
            # print(f"imu_roll is {imu_mz}")
            if data_imu_old is None:
                output_file.write(
                    f"{imu_time} {tsF.format(imu_accx)} {tsF.format(imu_accy)} {tsF.format(imu_accz)} {tsF.format(imu_gyrox)} {tsF.format(imu_gyroy)} {tsF.format(imu_gyroz)} {tsF.format(imu_temp)} {tsF.format(imu_pitch)} {tsF.format(imu_device_number)} {tsF.format(imu_roll)} {tsF.format(imu_mx)} {tsF.format(imu_my)} {tsF.format(imu_mz)}\n")

            elif len(data_imu_old) >0 and abs(data_imu_old[0]-data_imu[0])<1e5:
                output_file.write(
                    f"{imu_time} {tsF.format(imu_accx)} {tsF.format(imu_accy)} {tsF.format(imu_accz)} {tsF.format(imu_gyrox)} {tsF.format(imu_gyroy)} {tsF.format(imu_gyroz)} {tsF.format(imu_temp)} {tsF.format(imu_pitch)} {tsF.format(imu_device_number)} {tsF.format(imu_roll)} {tsF.format(imu_mx)} {tsF.format(imu_my)} {tsF.format(imu_mz)}\n")

            index = i
            data_imu_old = data_imu
            data_imu = []

    output_file.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.')
    args = parser.parse_args()
    file_list = get_full_filelist(base_dir=args.dir, target_ext='.dat')
    print(file_list)
    for filename in file_list:
        conver_dat_to_txt(filename)
    # filename ='./data/zqq1959_3.dat'
    # conver_dat_to_txt(filename)
