## 2024-11-01

1. [A repeating fast radio burst source in the outskirts of a quiescent galaxy](https://arxiv.org/abs/2410.23374)

   > Fast Radio Burst, Observation

   CHIME找到新的重复FRB20240209A，在2024年2月到7月探测到22次爆发，6次被`Outrigger`记录到。66公里的基线定位单脉冲到$\rm Ra=19h19m33s,\ Dec=+86d03m52s$，误差1x2角秒。

   <img src="./Figures/image-20241101143009902.png" alt="image-20241101143009902" width="680px" />

   Gemini的光学观测发现这个位置旁边有个大星系，FRB偏离星系中心$40\pm5\,\rm kpc$，是迄今为止宿主星系偏移量最大的FRB。如果按照宿主星系大小进行归一化，这个偏离与FRB20200120E相当。考虑了几种偏移大的原因，包括FRB被踢出宿主星系或者FRB形成于低亮度卫星星系，发现最合理的情况就是起源于球状星团。

2. [The Massive and Quiescent Elliptical Host Galaxy of the Repeating Fast Radio Burst FRB20240209A](https://arxiv.org/abs/2410.23336)

   > Fast Radio Burst, Galaxy, Observation

   对FRB20240209A的宿主星系Keck和Gemini的数据分析。红移在$z=0.1384\pm0.0004$，恒星质量$\log(M_*/M_\odot)=11.34\pm0.01$，恒星群年龄$11\,\rm Gyr$，这是迄今为止发现的质量最大、年龄最大的FRB宿主，是个椭圆星系，没有恒星形成。

   <img src="./Figures/image-20241101145734213.png" alt="image-20241101145734213" width="680px" />

   这样的星系环境类似短时伽马射线暴、Ia型超新星和超亮X射线源。宿主星系的特征加上FRB与星系的巨大偏移，得出结论FRB20240209A可能来双中子星/白矮星合并、白矮星吸积引起的坍缩而形成的磁星、一个高亮度的 X 射线双星。

3. [Cosmology with Fast Radio Bursts](https://arxiv.org/abs/2410.24072)

   > Fast Radio Burst, Cosmology, Review

   介绍各种宇宙学问题，以及快速射电暴研究如何约束宇宙学参数，以及了解重子在整个宇宙中的分布。

## 2024-11-04

1. [TOPO: Time-Ordered Provable Outputs](https://arxiv.org/abs/2411.00072)

   > Astronomy, Software

   [TOPO](https://github.com/santiagocasas/topo-cobaya)是`Time-Ordered Provable Outputs`，使用`deterministic hashing`生成输出的唯一数字指纹，并使用`Merkle Trees`以时间顺序的方式存储输出。旨在提高天体物理研究中的再现性和数据完整性的工具，为数据分析盲化提供了一种无需信任的替代方案。

   使用`TOPO-cobaya`演示了TOPO在宇宙学的实用性，展示了如何将盲化和验证无缝集成到MCMC计算中，从而使该过程在密码上可证明。该方法解决了可重复性危机中的紧迫挑战，并为天体物理数据分析提供了一个强大的、可验证的框架。

## 2024-11-05

1. [Separating repeating fast radio bursts using the minimum spanning tree as an unsupervised methodology](https://arxiv.org/abs/2411.02216)

   > Fast Radio Burst, Machine Learning, Classification

   用`Minimum Spanning Tree`根据FRB的参数区分重复FRB和非重复FRB。

2. [Constraining the Hubble constant with scattering in host galaxies of fast radio bursts](https://arxiv.org/abs/2411.02249)

   > Fast Radio Burst, Cosmology

   根据FRB的散射约束宿主星系的DM贡献，进一步提升使用DM估计哈勃常数的精度，最后得到结果是$H_0=74^{+7.5}_{-7.2}\,\rm km/s/Mpc$，中心值与近邻宇宙测量一致，与CMB不太一致。

## 2024-11-06

1. [Combining strongly lensed and unlensed fast radio bursts: to be a more precise late-universe probe](https://arxiv.org/abs/2411.03126)

   > Fast Radio Burst, Cosmology

   使用透镜FRB限制哈勃常数和暗能量状态方程。

2. [Morphology of 32 Repeating Fast Radio Burst Sources at Microsecond Time Scales with CHIME/FRB](https://arxiv.org/abs/2411.02870)

   > Fast Radio Burst, Statistics, Morphology

   对CHIME/FRB基带数据的32个爆发进行了形态分析。没有发现流量、色散、事件率和爆发持续时间之间有任何的相关性。发现重复FRB比非重复FRB带宽窄且持续时间长，与之前的结果一致。另外发现，重复/非重复FRB根据爆发持续时间归一化后，sub-burst的宽度是一致的，可能表明相同的辐射机制。

   <img src="./Figures/image-20241106160658448.png" alt="image-20241106160658448" width="680px" />

3. [Accelerating FRB Search: Dataset and Methods](https://arxiv.org/abs/2411.02859)

   > Fast Radio Burst, Software

   之江的文章，斜线检测找FRB。

4. [Dispersion Measures of Fast Radio Bursts through the Epoch of Reionization](https://arxiv.org/abs/2411.02699)

   > Fast Radio Burst, Cosmology

   基于星系形成和再电离的大规模辐射-流体动力学模拟，预测FRB的DM随红一的变化，发现DM的均值和标准差随着红移的增加而增加。

## 2024-11-07

1. [Neural Network Prediction of Strong Lensing Systems with Domain Adaptation and Uncertainty Quantification](https://arxiv.org/abs/2411.03334)

   > Gravitational Lensing, Deep Learning

   使用` Mean-variance Estimators`和`unsupervised domain adaptation`结合，预测透镜参数并获得不确定性。

## 2024-11-08

1. [Astronomaly Protege: Discovery Through Human-Machine Collaboration](https://arxiv.org/abs/2411.04188)

   > Astronomy, Machine Learning, Anomaly Detection

   在[Astronomaly](https://github.com/MichelleLochner/astronomaly)基础上扩展了`Protege`，基于少量优化的人类标签，使用自监督深度学习方法`Bootstrap Your Own Latent`来找到射电星系的低维表示，在这个特征空间中找不同形态的源，异常形态的png在[这里](https://github.com/MichelleLochner/mgcls.protege)。

   <img src="./Figures/image-20241108231316981.png" alt="image-20241108231316981" width="680px" />

## 2024-11-11

1. [The Spider Stellar Engine: a Fully Steerable Extraterrestrial Design?](https://arxiv.org/abs/2411.05038)

   > SETI, Astronomy, Pulsar

   当一个文明的恒星耗尽能量时，文明不可避免地要迁移到附近的恒星。这里研究了使用Spider Pulsar作为恒星发动机，捕获附近的恒星，并在捕获后喷射其耗尽的伴星，从而实现星际旅行。

## 2024-11-12

1. [Flaring gamma-ray emission coincident with a hyperactive fast radio burst source](https://arxiv.org/abs/2411.06996)

   > Fast Radio Burst, High Energy

   余文飞的文章。从Fermi望远镜中探测到FRB20240114A的GRB。

   <img src="./Figures/image-20241112203935917.png" alt="image-20241112203935917" width="680px" />

2. [A method based on Generative Adversarial Networks for disentangling physical and chemical properties of stars in astronomical spectra](https://arxiv.org/abs/2411.05960)

   > Stellar, Spectrum, Deep Learning

   [GANDALF](https://github.com/raul-santovena/gandalf)用`encoder-decoder`结构提取APOGEE和Gaia光谱的特征，从潜空间中提取物理参数。

## 2024-11-13

1. [Physics of radio antennas](https://arxiv.org/abs/2411.07507)

   > Radio, Telescope

   讨论半波偶极子的电磁学数理基础。

## 2024-11-14

1. [Application of Machine Learning Methods for Detecting Atypical Structures in Astronomical Maps](https://arxiv.org/abs/2411.08079)

   > Astronomy, Machine Learning

   在宇宙微波背景辐射图上找非典型异常结构。

## 2024-11-15

1. [AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model](https://arxiv.org/abs/2411.09012)

   > Astronomy, LLM

   [AstroSage-Llama-3.1-8B](https://huggingface.co/AstroMLab/AstroSage-8B)使用2007-2024年间天文相关的arxiv文章，以及数百万个合成问答，基于Llama-3.1 8B模型进行训练，在 AstroMLab-1 基准测试中，AstroSage-Llama-3.1-8B 的得分率高达 80.9%。

   <img src="./Figures/image-20241116005711622.png" alt="image-20241116005711622" width="680px" />

2. [Polarization properties of 28 repeating fast radio burst sources with CHIME/FRB](https://arxiv.org/abs/2411.09045)

   > Fast Radio Burst, Polarization, Observation

   报告CHIME探测到的20个重复暴的RM测量。发现重复FRB可以分为两类，一类是RM变化，一类RM不变。

   其中FRB20180916B的RM，先平稳的随机变化、再线性变化、再平稳的随机变化。FRB20190303A和FRB20190929C的RM符号变化。

   对重复和非重复FRB的偏振对比，发现`电子密度加权的视线方向磁场`可以略微区分两种FRB。

   <img src="./Figures/image-20241116011309400.png" alt="image-20241116011309400" width="680px" />

3. [Fast Radio Bursts and Interstellar Objects](https://arxiv.org/abs/2411.09135)

   > Fast Radio Burst, Theory

   认为星际天体`interstellar objects, ISO`与中子星的碰撞是FRB产生的源头。ISO-中子星的碰撞率与FRB事件率相当，FRB持续时间与ISO的大小一致，FRB的能量分布与观测到的太阳系星体的大小分布一致。

4. [Reinvestigation of Fast Radio Bursts Host Galaxy and Event Rate Density](https://arxiv.org/abs/2411.09203)

   > Fast Radio Burst, Statistics

   统计重复和非重复FRB的宿主星系DM贡献，没发现区别。

## 2024-11-18





