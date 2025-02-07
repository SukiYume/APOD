## 2025-02-03

1. [The Local Galactic Transient Survey Applied to an Optical Search for Directed Intelligence](https://arxiv.org/abs/2501.18903)

   > Transient, SETI

   传统的SETI研究主要集中在无线电频率上，但随着激光技术的不断发展，光学和近红外波段的激光通信成为了一个新的研究方向。

   LGTS旨在通过Las Cumbres Observatory的0.4米望远镜网络，探测仙女座星系（M31）、大麦哲伦云（LMC）和小麦哲伦云（SMC）中的光学瞬变信号。

   不同文明等级的激光功率
   $$
   P=F_e\epsilon_c10^{2S}
   $$
   其中$F_e$是太阳照度，$\epsilon_c$是激光转换效率，S是文明等级。

   文章的计算表明，利用本世纪可以构建的激光技术，LGTS的观测能力和TRIPP的检测能力足以探测到M31中使用的定向能量系统。

2. [Machine Learning in Gamma Astronomy](https://arxiv.org/abs/2501.19064)

   > High Energy, Deep Learning, Review

   通过成像大气切伦科夫望远镜（IACT）获得的天体粒子数据的最流行的深度学习方法，并提供了原始论文的参考文献。

   使用CNN进行**粒子类型分类**、**EAS参数重建**，使用GAN生成高质量的伽马/质子事件图像。

## 2025-02-04

1. [PyLMT: A transient detection pipeline for the 4-m International Liquid Mirror Telescope](https://arxiv.org/abs/2502.00556)

   > Transient, Deep Learning, Software

   `PyLMT`对光学图像进行微分，然后使用CNN进行判别图像中是否存在真的暂现源，然后使用另一个CNN对判断为真的暂现源进行分类。

2. [BatAnalysis -- A Comprehensive Python Pipeline for Swift BAT Time-Tagged Event Data Analysis](https://arxiv.org/abs/2502.00278)

   > High Energy, Software

   [BatAnalysis](https://github.com/parsotat/BatAnalysis)用于处理Swift Burst Alert Telescope（BAT）收集的时间标记事件（TTE）数据，包括数据获取、处理、光谱拟合和图像拼接。通过分析GRB 050724、FRB 180916、LMXB EXO 0748-676和GRB 210706A的数据，验证了软件的正确性和功能。

3. [A Fast Periodicity Detection Algorithm Sensitive to Arbitrary Waveforms](https://arxiv.org/abs/2502.00243)

   > Light Curve, Periodicity, Method

   [FPW](https://github.com/Sewhitebook/FPW)是一种相位分箱算法，通过将每个观测值分配到相应的相位箱中，计算每个周期或频率的统计量
   $$
   {\rm SFPW}=\frac{1}{\alpha^2}\sum_{m=1}^M\left[\frac{\sum_{j=1}^{Nm}x^2_{m,j}/\sigma^2_{m,j}}{\sum_{j=1}^{Nm}\left(\frac{1}{\sigma^2_{m,j}}+\frac{1}{\alpha^2}\right)}\right]
   $$
   其中，M是相位箱的数量，$Nm$是第$m$个相位箱中的观测数量，$x_{m,j}$ 是第$m$个相位箱中第$j$个光度观测值的均值减去后的值，$\sigma^2_{m,j}$是$x_{m,j}$的观测误差平方。

   用于检测非均匀采样时间序列数据中任意波形周期性。

4. [Million Points of Light (MPoL): a PyTorch library for radio interferometric imaging and inference](https://arxiv.org/abs/2502.00100)

   > Interferometry, Software

   [MPoL](https://mpol-dev.github.io/MPoL/)使用PyTorch建立了反向传播和梯度下降，用于解决射电干涉成像和推断的问题。

   <img src="./Figures/image-20250205154226843.png" alt="image-20250205154226843" width="680px" />

## 2025-02-05

1. [Discovery of an RRAT-like pulsar via its single pulses in an MWA imaging survey](https://arxiv.org/abs/2502.02130)

   > Pulsar, Observation

   使用MWA的成像数据检测到PSR J0031-5726，，它表现出介于正常脉冲星和RRATs之间的特征。PSR J0031-5726的单脉冲行为复杂，包括长尾的脉冲能量分布和剧烈的极化角变化。

2. [Exploring blazars through sonification. Visual and auditory insights into multifrequency variability](https://arxiv.org/abs/2502.01929)

   > Astronomy, Sonify

   结合视觉和听觉手段，展示了blazars的多频变异性分析。链接在[这里](https://www.guijongustavo.org/datasonification)。

3. [Thirty-five years of timing of M53A with Arecibo and FAST](https://arxiv.org/abs/2502.02042)

   > Pulsar, Timing, Observation

   结合FAST和Arecibo的数据给出球状星团NGC5024中的脉冲星M53A的计时解，确认伴星为一个氦白矮星。或许可以看看他们的数据有没有白矮星的辐射。

## 2025-02-06

1. [Propagation-induced Frequency-dependent Polarization Properties of Fast Radio Burst](https://arxiv.org/abs/2502.02857)

   > Fast Radio Burst, Theory

   王维扬的文章，讲FRB的辐射在等离子体中传播时，同时遇到法拉第旋转和转换，会发生偏振谱在庞加莱球面上随频率的旋转。

2. [Astromer 2](https://arxiv.org/abs/2502.02717)

   > Astronomy, Deep Learning

   [Astromer 2](https://github.com/astromer-science)使用BERT的结构，在光变曲线数据上进行训练，输出恒星标签。

3. [Earth Detecting Earth: At what distance could Earth's constellation of technosignatures be detected with present-day technology?](https://arxiv.org/abs/2502.02614)

   > SETI

   利用现有技术检测地球技术特征（technosignatures）的最大距离。

   1. **无线电传输:**
      - **间歇性天体目标无线电传输:** 例如，故意发送给外星智能的消息（METI）信号和行星雷达传输。计算得出其最大可探测距离为12000光年。
      - **持续性天体目标无线电传输:** 例如，NASA的深空网络（DSN）。其最大可探测距离为65光年。
      - **持续性全向无线电泄漏:** 例如，手机塔和电视广播站。其最大可探测距离为4.0光年。
      - **来自人造物体的无线电信号:** 例如，来自行星轨道器的下行链路。其最大可探测距离为0.97光年。
   2. **大气技术特征:**
      - 以NO₂为例，使用即将到来的6米级红外/光学/紫外望远镜进行直接成像光谱观测。计算得出其最大可探测距离为5.71光年。
   3. **光学和红外发射:**
      - **城市灯光:** 使用高压力钠灯的城市灯光。其最大可探测距离为0.036光年。
      - **定向激光:** 使用地面激光阵列和Keck II上的NIRSPEC仪器。未解析情况下的最大可探测距离为150天文单位，半解析情况下为1.8秒差距。
      - **热岛效应:** 以香港为例，计算得出其最大可探测距离为30天文单位。
   4. **空间或行星表面物体:**
      - **星际/星际探测器:** 例如，回声项目中的卫星。其最大可探测距离为0.145天文单位。
      - **行星表面物体:** 例如，阿波罗登月舱。其最大可探测距离为8600公里。
      - **卫星过境:** 以国际空间站为例，其最大可探测距离为1.3天文单位。

   人类对地球和太阳系的远程可探测影响跨越了12个数量级。

## 2025-02-07

1. [Multidisciplinary Science in the Multimessenger Era](https://arxiv.org/abs/2502.03577)

   > Astronomy, White Paper, Transient

   多信使天文学（TDAMM）在时间域和多信使天文物理学中的重要性。应用案例，核心坍缩超新星、中子星合并、快速射电暴。

2. [Self-Supervised Learning for Solar Radio Spectrum Classification](https://arxiv.org/abs/2502.03778)

   > Solar Flare, Deep Learning

   用BERT架构对太阳射电频谱图像进行预训练。

## 2025-02-10

