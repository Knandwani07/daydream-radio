# S3 Bucket Policy

This bucket policy allows public read access to objects stored in the S3 bucket used to host the Daydream Radio frontend.

---

## Purpose

The policy enables anyone on the internet to access files stored in the bucket, such as:

- HTML files
- CSS files
- JavaScript files
- Images and screenshots
- Other static website assets

This is commonly used when hosting a static website directly from Amazon S3.

---

## Permission Granted

### Public Object Read Access

```json
{
  "Sid": "PublicReadGetObject",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
}
```

This statement allows:

- Any user (`Principal: "*"`)
- To retrieve objects (`s3:GetObject`)
- From the specified S3 bucket

The permission applies only to objects inside the bucket and does not allow uploading, deleting, or modifying files.

---

## Complete Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
    }
  ]
}
```

---

## Security Notes

- This policy makes bucket objects publicly accessible.
- Only `GetObject` permission is granted.
- Users cannot upload, modify, or delete files.
- Replace `YOUR-BUCKET-NAME` with your actual S3 bucket name before deployment.
- For production workloads, consider using Amazon CloudFront and AWS Amplify for improved security, caching, and performance.

---

## Usage in Daydream Radio

The S3 bucket stores the static frontend assets for the application, including:

- `index.html`
- CSS styles
- JavaScript code
- Images and screenshots

Users access these files through a public HTTPS endpoint, allowing the Daydream Radio web application to load in a browser.
