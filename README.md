# 西浦选专业顾问

由学生开发的非校方专业选择辅助工具，支持专业比较与验证规划，不代表西浦教务。

规则与交付版本：**0.1.2-rc1**｜专业资料版本：**0.1.0-rc1**｜规则更新：2026-09-19。

## 快速开始

1. 按下表完成对应平台的安装或资料上传。
2. 输入 **开始选专业咨询**。
3. 回答问题，通常约需 **15–25 分钟**。

无需开发环境或 API Key，使用所选平台的账号与额度。支持文件系统 Skill 的工具可从 GitHub 下载本仓库，使用 `xjtlu-major-advisor/` 目录；其他平台请选用对应 ZIP。

| 平台 | 使用说明 | 分发包 |
| --- | --- | --- |
| WorkBuddy | [安装与启动](adapters/workbuddy/README.md) | [WorkBuddy 专用 ZIP](dist/xjtlu-major-advisor-workbuddy-0.1.2-rc1.zip) |
| TraeWork CN | [安装与启动](adapters/trae/README.md) | [TraeWork 专用 ZIP](dist/xjtlu-major-advisor-traework-0.1.2-rc1.zip) |
| ChatGPT | [入口与账号边界](adapters/chatgpt/README.md) | [插件包装 ZIP](dist/xjtlu-major-advisor-chatgpt-plugin-0.1.2-rc1.zip) |
| 豆包 | [上传与启动](adapters/doubao/README.md) | [分组资料 ZIP](dist/xjtlu-major-advisor-doubao-0.1.2-rc1.zip) |

**平台注意事项：** ZIP 不保证跨平台直接导入。ChatGPT 插件包不能通过普通聊天上传完成安装；豆包需先上传核心与索引，形成候选后再补充详细分组。四个平台均待真实客户端全流程验收，使用前请按平台记录抽查。

## 咨询流程与报告

开场只问“是否愿意去太仓？”，提供三个选项并等待回答，再逐轮了解年份、身份及经历，按候选专业核对课程和成绩。每轮只问一个主要问题，可随时回答“不知道”“跳过”“修改上一条”或“现在先出报告”。

默认交付三份独立 Word，均保留必要来源和限定条件：

1. 决策结论与适配候选
2. 你的选择画像与两个重点候选的差异
3. 就业探索、接下来的验证行动与信息边界

平台无法生成附件时，会说明限制并提供三组正文。

## 通用提示词

支持长文本指令的聊天环境可用[完整总控提示词](xjtlu-major-advisor/assets/universal-prompt.md)与[16 个场景指令](xjtlu-major-advisor/assets/prompt-commands.md)，详见[使用说明](prompts/README.md)。需搭配专业资料；提示词不提供联网或 Word 生成能力。

## 交付内容

- **核心：** [核心 SKILL.md](xjtlu-major-advisor/SKILL.md)、[通用核心 ZIP](dist/xjtlu-major-advisor-core-0.1.2-rc1.zip)、[完整源码 ZIP](dist/xjtlu-major-advisor-source-0.1.2-rc1.zip)。
- **专业资料：** [全专业索引](xjtlu-major-advisor/references/major-index.md)含 52 个官网入口及 52 份详细档案；英语四个方向分别保留，内部方向不视为独立备案专业。
- **来源与补充资料：** [来源登记](xjtlu-major-advisor/references/source-register.json)、[资料覆盖](validation/coverage.md)、含 53 条记录的[用户录取要求与校区表 T01](xjtlu-major-advisor/references/admission-table.md)，以及 8 张[职业／升学方向卡](xjtlu-major-advisor/references/career/index.md)。
- **示例：** 两套[虚构会话与完整报告](examples/README.md)，展示经历充分及信息不足时提前结束咨询两种情形。
- **验证与维护：** [验证结果](validation/results.md)、[平台能力矩阵](validation/platforms.md)、[维护与更新说明](maintenance/README.md)、[分发清单](dist/%E4%BA%A4%E4%BB%98%E6%B8%85%E5%8D%95.md)。

会话示例均为虚构资料；仓库不含个人咨询记录或报告。学校资料保留原始来源。

## 验证状态与使用边界

**已完成：** 核心规则、全目录专业档案、平台适配材料、豆包上传资料、示例及维护构建流程。

**已验证：** 公开官网正文读取、来源与课程转写、核心和兼容文件一致性、官方 Skill／插件结构，以及报告中记录的模型模拟，均不代表目标客户端实测。

**资料与结论限制：**

- 尚缺当届完整正式选择细则及 2026 届正式培养方案。T01 含部分第二学期课程、成绩录取依据及校区，但未注明发布单位、适用届别／身份，也无具体分数线，不能单独确认资格。
- 公开的 2026 年内地招生章程保留课程／成绩条件，所有真实专业默认标记为 `pending_verification`。取得适用依据前，仅提供条件性适配分析，不生成“已确认可选”的首选或排名。
