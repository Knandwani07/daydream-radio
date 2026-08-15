# Frontend

This is the frontend application for Daydream Radio, built using HTML, CSS, and vanilla JavaScript. It provides an interface for users to enter an ordered sequence of moods, optionally associate songs with those moods, and generate AI-powered stories through an AWS backend.

## Features

- Add and remove mood entries dynamically
- Optional song title input for each mood
- Example mood sequences for quick testing
- Story generation through API Gateway and AWS Lambda
- Display AI-generated stories and book recommendations
- Responsive design inspired by vinyl records and album liner notes

## Technologies Used

- HTML5
- CSS3
- JavaScript (Vanilla JS)
- Amazon API Gateway
- AWS Lambda
- Amazon Bedrock

## How It Works

1. User enters moods and optional song titles.
2. The frontend sends the data to the API Gateway endpoint.
3. AWS Lambda processes the request and generates a story using Amazon Bedrock.
4. The generated story and book recommendation are returned to the browser and displayed to the user.

## Configuration

Update the API endpoint before deployment:

```javascript
const API_URL = "YOUR_INVOKE_URL/generate";
```

## Main Components

- Mood Sequencer Input Form
- Example Mood Presets
- Story Generation Interface
- Book Recommendation Card
- Loading and Error States

This frontend is designed to be hosted as a static website using AWS Amplify or Amazon S3. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}
