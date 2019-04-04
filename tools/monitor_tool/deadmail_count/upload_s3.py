#! /usr/bin/python

import boto3

REGION='eu-central-1'
ACCESS_KEY='xxx'
SECRET_KEY='xxx'
s3 = boto3.resource('s3', region_name=REGION, aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
data = open('count.txt', 'rb')
s3.Bucket('test-bucket').put_object(Key='count.txt', Body=data)
# need to close data, otherwise memory leak
data.close()