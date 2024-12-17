from boto3.session import Session
import boto3
import logging
import os


logging.basicConfig(filename="log.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# Let's use Amazon S3
s3 = boto3.resource("s3")

# Print out bucket names to check you have accessibility
# for bucket in s3.buckets.all():
#     print(bucket.name)

#session = Session()
#OR
aws_access_key_id_val = os.environ["aws_access_key_id"]
aws_secret_access_key_val = os.environ["aws_secret_access_key"]
region_name_val = os.environ["region_name"]

# for debugging 
print(f"aws_access_key_id_val={aws_access_key_id_val} aws_secret_access_key_val={aws_secret_access_key_val} region_name_val={region_name_val} ")
logging.info("trying to connect to s3")
try:
    session = Session(aws_access_key_id=aws_access_key_id_val,
                      aws_secret_access_key=aws_secret_access_key_val,
                      region_name=region_name_val)    
    logging.info("session object created...")
    session.resource('s3').Bucket('bucket-logs').download_file(Key="logs/20221122_0_5ee03da676ac566336e2279decfc77b3.gz", Filename="/tmp/Local_file_name.gz")
    logging.info("log file was downloaded")
except Exception as e:
    logging.error(e)