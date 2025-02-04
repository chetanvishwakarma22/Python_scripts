import boto3
import argparse

parse = argparse.ArgumentParser(description="CLI to create EC2 instance")

parse.add_argument("ami", help="Instance Image ID (ami id) that we need to use for creating e 2 instance")
parse.add_argument("type", help="Instance Type")
parse.add_argument("Key", help="ssh key to connect to instance")
parse.add_argument("min", type=int, help="minimum number of instance to create")
parse.add_argument("max", type=int, help="maximum number of instance to create")
args = parse.parse_args()
ec2 = boto3.resource("ec2")


ec2.create_instances(ImageId=args.ami, InstanceType=args.type, KeyName=args.Key, MinCount=args.min, MaxCount=args.max)
print("EC2 instance created")
