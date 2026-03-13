# EdrawMax AI Diagram Skill

> **Author:** EdrawMax AI Team · **Organization:** Wondershare EdrawMax  
> **Version:** 2.0.0 · **License:** Proprietary © 2026 Wondershare EdrawMax. All rights reserved.

An AI skill for AI Agent(OpenClaw, Claude Code etc.) that generates professional diagrams from natural language descriptions using EdrawMax AI APIs.

---

## What This Skill Does

The `edrawmax-diagram` skill lets you describe a diagram in plain language and instantly receive a rendered image (PNG + SVG) along with the editable source code. It supports four diagram types:

| Diagram Type | Best For | API Endpoint |
|---|---|---|
| **Flowchart** | Processes, workflows, decision trees | `/skills/generate-flowchart` |
| **Infographic** | Data visualization, statistics, comparisons | `/skills/generate-infographic` |
| **Gantt Chart** | Project plans, timelines, schedules | `/skills/generate-gantt` |
| **Mind Map** | Knowledge maps, brainstorming, topic trees | `/skills/generate-mindmap` |

### What Problems It Solves

- **No design skills needed** — describe what you want in natural language; the AI handles layout, styling, and rendering.
- **Instant visual output** — get PNG and SVG files downloaded locally in seconds, ready to embed in docs or presentations.
- **Editable source code** — every diagram comes with its source code (Mermaid for flowcharts; proprietary DSL for others) so you can refine it later.
- **Multi-language support** — generate diagrams in 12 languages: English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Spanish, French, German, Italian, Portuguese, Russian, and Indonesian.

---

## Quick Start

### Trigger Phrases

The skill activates automatically when you say things like:

- *"Generate a flowchart for the user registration process"*
- *"Create a mind map for machine learning concepts"*
- *"Draw a Gantt chart for a 3-month product launch"*
- *"Make an infographic about global AI market trends in 2025"*

### API Base URL

```
https://api.edrawmax.cn/api/ai
```

### Request Format

```http
POST https://api.edrawmax.cn/api/ai/skills/generate-{type}
Content-Type: application/json

{
  "prompt": "your description here",
  "lang": "en",
  "platform": "web"
}
```

### Response

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "png_url": "https://...",
    "svg_url": "https://...",
    "mermaid_code": "..."
  }
}
```

> **Note:** Flowchart responses include `mermaid_code`; infographic, Gantt, and mind map responses include `source_code`.

### Download Images Locally

After a successful API call, the skill automatically runs the download script:

```bash
python skills/edrawmax-diagram/scripts/download_diagram.py \
  --png-url "<png_url>" \
  --svg-url "<svg_url>" \
  [--output-dir "<dir>"]
```

Output is saved to `./edrawmax_output/` by default.

---

## Supported Languages

| Code | Language |
|---|---|
| `en` | English |
| `cn` | Simplified Chinese (简体中文) |
| `tw` | Traditional Chinese (繁體中文) |
| `jp` | Japanese (日本語) |
| `kr` | Korean (한국어) |
| `es` | Spanish (Español) |
| `fr` | French (Français) |
| `de` | German (Deutsch) |
| `it` | Italian (Italiano) |
| `pt` | Portuguese (Português) |
| `ru` | Russian (Русский) |
| `id` | Indonesian (Bahasa Indonesia) |

---

## Error Handling

| Code | Message | Action |
|---|---|---|
| `400` | `prompt is required` | Provide a diagram description |
| `400` | `lang不合法` | Use a valid `lang` code from the table above |
| `2406` | Risk control rejection | Rephrase the prompt |
| `3001` | Concurrency limit | Wait briefly and retry once |
| `212200` | Generation failed | Retry once; contact support if it persists |
| `212201` | Render failed | Retry once; contact support if it persists |
| `500` | Internal server error | Report to support |

---

## Copyright

© 2026 Wondershare EdrawMax AI Team. All rights reserved.

This skill and all associated resources (source code, scripts, documentation, API references) are proprietary to Wondershare EdrawMax. Unauthorized copying, modification, distribution, or reverse engineering is strictly prohibited. Use is permitted solely within authorized EdrawMax products and services, subject to the [EdrawMax Terms of Service](https://www.edrawmax.com/terms/).

See [`skills/edrawmax-diagram/license.txt`](skills/edrawmax-diagram/license.txt) for full license terms.

---

## FAQ

**Q: Is the EdrawMax AI skill free to use?**  
A: Yes — it is currently free of charge during the promotional period.

**Q: What output formats are returned?**  
A: Each successful call returns a PNG URL, an SVG URL, and editable source code. The skill downloads both image formats locally.

**Q: What if generation fails after retry?**  
A: Contact the EdrawMax AI team at 📧 **ws-business@wondershare.cn** with details about your request.

**Q: Is my data safe?**  
A: Prompts are transmitted to EdrawMax AI servers over HTTPS. Do not include sensitive or personally identifiable information in diagram descriptions.

**Q: How do I report a bug or request a feature?**  
A: Send an email to 📧 **ws-business@wondershare.cn** describing the issue or feature request.

---

*For full API specifications, see [`skills/edrawmax-diagram/references/api-reference.md`](skills/edrawmax-diagram/references/api-reference.md).*
