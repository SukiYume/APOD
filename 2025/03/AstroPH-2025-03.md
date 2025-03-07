## 2025-03-03

1. [The Chinese pulsar timing array data release I. Polarimetry for 56 millisecond pulsars](https://arxiv.org/abs/2502.20820)

   > Pulsar, Polarization, PTA

   研究CPTA中的56颗毫秒脉冲星的偏振。大多数MSPs显示出较弱的成分（低于峰值流量的3%），25%的脉冲星显示出类似间脉冲的结构，大多数脉冲星显示出线性偏振位置角度跳跃。偏振百分比的分布与正常脉冲星的分布一致，表明MSPs的偏振特性与正常脉冲星相似。计算了每个脉冲星的RM和DM值，发现RM的变化可能与脉冲轮廓的频率演化有关。

   <img src="./Figures/image-20250303122416215.png" alt="image-20250303122416215" width="680px" />

## 2025-03-04



1. [The Host Galaxy of FRB 20190520B and Its Unique Ionized Gas Distribution](https://arxiv.org/abs/2503.01740)

   > Fast Radio Burst, Galaxy, Observation

   陈向蕾的文章，讲FRB 190520的宿主星系。PRS和FRB的位置位于Ha辐射的峰值，根据Ha辐射估计DM贡献为950个单位。

2. [An Unusual Change in the Radio Jets of GRS 1915+105](https://arxiv.org/abs/2503.01105)

   > High Energy, Radio, Observation

   GRS 1915+105（或称天鹰座V1487）是由一颗规则恒星和黑洞组成的X射线双星系统，“GRS”缩写自“源自GRANAT（GRANAT source）”。

   这篇文章讲VLA对这个源的观测，在1994年和2023年，发现喷流的位置角在30年间发生了偏转。认为这些突然的变化可能是由于该系统中存在一个未被发现的三级成分。

   <img src="./Figures/image-20250304131422270.png" alt="image-20250304131422270" width="680px" />

## 2025-03-05

1. [Mapping the Milky Way in 5-D with 170 Million Stars](https://arxiv.org/abs/2503.02200)

   > Stellar, Catalog

   使用[BRUTUS](https://github.com/joshspeagle/brutus)处理Pan-STARRS、2MASS、UKIDSS、unWISE和Gaia DR2的光度和天体测量数据，得到125万颗恒星的参数，建立了[Augustus](http://allsky.s3-website.us-east-2.amazonaws.com/)恒星目录。

   <img src="./Figures/image-20250305173304236.png" alt="image-20250305173304236" width="680px" />

2. [Microphysics of Circumgalactic Turbulence Probed by Fast Radio Bursts and Quasars](https://arxiv.org/abs/2503.02329)

   > Fast Radio Burst, Cosmology

   总结了通过FRBs和类星体观测来研究CGM湍流微观物理的方法。结果表明，CGM中的密度波动幅度较小，对FRB散射的贡献有限。然而，通过联合类星体和FRB观测，可以在一定程度上限制CGM湍流的耗散尺度。

3. [Constraints on the X-ray-to-radio fluence ratio of FRB 20240114A](https://arxiv.org/abs/2503.02580)

   > Fast Radio Burst, Observation, High Energy

   对FRB20240114A的射电和X射线同步观测。在2024年5月23日，使用Effelsberg探测到459次爆发，从1.3GHz到6GHz都有。X射线没找到爆发，射电最亮的流量是$1.4\times10^{-17}\,\rm erg/cm^2$，给出X射线和射电的能量比$\eta_{x/r}<1.2\times10^7$，这个值对SGR1935是$\eta_{x/r}\sim2.5\times10^5$。因此认为FRB与SGR的射电暴的机制是一致的。

## 2025-03-06

1. [Evidence for a hot galactic halo around the Andromeda Galaxy using fast radio bursts](https://arxiv.org/abs/2503.02947)

   > Fast Radio Burst, Galaxy, ISM

   使用VLA定位FRB 20230903A在红移0.09的星系，FRB 20230506C在红移0.39的星系，两个FRB都穿过M31的晕。估计了M31对DM的贡献，认为M31的需要有一个热晕才能提供足够的DM。作为M31存在热晕的间接证据。

## 2025-03-07

1. [An active repeating fast radio burst in a magnetized eruption environment](https://arxiv.org/abs/2503.04727)

   > Fast Radio Burst, Observation

   李晔的文章，FAST看fRB 20220529。

2. [Quasi-periodic oscillations of GHz-band polarization in a black hole](https://arxiv.org/abs/2503.04011)

   > Black Hole, Periodicity

   GRS 1915+105偏振流量变化，有准周期。在时间分辨率0.5s的情况下直接看时间序列。

   <img src="./Figures/image-20250307124552598.png" alt="image-20250307124552598" width="680px" />

3. [Finding White Dwarfs' Hidden Companions using an Unsupervised Machine Learning Technique](https://arxiv.org/abs/2503.04672)

   > Stellar, White Dwarf, Machine Learning

   通过Gaia CMD的颜色和天体测量选择白矮星候选体，然后使用[自组织映射SOM](https://github.com/JustGlowing/minisom/)应用到[Gaia的BP/RP光谱](https://gaia-dpci.github.io/GaiaXPy-website/)上，识别出两个主要由白矮星伴星（用SDSS和LAMOST确认的白矮星伴星数据）组成的神经元，并将其标记为白矮星伴星神经元。从这两个神经元中找到993个白矮星伴星，其中801个未被文献报道过。

   <img src="./Figures/image-20250307141055599.png" alt="image-20250307141055599" width="680px" />

   展示了SOM算法在识别Gaia XP光谱中的细微规律方面的强大能力。

4. [Magnetars](https://arxiv.org/abs/2503.04442)

   > Magnetar, Review

   磁星的综述。

   1. **磁星的定义和特性**：
      - **定义:** 磁星是一种孤立的中子星，其特征是拥有极强的磁场。
      - **发现:** 磁星最初通过其X射线和伽马射线爆发被发现，随后被识别为具有异常大X射线光度的脉冲星。
      - **能量辐射:** 磁星在不同能量带（从无线电到伽马射线）发射，表现出多种高能瞬变现象。
   2. **磁星的稳态辐射**：
      - **X射线和伽马射线:** 磁星的持续X射线辐射是其能量的主要释放方式，通常由一个或多个黑体成分和一个或多个幂律成分描述。
      - **光学和红外:** 大约三分之一的已知磁星在光学或红外波段有对应体，但其亮度较低且受银河系红化影响。
      - **无线电:** 部分磁星在无线电波段发射，显示出间歇性或突发性的爆发，通常与X射线爆发同时发生。
   3. **磁星的爆发和活动**：
      - **短爆发:** 这些是最频繁但能量最低的爆发，持续时间约为0.1-0.2秒，峰值光度为$10^{38}-10^{40}$ erg/s。
      - **中间爆发:** 持续时间介于短爆发和巨型爆发之间，光度可达$10^{41}-10^{32}$ erg/s。
      - **巨型爆发:** 这是最具能量的爆发事件之一，光度可达$10^{43}-10^{45}$ erg/s，仅记录了三次。
   4. **磁星的建模**：
      - **光谱建模:** 磁星的光谱由热辐射和复杂的磁层相互作用产生，通常使用黑体模型和幂律成分描述。
      - **磁场演化:** 磁场的演化通过欧姆耗散和霍尔效应描述，磁场衰减会影响磁星的热光度。

## 2025-03-10

