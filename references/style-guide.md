# Style Guide

Nine note styles are available. Each appends a style-specific instruction to the LLM prompt.

## Style Table

| Value | Label (中文) | Description | Best Use Case |
|---|---|---|---|
| `minimal` | 精简 | Concise, key points only | Quick review, short videos |
| `detailed` | 详细 | Full content with detailed discussion | Long lectures, comprehensive study |
| `academic` | 学术 | Formal, structured for academic reports | Research talks, papers |
| `tutorial` | 教程 | Detailed steps, key conclusions | How-to videos, coding tutorials |
| `xiaohongshu` | 小红书 | Social media style with emojis and hooks | Lifestyle, product reviews |
| `life_journal` | 生活向 | Personal, emotional expression | Vlogs, personal stories |
| `task_oriented` | 任务导向 | Goals, tasks, action items | Work meetings, project updates |
| `business` | 商业风格 | Formal business report style | Business presentations |
| `meeting_minutes` | 会议纪要 | Meeting minutes format | Recorded meetings |

## Style Descriptions (as injected into prompt)

### minimal
```
1. **精简信息**: 仅记录最重要的内容，简洁明了。
```

### detailed
```
2. **详细记录**: 包含完整的内容和每个部分的详细讨论。需要尽可能多的记录视频内容，最好详细的笔记
```

### academic
```
3. **学术风格**: 适合学术报告，正式且结构化。
```

### tutorial
```
9.**教程笔记**:尽可能详细的记录教程,特别是关键点和一些重要的结论步骤
```

### xiaohongshu
The full Xiaohongshu style prompt (social media viral content style):

```
4. **小红书风格**:
### 擅长使用下面的爆款关键词：
好用到哭，大数据，教科书般，小白必看，宝藏，绝绝子神器，都给我冲,划重点，笑不活了，YYDS，秘方，我不允许，压箱底，建议收藏，停止摆烂，上天在提醒你，挑战全网，手把手，揭秘，普通女生，沉浸式，有手就能做吹爆，好用哭了，搞钱必看，狠狠搞钱，打工人，吐血整理，家人们，隐藏，高级感，治愈，破防了，万万没想到，爆款，永远可以相信被夸爆手残党必备，正确姿势

### 采用二极管标题法创作标题：
- 正面刺激法:产品或方法+只需1秒 (短期)+便可开挂（逆天效果）
- 负面刺激法:你不XXX+绝对会后悔 (天大损失) +(紧迫感)
利用人们厌恶损失和负面偏误的心理

### 写作技巧
1. 使用惊叹号、省略号等标点符号增强表达力，营造紧迫感和惊喜感。
2. **使用emoji表情符号，来增加文字的活力**
3. 采用具有挑战性和悬念的表述，引发好奇心，例如"暴涨词汇量"、"无敌了"、"拒绝焦虑"等
4. 利用正面刺激和负面刺激，诱发读者的本能需求和动物基本驱动力，如"离离原上谱"、"你不知道的项目其实很赚"等
5. 融入热点话题和实用工具，提高文章的实用性和时效性，如"2023年必知"、"chatGPT狂飙进行时"等
6. 描述具体的成果和效果，强调标题中的关键词，使其更具吸引力，例如"英语底子再差，搞清这些语法你也能拿130+"
7. 使用吸引人的标题：
```

### life_journal
```
5. **生活向**: 记录个人生活感悟，情感化表达。
```

### task_oriented
```
6. **任务导向**: 强调任务、目标，适合工作和待办事项。
```

### business
```
7. **商业风格**: 适合商业报告、会议纪要，正式且精准。
```

### meeting_minutes
```
8. **会议纪要**: 适合商业报告、会议纪要，正式且精准。
```
