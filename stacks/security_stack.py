from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_ssm as ssm,
)
from constructs import Construct


class SecurityStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        project_name = self.node.try_get_context("project_name")
        env_name = self.node.try_get_context("env")

        lambda_security_group = ec2.SecurityGroup(
            self, 
            "lambdaSecurityGroup",
            security_group_name="lambda_security_group",
            vpc=vpc,
            description="Security group for lambda functions",
            allow_all_outbound=True
        )

        