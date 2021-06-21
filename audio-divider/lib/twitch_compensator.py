import moviepy.editor as mp


def compensator(folder_dir, audio_file):
    clip = mp.AudioFileClip(folder_dir)
    clip.write_audiofile(f'{folder_dir}\\f{audio_file}',
                         fps=11025,
                         bitrate='16k',
                         ffmpeg_params=['-vsync', '1'])
