import json
import boto3
import uuid
from datetime import datetime, timezone

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("PlaylistStories")

MODEL_ID = "amazon.nova-micro-v1:0"

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        pairs = body.get("pairs", [])  # expects [{"song": "...", "mood": "..."}, ...]

        if not pairs or not isinstance(pairs, list):
            return _response(400, {"error": "Request must include a non-empty 'pairs' list."})

        # Build the ordered mood sequence text
        sequence_lines = []
        for i, p in enumerate(pairs, start=1):
            song = str(p.get("song", "")).strip()
            mood = str(p.get("mood", "")).strip()
            if not mood:
                return _response(400, {"error": f"Entry {i} is missing a 'mood'."})
            sequence_lines.append(f"{i}. \"{song}\" — mood: {mood}" if song else f"{i}. mood: {mood}")
        sequence_text = "\n".join(sequence_lines)

        prompt = (
            "You are a short-fiction writer. Below is an ordered sequence of moods "
            "from a music playlist, each optionally paired with a song title. "
            "Write a story of medium length (200-250 words, roughly 2 short paragraphs)"
            "whose emotional arc follows this exact sequence, moving from one mood to "
            "the next in order. Do not mention the song titles or the word 'playlist' "
            "directly — let the moods drive the story instead.\n\n"
            f"Mood sequence:\n{sequence_text}\n\n"
            "After the story, on a new line, write exactly:\n"
            "BOOK_REC: [Title] by [Author] — [one-sentence reason it fits this mood]\n\n"
            "Only recommend a real, extremely famous, bestselling romantic comedy novel "
            "published in book form (not a movie, TV show, or screenplay). Double-check "
            "the author actually wrote that specific book before answering. If you are "
            "not certain both the title and author are correct together, choose a "
            "different, safer, more universally known title such as 'Pride and Prejudice' "
            "by Jane Austen or 'Bridget Jones's Diary' by Helen Fielding instead."
            "choose a different, more famous rom-com novel instead."
        )

        nova_body = {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 400,
                "temperature": 0.8
            }
        }

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(nova_body),
            contentType="application/json",
            accept="application/json"
        )

        response_body = json.loads(response["body"].read())
        raw_text = response_body["output"]["message"]["content"][0]["text"]

        # Split story from book recommendation
        if "BOOK_REC:" in raw_text:
            story_part, rec_part = raw_text.split("BOOK_REC:", 1)
            story_text = story_part.strip()
            book_rec = rec_part.strip()
        else:
            story_text = raw_text.strip()
            book_rec = None

        story_id = str(uuid.uuid4())
        table.put_item(Item={
            "storyId": story_id,
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "moodSequence": pairs,
            "story": story_text,
            "bookRec": book_rec
        })

        return _response(200, {
            "storyId": story_id,
            "story": story_text,
            "bookRec": book_rec
        })

    except (json.JSONDecodeError, KeyError) as e:
        return _response(400, {"error": f"Malformed request or unexpected model response: {str(e)}"})
    except Exception as e:
        return _response(500, {"error": f"Server error: {str(e)}"})


def _response(status_code, payload):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps(payload)
    }
