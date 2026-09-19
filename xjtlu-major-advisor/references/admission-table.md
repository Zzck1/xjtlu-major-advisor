# 专业录取要求与校区补充表

补充资料版本：`0.1.2-rc1`｜接收并提取：2026-09-19｜来源 `T01`：用户提供的《专业录取要求一览表_校区版.xlsx》。

工作表“专业录取要求”，`A1:D62`。下表忠实转写53条专业／方向记录，保留单元格定位；完整原文及空值见 [结构化资料](admission-table.json)。文件校验值：`8aa01b97b573d3218228904f079e9c7d3d22d8a0a98101b658d4d23b44f0e380`。原工作簿未随包附带。

## 使用范围

- 这是用户提供的参考表，发布单位、发布日期、适用届别及招生身份未注明，尚未核验为当届正式政策。使用时写“【待核实条件｜用户提供表 T01】”，不要直接标成已核实学校规定。
- C列表头为“第二学期专业要求课程”。学生其他学期的已选课程不能自动用来确认第二学期条件，不能直接因第一学期缺课判定不符合。先核对课程所属学期、选课或完成状态及是否可调整。
- `&` 表示本行并列列出的所有课程，不能当成任选。所有课程简称只保留原代码；本表没有其正式课程全名，不自行给MTH031等代码命名。
- B列如写按第一学期微积分或微积分与线性代数的算数平均分决定录取，只能据此提示需核对相关成绩及录取办法；没有具体分数线，不自行设60、70或其他门槛。
- B列原空白在下表记为“未注明”，不能解释为零条件。C列无指定课程不等于没有成绩、容量、作品或其他条件，尤其生物科学仍有B列成绩要求。
- 太仓意愿是学生的地点限制，不是学校资格。校区过滤方法见 [开场与初筛](intake-screening.md)。不同方向分别处理；不能把人工智能两个方向的校区或要求合并。
- 表中名称与官网名称有差异，映射仅方便检索；保留原名和来源行。必要时核对当届正式名称，不能凭相似名称转移门槛。
- 表里没有“广播电视学／Film and Television Production”这一官网索引条目，仍保留它及其未知状态，不按缺行排除。

## 逐行资料

|原行／范围|表中专业名称|第二学期要求课程|额外录取要求（原空白注明）|表中校区|专业／方向检索编号|
|---|---|---|---|---|---|
|4 / A4:D4|Civil Engineering / 土木工程|MTH031|未注明|本部|`xjtlu-civil-engineering`|
|5 / A5:D5|Bioinformatics / 生物信息学|MTH031|未注明|本部|`xjtlu-bioinformatics`|
|6 / A6:D6|Artificial Intelligence - Advanced Industrial AI Pathway / 人工智能-人工智能行业前沿方向|MTH031|未注明|太仓|`xjtlu-artificial-intelligence--aiai-xec`|
|7 / A7:D7|Data Science and Big Data Technology with Contemporary Entrepreneurialism / 数据科学与大数据技术|MTH031|未注明|太仓|`xjtlu-data-science-and-big-data-technology`|
|8 / A8:D8|Internet of Things Engineering with Contemporary Entrepreneurialism / 物联网工程|MTH031|未注明|太仓|`xjtlu-internet-of-things-engineering`|
|9 / A9:D9|Computer Science and Technology* / 计算机科学与技术*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-computer-science-and-technology`|
|10 / A10:D10|Digital Media Technology* / 数字媒体技术*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-digital-media-technology`|
|11 / A11:D11|Electrical Engineering* / 电气工程及其自动化*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-electrical-engineering`|
|12 / A12:D12|Electronic Science and Technology* / 电子科学与技术*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-electronic-science-and-technology`|
|13 / A13:D13|Information and Computing Science* / 信息与计算科学*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-information-and-computing-science`|
|14 / A14:D14|Mechatronics and Robotic Systems* / 机电电子工程*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-mechatronics-and-robotic-systems`|
|15 / A15:D15|Telecommunications Engineering* / 通信工程*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-telecommunications-engineering`|
|16 / A16:D16|Artificial Intelligence - Intelligent Systems Pathway* / 人工智能-智能系统方向*|MTH031|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-artificial-intelligence--is-sip`|
|18 / A18:D18|Industrial Design / 工业设计|MTH031 & PHY005|未注明|本部|`xjtlu-industrial-design`|
|19 / A19:D19|Intelligent Robotics Engineering with Contemporary Entrepreneurialism / 机器人工程|MTH031 & PHY005|未注明|太仓|`xjtlu-intelligent-robotics-engineering`|
|20 / A20:D20|Intelligent Manufacturing Engineering with Contemporary Entrepreneurialism / 智能制造工程|MTH031 & PHY005|未注明|太仓|`xjtlu-intelligent-manufacturing-engineering`|
|21 / A21:D21|Applied Mathematics* / 数学与应用数学*|MTH031 & PHY005|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-applied-mathematics`|
|23 / A23:D23|Biopharmaceuticals / 生物制药|PHY008|未注明|本部|`xjtlu-biopharmaceuticals`|
|25 / A25:D25|Intelligent Supply Chain with Contemporary Entrepreneurialism / 供应链管理|MTH032|未注明|太仓|`xjtlu-intelligent-supply-chain`|
|26 / A26:D26|Accounting* / 会计学*|MTH032|根据第一学期微积分的成绩决定是否录取|本部|`xjtlu-accounting`|
|27 / A27:D27|Economics and Finance* / 经济与金融*|MTH032|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-economics-and-finance`|
|28 / A28:D28|Economics* / 经济学*|MTH032|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-economics`|
|29 / A29:D29|Information Management and Information Systems* / 信息管理与信息系统*|MTH032|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-information-management-and-information-systems`|
|31 / A31:D31|Microelectronic Science and Engineering with Contemporary Entrepreneurialism / 微电子科学与工程|MTH031 & PHY007|未注明|太仓|`xjtlu-microelectronic-science-and-engineering`|
|32 / A32:D32|Applied Physics* / 应用物理学*|MTH031 & PHY007|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-applied-physics-bsc`|
|34 / A34:D34|Actuarial Science* / 精算学*|MTH031 & MTH033|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-actuarial-science`|
|35 / A35:D35|Financial Mathematics* / 金融数学*|MTH031 & MTH033|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-financial-mathematics`|
|36 / A36:D36|Biomedical Statistics* / 应用统计学*|MTH031 & MTH033|根据第一学期微积分及线性代数的算数平均分决定是否录取|本部|`xjtlu-applied-statistics`|
|38 / A38:D38|Media and Communication Studies / 传播学|本表无指定课程|未注明|本部|`xjtlu-communication-studies`|
|39 / A39:D39|English and Communication Studies / 英语（传播英语）|本表无指定课程|未注明|本部|`xjtlu-english-and-communication-studies`|
|40 / A40:D40|International Relations / 国际事务与国际关系|本表无指定课程|未注明|本部|`xjtlu-international-relations`|
|41 / A41:D41|English and Business - Finance and Economics Pathway / 英语（金融商务英语）- 金融经济方向|本表无指定课程|未注明|本部|`xjtlu-english-and-business--finance-economics`|
|42 / A42:D42|English and Business - Management Pathway / 英语（金融商务英语）- 商务管理方向|本表无指定课程|未注明|本部|`xjtlu-english-and-business--business-management`|
|43 / A43:D43|Applied Linguistics / 英语（语言学与语言应用）|本表无指定课程|未注明|本部|`xjtlu-applied-linguistics`|
|44 / A44:D44|English Studies in Global Context / 英语（全球语境下的英语研究）|本表无指定课程|未注明|本部|`xjtlu-english-studies`|
|45 / A45:D45|Translation Studies and Interpreting / 翻译|本表无指定课程|未注明|本部|`xjtlu-translation-and-interpreting`|
|46 / A46:D46|China Studies / 汉语与中国学|本表无指定课程|未注明|本部|`xjtlu-china-studies`|
|47 / A47:D47|Business Administration / 工商管理|本表无指定课程|未注明|本部|`xjtlu-business-administration`|
|48 / A48:D48|Human Resource Management and People Analytics / 人力资源管理|本表无指定课程|未注明|本部|`xjtlu-human-resource-management`|
|49 / A49:D49|International Business with a Language / 国际商务|本表无指定课程|未注明|本部|`xjtlu-international-business-with-a-language`|
|50 / A50:D50|Digital and Intelligent Marketing / 市场营销|本表无指定课程|未注明|本部|`xjtlu-marketing`|
|51 / A51:D51|Architecture / 建筑学|本表无指定课程|未注明|本部|`xjtlu-architecture`|
|52 / A52:D52|Urban Planning and Design / 城乡规划|本表无指定课程|未注明|本部|`xjtlu-urban-planning-and-design`|
|53 / A53:D53|Biomedical Sciences / 生物医学科学|本表无指定课程|未注明|本部|`xjtlu-biomedical-sciences`|
|54 / A54:D54|Materials Science and Engineering / 材料科学与工程|本表无指定课程|未注明|本部|`xjtlu-materials-science-and-engineering-2`|
|55 / A55:D55|Applied Chemistry / 应用化学|本表无指定课程|未注明|本部|`xjtlu-applied-chemistry`|
|56 / A56:D56|Environmental Science / 环境科学|本表无指定课程|未注明|本部|`xjtlu-environmental-science`|
|57 / A57:D57|Pharmaceutical Sciences / 药学|本表无指定课程|未注明|本部|`xjtlu-pharmaceutical-sciences`|
|58 / A58:D58|Psychology / 心理学|本表无指定课程|未注明|本部|`xjtlu-psychology-bsc`|
|59 / A59:D59|Digital Media Arts / 数字媒体艺术|本表无指定课程|未注明|本部|`xjtlu-digital-media-arts`|
|60 / A60:D60|Filmmaking / 影视摄影与制作|本表无指定课程|未注明|本部|`xjtlu-filmmaking`|
|61 / A61:D61|Arts, Technology and Entertainment with Contemporary Entrepreneurialism / 艺术与科技|本表无指定课程|未注明|太仓|`xjtlu-arts-technology-and-entertainment`|
|62 / A62:D62|Biological Sciences* / 生物科学*|本表无指定课程|根据第一学期微积分的成绩决定是否录取|本部|`xjtlu-biological-sciences`|

## 对资格的影响

本表只增加条件线索，不自动把任何学生转为“已确认可选”或“已确认不符合”。仍按 [资格规则](eligibility.md) 核对来源真实性、适用范围、完整必要条件和个人事实。全部判断保留所用表行及尚缺材料；学生选过、正在修读、计划选课、已通过与成绩达标分别记录。
