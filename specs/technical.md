# Technical Specification

## Agent API Contracts

### Trend Discovery Agent
**Input**
```json
{
  "platform": "youtube",
  "region": "global",
  "time_window_hours": 24
}
Output

{
  "videos": [
    {
      "video_id": "abc123",
      "platform": "youtube",
      "title": "AI Agents Explained",
      "views": 120000,
      "likes": 8400,
      "published_at": "2026-02-01T10:00:00Z"
    }
  ]
}

Content Analysis Agent

Input

{
  "video_id": "abc123",
  "title": "...",
  "description": "...",
  "transcript": "..."
}


Output

{
  "topics": ["AI agents", "automation"],
  "sentiment": "positive",
  "engagement_score": 0.87
}

Synthesis Agent

Input

{
  "analysis_results": [...],
  "time_window_hours": 24
}


Output

{
  "summary": "AI agent tooling is rapidly trending across platforms.",
  "confidence": 0.82,
  "supporting_videos": ["abc123", "def456"]
}

Database Schema (Logical ERD)
Video

video_id (PK)

platform

title

description

published_at

views

likes

Analysis

analysis_id (PK)

video_id (FK)

topics

sentiment

engagement_score

TrendReport

report_id (PK)

summary

confidence

created_at

TrendVideo (Join Table)

report_id (FK)

video_id (FK)


---

