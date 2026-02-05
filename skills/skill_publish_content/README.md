# Skill: Publish Content

## Purpose

Publish approved content to a target platform.

---

## Input Contract

```json
{
  "platform": "tiktok | instagram | youtube",
  "content_id": "string",
  "scheduled_time": "ISO-8601 timestamp",
  "caption": "string"
}

Output Contract
{
  "post_id": "string",
  "status": "published | scheduled",
  "platform_url": "string"
}
