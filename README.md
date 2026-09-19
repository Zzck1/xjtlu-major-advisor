# 西浦选专业顾问

规则与交付版本：**0.1.2-rc1**｜专业资料版本：**0.1.0-rc1**｜规则更新2026-09-19｜**候选版，存在明确待办**。这是非校方的学生决策辅助资料，不冒充西浦教务确认。

本次新增太仓意愿开场、用户录取要求校区表和完整通用提示词，见[本次更新记录](validation/intake-update.md)。三份 Word 的本机文件及逐页检查是0.1.1-rc1的历史验收，见[三份 Word 更新验收](validation/three-word-update.md)。

## 从 GitHub 获取

本仓库保存可复用技能和分发资料，技能目录是 `xjtlu-major-advisor/`。下载后将该目录用于支持文件系统 Skill 的工具；其他平台按下面对应说明选择 ZIP。启动语为 **开始选专业咨询**。

默认报告分为三个独立 Word：

1. 决策结论与适配候选。
2. 你的选择画像与两个重点候选的差异。
3. 就业探索、接下来的验证行动与信息边界。

仓库中的会话示例均为虚构资料，个人咨询记录与个人报告不在仓库中。学校资料保留原始来源；该项目为非校方决策辅助工具。

## 通用提示词

[使用说明](prompts/README.md)、[完整总控提示词](xjtlu-major-advisor/assets/universal-prompt.md)和[16个场景指令](xjtlu-major-advisor/assets/prompt-commands.md)可用于有长文本指令能力的聊天环境。需要搭配专业资料；提示词不会自动提供联网和Word能力。

## 学生怎么开始

按你使用的平台打开说明，完成安装或上传后输入 **开始选专业咨询**。开场只问“是否愿意去太仓？”，展示三个选项并等待回答，再逐轮了解年份、身份及经历；课程和成绩按具体候选需要核对。顾问每次问一个主要问题，通常约15–25分钟，最后默认生成三份 Word：决策结论与适配候选；你的选择画像与两个重点候选的差异；就业探索、接下来的验证行动与信息边界。三份都保留必要来源和限定条件；平台不能生成附件时明确说明并提供三组正文。可以随时说“不知道”“跳过”“修改上一条”或“现在先出报告”。无需安装开发环境或配置API Key，使用自己平台的账号与额度。

|平台|使用说明|分发包|
|---|---|---|
|WorkBuddy|[安装与启动](adapters/workbuddy/README.md)|[WorkBuddy专用ZIP](dist/xjtlu-major-advisor-workbuddy-0.1.2-rc1.zip)|
|TraeWork CN|[安装与启动](adapters/trae/README.md)|[TraeWork专用ZIP](dist/xjtlu-major-advisor-traework-0.1.2-rc1.zip)|
|ChatGPT|[入口与账号边界](adapters/chatgpt/README.md)|[插件包装ZIP](dist/xjtlu-major-advisor-chatgpt-plugin-0.1.2-rc1.zip)|
|豆包|[上传与启动](adapters/doubao/README.md)|[分组资料ZIP](dist/xjtlu-major-advisor-doubao-0.1.2-rc1.zip)|

同一个ZIP不保证跨平台直接导入。ChatGPT插件包不是“随便在聊天上传就安装”；豆包先上传核心与索引，形成候选后再补详细分组。四平台当前均未完成真实客户端全程咨询验收，使用前按平台记录中的步骤抽查。

## 已交付什么

- [核心SKILL.md](xjtlu-major-advisor/SKILL.md)、[通用核心ZIP](dist/xjtlu-major-advisor-core-0.1.2-rc1.zip)与[完整源码ZIP](dist/xjtlu-major-advisor-source-0.1.2-rc1.zip)。
- [全专业索引](xjtlu-major-advisor/references/major-index.md)：52个官网入口、52份逐项详细档案；英语四方向分别保留，内部方向不冒充独立备案专业。
- [来源登记](xjtlu-major-advisor/references/source-register.json)与[资料覆盖](validation/coverage.md)，新增[用户录取要求与校区表T01](xjtlu-major-advisor/references/admission-table.md)的53条记录；8张[职业/升学方向卡](xjtlu-major-advisor/references/career/index.md)。
- 两套[虚构示例会话与完整报告](examples/README.md)，分别展示经历充分与信息不足急停。
- [验证结果](validation/results.md)、[平台能力矩阵](validation/platforms.md)、[维护与更新说明](maintenance/README.md)及[分发清单](dist/交付清单.md)。

## 状态与剩余缺口

**已完成：**核心规则、全目录逐项资料档案、平台适配材料、豆包上传资料、示例及维护构建流程。

**已验证：**公开官网正文读取，来源及课程转写检查，核心和兼容文件一致性，官方Skill/插件结构校验，以及记录在验证报告中的模型模拟。它们不等于目标客户端实测。

**尚待验证：**WorkBuddy、TraeWork CN、ChatGPT和豆包中的真实导入、全文件阅读、一问一答等待、长对话保持和附件输出。本机只读确认了TraeWork CN产品及版本，未操作原生客户端导入。

**资料仍缺：**当届完整正式选择细则和2026届正式培养方案。已新增的用户表T01包含部分第二学期课程、成绩录取依据及校区，但未注明发布单位、适用届别／身份，也没有具体分数线，不能独自确认资格。公开2026内地章程说明可以选择但保留课程/成绩条件，因此所有真实专业默认 `pending_verification`。在取得适用依据前只能输出条件性适配分析，不能生成“已确认可选”的首选或排名。外部职业卡多为美国职业结构参考，不能替代中国具体岗位或执业规则。

目录与详情当前显示2027招生开始时间；开发核查日和适用学年是两个概念。8个条目的公开表述差异或课程重复已保留，不静默拼成确定结论。具体待办及解除条件见[验证结果](validation/results.md)。
