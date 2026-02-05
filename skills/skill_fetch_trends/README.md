# Skill: Fetch Trends

## Purpose

Retrieve current platform trends to inform content generation.

---

## Input Contract

```json
{
  "platform": "tiktok | instagram | youtube | x",
  "region": "string",
  "time_window_hours": 24,
  "category": "optional string"
}

## Output Contract

{
  "trends": [
    {
      "topic": "string",
      "velocity_score": 0.0,
      "sample_posts": ["string"]
    }
  ],
  "fetched_at": "ISO-8601 timestamp"
}