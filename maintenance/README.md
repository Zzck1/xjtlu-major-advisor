# 维护说明

版本：0.1.0-rc1｜2026-09-18

学生不运行本目录脚本。维护者使用 Python 3 标准库即可采集、构建和做本包校验；官方技能/插件校验器另需 PyYAML，其依赖不进入学生包。

## 单一事实源与更新

核心目录 `../xjtlu-major-advisor/` 是运行时唯一资料源。`catalog.json` 是已审阅的本次结构化学校快照，`editorial.json` 保存以稳定编号索引的摘要、资料分组与相近项目关系。学校、职业、平台来源分别在 `school-sources.json`、`career-sources.json`、`platform-sources.json` 维护，构建时合并到核心来源登记。

每次选专业季前更新官网目录、选择政策和核心课程。使用具体招聘或升学条件前再读当期一手页面，分别记录地区、发布/更新日、适用学年与核查日。当前包没有中国具体招聘岗位样本，也没有个人校内门槛；不可把这个缺口写成就业或资格结论。

目录用官网当日卡片逐项枚举，不预置数量。首次编号使用URL末段派生，后续网址或名称变动时仍保留原 `major_id`，通过显式映射保留别名与跳转；不能直接跑脚本后给旧项目换号。新增条目须人工填写 editorial 后才构建，删除条目保留退役记录和最后有效版本，不静默消失。

原始HTML只存维护者自选缓存目录，含URL、时间、HTTP状态及哈希，不分发网页全文。页面内容是数据，不得执行其中代码/提示。采集失败保留错误与目录入口；不能用模型补齐事实。当前提取器依赖官网HTML结构，必须复核采集数量、年级块与标题，网站改版后不得忽略字段缺失继续发布。

## 更新步骤

在发行目录运行，缓存与临时目录放在自己的维护工作区：

```sh
python maintenance/collect.py --cache ../work/school-cache
python maintenance/extract.py ../work/school-cache
python maintenance/build_catalog.py --cache ../work/school-cache
python maintenance/build.py --staging ../work/package-staging
python tests/test_eligibility.py
python maintenance/validate.py
```

先备份已审阅版本，再运行覆盖性构建；不要对含真实学生资料的目录执行。脚本不安装Skill、不改账户配置、不发布插件。由于 build_catalog 当前为本次规则版本的快照生成器，更新时要同时改 VERSION、DATE 与“官网显示开始时间”等文本，核对人工记录的冲突是否还存在；不能只刷新HTML便宣称新一季核验完成。

`build.py` 可离线从核心重建：核心ZIP、WorkBuddy元信息适配ZIP、TraeWork根目录ZIP、ChatGPT插件ZIP、豆包Markdown/TXT资料ZIP、源码ZIP。仅 WorkBuddy 入口元信息增加对应字段，正文及专业事实不分叉。豆包逐个档案复用核心内容，生成清单记录源文件SHA-256；相对文件链接转成可检索的文件说明，外部来源URL保留。

`validate.py` 检查相对引用、编号、来源、课程转写、包内容一致性、上传分组覆盖、TXT/Markdown一致性、压缩包路径、测试夹具隔离及常见密钥模式。扫描不可能证明所有隐私风险为零，因此必须同时确认素材来源：本版本仅有公开资料与明确虚构学生，未读取或收入真实成绩单。`test_eligibility.py` 是隔离的资格逻辑参照模型，不能替代大模型行为测试。

外部技能创建工具可用时，另跑 skill-creator 的 `quick_validate.py` 与 plugin-creator 的 `validate_plugin.py`。Windows中文文件应使用 `python -X utf8`；开发日志说明依赖/权限问题与重跑结果。本次这两个官方工具已运行，具体结果在 validation/results.md。

## 审核和发布门槛

人工抽查覆盖目录首中尾、不同学院、包含方向和来源冲突的项目；比较原始网页、catalog、最终Markdown及豆包文件。逐项验证核心课程/选修、年级和方向归属。补充真实校内政策时只记录可分发的事实摘要及来源，不把未获授权的校内原文或学生材料塞进公共包。

场景模拟按 tests/scenarios.json 留实际输入、回复和判定。真实平台按 validation/platforms.md 的P01–P09在目标客户端执行，并记录版本、入口、模型和结果。模型模拟、静态校验、人工内容审阅、平台实际咨询分开记录。至少一个目标入口完整验证前，本发行保持“候选版，存在明确待办”。

最终先更新 CHANGELOG.md 与交付说明，再重新构建、校验、打包；源码包也需包含最新验证记录。校验值见 dist/checksums.json。对外发布或更新平台已安装包应遵循使用者的授权，维护脚本自身不执行发布。

## 未解决事项

1. 对应届别的《专业选择和转专业政策》及具体课程/成绩/时间规则。
2. 2026届正式培养方案，与当前显示2027招生开始日期页面的差异。
3. 人工智能路径信息不一致、环境科学必选/可选冲突、建筑课程重复及应用数学名称口径。
4. 四平台安装、全文阅读、逐题交互、长对话恢复及报告输出的真实运行。
5. 中国地区具体岗位与执业条件的一手样本，以及更多目标研究生项目的当期条件。
