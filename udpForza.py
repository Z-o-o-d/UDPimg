import socket


import numpy as np
import cv2

import time
# 创建一个1920x1080的空白图像
image = np.zeros((1080, 1920, 3), dtype=np.uint8)



# 设置图像的颜色为红色
image[:, :, 0] = 0  # Blue通道
image[:, :, 1] = 0    # Green通道
image[:, :, 2] = 0    # Red通道




# 使用OpenCV显示图像
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# # image[:, :, 0] = 255  # Blue通道
# # image[:, :, 1] = 255    # Green通道
# # image[:, :, 2] = 0    # Red通道
# # cv2.imshow("Image", image)
# cv2.waitKey(0)

# cv2.destroyAllWindows()



ForzaUDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
LocalAddr=("127.0.0.1",7788)
ForzaUDPSocket.bind(LocalAddr)

BufferOffset = 0

def GetP(Menu=[], Data=[], BitSize = 4):
    "GetP(mainstring, DataName, BufferOffset)"
    # 获得字符串长度并设置字符串变化的位置
    if len(Menu) == 324:  # FH4
        BufferOffset = 12
    else:
        BufferOffset = 0

    number_table = {
        'IsRaceOn': 0,
        'TimestampMs':4,
        'EngineMaxRpm': 8,
        'EngineIdleRpm': 12,
        'CurrentEngineRpm': 16,
        'AccelerationX': 20,
        'AccelerationY': 24,
        'AccelerationZ': 28,
        'VelocityX': 32,
        'VelocityY': 36,
        'VelocityZ': 40,
        'AngularVelocityX': 44,
        'AngularVelocityY': 48,
        'AngularVelocityZ': 52,
        'Yaw': 56,
        'Pitch': 60,
        'Roll': 64,
        'NormSuspensionTravelFl': 68,
        'NormSuspensionTravelFr': 72,
        'NormSuspensionTravelRl': 76,
        'NormSuspensionTravelRr': 80,
        'TireSlipRatioFl': 84,
        'TireSlipRatioFr': 88,
        'TireSlipRatioRl': 92,
        'TireSlipRatioRr': 96,
        'WheelRotationSpeedFl': 100,
        'WheelRotationSpeedFr': 104,
        'WheelRotationSpeedRl': 108,
        'WheelRotationSpeedRr': 112,
        'WheelOnRumbleStripFl': 116,
        'WheelOnRumbleStripFr': 120,
        'WheelOnRumbleStripRl': 124,
        'WheelOnRumbleStripRr': 128,
        'WheelInPuddleFl': 132,
        'WheelInPuddleFr': 136,
        'WheelInPuddleRl': 140,
        'WheelInPuddleRr': 144,
        'SurfaceRumbleFl': 148,
        'SurfaceRumbleFr': 152,
        'SurfaceRumbleRl': 156,
        'SurfaceRumbleRr': 160,
        'TireSlipAngleFl': 164,
        'TireSlipAngleFr': 168,
        'TireSlipAngleRl': 172,
        'TireSlipAngleRr': 176,
        'TireCombinedSlipFl': 180,
        'TireCombinedSlipFr': 184,
        'TireCombinedSlipRl': 188,
        'TireCombinedSlipRr': 192,
        'SuspensionTravelMetersFl': 196,
        'SuspensionTravelMetersFr': 200,
        'SuspensionTravelMetersRl': 204,
        'SuspensionTravelMetersRr': 208,
        'CarOrdinal ': 212,
        'CarClass ': 216,
        'CarPerformanceIndex ': 220,
        'DriveTrain ': 224,
        'NumCylinders ': 228,
        'PositionX': 232 + BufferOffset,
        'PositionY': 236 + BufferOffset,
        'PositionZ': 240 + BufferOffset,
        'Speed': 244 + BufferOffset,
        'Power': 248 + BufferOffset,
        'Torque': 252 + BufferOffset,
        'TireTempFl': 256 + BufferOffset,
        'TireTempFr': 260 + BufferOffset,
        'TireTempRl': 264 + BufferOffset,
        'TireTempRr': 268 + BufferOffset,
        'Boost': 272 + BufferOffset,
        'Fuel': 276 + BufferOffset,
        'Distance': 280 + BufferOffset,
        'BestLapTime': 284 + BufferOffset,
        'LastLapTime': 288 + BufferOffset,
        'CurrentLapTime': 292 + BufferOffset,
        'CurrentRaceTime': 296 + BufferOffset,
        'Lap': 300 + BufferOffset,
        'RacePosition ': 302 + BufferOffset,
        'Accelerator ': 303 + BufferOffset,
        'Brake ': 304 + BufferOffset,
        'Clutch ': 305 + BufferOffset,
        'Handbrake ': 306 + BufferOffset,
        'Gear ': 307 + BufferOffset,
        'Steer': 308 + BufferOffset,
        'NormalDrivingLine ': 309 + BufferOffset,
        'NormalAiBrakeDifference ': 310 + BufferOffset
    }

    # 开始位置
    Pstart = []

    for key, value in number_table.items():
        if key in Data:
            Pstart.append(value)

    Value2Return = Menu[Pstart[0]:Pstart[0]+BitSize]
    
    # print(Value2Return)
    return Value2Return





while True:
    recv_data = ForzaUDPSocket.recvfrom(8196)
    # recv_data存储元组（接收到的数据，（发送方的ip,port））
    recv_msg = recv_data[0] # 信息内容
    send_addr = recv_data[1] # 信息地址
    # 4.打印接收到的数据
    # print(recv_data)
    # print("信息来自:%s 内容是:%s" %(str(send_addr),recv_msg.decode("gbk")))
    # print('接收数据长度', len(recv_data[0]))
    # print(GetP(recv_data[0], "Speed"))
    image[:, :, 0] = np.uint8(GetP(recv_data[0], "AccelerationX"))  # Blue通道
    image[:, :, 1] = np.uint8(GetP(recv_data[0], "AccelerationY"))     # Green通道
    image[:, :, 2] = np.uint8(GetP(recv_data[0], "AccelerationZ"))     # Red通道
    cv2.imshow("Image", image)
    cv2.waitKey(1)


# 5.退出套接字
udp_socket.close()


