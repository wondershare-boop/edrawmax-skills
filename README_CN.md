# 万兴图示 AI 图表技能（EdrawMax AI Diagram Skill）

> **作者：** 万兴图示 AI 团队（EdrawMax AI Team）· **组织：** Wondershare EdrawMax（万兴图示）  
> **版本：** 2.0.0 · **许可证：** 专有软件 © 2026 Wondershare EdrawMax（万兴图示）。保留所有权利。

这是一个面向 AI Agent（如: OpenClaw, Claude Code等） 的 AI 技能（Skill），通过万兴图示 AI API，将自然语言描述一键生成专业图表。

---

## 技能简介

`edrawmax-diagram` 技能让您用日常语言描述想要的图表，立即获得渲染好的图片（PNG + SVG）以及可二次编辑的源码。支持以下四种图表类型：

| 图表类型 | 适用场景 | API 端点 |
|---|---|---|
| **流程图** | 业务流程、操作步骤、决策分支 | `/skills/generate-flowchart` |
| **信息图** | 数据可视化、统计对比、报告展示 | `/skills/generate-infographic` |
| **甘特图** | 项目计划、里程碑、进度排期 | `/skills/generate-gantt` |
| **思维导图** | 知识梳理、头脑风暴、主题拆解 | `/skills/generate-mindmap` |

### 解决什么问题

- **无需设计能力** — 用自然语言描述需求，AI 自动完成布局、样式与渲染，即使不懂绘图工具也能产出专业图表。
- **秒级本地输出** — PNG 和 SVG 文件自动下载到本地，可直接嵌入文档、PPT 或 Wiki。
- **可编辑源码** — 每次生成均返回源码（流程图为 Mermaid 格式，其他类型为专有 DSL），方便后续微调。
- **多语言支持** — 支持 12 种语言生成图表内容，覆盖中英日韩及主流欧洲语言。

---

## 快速开始

### 触发方式

在 OpenClaw 中，用自然语言描述需求，技能将自动激活：

- *"帮我生成用户注册登录的流程图"*
- *"创建一张关于机器学习知识体系的思维导图"*
- *"画一个新产品上线三个月的甘特图"*
- *"制作一张 2025 年全球 AI 市场规模的信息图"*

### API 基础地址

```
https://api.edrawmax.cn/api/ai
```

### 请求格式

```http
POST https://api.edrawmax.cn/api/ai/skills/generate-{type}
Content-Type: application/json

{
  "prompt": "用户注册登录流程",
  "lang": "cn",
  "platform": "web"
}
```

### 请求参数说明

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `prompt` | string | 是 | — | 自然语言描述 |
| `lang` | string | 否 | `"cn"` | 语言代码，见下表 |
| `platform` | string | 否 | — | 平台标识：web / win / mac / ios / android / linux |

### 返回示例

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

> **注意：** 流程图返回 `mermaid_code`，信息图、甘特图、思维导图返回 `source_code`。

### 本地下载图片

API 调用成功后，技能会自动执行下载脚本，将图片保存到本地：

```bash
python skills/edrawmax-diagram/scripts/download_diagram.py \
  --png-url "<png_url>" \
  --svg-url "<svg_url>" \
  [--output-dir "<输出目录>"]
```

默认输出目录为 `./edrawmax_output/`。

---

## 支持语言

| 代码 | 语言 |
|---|---|
| `cn` | 简体中文 |
| `tw` | 繁體中文 |
| `en` | English（英语） |
| `jp` | 日本語（日语） |
| `kr` | 한국어（韩语） |
| `es` | Español（西班牙语） |
| `fr` | Français（法语） |
| `de` | Deutsch（德语） |
| `it` | Italiano（意大利语） |
| `pt` | Português（葡萄牙语） |
| `ru` | Русский（俄语） |
| `id` | Bahasa Indonesia（印尼语） |

---

## 错误处理

| 错误码 | 说明 | 建议操作 |
|---|---|---|
| `400` | `prompt is required` | 请提供图表描述 |
| `400` | `lang不合法` | 使用上表中的合法语言代码 |
| `2406` | 风控拦截 | 修改 prompt 表述后重试 |
| `3001` | 并发限制 | 稍等片刻后重试一次 |
| `212200` | 生成失败 | 重试一次，若仍失败请联系支持 |
| `212201` | 渲染失败 | 重试一次，若仍失败请联系支持 |
| `500` | 服务器内部错误 | 联系支持团队反馈 |

---

## 版权声明

© 2026 Wondershare EdrawMax AI Team（万兴图示 AI 团队）。保留所有权利。

本技能及所有相关资源（源码、脚本、文档、API 参考资料）均为万兴科技 Wondershare EdrawMax（万兴图示）的专有财产。未经书面授权，严禁复制、修改、分发或反向工程。本技能仅限在万兴图示授权产品和服务范围内使用，须遵守[万兴图示服务条款](https://www.edrawmax.com/terms/)。

完整许可条款见 [`skills/edrawmax-diagram/license.txt`](skills/edrawmax-diagram/license.txt)。

---

## 常见问题（FAQ）

**Q：使用 EdrawMax AI 图表技能是否需要付费？**  
A：目前为限时免费，用户可免费调用全部图表生成服务。

**Q：生成的图表支持哪些输出格式？**  
A：每次调用成功均返回 PNG 链接、SVG 链接和可编辑源码，技能会自动将图片下载到本地。

**Q：生成后可以修改图表内容吗？**  
A：可以。返回的源码（流程图为 Mermaid 格式，其他类型为专有 DSL）可导入 EdrawMax 进行二次编辑。

**Q：我的数据安全吗？**  
A：Prompt 通过 HTTPS 加密传输至万兴图示 AI 服务器。请勿在图表描述中包含敏感信息或个人隐私数据。

**Q：如何反馈问题或建议新功能？**  
A：请发送邮件至 📧 **ws-business@wondershare.cn**，描述您遇到的问题或希望增加的功能，我们将尽快回复。

**Q：API 是否有调用频率限制？**  
A：当并发请求过多时，API 会返回错误码 `3001`，稍等片刻重试即可。如需大批量调用或商务合作，请联系 📧 **ws-business@wondershare.cn**。

---

*完整 API 规范请参阅 [`skills/edrawmax-diagram/references/api-reference.md`](skills/edrawmax-diagram/references/api-reference.md)。*
