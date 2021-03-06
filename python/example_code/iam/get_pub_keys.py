# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3

user_name = 'your-name'

# Create IAM client
iam = boto3.client('iam')

ssh_public_keys_response = iam.list_ssh_public_keys(
    UserName = user_name,
    MaxItems = 100,
)

# Get SSH public key
for ssh_public_key in ssh_public_keys_response['SSHPublicKeys']:
    ssh_public_key = ssh_public_key['SSHPublicKeyId']
    ssh_public_key_response = iam.get_ssh_public_key(
        UserName = user_name,
        SSHPublicKeyId = ssh_public_key,
        Encoding = 'SSH',
    )
    print(ssh_public_key_response['SSHPublicKey']['SSHPublicKeyBody'])
 

# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]
# snippet-sourcedescription:[get_pub_keys.py demonstrates how to retrieve the specified SSH public key.]
# snippet-keyword:[Python]
# snippet-sourcesyntax:[python]
# snippet-sourcesyntax:[python]
# snippet-keyword:[AWS SDK for Python (Boto3)]
# snippet-keyword:[Code Sample]
# snippet-keyword:[AWS Identity and Access Management (IAM)]
# snippet-service:[iam]
# snippet-sourcetype:[full-example]
# snippet-sourcedate:[]
# snippet-sourceauthor:[jschwarzwalder (AWS)]

