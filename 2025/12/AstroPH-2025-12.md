## 2025-12-01

1. [The Parkes Observatory Pulsar Data Archive](https://arxiv.org/abs/2511.22702)

   > Pulsar, Survey

   Parkes在过去三十年中的脉冲星观测数据档案，包含400多个项目的200万份文件。介绍了档案的当前状态，并提供了关于这些数据集的获取、分析、数据处理、可视化、保存和传播的信息。

   <img src="./Figures/image-20251201131333587.png" alt="image-20251201131333587" widht="680px"/>

## 2025-12-02

1. [Non-detection of FAST and Parkes follow-up observation for 27 Parkes discovered FRBs](https://arxiv.org/abs/2512.01281)

   > Fast Radio Burst, Observation

   对Parkes探测到的27个非重复FRB进行FAST的观测，没探测到爆发，给个事件率上限。

2. [Nested Sampling for ARIMA Model Selection in Astronomical Time-Series Analysis](https://arxiv.org/abs/2512.01929)

   > Light Curve, Method, Periodicity

   自回归积分移动平均（ARIMA）模型提供了通用的参数化，描述时间序列的随机变化。结合嵌套采样算法，在自回归（AR）和移动平均（MA）阶数的网格上进行模型选择，并能高效地推断所选模型的参数。

## 2025-12-03

1. [Padé Approximants for Fast Radio Bursts Diffuse Dispersion Measure](https://arxiv.org/abs/2512.02357)

   > Fast Radio Burst, Cosmology

   为平坦宇宙、$\Lambda\rm CDM$、$\omega\rm CDM$推导了DM的近似公式，在$0.01\le z\le2$、$0.2\le\Omega_m\le1.0$、$-3.0\le\omega\le-0.5$范围内表现良好。
   $$
   {\rm DM}_{\rm diff} = \frac{{\rm DM}_{\rm diff}^c}{\sqrt{\Omega_m}}  \Bigg( \Phi \big[ x(0, \Omega_m) \big] - \sqrt{1+z} \cdot \Phi \big[ x(z, \Omega_m) \big]  \Bigg) <= \Lambda{\rm CDM}
   $$

2. [A Statistical Analysis of Fluence and Energy Distributions of Non-repeating Fast Radio Bursts Detected by CHIME](https://arxiv.org/abs/2512.02588)

   > Fast Radio Burst, Statistics

   用 CHIME 的 415 个非重复 FRB 做了系统统计，发现它们在流量、DM、红移和能量分布上都表现出明显的多段 / 多成分结构。

3. [Search for persistent radio emission towards selected localised Fast Radio Burst positions using the MeerKAT Telescope](https://arxiv.org/abs/2512.02693)

   > Fast Radio Burst, PRS, Observation

   目前有4个FRB对应PRS（FRB20121102A、FRB20190417A、FRB20190520B 和 FRB20240114A/存疑）。用MeerKAT对25个FRB进行观测，这里介绍了其中三个的结果。

   - FRB 20221106有一个射电源，总流量在 **0.48–0.54 mJy** 左右，分辨率不足，无法区分是宿主星系的射电信号还是PRS。

     <img src="./Figures/image-20251203135441111.png" alt="image-20251203135441111" width="680px" />

   - FRB 20181112有一个弱信号，总流量从约 **0.066 mJy** 降到 **0.024 mJy**，FRB 位置完全落在射电源内部，且重合显著。

     <img src="./Figures/image-20251203135503370.png" alt="image-20251203135503370" width="680px" />

   - FRB 20190102没有PRS，给出上限。

4. [The role of the galaxy stellar mass function in determining the cosmological distribution of astrophysical transients with applications to fast radio bursts and merging binary black holes](https://arxiv.org/abs/2512.02642)

   > Fast Radio Burst, Statistics, Cosmology

   做 FRB / 合并黑洞这类宇宙瞬变体的“总体统计”时，不能只用一条随红移变化的“宇宙平均恒星形成率曲线”，还必须把“哪一类星系在产这些东西”通过星系恒星质量函数（SMF）显式放进去，否则会系统低估/误判它们的形成效率和红移分布。

## 2025-12-04

1. [Radio Detection of a Local Little Red Dot](https://arxiv.org/abs/2512.03331)

   > Galaxy, Radio, LRD

   JWST 在高红移发现了大量“小红点”星系（LRDs），这些极其致密、光谱呈 V 型且 X 射线与射电都很弱的星系，其能量来源一直在 IMBH/SMBH 强吸积模型 vs. 极端大质量恒星团模型之间摇摆。作者认为，由于高红移 LRD 太远且难以在射电波段探测，不如先在本地宇宙寻找“Local LRD”类比体，于是选择了光谱性质与 LRD 相似的两个紧致矮星系 J1025+1402 和 J1047+0739。

   <img src="./Figures/image-20251204114341969.png" alt="image-20251204114341969" width="680px" />

   在 VLA C 阵 5 GHz（2010 年）和 A 阵 6 GHz（2018 年）的档案观测中，均清晰探测到 J1047+0739 的紧致射电辐射，流量从 ~43 μJy 增长到 ~117 μJy，一颗极亮射电超新星（或其再增亮）就足以解释观测到的射电辐射和时变性。

2. [Statistical and Temporal Analysis of Multi-component Burst-clusters from the Repeating FRB 20190520B](https://arxiv.org/abs/2512.03591)

   > Fast Radio Burst, QPO

   从190520的一个爆发中探测准周期。

   <img src="./Figures/image-20251204114545890.png" alt="image-20251204114545890" width="680px" />

3. [Large Language Models for Limited Noisy Data: A Gravitational Wave Identification Study](https://arxiv.org/abs/2512.04031)

   > LLM, Gravitational Wave

   用少量引力波数据在LLM上做微调，很少的训练就能做到97.4%的准确率，额外加入56万条模拟样本不会提升在真实数据上的表现。

## 2025-12-05

1. [Minuet: A Diffusion Autoencoder for Compact Semantic Compression of Multi-Band Galaxy Images](https://arxiv.org/abs/2512.04145)

   > Galaxy, Deep Learning

   [Minuet](https://github.com/alexandergagliano/Minuet)使用基于Transformer的AutoEncoder输出的扩散模型进行图像重建，实现星系特征提取与高保真度的概率性重建。在提取的特征上，构建了一个条件流来生成基于 SED 的红移、恒星质量和恒星形成速率的后验分布。

   <img src="./Figures/image-20251205140729523.png" alt="image-20251205140729523" width="680px" />

2. [Machine Phenomenology: A Simple Equation Classifying Fast Radio Bursts](https://arxiv.org/abs/2512.04204)

   > Fast Radio Burst, Machine Learning, Symbolic Regression

   以 FRB 为例，先用深度学习和 SHAP 从 CHIME Catalog 1 的 48 个观测量里选出 6 个最关键参数，再用 Buckingham–π 量纲分析构造无量纲组合，最后交给符号回归去搜索一条能把 FRB 分成两个高斯族的简单判别方程。
   $$
   \Theta_{\rm NDR}=(\nu_p-\Delta\nu)^{0.3}\Delta t^{0.3}+\frac{\nu_p}{0.3\Delta\nu}+\alpha
   $$

## 2025-12-08

1. [A Persistently Active Fast Radio Burst source Embedded in an Expanding Supernova Remnant](https://arxiv.org/abs/2512.05448)

   > Fast Radio Burst, Observation

   190520色散下降。

2. [A new Gaia census of OB associations within 1 kpc](https://arxiv.org/abs/2512.05854)

   > Star Cluster, Statistics

   OB 星协是恒星形成和银河结构的原始示踪器。使用Gaia数据，在太阳1kpc以内的范围内，找到了25000个O型和B型恒星，使用HDBSCAN最终生成了57个OB星协目录。发现其中41个OB星协在至少一个方向上表现出显著的膨胀模式，膨胀模式是各项异性的。

   <img src="./Figures/image-20251208150927153.png" alt="image-20251208150927153" width="680px" />

   把OB星协在3D空间位置中跟Radcliffe Wave进行匹配，之前已经有工作表明 Radcliffe Wave 被 **年轻恒星、开放星团和分子云**所追踪；这篇文章补充说明：**大量大质量 OB 协会也沿着 Radcliffe Wave 排布**。

   <img src="./Figures/image-20251208150854246.png" alt="image-20251208150854246" width="680px" />

## 2025-12-09

1. [Evidence of young magnetars in massive binary embedded in a supernova remnant as sources of active fast radio bursts](https://arxiv.org/abs/2512.07140)

   > Fast Radio Burst, Theory

   从FRB190520的色散下降认为周围存在超新星遗迹，同时对比FRB121102和FRB190417的RM变化，认为重复FRB是在SNR中的年轻磁星+大质量伴星的双星系统。

   <img src="./Figures/image-20251209163246524.png" alt="image-20251209163246524" width="680px" />

2. [Back-End System of BURSTT](https://arxiv.org/abs/2512.07300)

   > Fast Radio Burst, Transient, Instrument

   BURSTT的后端介绍，通过RFSoC完成波束合成，在CPU集群进行消色散和脉冲搜索（使用的CHIME的bonsai算法进行单脉冲搜索）。在$60^\circ\times120^\circ$超大视场上实现实时波束合成、通道化和消色散搜索，并触发基带数据记录。已经可以探测到Crab的巨脉冲和PSR B0329+54的单脉冲。

   <img src="./Figures/image-20251209163700658.png" alt="image-20251209163700658" width="680px" />

3. [Revealing Hidden Repeaters in the CHIME/FRB Catalog: Semi-Supervised Insights into the Fast Radio Burst Population](https://arxiv.org/abs/2512.06316)

   > Fast Radio Burst, Statistics, Machine Learning

   基于 CHIME/FRB Catalog 与 Blinkverse 数据库，构建了一套半监督机器学习框架，用于在表面非重复FRB 中挖掘隐藏的重复源。结合UMAP降维，使用随机森林、SVM、逻辑回归、AdaBoost、Gradient Boost在有标签的已知重复源/非重复源和大量无标签事件上迭代训练。

   <img src="./Figures/image-20251209164138182.png" alt="image-20251209164138182" width="680px" />

   结果表明色散量 DM、峰值频率和辐射量是区分重复源与非重复源的主导特征，模型识别出 36 个额外的重复候选，并指出“重复 vs 非重复”的差异可能既包含物理起源，也包含观测偏差。

   <img src="./Figures/image-20251209164453025.png" alt="image-20251209164453025" width="680px" />

4. [FIP-TOI: Fast Imaging Pipeline for Pulsar Localisation with a Transient-Oriented Radio Astronomical Imager](https://arxiv.org/abs/2512.06254)

   > Radio, Transient, Software

   [FIP-TOI](https://github.com/egbdfX/SVDimager)用于干涉阵中射电暂现源的快速成像。基于奇异值分解（SVD）并在 NVIDIA GPU 上并行实现，专门针对短时间尺度、多快照宽视场成像中的 w-term 问题进行优化，实现比传统 WSClean 成像器约快十倍的定位速度（4K×4K 图像）。

## 2025-12-10

1. [Machine learning classification of baseband data of CHIME FRBs](https://arxiv.org/abs/2512.08308)

   > Fast Radio Burst, Statistics, Machine Learning

   在 12 个已知重复源和 128 个“非重复”事件组成的 baseband 样本中，作者利用 16 个物理参数进行聚类，最终在 122 个标记为非重复的 FRB 中识别出 15 个重复源候选，同时将 31 个之前工作提出的重复候选重新归类为更像非重复的事件。

   <img src="./Figures/image-20251210133443341.png" alt="image-20251210133443341" width="680px" />

   这 15 个候选中有 14 个与以往的候选列表重合，1 个是新发现，而且其中一例后来被 CHIME/FRB 证实为真正的重复源。

2. [The Milky Way Imaging Scroll Painting Survey: Data Release 1 ](https://arxiv.org/abs/2512.08260)

   > Radio, Survey

   银河画卷[数据释放](https://doi.org/10.57760/sciencedb.27351)。

   <img src="./Figures/image-20251210133646776.png" alt="image-20251210133646776" width="680px" />

## 2025-12-11

1. [Discovery of the redback millisecond pulsar PSR J1728-4608 with ASKAP](https://arxiv.org/abs/2512.09339)

   > ASKAP, Pulsar, Observation

   ASKAP发现新的 redback 脉冲星，PSR J1728-4608，周期2.86ms，轨道周期5.05小时。对食变机制的建模表明，同步吸收是造成无线电波段观测到的食变的主要原因。

## 2025-12-12

1. [Irregularity in Active Fast Radio Burst Repeaters and Magnetar Periodic Radio Pulses: Time, Energy, and Frequency Analyses](https://arxiv.org/abs/2512.10249)

   > Fast Radio Burst, Statistics

   Shotaro使用我们的方法统计FRB和磁星的另一个工作。

2. [The Space-Based Time-Domain Revolution in Astrophysics](https://arxiv.org/abs/2512.10002)

   > Light Curve, Time Domain, Review

   回顾了过去 20 年里 **空间时间域光度测量**（CoRoT、Kepler/K2、TESS 等）如何通过连续、高精度的光变曲线，改变从恒星物理到银河、河外天体和太阳系在内的几乎所有天体物理分支，包括恒星震荡、对流与颗粒噪声、恒星自转与磁活动、耀发和年轻恒星、双星、银河考古、黑洞与中子星、爆发现象、活动星系核、潮汐瓦解事件以及小行星和行星大气等方面。

## 2025-12-15

