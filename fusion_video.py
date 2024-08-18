import os
import cv2

vita = cv2.VideoCapture()
suo = cv2.VideoCapture()
filelist = []
for filename in os.listdir('./'):
    if filename[-3:] == 'mp4':
        filelist.append(filename)
if len(filelist) == 2:
    vita.open(filelist[0])
    suo.open(filelist[1])
    frames = [int(vita.get(cv2.CAP_PROP_FRAME_COUNT)),
              int(suo.get(cv2.CAP_PROP_FRAME_COUNT))]
    size = (max(int(vita.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(suo.get(cv2.CAP_PROP_FRAME_WIDTH))),
            max(int(vita.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                int(suo.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    shi = cv2.VideoWriter(
        "output.avi",
        cv2.VideoWriter_fourcc('A', 'V', 'C', '1'),  # 编码格式
        2 * max(int(vita.get(cv2.CAP_PROP_FPS)),
                int(suo.get(cv2.CAP_PROP_FPS))),
        size
    )
    for i in range(2 * min(frames)):
        if i % 2 < 1:
            _, frame = vita.read()
        else:
            _, frame = suo.read()
        shi.write(frame)
    shi.release()
    vita.release()
    suo.release()


