## 2025-11-03

1. [IrisML: Neural Posterior Estimation for the Spectral Energy Distribution fitting](https://arxiv.org/abs/2510.26964)

   > Astronomy, SED, Deep Learning

   通过Transformer将测光滤镜、观测亮度和测量不确定性压缩为一个固定大小的表示，然后使用**Masked Autoregressive Flow**估计待定参数（如温度、金属丰度）的条件概率分布。

   <img src="./Figures/image-20251103125948402.png" alt="image-20251103125948402" width="680px" />

## 2025-11-04

1. [The Variable Universe with the Gaia mission and AI methods](https://arxiv.org/abs/2511.00147)

   > Astronomy, Deep Learning

   Gaia使用深度学习找变源。

   DR1包含有限天空区域的3,194个源（两个类）；DR2有550,737颗变星（9个可变性（子）类型）；DR3列出了1050万变量（24 + 可变性（子）类型，包括950万变星和100万变AGN），还识别出250万星系。

   为DR4开发了3个VAE，分别对不同的盖亚数据产品（BP和RP平均分光光度测量、折叠的G光变曲线、光变曲线的DMDT表示）进行训练，得到15个潜在变量，用于异常检测、聚类和分类。

   [**GaiaVari+**](https://www.gaiavari.space/)是在Zooniverse平台上的公民科学项目，旨在对盖亚DR3中的部分可变源进行分类，分类依赖于基本的天文图，如时间序列、折叠光变曲线、HR/颜色 - 星等图以及在银河系中的位置。

2. [Unveiling the distribution and redshift dependence of host galaxy dispersion measures using localized fast radio bursts](https://arxiv.org/abs/2511.01195)

   > Fast Radio Burst, Galaxy, Statistics

   对FRB的星系进行统计，发现DMhost和红移有正相关。

   <img src="./Figures/image-20251104142752894.png" alt="image-20251104142752894" width="680px" />

3. [ATCAT: Astronomical Timeseries CAusal Transformer](https://arxiv.org/abs/2511.00614)

   > Light Curve, Deep Learning

   [ATCAT](https://atcat.click/)使用Transformer在ELAsTiCC v1数据集上进行训练和评估，该数据集是LSST时间序列数据的现实模拟，提高了分类准确率。

   <img src="./Figures/image-20251104143032756.png" alt="image-20251104143032756" width="680px" />

4. [BOOM and Babamul: a real-time, multi-survey, optical alert broker system operating at scale](https://arxiv.org/abs/2511.00164)

   > Astronomy, Transient, Software

   [BOOM](https://github.com/boom-astro/boom)是一个专注于实时联合多个设备警报流的分析框架，依赖于非关系型 MongoDB 数据库，结合 Valkey 内存处理队列和 Kafka 集群进行消息共享。

   <img src="./Figures/image-20251104143420262.png" alt="image-20251104143420262" width="680px" />

5. [Deconvolution for Large Astronomical Surveys: A Study of the Scaled Gradient Projection Method on Zwicky Transient Facility Data](https://arxiv.org/abs/2511.00148)

   > Astronomy, Optical, Method

   使用Scaled Gradient Projection (SGP)算法对Zwicky Transient Facility (ZTF)数据的单波段去卷积。

   <img src="./Figures/image-20251104143557668.png" alt="image-20251104143557668" width="680px" />

## 2025-11-05

1. [Using Deep Learning for Robust Classification of Fast Radio Bursts](https://arxiv.org/abs/2511.02634)

   > Fast Radio Burst, Deep Learning, Classification

   用监督变分自编码器sVAE，输入CHIME探测到的FRB的参数，结合FRB是否重复的信息，对FRB进行监督分类。

   <img src="./Figures/image-20251105155708134.png" alt="image-20251105155708134" width="680px" />

2. [Measurement of angular cross-correlation between the cosmological dispersion measure and the thermal Sunyaev--Zeldovich effect](https://arxiv.org/abs/2511.02155)

   > Fast Radio Burst, ISM

   研究了快速射电暴（FRBs）的色散测量（DMs）与热Sunyaev-Zeldovich（tSZ）效应的 Compton y 参数之间的角向交叉相关性。通过结合DMs和tSZ效应，可以分离出星系际介质（IGM）和中间星系团中的气体密度和温度。

3. [ASTROFLOW: A Real-Time End-to-End Pipeline for Radio Single-Pulse Searches](https://arxiv.org/abs/2511.02328)

   > Fast Radio Burst, Software

   [AstroFlow](https://github.com/lintian233/astroflow)用YOLOv11n从Time-DM图中检测FRB。

## 2025-11-06

1. [Exploring the spectral characteristics of the periodic burster 4U 1323-62: Type-I X-ray burst and persistent emission](https://arxiv.org/abs/2511.03172)

   > Transient, High Energy

   4U 1323-62最初由Uhuru和Ariel V任务在1970年代发现，有周期性的发射，被分类为具有爆发特性的中子星。通过NuSTAR观测4U 1323-62的持续辐射和I型X射线爆发的光谱特性。研究发现持续辐射被很好地描述为吸收的热康普顿化模型。

   <img src="./Figures/image-20251107175502272.png" alt="image-20251107175502272" width="680px" />

## 2025-11-07

1. [Cutana: A High-Performance Tool for Astronomical Image Cutout Generation at Petabyte Scale](https://arxiv.org/abs/2511.04429)

   > Astronomy, Software

   [Cutana](https://github.com/ESA/Cutana)用于在天文学图像中生成大规模的图像切块。使用欧几里得快速数据发布1（Q1）中的数据进行测试，该数据集包含63.1平方度内的3000万个源。在8个图块、1个FITS文件和200,000个源的配置下，单线程Cutana的执行速度比Astropy快2.90倍，每秒处理878.3个切块，而Astropy为303.1个。

   <img src="./Figures/image-20251107180019967.png" alt="image-20251107180019967" width="680px" />

2. [Discovery of a 9.67-s pulsar in an ultraluminous X-ray source in NGC 4631 with XMM-Newton](https://arxiv.org/abs/2511.04282)

   > Pulsar, Transient, High Energy

   使用XMM-Newton的EPIC探测器对NGC 4631星系进行观测，使用Rayleigh（Z2）测试在0.147-1000秒的周期范围内进行搜索，在X-8中发现了周期为9.6652±0.0002秒的脉动，自转加速率为$(-9.6\pm0.5)\times10^{-8}s/s$，表明该紧凑天体为中子星。

## 2025-11-10

