import shutil


def file_move(origin_dir, target_dir):
    original = origin_dir
    target = target_dir
    shutil.move(original, target)
