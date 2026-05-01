## 2026-04-01

1. [Your Outie Is a Wonderful Astronomer: Macrodata Refinement of the Astro-ph ArXiv Feed at Phermon Industries](https://arxiv.org/abs/2603.29771)

   > Astronomy, ArXiv, April Fools

   一篇把每天读 astro-ph 新论文这件事写成**宏观数据精炼**的愚人节论文。作者提出 [Severed Floor](https://tingyuansen.github.io/severed-floor/) 框架：研究者先做 severance，把自己切成负责上班读 arXiv 的 innie 和不必再操心 astro-ph feed 的 outie；再让这些 innie 在一个像素风虚拟楼层里按专长分论文、讨论图表、写总结邮件。论文甚至说系统已经部署，21 位天文学系成员已经被 severed，并且所有 session 都有回放归档。基本就是把日常文献跟读，包装成一套企业化、戏仿式的论文流水线。

   <img src="./Figures/image-20260401115254606.png" alt="image-20260401115254606" width="680px" />

2. [Milky Way evolution on a human timescale](https://arxiv.org/abs/2603.29503)

   > Milky Way, Galaxy Dynamics, April Fools

   也是一篇愚人节风格论文。作者假装利用几十年的银河系监测数据，去研究银河系在“人类时间尺度”上的演化，并声称银心黑洞质量、银河棒图样速度、以及太阳到银心距离，都在短短几十年里发生了“惊人的快速演化”。这篇显然是在反讽天文学里“我们只能看到一个时间切片，却总想研究长期演化”这个基本困境。

   <img src="./Figures/image-20260401115402608.png" alt="image-20260401115402608" width="680px" />

3. [Survey of compact sources for pulsars and exotic objects -- I. Overview and initial discoveries](https://arxiv.org/abs/2603.28885)

   > Pulsar, Radio Survey, Compact Source

   介绍基于射电图像先选候选体、再做脉冲搜索的 SCOPE 巡天。作者用 GMRT 和 GBT 跟进了 31 个致密且陡谱的射电源，报告发现了两颗毫秒脉冲星：J1840+1102 和 J1827-0849。前者是一颗 1.6 ms 的 MSP，位于 Scutum-Centaurus 臂边缘；后者则是此前以为“射电宁静”的伽马脉冲星对应体。论文同时也对整批样本做了形态分类和谱分析，想说明 image-based pulsar survey 也是找脉冲星的一条有效路子。

4. [AI Cosplaying as Astrophysicists: A Controlled Synthetic-Agent Study of AI-Assisted Astrophysical Research Workflows](https://arxiv.org/abs/2603.29039)

   > Astronomy, LLM, Workflow

   用“合成研究者”系统评估 LLM 到底能不能真的提升天体物理研究工作流。作者没有直接做人类实验，而是模拟了 144 个不同职业阶段、不同 AI 使用习惯的 synthetic researchers，在 2592 个日常科研任务上比较单干和 4 种 AI 辅助策略，总共跑出 12960 个 episode。结果是：没有任何一种 AI 辅助策略能在所有任务上都赢过不使用 AI；效果高度依赖任务类型、使用方式以及“研究者”本身。整体结论比较务实：AI 在抽取、创意和批判类任务上可能有帮助，但在推导密集的物理任务上仍然很脆弱。

   <img src="./Figures/image-20260401115545972.png" alt="image-20260401115545972" width="680px" />

5. [STRADAViT: Towards a Foundational Model for Radio Astronomy through Self-Supervised Transfer](https://arxiv.org/abs/2603.29660)

   > Radio Astronomy, Deep Learning, Foundation Model

   做了一个面向射电天文学图像的自监督 ViT 预训练框架 [STRADAViT](https://huggingface.co/ISSA-ML/stradavit-base)，目标是把不同巡天、不同成像流程下的射电源形态表征统一起来。作者把 MeerKAT、ASKAP、LOFAR/LoTSS 和 SKA 的 512×512 cutout 混在一起继续预训练，再在 MiraBest、LoTSS DR2 和 Radio Galaxy Zoo 上测试迁移效果。

   <img src="./Figures/image-20260401115702773.png" alt="image-20260401115702773" width="680px" />

   结果显示，两阶段 continued pretraining 的版本整体最好，在线性探测和大多数 fine-tuning 设定下都优于原始初始化；相对强基线 DINOv2，增益不是全面碾压，但在 LoTSS DR2、RGZ DR1 等任务上仍有稳定提升。

## 2026-04-02

1. [Planetary Radar at the Arecibo Observatory](https://arxiv.org/abs/2604.00332)

   > Planetary Radar, Solar System, Review

   一篇 Arecibo 行星雷达的综述，系统回顾了 Gregorian upgrade 之后这套设施对太阳系研究带来的提升。升级后灵敏度提高了约 20 倍，使它在 1997–2020 年间观测到 889 个近地小行星和彗星，而此前 30 年总共只有 40 个；同时还能穿透金星和 Titan 的大气、看进水星和月球的阴影区、并探测月球和火星浅表层。文章按天体类型总结了它在水星极区冰、金星表面、月球火山与撞击坑、火星、土星环和 Titan、以及近地小天体形状、自转、双星结构、Yarkovsky/YORP 效应等方面的关键贡献。Arecibo 行星雷达曾经是太阳系雷达观测里独一档的设施，而现在没有现役或已规划设备能完全替代它。

   <img src="./Figures/image-20260402140520049.png" alt="image-20260402140520049" width="680px" />

2. [FAST Observations of Wave-like Structures in the Radio Dynamic Spectrum of AD Leo](https://arxiv.org/abs/2604.00457)

   > Stellar Radio Burst, M Dwarf, MHD Wave

   用 FAST 高时间和高频率分辨率观测 AD Leo 的射电暴，在动态谱里发现了带有波状包络的 sub-burst train。作者看到这些窄带、短时长子暴的中心频率、频率漂移率和流量会同时以 1.53 s 的周期调制，其中中心频率与漂移率大致同相、与流量大致反相，而且频率调制振幅还会以约 2.4 s 的 e-folding 时间增长。

   <img src="./Figures/image-20260402140615484.png" alt="image-20260402140615484" width="680px" />

3. [The RRATalog: a Galactic census of rotating radio transients](https://arxiv.org/abs/2604.01203)

   > Pulsar, RRAT, Population

   构建了一个包含 335 个 RRAT 的最新目录 RRATalog，并基于 4 个 Parkes 巡天里较均一的 RRAT 样本，结合观测选择效应做银河系 RRAT 总体建模。结果表明，RRAT 的径向分布和普通脉冲星相近，但光度函数更陡，幂律指数约为 $\alpha\approx-1.3$；如果只看峰值光度高于 30 mJy kpc$^2$ 且波束指向地球的源，可观测 RRAT 数量约为 $34000\pm1600$，而考虑低光度端 turnover 后，总可观测数量应小于约 7 万个。再加上 beaming 修正，作者估计银河系 RRAT 总数小于约 50 万，对应诞生率小于约每世纪 1.4 个，与银河系核塌缩超新星率并不冲突。论文整体支持一个图景：RRAT 不是必须单独起源的一类怪源，更可能是偏长周期、偏演化后期的中子星群体。

   <img src="./Figures/image-20260402140719418.png" alt="image-20260402140719418" width="680px" />

## 2026-04-03

1. [The Real and Pseudo Dispersion Measures of FRB 20220912A](https://arxiv.org/abs/2604.01825)

   > Fast Radio Burst, Dispersion Measure, Microshot

   测量FRB20220912A的窄脉冲的DM，说明microshot 和亮窄 burst 是测真实 DM 的好工具，而很多日常 DM 拟合值其实混进了 burst 形态本身带来的假 DM。

2. [GECAM discovery of a peculiar magnetar X-ray burst (MXB 221120) from SGR J1935+2154 associated with a fast radio burst](https://arxiv.org/abs/2604.02261)

   > Magnetar, Fast Radio Burst, X-ray Burst

   报告 SGR J1935+2154 的一次特殊 X 射线暴 MXB 221120，并指出它和一次 FRB 相关联。这个事件由 GECAM-B 在 2022-11-20 触发，同时 KM40m 也探测到了和它时间相关的射电脉冲。光谱方面，这篇最特别的结果是：MXB 221120 的时间积分谱最好由单黑体拟合，温度 $kT\approx18.6$ keV，因此它成了 SGR J1935+2154 里第一例呈现热谱的 FRB 相关 MXB。

   <img src="./Figures/image-20260403130343038.png" alt="image-20260403130343038" width="680px" />

## 2026-04-06

1. [Cosmological Constraints from GW-FRB Associations without Redshift Measurements for LIGO-Virgo and Cosmic Explorer](https://arxiv.org/abs/2604.03163)

   > Fast Radio Burst, Gravitational Wave, Cosmology

   研究引力波和FRB关联事件在没有红移测量时，能不能直接用引力波给出的光度距离 + FRB给出的DM来做宇宙学约束。作者建立了一个不依赖红移的框架，并比较了当前的LIGO-Virgo和未来的Cosmic Explorer，还测试了不同IGM DM分布模型、以及是否计入宿主星系DM的影响。结论是现在的LV灵敏度还不够，基本给不出有意义的约束；但CE时代即使没有光谱红移，也能比较稳地同时约束宇宙学参数和宿主星系DM参数，所以GW-FRB联合有机会变成一类新的精密宇宙学探针。 

## 2026-04-07

1. [The VLBI spectrum of the persistent radio source associated with FRB 20190417A](https://arxiv.org/abs/2604.03429)

   > Fast Radio Burst, Persistent Radio Source, VLBI

   用 EVN 在 5 和 8 GHz 对两个重复暴 FRB 的候选持续射电源做 VLBI 观测，想确认这些源是不是毫角秒尺度上的致密非热源。

   - 在 FRB 20190417A 位置上于 5 GHz 探测到一个 unresolved 的致密源，流量约 $150\pm45,\mu$Jy，而 8 GHz 没有探测到；结合 1.4 GHz 的 VLBI 数据，得到谱指数 $\alpha=-0.19\pm0.29$，基本是平谱。这个源的亮温 $T_b\gtrsim10^{6-7}$ K，说明确实是非热辐射，而且它落在已有的 $L_\nu–|RM|$ 关系上，支持持续射电源来自年轻星云或前向激波的解释。

     <img src="./Figures/image-20260407142032038.png" alt="image-20260407142032038" width="680px" />

   - 对 FRB 20181030A，则只给出了 5 和 8 GHz 的上限。

2. [LensAgent: A Self Evolving Agent for Autonomous Physical Inference of Sub-galactic Structure.](https://arxiv.org/abs/2604.03691)

   > Strong Lensing, LLM, Dark Matter Subhalo

   提出一个不用训练数据的 LLM agent 框架 [LensAgent](https://github.com/Leo-Fengxt/LensAgent)，目标是自动完成强引力透镜里的质量分布重建和亚结构搜索。它把高层逻辑推理和确定性的物理建模工具绑在一起，用 agent loop 在模型族选择、参数优化和残差驱动的 subhalo 搜索之间反复迭代，并显式结合光谱运动学来缓解 mass-sheet degeneracy。作者把它应用到 20 个 SLACS Grade A 强透镜上，想说明这种“自进化”的 agent 架构有机会把原本高度依赖专家手工拟合的流程自动化，从而服务 LSST 和 Euclid 时代的大样本透镜宇宙学。

3. [Dispersion Measure Distribution of Unlocalized Fast Radio Bursts as a Probe of the Hubble Constant](https://arxiv.org/abs/2604.03769)

   > Fast Radio Burst, Cosmology, Hubble Constant

   不再依赖 FRB 的宿主星系定位和红移，而是直接利用**未定位 FRB 的 DM 分布**来约束哈勃常数。作者从 CHIME Catalog II 里选了 2124 个没定位FRB，建模观测 DM 分布中银河系、宿主星系和宇宙学传播的贡献，得到 $H_0=73.8^{+14.0}_{-12.3}\ {\rm km\ s^{-1}\ Mpc^{-1}}$，1σ 精度大约 18%。

4. [FRB Searches with the Irish LOFAR Station](https://arxiv.org/abs/2604.03283)

   > Fast Radio Burst, LOFAR, Low Frequency

   报告 I-LOFAR 用高频天线在 2020–2022 年间对 6 个已知 FRB 源做低频搜索的结果，总观测时长 218 小时，但在 200 MHz 以下没有找到可信的单脉冲信号。目标包括 SGR 1935+2154、FRB 20180916A、FRB 20190303A、FRB 20200120E 等。文章本质上是一篇 null-result 报告：一方面说明这些源在 I-LOFAR 灵敏度下没有稳定可见的低频爆发，另一方面把相应的相干去色散 filterbank 数据保留下来，供以后做归档研究。

5. [From NVSS to RACS: Identifying truly Compact and Steep spectrum Radio sources](https://arxiv.org/abs/2604.04577)

   > Radio Survey, Pulsar, Steep Spectrum

   用 RACS 的更高分辨率和更好灵敏度，重新检查一批在 TGSS 里致密、但在 NVSS 里没探测到的陡谱射电源候选。作者对 171 个源做图像域形态刻画后，发现其中 66 个确实是致密源，87 个其实是弥散/展宽源，另外 18 个在 RACS 和 NVSS 都没探测到，意味着谱可能陡到 $\alpha<-2$。在那 66 个致密源里，又有 34 个的谱指数比-1.5更陡。论文的核心结论是：过去很多超陡谱致密源其实是被 NVSS 在银盘附近较差的成像质量误判了；现在借助 RACS，可以更干净地筛出真正值得跟进的脉冲星、HzRG 或其他特殊射电源候选。

6. [Fast Radio Burst Dispersion Measure–Timing Cross-Correlations: Bias Self-Calibration and Primordial Non-Gaussianity Constraints](https://arxiv.org/abs/2604.04897)

   > Fast Radio Burst, Cosmology, Primordial Non-Gaussianity

   这篇研究 FRB 的 DM 场怎样拿来约束原初非高斯性 $f_{\rm NL}$，并解决 IGM 电子 bias $b_e$ 和 PNG 信号之间的退化问题。作者提出把 FRB 的 DM 场与多条视线上的 Shapiro timing delay 做互相关 $C_\ell^{D\Delta t}$：DM 追踪的是 $b_e\delta_m$，而 timing delay 直接追踪引力势、与天体物理 bias 无关，因此交叉谱可以内部自校准电子 bias。Fisher 预报表明，把这个交叉谱并入联合分析后，$\sigma(b_e^0)$ 和 $\sigma(f_{\rm NL})$ 都能明显改善，恢复到接近“已知 bias”时的理想水平。也就是说，这篇是在给 FRB 宇宙学加一个 bias self-calibration 方案，让 DM 统计更有机会碰到 inflation 留下的 PNG 信号。

## 2026-04-08

1. [Accurate polarization calibration of FAST spectral data for measurements of Zeeman splittings of OH megamasers in IRAS 02524+2046](https://arxiv.org/abs/2604.05392)

   > OH Megamaser, Polarization, Zeeman Splitting

   给FAST的19波束接收机做了一个适用于 1050–1450 MHz 的Mueller matrix偏振定标方案，把圆偏振标定精度做到约0.01% - 0.08%，明显优于只靠注入参考信号时大约0.2%的残余泄漏。定标星暴星系 IRAS 02524+2046 的OH megamaser观测，发现这个源的OH线比以前认识的更复杂：1667 MHz 发射可能跨越从 $v_{\rm helio}\sim54750$ 到 $\sim53580\ {\rm km,s^{-1}}$ 的宽速度范围，而且总功率谱里混在一起的一些窄线成分，能在圆偏振谱里被分辨出来。最终拟合出 10 个显著的 Zeeman splitting 分量，对应原位磁场大约从 -24.5 mG 到 +20.6 mG，其中大多数是正值。

   <img src="./Figures/image-20260408143358945.png" alt="image-20260408143358945" width="680px" />

2. [Great Walls of Cosmic Baryons in the Northern Sky](https://arxiv.org/abs/2604.05093)

   > Fast Radio Burst, Baryons, Large-Scale Structure

   用第二版 CHIME/FRB catalog 里的几千个 FRB，直接在北天做额外 DM天空分布图，想看看局域大尺度结构里的重子会不会在 FRB 的色散量里留下空间各向异性。在北天发现了一个最显著的 DM 过量区，位于大约 $\alpha\approx12^{\rm h}$, $\delta\approx55^\circ$，尺度约 $30^\circ$，比全局平均高出约 $150\ {\rm pc\ cm^{-3}}$，显著性超过 $4\sigma$，他们把它叫做 Wall 1；另外在 $\alpha\approx2^{\rm h}$, $\delta\approx45^\circ$ 还有一个更弱的 Wall 2。Wall 1 和 Ursa Major supercluster 一带在空间上对得上，Wall 2 则和 Perseus-Pisces supercluster 有对应关系。作者还检查了 Galactic DM 模型、银河系 halo 各向异性、抽样和 jackknife 等影响，认为这些都不足以解释 Wall 1 的信号。

   <img src="./Figures/image-20260408143517492.png" alt="image-20260408143517492" width="680px" />

## 2026-04-09

1. [No Period Change in Two Long-Period AM CVn Binaries](https://arxiv.org/abs/2604.06460)

   > AM CVn, Binary, Gravitational Wave

   对两颗长周期 AM CVn 食双星 YZ LMi 和 Gaia14aae 做长期测量，检验它们的轨道周期变化。两者的轨道周期分别约为 28.3 分钟和 49.7 分钟，观测基线分别从 2006 年和 2015 年开始。结果发现，这两个系统的 $ \dot P $ 在 $2\sigma$ 内都与 0 一致。这说明在这些较长周期的 AM CVn 系统里，并没有看到比引力波辐射强很多的额外角动量损失。

2. [Euclid Quick Data Release (Q1) AgileLens: A scalable CNN-based pipeline for strong gravitational lens identification](https://arxiv.org/abs/2604.06648)

   > Strong Lensing, CNN, Euclid

   这篇文章给 Euclid Q1 数据做了一个端到端的强引力透镜自动搜索流水线 AgileLens。流程从 VIS catalog 出发，先剔除点源、对前景透镜星系施加 $I_E\le 24$ 的星等切，再做像素级伪影/噪声过滤，构建 96×96 cutout，并把 VIS 和 NISP 合成为保留 VIS 形态、同时体现 NISP 颜色对比的彩图。模型方面，作者比较了 6 种紧凑 CNN，最后发现改造过的 VGG16 最好；再经过 3 轮迭代微调后，对最终模型排前 4000 的候选做人工分级，得到 441 个 Grade A/B 候选透镜，其中 311 个和已有 Q1 强透镜目录重合，另外还新增了 130 个此前未报告的 A/B 候选。整体上，这篇是在说明：用一个相对轻量、可扩展的 CNN 流程，就能在 Euclid 这样的超大样本里高效捞出强透镜，并且足够容易扩展到后续更大面积的数据发布。

3. [LightCurveLynx: Forward Modeling of Time-Domain Surveys with Application to ZTF SN Ia DR2](https://arxiv.org/abs/2604.07134)

   > Supernova, Simulation, Time Domain

   发布一个面向时域巡天的端到端前向模拟框架 [LightCurveLynx](https://github.com/mi-dai/lightcurvelynx_ztf_sims)，用来生成真实感较强的光变曲线模拟。这个 Python 框架是模块化的：可以从参数先验、物理模型、观测时刻与波段、观测效应到噪声模型一路往前推。作者用它做了一个 ZTF SN Ia DR2 的 Ia 型超新星模拟样本，并把模拟结果和真实数据做了细致比较。结果显示，模拟和观测在参数分布上吻合得很好，Kullback-Leibler divergence 大约在 0.01–0.02。

## 2026-04-10

1. [Detection and Evolution of Linear Polarization of the Galactic Center Transient MAXI J1744-294](https://arxiv.org/abs/2604.07431)

   > Polarization, X-ray Binary, Radio, Transient, Observation

   报告银河中心暂现源 MAXI J1744−294 的首次射电线偏振探测，并跟踪了 2025-04-04 到 04-09 四个历元的偏振演化。作者在 33 和 43 GHz 上拟合 Stokes (Q, U) 后，得到一个共同的法拉第屏,约为 $RM=-63606^{+844}_{-861}\ {\rm rad\ m^{-2}}$，是银河系里已知第三大的 RM。这个值和银河中心磁星 PSR J1745−2900 很接近，因此支持 MAXI J1744 确实位于银河中心区域、受 Sgr A* 引力束缚。作者还在 4 月 6 日看到一个额外的偏振分量，对应再多一个约 $-6000\ {\rm rad\ m^{-2}}$ 的 RM；如果把它解释成喷流里的短寿命 knot，其局域磁场大约是 15–30 G。

   <img src="./Figures/image-20260410142913985.png" alt="image-20260410142913985" width="680px" />

2. [ASTRAFier: A Novel and Scalable Transformer-based Stellar Variability Classifier](https://arxiv.org/abs/2604.07437)

   > Stellar, Variable, Transformer, TESS, Deep Learning

   提出一个新的恒星变源分类模型 [ASTRAFier](https://github.com/jeraud/TESS-Transformer)，把 Transformer、BiLSTM 和 CNN 结合起来，输入原始时序光变而不依赖手工特征工程。作者分别在 Kepler 和 TESS 光变上训练和验证，分类准确率达到 94.26% 和 88.22%。同时，他们把模型实际部署到 TESS sectors 14、15、26 的约 280 万条 QLP 光变上，并发布了对应的变星候选目录。

   <img src="./Figures/image-20260410143107071.png" alt="image-20260410143107071" width="680px" />

3. [The ZTF-ULTRASAT experiment: Characterizing the non-transients in ULTRASAT’s high cadence survey](https://arxiv.org/abs/2604.07573)

   > ULTRASAT, High-cadence Survey, Variable Star

   为了给 ULTRASAT 的高频次紫外巡天做准备，作者用 ZTF 做了一个三晚的模拟实验，观测了 5 个靠近 ULTRASAT 北天高频次场的区域，测试未来 transient 搜索里会被什么“非暂现源”污染。实时筛选一共捞出 7 个候选，其中 5 个其实是持续变源，另外 2 个是伪警报。再结合 ZTF 的 SCoPe 变源分类结果，作者发现这里面有 3 个是短周期、高振幅的 RR Lyrae，另外 2 个表现出 flare 行为。结论很直接：高频次巡天里，短时标高振幅变星很容易伪装成 transient alert，因此最好在 real-time 过滤里结合已有的机器学习变源目录，提前把这类污染压下去。

4. [The Stack Search Tests on FAST Data: Discovery of Six Faint Isolated Millisecond Pulsars in NGC 6517 and NGC 7078 (M15)](https://arxiv.org/abs/2604.08268)

   > Millisecond Pulsar, Globular Cluster, Search Method

   用 FAST 的多历元数据做 power spectrum stacking，在 NGC 6517 里找到 4 颗新 MSP（NGC 6517S–V），周期约 3.68–6.02 ms；在 M15 里找到 2 颗（M15M 和 M15N），周期约 4.83 和 9.28 ms。M15N、NGC 6517U 和 NGC 6517V 用普通 PRESTO 频域搜索和 FFA 都没找出来。

   <img src="./Figures/image-20260410143510147.png" alt="image-20260410143510147" width="680px" />

5. [Expansion kinematics of young clusters. III. The kiloparsec sample](https://arxiv.org/abs/2604.08422)

   > Young Cluster, Gaia, Kinematics

   用 Gaia DR3 五参数天体测量加上校准过的径向速度，系统研究 23 个距离 1 kpc 内、年龄小于 60 Myr 的年轻星团的空间结构和膨胀运动。作者发现，大多数年轻星团在中心区域更平滑，但稀疏外层的层级结构可以存活到 10 Myr 以上；同时，多数样本在天球面上都显示出明显膨胀，而且常常是各向异性的，这种各向异性在 30 Myr 以上的星团里仍然常见。由膨胀得到的运动学年龄和等时线年龄在小于 10 Myr 的年轻样本里通常一致，但很多年龄更老的星团显示出明显更年轻的运动学年龄。作者据此认为，这些星团大多不是由致密、单块的团簇简单膨胀而来，而更可能一开始就带有显著的空间和运动学子结构。

   <img src="./Figures/image-20260410143437029.png" alt="image-20260410143437029" width="680px" />

## 2026-04-13

1. [Radio Astronomy with the Arecibo 305m Telescope: In Contemporaneous Context](https://arxiv.org/abs/2604.08775)

   > Radio, Arecibo, Review

   文章按时间梳理了 Arecibo 在类星体时代早期射电源定位、月掩星和行星际闪烁、脉冲星与双中子星、HI 与 OH 谱线、毫秒脉冲星与系外行星、Gregorian upgrade 之后的高频观测、ALFA 巡天、SETI、VLBI 等方面的关键贡献。

2. [The Northern High Time Resolution Universe pulsar survey III. Single-pulse search continuation, follow-up observations, and initial results](https://arxiv.org/abs/2604.09080)

   > Pulsar, Single-pulse Search, FRB

   继续处理北天 HTRU 巡天里的 single-pulse 数据，目前搜索完成度约 21%，并给出了第一批结果。最亮眼的发现是 Effelsberg 100 米望远镜的第一例 FRB 20110220A，最优 DM 约 501.0 pc cm$^{-3}$，宽度 $11.9\pm3.5$ ms，流量约 $0.6\pm0.1$ Jy ms。除此之外，作者还拿到了 RRAT J2028+28 的首个 L 波段探测、发现了一颗新的 RRAT J0404+53，并找到了 8 组新的 single-pulse train 和 272 个很暗的孤立 single-pulse 候选。

   <img src="./Figures/image-20260413161003182.png" alt="image-20260413161003182" width="680px" />

3. [Radio Monitoring Campaign of Active Repeater FRB 20220912A with CHIME](https://arxiv.org/abs/2604.09098)

   > Fast Radio Burst, Repeater, Monitoring

   用 CHIME/Pulsar 对高活跃重复暴 FRB 20220912A 做了约 1.5 年的长期监测，累计约 200 小时，分析了 400–800 MHz 里 828 个 burst。结果显示，这个源在发现后大约 10 周内一直很活跃，并且等待时间分布是双峰的。环境演化方面，他们报告了一个 2.3σ 的 DM 线性增加趋势，约 $1.4\pm0.6\ {\rm pc\ cm^{-3}\ yr^{-1}}$，但 RM 没看到显著变化。

   <img src="./Figures/image-20260413161107164.png" alt="image-20260413161107164" width="680px" />

4. [Long-period transiting exoplanets: advances in detection and characterization](https://arxiv.org/abs/2604.09254)

   > Exoplanet, Transit, Review

   这是一篇关于长周期凌星系外行星的综述，重点讲过去几年在“怎么找”和“怎么做深入刻画”上的进展。相比容易发现但受恒星强烈照射的 hot Jupiter，长周期的 warm/temperate planets 更接近形成和迁移后的原始状态，因此对理解行星形成、盘迁移和轨道演化更关键。

   内容上主要包括：TESS 时代的 monotransit/duotransit 搜索方法、单次凌星如何结合恒星密度去估轨道周期、后随光谱与测光如何补全质量和半径，以及这些长周期行星在内部结构、整体金属丰度、大气成分、卫星和行星环搜索方面的科学价值。

5. [Machine Learning as a Transformative Tool for (Exo-)Planetary Science](https://arxiv.org/abs/2604.09152)

   > Exoplanet, Planetary Science, Machine Learning, Review

   这是一篇综述性质的章节，讨论机器学习怎样在行星科学和系外行星科学里变成方法学层面的基础工具。作者把应用大致分成三类挑战

   - sequence modelling，比如处理径向速度和光变这类一维时序数据
   - pattern recognition，比如用卷积网络做图像和空间模式提取、异常检测、无监督聚类
   - generative models 和 emulator-based Bayesian analysis，比如给行星内部结构、形成演化和数值模拟做快速代理模型。

   文章的重点不是提出单个新算法，而是总结 NCCR PlanetS 团队在这些方向上的代表性做法，并说明 ML 正在如何改变异构、大规模、高维数据以及高代价物理模型的处理方式。

## 2026-04-14

1. [Learning What’s Real: Disentangling Signal and Measurement Artifacts in Multi-Sensor Data, with Applications to Astrophysics](https://arxiv.org/abs/2604.09787)

   > Astronomy, Foundation Model, Representation Learning

   把“不同仪器看到的同一个天体”当成天然自监督配对，可以学到更接近真实物理的表征。作者用同一个星系被不同巡天重复观测的数据，训练一个 dual-encoder + counterfactual generation 模型：一个编码器学物理本征信息，另一个编码器学仪器系统学和噪声，再通过条件生成去重建目标图像。文章用 DESI Legacy Imaging Survey 和 HSC 的星系图像做例子，说明这种表示学习可以支持跨仪器的 counterfactual 图像生成、去除测量混淆后的参数推断，以及仪器无关的相似源检索。

   <img src="./Figures/image-20260414141741608.png" alt="image-20260414141741608" width="680px" />

2. [To understand the radiative processes of pulsars and fast radio bursts with the FAST](https://arxiv.org/abs/2604.09987)

   > Pulsar, Fast Radio Burst, Review

   这是一篇围绕 FAST 观测成果展开的综述，核心目标是借助 FAST 近年来在脉冲星和 FRB 上的突破，重新审视**相干射电辐射机制**这个老问题。文章一方面总结了 FAST 在银河面脉冲星巡天、RRAT、毫秒脉冲星、单脉冲行为、偏振和脉冲形态等方面的关键结果；另一方面也回顾了 FAST 对重复暴 FRB 的高灵敏度观测，强调 pulsar 和 FRB 两类源在单脉冲现象学上的相似性，为统一理解相干辐射物理提供了新视角。

3. [Daily Predictions of F10.7 and F30 Solar Indices with Deep Learning](https://arxiv.org/abs/2604.10045)

   > Solar, Space Weather, Deep Learning

   提出一个深度学习模型 [SINet](https://nature.njit.edu/solardb/)，做太阳 F10.7 和 F30 指数的**日尺度中期预报**，预报时长覆盖 1 到 60 天。作者使用 NOAA 以及 Toyokawa/Nobeyama 的历史数据训练模型，并把它和 5 种相关的统计或深度学习方法比较。结果显示，SINet 在 F10.7 预测上整体优于这些基线；同时它也是作者所称的第一种针对 F30 的深度学习预测方法。到第 60 天时，SINet 对 F10.7 和 F30 的平均 MAPE 分别约为 10.1% 和 9.5%。

   <img src="./Figures/image-20260414141934906.png" alt="image-20260414141934906" width="680px" />

4. [A Multi-modal Fusion Network for Star-Galaxy Classification from CSST Simulated Datasets](https://arxiv.org/abs/2604.10086)

   > Galaxy, Classification, Deep Learning, CSST

   用 CSST 模拟数据做星/系分类，并把**图像**和**测光 catalog** 两种模态融合进一个网络里。作者构建了一个包含 32,371 颗恒星和 93,525 个星系的数据集，用 ResNet-50 处理图像，用 BiLSTM 处理 catalog 特征，再在高层做特征融合。结果显示，经过 50 个 epoch 训练后，模型对星系和恒星的 recall 分别达到 99.81% 和 99.66%。作者还专门检查了数据增强和多模态融合的作用，并指出这个模型对暗弱天体和高红移星系也仍然有较高准确率。

5. [Joint Observation of SGR J1935+2154 with Insight-HXMT and KM40m during the active episode of October 2022](https://arxiv.org/abs/2604.10131)

   > Magnetar, Fast Radio Burst, X-ray Burst

   报告 2022 年 10 月 SGR J1935+2154 活跃期里，Insight-HXMT 和 KM40m 的联合观测结果。作者在两台设备重叠观测时间内一共找到了 60 个 magnetar X-ray burst，但只探测到 1 个射电脉冲；其中 2022-10-21 的一个 X 射线暴（MXB 221021）和这个射电脉冲在时间上相关联。论文强调，这个关联事件的形态与此前著名的 MXB/FRB 200428 很不一样，而且系统比较后发现，和没有射电对应体的普通 MXB 相比，MXB 221021 在时域和能谱性质上也有一些特别之处。核心意思是：磁星不是每次 X 射线暴都会伴随射电暴，而“会出射电”的那一类 X 射线暴可能本身就有不同的物理条件。

   <img src="./Figures/image-20260414142132685.png" alt="image-20260414142132685" width="680px" />

6. [Searching for Gamma Ray Bursts associated with CHIME Fast Radio bursts](https://arxiv.org/abs/2604.10629)

   > Fast Radio Burst, Gamma-Ray Burst, Association

   系统搜索 CHIME 第二版 FRB catalog 和 Swift GRB 之间是否存在时空关联。和以前只用位置误差椭圆不同，这篇直接用了 CHIME 提供的**完整 localization probability maps** 来做空间交叉匹配，因此先找到了 130 对候选体；再加上红移一致性要求后，缩减到 45 对；最后再施加一个有物理动机的时间顺序条件——要求长暴在前、短暴在后——只剩 26 对。作者用 Monte Carlo 模拟评估后发现，这些候选的总体过量并没有统计显著性，各个 localization confidence level 上的分布也和随机结果一致。结论就是：目前还看不到可靠的 FRB–GRB 总体关联信号，但这个问题很可能被定位误差和大量偶然重合淹没了。

7. [A Falsifiable Timing Test for the Double-White-Dwarf Model of Long-Period Transients](https://arxiv.org/abs/2604.11317)

   > LPT, White Dwarf Binary, Timing, Theory

   针对新近出现的长周期射电暂现源（LPT），提出一个可证伪的**双白矮星模型计时检验**。作者以 CHIME/ILT J1634+44 为例：它有 841 s 的短周期、4206 s 的长周期调制，以及显著的负周期导数，这些性质让超紧致双星解释很有吸引力。如果把 841 s 看成轨道钟、4206 s 看成 spin-orbit beat，那么这个长周期调制就不再是自由参数，而必须和轨道周期、自转周期一起随引力波损失、磁耗散和潮汐相互作用共同演化。文章估计，对 J1634 这类参数，beat 周期漂移大约有 $|\dot P_b|\sim10^{-10}\ {\rm s,s^{-1}}$，对应一年内 O-C 漂移可达几十秒。也就是说，只要后续把短周期、长周期及其导数都量准，就能对超紧致双白矮星起源做一个非常直接的 timing falsification test。

   <img src="./Figures/image-20260414142219496.png" alt="image-20260414142219496" width="680px" />

## 2026-04-15

1. [A sample of short-lived Galactic radio transients from ASKAP VAST](https://arxiv.org/abs/2604.11881)

   > Transient, ASKAP, White Dwarf Binary, Survey

   用 ASKAP 的 VAST 巡天在银河平面里系统搜索射电暂现源，最终新找到 6 个和以往 GCRT/GRT 类似的 Galactic radio transients。结合档案数据后，作者认为这些源大致可分成两类：一类是分钟级、脉冲式的 sporadic radio emission；另一类是持续数周的 flare-like outburst。论文进一步把短时变那一类和已有的 optically bright long-period radio transients 联系起来，猜测它们可能来自宽轨道白矮星双星；而长时标爆发那一类，则可能和被尘埃遮挡的白矮星双星爆发现象有关。

   <img src="./Figures/image-20260415133647479.png" alt="image-20260415133647479" width="680px" />

2. [Probing Collapsed Dark Matter Halos with Fast Radio Bursts](https://arxiv.org/abs/2604.12189)

   > Fast Radio Burst, Dark Matter, Gravitational Lensing

   这篇文章提出用 FRB 的强引力透镜效应来探测 **core-collapsed SIDM halo**。如果暗物质有自相互作用，halo 在经历 gravothermal core collapse 之后会形成比标准 CDM 更陡的中心密度分布，这会增大透镜截面，并让 FRB 多像之间的时间延迟更长。

3. [FRTSearch: Unified Detection and Parameter Inference of Fast Radio Transients using Instance Segmentation](https://arxiv.org/abs/2604.12344)

   > Fast Radio Burst, Deep Learning

   [FRTSearch](https://github.com/BinZhang109/FRTSearch)用Mask R-CNN分割动态谱中的DM信号曲线，配合 IMPIC 算法把几何轨迹坐标反推出 DM 和 ToA。结果显示，在 FAST-FREX 基准上，FRTSearch 的 recall 达到 98.0%，相比 PRESTO 的误报数降低了 99.9% 以上，同时处理速度最高快到 13.9 倍；无需重训就成功检出了 ASKAP 的 19 个测试 FRB。

   <img src="./Figures/image-20260415134343316.png" alt="image-20260415134343316" width="680px" />

4. [Gravitational Gertsenshtein–Zel’dovich mechanism for the Association between GW190425 and FRB 20190425A](https://arxiv.org/abs/2604.12775)

   > Fast Radio Burst, Gravitational Wave, Magnetar, Theory

   针对 GW190425 和 FRB 20190425A 那个 2.5 小时延迟的候选关联，提出一个替代于 “supramassive neutron star collapse” 的新物理机制。作者设想：在双中子星并合点约 2.5 光时之外，恰好有一颗 magnetar。并合产生的 kHz 引力波先到达这颗磁星，在其强磁场里通过 Gertsenshtein–Zel’dovich 效应转化成 kHz 电磁波；然后这些低频电磁波再被相对论粒子做逆康普顿散射，提升到 GHz 波段，形成观察到的 FRB。地球直接先收到 GW，另一束 GW 传播到磁星后再“转手”生成 FRB，所以自然得到约 2.5 小时延迟。

   <img src="./Figures/image-20260415134450687.png" alt="image-20260415134450687" width="680px" />

5. [The spectrum of the persistent radio source associated with FRB 20190417A](https://arxiv.org/abs/2604.12791)

   > Fast Radio Burst, Persistent Radio Source, Spectrum

   这篇文章系统测量了 FRB 20190417A 对应持续射电源的宽频谱，频率覆盖从 144 MHz 到 6 GHz。作者结合 uGMRT、VLA、VLASS 和 LoTSS 数据发现，这个 PRS 在 GHz 频段基本服从幂律谱，1–6 GHz 的谱指数约为 $\alpha = 0.20 \pm 0.05$，但在 144 MHz 没有探测到，因此把低频 turn-over 频率限制在 >370 MHz（95% 置信度）。这意味着它是一个相对平坦谱、并且在低频发生自吸收或吸收截断的源。作者将其与 magneto-ionic nebula 尤其是年轻 flaring magnetar 在超新星抛射物后方吹起的 nebula 模型进行比较，认为这种解释是相容的；在 multi-zone magnetar wind nebula 图景下，他们估计该源年龄 t<250 年、半径 R<0.4 pc。

   <img src="./Figures/image-20260415134708192.png" alt="image-20260415134708192" width="680px" />

## 2026-04-16

1. [BROOM: a python package for model-independent analysis of microwave astronomical data](https://arxiv.org/abs/2604.14088)

   > CMB, Component Separation, Software

   发布一个做微波天文数据盲源分离的 Python 包 [BROOM](https://github.com/alecarones/broom)，核心是把各种 ILC / NILC / GILC 一类的 minimum-variance 方法系统化，既能重建 CMB、SZ 和 foreground moments，也能做微波天空模拟、估计残余前景污染、计算角功率谱。

   <img src="./Figures/image-20260416131014195.png" alt="image-20260416131014195" width="680px" />

2. [The 256-antenna Coherent All-Sky Monitor](https://arxiv.org/abs/2604.13903)

   > Fast Radio Burst, Radio Instrumentation, Aperture Array

   介绍正在 OVRO 部署的 256 天线 Coherent All-Sky Monitor（CASM-256），工作在 375–500 MHz，是一个大视场、全数字、实时 GPU 处理的低频 aperture array。它的目标很明确：用大约 (10^4) 平方度的视场和较高点源灵敏度，系统寻找本地宇宙 FRB、银河系 FRB analog、脉冲星 giant pulse 以及长周期射电暂现源，并已经展示了前两打天线的 on-sky 数据和实时 FRB 搜索流水线。文章还特别强调这套思路的可扩展性，认为未来扩展到上万天线后，有机会探测到百万级 FRB。

   <img src="./Figures/image-20260416131123907.png" alt="image-20260416131123907" width="680px" />

3. [Requiem for a belt: A spatial and kinematical reinterpretation of Gould’s Belt in light of Gaia](https://arxiv.org/abs/2604.13225)

   > Gaia, Gould’s Belt, Local Structure

   用 Gaia DR3 的年轻大质量恒星和近邻年轻星团重新审视 Gould’s Belt，结论相当直接：它不像一个真实存在的、统一的、倾斜膨胀旋转环，而更像是几个星团家族——主要是 αPer、Cr135、M6 和 γVel——在本地银河环境里碰巧排成的一个 3D asterism。作者指出，经典上归因于 Gould’s Belt 的扩张、旋转和整体运动，可以由这些 cluster families 的叠加、太阳反射运动以及对 LSR 的历史假设来解释，而它那条著名的倾斜几何则很大程度上来自 Radcliffe Wave 的起伏。换句话说，这篇是在给 “Gould’s Belt 是一个物理结构” 这件事写悼词。

   <img src="./Figures/image-20260416131228022.png" alt="image-20260416131228022" width="680px" />

4. [An Information-Theoretic Metric for Transient Classification and Novelty Detection](https://arxiv.org/abs/2604.13207)

   > Rubin, Transient Classification, Information Theory

   提出一个面向 Rubin/LSST 时域科学的新 metric，用信息论里的 cross-entropy 去量化**一个新瞬变在已知瞬变总体里到底有多意外**。作者把 LSST 夜间 triplet 观测映射到离散的 observable phase space，再比较新观测和已知 transient population 的经验分布，从而同时服务几个问题：不同瞬变类之间的可分性、观测策略和 alert pipeline 的优化、稀有/新奇源的发现，以及后随资源该优先分给谁。

   <img src="./Figures/image-20260416131332181.png" alt="image-20260416131332181" width="680px" />

5. [Secular Brightness Trends of Starlink and OneWeb Satellites](https://arxiv.org/abs/2604.13145)

   > Satellite, Light Pollution, Survey Monitoring

   用 MMT9 机器人台站在 2021–2026 年间积累的约 160 万条卫星测光，研究 Starlink 和 OneWeb 在运营轨道上的长期亮度变化。结果是：Starlink VisorSat 在这五年里显著变亮了约 0.6 等，对应约每年 0.122 等；OneWeb 则显著变暗了约 0.4 等，对应约每年 0.078 等；而 Starlink V1.5 也有变亮趋势，但统计上不显著。

   <img src="./Figures/image-20260416131410898.png" alt="image-20260416131410898" width="680px" />

## 2026-04-17

1. [A fast X-ray transient with chromatic flares: signatures of violent collisions induced by late-time central engine reactivation](https://arxiv.org/abs/2604.14341)

   > Fast X-ray Transient, Central Engine, Shell Collision

   报告 Einstein Probe 发现的一例明亮河外快 X 射线暂现源 EP250302a，红移 z=1.131。后随阶段出现了一个针状的 X 射线 flare，同时光学波段却表现为更平滑的再增亮。作者据此认为，这很像两团相对论壳层在晚期发生了剧烈碰撞，其中 X 射线的尖锐 flare 和光学的平滑 bump 反映了不同辐射区和不同碰撞动力学；而这种 violent shell collision 又强烈暗示中心引擎在晚期被重新激活。

   <img src="./Figures/image-20260417133333910.png" alt="image-20260417133333910" width="680px" />

2. [Closing the Observational Gap in Cosmic Dynamics: AI-Enabled Reconstruction of the Universe’s Vorticity and Rotational Flow Morphology](https://arxiv.org/abs/2604.14653)

   > Cosmology, Vorticity, AI Reconstruction

   这篇文章尝试直接从 SDSS 星系分布里重建宇宙大尺度结构的三维速度场和涡度场，目标是补上“宇宙旋转流形态一直难以直接观测”的缺口。作者用 $\Lambda$CDM 模拟训练一个 U-Net 类深度网络，再把它应用到 SDSS DR7 星系数据上，恢复出 cluster、filament、void 里的 coherent vortical structures 和 spiral-like flows。重建结果给出的速度场、涡度场功率谱都与 $\Lambda$CDM 预测统计一致，而且用这个速度场去消除 redshift-space distortion 之后，星系聚类信号也变得接近各向同性。

   <img src="./Figures/image-20260417133413609.png" alt="image-20260417133413609" width="680px" />

3. [A Generalized Algorithmic Framework for Detecting Faraday Rotation Measure Flares in Repeating Fast Radio Bursts](https://arxiv.org/abs/2604.15012)

   > Fast Radio Burst, Rotation Measure, Algorithm

   重复暴的 RM 演化可以很平滑、也可以很混乱，再加上观测时间采样很不均匀，所以很难把真正短时、局域的 magneto-ionic 结构穿越事件，与一般性的长期漂移或随机波动区分开。为此，他们设计了一个自适应时间窗、稳健基线估计和显著性评分结合的 pipeline，用来统一识别和刻画 RM flare。把这套方法应用到 15 个 RM 有明显变化的重复暴之后，结果发现高置信 RM flare 其实非常罕见，只有 FRB 20220529A 在标准参数下显示出统计显著的事件，其他活跃源更多表现为本征大幅波动或长期 secular evolution。

## 2026-04-20

1. [Induced Scattering of Strong Waves in Pair Plasmas](https://arxiv.org/abs/2604.15798)

   > Fast Radio Burst, Plasma Physics, Theory

   研究 FRB 强电磁波在 pair plasma 里传播时的 induced scattering 问题。作者重新推导了任意振幅线偏振电磁波在 pair plasma 中的稳态解，指出真正控制非线性的不是通常的强度参数 $a_0$，而是 $a_0\omega_{\rm pe}/\omega_0$。散射饱和程度由 $a_0\omega_0/\omega_{\rm pe}$ 控制，当这个量很大时，入射波几乎不会被显著散射。对 FRB 来说，强波不一定会被磁星风中的等离子体严重散射掉，前提是频率足够高、等离子体频率足够低。

2. [Probing Primordial Black Holes with upcoming Radio Telescopes: a case study for LOFAR2.0, FAST Core Array and BINGO](https://arxiv.org/abs/2604.16154)

   > Fast Radio Burst, Primordial Black Hole, Gravitational Lensing

   用未来 FRB 样本中的引力透镜事件，预报 LOFAR2.0、FAST Core Array 和 BINGO 对原初黑洞暗物质比例$f_{\rm PBH}$的约束能力。方法上，作者把 PBH 当作点质量透镜，计算 FRB 被透镜后两个像之间的时间延迟、放大比和 survey optical depth，再结合不同望远镜的 SNR、时间分辨率和预期 FRB 数量做 forecast。结果显示，LOFAR2.0 预计可在 $M_{\rm PBH}>1M_\odot$ 处约束到$f_{\rm PBH}<0.16$；FAST Core Array 可在 $M_{\rm PBH}>10M_\odot$ 处约束到 $f_{\rm PBH}<0.39$；BINGO 则可在 $M_{\rm PBH}>10^{-2}M_\odot$ 处给出 $f_{\rm PBH}<0.39$ 量级约束。虽然这些限制不一定比现有最强约束更紧，但 FRB lensing 是独立且互补的 PBH 探针，未来随着 FRB 数量增加会更有价值。

   <img src="./Figures/image-20260420155826358.png" alt="image-20260420155826358" width="680px" />

3. [Solar Cycle Prediction: Challenges, Progress, and Future Perspectives](https://arxiv.org/abs/2604.16183)

   > Solar, Space Weather, Solar Cycle, Review

   这是一篇太阳周预测综述，系统比较了 precursor、非线性曲线拟合、统计/机器学习、dynamo 和 surface flux transport 等方法在过去太阳周上的表现。作者统计了约 100 个对 Solar Cycle 24 的预测和 130 多个对 Solar Cycle 25 的预测，结论比较悲观：多数方法都没能提前准确预测峰值，Cycle 24 往往被预测成强周期，而 Cycle 25 又常被预测成弱周期；只有在太阳周已经开始上升之后，预测才明显接近真实情况。机器学习方法的表现也不理想。文章认为，极区磁场及其 proxy 仍然是物理上最可靠的预测量，但如果在太阳极小之前太早使用，也容易出错；dynamo 和 SFT 模型正在改进，但需要更好地同化极区磁场、经向流变化等观测和物理过程。一个重要结论是：**在前一个太阳周峰值之前就预测下一个太阳周，本质上没有物理意义。**

   <img src="./Figures/image-20260420160028632.png" alt="image-20260420160028632" width="680px" />

## 2026-04-21

1. [AstroSURE: Learning to Remove Noise from Astronomical Images Without Ground Truth Data](https://arxiv.org/abs/2604.16793)

   > Astronomy Imaging, Denoising, Deep Learning

   做了一个不需要干净 ground truth 图像的天文图像去噪框架 `AstroSURE`，比较 Noise2Noise、SURE 和 blind-spot/self-supervised 类方法在低光子数天文图像上的表现。这里的去噪更适合帮助检出弱源，不等价于能直接用于精密测光、形态测量或 PSF 敏感分析。

2. [Search for galactic structures and study of their kinematics in the Gaia era](https://arxiv.org/abs/2604.16948)

   > Milky Way, Gaia, Stellar Kinematics, Review

   这是一篇 Gaia 时代银河系结构和运动学研究的简短综述，回顾了 Gaia 的视差、自行和径向速度数据怎样改变了近邻年轻星协、银河旋转、旋臂结构、Radcliffe Wave 和 phase spiral 的研究。文章特别讨论了 200 pc 内年轻星群的膨胀运动、Radcliffe Wave 的空间和速度波动、以及它是否在银河其他位置有类似物。作者指出，先前有人提出的 Carina-Sagittarius 到 Scutum arm 之间的 maser 链并不显示 Radcliffe Wave 那样明显的 $z$ 和 $V_z$ 周期扰动，因此不像是它的类似物；而 Gaia 发现的 $z-V_z$ phase spiral 则说明银河盘在过去受到过大尺度扰动，很可能和 Sagittarius 矮星系的近心通过有关。

   <img src="./Figures/image-20260421130704873.png" alt="image-20260421130704873" width="680px" />

3. [Simple approximations of some statistical functions](https://arxiv.org/abs/2604.17094)

   > Statistics, Observation Processing, Approximation

   给观测数据处理中常用的几个统计函数提供简单快速近似公式，包括标准正态分布反函数、Student (t) 分布分位数，以及离群值剔除准则里的统计阈值。

4. [Signatures of Suppressed Matter Clustering revealed by Fast Radio Bursts](https://arxiv.org/abs/2604.17162)

   > Fast Radio Burst, Baryon Feedback, Cosmology

   用有红移和 DM 的 109 个 FRB，直接约束反馈过程对小尺度物质聚集的抑制。FRB 的 cosmic DM 视线间散布来自电离气体密度涨落，而这些涨落受星系形成反馈调控，因此可以反推出 halo 气体分布和 matter power spectrum suppression。作者用 halo model 做贝叶斯推断，发现现有 FRB 样本已经能在 $k\sim0.1-3\,h\,{\rm Mpc}^{-1}$ 的尺度上对反馈强度给出约束。结果倾向于较温和的反馈，约 $2\sigma$ 排除 Illustris 和 OWLS-AGN 这类极端大尺度反馈情形。

   <img src="./Figures/image-20260421130908528.png" alt="image-20260421130908528" width="680px" />

5. [Spatio-temporal Characteristics of Very Long-periodic Pulsations in Solar Metrewave Bursts: Implications for Their Origins](https://arxiv.org/abs/2604.17724)

   > Solar Radio Burst, QPP, MHD Wave

   研究 2024-02-14 太阳米波 I 型暴链里的 very long-periodic pulsations。CBSm、DART 和 MUSER-L 同时在 210–280 MHz 附近看到 7 组重复的射电脉动结构，FFT 得到准周期约 $160^{+11}_{-6}$ s。结合 DART 成像和 SDO 观测，作者发现这些 I 型暴链位于两组太阳黑子本影上方，并由日冕环连接；黑子本影和日冕环中也能看到约 170 s 的准周期。由于这些暴链具有强圆偏振和高亮温，并且与新浮现磁通有时空相关，作者认为 I 型暴主要由 plasma emission 产生，而其中的长周期调制很可能来自黑子本影激发的 slow magnetoacoustic waves；射电暴链的频率漂移则可能反映日冕环中密度沿高度衰减。

   <img src="./Figures/image-20260421130940193.png" alt="image-20260421130940193" width="680px" />

## 2026-04-22

1. [Machine Learning Supports Existence of Previously Unrecognized Transient Astronomical Phenomena in Historical Observatory Images](https://arxiv.org/abs/2604.18799)

   > Astronomy, Transient, Historical Plate, Machine Learning, Artifact

   这篇文章研究的是 Sputnik 发射之前的历史天文底片中，那些**出现后又很快消失**的星点状暂现源到底是不是底片缺陷。作者之前声称这类暂现源在地球阴影中数量会下降（shadow deficit），并且在核试验前后一天内更容易出现（nuclear window），但这个结论一直有争议，因为反对意见认为自动管线识别出的很多暂现源只是照相底片缺陷。

   这次作者用机器学习做了一层筛选：训练集是 250 对相隔 30 分钟拍摄的暂现源图像，由专家目视标注真实源/底片缺陷”。在控制 ML 识别出的伪影之后，核试验时间窗内的暂现源数量仍然显著偏高；被模型判定为更可能真实的候选也更倾向于落在核试验时间窗内。同时，地球阴影中的暂现源缺失也仍然显著，而且在更可能真实的那部分候选中最明显。作者因此认为，历史底片中可能**确实存在一类尚未被认识的暂现现象**。

   <img src="./Figures/image-20260423115212492.png" alt="image-20260423115212492" width="680px" />

2. [White dwarf + M dwarf Detached Binaries in Long Period Radio Transients: Observed Binary Parameters, Evolution, and Population Constraints](https://arxiv.org/abs/2604.18688)

   > Long Period Radio Transient, White Dwarf, M Dwarf, Binary, Stellar Evolution

   长周期射电暂现源（LPT）是一类周期从几分钟到数小时的慢速射电脉冲源。目前已发表的 13 个 LPT 中，有两个源 ILT J1101+5521 和 GLEAM-X J0704-37 通过光学光谱与**白矮星 + M 矮星**近距双星联系起来。

   这篇文章对 ILT J1101+5521 做了新的 Keck I/LRIS 光学光谱观测，看到来自 M 矮星的 Hα 发射，并确认其轨道周期几乎等于射电周期，大约是 2.092 小时。作者还比较了 ILT J1101+5521 和 GLEAM-X J0704-37，发现两个系统的射电脉冲都大致出现在 M 矮星红移最大之后，如果射电周期就是轨道周期，这说明射电脉冲相位和双星轨道几何之间可能有稳定关系。

   两个系统都有又冷又重的白矮星，质量约 $0.84-1.0,M_\odot$，有效温度约 $5200-7300,\mathrm{K}$，意味着它们的碳氧核几乎已经高度结晶。两个系统也都很接近 face-on，倾角约 $13^\circ-28^\circ$；作者因此猜测，LPT 的相干射电脉冲产生可能强烈依赖观测倾角。

   最后作者根据这两个已知系统估计 WD+M dwarf LPT 的空间密度下限约 $\rho \gtrsim 10^{-8},\mathrm{pc}^{-3}$；如果当前射电搜索在 2 kpc 内的完备性是 100% 或 10%，那么 2 kpc 内可能分别有约 100 或 2000 个类似系统。Rubin/LSST 未来应该能看到这些系统中 M 矮星的光学对应体。

   <img src="./Figures/image-20260423115355658.png" alt="image-20260423115355658" width="680px" />

## 2026-04-23

1. [Quasi-Periodic Microstructures in Pulsar Emission: Automated Detection and Archival Survey](https://arxiv.org/abs/2604.19883)

   > Pulsar, Radio, Microstructure, Survey

   开发了 Python 工具 **QMIST**，自动从去色散的脉冲星单脉冲时间序列中搜索准周期微结构。作者用 GMRT、GBT 和 Parkes 档案数据对 27 颗脉冲星做多历元巡天，回收了已有微结构探测，并首次在 B1451−68、B1706−16、B1845−19 中发现准周期微结构；还给已知有微结构但周期不明的 B0540+23 测出典型周期。

2. [SN 2007it on the RISE -- a radio detection of an interacting supernova 18 years post-explosion](https://arxiv.org/abs/2604.20076)

   > Supernova, Radio, CSM, Multiwavelength

   RISE 项目用 ATCA 首次探测到 II 型超新星 **SN 2007it** 的射电辐射，时间是爆炸后 18 年多。2026 年 4 月 8 日在 5.5 GHz 测到 $3.30\pm0.13,{\rm mJy}$，在 9.0 GHz 测到 $3.54\pm0.24,{\rm mJy}$，谱指数约 $\alpha=0.1\pm0.2$。ASKAP 在 2026 年 1 月 11 日 0.88 GHz 没探测到，说明它可能快速增亮，或低频被内部吸收压低；后者意味着有较厚的星周物质。

   <img src="./Figures/image-20260423121844668.png" alt="image-20260423121844668" width="680px" />

3. [Neo: Photometric Super-Resolution for Improving Galaxy Morphological Measurements using Conditional Generative Adversarial Networks](https://arxiv.org/abs/2604.20195)

   > Galaxy, Deep Learning, Super-Resolution, Morphology

   提出 [Neo](https://purl.archive.org/neo/code)，一个条件 GAN，把地面 HSC 图像转换成接近 HST 质量的 6 倍超分辨率图像，用来改善星系形态参数测量。训练数据来自 COSMOS 中 HSC i-band 与 HST/ACS F814W 的重叠区域：HSC 像素尺度 0.168″、PSF FWHM 约 1.3″；HST 像素尺度 0.03″、PSF FWHM 约 0.09″。训练约 150 万个 cutout，验证约 40 万个 cutout。结果显示，Neo 生成图像在有效半径、FWHM、轴比、浓度和方向角等参数上比直接用 HSC 更接近 HST，文章概括为 2–10 倍精度提升；还展示了大图 mosaic 拼接和在 DEEP2-3 区域上的泛化。限制主要是饱和源和背景扣除不佳。

   <img src="./Figures/image-20260423181442484.png" alt="image-20260423181442484" width="680px" />

4. [Review: A new method for estimation and use of systematic errors in Poisson regression](https://arxiv.org/abs/2604.20632)

   > Statistics, Poisson Regression, Systematic Errors, X-ray Spectrum

   综述一种在 Poisson 回归中加入系统误差的方法，面向天文计数数据，尤其是 X-ray 光谱。做法是保留 Poisson 数据模型，但把模型均值 $M_i$ 当成带内禀变化的随机变量，系统误差用相对量 $f_i=\sigma_{{\rm int},i}/\hat\mu_i$ 表示；这样 Cash statistic 可推广为 $C_{\rm min,sys}$，同时估计拟合优度和系统误差水平。例子是 XMM-Newton/RGS 对 1ES 1553+113 的光谱：原始 $C_{\rm min}=1861.8$、自由度 1478，名义上拟合很差；用该方法估计平均系统误差为 $1.8\pm0.2%$，若假设 2% 系统误差，拟合的 p-value 变为 0.83。对一个候选 O VII 吸收线，$\Delta C=6.6$ 原本对应 $p=0.010$，但若有 5% 系统误差则变为 $p=0.036$，说明弱线探测需要显式考虑系统误差。

## 2026-04-24

1. [The Dyson Minds 2025 Workshop: SETI around Black Holes](https://arxiv.org/abs/2604.21886)

   > SETI, 黑洞, technosignature

   如果有非常高级的文明，不是住在行星上，而是在**超大质量黑洞附近收集能量、做超大规模计算**，那天文学家有没有可能从观测数据里把它们找出来。作者认为，最值得找的信号仍然是**废热**，也就是中红外多出来的热辐射；但不能只看这个，还应该同时留意**异常光谱、异常变光、偏振异常、X 射线掩食**之类的信号。文章最实际的建议是：用**异常检测**方法，重新筛查 WISE、JWST、EHT 等已经存在的档案数据，看看里面有没有被常规流程漏掉的异常源。

## 2026-04-27

1. [Euclid Quick Data Release (Q1). AstroVink: A vision transformer approach to find strong gravitational lens systems](https://arxiv.org/abs/2604.21977)

   > Gravitational Lensing, Vision Transformer, Deep Learning

   Euclid 里强透镜太稀少、人工筛选太慢。把 DINOv2 的 vision transformer 微调成一个叫 AstroVink 的分类器，先用模拟透镜和非透镜训练，再把 Q1 里已经确认的透镜，以及一批最容易混淆的假阳性样本加进去重训。原始模型在测试集中 top 500 能找回 88/110 个已知透镜，平均看 5.7 个候选能找到 1 个；重训后 top 500 能找回 **110/110**，效率提高到 **看 4.5 个候选就能找到 1 个透镜**。

   <img src="./Figures/image-20260427155141916.png" alt="image-20260427155141916" width="680px" />

2. [Large language models are not the problem](https://arxiv.org/abs/2604.22071)

   > LLM, Astronomy

   如果一个 LLM 真能完整复制你的科研贡献，那问题往往不在 LLM，而在这类工作本来就太机械、太依赖流水线。文中先用自己的使用方式举例：把 LLM 当成第一轮讨论对象，用来 stress-test 论证、找思路漏洞、快速摸清陌生技术；AI 辅助写代码也可以，但前提是代码最后必须经过验证、同行审阅和版本控制。她真正担心的，是让 AI 在几乎没有人类负责的情况下，自己设计、执行、写作并投稿。

   作者最后把矛头指向学术生态本身：**publish-or-perish、用发文量代替质量、学生培养被“生产力逻辑”挤压，这些问题都早在 LLM 之前就存在。** 所以她主张的不是全面禁用，而是区分“自动化科研”和“增强研究者”：前者值得警惕，后者本质上和望远镜、计算机一样，只是帮人更好地思考和工作。文章给出的实际建议也很朴素：披露 LLM 的使用方式、作者必须能解释并负责文中的分析、评价体系少看数量多看质量。**核心结论是：LLM 不是天体物理的主要威胁，它只是把原本就有的问题照得更亮。**

3. [Backlighting the Cosmic Web with Fast Radio Bursts: An Anthology of Dispersion Measure Cross-Correlations with Large-Scale Structure and Baryon Tracers](https://arxiv.org/abs/2604.22105)

   > FRB, DM, Cosmology

   这篇想把 FRB 的色散量 DM 从单个源的一条积分量变成给宇宙网做背光的统计探针：如果一条 FRB 视线穿过更多电子、更致密的环境，它的 DM 就应该系统性更大。作者用 3455 个 CHIME/FRB 源，把 DM 和十类 tracer 做角互相关，包括星系、弱透镜、CIB、CMB lensing、tSZ、X-ray 结构和射电连续谱。文中的基本写法是把 DM 涨落场写成
   $$
   D(\hat x)=\int_0^{\chi_H} d\chi, W_D(\chi),\delta_e(\hat x,\chi),
   $$
   也就是把视线上的电子密度涨落投影到天球上，再看它和各种大尺度结构 tracer 有没有一起涨。十类 probe 都看到了显著正相关，显著性大约在 2.6–5σ，例如 galaxies 是 2.8σ、weak lensing 是 2.6σ、CIB 是 4.0σ、CMB lensing 是 3.3σ、tSZ 是 3.8σ、X-ray clusters 是 5.0σ、SXRB 是 4.1σ。这说明穿过更致密环境的 FRB 视线，DM 的确更大。

4. [Variability of Sagittarius A* at 3 GHz on minute-scale with MeerKAT](https://arxiv.org/abs/2604.22638)

   > Radio, Transient, MeerKAT

   这篇想摸清 Sgr A* 在低频射电、特别是 **3 GHz 附近分钟尺度** 上怎么变，因为这个区间以前基本没被系统看过。作者用 MeerKAT 连续看了 8 小时，在 uv-domain 里做点源拟合，拿到 1 分钟分辨率的光变曲线和子频段谱指数。测到的平均流量是 $(827 \pm 0.1_{\rm stat} \pm 33_{\rm sys})$ mJy，调制度 6.11%，平均谱指数 $\alpha=0.08\pm0.03$。他们还用二阶结构函数去估计特征时间尺度，得到斜率 $0.81\pm0.05$，对应的特征时间大约120 分钟。

   更关键的是两个子频段之间测到了$826\pm97$ 秒的时延，这明显大于简单绝热膨胀模型给出的约 390–490 秒，所以作者认为**这次 3 GHz 的变光不太像单纯的绝热膨胀**。

   ## 2026-04-28

   1. [A machine learning approach to meteor classification](https://arxiv.org/abs/2604.22986)

      > Meteor, Machine Learning, Classification, Composition

      使用13个直接观测到的流星参数，对LO-CAMS 2023年的28177个高质量流星事件建立可扩展分类框架，并用GMN中的已知流星雨辅助解释结果。传统$K_b$参数只使用少数进入大气参数，这里通过因子分析和高斯混合模型从多维观测量中恢复运动学、激活阈值、尺寸和观测几何等潜在因子。

      最终给出$H_{\rm class}$硬度分类，用数据驱动方式把流星体从富铁或碳质等较硬材料到较软彗星物质排序。3、6、11类模型展示了逐渐细化的物理结构，轨道空间检查与彗星族、JFC和小行星来源的预期基本一致。配套Python实现[hcmm](https://github.com/sammmelg/hcmm)用于把GMN数据转换并应用11类模型。

      <img src="./Figures/image-20260428213859357.png" alt="image-20260428213859357" width="680px" />

   2. [Beyond the Final Label: Exploiting the Untapped Potential of Classification Histories in Astronomical Light Curve Analysis](https://arxiv.org/abs/2604.23792)

      > Light Curve, Classification, Deep Learning, LSST

      面向Rubin LSST实时警报场景，问题不是只给完整光变曲线的最终分类，而是利用分类概率随时间演化的历史。基于ELAsTiCC合成光变曲线和多个警报经纪系统输出的分类概率序列，构造输入为原始流量、五类超新星概率历史和时间特征的序列模型。

      模型采用单层LSTM加additive attention，并提出基于Wasserstein距离的早期稳定分类指标，用来评价概率分布是否更早收敛且保持准确。相对ELAsTiCC基线分类器，分类历史能提高准确率和加权F1，弱基线上的收益最明显；同时减少标签反复跳变。代码和数据在[GitHub](https://github.com/grantzzhou/LSST_beyond_the_final_label)和[Zenodo](https://zenodo.org/records/18748762)。

      <img src="./Figures/image-20260428221200085.png" alt="image-20260428221200085" width="680px" />

   3. [SCAT Data Release 1: 1810 optical spectra of 1330 transients](https://arxiv.org/abs/2604.23794)

      > Transient, Supernova, Spectroscopy, Data Release

      发布SCAT巡天第一批光谱瞬变数据，覆盖2018年3月至2023年1月的UH 2.2 m望远镜SNIFS观测。数据包括1330个瞬变源的1810条光谱，并合并公开多波段光变曲线、光变拟合、爆发或首光时间估计、峰值亮度、宿主星系匹配、红移和距离信息。

      <img src="./Figures/image-20260428221242226.png" alt="image-20260428221242226" width="680px" />

      DR1包含722个Ia型超新星、275个II型超新星、78个Ibc型超新星、48个核区瞬变、172个恒星现象和35个其他类别对象的光谱，为实时光度分类和光变分类管线提供训练和验证样本。数据发布在[Zenodo](https://zenodo.org/records/19188201)，其中包含FITS和ASCII光谱、汇总图、光变曲线和文档。

   4. [LStein: A new approach to visualizing sparse 2.5-dimensional data](https://arxiv.org/abs/2604.24034)

      > Visualization, Light Curve, Tool, Method

      提出[LStein](https://github.com/TheRedElement/LStein)，用于把稀疏2.5维数据投影到二维图中，核心动机是多波段天文光变曲线：时间和流量构成曲线，波长或通带维度稀疏采样且常被普通多面板图忽略。方法用环形扇区面板编码第三维关系，使相近通带在图上也更接近。

      与多面板、单面板和3D图比较后，LStein更适合保留通带间距、减少曲线脱离波长关系的问题，但仍建议与传统可视化结合使用。Python实现支持matplotlib和Plotly后端，可生成静态出版图或交互网页图；文档在[Read the Docs](https://lstein.readthedocs.io/en/latest/)。示例扩展到超新星光谱演化、射电脉冲星频段、机器学习超参数搜索等稀疏第三维数据。

      <img src="./Figures/image-20260428221325367.png" alt="image-20260428221325367" width="680px" />

   5. [SVOM Real-time Response and Collaboration System](https://arxiv.org/abs/2604.24265)

      > Gamma Ray Burst, SVOM, Instrument, BeiDou

      介绍SVOM任务的实时响应和协同观测系统，重点是使用北斗三号短报文服务完成卫星到地面触发告警下行，以及ToO观测指令上行。系统覆盖星上触发、北斗链路、地面接收和融合、任务规划、Swift与Einstein Probe协同观测等流程。

      首年在轨运行中，摘要给出SVOM探测172个伽马暴，并执行1040次观测，包括122次ToO EX、48次ToO MM和870次ToO NOM；结论段又写触发184个伽马暴，全文对总数存在口径差异。北斗链路使瞬变源告警可在秒级传到地面，ToO指令从接收到成功上行平均少于30分钟、最快少于2分钟，提升了多卫星联合响应效率。

      <img src="./Figures/image-20260428221410048.png" alt="image-20260428221410048" width="680px" />

   7. [StarCLR: Contrastive Learning Representation for Astronomical Light Curves](https://arxiv.org/abs/2604.24516)

      > Variable Star, Light Curve, Deep Learning, Contrastive Learning

      提出StarCLR，用对比学习为天文光变曲线学习可迁移的时间表示，减少对手工特征和单一巡天专用模型的依赖。模型是Transformer encoder，输入为观测时间和流量；预训练时从部分重叠子序列构造正样本对，在TESS前69个sector的764986条光变曲线上学习表示。

      微调阶段冻结主干，只训练分类头，并在TESS、ZTF和Gaia变星分类数据上评估。macro F1分别达到84.35%、87.82%和92.73%，相对从零训练的LSTM和Transformer在TESS、ZTF上更好，稀疏采样ZTF上的收益最明显；Gaia结果很大程度还依赖静态天体物理特征。推理代码和预训练权重在[StarCLR-Inference](https://github.com/dj-y/StarCLR-Inference)。
      
      <img src="./Figures/image-20260428221439254.png" alt="image-20260428221439254" width="680px" />

## 2026-04-29

1. [The effects of image augmentations when training machine learning models in astronomy](https://arxiv.org/abs/2604.24862)

   > Galaxy, Deep Learning, Data Augmentation

   测试天文图像分类中数据增强是否总能提高模型表现，具体任务是用Zoobot对Galaxy Zoo DECaLS星系形态进行分类。实验使用约230000张GZD 5星系图像，按80/20划分训练和测试集，并从训练集中取10%、25%、50%、100%四种规模；同一EfficientNet B0版Zoobot分别使用Original、Rotation plus Flip、Rotation、Flips、Zoom、None六种增强配置训练。

   数据增强通常有帮助，尤其在训练集较小时，不做增强的模型表现明显较差。随着训练集变大，不同合理增强方案之间差异变小，固定容量模型会接近饱和点，此后增加复杂增强主要增加训练时间，性能收益有限。

   <img src="./Figures/image-20260429151756998.png" alt="image-20260429151756998" width="680px" />

2. [Rotation Measure Substructures Induced by the Ponderomotive Force of Inertial Alfvén Waves](https://arxiv.org/abs/2604.25469)

   > Fast Radio Burst, Rotation Measure, Plasma, Theory

   解释重复FRB中短时标$RM$子结构，尤其是FRB 20201124A和FRB 20220529中叠加在长期$RM$演化上的快速下降和恢复。模型把FRB源附近环境视为低$\beta$磁化等离子体，大尺度Alfvén扰动通过湍流级联或磁重联产生惯性Alfvén波，波的ponderomotive force会把电子从波包核心排出，形成电子密度空穴。

   解析计算把密度耗尽、波电流强度、$RM$和$DM$变化联系起来，并与观测到的$RM$ dips比较。典型磁星和大质量伴星双星风参数下，约$15R_\odot$尺度的IAW湍流区可产生$\Delta RM \sim -40$到$-60\,{\rm rad\,m^{-2}}$，可解释FRB 20201124A的部分短时下降，也能覆盖FRB 20220529较大波动的一部分。

3. [Enabling real-time multi-messenger follow-up of transient events with Astro-COLIBRI](https://arxiv.org/abs/2604.25529)

   > Transient, Multi Messenger, Tool, Alert

   [Astro COLIBRI](https://astro-colibri.com/)是面向瞬变源实时跟进的平台，用于把GRB、FRB、超新星、新星、AGN flare、引力波和高能中微子等事件放入多信使、多波段上下文中。系统包含公共RESTful API、实时数据库、云端推送、网页端和iOS/Android移动端，持续监听GCN、TNS、Fink等警报流，并按用户过滤规则推送事件。

   平台界面提供时间线、事件卡片、天图、10度锥形搜索、可见性曲线、外部报告链接和ToO提交入口，也可调用tilepy为定位较差事件生成铺砖计划。数据库自2016年以来已归档超过100000个事件，主要贡献是把分散的瞬变警报、观测条件和多波段信息集中到一个可操作的跟进工具中。API文档在[这里](https://astro-colibri.science/apidoc)。

4. [Fast radio burst dispersion is an unbiased tracer of matter on large scales](https://arxiv.org/abs/2604.25828)

   > Fast Radio Burst, Cosmology, Dispersion Measure, Large Scale Structure

   论证FRB的色散量$DM$在大尺度上可作为近似无偏的物质分布示踪量。核心依据是重子数守恒：在大尺度线性区，全部重子场必须以单位bias追踪总物质场；FRB色散主要追踪弥散电离气体，而这部分包含约90%的重子，因此只需对恒星和中性气体成分做百分量级修正。

## 2026-04-30

1. [TwinSpecNet: Extending APOGEE’s chemical reach to low-S/N spectra via empirical paired learning](https://arxiv.org/abs/2604.26491)

   > Milky Way, Spectroscopy, Deep Learning, Stellar Abundance

   TwinSpecNet利用APOGEE多次观测同一恒星的特点，把低$S/N$ visit光谱和同一恒星的高$S/N$合并光谱组成经验配对样本，学习低信噪比谱中的可恢复化学信息。模型采用Vision Transformer编码器，先用320万组visit combined光谱对做去噪重建预训练，再用550354条带ASPCAP标签的visit光谱做恒星参数和丰度回归，并输出校准不确定度。在$S/N_{\rm visit}\sim20$–60区间，TSN相对visit级ASPCAP显著降低标签散布，同时保持在ASPCAP标尺上。

   <img src="./Figures/image-20260430144421000.png" alt="image-20260430144421000" width="680px" />

2. [Cosmological evolution of fast radio bursts and its rapid decline relative to star formation rate](https://arxiv.org/abs/2604.26574)

   > Fast Radio Burst, Cosmology, CHIME, Population

   使用[CHIME/FRB Catalog 2](https://zenodo.org/records/18843430)研究非重复FRB的宇宙学演化。样本从3558个一次性爆发出发，按银河系和河外$DM$贡献、流量及流量误差筛选后得到2982个FRB，并在0.2 Jy和0.5 Jy两个流量阈值下分析；红移由IllustrisTNG给出的$DM$概率分布反推伪红移，并同时测试上下限。

   通过Efron Petrosian方法校正截断效应后，FRB光度存在强红移演化，约为$L_0\propto(1+z)^{6.38}$。去演化后用Lynden Bell $C^{-}$方法得到的光度函数可由broken power law描述，断点约对应毫秒爆发能量$\sim10^{38}$ erg；共动形成率在高红移快速下降，$\rho(z)\propto(1+z)^{-5.38\pm0.02}$。该演化不直接追踪宇宙恒星形成率，更接近短伽马暴，指向带明显时延的老年族群通道。

3. [Coronal Diagnostics Via Modelling Periodic-Beaded Stripes of Solar Radio Bursts](https://arxiv.org/abs/2604.26783)

   > Solar, Radio Burst, Corona, Periodicity

   基于中国子午工程二期CBSm米波太阳射电频谱仪的高时间和频率分辨率数据，分析Type IV连续谱中的periodic beaded stripes。此类条纹多出现在耀斑后相，也可在耀斑前出现，常位于复杂磁结构附近；条纹以0.2–1.5 s周期首尾相接，单条持续0.3–2 s、带宽0.3–5 MHz，并带有约0.1 s的珠状调制和低频侧吸收。

   用double plasma resonance不稳定性的线性动理论建模链状条纹，密度和磁场的缓慢演化控制整体漂移和条纹连续性，密度或磁场扰动产生珠状结构和畸变。对5天内30组stripe chains的拟合给出源区磁场约0.2–1.7 G、电子密度约$(1$–$7)\times10^8\,{\rm cm^{-3}}$。这些结果支持多谐波upper hybrid波产生周期条纹、低频MHD波调制珠状结构的图像，并把这种精细结构转化为日冕磁场和密度诊断工具。

   <img src="./Figures/image-20260430144651621.png" alt="image-20260430144651621" width="680px" />
