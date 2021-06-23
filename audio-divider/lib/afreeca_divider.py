import moviepy.editor as mp


def extractor(folder_dir, tmp_folder_dir, video_file, platform):
    clip = mp.VideoFileClip(f'{folder_dir}/{video_file}')
    clip.audio.write_audiofile(f'./tmp/{platform}_{video_file}.mp3',
                               ffmpeg_params=['-map', '0:a'],
                               fps=11025,
                               bitrate='16k',
                               )
