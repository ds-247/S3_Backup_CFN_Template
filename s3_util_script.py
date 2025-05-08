import boto3
import zipfile

BUCKET_NAME = 'lambda-copy-code-bucket'
REGION_NAME = 'ap-south-1'
ZIP_FILE_NAME = 'lambda_function.zip'
LAMBDA_HANDLER_FILE_PATH= 'lambda_function.py'

def create_bucket(s3_client, bucket_name, region):
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region},
        )
        print(f"Bucket {bucket_name} created:")
        return True
    except Exception as e:
        print(f"Error creating bucket {bucket_name}: {e}")
        return False


def zip_lambda_function():
    try:
        with zipfile.ZipFile(ZIP_FILE_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(LAMBDA_HANDLER_FILE_PATH)
        print(f"Zipped {LAMBDA_HANDLER_FILE_PATH} to {ZIP_FILE_NAME}")
        return True
    except Exception as e:
        print(f"Error zipping {LAMBDA_HANDLER_FILE_PATH}: {e}")
        return False


def upload_to_s3(s3_client, bucket_name, file_path):
    try:
        s3_client.upload_file(file_path, bucket_name, file_path)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{file_path}")
        return True
    except Exception as e:
        print(f"Error uploading {file_path} to s3://{bucket_name}: {e}")
        return False


def main() :
    s3 = boto3.client('s3', REGION_NAME)
    # if not create_bucket(s3, BUCKET_NAME, REGION_NAME):
    #     return
    
    # if not zip_lambda_function():
    #     return

    # if not upload_to_s3(s3, BUCKET_NAME, ZIP_FILE_NAME):
    #     return

    
    

    

if __name__ == "__main__":
    main()