from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,
)
from constructs import Construct


class VPCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        project_name = self.node.try_get_context("project_name")
        env_name = self.node.try_get_context("env")

        self.vpc = ec2.Vpc(
            self,
            "devVPC",
            cidr="172.32.0.0/16",
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    cidr_mask=24
                ),
                 ec2.SubnetConfiguration(
                    name="Isolated",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24
                ),
            ],
            nat_gateways=1
        )

        private_subnets = [subnet.subnet_id for subnet in self.vpc.private_subnets]
        
        count:int = 1

        for ps in private_subnets:
            ssm.StringParameter(self, f"private-subnet{count}",
                string_value=ps,
                parameter_name= f"/{env_name}/private-subnet{count}"
            )
            count += 1
