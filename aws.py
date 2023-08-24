了解しました。API Gateway での Auth0 認証に関して、以下の手順とサンプルコードを提供します。

1. Lambda Authorizer の作成
Auth0 から発行された JWT トークンを検証するための Lambda Authorizer を作成します。

python
Copy code
import jwt
import requests

AUTH0_DOMAIN = 'YOUR_AUTH0_DOMAIN'
AUTH0_AUDIENCE = 'YOUR_API_AUDIENCE'
JWKS_URL = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'

def lambda_handler(event, context):
    token = event['authorizationToken']
    header = jwt.get_unverified_header(token)
    jwks = requests.get(JWKS_URL).json()
    rsa_key = {}
    for key in jwks['keys']:
        if key['kid'] == header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e'],
            }
    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=['RS256'],
            audience=AUTH0_AUDIENCE,
            issuer=f'https://{AUTH0_DOMAIN}/'
        )
        return {
            'principalId': payload['sub'],
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': event['methodArn']
                }]
            }
        }
    except Exception as e:
        print(e)
        raise Exception('Unauthorized')

このコードは、Auth0 からの JWT トークンをデコードし、正しいかどうかを検証します。正しい場合、API Gateway エンドポイントへのアクセスを許可するポリシードキュメントを返します。

2. CloudFormation YAML の設定
以下は、上記の Lambda Authorizer を使用して API Gateway を設定する CloudFormation YAML の一部です：

yaml
Copy code
Resources:
  Auth0AuthorizerFunction:
    Type: AWS::Lambda::Function
    Properties: 
      Handler: index.lambda_handler
      Role: arn:aws:iam::YOUR_ACCOUNT_ID:role/execution_role
      FunctionName: Auth0AuthorizerFunction
      CodeUri: ./path_to_your_lambda_code/
      Runtime: python3.8

  ApiGatewayAuth0Authorizer:
    Type: 'AWS::ApiGateway::Authorizer'
    Properties:
      AuthorizerResultTtlInSeconds: 300
      IdentitySource: 'method.request.header.Authorization'
      Name: auth0-authorizer
      RestApiId: 
        Ref: YourApiGatewayResource
      Type: TOKEN
      AuthType: custom
      AuthorizerUri: 
        Fn::Sub: arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${Auth0AuthorizerFunction.Arn}/invocations
注意: 上記の YAML は例示的なものであり、実際の環境や要件に合わせて適切に変更する必要があります。

これで、API Gateway のエンドポイントは Auth0 で生成された JWT トークンを必要とするようになります。正しいトークンを持っているクライアントのみがアクセスを許可されます。