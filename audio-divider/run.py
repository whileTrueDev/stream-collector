from multiprocessing import Pool
from lib.afreeca_divider import extractor
from lib.twitch_compensator import compensator
from lib.folder_handler import call_file_list, file_remover
from lib.s3_connect import S3Connector
from lib.db_connect import DbHandler
import os


class Main:

    # def __init__(self):
    #     self.db_conn = DbHandler()

    def main(self, platform):
        self.conn = S3Connector()
        self.db_conn = DbHandler()

        folder_dir = f'./videos/{platform}'
        tmp_folder_dir = './tmp'
        print(folder_dir)

        for file in call_file_list(folder_dir):
            try:
                if platform == 'afreeca':
                    extractor(folder_dir, file, platform)
                elif platform == 'twitch':
                    compensator(folder_dir, file, platform)
            except Exception as e:
                print(f'error {e}')
            else:
                print('file romove')
                # file_remover(folder_dir, file)

        for file_name in call_file_list(tmp_folder_dir):
            try:
                stream_id = file_name.split('_')[2].split('.')[0]
                title = self.db_conn.get_stream_date(stream_id)
                self.conn.upload_file(tmp_folder_dir, file_name, title)
            except Exception as e:
                print(f'error {e}')
            else:
                file_remover(tmp_folder_dir, file_name)

    def run(self):
        with Pool(processes=2) as pool:
            platform_list = ['afreeca', 'twitch']
            pool.map(self.main, platform_list)


if __name__ == '__main__':
    Main().run()
