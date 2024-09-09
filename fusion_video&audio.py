import os
from pydub import AudioSegment as AS
import cv2
import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip

vita = cv2.VideoCapture()
suo = cv2.VideoCapture()
filelist = []
final_fps = 0
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
    final_fps = 2 * max(int(vita.get(cv2.CAP_PROP_FPS)),
                int(suo.get(cv2.CAP_PROP_FPS)))
    shi = cv2.VideoWriter(
        "output.mp4",
        cv2.VideoWriter_fourcc('a', 'v', 'c', '1'),  # 编码格式
        final_fps,
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

for videoname in os.listdir('./'):
    if videoname == 'output.mp4':
        hua = VideoFileClip('./'+videoname)
        final_bps = str(ffmpeg.probe('./'+videoname)['bit_rate'])+'k'
        for audioname in os.listdir('./'):
            if audioname[-3:] == 'wav':
                su = AudioFileClip('./'+audioname)
                song = AS.from_file('./'+audioname, format='wav')
                final_audio_bps = str((song.frame_rate / 1000) * song.sample_width * 8 * song.channels) + 'k'
                hua = hua.set_audio(su)
                hua.write_videofile('./'+'output.mp4', fps=final_fps, codec='mpeg4',
                                    bitrate=final_bps, audio=True, audio_fps=48000,
                                    preset="medium", audio_codec=None,
                                    audio_bitrate=final_audio_bps, audio_bufsize=2000)
                break
        break




