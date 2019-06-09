""" This script will create a bucket in AWS
    And print the buckets that are present for that profile
"""

import boto3 #AWS SDK for Python
import click
import sys

session = boto3.Session(profile_name='PythonAutomation') #A session stores configuration state and allows you to create service clients and resources

s3 = session.resource('s3') #Create a resource service client by name.

"""Create a bucket ; Test: automatingawstest
"""


#response = s3.create_bucket(
#    ACL='authenticated-read',
#    Bucket='automatingawstest',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'us-west-1'
#    },
"""    GrantFullControl='deny',
    GrantRead='deny',
    GrantReadACP='deny',
    GrantWrite='deny',
    GrantWriteACP='deny',
    ObjectLockEnabledForBucket=True"""
#)

"""Show all buckets
"""


@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass


@cli.command('list-buckets')
def list_buckets():
    "List All s3 Buckets" #Doc String
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command("list-bucket-objects")
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List All s3 Bucket Objects"
    for objects in s3.Bucket(bucket).objects.all():
        print(objects)


if __name__ == "__main__":
    cli()