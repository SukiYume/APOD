## 2024-09-02

1. [Deep learning approach for identification of HII regions during reionization in 21-cm observations -- III. image recovery](https://arxiv.org/abs/2408.16814)

   > HI, Deep Learning

   [SERNet](https://github.com/micbia/serenet)用于SKA-low从前景污染中分离出21cm信号，从而探测在店里期间的电离区和中性区。

## 2024-09-03

今日停更。

## 2024-09-04

1. [Forecasts for Helium Reionization Detection with Fast Radio Bursts in the Era of Square Kilometre Array](https://arxiv.org/abs/2409.01543)

   > Fast Radio Burst, Cosmology

   FRB的DM和红移测量可以检测氦离子再电离。假设宇宙模型中的再电离发生在某一个特定的红移，SKA二期探测到的$10^6$个FRB可以使HeII再电离的信噪比接近$32-50\sigma$。

## 2024-09-05

1. [Rapid Automatic Multiple Moving Objects Detection Method Based on Feature Extraction from Images with Non-sidereal Tracking](https://arxiv.org/abs/2409.02405)

   > Astronomy, Deep Learning

   从光学图像中提取物体特征（中心点、形状、流量），然后标记为运动物体和恒星，用全连接网络分类特征，跟踪物体。

   <img src="./Figures/image-20240906005730157.png" alt="image-20240906005730157" width="680px" />

## 2024-09-06

1. [Asking Fast Radio Bursts (FRBs) for More than Reionization History](https://arxiv.org/abs/2409.03255)

   > Fast Radio Burst, Cosmology

   用FRB的DM测量再电离。

   在知道红移的情况下，1000个DM测量值可以区分不同的再电离模型。$\sigma(DM)/\overline{DM}$取决于电离泡的大小和再电离历史。DM的角方差（结构函数）中编码了有关再电离持续时间的和典型气泡大小的信息。

## 2024-09-09

1. [White dwarf fundamentals](https://arxiv.org/abs/2409.03941)

   > White Dwarf, Review

   文章讨论了白矮星的发现、它们作为简并天体的性质、它们与恒星演化早期阶段的联系，以及它们在逐渐冷却过程中所经历的演化。文章还描述了从白矮星致密的核心到稀薄的大气层的不同物理条件，提供了已知白矮星数量不断增加的一些关键统计数据，介绍了它们光谱的多样性、行星物质的吸积以及磁场的存在。最后，这篇文章还强调了白矮星在其他天文学领域的重要作用。

## 2024-09-10

1. [Application of Physics-Informed Neural Networks in Removing Telescope Beam Effects](https://arxiv.org/abs/2409.05718)

   > Radio, Deep Learning

   用FFT代替U-Net的一些卷积层，从干涉阵观测数据中恢复洁图。

   <img src="./Figures/image-20240911011502439.png" alt="image-20240911011502439" width="680px" />

## 2024-09-11

1. [FAST Observations of Four Comets to Search for the Molecular Line Emissions between 1.0 and 1.5 GHz Frequencies](https://arxiv.org/abs/2409.06227)

   > Radio, Comet

   用FAST对四颗彗星`C/2020 F3 (NEOWISE)`、`C/2020 R4 (ATLAS)`、`C/2021 A1 (Leonard)`、`67P/Churyumov-Gerasimenko`进行了观测，没有发现明确的分子发射信号。

## 2024-09-12

1. [Waste Heat and Habitability: Constraints from Technological Energy Consumption](https://arxiv.org/abs/2409.06737)

   > Astrobiology

   根据热力学定律，废热产生是能量转换的必然结果。在宜居行星上可能存在技术物种，特点是能源消耗和废热产生持续呈指数增长。这里发现，从能量消耗指数增长开始，此类类地行星都会在1000年的时间尺度上丧失宜居条件。

## 2024-09-13

1. [nifty-ls: Fast and Accurate Lomb-Scargle Periodograms Using a Non-Uniform FFT](https://arxiv.org/abs/2409.08090)

   > Astronomy, Periodicity, Software

   [nifty-ls](https://github.com/flatironinstitute/nifty-ls/)使用`Flatiron Institute NUFFT`加速Lomb-Scargle的非均匀FFT计算，比Astropy的实现快，并且还可以在CUDA上运行。

## 2024-09-16

1. [A Radio Technosignature Search of TRAPPIST-1 with the Allen Telescope Array](https://arxiv.org/abs/2409.08313)

   > Exoplanet, Astrobiology, SETI

   地外智慧生命处于通信或者科学的目的，可能会向他们附近的其它行星发射雷达信号。因此，从地球上看那些行星-行星掩星（PPOs）系统，就有可能探测到这些信号的溢出。

   使用窄带技术特征搜索代码[turboSETI](https://github.com/UCBerkeleySETI/turbo_seti)结合[NbeamAnalysis](https://github.com/SETIatHCRO/ATA-Utils/tree/master/NbeamAnalysis)信号过滤工具，从`Allen Telescope Array`望远镜阵列观在2022年10月底观测`TRAPPIST-1 `的0.9-9.3GHz的数据中找SETI信号，使用[NbodyGradient](https://github.com/Tusay/NbodyGradient.jl)预测行星-行星掩食的时刻，最后发现2264个信号在掩食窗口，但是没有非人类来源的信号。

   <img src="./Figures/image-20240916223500581.png" alt="image-20240916223500581" width="680px" />

## 2024-09-17

1. [Kinematic study of the Orion Complex: Analysing the young stellar clusters from big and small structures](https://arxiv.org/abs/2409.09206)

   > Stellar, Cluster, Orion, Kinematics

   在Gaia DR3的5D运动学参数空间中，用HDBSCAN对Orion的恒星进行聚类，加入APOGEE和GALAH DR3的径向速度进行运动学分析，发现Orion OB1 association在膨胀，以及$\lambda$ Orion的膨胀。

   <img src="./Figures/image-20240917191154244.png" alt="image-20240917191154244" width="680px" />

2. [Minor planets, asteroids, comets and interplanetary dust within 30 au](https://arxiv.org/abs/2409.09540)

   > Planetary Science, Solar, Asteroid

   讨论小天体群（小行星、彗星、尘埃粒子）的形成和演化。

   <img src="./Figures/image-20240917191407801.png" alt="image-20240917191407801" width="680px" />

3. [Exploring the time variability of the Solar Wind using LOFAR pulsar data](https://arxiv.org/abs/2409.09838)

   > Pulsar, DM, Solar

   用脉冲星计时阵的DM数据测量太阳风。发现1AU处的电子密度与脉冲星的黄道纬度（ELAT）之间存在很强的相关性。$\left|{\rm ELAT}\right|<3^\circ$的脉冲星的平均电子密度明显更高。我们观察到不同脉冲星的电子密度具有不同的时间模式。

   <img src="./Figures/image-20240917191746934.png" alt="image-20240917191746934" width="680px" />

4. [The CRAFT Coherent (CRACO) upgrade I: System Description and Results of the 110-ms Radio Transient Pilot Survey](https://arxiv.org/abs/2409.10316)

   > Transient, Instrument, Survey

   CRACO是ASKAP升级的暂现源巡天，寻找FRB、脉冲星和超长周期天体（ULPO）。调试阶段的时间分辨率是110ms，消多个色散，然后在$空间\times时间\times色散$空间上做boxcar来找信号。发现了两个FRB、4个脉冲星和两个新的RRAT，并通过其子脉冲结构探测到了一个已知的 ULPO，GPM J1839-10。在110ms的灵敏度是11.6 Jy ms。

   <img src="./Figures/image-20240917192435870.png" alt="image-20240917192435870" width="680px" />

   CRACO目前的时间分辨率是13.8ms，预计2024年底之前做到1.7ms的时间分辨率，灵敏度为1.5 Jy ms，可以探测到比CRAFT多10倍的FRB，也即每天0.5-2个FRB。

5. [Sherpa: An Open Source Python Fitting Package](https://arxiv.org/abs/2409.10400)

   > Astronomy, Software

   [Sherpa](https://github.com/sherpa/sherpa)是用于天文数据分析的工具，其中使用了各种统计和优化方法对数据进行拟合。

   <img src="./Figures/image-20240917193141775.png" alt="image-20240917193141775" width="680px" />

## 2024-09-18


