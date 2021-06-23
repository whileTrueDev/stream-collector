import boto3
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class S3Connector:
    def __init__(self):
        self.s3 = boto3.client('s3',
                               aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                               aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                               region_name=os.getenv('AWS_DEFAULT_REGION'),
                               )
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')

    def upload_file(self, path, file_name, title, client_id):

        platform = file_name.split('_')[0]
        stream_id = file_name.split('_')[2].split('.')[0]
        home_directory = os.getenv('HOME_DIRECTORY')

        self.s3.upload_file(
            f'{path}/{file_name}',
            self.bucket_name,
            f'{home_directory}/{platform}/{client_id}/{stream_id}/audio/{title} 방송.mp3',
        )
