## 2026-09-01

1. [Type I Solar Radio Bursts Modulated by Solar Flares](https://arxiv.org/abs/2608.29744)

    > Solar radio bursts, Solar flares, Magnetic reconnection, Solar radio imaging

    作者以 2023 年 12 月 24 日 AR 3529 的一次 M2.9 耀斑为例，联合 ORFEES/NRH 射电观测、SDO EUV 与磁场数据，追问耀斑如何调制持续的 Type I 噪暴。耀斑前 Type I 发射位于约 100–350 MHz；耀斑期间其强度受抑，同时出现正、反向两支 Type III，起始频率由约 220 MHz 降至 188 MHz，之后仅在较高频率恢复。磁通取消、EUV 喷流、射电源位置和 PFSS 外推共同支持一种图景：预耀斑的小尺度重联向闭合磁环补给非热电子，而耀斑时较高处的重联释放双向电子束、破坏电子俘获，因而压低 Type I 辐射。作者也强调，投影源位置与局部密度结构不足以唯一确定重联高度；把频率下降直接解释为重联上升并不自洽，仍需更多事件检验。

    <img src="./Figures/image-202609010000001.png" alt="image-202609010000001" width="680px" />

2. [DINOspec: Efficient Multimodal Alignment of Vision and Spectral Foundation Models for Astronomy](https://arxiv.org/abs/2608.30503)

    > Foundation models, Multimodal learning, Astronomical spectroscopy, Representation alignment

    论文提出 DINOspec：不重新训练视觉和光谱主干，而是冻结 DINOv3 图像编码器与 AION-1 光谱 tokenizer，再用轻量适配器和 CLIP 式对比损失把两种表征对齐。作者以 20,472 个 HSC–DESI 交叉匹配星系训练，并比较不同适配器初始化和分支冻结策略，以检验独立基础模型间的非对称迁移。在形态分类与光谱分类上，最佳配置分别将 F1 从 0.72 提升至 0.78、从 0.70 提升至 0.74；光谱红移预测则仍维持在约 \(R^2=0.9\)，几乎没有增益。结论是轻量跨模态对齐只会在两个模态确有互补信号时发挥作用；同时，形态评测依赖规模较小的 HSC 交叉样本，不能直接外推到任意巡天组合。

    <img src="./Figures/image-202609010000002.png" alt="image-202609010000002" width="680px" />

3. [Learning Radio Astronomical Representations with LeJEPA and Very Small Models](https://arxiv.org/abs/2608.30594)

    > Radio galaxies, Foundation models, Transfer learning

    本文检验小模型能否直接从领域内无标签无线电图像学到可迁移表征，以减少对大型自然图像基础模型迁移的依赖。作者在 RGZ20k 上比较 LeJEPA、SimCLR 与 BYOL，并在 RGZ、FIRST、MiraBest 三套无线电星系形态集上做线性探测和全量微调。约 6M 参数的 LeJEPA ViT-Tiny 在三套集上的全量微调 F1 为 0.72–0.96，普遍优于同尺寸基线，并达到或超过 22M 参数 EUPE ViT-S 的表现；图中的标注量曲线尤其显示其低标签优势。嵌入分析还表明 LeJEPA 较少放大相关无线电数据集之间的差异，但所有数据大多来自经相近 sigma-clipping 处理的 VLA 图像，尚不能证明它对不同仪器、频段或成像管线同样稳健。

    <img src="./Figures/image-202609010000003.png" alt="image-202609010000003" width="680px" />

4. [The DSA/Chronoscope fast radio burst survey: forecasts and science overview](https://arxiv.org/abs/2608.30943)

    > Fast radio bursts, Survey forecasts, Cosmology, Radio interferometry

    这是一篇 DSA/Chronoscope FRB 巡天的参考设计与科学预报，而非实际巡天数据发布。作者从现有 CHIME/FRB、Murriyang HTRU 等巡天率出发，结合仪器灵敏度、源计数与频谱先验，估计实时后端在全视场毫秒搜索中的样本量、定位和宿主跟进能力。基线方案需搜索约 \(6\times10^6\) 个波束，预期每个搜索子带每年发现约 \(10^4\) 个 FRB，名义五年跨子带总样本可达约 \(10^5\)。以模拟 DM 和 DESI 类星系的交叉相关为例，作者展示该样本可从 CGM 到大尺度结构约束宇宙重子与反馈；不过所有产出仍依赖未完全验证的 on-sky 灵敏度、FRB 源计数、频谱、算力以及宿主红移获取率。

    <img src="./Figures/image-202609010000004.png" alt="image-202609010000004" width="680px" />

5. [Agentic research is oxymoronic](https://arxiv.org/abs/2608.31161)

    > Research ethics, Agentic AI, Scientific interpretation, Astronomy

    这不是性能比较或实证研究，而是一篇关于科研解释、作者责任和 AI 使用的立场短文。作者基于自身使用 agentic LLM 的经验，区分了可由工具协助且能独立验证的事务（如调试与计算）与不可直接外包的科学解释：若研究者不能理解并承担解释，就不应把机器生成的解释视为自己的研究贡献。文章将大量缺乏人类解释和责任归属的论文累积称为“deliteration”，并主张期刊要求解释工作的人类披露、公开分析数据与中间结果、设置 AI 伦理讨论，同时正视“publish or perish”对早期研究者的激励。上述论证是规范性主张而非量化因果证据；原文 HTML 与源文件均不含图表，因此不附图。

## 2026-09-02

1. [Extended radio emission in and around the merging cluster A520 as seen by MeerKAT](https://arxiv.org/abs/2609.00156)

    > Galaxy Clusters, Radio Halo, MeerKAT, Radio Relics, Observation

    MeerKAT 深度成像正在并合的 A520，追踪中心射电晕、冲击前沿及维里半径附近的低表面亮度结构。中心晕在 NE–SW 方向受两条 X 射线冲击界定，NW/SE 翼将晕系统扩展至约 2 Mpc；射电—X 射线亮度关系呈次线性，支持大尺度湍流再加速。东北约 1.2 Mpc 的射电尾与暗子团 c1/c2 共位，较高的射电/X 射线比支持气体再吸积、压缩和湍流再加速共同增强宇宙线电子。两座外周遗迹和连接暗子团的射电桥表明并合生成的非热结构延伸到维里半径外。带内谱指数、低亮度成分的系统误差及射电桥的三维几何仍需更宽频和更深 X 射线观测检验。

    <img src="./Figures/image-202609020000001.png" alt="image-202609020000001" width="680px" />

2. [Archival transients detected with the MeerLICHT telescope I: Supernovae](https://arxiv.org/abs/2609.01052)

    > Supernovae, Transients, MeerLICHT, Light Curves, Observation

    以五年 MeerLICHT 瞬变档案和 TNS 光谱分类表为基础，研究系统建立 125 个超新星目录，并为其中 14 个具有早期多巡天覆盖的事件合并 MeerLICHT-$q$、ATLAS-$c,o$ 和 ZTF-$g,r$ 光变。时延校正后的复合光变由 $F=A(t-t_0)^2+B$ 拟合，以测量爆炸时刻和源静止系上升时间。模型为多数事件的早期上升提供稳健描述，图中的上升时间—峰值亮度平面将 Ia、IIP/L、IIn 和 Ic 事件置于不同区域，并复现 Ia 更亮事件具有更长上升时间的趋势。复合伪滤光片固定幂律指数，早期颜色演化、滤光片差异和稀疏相位覆盖会进入个体事件的系统误差。

    <img src="./Figures/image-202609020000002.png" alt="image-202609020000002" width="680px" />

## 2026-09-03

1. [Are Repeaters Prevalent Among the Known Fast Radio Burst Sources?](https://arxiv.org/abs/2609.02037)

    > Fast Radio Bursts, CHIME, Repetition, Population Statistics, Observation

    研究基于第二版 CHIME/FRB 目录，将观测单发源与每个重复源的首次暴和最高 fluence 暴构成可比样本，以 $\tau$ 统计和 Lynden–Bell $C^-$ 法校正能量—红移截断后重建能量函数与共动事件率。三类样本均呈折断幂律能量函数，重复源的高能端更陡，表明其暴发能量分布具有人口学差异。事件率演化中，单发样本 $B=-5.57$，两组重复源集中于 $-8.6$ 至 $-9.1$；等样本随机重采样保留了这一差异。结果支持一部分观测单发 FRB 具有独立的人口学性质，并指向多条前身通道。DM 推红移、经验完备阈值和选择函数决定绝对速率，因而结论适用于同一 CHIME 选择下的相对比较。计算工具已公开为 [Nonpara-Flask](https://github.com/xxxfei710/Nonpara-Flask)。

    <img src="./Figures/image-202609030000001.png" alt="image-202609030000001" width="680px" />

2. [Demonstrating the Time-Domain Capabilities of the 4-m International Liquid Mirror Telescope: An Early Census of Transient and Variable Detections](https://arxiv.org/abs/2609.02221)

    > Time Domain Astronomy, Transients, Variable Stars, ILMT, Observation

    ILMT 的 PyLMT 管线以差分成像、机器学习分类和目录交叉匹配处理近 3700 张 CCD 帧，形成约 2.3 万条告警，并给出小行星、变星、活动星系核和 21 个超新星候选的早期普查。固定指向液体镜逐夜重复扫描同一条天区，ZTF 存档将关键候选的光变延伸到更长时基；多帧检测、MPC、SIMBAD 和 TNS 共同用于候选验证。样本包含获得光谱确认的 Ia 型 SN 2024cjb、未编入 VSX 的食双星与 BY Dra 候选，以及多类活动星系核和近地小行星。公开 [DART](https://ilmt-dart.shares.zrok.io/) 仪表盘提供按坐标、目录类别、主机类型和机器学习得分筛选告警的界面。固定天顶条带、有限视场和季节性覆盖构成明确选择函数，更长时间基线与完整效率建模将扩展这份首批普查的统计解释。

    <img src="./Figures/image-202609030000002.png" alt="image-202609030000002" width="680px" />

3. [High performance Stingray](https://arxiv.org/abs/2609.02857)

    > X Ray Timing, Spectral Timing, High Performance Computing, Python, Tool

    Stingray 的性能更新面向大规模高能时序数据，把 Bartlett periodogram 和 cross spectrum 的分段计算实现为 memory-mapped 的 map–reduce 流程，并比较 multiprocessing、MPI 和 CUDA 直方图路径。该流程以事件数据段为计算单元。2–128 GB 模拟表明常用计时操作随数据规模线性或次线性增长，MPI 在小段和大段区间均展现最稳健的并行效率。XMM-Newton 对 Cyg X-1 的 CHOCBOX 实测中，完整监测的 Bartlett periodogram 速度约为对照流程的 16 倍，若干 spectral-timing 产品也获得加速。GPU 直方图在约 $10^8$ 个计数以上越过 CPU 性能交点，将 FFT 一并置入 GPU 可进一步降低数据传输占比。MPI 包装器与 GPU 路径目前处于 HENDRICS 的验证性实现阶段，能量分辨的 spectral-timing 产品需要更广泛基准；安装版本见 [stingray](https://pypi.org/project/stingray/2.2.7/)。

    <img src="./Figures/image-202609030000003.png" alt="image-202609030000003" width="680px" />

## 2026-09-04

1. [Morphology of Radio Sources in Representation Space](https://arxiv.org/abs/2609.03779)

    > Radio Galaxies, Morphology, Representation Learning, LOFAR, Deep Learning

    LoTSS-DR3 的 108,885 个已分辨射电源被投影到先前在 DR2 训练的 SimCLR–ResNet18 分类器集成表征空间，研究据低置信度样本的 HDBSCAN 簇和视觉核验扩展其形态分类。12 个既有类覆盖 88% 的 DR3 样本，低置信度部分新增 elongated core、FR-ambiguous、connected edge-bright、winged、complex 与 isolated lobe 六类。最近质心分类将新增簇赋给低置信度样本，图中的 UMAP 显示这些类型位于既有形态簇之间或外侧，并保留各自的罕见人口比例。结果表明预训练表征可在新巡天版本中定位未见形态，并为长尾形态构建后续标注集。新增簇的完整度与纯度受训练集中形态覆盖、源居中差异和视觉筛选限制。LoTSS-DR3 源目录已公开为 [LoTSS-DR3](https://lofar-surveys.org/dr3.html)。

    <img src="./Figures/image-202609040000001.png" alt="image-202609040000001" width="680px" />

2. [nufftcf: Fast Auto- and Cross-Correlation Function Estimation for Irregularly-Sampled Time Series via the Non-Uniform FFT](https://arxiv.org/abs/2609.03866)

    > Time Series, Correlation Function, NUFFT, Astronomy, Tool

    nufftcf 为不规则采样序列的自相关与互相关估计提供统一 Python 接口，以 FINUFFT 的非均匀 FFT 重写 Gaussian 和 rectangle kernel 的 Wiener–Khinchin 计算，并用双指针扫描求 lag bin 的有效配对数。合成 ACF/CCF 与 pastas、pyZDCF 的比较显示，NUFFT 结果在各自统计精度内保持一致；不规则数据基准把计算复杂度由 $O(n^2)$ 降至 $O(n\log n)$。含季节缺口、异方差测量误差和相关噪声的恒星模拟光变中，算法恢复了注入的 12 d 自转周期，20 组蒙特卡洛的噪声相关时标均值与 3.5 d 注入值相符。相关峰取最大值会引入与每个 lag 噪声水平同量级的选择偏差，密集 lag 网格的误差条需要用户以 bootstrap 或蒙特卡洛另行估计。代码、基准和 notebook 已公开于 [nufftcf](https://github.com/jecampagne/nufftcf)。

    <img src="./Figures/image-202609040000002.png" alt="image-202609040000002" width="680px" />

3. [A targeted search for fast radio bursts from magnetars in elliptical galaxies](https://arxiv.org/abs/2609.04118)

    > Fast Radio Bursts, Magnetars, Globular Clusters, Radio Survey, Observation

    这项 GBT L-band 定向巡天以 GREENBURST 与 VEGAS 搜索五个邻近椭圆星系的球状星团系统，结合单脉冲检索、人工候选核验、DM 预算、PATH 宿主概率与零计数似然约束磁星 FRB 率。M49 方向发现的 FRB 20240817A 具有 $DM=983\,\mathrm{pc\,cm^{-3}}$；银河、Virgo ICM 与 M49 热晕的前景电子柱留下大量 DM 余量，背景源解释得到支持。M49 方向同一低 DM 区间的低显著度脉冲聚集保留一个待跟进的重复源候选。五个星系的合并似然给出单个活跃源基准暴发率 $R_0<0.028\,\mathrm{hr^{-1}}$，压低了球状星团磁星模型的高率区域。该约束依赖球状星团数目、主波束覆盖分数和能量函数先验，扩展马赛克与更深重复观测将提高确认能力。

    <img src="./Figures/image-202609040000003.png" alt="image-202609040000003" width="680px" />
