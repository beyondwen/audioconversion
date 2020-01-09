from pydub import AudioSegment

AudioSegment.converter = r"D:\\work\\audioconversion\\ffmpeg.exe"
song = AudioSegment.from_mp3("D:\\work\\audioconversion\\DJ阿福 - 陈公子专属音乐.mp3")
song.export("D:\\work\\audioconversion\\test.mp4", format="mp4", bitrate="320k")
