# 🎵 Daydream Radio

> Every playlist has an emotional shape. Daydream Radio turns that shape into a story.

<img width="1303" height="873" alt="image" src="https://github.com/user-attachments/assets/dc36e38f-0995-4d67-ad45-319c6bff6681" />


Daydream Radio is a generative storytelling application that transforms an ordered sequence of moods into a short narrative whose emotional arc follows the exact progression provided by the user. Alongside the story, the application recommends a book that matches the same emotional journey.

Instead of generating generic text from a single mood, Daydream Radio is built around **sequence**. The order of moods entered by the user directly determines how the story unfolds, making each generated narrative a reflection of the playlist's emotional progression.

---

## ✨ Features

- Generate original stories from mood sequences
- Emotional arc follows the exact order of moods entered
- Optional song titles for additional context
- AI-powered story generation using Amazon Bedrock (Nova Micro)
- Personalized book recommendations
- Story persistence using DynamoDB
- Responsive, single-page web interface
- Fully serverless AWS architecture

---

## 🏗️ Architecture

```text
Browser
   │
   ▼
Amazon API Gateway
   │
   ▼
AWS Lambda
   │
   ├── Amazon Bedrock (Nova Micro)
   │       └── Story & Book Recommendation Generation
   │
   └── Amazon DynamoDB
           └── Story Persistence
   │
   ▼
Response Returned to Browser
```

---

## ☁️ AWS Services Used
<ul>
<li>Amazon Bedrock (Nova Micro)</li>
<li>AWS Lambda</li>
<li>Amazon API Gateway</li>
<li>Amazon DynamoDB</li>
<li>AWS Amplify</li>
</ul>

---

## 🖥️ Frontend

The frontend is a lightweight single-page application built with:

- HTML
- CSS
- Vanilla JavaScript

Users can:

- Add mood entries
- Optionally associate songs with moods
- Generate stories
- View AI-generated book recommendations

The interface is styled to resemble album liner notes and vinyl record sleeves, reinforcing the music-inspired experience.

---


## 📂 Project Structure

```text
daydream-radio/
│
├── backend/
│   ├── generate-playlist-story-lambda.md
│   └── lambda_function.py
│
├── frontend/
│   ├── README.md
│   └── index.html
│
├── iam/
│   ├── iam-inline-policy.md
│   └── inline-policy.json
│
├── policies/
│   ├── bucket-policy.md
│   └── bucket-policy.json
│
├── README.md
│
└── learnings-and-improvements.md
```

---
## Folder/File Purpose


| Path                                        | Description                                                                 |
| ------------------------------------------- | --------------------------------------------------------------------------- |
| `backend/lambda_function.py`                | Lambda function that generates stories using Amazon Bedrock and stores them in DynamoDB |
| `backend/generate-playlist-story-lambda.md` | Documentation for the Lambda function                                       |
| `frontend/index.html`                       | Frontend application UI                                                     |
| `frontend/README.md`                        | Frontend documentation                                                      |
| `iam/inline-policy.json`                    | IAM policy attached to the Lambda execution role                            |
| `iam/iam-inline-policy.md`                  | Explanation of IAM permissions                                              |
| `policies/bucket-policy.json`               | S3 bucket policy for static website hosting                                 |
| `policies/bucket-policy.md`                 | Explanation of the bucket policy                                            |
| `learnings-and-improvements.md`             | Key lessons learned and future enhancements                                 |
| `README.md`                                 | Main project documentation and architecture overview                        |
---

## 🌐 Live Demo

**Application:**  
https://staging.d112uiupbxweq8.amplifyapp.com/

---

## 👤 Author

**Khushi Nandwani**

---

## 🤝 Let's Connect

- 💼 **LinkedIn:** https://www.linkedin.com/in/khushi-nandwani/
- 💻 **GitHub:** https://github.com/Knandwani07
- 📬 **Substack:** https://substack.com/@khushinandwani07
- ✍️ **Dev Community:** https://dev.to/khushi_nandwani07
- 📝 **Medium:** https://medium.com/@khushinandwanii
- 🌐 **Portfolio:** https://main.d1n4wt6uo5bfx6.amplifyapp.com/

