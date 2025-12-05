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

