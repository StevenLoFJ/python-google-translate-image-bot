import boto3
from botocore.exceptions import NoCredentialsError
from boto3.s3.transfer import S3Transfer
def uploadToS3(dir, bucket, fileName):
    
    # If S3 object_name was not specified, use file_name
    s3client = boto3.client(
        's3',
#add aws cred here
         )
    
    transfer = S3Transfer(s3client)
    prefix= 'img-result/'
    try:
        transfer.upload_file(dir+fileName, bucket, prefix+fileName, extra_args={'ServerSideEncryption': "AES256"})
        return f'https://itemku-upload-alpha.s3.ap-southeast-1.amazonaws.com/{prefix+fileName}'
    
    except NoCredentialsError:
        print("Credentials not available")