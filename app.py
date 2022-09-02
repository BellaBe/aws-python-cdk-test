#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.python_aws_cdk_test_stack import PythonAwsCdkTestStack
from stacks.security_stack import SecurityStack
from stacks.vpc_stack import VPCStack


app = cdk.App()

vpc_stack = VPCStack(app, "vpcStack");
security_stack = SecurityStack(app, "securityStack", vpc=vpc_stack)

app.synth()
