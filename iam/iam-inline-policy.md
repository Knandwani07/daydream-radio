# IAM Inline Policy

This IAM policy grants the Lambda function permission to invoke Amazon Bedrock models and interact with the DynamoDB table used by Daydream Radio.

---

## Purpose

The policy enables the Lambda function to:

1. Send prompts to Amazon Bedrock for story generation.
2. Store generated stories in DynamoDB.
3. Read story records from DynamoDB when needed.

---

## Permissions Granted

### Amazon Bedrock

```json
{
  "Sid": "BedrockInvoke",
  "Effect": "Allow",
  "Action": "bedrock:InvokeModel",
  "Resource": "*"
}
```

Allows the Lambda function to invoke foundation models through Amazon Bedrock.

Used for:

- Story generation
- Book recommendation generation

---

### Amazon DynamoDB

```json
{
  "Sid": "DynamoDBWriteRead",
  "Effect": "Allow",
  "Action": [
    "dynamodb:PutItem",
    "dynamodb:Scan"
  ],
  "Resource": "ARN_OF_PLAYLISTSTORIES_TABLE"
}
```

Allows the Lambda function to:

- Store newly generated stories (`PutItem`)
- Retrieve stored stories (`Scan`)

The permission is restricted to the **PlaylistStories** DynamoDB table.

---

## Complete Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockInvoke",
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": "*"
    },
    {
      "Sid": "DynamoDBWriteRead",
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:Scan"
      ],
      "Resource": "ARN_OF_PLAYLISTSTORIES_TABLE"
    }
  ]
}
```

---

## Security Notes

- The DynamoDB permission follows the principle of least privilege by restricting access to a single table.
- The Bedrock permission allows model invocation only and does not grant administrative access.
- In production environments, the Bedrock resource can be further restricted to specific model ARNs where supported.
