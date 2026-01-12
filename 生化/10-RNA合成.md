下面我把你这段**语音转写**里的关键信息，按“考试笔记”方式捋成一份**结构化整理版**（同时把你老师反复强调的英文术语都补齐）。我会把明显的识别错误顺手纠正：比如“2a=RNA”，“35032=3’–5’磷酸二酯键”，“500到300=5’→3’”，“三本枪击端=3’羟基端(3’-OH)”等。

---

## 0. 先导：复制 vs 转录（老师开头顺带复习）

* **DNA合成方向**：只能 **5’→3’** 延伸。
* **DNA复制需要引物（primer）**：因为DNA聚合酶必须抓住一个现成的 **3’-OH** 来加第一个核苷酸。
* **转录不需要引物**：RNA聚合酶可以让两个NTP直接形成第一个 **3’–5’磷酸二酯键**（老师强调“更简单”）。

---

## 1. RNA总分类（真核为例，老师那张表的核心意思）

### 1) 按是否编码蛋白质

* **编码RNA（coding RNA）**：主要是 **mRNA（messenger RNA）**
* **非编码RNA（noncoding RNA, ncRNA）**：很多类

  * **rRNA（ribosomal RNA）**：约占总RNA **~80%**，**最稳定**
  * **tRNA（transfer RNA）**：常见小ncRNA
  * **snRNA（small nuclear RNA）**：小核RNA（后面剪接要用）
  * **miRNA（microRNA）/ siRNA（small interfering RNA）**：基因表达调控（老师提到“诺奖相关”）
  * **lncRNA（long noncoding RNA）**：长链非编码RNA，调控为主

### 2) 稳定性印象（考试常问“谁最稳/谁最短命”）

* **mRNA**：很不稳定

  * 原核：常常只有**几分钟**
  * 真核：一般**几小时级**（老师原话“最长也是几小时”）
* **rRNA**：非常稳定、含量巨大 → 人类最早“发现RNA”常先见到它

### 3) 老师的“六边形战士”总结（RNA功能多样）

RNA可以同时扮演：

* **遗传信息携带者**（很多病毒基因组就是RNA）
* **遗传信息传递参与者**（mRNA/tRNA/rRNA是中心法则主力）
* **表达调控者**（lncRNA/miRNA/siRNA）
* **催化者**：**ribozymes（核酶）** 具催化功能
  → 这也被用作“RNA世界假说”论据（生命起源讨论：先有核酸还是先有蛋白）。

---

## 2. 转录的核心概念（老师说“先上概念，再讲体系，再讲过程，再讲加工”）

### 1) 转录是什么（transcription）

* **定义**：把DNA上某一段遗传信息**按碱基互补配对**抄到RNA上。
* **关键点**：转录的是DNA的一个**片段（segment）**，通常就是一个**基因（gene）**，不是全基因组复制。
* 所以：**转录起始（initiation）极其关键** → 也是基因表达调控的重要控制点。

### 2) transcript / transcription（别混）

* **transcription**：过程=转录
* **transcript**：产物=转录本（如 primary transcript 初级转录本）

### 3) 不对称转录（asymmetric transcription）

DNA是双链，但：

* 每次转录**只有一条链作模板**（单链模板）
* 对于“多基因DNA片段”，不同基因的模板链**不固定**，可能在不同链上。

### 4) 模板链与编码链（template vs coding）

* **template strand（模板链）**：真正被RNA聚合酶读取的那条
* **coding strand（编码链）**：与RNA序列**相同（只差T↔U）**
* 也叫：

  * **sense strand（正义链）** = coding strand
  * **antisense strand（反义链）** = template strand
* **常识提醒（老师强调）**：在 GenBank/基因序列展示里，通常给的是 **coding/sense链** 的序列。

### 5) 转录泡（transcription bubble）

* 局部解链形成“泡”
* **打开约17 bp**
* 新合成RNA与模板DNA局部形成 **~8 bp RNA–DNA杂化双链**

---

## 3. 转录反应本质（体系组成）

转录是一个聚合反应，核心元素：

* **底物**：4种 **NTP（ATP, UTP, GTP, CTP）**
* **酶**：**RNA polymerase（RNA聚合酶）**
* **模板**：DNA双链中的一条链
* **启动子**：**promoter**
* **金属离子**：作为催化辅助
* **不需要引物（primer）** ← 转录区别于复制的重要点之一
* **合成方向**：仍是 **5’→3’**

---

## 4. 原核RNA聚合酶（以大肠杆菌为例，考试重点）

### 1) 名称

* **DNA-dependent RNA polymerase**（DNA指导的RNA聚合酶）

### 2) 组成：核心酶 + σ因子

* **核心酶（core enzyme）**：**α₂ββ’ω**（5个亚基，结合紧密）
* **全酶（holoenzyme）**：核心酶 + **σ因子（sigma factor）**

  * σ与核心酶结合相对疏松
  * **只在起始阶段负责“识别并结合启动子”**
  * 进入延长后σ通常解离（老师也说“不必纠结精确脱离时点”，知道它“主要负责起始识别”即可）

### 3) 校对能力与错误率

* 原核RNA聚合酶**无proofreading（校对/纠错）**
* 错误率约 **10⁻⁴ ~ 10⁻⁵**
* 老师解释“为什么还能接受”：

  * mRNA寿命短、会降解
  * 蛋白不遗传
  * 多拷贝表达，少量错误可被系统“容忍”

### 4) 利福平（rifampin）考点穿插

* **rifampin** 抑制原核RNA聚合酶 **β亚基** → 抑制细菌转录
* 对真核核内RNA聚合酶一般**不敏感** → 可作为抗菌/抗结核药
* 老师还提到：线粒体系统“介于原核与真核之间”，因此可能解释某些副作用（点到为止）。

---

## 5. 原核启动子 promoter（考试重点中的重点）

### 1) 定义

* **promoter**：一段**特异DNA序列**，被RNA聚合酶（主要靠σ因子）**特异识别并结合**，决定**转录起始位点与强度**。

### 2) 三部分结构（按TSS计数）

* **TSS（transcription start site）**：转录起始点，标为 **+1**
* 上游用负号计数（没有“0”）
* **-10区**：**Pribnow box**（老师说“结合部位”）

  * 共识序列（consensus sequence）：**TATAAT**
* **-35区**（老师说“识别部位”）

  * 共识序列：**TTGACA**
* **共识/保守序列（consensus sequence）**：在很多不同基因启动子同位置统计出来的“相似序列”，突变会影响启动子活性与转录水平。
* 例：**lac操纵子启动子**常作为“强启动子”用于表达载体构建（老师后面还会在基因表达调控/基因工程提）。

---

## 6. 原核终止子 terminator（两型都要会）

### 1) ρ非依赖型（intrinsic / 內在终止）

终止子DNA结构特点：

* **inverted repeat（反向重复）/ palindrome（回文结构）**
* 后接一段 **AT富集**（转录成RNA后体现为U-rich）

转录后RNA表现为：

* 反向重复 → RNA内部互补形成 **hairpin（发夹/茎环结构）**
* 后面跟 **poly-U（UUU…）**
  → 促使RNA聚合酶停顿并释放RNA，转录终止。

> 老师还顺带点了“CRISPR里的P = palindromic（回文）”，说明回文结构在分子生物学里很常见。

### 2) ρ依赖型（rho-dependent）

* 需要 **ρ因子（Rho factor）**：有 **ATPase** + **helicase（解旋/解链）** 活性
* 识别RNA上的特定位点（老师提到 **rut/rat 元件** 的意思：可识别结合位点）
* 水解ATP供能 → 破坏RNA–DNA杂交区 → 把RNA“拽下来” → 终止。

---

## 7. 原核转录过程三阶段（起始-延长-终止）

### 1) 起始（initiation）

* RNA聚合酶全酶结合promoter → **closed complex（闭合复合物）**
* 局部解链形成转录泡 → **open complex（开放复合物）**
* 形成第一个磷酸二酯键（无需引物）
* **abortive initiation（流产性起始）**：常先合成≤10 nt短片段，可能反复失败
* 合成长度超过 ~10 nt → **promoter clearance（启动子清除）** → 进入延长

### 2) 延长（elongation）

* σ因子多已解离，核心酶推进
* 维持转录泡（~17 bp）与RNA–DNA杂交（~8 bp）
* RNA链 **5’→3’** 延伸

### 3) 终止（termination）

* 到terminator后按ρ依赖或非依赖方式释放：

  * RNA转录本 + RNA聚合酶 + DNA模板分开
  * 进入下一轮转录循环

---

## 8. 真核转录：了解为主，但有几块是高频概念

### 1) 真核RNA聚合酶（重点是“产物不同”）

* **RNA pol I**：主要转录 **28S、18S、5.8S rRNA**
* **RNA pol II**：主要转录 **mRNA**（还包括部分snRNA、lncRNA、miRNA等）
* **RNA pol III**：主要转录 **tRNA、5S rRNA**
* **α-amanitin（鹅膏毒素）敏感性**常用来区分：pol II通常最敏感（老师表格提到“高敏感/中度/不敏感”层次）

### 2) 真核启动子更复杂（近端+远端）

近端常见元件（都是DNA序列，属于**顺式作用元件 cis-acting elements**）：

* **TATA box（-25附近）**
* **CAAT box（~ -70）**
* **GC box（~ -40到-110区间）**
  远端调控：
* **enhancer（增强子）** / **silencer（抑制子）**：可远到 **~10³–5×10⁴ bp**
* 还会涉及 **mediator（介导子）**、**insulator（隔离子）** 的概念（老师讲“为什么不就近调控”）

### 3) cis vs trans（老师讲得很清楚，按这句话背）

* **cis-acting element（顺式作用元件）**：和被调控基因在**同一条DNA分子**上的调控序列（各种box、enhancer等）
* **trans-acting factor（反式作用因子）**：由**另一处基因编码**、产物是**蛋白质**，可扩散去结合cis元件（如 **transcription factor 转录因子**）

### 4) 真核起始需要PIC（前起始复合物）

* 不是“RNA pol II + promoter”就能起始
* 需要一堆 **general transcription factors（通用转录因子）**：如 **TFIID（含TBP）**、TFIIB、TFIIF、TFIIE、TFIIH…
* RNA pol II 的 **CTD（C-terminal domain，羧基端结构域）磷酸化**与起始/延长切换、加工耦联有关（老师点到“能调节活性”）

---

## 9. 原核 vs 真核：转录与翻译关系（考试很爱考“为什么能同时/不能同时”）

* **原核**：无核膜；mRNA无需成熟加工 → **转录与翻译可偶联（coupling）**，可见“羽毛状”现象
* **真核**：有核膜；pre-mRNA需加工、出核 → 转录与翻译有**时间+空间隔离**

> 额外提醒：老师也说“原核不是所有RNA都不加工”，**原核rRNA、tRNA仍可有加工**；只是原核**mRNA**通常不需要那套真核式加工。

---

## 10. 真核mRNA转录后加工（这里老师明确说：必须掌握）

### 1) pre-mRNA / hnRNA

* 真核mRNA初级转录本：**primary transcript**
* 又叫 **hnRNA（heterogeneous nuclear RNA，核内不均一RNA）**
* 需要加工后才变成 **mature mRNA（成熟mRNA）**

### 2) 四大加工类型（老师先总起）

* **cleavage（切割/剪切）**
* **ligation（连接）**
* **modification（修饰）**：共价改变（类比蛋白磷酸化、DNA甲基化；tRNA稀有碱基也属此类）
* **RNA editing（RNA编辑）**

### 3) 真核mRNA三大经典加工 + 编辑（老师列的“考点四件套”）

1）**5’ capping（5’端加帽）**

* 帽结构：**m⁷G cap（7-甲基鸟苷帽）**
* 连接特点：通过 **5’–5’ 三磷酸桥** 连到第一个核苷酸：**m⁷GpppN**
* 常见还有 **2’-O-甲基化**（老师提到“第一个核苷酸2’羟基也可甲基化”）
* **发生时机**：转录延长到 **~25–30 nt** 就能开始加帽（说明加工与转录可耦联）
* **功能**：

  * 保护mRNA免降解
  * 参与翻译起始（后面翻译章节会再考）

2）**3’ polyadenylation（3’端加尾）**

* **poly(A) tail（多聚A尾）**：老师写作 **poly A tail / polyadenylation**
* 基本思路：先识别信号并**切割（cleavage）**，再在3’端**添加A（terminal addition）**
* **功能**：

  * 保护mRNA
  * 参与翻译起始/效率与稳定性调控

3）**splicing（剪接）**

* 真核基因是 **split gene（断裂基因）**：**exon（外显子）** 与 **intron（内含子）** 间隔排列
* 加工时去除intron、连接exon → 成熟mRNA
* 老师顺带复习：真核mRNA一般是 **monocistronic（单顺反子）**：最终一个mRNA通常编码一条多肽链

4）**RNA editing（RNA编辑）**

* 老师在总表里点到（细节通常后面会展开）

### 4) 多顺反子 vs 单顺反子（老师说后面操纵子会再讲，但这里先记住）

* **polycistronic mRNA（多顺反子mRNA）**：原核常见；一条mRNA可编码多条多肽链（多个结构基因成簇串联）
* **monocistronic mRNA（单顺反子mRNA）**：真核常见；一个结构基因对应一条mRNA，最终翻译出一条多肽链（即使有多个外显子，也只有首外显子有起始密码子、末外显子有终止密码子）

---

# 你这段内容的“必背清单”（按老师口吻抓重点）

1. **transcription / transcript** 的区别
2. **asymmetric transcription**：单链模板 + 模板链不固定
3. **template strand vs coding strand（antisense vs sense）** + GenBank给sense链
4. **transcription bubble：17 bp打开、8 bp杂交**
5. **原核RNA聚合酶：核心酶α₂ββ’ω + σ因子；σ识别启动子**
6. **原核promoter三件套：TSS(+1)、-10 Pribnow(TATAAT)、-35(TTGACA)，共识序列突变影响强度**
7. **原核terminator两型：ρ非依赖(回文→发夹+poly-U)；ρ依赖(ATPase/helicase拉脱)**
8. **起始-流产性起始-启动子清除（>10 nt）-延长-终止**
9. **真核：pol I/II/III产物；cis元件 vs trans因子；PIC很复杂；CTD磷酸化**
10. **真核pre-mRNA=hnRNA；5’cap(m⁷GpppN)、3’poly(A)、splicing、editing；转录与加工可耦联；与翻译时空分离**

---

## 英文术语表（你老师反复点名、最该写进笔记末尾那种）

| 中文                   | 英文                                   |
| ---------------------- | -------------------------------------- |
| 转录                   | transcription                          |
| 转录本/转录产物        | transcript                             |
| 模板链                 | template strand                        |
| 编码链                 | coding strand                          |
| 正义链/反义链          | sense / antisense                      |
| 不对称转录             | asymmetric transcription               |
| 转录泡                 | transcription bubble                   |
| 启动子                 | promoter                               |
| 转录起始点             | TSS (transcription start site)         |
| 共识/保守序列          | consensus sequence                     |
| -10区 / Pribnow盒      | -10 region / Pribnow box (TATAAT)      |
| -35区                  | -35 region (TTGACA)                    |
| 终止子                 | terminator                             |
| ρ因子                  | Rho factor                             |
| ρ依赖/非依赖终止       | rho-dependent / intrinsic termination  |
| 反向重复/回文结构      | inverted repeat / palindromic sequence |
| 发夹/茎环结构          | hairpin / stem-loop                    |
| RNA聚合酶核心酶/全酶   | core enzyme / holoenzyme               |
| σ因子                  | sigma factor                           |
| 流产性起始             | abortive initiation                    |
| 启动子清除             | promoter clearance                     |
| 顺式作用元件           | cis-acting element                     |
| 反式作用因子           | trans-acting factor                    |
| 转录因子               | transcription factor                   |
| 增强子/抑制子          | enhancer / silencer                    |
| 介导子/隔离子          | mediator / insulator                   |
| 前起始复合物           | PIC (preinitiation complex)            |
| TATA结合蛋白           | TBP (TATA-binding protein)             |
| 真核RNA聚合酶I/II/III  | RNA polymerase I/II/III                |
| hnRNA（核内不均一RNA） | heterogeneous nuclear RNA (hnRNA)      |
| 5’加帽/帽结构          | 5’ capping / m⁷G cap                   |
| 5’–5’三磷酸连接        | 5’-5’ triphosphate linkage             |
| 3’加尾/多聚A尾         | polyadenylation / poly(A) tail         |
| 剪接                   | splicing                               |
| 外显子/内含子          | exon / intron                          |
| RNA编辑                | RNA editing                            |
| 多顺反子/单顺反子      | polycistronic / monocistronic          |

---

如果你接下来要把这段直接变成 **Anki 卡片**（比如“概念问答 + 英文填空cloze + 术语表”那种），我也能按你一贯的格式（中英对照、重点高亮、附词表）把它“制卡化”。你现在这段内容已经非常适合出题了：尤其是 **promoter(-10/-35)、σ因子、ρ终止、m⁷GpppN、pol I/II/III、cis/trans** 这些点，几乎都是标准考点。
