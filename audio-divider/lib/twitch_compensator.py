import moviepy.editor as mp


def compensator(folder_dir, tmp_folder_dir, audio_file):
    clip = mp.AudioFileClip(f'{folder_dir}/{audio_file}')
    clip.write_audiofile(f'{tmp_folder_dir}/{audio_file}',
                         fps=11025,
                         bitrate='16k',
                         ffmpeg_params=['-vsync', '1'])
