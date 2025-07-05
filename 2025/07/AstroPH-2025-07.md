## 2025-07-01

1. [Constraining the Origin of FRB 20121102A's Persistent Radio Source with Long-Term Radio Observations](https://arxiv.org/abs/2506.23861)

   > Fast Radio Burst, PRS, Observation

   uGMRT在2023年对FRB121102的PRS的观测，结合了其他望远镜的数据。发现PRS在L波段和745MHz的流量没有显著的长期变化，其流量变化完全可以由星际闪烁解释，在400MHz没有探测到PRS。

   <img src="./Figures/image-20250701153328809.png" alt="image-20250701153328809" width="680px" />

   磁星风星云模型和超星云模型在解释PRS的长期演化时存在困难，而低光度活动星系核模型则与观测结果较为一致。

2. [An investigation into correlations between FRB and host galaxy properties](https://arxiv.org/abs/2506.23403)

   > Fast Radio Burst, Galaxy, Statistics

   统计ASKAP的FRB与宿主星系属性的关系。

   - 发现散射时间尺度与恒星面密度、质量加权年龄和气体相金属丰度显著相关。致密的宿主星系可能具有更多的电离物质，导致更强的散射。

     <img src="./Figures/image-20250701153624231.png" alt="image-20250701153624231" width="680px" />

   - RM与宿主星系的光盘轴比b/a之间存在强反相关，表明边缘朝向的宿主星系可能使FRB通过更多的星系介质，从而增加RM值。

     <img src="./Figures/image-20250701153643329.png" alt="image-20250701153643329" width="680px" />

   - 圆极化分数与宿主星系的有效半径呈弱负相关，但这一结果主要受一个数据点的影响。

     <img src="./Figures/image-20250701153658943.png" alt="image-20250701153658943" width="680px" />

## 2025-07-02

1. [The radiative subpulse modulation and spectral features of PSR B1929+10 with the whole pulse phase emission](https://arxiv.org/abs/2507.00610)

   > Pulsar, Observation

   FAST对PSR B1929+10的观测，发现其在整个360°经度范围内都有辐射，表明其为全经度辐射脉冲星。

   平均脉冲轮廓中至少检测到15个辐射成分。强辐射成分（主脉冲和中间脉冲）的光谱指数较平，小于1.7；而弱辐射成分的光谱指数较陡，大于2.3。

   在单脉冲中检测到窄带辐射特征和线性偏振位置角（PPA）的频繁跳变。通过旋转矢量模型（RVM）拟合观测到的PPA变化，得到脉冲星的倾角α为55.62°，撞击角β为53.47°。

2. [An outer-disk SX Phe variable star in Rubin Data Preview 1](https://arxiv.org/abs/2507.00192)

   > Variable, Stellar, Light Curve, Periodicity

   在LSST Data Preview 1中发现一颗SX Phoenicis型脉动变星。

   <img src="./Figures/image-20250702133402471.png" alt="image-20250702133402471" width="680px" />

   计算DP1数据g和r波段的StetsonJ、IQR和Chi2值，使用IsolationForest进行异常检测，筛选出前10个异常对象。使用[Psearch](https://github.com/AbhijitSaha/Psearch)结合Lomb-Scargle周期图和相位离散最小化（2025-06-19/3）来找周期，最终确定了一颗周期为0.0767天（1.841小时）的变星，其g和r波段的脉动幅度分别为0.60和0.38星等。

   Psearch中实现了另一种周期搜索的方法，Lafler–Kinman，使用不同周期对光变曲线$(t_i,m_i)$进行折叠
   $$
   \phi_i=\frac{t_i\mod P}{P}
   $$
   然后按照相位进行排序，计算散度统计量
   $$
   \Theta(P)=\frac{\sum_{i=1}^N(m_{i+1}-m_i)^2+(m_1-m_N)^2}{\sum_{i=1}^N(m_i-\bar m)^2}
   $$
   相邻相位点差异越小，折线越平滑，$\Theta$越小。真实周期对应其最小值。

   - Lafler–Kinman 不分箱，直接按相位连成一条“折线”，度量这条折线的“长度”或“弯曲程度”。适合数据点较少、但噪声不太严重的情况。
   - PDM 则先把相位区间分箱，对每个箱内的离散度做统计，对箱大小和箱数比较敏感，但对异常点和采样不均匀更鲁棒一些。

3. [A period-increasing oscillation signal in a long gamma-ray burst](https://arxiv.org/abs/2507.00873)

   > High Energy, Periodicity, QPO

   在长伽马射线暴GRB131122B中观测到的一个周期逐渐增加的振荡信号。从Fermi/GBM、Swift/BAT和CGRO/BATSE等探测器记录的光曲线中视觉筛选GRB，使用0.2Hz和2.0Hz两个特征频率+Tukey窗口对光变曲线进行带通滤波，对滤波后的光曲线进行WWZ变换，发现频率随时间递减。

   <img src="./Figures/image-20250702140740914.png" alt="image-20250702140740914" width="680px" />

## 2025-07-03

1. [Calibrating DM_IGM - z relation using host galaxies of FRBs](https://arxiv.org/abs/2507.01270)

   > Fast Radio Burst, Statistics, Cosmology

   通过SED+Sersic拟合FRB宿主星系的参数，发现河外部分DM与sSFR正相关，根据此来校准Macquart（DM-z）关系。

   <img src="./Figures/image-20250703191632832.png" alt="image-20250703191632832" width="680px" />

2. [LIGHTS. A robust technique to identify galaxy edges](https://arxiv.org/abs/2507.01085)

   > Galaxy, Method

   提出一种稳健的找星系边缘的方法。通过SED或者颜色组合推导出星系的表面质量密度图，然后做密度图的二阶导，找到曲率变化最小的点，作为星系边缘。

   <img src="./Figures/image-20250703191935845.png" alt="image-20250703191935845" width="680px" />

3. [Meteoroid stream identification with HDBSCAN unsupervised clustering algorithm](https://arxiv.org/abs/2507.01501)

   > Meteoroid, Machine Learning

   CAMS流星体轨道数据库v3.0，包含471,582条流星轨道记录。定义了三种输入特征向量用于聚类：

   - **LUTAB向量**：基于CAMS查找表的四个参数，包括太阳黄道经度、太阳中心黄道辐射坐标、地球中心速度和辐射纬度。
   - **ORBIT向量**：基于五个日心轨道元素，包括近日点距离、偏心率、倾角、升交点和近地点角。
   - **GEO向量**：基于六个地球中心参数，包括太阳黄道经度、升交点余弦、升交点正弦、辐射余弦、辐射正弦和地球中心速度除以72。

   使用HDBSCAN进行聚类，使用轮廓系数、归一化互信息（NMI）和F1分数评估聚类性能，并通过主成分分析（PCA）支持分析。结果使用GEO向量时，HDBSCAN确认了39个流星体流，其中21个与CAMS高度匹配；使用ORBIT向量时，识别出30个流星体流，其中13个匹配度高。

   <img src="./Figures/image-20250703192309556.png" alt="image-20250703192309556" width="680px" />

4. [SpecCLIP: Aligning and Translating Spectroscopic Measurements for Stars](https://arxiv.org/abs/2507.01939)

   > Stellar, Spectrum, Deep Learning

   SpecCLIP用于解决恒星光谱分析中的对齐和翻译问题。在LAMOST低分辨率光谱上进行预训练，经过6个自注意力层处理后，得到一个768维的标记嵌入。Gaia XP光谱则使用一个简单的多层感知器（MLP）自编码器进行预训练。然后使用CLIP的方法进行对比学习。预测恒星参数。

   <img src="./Figures/image-20250703192745364.png" alt="image-20250703192745364" width="680px" />

## 2025-07-04

1. [Multi-year Polarimetric Monitoring of Four CHIME-Discovered Repeating Fast Radio Bursts with FAST](https://arxiv.org/abs/2507.02355)

   > Fast Radio Burst, Observation

   冯毅的文章，FAST观测4个重复FRB的偏振。

2. [Envisioning the Distance Ladder in the Era of the Habitable Worlds Observatory](https://arxiv.org/abs/2507.02056)

   > Stellar, Cosmology

   在哈勃常数测量中，利用即将推出的宜居世界天文台（Habitable Worlds Observatory, HWO）构建一个两步距离阶梯的可能性，以消除对Ia型超新星的依赖，并实现1%精度的H0测量。

   <img src="./Figures/image-20250705002932267.png" alt="image-20250705002932267" width="680px" />

   HWO将能够在100 Mpc的距离上探测到Cepheid变星，并通过测量其周光关系来精确确定距离。

3. [H.E.S.S. programme searching for VHE gamma rays associated with FRBs](https://arxiv.org/abs/2507.02143)

   > Fast Radio Burst, High Energy

   H.E.S.S.（高能立体系统）项目对快速射电暴（FRBs）的观测研究，旨在寻找与这些高能、短寿命的射电爆发相关的甚高能（VHE）伽马射线。给出了上限。

   <img src="./Figures/image-20250705003153813.png" alt="image-20250705003153813" width="680px" />

4. [Image Marker](https://arxiv.org/abs/2507.02153)

   > Astronomy, Software

   [Image Marker](https://github.com/andikisare/imgmarker)是一个多功能、高效的图像标记工具。

   <img src="./Figures/image-20250705003508922.png" alt="image-20250705003508922" width="680px" />

## 2025-07-07

