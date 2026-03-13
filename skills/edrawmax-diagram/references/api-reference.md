# EdrawMax（万兴图示）AI Skills — API Reference

> **Owner:** EdrawMax AI Team（万兴图示 AI 团队）· **Organization:** Wondershare EdrawMax（万兴图示）
> © 2026 Wondershare EdrawMax（万兴图示）. All rights reserved.

## Base URL

```
https://api.edrawmax.cn/api/ai
```

- **Auth**: None required
- **Content-Type**: `application/json`
- **Note**: `user_id` is auto-extracted from `X-User-ID` request header (defaults to 0)

---

## 1. Generate Flowchart

```
POST /skills/generate-flowchart
```

Create a Mermaid flowchart from natural language.

**Request:**

```json
{
  "prompt": "用户注册登录流程",
  "lang": "cn",
  "platform": "web"
}
```

**Success Response:**

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "png_url": "https://xxx.oss.com/work/.../thumb.png",
    "svg_url": "https://xxx.oss.com/work/.../main.svg",
    "mermaid_code": "flowchart TD\n    A[开始] --> B[输入手机号]\n    B --> C{验证码是否正确?}\n    C -->|是| D[设置密码]\n    C -->|否| B\n    D --> E[注册成功]"
  }
}
```

| Response Field | Type | Description |
|---|---|---|
| png_url | string | PNG image URL on OSS |
| svg_url | string | SVG vector image URL on OSS |
| mermaid_code | string | Mermaid source code for editing/rendering |

---

## 2. Generate Infographic

```
POST /skills/generate-infographic
```

Create an infographic from natural language.

**Request:**

```json
{
  "prompt": "2025年全球AI市场规模分析",
  "lang": "cn",
  "platform": "web"
}
```

**Success Response:**

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "png_url": "https://xxx.oss.com/work/.../thumb.png",
    "svg_url": "https://xxx.oss.com/work/.../main.svg",
    "source_code": "..."
  }
}
```

| Response Field | Type | Description |
|---|---|---|
| png_url | string | PNG image URL on OSS |
| svg_url | string | SVG vector image URL on OSS |
| source_code | string | Diagram source code |

---

## 3. Generate Gantt Chart

```
POST /skills/generate-gantt
```

Create a Gantt chart from natural language.

**Request:**

```json
{
  "prompt": "新产品上线项目计划，包含需求分析、开发、测试、上线四个阶段",
  "lang": "cn",
  "platform": "web"
}
```

**Success Response:**

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "png_url": "https://xxx.oss.com/work/.../thumb.png",
    "svg_url": "https://xxx.oss.com/work/.../main.svg",
    "source_code": "..."
  }
}
```

| Response Field | Type | Description |
|---|---|---|
| png_url | string | PNG image URL on OSS |
| svg_url | string | SVG vector image URL on OSS |
| source_code | string | Diagram source code |

---

## 4. Generate Mind Map

```
POST /skills/generate-mindmap
```

Create a mind map from natural language.

**Request:**

```json
{
  "prompt": "机器学习知识体系梳理",
  "lang": "cn",
  "platform": "web"
}
```

**Success Response:**

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "png_url": "https://xxx.oss.com/work/.../thumb.png",
    "svg_url": "https://xxx.oss.com/work/.../main.svg",
    "source_code": "..."
  }
}
```

| Response Field | Type | Description |
|---|---|---|
| png_url | string | PNG image URL on OSS |
| svg_url | string | SVG vector image URL on OSS |
| source_code | string | Diagram source code |

---

## Shared Request Parameters

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| prompt | string | Yes | — | Natural language description |
| lang | string | No | "cn" | Output language |
| platform | string | No | — | Platform identifier |

### Supported Languages

| Code | Language | Code | Language |
|---|---|---|---|
| en | English | it | Italiano |
| cn | 简体中文 | tw | 繁體中文 |
| jp | 日本語 | pt | Português |
| kr | 한국어 | ru | Русский |
| es | Español | id | Bahasa Indonesia |
| fr | Français | de | Deutsch |

---

## Error Codes (All Endpoints)

| code | msg | Cause |
|---|---|---|
| 400 | bad param: prompt is required | prompt empty or malformed |
| 400 | bad param: lang不合法 | lang not in allowed enum |
| 2406 | risk control rejection | Sensitive/violating content |
| 3001 | concurrency limit | Too many concurrent requests for user |
| 212200 | 生成失败 | AI model call failed or timed out |
| 212201 | 渲染失败 | Rendering service or OSS upload failed |
| 500 | panic | Internal server error |
