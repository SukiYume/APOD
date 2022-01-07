## 2022-01-03

1. [Has the impact flux of small and large asteroids varied through time on Mars, the Earth and the Moon?](https://arxiv.org/abs/2112.15274)

   > Planetary Science, Solar System, Moon, Mars, Asteroid

   通常认为太阳系在过去30亿年间小行星的撞击流量是恒定的。地月系统在过去20亿年间出现撞击的峰值，可能与主带小行星碎裂相关。通过研究火星上大于20公里的521个撞击坑的大小和频率分布，表明小型（>5m）和大型（>1km）小行星的流量是耦合的`coupled`，在过去6亿年间没有发生变化。地球上在奥陶纪时期（4.7亿年）形成的大量撞击坑可能是保存偏差，月球上撞击的峰值可能是定年的不确定性导致的。

   因此得到结论，太阳系内大型（>1km）和小型（>100m）的陨石坑的产生速率是兼容的，小行星碎裂对陨石坑形成率的影响是有限的。这与传统模型一致：`Yarkovsky 效应`将小行星碎裂产生的大型碎片推向轨道共振，小型碎片通过碰撞被磨碎。

## 2022-01-04

1. [A MeerKAT, e-MERLIN, H.E.S.S. and Swift search for persistent and transient emission associated with three localised FRBs](https://arxiv.org/abs/2201.00069)

   > High Energy, Fast Radio Burst, Host Galaxy

   使用`MeerKAT`搜索非重复暴`FRB20190714A`和重复暴`FRB20190711A`和`FRB20171019A`可能存在的持续射电辐射。同时使用`H.E.S.S.`、`e-Merlin`和`Swift`在伽马射线、X射线、紫外、光学和射电波段对`FRB20171019A`进行观测，没有信号探测给出其在不同波段的辐射通量上限。

   对非重复暴`FRB20190714A`在$z=0.2365$处探测到$\sim53\ \rm mJy/beam$的峰值亮度的弥漫辐射，这可能是其宿主星系的持续辐射，是第三个有持续射电辐射的快速射电暴，表明可能是重复暴。但是`MeerKAT`对这三个快速射电暴的观测，在$0.08\rm \ Jy\cdot ms$的阈值下没有探测到重复爆发。

2. [On the period-age relation of long-period variables](https://arxiv.org/abs/2201.00201)

   > Stellar, Variables

   长周期变星存在经验上的`周期-年龄`关系，但这一关系很少有理论支撑。使用`nonlinear pulsation calculations`模拟长周期脉动变星的周期分布，与等龄线结合，观察周期和年龄的关系，并与银河系中长周期变星的观测进行比较，发现模型预测与观测一致，即**周期随年龄的增加而减小**，并且富氧和富碳的周期年龄关系有不同的斜率。

   这一关系应包含在`fundamental mode`脉动的变星都包含进来，并且由于周期分布有一定的宽度，因此使用这一关系研究单个长周期变星的年龄时需要谨慎考虑弥散。

   <img src="Figures/image-20220104170805281.png" alt="image-20220104170805281" style="zoom:50%;" />

## 2022-01-05

1. [Are the Newly-Discovered z∼13 Drop-out Sources Starburst Galaxies or Quasars?](https://arxiv.org/abs/2201.00823)

   > Extragalactic Galaxy, Cosmology

   `Harikane et al. (2021b)`探测到两个$z\sim13$的星系候选体，距离大爆炸只有$330\ \rm Myr$。研究这两个源的物理性质，包括`紫外光亮度`和`数密度`等，这两个源可能是`恒星形成星系`或者`类星体`。如果是`恒星形成星系`，则需要极高的恒星形成率，或者恒星形成率随晕质量的增加而增加，或者初始质量函数更平。如果是`类星体`，则由黑洞产生的紫外光亮度是$10^8M_\odot$，需要极大质量的黑洞，但与$z\sim7.5$的类星体所需参数一致。

2. [A comprehensive observational study of the FRB 121102 persistent radio source](https://arxiv.org/abs/2201.00999)

   > Fast Radio Burst, Extragalactic Galaxy, AGN, Radio

   使用VLA的`Ku 12-18GHz`和`K 18-26GHz`波段测量FRB121102的`PRS`的流量变化来限制其物理大小。两个波段的流量有变化可能是由于银河系的折射闪烁造成，并且要求源的大小$<10^{17}\ \rm cm$。VLA的观测发现流量变化小于闪烁理论对`PRS`的预测，说明其可能不是AGN。

   使用Keck测量$H_\alpha$，从发射线宽度估计可能存在的超大质量黑洞的质量为$<10^{4\sim5}\ M_\odot$。如果`PRS`是一个AGN，观测到的射电和X射线的光度应该对应更大质量的黑洞。另外也没有从Keck的光谱和PanSTARRS的目录中发现`PRS`相同红移的近邻星系。

   因此，没有发现任何证据支持FRB121102的`PRS`是一个AGN。

## 2022-01-06

1. [Detection of extragalactic Ultra-Compact Dwarfs and Globular Clusters using Explainable AI techniques](https://arxiv.org/abs/2201.01604)

   > Extragalactic Galaxy, Cluster, Machine Learning

   星系周围的致密恒星系统，如超致密矮星`UCDs`和球状星团`GCs`，可以用来示踪星系的合并事件。由于缺乏光谱信息，使用成像数据探测`UCDs`和`GCs`是不稳定的。这里使用`Localized Generalized Matrix Learning Vector Quantization`向量量化聚类和随机森林，并使用`Synthetic Minority Over-sampling`的方法处理样本不均匀的问题，从`Fornax`的$\rm u,g,r,i,J,Ks$六个滤光片数据中识别对象。两个方法都做到了$93\%$的查全率，并且`LGMLVQ`还可以返回不同类别不同特征的重要性。结果表明，$g-r$的颜色对聚类提供了更多的信息。

## 2022-01-07

1. [SORA: Stellar Occultation Reduction and Analysis](https://arxiv.org/abs/2201.01799)

   > Planetary Science, Solar System, Light Curve, Software

   恒星掩星可以用来确定掩星体的尺寸、形状、天体测量等信息。LSST观测预期太阳系内天体数量将增加。[SORA](https://github.com/riogroup/SORA)是用来做掩星数据归算的程序，包括从预测掩星事件以及确定天体大小、形状和位置。

## 2022-01-10

