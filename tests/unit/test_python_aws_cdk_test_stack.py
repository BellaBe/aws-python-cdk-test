import aws_cdk as core
import aws_cdk.assertions as assertions

from python_aws_cdk_test.python_aws_cdk_test_stack import PythonAwsCdkTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_aws_cdk_test/python_aws_cdk_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonAwsCdkTestStack(app, "python-aws-cdk-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
