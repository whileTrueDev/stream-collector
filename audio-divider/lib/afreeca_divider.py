import moviepy.editor as mp


def extractor(folder_dir, video_file):
    clip = mp.VideoFileClip(f'{folder_dir}\\{video_file}')
    clip.audio.write_audiofile(r'C:\Users\whiletrue2\Desktop\stream-collector\audio-divider\audio\afreeca\test.mp4',
                               ffmpeg_params=['-map', '0:a'],
                               fps=11025,
                               bitrate='16k',
                               )
