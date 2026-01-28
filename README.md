# AI 新闻摘要与可视化报告生成器

一个基于AI技术的新闻摘要和可视化报告生成工具，能够自动收集、整理和呈现最新的AI领域资讯，并生成精美的HTML报告和配音脚本。

## ✨ 主要功能

### 📊 可视化HTML报告
- **精美界面设计**：采用现代化渐变背景和卡片式布局
- **响应式设计**：支持桌面和移动设备浏览
- **分类展示**：按新闻类别和重要性进行组织展示
- **时间线视图**：按日期归档的历史报告查看

### 🎙️ 专业配音脚本
- **结构化脚本**：包含视觉提示、语气指导和内容分段
- **多语言支持**：支持中文配音脚本生成
- **时间戳标记**：为视频制作提供精确的时间参考
- **专业格式**：符合广播级制作标准

### 🤖 AI智能处理
- **自动摘要生成**：从原始新闻中提取关键信息
- **智能分类**：按技术领域、公司动态、产品发布等分类
- **关键词提取**：自动识别和标记重要技术术语
- **趋势分析**：识别AI领域的发展趋势和热点

## 🚀 快速开始

### 环境要求
- Python 3.8+
- 现代浏览器（Chrome、Firefox、Safari、Edge）
- 科学上网环境（如使用代理或VPN）

### 安装和使用
```bash
# 克隆项目
git clone <repository-url>
cd news-summary

# 安装依赖
pip install -r requirements.txt

# 运行AI新闻收集
python .trae/skills/Reiner-ai-daily/extract_news.py

# 查看生成的报告
open Report/Reiner-AI-信息差-最新日期.html
```

## 📁 项目结构

```
news-summary/
├── .trae/                    # Trae IDE 配置和技能
│   └── skills/
│       └── Reiner-ai-daily/  # AI日报生成技能
│           ├── SKILL.md      # 技能说明文档
│           └── extract_news.py # 新闻提取脚本
├── Report/                   # 生成的HTML报告
│   └── Reiner-AI-信息差-YYYY-MM-DD.html
├── voiceover-script-YYYY-MM-DD.txt # 配音脚本文件
└── README.md                # 项目说明文档
```

## 🔧 技术特性

- **自动化流程**：从数据收集到报告生成全自动完成
- **模块化设计**：易于扩展新的数据源和输出格式
- **高质量输出**：专业级的视觉设计和内容组织
- **持续更新**：支持定期自动生成最新资讯报告

## 📝 输出示例

### HTML报告包含：
- 当日AI新闻头条
- 分类新闻卡片（技术突破、产品发布、市场动态等）
- 可视化数据图表
- 关键词标签云
- 时间线导航

### 配音脚本包含：
- 新闻分段和视觉提示
- 语气指导和节奏控制
- 专业播音稿格式
- 时间戳和转场标记

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目：

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢 [Trae IDE](https://trae.ai) 提供的强大开发环境
- 感谢所有开源项目的贡献者
- 特别感谢 [OpenAI](https://openai.com) 提供的 AI 技术支持

感谢所有为这个项目提供想法和贡献的开发者们！

---

**保持关注AI前沿，掌握科技动态！**