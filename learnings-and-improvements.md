# Learnings and Improvements

## Key Learnings

### 1. CORS Configuration Matters

One of the most valuable lessons from this project was learning that API Gateway CORS settings are separate from the CORS headers returned by Lambda. Even when Lambda returned the correct headers, the browser blocked requests until CORS was explicitly configured and deployed at the API Gateway level.

### 2. Small Configuration Errors Cause Big Issues

A simple Lambda handler mismatch (`handler` vs `lambda_handler`) resulted in a `Runtime.HandlerNotFound` error. This reinforced the importance of checking runtime configuration before assuming the application logic is broken.

### 3. CloudWatch Logs Are Essential

Browser errors such as "Failed to fetch" often provide very little information. Using CloudWatch Logs made it much easier to identify and resolve backend issues quickly.

### 4. Prompt Engineering Improves Reliability

Amazon Nova Micro can generate creative and useful content, but it may occasionally produce incorrect information with high confidence. Careful prompt design significantly improved the consistency and reliability of generated book recommendations.

### 5. Backend-First Development Simplifies Testing

Building and validating the backend before creating the frontend made troubleshooting much easier. Lambda functions could be tested independently before introducing browser and networking complexities.

---

## Future Improvements

### Spotify Integration

Allow users to import moods directly from Spotify playlists instead of entering them manually.

### Story History

Provide a gallery where users can revisit previously generated stories.

### User Authentication

Enable users to create accounts and save their favorite stories.

### Multiple Story Styles

Allow story generation in different genres such as romance, fantasy, mystery, and science fiction.

### Improved Recommendations

Enhance book recommendation validation to reduce the possibility of incorrect title-author pairings.

### Story Sharing

Generate shareable links for stories and recommendations.

### AI-Generated Cover Art

Create custom cover images based on the mood sequence and generated story.

### Analytics Dashboard

Track generation counts, popular moods, and user engagement metrics.
