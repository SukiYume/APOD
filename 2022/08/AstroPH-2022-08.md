## 2022-08-01

1. [The sky at one terabit per second: Architecture and implementation of the Argus Array Hierarchical Data Processing System](https://arxiv.org/abs/2207.14304)

   > Optical, Telescope

   `Argus Optical Array`由900个20.3cm的望远镜组成，集光能力相当于全天视场的5m望远镜。高速运行时，极限星等16.1，每秒观测7916平方度，每晚产生4.3PB的数据；常速运行时，极限星等19.1，每30秒观测一次7916平方度，每晚产生145TB的数据。

   这里介绍的是数据处理系统`Argus-HDPS`，夜间产生暂现源警报以及15分钟的节奏产生整个视场全分辨率联合分析。长期光变曲线在日间进行。

2. [Inferring the Energy and Distance Distributions of Fast Radio Bursts using the First CHIME/FRB Catalog](https://arxiv.org/abs/2207.14316)

   > Fast Radio Burst

   假设$DM_{host}$是`LogNormal`，能量分布是Schechter函数，归一化系数假设与SFR有关，写了一个似然函数，从CHIME的Catlog里拟合这个函数。估计特征能量$2.38^{+5.35}_{-1.64}\times10^{41}\,\rm erg$，幂律指数$-1.3^{+0.7}_{-0.4}$。

3. [Reconnection-powered fast radio transients from coalescing neutron star binaries](https://arxiv.org/abs/2207.14435)

   > Fast Radio Burst, Theory

   这里使用`global force-free`电动力学模拟证明，两颗磁场强度远低于磁星的中子星的碰撞可以产生FRB。

   <img src="Figures/image-20220801184153038.png" alt="image-20220801184153038" style="zoom:50%;" />

## 2022-08-02

1. [Gaia Data Release 3: Summary of the content and survey properties](https://arxiv.org/abs/2208.00211)

   > Gaia, Survey

   Gaia数据集内容介绍。包含了与EDR3相同的源表、天体位置、自行、视差以及G/BP/RP测光。同时引入了大量新的数据产品，包括100万个天体的RVS光谱，2.2亿条BP/RP光谱，以及24种变星类型约1000万个天体的光变曲线分析结果。DR3包含4.7亿个天体的天体物理参数和1.5亿个天体的类别（恒星、星系和类型题）概率。超过15万个太阳系天体，从BP/RP光谱得到的6万个小行星。以及一个额外的数据集，M31的测光巡天。

2. [Limits on Fast Radio Burst-like Counterparts to Gamma-ray Bursts using CHIME/FRB](https://arxiv.org/abs/2208.00803)

   > Fast Radio Burst, GRB

   CHIME的FRB与`Swift/BAT`和`Fermi/GBM`在2018.7.17-2019.7.8之间探测到的81个GRB交叉匹配，没找到$3\sigma$以上置信度的，空间上重合、时间上相差一周内的对应体。

3. [A measurement of Hubble's Constant using Fast Radio Bursts](https://arxiv.org/abs/2208.00819)

   > Fast Radio Burst, Cosmology, Hubble Constant

   使用ASKAP定位的16个FRB和ASKAP+Parkes未定位的FRB，结合`红移-色散`关系、广度函数、气体分布、星系演化、$DM_{\rm host}$，估计哈勃常数为$73^{+12}_{-8}\,\rm km/s/Mpc$。这里估计的$DM_{\rm host}$中位数是$186^{+59}_{-48}\,\rm pc/cm^3$，比之前研究中估计的结果更大，表明FRB的宿主环境对DM的贡献比预期更大。并且此次测试证实了FRB群体演化与恒星形成率相似。

4. [J-comb: An image fusion algorithm to combine observations covering different spatial frequency ranges](https://arxiv.org/abs/2208.00588)

   > Radio, Software

   焦斯汗的文章。把地面低分辨率和空间高分辨率的射电图像组合起来。

## 2022-08-03

1. [Robust Clustering of the Local Milky Way Stellar Kinematic Substructures with Gaia eDR3](https://arxiv.org/abs/2208.01056)

   > Gaia, Clustering, Structure

   `HDBSCAN`用在Gaia EDR3找太阳系附近的运动亚结构，并提供一个稳定的聚类目录。

## 2022-08-04

1. [The Sparkler: Evolved High-Redshift Globular Clusters Captured by JWST](https://arxiv.org/abs/2208.02233)

   > JWST, Galaxy, Globular Cluster

   研究被`SMACS J0723.3-7327`星系团`lensing`的星系`Sparkler`，周围的致密源`sparkles`。在JWST/NIRCam中没有空间分辨，在JWST/NIRISS光谱中有`OIII`的发射，但是没有恒星形成的迹象，认为这些星团是在$z=1.378$的`evolved`球状星团，SED拟合年龄大约是$3.9-4.1Gyr$，在大爆炸后0.5Gyr形成。如果被证实，这些星团可能是宇宙中最早被观测到的停止恒星形成的天体之一。

   <img src="Figures/image-20220804171740326.png" alt="image-20220804171740326" style="zoom:50%;" />

## 2022-08-05

1. [Sensitive Multi-beam Targeted SETI Observations towards 33 Exoplanet Systems with FAST](https://arxiv.org/abs/2208.02421)

   > SETI, Exoplanet

   张同杰他们的文章。FAST的SETI终端看系外行星，找到1140MHz的频漂信号，特征与假定的ETI技术特征一致，但是偏振特征排除其是地外信号的可能性。

   <img src="Figures/image-20220805143032311.png" alt="image-20220805143032311" style="zoom:50%;" />

## 2022-08-08

