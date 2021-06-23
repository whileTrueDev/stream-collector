from os import remove, listdir


def call_file_list(path):
    """
        path : 파일 경로
    """
    path_dir = path
    file_list = listdir(path_dir)
    # 날짜순 정렬
    file_list = sorted(file_list)
    return file_list


def file_remover(folder_dir, file_name):
    remove('/'.join([folder_dir, file_name]))
