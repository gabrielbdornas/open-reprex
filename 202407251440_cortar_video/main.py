from pathlib import Path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime, timedelta

def time_to_seconds(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M:%S')
    delta = timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second)
    return delta.total_seconds()

path = Path(__file__).parent
video_name = 'webnar_8.mp4' # mudar nome do audio
video_path = path / 'arquivos' / video_name
cut_video_path = path / 'webnar_8_cortado.mp4'
# hh:mm:ss
time_start = time_to_seconds('00:00:00')
time_end = time_to_seconds('02:40:00')

ffmpeg_extract_subclip(
    video_path,
    time_start,
    time_end,
    targetname=cut_video_path)
