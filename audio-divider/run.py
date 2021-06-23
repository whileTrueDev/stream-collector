from multiprocessing import Pool
import schedule
import time
import platform as pt
from lib.afreeca_divider import extractor
from lib.twitch_compensator import compensator
from lib.folder_handler import call_file_list, file_remover
from lib.s3_connect import S3Connector
from lib.db_connect import DbHandler
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)


class Main:

    # def __init__(self):
    #     self.db_conn = DbHandler()

    def main(self, platform):
        self.conn = S3Connector()
        self.db_conn = DbHandler()
        local_dir = os.getenv('LOCAL_DIRECTORY')
        folder_dir = local_dir + '\\' + platform if pt.system() == 'Windows' else f'./videos/{platform}'
        tmp_folder_dir = './tmp'

        for file in call_file_list(folder_dir):
            try:
                if platform == 'afreeca':
                    extractor(folder_dir, tmp_folder_dir, file)
                elif platform == 'twitch':
                    compensator(folder_dir, tmp_folder_dir, file)
            except Exception as e:
                print(f'error {e}')
            else:
                print(f'{file}수집된 파일 삭제')
                file_remover(folder_dir, file)

        for file_name in call_file_list(tmp_folder_dir):
            try:
                user_id = file_name.split('_')[1]
                stream_id = file_name.split('_')[2].split('.')[0]
                if user_id == 'kevin20222':
                    title = '2021-06-23 00:00:00'
                    client_id = '173919802'
                else:
                    title, client_id = self.db_conn.get_stream_date(stream_id)
                self.conn.upload_file(tmp_folder_dir, file_name, title, client_id)
            except Exception as e:
                print(f'error {e}')
            else:
                print(f'{file_name} 비트레이트 변경 파일 삭제')
                file_remover(tmp_folder_dir, file_name)

    def create_pool(self):
        with Pool(processes=2) as pool:
            platform_list = ['afreeca', 'twitch']
            pool.map(self.main, platform_list)

    def run(self):
        # self.create_pool()
        schedule.every(1).minutes.do(self.create_pool)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    exe = Main()

    exe.run()
