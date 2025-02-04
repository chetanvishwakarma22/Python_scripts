aws={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data",
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}


print(aws)
print(aws["Version"])
print(aws["Statement"])
print(aws["Statement"][0])
print(aws["Statement"][1])
print(aws["Statement"][0]["Action"])
print(aws["Statement"][0]["Action"][0])
print(aws["Statement"][2]["Action"])
print(aws["Statement"][2]["Action"][0])
print(aws["Statement"][2]["Action"][1])
print(aws["Statement"][2]["Resource"])
print(aws["Statement"][2]["Resource"][0])
print(aws["Statement"][2]["Resource"][1])
print(aws["Statement"][2]["Condition"])
print(aws["Statement"][2]["Condition"]["Bool"])
print(aws["Statement"][2]["Condition"]["Bool"]["aws:MultiFactorAuthPresent"])
