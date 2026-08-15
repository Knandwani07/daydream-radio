# Generate Playlist Story Lambda

This AWS Lambda function powers the backend of **Daydream Radio**. It accepts an ordered sequence of moods (optionally paired with song titles), generates a story whose emotional arc follows that sequence using Amazon Bedrock (Nova Micro), recommends a matching book, and stores the result in Amazon DynamoDB.

---

## What This Function Does

1. Receives a request from API Gateway.
2. Validates the submitted mood sequence.
3. Builds a prompt based on the ordered moods.
4. Sends the prompt to Amazon Bedrock (Nova Micro).
5. Extracts the generated story and book recommendation.
6. Stores the result in DynamoDB.
7. Returns the generated content to the frontend.

---

## AWS Services Used

- **Amazon Bedrock (Nova Micro)** – Generates stories and book recommendations.
- **AWS Lambda** – Runs the serverless backend logic.
- **Amazon DynamoDB** – Stores generated stories and metadata.
- **Amazon API Gateway** – Exposes the Lambda function through an HTTP endpoint.

---

## Expected Request Format

```json
{
  "pairs": [
    {
      "song": "Blinding Lights",
      "mood": "restless energy"
    },
    {
      "song": "Golden Hour",
      "mood": "dreamy detachment"
    },
    {
      "song": "Daylight",
      "mood": "wide-awake clarity"
    }
  ]
}
```

The `song` field is optional, but every entry must contain a valid `mood`.

---

## Example Response

```json
{
  "storyId": "12345678-abcd-1234-abcd-1234567890ab",
  "story": "Generated story text...",
  "bookRec": "Pride and Prejudice by Jane Austen — A charming story that mirrors the emotional journey."
}
```

---

## DynamoDB Table

Table Name:

```text
PlaylistStories
```

Stored Attributes:

```json
{
  "storyId": "uuid",
  "createdAt": "timestamp",
  "moodSequence": [],
  "story": "generated story",
  "bookRec": "book recommendation"
}
```

---

## Environment Configuration

```python
MODEL_ID = "amazon.nova-micro-v1:0"
TABLE_NAME = "PlaylistStories"
REGION = "us-east-1"
```

---

## Error Handling

The function handles:

- Invalid JSON requests
- Missing mood entries
- Empty mood sequences
- Unexpected Bedrock responses
- Internal server errors

Appropriate HTTP status codes are returned for each error scenario.

---

## CORS Support

The Lambda response includes CORS headers to allow requests from the frontend application:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: OPTIONS,POST
```

---

## Flow

```text
Frontend
    │
    ▼
API Gateway
    │
    ▼
AWS Lambda
    │
    ├── Amazon Bedrock (Nova Micro)
    │       └── Generate Story + Book Recommendation
    │
    └── Amazon DynamoDB
            └── Store Generated Story
    │
    ▼
Response Returned to Frontend
```
