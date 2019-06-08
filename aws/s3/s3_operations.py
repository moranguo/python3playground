import boto3


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-central-1'
        }
    )


if __name__ == "__main__":
    create_bucket("babababab")
