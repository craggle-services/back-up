# back-up
{
  "version": 4,
  "terraform_version": "1.9.6",
  "serial": 269,
  "lineage": "18c8a02b-6f6d-00dd-ee71-80f2eb931bec",
  "outputs": {
    "api_base_url": {
      "value": "https://2y40hh32si.execute-api.ap-southeast-2.amazonaws.com/prod",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "managed",
      "type": "aws_api_gateway_deployment",
      "name": "deployment",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "canary_settings": [],
            "created_date": "2024-08-09T11:01:55Z",
            "description": "",
            "execution_arn": "arn:aws:execute-api:ap-southeast-2:730335633209:2y40hh32si/prod",
            "id": "ui8enu",
            "invoke_url": "https://2y40hh32si.execute-api.ap-southeast-2.amazonaws.com/prod",
            "rest_api_id": "2y40hh32si",
            "stage_description": null,
            "stage_name": "prod",
            "triggers": {
              "redeployment": "90c63469382c0da0efa1b148f0e498beda044d0a"
            },
            "variables": null
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_integration.integration",
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_api_gateway_integration",
      "name": "integration",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "index_key": "chat",
          "schema_version": 0,
          "attributes": {
            "cache_key_parameters": [],
            "cache_namespace": "dz8iaa",
            "connection_id": "",
            "connection_type": "INTERNET",
            "content_handling": "",
            "credentials": "",
            "http_method": "POST",
            "id": "agi-2y40hh32si-dz8iaa-POST",
            "integration_http_method": "POST",
            "passthrough_behavior": "WHEN_NO_MATCH",
            "request_parameters": {},
            "request_templates": {},
            "resource_id": "dz8iaa",
            "rest_api_id": "2y40hh32si",
            "timeout_milliseconds": 29000,
            "tls_config": [],
            "type": "AWS_PROXY",
            "uri": "arn:aws:apigateway:ap-southeast-2:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-southeast-2:730335633209:function:api_lambda/invocations"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "collect_data",
          "schema_version": 0,
          "attributes": {
            "cache_key_parameters": [],
            "cache_namespace": "nds1ye",
            "connection_id": "",
            "connection_type": "INTERNET",
            "content_handling": "",
            "credentials": "",
            "http_method": "GET",
            "id": "agi-2y40hh32si-nds1ye-GET",
            "integration_http_method": "POST",
            "passthrough_behavior": "WHEN_NO_MATCH",
            "request_parameters": {},
            "request_templates": {},
            "resource_id": "nds1ye",
            "rest_api_id": "2y40hh32si",
            "timeout_milliseconds": 29000,
            "tls_config": [],
            "type": "AWS_PROXY",
            "uri": "arn:aws:apigateway:ap-southeast-2:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-southeast-2:730335633209:function:api_lambda/invocations"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "get_session",
          "schema_version": 0,
          "attributes": {
            "cache_key_parameters": [],
            "cache_namespace": "f5swqp",
            "connection_id": "",
            "connection_type": "INTERNET",
            "content_handling": "",
            "credentials": "",
            "http_method": "GET",
            "id": "agi-2y40hh32si-f5swqp-GET",
            "integration_http_method": "POST",
            "passthrough_behavior": "WHEN_NO_MATCH",
            "request_parameters": {},
            "request_templates": {},
            "resource_id": "f5swqp",
            "rest_api_id": "2y40hh32si",
            "timeout_milliseconds": 29000,
            "tls_config": [],
            "type": "AWS_PROXY",
            "uri": "arn:aws:apigateway:ap-southeast-2:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-southeast-2:730335633209:function:api_lambda/invocations"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "get_statistics",
          "schema_version": 0,
          "attributes": {
            "cache_key_parameters": [],
            "cache_namespace": "ftgqol",
            "connection_id": "",
            "connection_type": "INTERNET",
            "content_handling": "",
            "credentials": "",
            "http_method": "GET",
            "id": "agi-2y40hh32si-ftgqol-GET",
            "integration_http_method": "POST",
            "passthrough_behavior": "WHEN_NO_MATCH",
            "request_parameters": {},
            "request_templates": {},
            "resource_id": "ftgqol",
            "rest_api_id": "2y40hh32si",
            "timeout_milliseconds": 29000,
            "tls_config": [],
            "type": "AWS_PROXY",
            "uri": "arn:aws:apigateway:ap-southeast-2:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-southeast-2:730335633209:function:api_lambda/invocations"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "new_session",
          "schema_version": 0,
          "attributes": {
            "cache_key_parameters": [],
            "cache_namespace": "ctxx3u",
            "connection_id": "",
            "connection_type": "INTERNET",
            "content_handling": "",
            "credentials": "",
            "http_method": "POST",
            "id": "agi-2y40hh32si-ctxx3u-POST",
            "integration_http_method": "POST",
            "passthrough_behavior": "WHEN_NO_MATCH",
            "request_parameters": {},
            "request_templates": {},
            "resource_id": "ctxx3u",
            "rest_api_id": "2y40hh32si",
            "timeout_milliseconds": 29000,
            "tls_config": [],
            "type": "AWS_PROXY",
            "uri": "arn:aws:apigateway:ap-southeast-2:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-southeast-2:730335633209:function:api_lambda/invocations"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_method.method",
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_api_gateway_method",
      "name": "method",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "index_key": "chat",
          "schema_version": 0,
          "attributes": {
            "api_key_required": false,
            "authorization": "NONE",
            "authorization_scopes": [],
            "authorizer_id": "",
            "http_method": "POST",
            "id": "agm-2y40hh32si-dz8iaa-POST",
            "operation_name": "",
            "request_models": {},
            "request_parameters": {},
            "request_validator_id": "",
            "resource_id": "dz8iaa",
            "rest_api_id": "2y40hh32si"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "collect_data",
          "schema_version": 0,
          "attributes": {
            "api_key_required": false,
            "authorization": "NONE",
            "authorization_scopes": [],
            "authorizer_id": "",
            "http_method": "GET",
            "id": "agm-2y40hh32si-nds1ye-GET",
            "operation_name": "",
            "request_models": {},
            "request_parameters": {},
            "request_validator_id": "",
            "resource_id": "nds1ye",
            "rest_api_id": "2y40hh32si"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "get_session",
          "schema_version": 0,
          "attributes": {
            "api_key_required": false,
            "authorization": "NONE",
            "authorization_scopes": [],
            "authorizer_id": "",
            "http_method": "GET",
            "id": "agm-2y40hh32si-f5swqp-GET",
            "operation_name": "",
            "request_models": {},
            "request_parameters": {},
            "request_validator_id": "",
            "resource_id": "f5swqp",
            "rest_api_id": "2y40hh32si"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "get_statistics",
          "schema_version": 0,
          "attributes": {
            "api_key_required": false,
            "authorization": "NONE",
            "authorization_scopes": [],
            "authorizer_id": "",
            "http_method": "GET",
            "id": "agm-2y40hh32si-ftgqol-GET",
            "operation_name": "",
            "request_models": {},
            "request_parameters": {},
            "request_validator_id": "",
            "resource_id": "ftgqol",
            "rest_api_id": "2y40hh32si"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        },
        {
          "index_key": "new_session",
          "schema_version": 0,
          "attributes": {
            "api_key_required": false,
            "authorization": "NONE",
            "authorization_scopes": [],
            "authorizer_id": "",
            "http_method": "POST",
            "id": "agm-2y40hh32si-ctxx3u-POST",
            "operation_name": "",
            "request_models": {},
            "request_parameters": {},
            "request_validator_id": "",
            "resource_id": "ctxx3u",
            "rest_api_id": "2y40hh32si"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_api_gateway_resource.resource",
            "aws_api_gateway_rest_api.api",
            "aws_iam_role.lambda_exec",
            "aws_lambda_function.api_lambda"
          ]
        }
      ]
    }
  ]
}
