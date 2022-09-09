## 2022-09-01

1. [A Semi-blind PCA-based Foreground Subtraction Method for 21 cm Intensity Mapping](https://arxiv.org/abs/2208.14675)

   > Radio, Machine Learning, PCA, HI

   PCA和SVD被广泛应用于21cm成图中前景消除。这里指出这两种方法无法完全干净地分离21cm信号和前景。这里提出一种方法`Singular Vector Projection`，使用`left/right`的`singular vectors`，可以将恢复的21cm信号误差降低几个数量级。

## 2022-09-02

1. [The ultra narrow FRB20191107B, and the origins of FRB scattering](https://arxiv.org/abs/2209.00311)

   > Fast Radio Burst, Detection

   `UTMOST`探测到`FRB 20191107B`，色散$714.9\,\rm pc/cm^{-3}$，有三个部分，持续时间非常短，最亮的部分只有$11.3\,\rm \mu s$，散射时标为$21.4\,\rm \mu s$。模拟估计，`UTMOST`可能漏掉了60%这样的窄事件。

   `FRB 20191107B`的高DM和小散射时标给IGM的湍流强度设定一个上限，量化为散射尺度$SM_{IGM}<8.4\times10^{-7}\,\rm kpc/m^{-30/2}$。与其它FRB一起做统计，没发现DM和散射之间的关联，表明IGM不是FBR散射的主要来源，因此支持以前的研究结果，即宿主星系中源的局域环境最可能主导FRB的散射。

   <img src="Figures/image-20220902155736363.png" alt="image-20220902155736363" style="zoom:80%;" />

2. [The JWST Early Release Science Program for Direct Observations of Exoplanetary Systems II: A 1 to 20 Micron Spectrum of the Planetary-Mass Companion VHS 1256-1257 b](https://arxiv.org/abs/2209.00620)

   > JWST, Exoplanet, Spectrum

   `VHS 1256b`是褐矮星伴星，很年轻，质量小于$20M_{Jup}$，轨道半径约$150AU$，与可以直接成像的系外行星`HR 8799c/d/e`有相同的光度和光谱特征。

   用JWST的NIRSpec IFU和MIRI MRS观测，覆盖$1-20\,\rm \mu m$，分辨率1000-3700。根据与模板褐矮星光谱、分子不透明度和大气模型比较，光谱中找到了水、甲烷、一氧化碳、二氧化碳、钠和钾。`VHS 1256b`的光谱形状收到了不平衡化学和云层的影响。并且第一次对行星质量的伴星探测到了硅酸盐云。

   <img src="Figures/image-20220902161811226.png" alt="image-20220902161811226" style="zoom:50%;" />

## 2022-09-05

1. [Binaries with possible compact components discovered from the LAMOST Time-Domain Survey of four K2 plates](https://arxiv.org/abs/2209.00765)

   > Stellar, Binary

   看看搞恒星的在干啥。以前不知道LAMOST还有时变光谱数据，从中可以提取时变径向速度，那么就可以找轨道周期双星了。这里找到了三个有致密天体伴星的双星系统。LAMOST中分光谱中没有双线（两个同类型恒星的发射线）、没有X射线对应体、光谱分解也没有额外的光学吸收，支持伴星是致密天体。

## 2022-09-06

美国劳动节停更。

## 2022-09-07

1. [Symmetry Breaking in Repeating Fast Radio Bursts](https://arxiv.org/abs/2209.01700)

   > Fast Radio Burst, Theory

   `sad trombone`指随时间增加频率向下漂移的的结构，这样的结构是不对称的。一些模型预测所有类似FRB180916这样的周期重复FRB都会有相同的`sign of temporal asymmetry`，一些模型预测`both signs`同样丰富。

2. [A pilot ASKAP survey for radio transients towards the Galactic Centre](https://arxiv.org/abs/2209.02352)

   > ASKAP, Radio Transient

   用ASKAP看银河系中心射电瞬变源和偏振。巡天范围由五块面积组成，每块观测12分钟，在1天到4个月的周期内重复7-9次。总共探测到8个高度可变的源和7个高度圆偏振的源，其中7个是已知脉冲星，1个事低质量X射线双星，三个与光学或红外源重合，可能是恒星，剩下三个可能与`class of Galactic Centre Radio Transients`有关。如果这类源是各向同性的，那么这项调查将会发现40个爆发。

## 2022-09-08

1. [SPARKESX: Single-dish PARKES data sets for finding the uneXpected -- A data challenge](https://arxiv.org/abs/2209.03080)

   > Radio, Dataset

   基于Parkes的模拟观测产生的数据集，作为数据挑战用于寻找未知类型天体的算法开发。数据中注入了大量模拟的信号，包括脉冲星、FRB、特征不清的信号和未知信号。数据在[这里](https://doi.org/10.25919/fd4f-0g20)。

   <img src="Figures/ParkesSparkesX.png" alt="ParkesSparkesX" style="zoom:50%;" />

2. [Classifying Transients Using Host Galaxy Photometry](https://arxiv.org/abs/2209.02784)

   > Transient, Variable, Machine Learning, Classification

   根据宿主星系的测光亮度和颜色来区分暂现源的种类，用于LSST实时报告。大致可以区分出八种暂现源种类，包括TDE、SNIa、SNIa-91bg、SNIa-91T、SNIb、SNII、SNIIn、SNIIP。数据在[这里](https://sandbox.zenodo.org/record/1086145)，代码在[这里](https://github.com/marinakiseleva/thex_model)和[这里](https://github.com/marinakiseleva/z_dist)。

## 2022-09-09

1. [High Velocity Stars in SDSS/APOGEE DR17](https://arxiv.org/abs/2209.03560)

   > Stellar, Velocity, Dynamics

   APOGEE和Gaia数据找到银心坐标系下，速度大于$450km/s$的23颗恒星，其中3颗可能不受银河引力势的约束。所有23颗都是红巨星支恒星，遵循了典型的晕星丰度模式。没有找到超高速星，但这样的结果对距离非常敏感（由于速度是距离乘出来的）。

2. [Opening the era of quasar host studies at high redshift with JWST](https://arxiv.org/abs/2209.03359)

   > Galaxy, Quasar, JWST

   从SDSS和AEGIS中选出5个$z\sim1.6-3.5$的类星体的宿主星系，然后根据HST和JWST的数据进行测光分析。结果表现出，JWST提供了探测$z>3$的类星体宿主的能力，并且能够解析$z\sim2$的形态结构（spiral arms、bar）。这些类星体的宿主是盘状的，并且缺乏合并的特征。

## 2022-09-12

