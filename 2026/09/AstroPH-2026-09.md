## 2026-09-01

1. [Type I Solar Radio Bursts Modulated by Solar Flares](https://arxiv.org/abs/2608.29744)

    > Solar, Radio, Flare

    作者以 2023 年 12 月 24 日 AR 3529 的一次 M2.9 耀斑为例，联合 ORFEES/NRH 射电观测、SDO EUV 与磁场数据，追问耀斑如何调制持续的 Type I 噪暴。耀斑前 Type I 发射位于约 100–350 MHz；耀斑期间其强度受抑，同时出现正、反向两支 Type III，起始频率由约 220 MHz 降至 188 MHz，之后仅在较高频率恢复。磁通取消、EUV 喷流、射电源位置和 PFSS 外推共同支持一种图景：预耀斑的小尺度重联向闭合磁环补给非热电子，而耀斑时较高处的重联释放双向电子束、破坏电子俘获，因而压低 Type I 辐射。作者也强调，投影源位置与局部密度结构不足以唯一确定重联高度；把频率下降直接解释为重联上升并不自洽，仍需更多事件检验。

    <img src="./Figures/image-202609010000001.png" alt="image-202609010000001" width="680px" />

2. [DINOspec: Efficient Multimodal Alignment of Vision and Spectral Foundation Models for Astronomy](https://arxiv.org/abs/2608.30503)

    > Galaxy, Spectrum, Deep Learning

    论文提出 DINOspec：不重新训练视觉和光谱主干，而是冻结 DINOv3 图像编码器与 AION-1 光谱 tokenizer，再用轻量适配器和 CLIP 式对比损失把两种表征对齐。作者以 20,472 个 HSC–DESI 交叉匹配星系训练，并比较不同适配器初始化和分支冻结策略，以检验独立基础模型间的非对称迁移。在形态分类与光谱分类上，最佳配置分别将 F1 从 0.72 提升至 0.78、从 0.70 提升至 0.74；光谱红移预测则仍维持在约 \(R^2=0.9\)，几乎没有增益。结论是轻量跨模态对齐只会在两个模态确有互补信号时发挥作用；同时，形态评测依赖规模较小的 HSC 交叉样本，不能直接外推到任意巡天组合。

    <img src="./Figures/image-202609010000002.png" alt="image-202609010000002" width="680px" />

3. [Learning Radio Astronomical Representations with LeJEPA and Very Small Models](https://arxiv.org/abs/2608.30594)

    > Galaxy, Radio, Deep Learning

    本文检验小模型能否直接从领域内无标签无线电图像学到可迁移表征，以减少对大型自然图像基础模型迁移的依赖。作者在 RGZ20k 上比较 LeJEPA、SimCLR 与 BYOL，并在 RGZ、FIRST、MiraBest 三套无线电星系形态集上做线性探测和全量微调。约 6M 参数的 LeJEPA ViT-Tiny 在三套集上的全量微调 F1 为 0.72–0.96，普遍优于同尺寸基线，并达到或超过 22M 参数 EUPE ViT-S 的表现；图中的标注量曲线尤其显示其低标签优势。嵌入分析还表明 LeJEPA 较少放大相关无线电数据集之间的差异，但所有数据大多来自经相近 sigma-clipping 处理的 VLA 图像，尚不能证明它对不同仪器、频段或成像管线同样稳健。

    <img src="./Figures/image-202609010000003.png" alt="image-202609010000003" width="680px" />

4. [The DSA/Chronoscope fast radio burst survey: forecasts and science overview](https://arxiv.org/abs/2608.30943)

    > Fast Radio Burst, Survey, Cosmology

    这是一篇 DSA/Chronoscope FRB 巡天的参考设计与科学预报，而非实际巡天数据发布。作者从现有 CHIME/FRB、Murriyang HTRU 等巡天率出发，结合仪器灵敏度、源计数与频谱先验，估计实时后端在全视场毫秒搜索中的样本量、定位和宿主跟进能力。基线方案需搜索约 \(6\times10^6\) 个波束，预期每个搜索子带每年发现约 \(10^4\) 个 FRB，名义五年跨子带总样本可达约 \(10^5\)。以模拟 DM 和 DESI 类星系的交叉相关为例，作者展示该样本可从 CGM 到大尺度结构约束宇宙重子与反馈；不过所有产出仍依赖未完全验证的 on-sky 灵敏度、FRB 源计数、频谱、算力以及宿主红移获取率。

    <img src="./Figures/image-202609010000004.png" alt="image-202609010000004" width="680px" />

5. [Agentic research is oxymoronic](https://arxiv.org/abs/2608.31161)

    > Astronomy, LLM

    这不是性能比较或实证研究，而是一篇关于科研解释、作者责任和 AI 使用的立场短文。作者基于自身使用 agentic LLM 的经验，区分了可由工具协助且能独立验证的事务（如调试与计算）与不可直接外包的科学解释：若研究者不能理解并承担解释，就不应把机器生成的解释视为自己的研究贡献。文章将大量缺乏人类解释和责任归属的论文累积称为“deliteration”，并主张期刊要求解释工作的人类披露、公开分析数据与中间结果、设置 AI 伦理讨论，同时正视“publish or perish”对早期研究者的激励。上述论证是规范性主张而非量化因果证据；原文 HTML 与源文件均不含图表，因此不附图。

## 2026-09-02

1. [Extended radio emission in and around the merging cluster A520 as seen by MeerKAT](https://arxiv.org/abs/2609.00156)

    > Galaxy, Cluster, Radio

    MeerKAT 深度成像正在并合的 A520，追踪中心射电晕、冲击前沿及维里半径附近的低表面亮度结构。中心晕在 NE–SW 方向受两条 X 射线冲击界定，NW/SE 翼将晕系统扩展至约 2 Mpc；射电—X 射线亮度关系呈次线性，支持大尺度湍流再加速。东北约 1.2 Mpc 的射电尾与暗子团 c1/c2 共位，较高的射电/X 射线比支持气体再吸积、压缩和湍流再加速共同增强宇宙线电子。两座外周遗迹和连接暗子团的射电桥表明并合生成的非热结构延伸到维里半径外。带内谱指数、低亮度成分的系统误差及射电桥的三维几何仍需更宽频和更深 X 射线观测检验。

    <img src="./Figures/image-202609020000001.png" alt="image-202609020000001" width="680px" />

2. [Archival transients detected with the MeerLICHT telescope I: Supernovae](https://arxiv.org/abs/2609.01052)

    > Supernovae, Light Curve, Catalog

    以五年 MeerLICHT 瞬变档案和 TNS 光谱分类表为基础，研究系统建立 125 个超新星目录，并为其中 14 个具有早期多巡天覆盖的事件合并 MeerLICHT-$q$、ATLAS-$c,o$ 和 ZTF-$g,r$ 光变。时延校正后的复合光变由 $F=A(t-t_0)^2+B$ 拟合，以测量爆炸时刻和源静止系上升时间。模型为多数事件的早期上升提供稳健描述，图中的上升时间—峰值亮度平面将 Ia、IIP/L、IIn 和 Ic 事件置于不同区域，并复现 Ia 更亮事件具有更长上升时间的趋势。复合伪滤光片固定幂律指数，早期颜色演化、滤光片差异和稀疏相位覆盖会进入个体事件的系统误差。

    <img src="./Figures/image-202609020000002.png" alt="image-202609020000002" width="680px" />

## 2026-09-03

1. [Are Repeaters Prevalent Among the Known Fast Radio Burst Sources?](https://arxiv.org/abs/2609.02037)

    > Fast Radio Burst, Population, Statistics

    研究基于第二版 CHIME/FRB 目录，将观测单发源与每个重复源的首次暴和最高 fluence 暴构成可比样本，以 $\tau$ 统计和 Lynden–Bell $C^-$ 法校正能量—红移截断后重建能量函数与共动事件率。三类样本均呈折断幂律能量函数，重复源的高能端更陡，表明其暴发能量分布具有人口学差异。事件率演化中，单发样本 $B=-5.57$，两组重复源集中于 $-8.6$ 至 $-9.1$；等样本随机重采样保留了这一差异。结果支持一部分观测单发 FRB 具有独立的人口学性质，并指向多条前身通道。DM 推红移、经验完备阈值和选择函数决定绝对速率，因而结论适用于同一 CHIME 选择下的相对比较。计算工具已公开为 [Nonpara-Flask](https://github.com/xxxfei710/Nonpara-Flask)。

    <img src="./Figures/image-202609030000001.png" alt="image-202609030000001" width="680px" />

2. [Demonstrating the Time-Domain Capabilities of the 4-m International Liquid Mirror Telescope: An Early Census of Transient and Variable Detections](https://arxiv.org/abs/2609.02221)

    > Transient, Variable, Survey

    ILMT 的 PyLMT 管线以差分成像、机器学习分类和目录交叉匹配处理近 3700 张 CCD 帧，形成约 2.3 万条告警，并给出小行星、变星、活动星系核和 21 个超新星候选的早期普查。固定指向液体镜逐夜重复扫描同一条天区，ZTF 存档将关键候选的光变延伸到更长时基；多帧检测、MPC、SIMBAD 和 TNS 共同用于候选验证。样本包含获得光谱确认的 Ia 型 SN 2024cjb、未编入 VSX 的食双星与 BY Dra 候选，以及多类活动星系核和近地小行星。公开 [DART](https://ilmt-dart.shares.zrok.io/) 仪表盘提供按坐标、目录类别、主机类型和机器学习得分筛选告警的界面。固定天顶条带、有限视场和季节性覆盖构成明确选择函数，更长时间基线与完整效率建模将扩展这份首批普查的统计解释。

    <img src="./Figures/image-202609030000002.png" alt="image-202609030000002" width="680px" />

3. [High performance Stingray](https://arxiv.org/abs/2609.02857)

    > High Energy, Timing, Software

    Stingray 的性能更新面向大规模高能时序数据，把 Bartlett periodogram 和 cross spectrum 的分段计算实现为 memory-mapped 的 map–reduce 流程，并比较 multiprocessing、MPI 和 CUDA 直方图路径。该流程以事件数据段为计算单元。2–128 GB 模拟表明常用计时操作随数据规模线性或次线性增长，MPI 在小段和大段区间均展现最稳健的并行效率。XMM-Newton 对 Cyg X-1 的 CHOCBOX 实测中，完整监测的 Bartlett periodogram 速度约为对照流程的 16 倍，若干 spectral-timing 产品也获得加速。GPU 直方图在约 $10^8$ 个计数以上越过 CPU 性能交点，将 FFT 一并置入 GPU 可进一步降低数据传输占比。MPI 包装器与 GPU 路径目前处于 HENDRICS 的验证性实现阶段，能量分辨的 spectral-timing 产品需要更广泛基准；安装版本见 [stingray](https://pypi.org/project/stingray/2.2.7/)。

    <img src="./Figures/image-202609030000003.png" alt="image-202609030000003" width="680px" />

## 2026-09-04

1. [Morphology of Radio Sources in Representation Space](https://arxiv.org/abs/2609.03779)

    > Radio, Morphology, Deep Learning

    LoTSS-DR3 的 108,885 个已分辨射电源被投影到先前在 DR2 训练的 SimCLR–ResNet18 分类器集成表征空间，研究据低置信度样本的 HDBSCAN 簇和视觉核验扩展其形态分类。12 个既有类覆盖 88% 的 DR3 样本，低置信度部分新增 elongated core、FR-ambiguous、connected edge-bright、winged、complex 与 isolated lobe 六类。最近质心分类将新增簇赋给低置信度样本，图中的 UMAP 显示这些类型位于既有形态簇之间或外侧，并保留各自的罕见人口比例。结果表明预训练表征可在新巡天版本中定位未见形态，并为长尾形态构建后续标注集。新增簇的完整度与纯度受训练集中形态覆盖、源居中差异和视觉筛选限制。LoTSS-DR3 源目录已公开为 [LoTSS-DR3](https://lofar-surveys.org/dr3.html)。

    <img src="./Figures/image-202609040000001.png" alt="image-202609040000001" width="680px" />

2. [nufftcf: Fast Auto- and Cross-Correlation Function Estimation for Irregularly-Sampled Time Series via the Non-Uniform FFT](https://arxiv.org/abs/2609.03866)

    > Time Series, Statistics, Software

    nufftcf 为不规则采样序列的自相关与互相关估计提供统一 Python 接口，以 FINUFFT 的非均匀 FFT 重写 Gaussian 和 rectangle kernel 的 Wiener–Khinchin 计算，并用双指针扫描求 lag bin 的有效配对数。合成 ACF/CCF 与 pastas、pyZDCF 的比较显示，NUFFT 结果在各自统计精度内保持一致；不规则数据基准把计算复杂度由 $O(n^2)$ 降至 $O(n\log n)$。含季节缺口、异方差测量误差和相关噪声的恒星模拟光变中，算法恢复了注入的 12 d 自转周期，20 组蒙特卡洛的噪声相关时标均值与 3.5 d 注入值相符。相关峰取最大值会引入与每个 lag 噪声水平同量级的选择偏差，密集 lag 网格的误差条需要用户以 bootstrap 或蒙特卡洛另行估计。代码、基准和 notebook 已公开于 [nufftcf](https://github.com/jecampagne/nufftcf)。

    <img src="./Figures/image-202609040000002.png" alt="image-202609040000002" width="680px" />

3. [A targeted search for fast radio bursts from magnetars in elliptical galaxies](https://arxiv.org/abs/2609.04118)

    > Fast Radio Burst, Magnetar, Survey

    这项 GBT L-band 定向巡天以 GREENBURST 与 VEGAS 搜索五个邻近椭圆星系的球状星团系统，结合单脉冲检索、人工候选核验、DM 预算、PATH 宿主概率与零计数似然约束磁星 FRB 率。M49 方向发现的 FRB 20240817A 具有 $DM=983\,\mathrm{pc\,cm^{-3}}$；银河、Virgo ICM 与 M49 热晕的前景电子柱留下大量 DM 余量，背景源解释得到支持。M49 方向同一低 DM 区间的低显著度脉冲聚集保留一个待跟进的重复源候选。五个星系的合并似然给出单个活跃源基准暴发率 $R_0<0.028\,\mathrm{hr^{-1}}$，压低了球状星团磁星模型的高率区域。该约束依赖球状星团数目、主波束覆盖分数和能量函数先验，扩展马赛克与更深重复观测将提高确认能力。

    <img src="./Figures/image-202609040000003.png" alt="image-202609040000003" width="680px" />

## 2026-09-07

1. [The DESI Data Release 1 white dwarf catalogue](https://arxiv.org/abs/2609.04314)

    > White Dwarf, DESI, Catalog

    DESI DR1 对 63,968 个白矮星候选逐谱检查并进行大气模型拟合，确认 44,409 个 $p\mathrm{WD}_{\rm DESI}\geq0.5$ 的白矮星，形成目前规模最大的光谱确认目录。目录给出谱型、氢/氦/混合大气参数、径向速度及分类置信度，并区分 38,904 个具有清晰选择函数的主样本与附带观测来源。HR 图展示了常见和稀有谱型在统一 DESI 光谱中的覆盖。亮度限制、目标优先级、低信噪比分类退化和邻近源入纤维污染共同限定了人口统计时的质量剪裁。

    <img src="./Figures/image-202609070000001.png" alt="image-202609070000001" width="680px" />

2. [Improvements to Asteroseismic Fitting of White Dwarfs in the Gaia Era](https://arxiv.org/abs/2609.04323)

    > White Dwarf, Asteroseismology, Simulation

    这项受控实验以 $T_{\rm eff}=11910\,\mathrm{K}$、$M=0.720\,M_\odot$ 的合成 DAV 和三条含 1 s 噪声的脉动周期，检验质量—温度网格拟合的解简并。将模型周期插值为细网格、枚举固定 $(\ell,k)$ 模态组合并拟合各解岛的概率后，周期数据留下 28 个候选；加入 Gaia 绝对 $G$ 星等后为 11 个。真解位于该候选集合内，最低 $\chi^2$ 对应另一候选，说明最优点选择不足以表达后验结构。真实恒星的内部自由度、测光系统误差和 WDEC 对流伪影会增加复杂度。

    <img src="./Figures/image-202609070000002.png" alt="image-202609070000002" width="680px" />

3. [Identifying Casual SETI Transmissions and Ultra-Faint RFI with Cumulant Imaging](https://arxiv.org/abs/2609.04472)

    > SETI, RFI, Imaging

    研究把传统射电功率图解释为二阶累积量 $\kappa_2$，再以四阶及更高累积量成像检索调制通信的非高斯电场统计。近似高斯的自然随机辐射在高阶图中消失，宽带连续通信和微弱 RFI 因而留下可定位的调制功率信号。图示模拟在 8 s、100 kHz 内将 0.3 Jy 调制源置于 0.7 Jy 自然背景上，$\kappa_4$ 图以超过 $40\sigma$ 恢复该源。窄线或脉冲信标仍适合常规功率搜索；高阶统计量的解析噪声分布、相干天体前景和仪器非线性需要实测标定。

    <img src="./Figures/image-202609070000003.png" alt="image-202609070000003" width="680px" />

4. [Through a glass, darkly: a combined framework for estimating fast radio burst host galaxy and population properties in an era of uncertain host identification](https://arxiv.org/abs/2609.04765)

    > Fast Radio Burst, Host Galaxy, Statistics

    该框架将 zDM 的 DM—红移人口似然、PATH 的候选宿主归属和宿主星系分布合并为联合后验，保留已见与未见宿主的概率。1,000 个合成 CRACO 类事件表明，在 30 arcsec 定位误差下仍可恢复输入宿主人口，传统 PATH 的高置信度关联数为零。对 43 个 CRAFT FRB 的应用得到相对半光半径偏移尺度 $\theta_0=0.41^{+0.13}_{-0.09}$，并支持宿主偏暗；代码已公开为 [zDM](https://github.com/FRBs/zdm)。有限光学图像大小、星系目录深度和宿主先验会改变该推断。

    <img src="./Figures/image-202609070000004.png" alt="image-202609070000004" width="680px" />

5. [Exploring the connection between Fast Radio Bursts and binary neutron star mergers](https://arxiv.org/abs/2609.05209)

    > Fast Radio Burst, Binary, Simulation

     SEVN 与宇宙星系形成率生成 BNS 合并人口，MS1、APR4、H4 状态方程决定磁星残余比例；共同包层效率给出本地合并率 $3.4$–$156\,\mathrm{Gpc^{-3}\,yr^{-1}}$。研究向每个并合或磁星残余分配 CHIME 风格的 FRB 能量并施加探测选择，预测可检出非重复关联 FRB 为 $0.01$–$14.92\,\mathrm{yr^{-1}}$，相对 CHIME 的 $698\,\mathrm{yr^{-1}}$ 至多约占 2%。重复源预测把单次可见爆发视为重复源，给出乐观上界；BNS 通道构成可检验的 FRB 子人口和 FRB—引力波联合搜索目标。

## 2026-09-08

今日停更

## 2026-09-09

1. [AstroSpecLM: A Spectrum-Language Model for Evidence-Grounded Astronomical Spectral Analysis](https://arxiv.org/abs/2609.07102)

    > Spectrum, LLM, Deep Learning

    AstroSpecLM 将 DESI 一维光谱编码接入 Qwen3-4B，检验语言模型能否同时给出谱学预测和可追溯的自然语言解释。训练集由 58,558 条质量筛选光谱衍生 305,536 段事实约束对话；冻结的 SpecMAE 经投影器把谱 token 送入语言模型。目录标签和谱线测量会预先抽取为参考事实，降低回答脱离可见谱学证据的风险。独立 AstroSpecQA 上，对象分类准确率为 98.56%，恒星子类为 87.56%，红移 MAE 为 0.015。有效温度回归的 MAE 为 335.2 K，低于专用 SpecMAE 的 162.3 K，显示生成式连续参数估计仍有明确边界。评测覆盖 DESI 与四项定义明确的任务，跨仪器泛化和解释可靠性仍需外部验证。

    <img src="./Figures/image-202609090000001.png" alt="image-202609090000001" width="680px" />

2. [Mining the time axis with TRON - III. Discovery of a nulling pulsar towards the SMC with MeerKAT](https://arxiv.org/abs/2609.07528)

    > Pulsar, MeerKAT, Observation

    TRON 在小麦哲伦云方向的 MeerKAT 残差图像时间立方中捕获分钟尺度变异，后续 UHF 波束形成确认它来自消隐脉冲星 PSR J0052−7551。该源自转周期为 0.5527 s，色散量为 $29.24\,\mathrm{pc\,cm^{-3}}$。高斯混合模型给出 $31.5\pm0.6\%$ 的消隐比例，连续消隐长度服从指数分布，支持随机开关过程。其视线 DM 约为银河系预期贡献，投影在 SMC 边缘不足以确定距离归属。可见度功率谱还有 5–7 s 准周期特征，其天体或技术来源仍未确定。TRON 的逐时间样本残差成像和候选筛选将此类慢变调制转为可跟进候选，不同周期和变异幅度下的完备性仍需注入测试量化。

    <img src="./Figures/image-202609090000002.png" alt="image-202609090000002" width="680px" />

3. [The Association of Solar Radio Bursts with Eruptive and Confined Flares](https://arxiv.org/abs/2609.07999)

    > Solar, Radio, Flare

    这项统计将 2010–2016 年耀斑按是否伴随日冕物质抛射分为喷发和受限两类，并逐一判读米波动态谱中的 II、III 和 IV 型射电暴。M1.4 以上喷发耀斑的 II、III、IV 型关联率为 44%–60%，受限耀斑的 II 型和 IV 型关联率仅为 1% 和 7%。II 型多与激波相连，III 型追踪逃逸电子束，IV 型反映后耀斑磁环中的捕获电子。整体差异支持喷发耀斑具有更易形成大尺度重联与粒子逃逸通道的拓扑。同一耀斑等级阈值提升了两类比较的可比性，动态谱可见性和目录分类仍会影响绝对发生率。事件分类与 757 份动态谱已公开于 [Zenodo](https://doi.org/10.5281/zenodo.20318255)。

    <img src="./Figures/image-202609090000003.png" alt="image-202609090000003" width="680px" />

4. [A Missing Tool for Calculating Auto/Cross-correlation Function under Nonuniform Sampling Observations](https://arxiv.org/abs/2609.08604)

    > Time Series, Statistics, Method

    NUACF 与 NUCCF 为不均匀采样光变构造带时间间隔权重和错位惩罚的自相关、互相关估计，并以蒙特卡洛模拟给出各时延的置信区间。权重同时反映观测间隔和配对错位，避免把不规则序列直接重采样后再解释峰值。注入 $3.55\,\mathrm{d}$ 时延的模拟、造父变星、盾牌座 $\delta$ 型变星和 Fairall 9 检验表明，该方法可在缺口与非等间隔采样下恢复相关结构。用于 HE 0435−1223 时，NUCCF 给出显著性超过 $4\sigma$ 的宽时延边界，可作为精密透镜模型的独立交叉核验。稀疏窗口会展宽峰并降低显著性；该估计不能替代包含传递函数、透镜几何或复杂噪声的物理前向拟合。实现、示例和数据见 [Zenodo](https://doi.org/10.5281/zenodo.20809667)。

    <img src="./Figures/image-202609090000004.png" alt="image-202609090000004" width="680px" />

5. [Constraints on the Low-frequency Radio Emission of the Galactic FRB Source SGR 1935+2154](https://arxiv.org/abs/2609.08668)

    > Fast Radio Burst, Low Frequency, Observation

    Pushchino LPA 以约 110 MHz 的逐日 3.5 分钟观测重析 SGR 1935+2154 在 2020 年两个活动期的低频辐射，同时执行去色散单脉冲检索与已知自转周期折叠搜索。活动期分别覆盖 3–5 月和 9–11 月。数据没有发现显著 FRB 型爆发，折叠候选的最高信噪比低于 3.16，周期谱光度上限为 $2.08\times10^{19}\,\mathrm{erg\,s^{-1}\,Hz^{-1}}$。零检出经注入模拟转为爆发率上限，采用的对数正态光度函数给出约 $10^{1.5}\,\mathrm{d^{-1}}$。结果只约束可见的低频辐射，短日观测以外发生的爆发仍可能漏检。该约束依赖光度函数、频谱、持续时间和观测可见性；与高频活动比较时还需统一能量尺度和探测选择函数。

    <img src="./Figures/image-202609090000005.png" alt="image-202609090000005" width="680px" />

6. [A Unified Timescale Relation for Quasi-Periodic Eruptions and Repeated Nuclear Transients](https://arxiv.org/abs/2609.08737)

    > High Energy, Transient, Periodicity

    研究汇编 26 个准周期爆发、重复核瞬变和重复部分潮汐瓦解候选，测量源静止系复发时间、耀斑上升时间与黑洞质量；定量回归只使用 QPE 和 RNT。回归采用 linmix 处理双变量测量误差和人口内禀散度，rpTDE 只在图中提供现象学比较。复发时间随黑洞质量呈正向趋势，但内禀散度接近一 dex，单独子类的相关显著性较弱。更紧的经验关系为 $t_{\rm rec}\propto t_{\rm rise}^{1.00\pm0.07}$，内禀散度为 0.29 dex，从小时尺度 QPE 延伸至月、年尺度核瞬变。该关系可为后续监测给出近似复发窗口；质量关系的适用范围是合并样本，共同辐射机制仍未确定。

    <img src="./Figures/image-202609090000006.png" alt="image-202609090000006" width="680px" />

7. [Euclid: Quick Data Release (Q1) -- Exploring the detailed visual morphology of galaxies in clusters](https://arxiv.org/abs/2609.08962)

    > Galaxy, Morphology, Deep Learning

    Euclid Q1 的 Zoobot 视觉形态目录结合光度红移和恒星质量，在 $0.2\leq z\leq0.5$ 的 71 个星系团中识别出 1,754 个成员，并测量形态—局部密度和形态—团心距离关系。分类使用预测的志愿者投票分数，并按恒星质量完备性加权。1.5 $R_{500c}$ 内，平滑星系比例由最高密度的 63% 降至低密度的 36%，盘状或具特征星系相应增多；从团核到 1.5 $R_{500c}$，平滑比例也由 64% 降至 39%。约 $R_{500c}$ 外形态分离趋平，外围的场星系混入影响绝对比例。带棒星系的平均比例约为 26%，质量依赖趋势仍受有限样本和较大误差限制。Q1 只含深场区域，终版宽巡天将以更大的团样本检验这些环境关系。

    <img src="./Figures/image-202609090000007.png" alt="image-202609090000007" width="680px" />

## 2026-09-10

1. [Dispersion Measure Variability in Fast Radio Bursts from Photoionization](https://arxiv.org/abs/2609.09285)

    > Fast Radio Burst, Dispersion Measure, Theory

    年轻磁星的可变 X 射线照射超新星抛射物中的致密扫掠壳，检验光致电离能否造成重复 FRB 的长期 $DM$ 变化。壳层电离和复合的响应快于膨胀抛射物，代表性参数给出的复合时间约为 4.8 年、平衡可变色散量约 $23\,\mathrm{pc\,cm^{-3}}$。FRB 121102 的 $DM$ 在 2019 年前后达到高值后下降约 $25\,\mathrm{pc\,cm^{-3}}$，模型用随时间衰减的电离辐照再现了这一转折。持续的高活动会使下降曲线趋平并可能重新上升。射电爆发率为高能辐照提供定性代理，壳层组成和 X 射线光变决定绝对幅度。持续的多波段监测可直接检验这一时间联系。

    <img src="./Figures/image-202609100000001.png" alt="image-202609100000001" width="680px" />

2. [Time-Domain Dust Astrophysics. II. TransRAT: Time-Dependent Grain Alignment and Disruption by Cosmic Transients and Their Observational Signatures](https://arxiv.org/abs/2609.09555)

    > Dust, Polarization, Simulation

    TransRAT 将尘埃辐射转矩对齐、旋转破裂、碎片再分配和偏振辐射转移置于同一时变计算，模拟 II-P 超新星照亮均匀一域分子云。辐照上升会迅速增强对齐并产生偏振耀斑，偏振方向可经历 B-RAT、k-RAT 和 B-RAT 的切换。图示显示距源约 5 pc 的云可保留增强偏振，近云的 RAT-D 与升华则留下长期亏损；约 1 pc 的响应延迟为 20–100 天。粒径重分配还能把偏振峰值波长推向更短波段，并留下远长于瞬变本身的记忆。均匀薄云设定未包含三维结构、内部光源、遮蔽和光学深度演化，实际视线需要相应重算。

    <img src="./Figures/image-202609100000002.png" alt="image-202609100000002" width="680px" />

3. [Pulse Signal Simulation of Pulsars](https://arxiv.org/abs/2609.09655)

    > Pulsar, Simulation, Software

    这篇进行中的学位论文将单体脚本重构为模块化 `pulsar_sim`，以多高斯本征剖面、时变 $DM$、离散星际介质事件、散射、$DM$ 展宽和噪声生成兼容 PSRFITS 与 PSRCHIVE 的档案。28 个 InPTA 毫秒脉冲星的剖面参数提供输入。Band 3 的 9 个比较目标中有 7 个给出近随机残差和接近 1 的约化卡方，Band 5 的 18 个目标中有 15 个与实测剖面良好对齐。图中展示一个 Band 5 数据—模拟配对及其残差。J2145−0750 的宽度残差提示本征频率演化；闪烁未纳入模型，多高斯表示和有限频段比较仍限制结论的外推范围。更大样本和跨仪器观测将检验模拟器的稳健性。

    <img src="./Figures/image-202609100000003.png" alt="image-202609100000003" width="680px" />

4. [Time-Correlated Profile Variability in the MeerKAT Pulsar Timing Array](https://arxiv.org/abs/2609.09919)

    > Pulsar, Timing, Gaussian Process

    六年 MeerKAT 脉冲星计时阵列数据覆盖 84 个毫秒脉冲星，二维高斯过程同时拟合脉冲相位和频率方向的剖面残差。研究在 18 个源中检出时间相关变异，变异样本包含散射主导的色散结构和以频率近乎无关变化为主的对象。纳入检出选择效应后，至少约 40% 的毫秒脉冲星在 95% 可信度下具有本征剖面变异，许多幅度低于 1%。当前数据没有检出与剖面状态显著相关的自转频率导数变化；模拟显示更小的状态变化可贡献微弱非色散计时噪声。状态持续时间和现有精度限制这一关联检验，延长基线可提高灵敏度。

    <img src="./Figures/image-202609100000004.png" alt="image-202609100000004" width="680px" />

5. [The first MeerKAT S-band globular cluster pulsar survey](https://arxiv.org/abs/2609.10184)

    > Pulsar, Globular Cluster, Survey

    MeerKAT 在 2023–2024 年以约 2.4 GHz 的 S 波段观测 14 个球状星团，重检出 39 个已知脉冲星，并在高前景色散量的 Glimpse-C01 发现 4 个新毫秒脉冲星。巡天使用宽 $DM$ 搜索、候选筛选、折叠和流量测量；约两小时单历元数据给出的特征灵敏度处于数十微央量级。新源 C 的初步轨道周期约 5.03 天，D 也呈现数天量级的双星轨道，仍需延长定时以确定伴星性质与日食行为。星团内与前景的 $DM$ 差异支持宽且自适应的检索窗口。单历元灵敏度提供参考值，完备性需要针对加速度、闪烁、亮度变化和自转周期单独计算；重复观测将量化这些选择效应。

    <img src="./Figures/image-202609100000005.png" alt="image-202609100000005" width="680px" />

6. [The solar Galactocentric distance and local kinematic parameters from Gaia DR3 using Bottlinger's equations](https://arxiv.org/abs/2609.10258)

    > Milky Way, Gaia, Kinematics

    研究以约 1300 万颗 Gaia DR3 明亮巨星的空间速度为输入，利用 Bottlinger 方程的广义最小二乘解和空间分箱同时拟合银河中心距与局部运动学参数。$|z|<0.5\,\mathrm{kpc}$ 的薄盘样本给出 $R_0=8.165\pm0.024\,\mathrm{kpc}$，扩展至 $|z|<1.0\,\mathrm{kpc}$ 时得到 $8.333\pm0.022\,\mathrm{kpc}$。太阳特异运动在两个样本间较稳定，垂向截取造成的 $R_0$ 差异构成主要系统敏感性。Gaia 类模拟支持在更远距离恢复 $R_0$ 的能力，也显示轴对称拟合会受非轴对称结构和样本选择影响。图中将本工作两个结果与恒星轨道、脉泽、标准烛光和既有运动学测量并列比较。垂向选择的系统差异需要在更丰富的银河模型中继续校准。

    <img src="./Figures/image-202609100000006.png" alt="image-202609100000006" width="680px" />

## 2026-09-11

1. [More than half of recent astronomy papers are written with language-model assistance](https://arxiv.org/abs/2609.10664)

    > Astronomy, LLM, Statistics

    AstroMLab 更新语料覆盖 433,176 篇天文论文，并从 2015 至 2026 年中期的 207,111 篇首投论文提取词汇痕迹。分层负二项混合模型以作者声明的模型使用作为校准锚点，估计辅助写作比例随首投季度的变化。十二个高频标记词在 2023 至 2026 年呈现不同轨迹，模型让其超额率逐年自由变化。不同子领域的写作习惯也会影响标记词在样本间的可迁移性。主规格给出 2025 年的比例为 $54^{+8}_{-8}\%$，2026 年上半年升至 $87^{+8}_{-10}\%$。背景词汇漂移和声明样本的代表性决定主要系统不确定度，该估计覆盖留有可识别语言痕迹的辅助使用。代码和派生数据已公开于 [llm-in-astro-ph](https://github.com/seratsaad/llm-in-astro-ph)。

    <img src="./Figures/image-202609110000001.png" alt="image-202609110000001" width="680px" />

2. [The CHIME/FRB Outriggers: Commissioning the Hat Creek Outrigger and an Updated Calibration Scheme for Mitigating RFI](https://arxiv.org/abs/2609.10686)

    > Radio, Instrument, RFI

    CHIME/FRB 的 Hat Creek Outrigger 在 400--800 MHz 为 128 个双偏振馈源重建复增益并更新馈源位置。日标定把校准星本征向量经过 RFI 标记、MCMC 解缠和 Matérn 高斯过程插值，恢复时频增益。RFI 在频带中长期占据显著比例，实时掩膜和频率方向插值决定可用于相干波束形成的阵元。更新后的两偏振在约八成频带达到接近理论的热噪声表现，该流程已纳入日常运行。波束形成的 X/Y 偏振 SEFD 由 990/660 Jy 降至 530/390 Jy；14 颗脉冲星的交叉相关样本给出中位信噪比提升 67%/52%。结果归因于校准与位置的共同更新，长期增益漂移和新的 RFI 环境需要连续监测。

    <img src="./Figures/image-202609110000002.png" alt="image-202609110000002" width="680px" />

3. [Solar Flare Prediction Using a Hybrid Convolutional Neural Network and Transformer Model](https://arxiv.org/abs/2609.10772)

    > Solar Flare, Deep Learning, Prediction

    研究以 2023 年 1 月至 2024 年 9 月的 SDO/HMI SHARP 小时磁图和 GOES 标签构成活动区级样本，涵盖 442 次 C、127 次 M 和 9 次 X 耀斑。ImageNet 预训练 ResNet50 提取连续六帧图像嵌入，位置编码后的六层八头 Transformer 在活动区级十折交叉验证中预测 24、36、72 小时耀斑等级。加权损失和过采样平衡类别比例，六帧序列保留活动区磁场演化信息，四类 ROC AUC 落在 0.94--0.98。相邻磁图的时间信息在各预警窗口中持续增强类别区分，实际业务预警仍需滚动更新。24 小时窗口的加权 $F_1=0.9149$，高于单独 ResNet50 的 0.7539。X 类样本数量有限，训练期内交叉验证需要由跨太阳活动阶段和外部仪器的测试补充。

    <img src="./Figures/image-202609110000003.png" alt="image-202609110000003" width="680px" />

4. [Evidence for the binary nature of the long-period radio transient ASKAP/DART J1832-0911](https://arxiv.org/abs/2609.11068)

    > LPT, Binary, Polarization

    ASKAP 在 2023 年 12 月至 2025 年 9 月的 800--1100 MHz 监测中，于 91 个脉冲时段检出 87 个脉冲，给出 ASKAP/DART J1832-0911 的周期 $P=2656.25325\pm0.00015\,\mathrm{s}$。脉冲由约 39、65、92 s 的准周期子结构构成，位置角、去电离层 $RM$、谱指数和亮度随相位协同演化。时间排序的全脉冲图还记录了发射形态、偏振和亮度的长期重排。近同步超紧致异步极性双星模型将这些漂移与 X 射线周期联系起来，并把两个非同步周期的拍频解释为重亮窗口，预测它可能在 2027 年 7 月前后再次增亮。这一时点可由连续监测检验。现有证据支持双星图景，磁星及其他机制仍可解释部分观测；动态谱和脚本见 [J1832-0911_binary](https://github.com/CsanadHorvath/J1832-0911_binary)。

    <img src="./Figures/image-202609110000004.png" alt="image-202609110000004" width="680px" />

5. [The EDD Radio Astronomy Backend Framework](https://arxiv.org/abs/2609.11177)

    > Radio, Instrument, Software

    EDD 以开放源代码核心和插件组织射电后端，主控制器用状态机、KATCP、组播 SPEAD 数据流以及 Ansible/Docker 完成控制、部署和监测，已覆盖谱学、脉冲星、基带、VLBI、相关和波束形成模式。各模式共享统一的运行接口。框架已部署于 Effelsberg、SKAMPI、TNRT 和 ARGOS，满足真实仪器的配置、状态控制和数据传输需求。在 Effelsberg 的同步脉冲星观测中，P217mm L 波段由接收机焦点数字化的 EDD 相比 PSRIX 获得 20--110% 的信噪比增益和约 20--40% 的 ToA 误差缩减。共享法拉第室模拟输入的 C 波段对照量化了较小的后端差异，L 波段优势主要来自避开约 400 m 模拟传输链路。项目见 [EDD](https://gitlab.mpcdf.mpg.de/mpifr-bdg/edd)。

    <img src="./Figures/image-202609110000005.png" alt="image-202609110000005" width="680px" />

6. [Nonbirefringent model of orthogonal polarization modes in radio pulsars - New view on S swing and mode structure in pulsar beam](https://arxiv.org/abs/2609.11220)

    > Pulsar, Polarization, Theory

    二维几何模型让横向延展的连续发射区在每个局部元只产生 O 模，并对朝向视线的径向位置角进行 Stokes $Q/U$ 非相干叠加。空心锥模拟自然给出 RVM 形位置角摆动、$90^\circ$ 正交模跳变、O--X--O 的模式分离和单脉冲中的不同模态。多条视线切割同时呈现双峰强度、低线偏振分数和不同的中心模式占优，显示模式结构会随发射区横向形状变化。该构造使 RVM 拟合几何追踪发射区形状，因而改变了它与偶极子方位面的对应解释。模型采用理想化锥形发射区和束元，尚未直接拟合具体脉冲星的偏振数据。

    <img src="./Figures/image-202609110000006.png" alt="image-202609110000006" width="680px" />

7. [Learning JWST. I. A Foundation Model for New Population Discoveries and Morphology-Aware Photometric Redshift Measurements in the JADES Survey](https://arxiv.org/abs/2609.11879)

    > Galaxy, JWST, Deep Learning

    FM-JADES-v1 在 JADES DR5 的 482,444 个目标上进行自监督多模态训练，将 16 个 NIRCam 波段图像、测光、尺度和颜色等目录特征共同编码。掩码重建、跨模态对齐和 VICReg 约束生成的嵌入，在统一七波段高信噪比子样本中经 UMAP/HDBSCAN 分出高红移星系和红致密 LRD 等孤立岛。五个分离岛还包括亮点源与图像伪影，结果可同时支持天体候选筛选和质量控制。C01 岛包含 100 个已知光谱红移大于 7 源中的 91 个；仅用 F115W、F200W、F356W 时光度红移的 $\sigma_{\rm NMAD}=0.157$，低于模板法 EAZY 的 0.44。巡天深度、缺失波段和嵌入聚类会引入选择结构，候选人口仍需光谱跟进确认。

    <img src="./Figures/image-202609110000007.png" alt="image-202609110000007" width="680px" />

## 2026-09-14

1. [Spin-polarization of the neutron ocean in magnetar crusts](https://arxiv.org/abs/2609.12539)

    > Magnetar, Magnetic Field, Theory

    研究把自由中子的磁矩耦合与自旋极化加入磁星壳层的中子滴落条件，并以修改的 magcrust、AME20/UNEDF1 核质量表重算平衡组成。$B\gtrsim10^{17}\,\mathrm{G}$ 时，极化使滴落点中子化学势下降，外壳厚度随之缩小；在 $10^{18}\,\mathrm{G}$，相对于省略自旋极化的计算，滴落密度为 28--32%，压力为 12--17%。最深的富中子层和超重核层失去稳定区间，壳层喷发物电子丰度升至约 0.38--0.40，扩展的内壳可提供自由中子参与巨耀斑 r 过程。这一趋势跨所测试的核质量表保持稳定。计算采用冷催化平衡和理想稀薄中子气体，配对、核子相互作用与晶格能带修正仍需纳入后续模型。

    <img src="./Figures/image-202609140000001.png" alt="image-202609140000001" width="680px" />

2. [E-INSPIRE - II. Finding relics from wide-sky multi-band surveys: A proof-of-concept machine learning regression algorithm](https://arxiv.org/abs/2609.12608)

    > Galaxy, Machine Learning, Regression

    E-INSPIRE 以约 430 个具全谱拟合星族、运动学和结构参数的超致密大质量星系训练连续遗迹度 $DoR$ 回归，并在独立 INSPIRE 的 52 个星系上检验跨样本迁移。多种算法比较后，涵盖星族参数、$\alpha$ 丰度和速度弥散的多项式核 SVR 在测试集获得 $R^2=0.824$；简化的 Euclid-like 特征集仍为 0.783。年龄和金属丰度在高 $DoR$ 区趋于饱和，预测值向中间范围收缩；以 $DoR\geq0.6$ 筛选时，精确率为 0.91、召回率为 0.83。该结果可用于安排高优先级的光谱跟进。当前输入来自定义 $DoR$ 的光谱星族分析，纯测光巡天需要采用实际观测量重新训练并执行端到端验证；[INSPIRE 数据](https://archive.eso.org/scienceportal/home?data_collection=INSPIRE) 已公开。

    <img src="./Figures/image-202609140000002.png" alt="image-202609140000002" width="680px" />

## 2026-09-15

1. [Astrophysics in the Era of Artificial Intelligence powered by Large Language Models](https://arxiv.org/abs/2609.13301)

    > Astronomy, LLM

    这篇观点文章以两个明确的极端前提推演大语言模型进入天体物理后的制度变化：研究评价愈发围绕论文产出，AI 的能力范围被限定为常规稿件生成，原创洞见由人类研究者提供。推演认为，论文篇数和引文若失去区分度，例行写作、检索和代码整理可交由自动化系统，研究者会将更多时间投入问题定义、观测解释和理论创造。文章进一步设想开放且 AI 辅助的同行评议、单作者研究和培训路径调整。论证依托轶事、价值判断与反事实假设，没有给出当前 AI 使用、科研产出或就业后果的实证估计，因此适合作为研究文化的情景讨论。

2. [Decoding RR Lyrae light curves with deep learning for accurate absolute magnitude estimation](https://arxiv.org/abs/2609.14342)

    > Variable, Light Curve, Deep Learning

    Gaia DR3 的近 8 万个 RRab 和 RRc 相位折叠 $G$ 波段光变曲线用于训练两套 BiLSTM，模型直接回归绝对星等，并省去单独估计金属丰度的步骤。训练集包含 63,043 个 RRab 和 16,602 个 RRc，两个子型各自建模以保留不同的脉动形态。双向网络从相位序列的全局和局部相关性提取亮度信息。验证 RMSE 为 0.053/0.036 mag，外部球状星团以及 LMC、Sculptor 两个基准星系的聚合距离精度约为 1%。两个基准星系的距离模数同既有测量一致。相位消融显示不同子型依赖不同的光变局部形态。训练标签的光度标定、极端金属丰度覆盖和 RRab/RRc 间的偏移会传播到距离误差；输入数据见 [Gaia Archive](https://gea.esac.esa.int/archive/)。

    <img src="./Figures/image-202609150000002.png" alt="image-202609150000002" width="680px" />

3. [Hardware-aware quantum attention for fast radio burst identification](https://arxiv.org/abs/2609.15108)

    > Fast Radio Burst, Deep Learning, Classification

    该工作将 FAST 原始 PSRFITS 切分为动态谱图，用参数化量子电路替换 Vision Transformer 的 Q/K/V 投影，分词、注意力混合和分类层仍由经典硬件执行。由两颗重复 FRB、一颗 RRAT 和干扰样本构成的 6000 个标注片段中，QViT 的准确率为 94.00%、召回率为 98.30%，与紧凑的经典 ViT 相近；未参与训练的 FRB 20220912A 召回率为 97.11%。Baihua 实机在 82 个低信噪比片段给出平均 Hellinger 保真度 $0.9161\pm0.0074$。量子电路只承担投影模块，实机输出仍需经过经典层形成最终分类。这些结果覆盖标注片段和量子投影的一致性检验，连续盲搜完备度、每小时虚警率与巡天吞吐量仍待测量；[代码和处理后片段](https://github.com/euli0323/qvit-frb-code/tree/main)已公开。

    <img src="./Figures/image-202609150000003.png" alt="image-202609150000003" width="680px" />

4. [Discovery of Two Consecutive Profile Change Events in the Millisecond Pulsar PSR J0437-4715](https://arxiv.org/abs/2609.15263)

    > Pulsar, Polarization, Timing

    Murriyang 的 UWL 接收机在 704--4032 MHz 对 PSR J0437−4715 积累约七年全 Stokes 观测。研究以历元定制模板和 Matrix Template Matching 修正接收机偏振漂移，再用 PCA 与 MCMC 分解剖面残差，检出 MJD 58082 和 59670 起始的两个连续离散事件，均作用于三个相同脉冲相位区。这是毫秒脉冲星中首次报告的连续同相位事件。独立 MeerKAT L 波段残差重现了两次事件的时间形态；位置角和线偏振分数的局域变化及频率依赖支持磁层起源。两个独立阵列在主事件时刻给出一致的残差结构，增强了剖面变化的天体物理可信度。现有基线只含两次事件，重复率、触发机制和对 PTA 定时残差的定量影响仍需持续监测。

    <img src="./Figures/image-202609150000004.png" alt="image-202609150000004" width="680px" />

5. [PYRA and MYTHRA: new statistical analysis for image reconstruction](https://arxiv.org/abs/2609.15365)

    > Imaging, Interferometry, Software

    PYRA 在 MiRA 内随机扫描像素尺度、视场、正则化权重等参数，批量生成干涉成像重建；MYTHRA 用 L 曲线、$\chi^2$ 筛选、同网格重采样和逐像素离散度图选择并平均稳定解。该策略在 2024 干涉成像盲测取得总分第一，并在 VLTI/MATISSE 的 $\pi^1$ Gru 和 3 Pup 数据中恢复伴星相关的非对称结构和波长分层。统计平均压低单个参数配置带来的伪结构，并把保留解的像素间离散度转化为不确定度图。$\pi^1$ Gru 使用 1000 个重建，3 Pup 使用 3360 个重建。L 曲线窗口、$\chi^2$ 阈值、正则化和稀疏 $(u,v)$ 覆盖共同决定保留的集合，物理解释需要独立观测或建模复核；[PYRA](https://github.com/jdrevon/PYRA/tree/main) 与 [MYTHRA](https://github.com/jdrevon/MYTHRA/tree/main) 已公开。

    <img src="./Figures/image-202609150000005.png" alt="image-202609150000005" width="680px" />

## 2026-09-16

1. [Discovery of radio emission from the exoplanet β Pictoris b](https://arxiv.org/abs/2609.16720)

    > Exoplanet, Radio, Magnetic Field

    MeerKAT 在四个 L/S 波段历元观测到 $\beta$ Pictoris b 的持续射电与重复、强圆偏振爆发。研究以 Gaia/VLBI 参考源建立仿射天体测量框架并传播系统误差，点源注入、电离层和参考源删点检验共同约束定位系统误差，射电位置与行星 b 一致，宿主星以 4.4$\sigma$ 被排除。高频爆发延伸至 3.5 GHz，强圆偏振和快速时变支持电子回旋脉泽辐射，并给出局域磁场 $B\gtrsim1.25\,\mathrm{kG}$，构成首个系外行星磁场直接测量。爆发间隔与自转调制相容，磁层--电离层耦合可解释观测功率。磁场量限定义为发射区下限，静息射电成分和等离子体来源仍需长期监测。

    <img src="./Figures/image-202609160000001.png" alt="image-202609160000001" width="680px" />

2. [A fast radio burst from a non-targeted low-frequency survey](https://arxiv.org/abs/2609.17275)

    > Fast Radio Burst, Low Frequency, Survey

    MWA SMART 宽视场电压巡天通过 BLINK 动态成像和 STRIDE 像素级去色散，在 150 MHz 附近首次非定向发现 FRB 20191203A。动态谱和 DM--时间图显示冷等离子体色散的预期弓形结构。处理将电压数据保持毫秒级时间与 kHz 级频率分辨率，候选在不同成像参数、重新相位和独立波束形成流程中均被复现。该爆发的 $DM=393\,\mathrm{pc\,cm^{-3}}$，散射尾为 $90\pm20$ ms，显示强传播展宽仍可在低频恢复。一个事件在有效曝光下给出 $54\,\mathrm{sky^{-1}\,day^{-1}}$ 的速率估计，与高频样本相容。角分级定位无法关联宿主，单事件泊松区间和未完成巡天处理限制了种群结论；[BLINK/STRIDE 代码](https://github.com/PaCER-BLINK-Project)已公开。

    <img src="./Figures/image-202609160000002.png" alt="image-202609160000002" width="680px" />

## 2026-09-17

1. [Rethinking Domain Specialization for Open-Ended Scientific Reasoning in Astronomy Language Models](https://arxiv.org/abs/2609.17644)

    > Astronomy, LLM

    研究从 2017--2026 年公开天文奥赛材料构建 300 道自由作答题，其中 204 道纯文本、96 道关联图像；固定 GPT-5 裁判与 BLEU、ROUGE-L、BERTScore 和句向量指标共同评估通用、多模态及天文专用模型。GPT-5.5 在全样本和共同纯文本集的裁判分数为 0.6700 和 0.7083，Gemma 4 31B 为 0.3933 和 0.4314，AstroSage 70B 在共同纯文本集为 0.3333。图像关联题使 GPT-5.5 由 0.708 降至 0.589；二次裁判和各参考指标也会改变接近模型的比较。ROUGE-L 和余弦相似度与裁判分数仅有中等相关，BERTScore、BLEU 的相关方向相反，单一自动指标不足以代表科学正确性。专用模型的基座规模、训练数据和部署条件不同，公开题目的训练集暴露无法排除；[基准流程代码](https://github.com/vanessalama09/astrobench)已公开，结构化数据集待许可审查后发布。

    <img src="./Figures/image-202609170000001.png" alt="image-202609170000001" width="680px" />

2. [FRB 20250607A: Weirder Than Fiction](https://arxiv.org/abs/2609.18086)

    > Fast Radio Burst, Polarization, Scattering

    ASKAP 的 CRAFT/CRACO 在 919.5 MHz 发现双成分 FRB 20250607A，并以 0.016688 ms、0.120 MHz 的全 Stokes 动态谱分别测量两段辐射。整体结构最大化给出 $DM=335.87^{+0.34}_{-0.26}\,\mathrm{pc\,cm^{-3}}$；分量 DM 在正式不确定度内同整体值一致。第二成分的散射时间为 $1.25\pm0.02$ ms，闪烁去相关带宽为 $0.7113\pm0.031$ MHz，$m_g=0.3014$，两屏幕模型将主散射屏限制在源侧约 61 kpc 内。时间分辨 RM、圆偏振及散射尾中持续的位置角摆动共同支持近源复杂磁化等离子体。Burn 定律拟合还给出 $\sigma_{\rm RM}=3.56\pm0.03\,\mathrm{rad\,m^{-2}}$；逐时段去旋后仍出现约 $+30^\circ$ 的尾部摆动。广义法拉第旋转的拟合在两个分量中均未获统计支持。有限频带仍限制闪烁标度测量，现有数据未确证分量间 DM 差；[FIRES](https://github.com/JoelBalzan/FIRES) 和 [FRBop](https://github.com/JoelBalzan/FRBop) 已公开。

    <img src="./Figures/image-202609170000002.png" alt="image-202609170000002" width="680px" />

3. [Transitioning from ADS to SciX to Serve 21st Century Astronomy](https://arxiv.org/abs/2609.18091)

    > Astronomy, Digital Library

    本文说明 NASA ADS 将在 2026 年 11 月 16 日完成向 Science Explorer（SciX）的扩展。天文学用户以现有 ADS 凭据登录后，设置、文献库、提醒和旧链接将继续可用，底层 API 与数据库保持兼容，astropy 和 ads Python 包可继续访问。SciX 在天体物理界面提供学科偏好的混合相关性排序，同时检索跨天体物理、行星科学、日球物理和地球科学的资源；2026 年 8 月中旬索引超过 3650 万篇条目和 4 亿条引文。数据、软件、资助、提案关联及 UAT 关键词扩展了检索线索。实时库持续增长，案例查询的当前结果会随之变化；[三个 Zenodo 案例](https://doi.org/10.5281/zenodo.22055128)保存了可复现实例和当时的结果集。

    <img src="./Figures/image-202609170000003.png" alt="image-202609170000003" width="680px" />

4. [Toward Autonomous Radio Follow-up of Multi-messenger Transients with RADAR: From Alert Parsing to Inference and Observation Scheduling](https://arxiv.org/abs/2609.18233)

    > Transient, LLM, Software

    RADAR 将引力波告警后的 GCN 通报解析、保留站点数据所有权的射电余辉 MCMC 推断和 VLA 排程草案连成一条链路。针对 GW170817 的 96 条人工标注射电记录，GPT-5.5 的事件级 $F_1=0.893\pm0.010$、GCN 级召回率为 $0.794\pm0.013$；多事件通报的漏枚举构成主要误差。服务器线程池与站点子进程池把 16 核联邦采样率从约 3.2 提至约 120 samples s$^{-1}$，接近本地 parallel emcee 的 123。SAGE 生成的六个保留 VLA 排程有四个通过 21/21 项 SCORE，两个因总时长超限得 20/21；OPT 检查还能发现 LOOP-START 的隐含时长。FIESTA 单次计算约快五倍。Python GIL 限制其当前子进程扩展效率，afterglowpy 的效率更高。GW170817 公开资料的训练集暴露无法排除，设施提交仍保留人工关口；[RADAR-II 代码](https://github.com/diaspora-project/radar-ii)已公开。

    <img src="./Figures/image-202609170000004.png" alt="image-202609170000004" width="680px" />

5. [cosmokdtree: a flexible OpenMP-parallelized k-d tree for computational astrophysics applications](https://arxiv.org/abs/2609.18316)

    > Astronomy, Software

    cosmokdtree 以 Fortran 和 OpenMP 实现可配置维数、精度、周期边界与 $N_{\rm leaf}=16$ 默认叶节点的 k-d tree，并提供 F2PY Python 接口。作者在均匀和非均匀分布、最高约 $10^9$ 点的测试中比较 scipy、coretran 和 torch_kdtree：16 核构树相对所测 CPU 实现快约 10--20 倍，在重叠规模内比消费级 GPU 版本慢约两倍；$k=10$--1000 的 kNN 和多数球查询也给出最低耗时。FoF 演示在 $N>10^6$ 保持 $\mathcal{O}(N\log N)$ 标度，80,000 粒子的自适应 SPH 网格化由暴力法 428.61 s 降至 0.86 s。构建时间随维数增加在测试范围内近似 $\mathcal{O}(\log D)$，批量查询的并行扩展优于单个大规模检索。双精度树约占 scipy 两倍内存，9 维 kNN 受维数灾难显著变慢，数据中心 GPU 仍未纳入比较；[代码和测试](https://github.com/oscarmonllor99/cosmokdtree)已公开。

    <img src="./Figures/image-202609170000005.png" alt="image-202609170000005" width="680px" />

## 2026-09-18

1. [Gravitas: A Browser-Based Astrophysics Laboratory for Prediction, Measurement, and Discovery](https://arxiv.org/abs/2609.19327)

    > Astronomy, Simulation, Software

    Gravitas v1.0.0 将可配置的二维牛顿引力沙盒、59 个情景和 22 项引导式探究置于浏览器中，让学生以预测—测试—测量—修正—解释的循环操作轨道、系外行星、星系旋转与引力波模型。凌星、视向速度和天体测量面板由同一演化状态与观测几何生成，A/B 实验、可复现链接、CSV 和报告导出保留证据链。公开验证面板列出 243 项通过的科学检查，覆盖轨道、守恒、观测量与近似模型。引导活动还能将数值积分可靠性、观测选择效应和模型近似纳入学生可检验的测量任务。核心动力学采用二维牛顿点质量及软化近遇；课堂学习增益需要独立教学研究检验，[Gravitas](https://gravitas-sim.online) 可直接使用。

    <img src="./Figures/image-202609180000001.png" alt="image-202609180000001" width="680px" />

2. [Kinematics of the System of Young Open Clusters based on Gaia DR3 Data](https://arxiv.org/abs/2609.19732)

    > Cluster, Gaia, Kinematics

    研究用 Gaia DR3 的 Hunt--Reffert 目录中 2,384 个年龄不超过 100 Myr 的疏散星团追踪年轻银盘速度场，并以极大似然和仿射不变 MCMC 同时拟合圆周转动、四臂密度波与速度弥散。太阳半径处线速度为 $242.35\pm1.05\,\mathrm{km\,s^{-1}}$，转动曲线在约 7.5--8 kpc 后缓慢下降；运动学旋臂俯仰角为 $-11.69\pm0.33^\circ$。拟合包含径向与切向两类旋臂扰动，二者均约 $-3\,\mathrm{km\,s^{-1}}$，不同似然形式与二维、三维检验给出相近的主参数。结果与银河系脉泽测量总体一致。年轻星团的平均视向速度误差接近速度弥散，分析固定 Gaia 距离标尺和太阳银心距离，未对这两项作独立再标定。

    <img src="./Figures/image-202609180000002.png" alt="image-202609180000002" width="680px" />

3. [Gaia method paper: an algorithm to detect flare events in Gaia time-series](https://arxiv.org/abs/2609.20417)

    > Stellar, Flare, Gaia

    Gaia DR3 的 flaring_stars 流程在 $G$、$G_{\rm BP}$、$G_{\rm RP}$ 同时增亮和变蓝时确认耀斑，并以逐历元修正超额因子剔除跨波段不一致的仪器或标定异常。它在 474,026 颗旋转调制变星中检出 3,217 次耀斑，来自 2,818 颗恒星；电子版星表保存宿主和事件参数。整体检出率约 0.6%，在约 3,000 K 处升至 1.8%，检出灵敏度在 $9.5\lesssim G\lesssim14.1$ 近似均匀。流程以谐波模型或裁剪均值估计静止态，避免把旋转调制误作为耀斑；完整度筛选后的振幅相关性明显减弱。Gaia 的稀疏单历元采样使振幅和能量成为下限，温度只适用于通过严格多波段一致性筛选的子样本。

    <img src="./Figures/image-202609180000003.png" alt="image-202609180000003" width="680px" />

4. [Offline vs Real-Time Validation and Performance Assessment of Heimdall Detection Pipeline for Fast Radio Bursts](https://arxiv.org/abs/2609.20635)

    > Fast Radio Burst, Detection, Software

    研究以 Northern Cross 北南臂 16 个圆柱的滤波器组数据，比较 Heimdall 从 SIGPROC 文件读取与通过 PSRDADA 共享内存环形缓冲实时读取的单脉冲搜索。11 组注入 FRB 文件和 11 组真实 FRB 文件给出到达时刻、色散量约 3% 内的一致性，信噪比约 10% 内一致。调节 gulp、缓冲块和块数后，代表性真实文件的 PSRDADA 加速最高达 2.33 倍，测试配置可满足实时约束。实时模式以异步生产者—消费者结构在内存中传递数据，当前测试中 GPU 去色散成为主导耗时。当前生产端由 CPU 写入器模拟，Heimdall 仍为单波束单 GPU；完整波束形成器与多波束实测决定部署性能。

    <img src="./Figures/image-202609180000004.png" alt="image-202609180000004" width="680px" />

## 2026-09-21

1. [Flux Density Calibration of Radio Bursts Detected in the Sidelobes of the Canadian Hydrogen Intensity Mapping Experiment](https://arxiv.org/abs/2609.21074)

    > Radio, CHIME, Method

    CHIME/FRB 为旁瓣中发现的 FRB、脉冲星和长周期瞬变建立强度与基带两套流量密度标定：全息主波束、FFT 形成波束、通道掩蔽和频率拼接共同约束强度谱，基带则直接朝源形成波束。九个蟹状星云脉冲的基带/强度流量比中位数为 0.998，分数 RMSE 为 0.106；稳态源检验显示整体校准与源流量表相容。合并不确定度随时角和数据产品从 20% 升至 42%，使明亮旁瓣瞬变可以进入定量流量比较。该流程也使旁瓣发现的稀有明亮事件能与主波束样本置于同一流量尺度。全息轨迹仍只覆盖有限亮源，远旁瓣和未采样赤纬的系统误差决定可用范围。

    <img src="./Figures/image-202609210000001.png" alt="image-202609210000001" width="680px" />

2. [A mechanism for fast radio bursts and their narrow spectra](https://arxiv.org/abs/2609.21076)

    > Fast Radio Burst, Magnetar, Theory

    研究提出磁星爆发电磁脉冲在外磁层穿过环境 kHz 快模波时，$F\rightarrow F+A$ 受激散射会以 $\Gamma^2$ 把频率推至 GHz，并指数放大初始 GHz 种子。非饱和数值解给出 $\nu_{\rm peak}\simeq0.79\Gamma^2\nu_0$、$\Delta\nu/\nu\simeq0.18$ 的窄谱。饱和阶段的波泵耗尽形成低频截止与时频下漂，最强微秒成分可达爆发功率约 1%。这一途径把持续时间和辐射能量同脉冲本身的宽度和能量联系起来，也为窄带爆发提供可计算的时频预测，并可联系微结构观测。结论依赖爆发脉冲的快速上升和活跃磁星外磁层已存在 kHz 湍波，外部传播及真实脉冲结构会改变可观测谱形。

    <img src="./Figures/image-202609210000002.png" alt="image-202609210000002" width="680px" />

3. [CRAFT HTR2: Polarimetry of 64 non-repeating fast radio bursts from the updated CRAFT catalogue](https://arxiv.org/abs/2609.21177)

    > Fast Radio Burst, Polarization, Catalog

    ASKAP/CRAFT HTR2 将高时间分辨全 Stokes 数据扩展为 64 个表观非重复 FRB 的样本，以结构最大化 DM、RM 合成和生存分析比较 ASKAP、CHIME 与 DSA。ASKAP 和 CHIME 的 $|RM_{\rm EG}|$ 中位数为 119.8 与 $54.1\,\mathrm{rad\,m^{-2}}$，文章给出 CHIME 分布更低的统计证据。三组线偏振分数相容；新增基带事件中出现更宽、更暗且未检出偏振的一群源。这为不同频段的传播环境比较提供共同观测基础，更大样本可辨析不同选择效应。联合 RM、偏振与宿主信息可进一步分离源内和星际传播贡献，并获得更稳健结果。多数新增源缺少宿主光谱红移，宽度、光度与偏振的关系仍处于候选阶段。

    <img src="./Figures/image-202609210000003.png" alt="image-202609210000003" width="680px" />

4. [From Observation to Ground Truth: Reconstruction Losses of Galaxy Imaging Under Heteroscedastic Noise](https://arxiv.org/abs/2609.21350)

    > Galaxy, Imaging, Deep Learning

    研究以 IllustrisTNG50 的 1,153 个子晕生成 8,071 幅 SKIRT 无噪声真值图及带空间变噪声的观测，在相同 VAE 架构内比较 MSE、MAE 与逐像素逆方差 $\chi^2$ 重建损失。$\chi^2$ 训练在大部分 SNR 区间给出最低中位相对误差，半光半径的中位相对误差为 0.14%，并较好保留微弱结构。这一设计把损失函数与观测方差直接对应，避免高噪声像素主导学习。DESI 三波段示例的残差也更符合输入的不确定度模型；[代码与基准材料](https://github.com/Rh-YE/obs2gt) 已公开。模拟采用固定 PSF、特定噪声模型和 VAE 设定，真实 DESI 图像缺少无噪声真值，定量恢复精度需要独立标定。

    <img src="./Figures/image-202609210000004.png" alt="image-202609210000004" width="680px" />

5. [LenNet: Direct Detection and Localization of Strong Gravitational Lenses in Wide-Field Sky Survey Images](https://arxiv.org/abs/2609.21661)

    > Gravitational Lensing, Object Detection, Deep Learning

    LenNet 直接在 KiDS 原始巡天图上检测并定位星系—星系强透镜，训练数据由 9,147 个注入实测背景的模拟透镜构成，规避了逐候选裁图产生的大规模检索负担。模拟测试的 $F_1=97.11\%$；以有限 KiDS 候选进行迁移学习后，真实图像测试的 $F_1$ 为 89.47%。检测框保留透镜周边环境，并能与常见 YOLO 基线比较精确率—召回率曲线。全图处理还便于在同一输入中学习透镜弧与周边星系的相对位置。迁移样本多为形态候选且缺少光谱确认，模拟到真实的域差异限制巡天完备度与纯度的物理解释。

    <img src="./Figures/image-202609210000005.png" alt="image-202609210000005" width="680px" />

6. [Morphology classification for galaxies in the Kilo Degree Survey using a label-efficient self-supervised learning framework](https://arxiv.org/abs/2609.21705)

    > Galaxy, Classification, Deep Learning

    该框架对 KiDS DR5 的 305,583 幅无标签星系彩色图做 SimCLR 对比预训练，再用 5,000 个人工标注样本训练冻结的 ResNet-50 分类头，区分椭圆、旋涡、透镜盘、非规则和其他五类。测试平均准确率为 $90.5\pm0.2\%$，全样本分类后的 Sérsic 指数—有效半径分布同标注样本的总体形态相符。预训练表征还降低了每次扩展标注集时的人工筛选压力。结果形成亮星系的形态目录，可用于选择不同结构族群开展后续统计。人工标签的主观边界、固定中心裁剪和 KiDS 的波段与 PSF 限制跨巡天直接使用，目标巡天需要重新预训练和适配。

    <img src="./Figures/image-202609210000006.png" alt="image-202609210000006" width="680px" />

7. [Euclid: Quick Data Release (Q1) -- Optical hotspots in powerful radio galaxies](https://arxiv.org/abs/2609.21930)

    > Galaxy, Radio, Multi Wavelength

    研究将 Euclid Q1 北深场的光学/近红外图与 LOFAR、VLASS 射电结构匹配，在确认的 FRII 射电星系中筛选终端热点对应体。半角秒 LOFAR 覆盖内只有 $2/29$ 候选与紧致热点位置一致，推得可信检出比例约为 7--15%，低分辨图像中的偶然重合占据重要部分。两例最清晰源的射电至光学 SED 与近等分配磁场下电子加速至约 1 TeV 相容，其中一例为已知最高红移光学热点。这一筛选链为全宽域 Euclid 与国际基线 LOFAR 的统计研究提供直接模板。当前高分辨覆盖有限，单区 SED 模型无法解析热点内部结构，磁场和粒子谱的简并仍需更宽样本检验。

    <img src="./Figures/image-202609210000007.png" alt="image-202609210000007" width="680px" />

## 2026-09-22

1. [Chromospheric sensitivity of stellar spectral lines: an unsupervised machine learning classification](https://arxiv.org/abs/2609.22532)

    > Stellar, Spectrum, Machine Learning

    研究以 NLTE G2 色球模型生成的 6,403 条可见光原子谱线为样本，保留每条线随加热增强的九维响应轨迹，再以 PCA 和 DBSCAN 聚类。活动敏感线约占样本的 11%，稳定核可作为对活动较不敏感的测量候选，敏感群则适合作为色球诊断。低能级能量在两类之间呈统计偏移，分布重叠使它不能独立决定单条线的类别。光谱敏感性图还显示平均变化近零的谱线可具有阈值或补偿式非线性响应。阈值仍处于完善阶段，合成谱没有仪器展宽、旋转和混合线，真实高分辨观测需要完成外部校准。

    <img src="./Figures/image-202609220000001.png" alt="image-202609220000001" width="680px" />

2. [A dynamic magneto-ionic environment around a long-period radio transient](https://arxiv.org/abs/2609.23259)

    > LPT, Polarization, Rotation Measure

    FAST 的四个全 Stokes 历元追踪到长周期射电瞬变 CHIME J0630+25 的偏振演化，每个历元均检出脉冲，表明活动已持续数月；该源自转周期为 421 s。其旋转量度从约 $-400$ 变至 $-1630\,\mathrm{rad\,m^{-2}}$；一次观测内的变化约为 $536\,\mathrm{rad\,m^{-2}}$，持续约 2500 s。低 DM 视线上的银河前景远不足以产生这一振幅和速度，结果要求源附近存在致密、磁化且快速演化的法拉第旋转区。与双星脉冲星的比较使伴星或局域等离子体成为可检验的解释。一个复杂偏振条纹也可由本征位置角摆动和模式转换形成，轨道周期与局域介质结构需要高采样率全 Stokes 持续监测。

    <img src="./Figures/image-202609220000002.png" alt="image-202609220000002" width="680px" />

3. [XMST II: The spatial and kinematic structure of Galactic OB associations in Gaia DR3](https://arxiv.org/abs/2609.23515)

    > Stellar, Kinematics, Clustering

    XMST 将三维空间连接、横向速度和消光分成连续的层级检验，使不同单位与不确定度的观测量各自承担物理角色。作者在 1,000 个蒙特卡洛实现中比较两种细化顺序，先用运动学再用消光时平均 Jaccard 相似度为 0.8354，刻意重叠的族群有 98.6% 被分开。该流程保留第一阶段的空间度量，同时要求新增子群重建后仍具空间连贯性。Gaia DR3 的 OB 星协应用也显示完整细化能提高与既有成员划分的一致性。单一全局断裂尺度、只含横向速度和输入覆盖要求限定了适用范围，星协的共同年龄与起源仍需独立证据确认；[XMST-Paper-II 代码](https://github.com/mjgallawayastro-stack/XMST-Paper-II)已公开。

4. [A Sample of 459 Galaxy Groups Identified from the FAST All Sky HI Survey DR2](https://arxiv.org/abs/2609.24060)

    > Galaxy, HI, Catalog

    作者直接从 FASHI DR2 的 H I 信号寻找群系，利用密度对比和至少五个 H I 成员的门槛得到 459 个星系群、共 3,015 个 H I 源。群系红移分布在 $z\sim0.02$ 附近达到峰值，光学光谱对应体提供成员总恒星质量作为群质量代理。总 H I 质量随总恒星质量显著增加，H I 与恒星质量之比则显著下降，说明更富集的群保有更大气体库，同时相对气体含量逐步耗减。该盲选样本可用于本地宇宙的环境演化和大尺度结构研究。它优先选择 H I 富集且高丰度的系统，光学覆盖与光谱深度也会传入恒星质量关系的完整度。

    <img src="./Figures/image-202609220000004.png" alt="image-202609220000004" width="680px" />

5. [Constraints on Axion-like Dark Matter from Cosmic Birefringence with a Polarization Array of Repeating Fast Radio Bursts](https://arxiv.org/abs/2609.24085)

    > Fast Radio Burst, Dark Matter, Polarization

    研究以三颗高活跃重复 FRB 的 FAST 偏振位置角数据建立分层贝叶斯模型，同时拟合爆发间本征散布、宿主端项和共同的地球端项。三个源的宿主暗物质密度与本地标度相近，完整双端模型因此避免把任一端的贡献预先省略。各源与联合 FRB 偏振阵列都没有给出轴子诱导周期调制的显著证据。在 $10^{-23}$--$10^{-18}\,\mathrm{eV}$ 的质量区间，95% 可信上限把耦合限制在 $10^{-12.6}$--$10^{-7.9}\,\mathrm{GeV^{-1}}$。阵列在低质量端可改善单源约束，当前灵敏度主要来自自相关；爆发活动的非规则采样和最长约 472 天的基线仍限制慢振荡信号，长期监测和更多稳定偏振源将提高灵敏度。

    <img src="./Figures/image-202609220000005.png" alt="image-202609220000005" width="680px" />

6. [Fast Radio Bursts Associated with Persistent Radio Sources Prefer Hydrogen-poor Superluminous Supernova Host Environments](https://arxiv.org/abs/2609.24240)

    > Fast Radio Burst, PRS, Host Galaxy

    工作将四个已确认 FRB-PRS 宿主与 SLSN-I、SLSN-II、核心坍缩超新星、普通定位 FRB 及红移受控模拟星系比较。FRB-PRS 宿主集中在低恒星质量、高比星形成率和低金属丰度区，与富氢贫乏型超亮超新星 SLSN-I 的质量、星形成和化学丰度分布相容。它们相对普通 FRB 宿主和按恒星形成率加权的星系母体呈系统偏移，支持年轻磁星及受限前身环境的图景。以 SLSN-I 抛射物总体性质估算，600 MHz 的自由—自由透明时间约为 29 年，年轻遗迹可在较高频段先进入可观测窗口。四个宿主的样本规模仍很小，宿主相似性不能单独确立共同前身，抛射物电离状态和密度结构也会改变透明时间。

    <img src="./Figures/image-202609220000006.png" alt="image-202609220000006" width="680px" />

7. [Rotating Radio Transient Phases of Isolated Neutron Star Systems and Descendants of Central Compact Objects](https://arxiv.org/abs/2609.24286)

    > RRAT, Neutron Star, Theory

    该工作在回落盘模型中计算孤立中子星的自旋演化，并把内盘进入光柱、增强死脉冲星开放磁通的阶段定义为 RRAT 相。得到的 RRAT 区域覆盖已知源在 $P$--$\dot P$ 图上的主要分布，说明这一演化通道可再现其周期和周期导数范围。作者还沿同一轨迹考察中心致密天体后代：三颗拥有测得 $\dot P$ 的经典 CCO 在模型中不会演化成射电脉冲星，Calvera 类源则可进入寿命超过 $10^8$ 年的射电脉冲星相。结果把稀疏爆发与长期盘—磁层演化联系起来。模型没有从微观机制计算射电爆发，初始盘质量、磁场及出生率假设仍会影响 RRAT 与 CCO 的种群推断。

    <img src="./Figures/image-202609220000007.png" alt="image-202609220000007" width="680px" />

8. [Fast and accurate astronomical source deblending with Density-Peak Clustering](https://arxiv.org/abs/2609.24318)

    > Imaging, Clustering, Software

    ADP 将密度峰聚类改造成像素级去混叠器，并以受控双源、合成多源和 Euclid Q1 实像的统一真值框架同 ASTErIsM 比较。双源模拟中两者的测光差异通常低于 1%，最困难构型达到 5--7%；多源模拟里 ADP 恢复的真值源多约 8%。Euclid 实像的分割面积、椭率、位置角和测光总体一致，最小最暗源是差异集中的区域。对 $19200\times19200$ 像素图像的端到端测试给出 12--156 倍加速，适合大巡天的高吞吐处理。当前验证的形态与观测条件仍有限，串行步骤和异质检测区域会削弱高线程数效率，分布式内存版本仍待实现。

    <img src="./Figures/image-202609220000008.png" alt="image-202609220000008" width="680px" />

9. [Stellar flare detection and characterization in ZTF High-cadence light curves](https://arxiv.org/abs/2609.24335)

    > Stellar, Flare, Light Curve

    作者对 ZTF Extended Deep-Drilling 的约 2,800 万条、单段约 6.2 小时的高采样光变曲线先做 Tukey 双权稳健去趋势，再用连续显著点、时间间隔和人工图像审查筛选耀斑。流程最终保留 310 颗恒星上的 331 次耀斑，并对具可靠距离的子样本以黑体假设估算能量。经验耀斑模板给出能量与持续时间的幂律指数 $0.19\pm0.01$，衰减时间、上升时间和半高全宽也与能量相关。结果说明短时段地基高采样可产生跨演化阶段的统计耀斑样本。初始候选含大量混叠、鬼影、小行星和 CCD 伪信号，人工复核仍是可靠性关口；模板自由度会改变复杂耀斑的形态分类。

    <img src="./Figures/image-202609220000009.png" alt="image-202609220000009" width="680px" />

10. [Transit timing variation](https://arxiv.org/abs/2609.24645)

    > Exoplanet, Timing, Review

    这篇综述系统整理凌星中点相对线性星历的 $O-C$ 偏差如何揭示多行星引力摄动，并可约束凌星或未凌星扰动体的质量和轨道参数。文章说明近平均运动共振会增强 TTV，同时要求通过共振角、长期数值积分和稳定性指标区分表面周期比接近与真实动力学结构。参数反演覆盖解析近似、N 体积分、全局和局部优化及贝叶斯后验采样，链收敛和参数相关性检查决定不确定度是否可信。TTV 与径向速度对质量—半径空间的灵敏度不同，二者的样本不能直接混作无偏人口。文中以 TOI-216 型合成系统演示轨道积分、工具比对和后验分析；[TTV_DataAnalysis 示例](https://github.com/lucaborsato/TTV_DataAnalysis)已公开。解析公式的适用范围、观测基线和计时精度共同限制可辨识参数，稳定性判断也依赖积分时间与模型选择。

    <img src="./Figures/image-202609220000010.png" alt="image-202609220000010" width="680px" />

## 2026-09-23

1. [A Brief Review on the Statistical Properties of Fast Radio Bursts](https://arxiv.org/abs/2609.25810)

    > Fast Radio Burst, Statistics, Review

    这篇综述汇集 CHIME、ASKAP、DSA-110、FAST 等目录的 FRB 统计结果，按表观单次源、重复源、周期性和偏振四条线索组织证据。局域化样本给出的宿主色散量中位数约为 $150\ \mathrm{pc\,cm^{-3}}$，能量函数常取指数 $1.8--1.9$ 并在约 $10^{42}$ erg 出现高能截断。CHIME 表观单次源的红移分布支持相对恒星形成史受抑的演化或数十亿年的延迟。重复源的能量、流量和等待时间常呈折弯、多峰或 Weibull 结构，RM 与偏振角的源际差异连接局域磁离子环境。不同巡天灵敏度、色散量分解和长期曝光共同限定这些人口学解释。文章将这些量视为同一选择函数下的观测投影，并把未来宽带极化、深度复访和更大局域化样本列为鉴别形成通道的关键。原始版本只提供四张汇总表格，未提供可嵌入的原始图件。

2. [IXPE observation of the new magnetar source EP J223759.5+531421](https://arxiv.org/abs/2609.25958)

    > Magnetar, Polarization, X Ray

    IXPE 在 2026 年 7 月的约 $200\ \mathrm{ks}$ 跟踪中获得 EP J223759.5+531421 的约 $6$ 万个 $2--8\ \mathrm{keV}$ 净计数，并同 EP-FXT 做联合时谱偏振分析。$2--7.5\ \mathrm{keV}$ 的相位及能量平均偏振度约 $7\%$，显著性超过 $4\sigma$；$4--7.5\ \mathrm{keV}$ 次峰附近的相位分辨偏振度达到约 $63\%$。偏振角在一个自转周期内由 $-90^\circ$ 连续摆到 $+90^\circ$，RVM 拟合给出视线与自转轴夹角约 $28^\circ$、磁轴夹角约 $109^\circ$。约 $0.5\ \mathrm{keV}$ 的暖区和约 $1\ \mathrm{keV}$ 的热点具有不同偏振性质，支持反足热帽加小尺度大气热点的几何图像。双峰光变在各能段持续存在，热区温度与面积的相位变化支持局域表面辐射。相位平均的低偏振来自旋转中 Stokes 矢量抵消，因而相位分辨测量更直接约束内禀偏振。现有曝光为衰减阶段的偏振时变留下后续监测空间。

    <img src="./Figures/image-202609230000002.png" alt="image-202609230000002" width="680px" />

3. [Einstein Probe discovery of the magnetar EP J223759.5+531421](https://arxiv.org/abs/2609.25990)

    > Magnetar, X Ray, Observation

    Einstein Probe 在 2026 年 6 月 28 日发现 EP J223759.5+531421 的爆发，EP、XMM--Newton、NuSTAR、SVOM 与 IXPE 的随访给出约 $6\ \mathrm{s}$ 脉冲和平均周期导数约 $2.8\times10^{-12}\ \mathrm{s\,s^{-1}}$。相应的名义极区偶极磁场约为 $2.6\times10^{14}\ \mathrm{G}$，特征年龄约 $34\ \mathrm{kyr}$。采用 $3.3\ \mathrm{kpc}$ 距离时，$0.5--30\ \mathrm{keV}$ 光度首月由 $1.2\times10^{35}$ 降至 $5.7\times10^{34}\ \mathrm{erg\,s^{-1}}$，热辐射区面积同步收缩，硬幂律尾部仍可见。$0.5--10\ \mathrm{keV}$ 脉冲分数在约 $7\ \mathrm{keV}$ 以下为 $20--25\%$，更高能段下降，显示多温区和磁层散射共同调制光变。经验指数衰减的 $e$ 折叠时间约 $31$ 天，拟合残差显示完整冷却曲线仍待覆盖。12 个短 X 射线暴巩固磁星归类，GTC 与 FAST 分别给出 $K_s>21\ \mathrm{mag}$ 和约 $2.3\ \mathrm{\mu Jy}$ 的深限。源在银道面下约 $0.26\ \mathrm{kpc}$，计时噪声、距离和真实年龄共同需要持续跟踪。

    <img src="./Figures/image-202609230000003.png" alt="image-202609230000003" width="680px" />

4. [Bayesian Galaxy Asymmetry](https://arxiv.org/abs/2609.26472)

    > Galaxy, HI, Bayesian

    这项工作为 $21\ \mathrm{cm}$ H I 数据立方体的平方差星系不对称度建立贝叶斯后验，将噪声不确定度直接转化为每个目标的概率分布，并用覆盖率检验校准相关像素的过采样因子。WALLABY 应用中，后验众数与既有 $A_{\mathrm{3D}}$ 测量保持一致，同时得到 331 个可靠后验，相比 116 个频率学估计使可用样本接近三倍。新增目标主要位于低不对称度端，后验宽度提供统一的置信度门槛。推导以均匀高斯噪声和固定中心为基础，泊松噪声、掩膜非均匀性和分辨率损失需要独立建模；[galaxy_asymmetry 代码库](https://github.com/mathieu-pc/galaxy_asymmetry/)已公开。

    <img src="./Figures/image-202609230000004.png" alt="image-202609230000004" width="680px" />

5. [Catalogue of Solar Radio Bursts Detected by the LOFAR LV614 Station at the Irbene Observatory during Solar Cycle 25](https://arxiv.org/abs/2609.26535)

    > Solar Radio Burst, LOFAR, Catalog

    LOFAR LV614 站在 2022 年 6 月至 2025 年 8 月以每周节奏积累 194 次、共 1125.2 小时的 $29--60\ \mathrm{MHz}$ 太阳观测，并用 Cas A 完成绝对带通和流量标定。目录收录 335 个爆发，其中 I 至 V 型分别为 23、8、293、6 和 5 个，峰值流量覆盖 $0.3--234\ \mathrm{SFU}$。II 型和 III 型的平均频率漂移分别为 $0.043$ 和 $4.383\ \mathrm{MHz\,s^{-1}}$，III 型电子束速度在基频和二次谐波假设下分别达到 $0.005--0.477c$ 与 $0.008--0.794c$。I 型和 III 型的峰值流量分布随流量递减，拟合幂律指数约为 $-0.9$ 和 $-1.25$。目录还给出峰值频率、源高和漂移率，可作为自动识别训练与空间天气个例研究的数据底座。摘要和结论的分型计数相加为 335，正文示例段落的若干逐型数值与该组统计不一致，目录使用前需核验版本。峰频换算的源高和速度依赖 Newkirk 密度模型与发射谐波选择；[Zenodo 目录](https://doi.org/10.5281/zenodo.20157853)已公开。

    <img src="./Figures/image-202609230000005.png" alt="image-202609230000005" width="680px" />

## 2026-09-24

1. [Interference Meets Inference: Bayesian Time-Series Modeling of Radio-Frequency Interference](https://arxiv.org/abs/2609.26904)

    > RFI, Bayesian, Time Series

    研究把射频干扰识别重写为一维时间序列的贝叶斯混合推断：每夜用 24 阶 Legendre 多项式描述平滑增益背景，残差由高斯净空分量和正偏 Cauchy 污染分量共同拟合，并为每个时样给出 RFI 后验概率。作者在 2014 年 MWA Phase I EoR 高频段的 3,168 段两分钟观测上运行 50 组指向、偏振和频段拟合，约 2% 的夜晚经质控剔除。结果显示 XX 偏振普遍比 YY 污染更高，181--188 MHz 的 TV7 带与西向 1 号指向最突出，随机拆分和按时序拆分均揭示夜际占空度超过二项抽样散布。软标签与 SSINS 硬标记在强干扰和时间趋势上相合，同时保留分类置信度和下游误差传播信息。子带平均降低了窄带 RFI 灵敏度，独立时样状态也尚未表达干扰的时间持续性；[bayesian-rfi 代码](https://github.com/jade-ducharme/bayesian-rfi)已公开。

    <img src="./Figures/image-202609240000001.png" alt="image-202609240000001" width="680px" />

2. [A multi-telescope fit to the FRB population, allowing for FRB repetition](https://arxiv.org/abs/2609.27282)

    > Fast Radio Burst, Population, Statistics

    工作用 zDM 联合拟合 ASKAP、Parkes、DSA、FAST、MeerKAT 与 CHIME catalogue 1，以单一内禀 FRB 种群和幂律重复率分布连接表观单次源与重复源。含重复统计的 CHIME 与 CRAFT ICS 合计 520 个源、16 个重复源；其余望远镜样本因缺少可靠的视场停留时间，只进入红移、DM 和信噪比似然。对于主机系 $10^{39}$ erg 以上的爆发，得到 $\log_{10}R_{\rm min}=-4.23^{+1.10}_{-1.74}$、$R_\gamma=-2.20^{+0.12}_{-0.22}$，且 $R_{\rm max}\gtrsim1\,\mathrm{d^{-1}}$。拟合可重现 CHIME catalogue 1 的 DMEG 累计分布，KS $p=0.9$，未参与拟合的 catalogue 2 给出 $1.8\times10^{-4}$，提示新目录的重复源归属与模型假设需要进入下一轮推断。模型还把 CHIME 低频样本与局域化样本的频谱杠杆共同纳入约束。全体源共享同一能量、谱和演化分布，泊松爆发假设和活动窗仍限制物理解读；[zDM 代码和数据](https://github.com/FRBs/zdm)已公开。

    <img src="./Figures/image-202609240000002.png" alt="image-202609240000002" width="680px" />

3. [Kelvin-Helmholtz vortices in the Martian +E hemisphere downstream of crustal magnetic anomalies](https://arxiv.org/abs/2609.27474)

    > Mars, Magnetic Field, Observation

    MAVEN 在 2023 年 5 月 15 日 04:06--04:19 UT 穿过火星南半球的过渡层，连续检出五个 Kelvin--Helmholtz 涡旋脊；H$^+$、O$^+$、O$_2^+$ 成分交替、双极磁场、中心压力亏损及最小方差分析共同支持充分卷起的 KH 结构。天问一号在 03:22--04:00 UT 测得稳定上游 IMF，时钟角为 $211.9^\circ$，将事件稳健置于传统不利的 +E 半球。根据局地等离子体状态，作者估计相速约 $81\,\mathrm{km\,s^{-1}}$、波长约 $8065\,\mathrm{km}$、线性增长率 $4.07\times10^{-2}\,\mathrm{s^{-1}}$；南部强壳磁异常下游的抬升弱磁场边界可提供起伏种子并降低磁张力稳定作用。圆柱模型给出氧离子输运上限约 $8.65\times10^{24}\,\mathrm{s^{-1}}$，表示事件级可能贡献。单个事例、六分钟上游空档、代理太阳风等离子体参数和未直接观测到的涡旋脱离共同限制全球逃逸率外推；[可复现代码与处理数据](https://doi.org/10.5281/zenodo.21821801)已公开。

    <img src="./Figures/image-202609240000003.png" alt="image-202609240000003" width="680px" />

## 2026-09-25

1. [AstroGenesis: A Domain-Specific Multi-Agent AI for Astrophysical Research](https://arxiv.org/abs/2609.28579)

    > Astronomy, LLM, Software

    AstroGenesis 将文献检索、多波段数据访问、理论建模和研究构想放入由 Supervisor 与 Planner/Replanner 协调的多智能体框架，现有完整领域实现聚焦耀变体。文献代理结合稠密—稀疏检索、引文扩展和交叉编码器重排序；单篇与多篇问题的前五名结果分别有 $76.6\%$ 和 $79.2\%$ 至少包含一篇相关论文。理论代理用预训练神经网络代理与贝叶斯推断拟合 SSC、EIC、强子和混合模型，并可组合电磁与中微子约束。本文报告研究工作流框架及其检索评估。GRB、TDE、FRB 模块和原始数据处理属于后续开发范围，多篇问题的 Recall@10 与 Evidence Coverage@10 分别为 $0.497$ 和 $0.354$；物理假设、数据处理和科学解释需要研究者独立核验。

    <img src="./Figures/image-202609250000001.png" alt="image-202609250000001" width="680px" />

2. [A Practical Primer on Software Citation in Research](https://arxiv.org/abs/2609.28622)

    > Astronomy, Software

    这篇跨学科指南把研究软件引用整理为七步：盘点直接贡献结果的软件、审视关键依赖、记录版本、遵循首选引文、写入正式参考文献、提供软件说明和最终核验。作者建议把版本、DOI 与代码入口保留在正式条目中，并让领域内软件说明和参考文献配套出现。软件发布端的五步流程要求为每个版本建立持久标识符、在 CITATION.cff 等文件给出引文、维护作者与元数据，社区登记和软件论文可提高发现性。依赖引用范围由软件对科学结果、可复现性和开发者贡献的实际作用决定；环境、容器、依赖树和文档仍需独立保存。

    <img src="./Figures/image-202609250000002.png" alt="image-202609250000002" width="680px" />

3. [Probing the Metallicity Dependence of Fast Radio Burst Progenitors with CHIME/FRB Outrigger Dwarf Host Galaxies](https://arxiv.org/abs/2609.28629)

    > Fast Radio Burst, Host Galaxy, Metallicity

    工作在 CHIME/FRB Outriggers 定位源中表征八个宿主，并新增五个恒星质量 $\log(M_\ast/M_\odot)=8.1$--$9.1$ 的矮星系宿主。统一的 O3N2 丰度标定显示，重复源和表观单次源的宿主金属丰度分布由 log-rank 检验区分，$p=0.001$；重复矮宿主大多低于 $12+\log(\mathrm{O/H})=8.35$，关联持久射电源的重复源几乎都低于 $8.2$。作者将这一趋势与低金属环境中快速自旋磁星前身的可能性联系起来。宿主 DM、RM 与 $1\ \mathrm{GHz}$ 散射时间没有给出超过 $3\sigma$ 的金属丰度相关性。样本规模、宿主识别深度和散射选择效应共同限制前身通道的物理解读。

    <img src="./Figures/image-202609250000003.png" alt="image-202609250000003" width="680px" />

4. [Mapping the Milky Way in Six Dimensions: A contiguous, homogenised, phase-space catalogue of Gaia DR3 tracers up to 250 kpc.](https://arxiv.org/abs/2609.28652)

    > Milky Way, Kinematics, Catalog

    工作将 Gaia DR3 与 DESI、SDSS/BOSS、APOGEE、LAMOST、GALAH、GES 等十四项巡天的距离和视向速度资料同质化，形成 32,552,876 颗独特恒星的连续六维目录，覆盖银河系内区至约 $250\ \mathrm{kpc}$，其中有 517,123 颗远晕示踪体。流程以重复观测归一化不确定度、校正相对 Gaia 的速度零点、图式去重和加权合并控制异构记录。日心距离不大于 $15\ \mathrm{kpc}$ 时中位相对距离误差约为 $2.7\%$，更远处约为 $29\%$，全目录中位相对视向速度误差约为 $8.31\%$。星团、矮星系和人马座星流验证显示远晕的分光光度距离和速度信息具有互补价值。目录与数据产品将在论文接收后按向通讯作者合理请求提供。

    <img src="./Figures/image-202609250000004.png" alt="image-202609250000004" width="680px" />

5. [Cluster Membership Probabilities: A Review of Methods and Gaia Applications](https://arxiv.org/abs/2609.28753)

    > Cluster, Gaia, Review

    这篇综述系统比较空间、运动学、光度、密度聚类、贝叶斯、机器学习和重采样方法，并将逐星成员概率与候选体自身是否为真实星团的对象级可信度定义为两个独立推断量。CANTAT20 在 $G<18$ 的 1,481 个星团中使用 UPMASK；HUNT23 报告 7,167 个检出体和 2,387 个新候选体；UCC 汇集 13,684 个候选体。亮星成员表中，UCC 与 CANTAT20 的交叠通常为 $75$--$80\%$，与 HUNT23 为 $70$--$75\%$；HUNT23 延伸到 $G\sim20$ 时部分交叠降至约 $35\%$。作者要求成员表明确数据版本、输入维度和协方差、选择函数、算法与超参数、概率校准、验证集合和源标识，使跨目录比较具有可复现的条件。

    <img src="./Figures/image-202609250000005.png" alt="image-202609250000005" width="680px" />

6. [DETECT: Real-Time Identification of Transients with DESI Spectroscopic Redshift](https://arxiv.org/abs/2609.28951)

    > Transient, Host Galaxy, Software

    DETECT 每小时接入 TNS 暂现源报告，并通过 HEALPix 在约 2,200 万条 DESI EDR 与 DR1 光谱记录中检索候选宿主。系统按照星系形态使用方向光半径规则：DEV、SER、COMP 采用 $4$ 倍阈值，EXP、REX 采用 $8$ 倍阈值，边界案例进入人工复核。4,474 颗具有已知红移的超新星标定给出 $92.5\%$ 完备度和 $0.4\%$ 错误宿主率；2020--2024 年约 $1.2\times10^5$ 个 TNS 报告的回溯分析为约 $15\%$ 找到 DESI 光谱宿主，并形成约 5,400 个暂现源的 Gold 样本。2025 年运行在报告后数小时内将 SN 2025wny 与 $z=0.375$ 宿主关联，得到约 $-22.5$ 等的绝对星等。DESI 天区覆盖、无光谱宿主和光变质量限定总体回收率，公共社区访问属于后续计划。

    <img src="./Figures/image-202609250000006.png" alt="image-202609250000006" width="680px" />

7. [Exoplanet Detection Techniques: Radial Velocity](https://arxiv.org/abs/2609.29378)

    > Exoplanet, Radial Velocity, Review

    本章从开普勒径向速度半振幅出发说明行星质量、周期、偏心率、倾角和恒星质量如何进入速度信号；太阳—地球类似系统的半振幅仅约 $9\ \mathrm{cm\,s^{-1}}$。高分辨率光谱的交叉相关和模板匹配需要同恒星活动指标一起使用，避免旋转调制和谱线形状变化产生伪行星周期。55 Cnc 的 1989--2020 年公开数据可由五个周期约为 $0.736$、$14.6$、$44.4$、$261$ 和 $4,800$ 天的行星拟合，残差均方根由约 $52.7$ 降至 $22.6\ \mathrm{m\,s^{-1}}$。TIC-172900988 的实例给出约 $151.2$ 天的强周期信号，贝叶斯因子超过 1,005；TOI-776 展示凌星与速度联合拟合如何给出真实质量。径向速度单独只约束 $M_{\rm p}\sin i$，长期基线、活动建模和选择函数决定低振幅信号及人口学结论的可靠性。

    <img src="./Figures/image-202609250000007.png" alt="image-202609250000007" width="680px" />

8. [Estimates of magnetic field strength in the solar corona using observations of thermal radio emission at low frequencies](https://arxiv.org/abs/2609.29602)

    > Solar, Radio, Magnetic Field

    升级后的 GRAPH 在 2025 年 4 月 12 日以 $51\ \mathrm{MHz}$、$1\ \mathrm{MHz}$ 带宽和 $10\ \mathrm{s}$ 积分对无爆发时段的热日冕取得 Stokes I 与 V 图像。偏振峰值附近的 Stokes I 亮温约为 $7.3\times10^5\ \mathrm{K}$，Stokes V 约为 $0.2\times10^5\ \mathrm{K}$，圆偏振度约为 $2.7\%$。作者在参数化密度、温度和磁场日冕中追踪普通模与异常模射线，同时拟合强度和偏振剖面，在约 $1.65\pm0.15\,R_\odot$ 处得到 $1.55\pm0.3\ \mathrm{G}$ 的局域磁场与约 $3.2\times10^7\ \mathrm{cm^{-3}}$ 的电子密度。温度由 $1.4\times10^6$ 改为 $1.0\times10^6\ \mathrm{K}$ 时，场强解约为 $1.13\pm0.3\ \mathrm{G}$。密度、温度、磁场参数化和一维赤道面几何共同决定系统误差，二维模拟与更多频率和历元将检验反演的稳定性。

    <img src="./Figures/image-202609250000008.png" alt="image-202609250000008" width="680px" />

## 2026-09-28

1. [Spectral and Polarization Properties of Coherent Radio Emission from Relativistic Magnetized Pair Plasma Shocks](https://arxiv.org/abs/2609.30494)

    > Fast Radio Burst, Polarization, Simulation

    三维粒子模拟检验磁化电子—正电子激波能否同时解释 FRB 的频谱和偏振，并将不同视线方向的辐射积分到球形激波表面。谱峰附近始终由 X 模主导，保持接近完全的线偏振和稳定偏振角；较弱的高频辐射中 O 模增强，可产生圆偏振与偏振角变化。球面积分后的完整谱包络相对半高宽约为 $0.57$–$0.82$，高纬度辐射进一步展宽频谱。灵敏度有限时，最亮的窄谱峰仍可能单独被探测到，但同时具有窄带、强圆偏振和大幅偏振角变化的重复爆发对该模型构成挑战。这些结论适用于冷上游、平滑球面和忽略辐射冷却的模拟条件。

    <img src="./Figures/image-202609280000001.png" alt="image-202609280000001" width="680px" />

2. [FOTO: Figure-Level Semantic Search for Astronomy](https://arxiv.org/abs/2609.30536)

    > Astronomy, LLM, Software

    FOTO 支持通过自然语言描述检索天文论文中的具体图件，索引覆盖 53,839 篇论文的 482,750 条图注。系统用本地开放模型编码标题与图注，再由大语言模型核验候选图件并重排序，也支持草图查询。合成查询测试中，目标图进入前二十项的比例随描述方式变化，约为 $29\%$–$79\%$；详细描述的效果优于模糊描述。重排序进一步提高首位命中率，其评估范围限于目标图已进入候选池的查询，端到端检索仍受第一阶段召回限制。[代码与部署说明](https://github.com/htohfa/Figure-Finder/)已公开；原文用表格呈现评估结果。

3. [Tracing the Host-Galaxy Environments of FRBs with a New Sample of Localized Sources Detected with the DSA-110](https://arxiv.org/abs/2609.30616)

    > Fast Radio Burst, Host Galaxy, Dispersion Measure

    对 43 个具有宿主光谱红移的 DSA-110 定位 FRB 联合分析色散量、旋转量、散射和闪烁，约束爆发所在的磁化等离子体环境。扣除银河系与星系际贡献后，宿主静止系色散量分布的中位数约为 $242\ \mathrm{pc\,cm^{-3}}$，并与宿主旋转量绝对值呈正相关。散射性质与银河系脉冲星的经验关系大体相容，宿主色散分布也更接近 FIRE-2 中年龄小于 $10\ \mathrm{Myr}$ 的恒星群体预测。这些证据支持 FRB 偏好电离氢区及年轻磁星前身的解释；结论依赖前景扣除、宿主选择和模拟星系的代表性。[观测数据](https://code.deepsynoptic.org/dsa110-archive/)可公开获取。

    <img src="./Figures/image-202609280000003.png" alt="image-202609280000003" width="680px" />

4. [Probing the cosmic web with fast radio bursts: II. Scintillation](https://arxiv.org/abs/2609.31106)

    > Fast Radio Burst, Scintillation, Theory

    研究建立宇宙网冷云团的多重散射屏模型，利用前景散射展宽 FRB 表观像、进而压低银河系闪烁的效应探测多相气体。模型结合冷却破碎尺度、湍流和视线相交概率，预报闪烁抑制比例随红移及色散量的变化。在典型银河系散射屏条件下，若大质量星系晕内冷云团体积填充率至少为 $10^{-4}$，平均星系际色散量超过约 $500\ \mathrm{pc\,cm^{-3}}$ 的多数 FRB 将在约 $1\ \mathrm{GHz}$ 以下出现闪烁抑制。丝状体和片状体主要影响更高红移视线。这些结果属于模型预报，实际检验需同时约束云团尺寸、湍流、银河系散射屏和仪器频率分辨率。

    <img src="./Figures/image-202609280000004.png" alt="image-202609280000004" width="680px" />

5. [The NEMESIS general YSO catalogue - I. Supervised classification with deep learning methods](https://arxiv.org/abs/2609.31109)

    > YSO, Classification, Deep Learning

    NEMESIS 将异构测光资料绘制成统一的光谱能量分布图，训练卷积网络集成投票，对文献中的年轻恒星候选体进行一致分类，得到含 274,408 个独特候选源的 NGYSO 星表。SED 集成分类器在留出测试集上的 $F_1$ 为 $96.90\%$，外部非年轻恒星样本的误报率约为 $0.99\%$。候选体的颜色—绝对星等分布与前主序星一致，空间分布也呈现与本地泡边界及 Radcliffe Wave 的关联。误报率与最终星表污染比例具有不同分母；足够的多波段覆盖要求和输入目录选择限制了完备度。[DLYSO 分类工具](https://github.com/martongabor/DLYSO)已开源。

    <img src="./Figures/image-202609280000005.png" alt="image-202609280000005" width="680px" />

6. [JWST detection of methane emission from a young brown dwarf](https://arxiv.org/abs/2609.31178)

    > Brown Dwarf, Spectrum, JWST

    JWST/NIRSpec 对 IC 348 中质量约为 $6\,M_{\rm Jup}$ 的年轻褐矮星 LRL 11001 取得中分辨率光谱，发现位于 $3.324$ 和 $3.333\ \mu\mathrm{m}$ 的甲烷热带发射线。更精细的脂肪族碳氢吸收结构可由 CH₂ 与 CH₃ 伸缩振动拟合，支持较大烷烃作为吸收载体。这是年轻褐矮星中首次探测到该甲烷发射特征，与其缺乏预期甲烷吸收的光谱共同约束非平衡化学。发射的大气起源受到支持，热激发与外部辐射泵浦仍待建模区分；垂直混合抑制深层甲烷、上层甲烷保留并发光的图景属于待检验解释。

    <img src="./Figures/image-202609280000006.png" alt="image-202609280000006" width="680px" />

7. [A Comprehensive Study of the Magnetic White Dwarfs in DESI DR1](https://arxiv.org/abs/2609.31565)

    > White Dwarf, Magnetic Field, DESI

    DESI DR1 光谱识别出 833 个磁性白矮星系统，并以偏心偶极场大气模型拟合其中 762 个；127 个谱线异常尖锐或浅弱的目标通过限制表面谱线形成区域的斑块模型获得更好的拟合。质量、冷却年龄和场强分布显示，多种磁场形成通道共同参与：部分对象与前身星遗留磁场逐渐浮出表面的预报相容，年轻大质量强磁对象支持并合起源，许多对象的年龄仍早于核心结晶。斑块模型提供复杂场形与成分分布的有效描述，表面几何解具有简并；样本也偏向较亮对象和较强磁场。[光谱拟合产品](https://doi.org/10.5281/zenodo.22878226)已公开。

    <img src="./Figures/image-202609280000007.png" alt="image-202609280000007" width="680px" />

## 2026-09-29

1. [Correlated Signatures of Plasma Lensing in Fast Radio Bursts](https://arxiv.org/abs/2609.31842)

    > Fast Radio Burst, Plasma Lensing, Theory

    一维高斯等离子体透镜模型推导了快速射电暴在折叠焦散附近的联合观测判据，覆盖可分辨双像、非相干重叠和相干干涉三种情形。双像群时延随放大率的倒数变化，平滑频谱包络宽度随放大率平方的倒数变化，干涉条纹间距则由群时延的倒数决定。高倍放大与清晰条纹分别约束辐射区尺度，条纹对比度还受带通、偏振及散射影响。第三像的亮度和到达顺序、时频轨迹及差分色散可进一步检验同一透镜解。结论依赖所选透镜几何；稀疏薄片、细丝和界面更有利于形成可辨认的孤立透镜事件。

    <img src="./Figures/image-202609290000001.png" alt="image-202609290000001" width="680px" />

2. [Observations of Repeating Tidal Disruption Events](https://arxiv.org/abs/2609.33809)

    > TDE, High Energy, Review

    这篇综述整理光学与 X 射线波段的重复核区耀发，讨论恒星多次部分潮汐瓦解、活动星系核吸积变化及相关观测判据。光学样本按 TDE、Bowen 荧光耀发和 AGN 光谱分类，X 射线样本按复发时标比较；AT 2022dbl 的两次近乎相同光谱，以及 AT 2023uqm 周期性增强的耀发，提供不同类型的重复瓦解线索。部分 X 射线源呈现日冕形成和骤然熄灭。样本整体具有明显异质性，红噪声、档案选择效应及后星暴星系中较高的独立 TDE 发生率均会影响判定。可靠确认需要联合宿主性质、多次光谱和长期复发记录。

    <img src="./Figures/image-202609290000002.png" alt="image-202609290000002" width="680px" />

3. [Discovery of a 62-min long-period transient with near-orthogonal rotator geometry](https://arxiv.org/abs/2609.34102)

    > LPT, Polarization, Observation

    MeerKAT 与 ASKAP 档案数据发现周期为 $62.20\pm0.02$ 分钟的长周期射电暂现源 LPT J1555−5631，其脉冲仅在一次短暂活动窗口内被探测到。每周期出现振幅相近、宽度不同的主脉冲和间脉冲，较短相位间隔为 $165.4^\circ$；间脉冲近乎完全圆偏振，两者的圆偏振符号相反。双磁极辐射支持磁轴与自转轴近乎正交的几何，非对跖间隔和平坦偏振位置角进一步提示不对称磁场或延展辐射区。电子回旋脉泽可解释若干特征，源的中子星或白矮星身份仍待确认，距离与周期导数也缺乏可靠约束。

    <img src="./Figures/image-202609290000003.png" alt="image-202609290000003" width="680px" />

4. [Fast radio burst - persistent radio source systems I. A 1.2 GHz search and catalog definition](https://arxiv.org/abs/2609.35729)

    > Fast Radio Burst, PRS, Catalog

    uGMRT 连续谱观测搜寻快速射电暴的持续射电对应体，并结合文献构建含 75 个 FRB 的光度测量与上限目录。新数据在多个重复源及一个表观单次源附近发现候选持续射电源，其物理关联仍受定位精度和角分辨率限制。对灵敏度达标的子样本，亮于 $10^{29}\ \mathrm{erg\,s^{-1}\,Hz^{-1}}$ 的持续源在仅计入已确认关联时占约 $6\%$，纳入全部候选后估计比例约翻倍。重复源与表观单次源的发生率分布仍明显重叠，重复源偏好仅在包容候选的情形下获得边缘证据。[源目录](https://github.com/davidepelliciari/PRS-catalogue)已公开。

    <img src="./Figures/image-202609290000004.png" alt="image-202609290000004" width="680px" />

5. [Fast radio burst - persistent radio source systems II. A faint PRS associated with the nearby FRB 20181030A?](https://arxiv.org/abs/2609.35730)

    > Fast Radio Burst, PRS, VLBI

    EVN 毫角秒成像探测到 FRB 20181030A 附近的候选持续源 20181030A-S1，测得流量密度为 $280\pm30\ \mu\mathrm{Jy}$。若它位于 NGC 3252，其尺度上限为 $R<0.5\ \mathrm{pc}$（68% 置信水平），谱光度约为 $10^{26}\ \mathrm{erg\,s^{-1}\,Hz^{-1}}$，显著低于已确认的 FRB 持续源。低旋转量、紧致性及射电谱可由磁星风星云示例模型共同解释，高频未探测结果要求辐射谱快速下降。模型参数具有简并，FRB 本身的定位仍较粗，背景紧致射电源的偶然投影也保留可能性；更精确定位将决定这一低光度关联是否成立。

    <img src="./Figures/image-202609290000005.png" alt="image-202609290000005" width="680px" />

6. [Fast radio burst - persistent radio source systems III. The relation bewteen PRS luminosity and FRB rotation measure](https://arxiv.org/abs/2609.35733)

    > Fast Radio Burst, PRS, Rotation Measure

    研究利用 50 个具有旋转量测量的 FRB，将持续射电源探测与光度上限纳入统一贝叶斯分析，并分别处理已确认关联及包含候选的样本。全样本保守情形得到 $L_\nu\propto|RM|^\beta$，其中 $\beta=1.43\pm0.26$，在两倍标准差范围内与线性标度相容。纳入未探测源后，关系的本征散度明显增大；在散度主要由演化驱动的假设下，结果偏向快速膨胀或高效粒子加速情景。星云尺寸的推断受电子参数简并与先验影响，种群异质性和中心引擎差异也可能贡献散度，演化模型比较因此具有条件性。

    <img src="./Figures/image-202609290000006.png" alt="image-202609290000006" width="680px" />
