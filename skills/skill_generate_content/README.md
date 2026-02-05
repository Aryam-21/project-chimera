# Skill: Generate Content

## Purpose

Generate platform-optimized content based on trends and brand constraints.

---

## Input Contract

```json
{
  "platform": "tiktok | instagram | youtube",
  "trend_topic": "string",
  "tone": "educational | entertaining | promotional",
  "brand_constraints": ["string"],
  "max_length_seconds": 60
}

Output Contract
{
  "script": "string",
  "hook": "string",
  "hashtags": ["string"],
  "confidence_score": 0.0
}