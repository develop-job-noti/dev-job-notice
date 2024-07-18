
# System
import os
import boto3

# Project
from core.constants import AWS


def get_aws_s3():
    return None


class S3:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS.AWS_SECRET_ACCESS_KEY,
        region_name=AWS.AWS_S3_REGION_NAME
    )

    @classmethod
    def file_upload(cls, file_path, s3_path):
        cls.s3_client.upload_file(
            file_path,
            AWS.AWS_S3_BUCKET_NAME,
            s3_path
        )
        return True

    @classmethod
    def get_file(cls, file_key, local_path):
        with open(local_path, 'wb') as f:
            cls.s3_client.download_fileobj(AWS.AWS_S3_BUCKET_NAME, file_key, f)

    @classmethod
    def prefix_exits(cls, path):

        res = cls.s3_client.list_objects_v2(
            Bucket=AWS.AWS_S3_BUCKET_NAME,
            Prefix=path,
            MaxKeys=1
        )

        return 'Contents' in res

    @classmethod
    def list_files(cls, prefix):
        response = cls.s3_client.list_objects_v2(
            Bucket=AWS.AWS_S3_BUCKET_NAME,
            Prefix=prefix
        )
        if 'Contents' in response:
            return [content['Key'] for content in response['Contents']]
        return []

    @classmethod
    def upload_directory(cls, directory_path, s3_prefix):
        for root, _, files in os.walk(directory_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, directory_path)
                s3_path = os.path.join(
                    s3_prefix, relative_path).replace("\\", "/")
                cls.file_upload(local_path, s3_path)
