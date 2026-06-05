## 2026-06-01

1. [The EPS Research Astro-RAG Platform: A Unified Open-Science Infrastructure for Cross-Epoch Astrophysical Kinematic Analysis, LLM-Assisted Research Workflows, and Educational Outreach](https://arxiv.org/abs/2605.30384)

   > Astronomy, RAG, LLM, Tool, Data Release

   面向跨红移天体运动学分析和 LLM 辅助检索，[EPS Research Astro-RAG Platform](https://github.com/eps-research/rag-corpus-series) 整合四个机器可读语料库：438 个 HI 旋转曲线星系、129 个矮星系或不规则星系、174 个银河系球状星团，以及 31 个高红移 ALMA [CII] 星系，总计 772 个对象。数据以 JSON、CSV、RAG-ready JSONL 和逐源 ZIP 形式发布，并配套 120 个已通过 `nbconvert` 执行验证的 Jupyter notebooks 与 QuickStart 复现实例。

   平台的核心贡献是把本地宇宙、银河系球状星团和高红移星系放入统一 schema 与分析框架，便于比较 HI 旋转曲线、球状星团动力学和高红移气体运动学。四个语料库均以 CC BY 4.0 发布在 Zenodo，QuickStart 可在一次克隆后自动下载数据并复现核心 cross epoch omega 结果；LLM fine tune 和 RAG 工具仍属于后续阶段规划。

2. [Transformer-Based Source Detection and Morphological Classification in LOFAR Deep-Field Continuum Images](https://arxiv.org/abs/2605.30500)

   > Radio, Deep Learning, Source Detection, LOFAR

   面向深场射电连续谱巡天中的源检测和形态分类，使用 RF-DETR 这类 transformer set prediction detector 处理 LOFAR Deep Fields 150 MHz 图像。模型在 ELAIS-N1 DR1 上训练，采用五类互斥标签：Compact、Single Extended、Multi Extended、Flagged 和 Spurious；推理时用滑动窗口覆盖 ELAIS-N1、Lockman Hole、Boötes 和 EDFN 四个深场，并把结果与 PyBDSF 目录和人工识别的大尺度射电星系样本比较。

   在 ELAIS-N1 验证集上，RF-DETR 的整体检测 F1 约为 91%，匹配后的分类 F1 约为 99%。跨四个深场应用时得到 43,805 到 75,609 个源，Compact 源占 92%–95%，说明单一训练场可迁移到不同深度和校准条件的图像。相比 PyBDSF，RF-DETR 能把双瓣或多成分射11电星系统一成源级检测，并显式标出伪源和受伪影影响的目标；对人工整理的 extended radio galaxies，恢复率约 94%，对 giant radio galaxies 约 86%。

   <img src="./Figures/image-20260601115935829.png" alt="image-20260601115935829" width="680px" />

3. [Characterising and mitigating Bluetooth and WiFi radio frequency interference at the Parkes Observatory](https://arxiv.org/abs/2605.30761)

   > Radio, RFI, Parkes, Instrument

   针对 Murriyang/Parkes 64 米望远镜 UWL 接收机中 2368–2496 MHz 子带的 RFI，分析 Wi-Fi、Bluetooth 和 NBN 信号在时间、频率和指向上的分布。材料包括多年校准观测的 1 MHz 频谱快照，以及 2023 年 8 月 10 日观测 Vela pulsar 时记录的 10 秒、16 bit 电压数据；后者用于在保留脉冲星信号的同时测试实时可行的 RFI 缓解方法。

   比较了 DSPSR spectral kurtosis、简单功率阈值和基于 Bluetooth 解调信号的阈值。无处理时 Vela 脉冲几乎不可用；调优后的 spectral kurtosis 可达到最高相对 S/N 516，但剔除约 33.4% 数据；8.69 dB 简单功率阈值只剔除约 0.4% 数据，S/N 达 341，更适合低复杂度实时部署。原本约 70% 子带长期被弃用，RFI 的时间频率局域性说明经过在线阈值处理后，超过 90% 的该子带可重新用于科学观测。

   <img src="./Figures/image-20260601120022045.png" alt="image-20260601120022045" width="680px" />

4. [Interstellar Scintillation of Three Nearby Pulsars with FAST](https://arxiv.org/abs/2605.30918)

   > Pulsar, FAST, Scintillation, Observation

   利用 FAST 19 波束接收机 L 波段 1.0–1.5 GHz 数据研究 PSR J0837+0610、J1136+1551 和 J1239+2453 的星际闪烁。处理流程包括 DSPSR 折叠和消色散、PSRCHIVE 去除 RFI、由动态谱计算二维自相关函数，并用 NuT transform 增强 secondary spectrum 中的 scintillation arcs；弧曲率用于估计散射屏距离和频率标度。

   PSR J0837+0610 和 J1239+2453 各检测到一个主要 scintillation arc，PSR J1136+1551 检测到三个清晰弧。J0837+0610 和 J1239+2453 的弧曲率频率标度分别约为 $\eta \propto \nu^{-2.0\pm0.6}$ 和 $\eta \propto \nu^{-1.9\pm0.6}$，J1136+1551 两个较清晰弧也接近 $\nu^{-2}$。推得散射屏距离约为 421 pc、196 pc、146 pc、39 pc 和 253 pc；除 J0837+0610 外，其余屏多位于距地球约 100–200 pc 范围，可能与 Local Bubble 子结构有关，但单历元观测仍需要长期闪烁监测或 VLBI 验证。

   <img src="./Figures/image-20260601120133586.png" alt="image-20260601120133586" width="680px" />

5. [Frequency-time-resolved Imaging Spectroscopy of Fine Structures in a Solar Radio Noise Storm](https://arxiv.org/abs/2605.31450)

   > Solar, Radio, LOFAR, Observation, Simulation

   针对太阳射电 noise storm 中异常紧凑的表观源尺寸，使用 LOFAR 对 2015 年 6 月 23 日接近日面中心的事件进行 30–40 MHz 频率时间分辨成像光谱分析，并结合各向异性射电波散射模拟。观测覆盖宽带连续谱及其中的 type I bursts、S-bursts 和 spikes；Nançay Decameter Array 提供 20–80 MHz 动态谱背景，LOFAR 覆盖约 10:45–12:30 UT。

   连续谱源在几十分钟内穿过日面，31.3–38.4 MHz 的表观主轴约从 $8.0'$ 降到 $4.3'$，小于相近频率 type III burst 源尺寸的一半。type I bursts、S-bursts 和 spikes 的动态谱形态不同，但在相同频率下与连续谱具有近似相同的表观尺寸；spike 的质心可与连续谱相差约 $500''$，提示其磁场系统可能不同。模拟表明，闭合磁场结构中的各向异性湍流会把辐射偏离视线方向，使观测到的源更紧凑；过密等离子体、较陡密度梯度、较低散射率和强各向异性也有贡献，但主导因素是大尺度日冕磁场与传播环境，而非不同精细结构的内禀发射机制。
   
   <img src="./Figures/image-20260601120200319.png" alt="image-20260601120200319" width="680px" />

## 2026-06-02

1. [A 0.03 Hz Radio Quasi-periodic Oscillation During the 2025 Flare of GRS 1915+105](https://arxiv.org/abs/2606.01823)

   > Microquasar, Radio, QPO, Jet, Observation

   对微类星体 GRS 1915+105 的 2025 年射电耀发进行每周监测，使用上海天马 65 m 与佘山 25 m 望远镜组成的约 6 km 单基线，在 S band 2.25 GHz 和 X band 8.42 GHz 同时观测。172 天内共分析 24 次观测、61 个 scan，并结合 NICER 1–10 keV 数据；2 秒时间分辨率光变用于功率谱和 Lomb Scargle 分析。

   射电耀发在 X band 先于 S band 达峰，谱指数从约 $+0.5$ 变到 $-0.75$，符合膨胀喷流中的 synchrotron self absorption。MJD 60765 和 60772 的两个连续观测中检测到 $\sim0.03$ Hz QPO 及 $\sim0.06$ Hz 谐波；MJD 60765 的双波段联合显著性超过 $5.9\sigma$，总联合显著性超过 $5\sigma$。该频率在 S/X 两个波段一致，并与 2021 年另一场射电耀发中的 0.03 Hz 信号相同，说明它更像吸积喷流系统的特征时标；但 X 射线强遮蔽导致无法确认其是否直接来自内吸积流，喷流进动或其它全局调制仍需同步 X 射线时变和高分辨率射电成像验证。

   <img src="./Figures/image-20260602134310775.png" alt="image-20260602134310775" width="680px" />

2. [Fast radio bursts, magnetars and earthquakes: their "family feud"?](https://arxiv.org/abs/2606.01855)

   > Fast Radio Burst, Magnetar, Statistics, Method

   为区分重复 FRB 的触发机制是否更像地震、磁星耀发或其它突发现象，构造 Pincus Lyapunov diagram，将事件序列映射到 stochasticity chaos 平面。数据包括 FRB 20121102A、20190520B、20201124A、20220912A、20240114A，多个磁星耀发、脉冲星 glitch、太阳耀发和地震序列；底层数据整理在 [ScienceDB](https://doi.org/10.57760/sciencedb.Fastro.00031)。每个源用 Pincus Index 描述随机性，用 Lyapunov Exponent 描述混沌性。

   PLD 中不同现象形成不同区域：地震偏高混沌低随机，脉冲星 glitch 偏高随机低混沌，磁星耀发和太阳耀发位于中间且相互接近，重复 FRB 形成独立且紧凑的区域。与 FRB 群体比较时，磁星耀发的 energy distance 为 0.138、$p=0.031$，脉冲星 glitch 为 0.111、$p=0.020$，可在 5% 水平拒绝同分布假设；FRB 20240114A 与其它 FRB 的比较为 $p=0.630$，内部自洽检验为 $p=0.984$。FRB 20240114A 在 8 个月内爆发率大幅变化，但 PI 和 LE 仍稳定，说明重复 FRB 的时能统计特征不只是活动率或样本量效应。

   <img src="./Figures/image-20260602134331061.png" alt="image-20260602134331061" width="680px" />

3. [AstroSkyFlow: an astronomical sky image flow simulator for time domain survey validation and machine learning](https://arxiv.org/abs/2606.02140)

   > Astronomy, Simulation, Tool, Time Domain, Machine Learning

   [AstroSkyFlow](https://github.com/laomuliubingbing/AstroSkyFlow) 是面向时域巡天验证和机器学习训练的多历元天区图像模拟器。给定观测计划后，OCS 模拟器负责望远镜指向、读出占用、可见性和安全约束，图像模拟器再生成天空源、PSF、星系形态、快移目标轨迹、内禀变源、消光、大气折射、天光背景、空间相关 scintillation、散射光、光学系统和探测器响应。恒星和星系来自用户目录或 Gaia DR3 查询，快移目标由星历动态传播，变量和暂现源可注入指定光变模型。

   验证使用上海木光天文台 CDK14 对 WASP 11 b 凌星的 75 张 180 秒图像，以及兴隆 85 cm 望远镜对 V0554 Dra 的 188 张 30 秒图像，并与 SkyMaker 比较。AstroSkyFlow 在噪声特性、CDPP 曲线和 PSF FWHM 分布上更接近真实观测，SkyMaker 对暗源噪声低估更明显；注入恢复测试能恢复凌星、几何/菲涅耳掩星、超新星和小行星轨迹等信号，超新星光变相对残差 RMS 约为 8%。当前限制包括 PSF 采用 Moffat 近似、星系用简单 Sérsic 模型、未处理静态源自行和视差，大规模生产还需要并行化优化。

   <img src="./Figures/image-20260602134353840.png" alt="image-20260602134353840" width="680px" />

## 2026-06-03

1. [One Transit Is All You Need: Detecting Exoplanets Through Learned Stellar Behaviour with EXOVEIL](https://arxiv.org/abs/2606.02778)

   > Exoplanet, Transit, Deep Learning, Kepler, Tool

   [EXOVEIL](https://github.com/Pratik25priyanshu20/ExoVeil) 把凌星搜索改写成预测残差中的异常检测：先用 6 层、8 头的 causal Transformer world model 学习恒星在无凌星情况下的原始光变，再用方盒模板 matched filter 从残差中找 transit shaped dip，最后用 XGBoost 基于 21 个特征区分行星和假阳性。训练使用 16,499 条 Kepler 光变，约 2,000 个含行星目标的已知凌星区间在自监督训练中被插值掩蔽，分类器用约 1,000 个 DR25 TCE 标签训练。

   在 Kepler DR25 上分类 AUC 为 0.938，仅使用 flux time series，低于依赖 Data Validation 诊断量的 ExoMiner，但能处理分类式系统无法处理的单次凌星。盲搜 3,737 颗 Kepler 星恢复 2,873 个已知确认行星信号，并找到 179 个不在 DR25 TCE 目录中的 transit like 信号，其中 46 个为 Tier 1 monotransit 候选；1000 ppm 单次凌星注入恢复率为 32.3%（假阳性修正后），零样本迁移到 TESS PLATO LOPS2 区域时恢复 47/47 个确认行星，PLATO 25 秒 cadence 模拟中灵敏度接近 100 ppm。

   <img src="./Figures/image-20260603112810890.png" alt="image-20260603112810890" width="680px" />

2. [Data-Driven Forecasting of three-Component Seismograms Using Transformer Architectures](https://arxiv.org/abs/2606.02912)

   > Seismology, Transformer, Simulation, Method

   [SeismoGPT](https://github.com/wesmail/seismogpt) 用 2600 万参数 causal Transformer 直接在时域预测三分量地震波形，把任务定义为物理约束的 continuation：输入从 P 波到 S 波后某个相对窗口的上下文，之后完全自回归生成未来波形。训练和评估基于合成地震图，覆盖震源深度 5–100 km、震中距 $10^\circ$–$90^\circ$、震级 $3\leq M_w\leq7$；三种配置分别比较 120 秒与 240 秒预测跨度，以及额外 post S 上下文对长跨度预测的影响。

   三种配置下 median normalized cross correlation 为 0.93–0.97，代表性预测能保持相位相干和谱能量分布。预测质量在大震中距和低震级时下降，主要因为波场较弱、相干性低且色散更强；震源深度影响较小。失败样例通常是逐步自回归 rollout 中的相位漂移，而非生成非物理波形。结果说明 transformer sequence model 可以从数据中学习稳定的地震波场延拓，但当前固定 patch tokenization 仍限制长时标高保真预测，后续需要更结构化或物理知情的表示。

   <img src="./Figures/image-20260603112836426.png" alt="image-20260603112836426" width="680px" />

3. [Multimodal Transformer Based Generic Mixture Density Network for Scattering Timescale Estimation of Fast Radio Bursts](https://arxiv.org/abs/2606.03596)

   > Fast Radio Burst, Deep Learning, Scattering, CHIME

   [MT-GMDN](https://github.com/kharelb/Scattering-Timescale-Estimation-With-Transformers) 面向 FRB 散射时标 $\tau$ 的快速概率估计，输入 CHIME/FRB Catalog 2 的去色散动态谱和对应 time series profile。动态谱分支把每个时间 bin 作为 token、频率向量作为 embedding，time series 分支用平行 transformer 捕捉脉冲不对称和散射尾；两路 latent representation 拼接后进入 mixture density regression head，同时输出零散射/未分辨散射的 Bernoulli 概率，以及 $\tau>0$ 时 lognormal 分布的参数。

   数据来自 CHIME/FRB Catalog 2，原始动态谱覆盖 400–800 MHz、16,384 个频率通道和约 160 个时间采样，频率方向下采样到 256 通道。对有可测散射的 Catalog 2 测试样本，MT-GMDN 的 $\tau$ 点估计 $R^2$ 达 94%，散射检测 AUC 为 0.87，测试集 recall 约 90%。在低 SNR 合成事件上，MT-GMDN 比 fitburst 更稳健，$R^2$ 为 68% 对 39%，并给出随 SNR 和 $\tau$ 变化的异方差不确定度；训练完成后推理约比 fitburst 快 $10^4$ 倍，适合大规模 FRB 参数自动化测量，但经典拟合方法仍适合作为验证基准。
   
   <img src="./Figures/image-20260603113028353.png" alt="image-20260603113028353" width="680px" />

## 2026-06-04

1. [Kinematic modelling of clusters with Gaia: the Death Throes of the Hyades](https://arxiv.org/abs/2007.02969)

   > Star Cluster, Gaia, Kinematics, Observation, Method

   针对星团内部速度场、旋转、剪切和潮汐尾运动，建立一个把 Gaia 视差、自行和部分径向速度联合起来的前向层级模型，建模代码为 [kinesis](http://github.com/smoh/kinesis)。星团成员的三维速度被写成线性速度场加随机弥散：

   $$
   \boldsymbol{v}_{i}\sim
   \mathcal{N}\left(\boldsymbol{v}_{0}+\mathbf{T}(\boldsymbol{b}_{i}-\boldsymbol{b}_{0}),\mathbf{\Sigma}\right),
   $$

   其中 $\boldsymbol{v}_{0}$ 是参考位置 $\boldsymbol{b}_{0}$ 的平均速度，$\mathbf{T}=dv_l/dx_k$ 是速度梯度张量，$\mathbf{\Sigma}$ 是完整三维速度弥散矩阵。背景污染用宽的各向同性高斯分量表示：

   $$
   \boldsymbol{v}_{i}\sim \mathcal{N}(\boldsymbol{v}_{0,\rm bg},\sigma_{\rm bg}^{2}\mathbf{I}),
   \qquad
   \mathcal{L}=f_{\rm mem}\mathcal{L}_{\rm cl}+(1-f_{\rm mem})\mathcal{L}_{\rm bg}.
   $$

   速度梯度的物理解释来自把 $\mathbf{T}$ 分解为反对称旋转项和对称剪切项：

   $$
   \frac{1}{2}(\mathbf{T}-\mathbf{T}^{T})=
   \begin{bmatrix}
   0&-\omega_z&\omega_y\\
   \omega_z&0&-\omega_x\\
   -\omega_y&\omega_x&0
   \end{bmatrix},
   $$

   $$
   \frac{1}{2}(\mathbf{T}+\mathbf{T}^{T})=
   \begin{bmatrix}
   w_4&w_3&w_2\\
   w_3&w_5&w_1\\
   w_2&w_1&3\kappa-w_4-w_5
   \end{bmatrix},
   \qquad
   \kappa=\frac{1}{3}(T_{xx}+T_{yy}+T_{zz}).
   $$

   这里 $\boldsymbol{\omega}$ 描述刚体旋转，$w_1,\ldots,w_5$ 描述剪切，$\kappa$ 描述各向同性膨胀或收缩。只用天体测量会让平均速度和 $\kappa$ 存在退化，并且通常只能约束 $\mathbf{T}$ 的 8 个独立组合；加入部分 Gaia DR2 亮星径向速度后，可以打破径向速度梯度方向的信息缺失，约束全部 9 个速度梯度分量。

   从三维速度到观测量的关键推导是投影和高斯边缘化。对每颗星定义

   $$
   \boldsymbol{a}_{i}=
   \begin{bmatrix}
   \pi_i\\
   \mu_{\alpha,i}\\
   \mu_{\delta,i}
   \end{bmatrix},
   \qquad
   \bar{\boldsymbol{a}}_{i}(d_i,\boldsymbol{v}_i)=
   \begin{bmatrix}
   1/d_i\\
   \boldsymbol{p}_i^T\boldsymbol{v}_i/d_i\\
   \boldsymbol{q}_i^T\boldsymbol{v}_i/d_i
   \end{bmatrix},
   $$

   其中 $\boldsymbol{p}_i$ 和 $\boldsymbol{q}_i$ 是赤经、赤纬方向单位矢量。由于 Gaia 测量误差和内部速度弥散都取高斯分布，潜在的 $\boldsymbol{v}_i$ 可以解析边缘化，得到

   $$
   \boldsymbol{a}_{i}\sim
   \mathcal{N}\left(
   \bar{\boldsymbol{a}}_{i}(d_i,\boldsymbol{v}_{0,\rm cl/bg}),
   \mathbf{D}_{i}
   \right),
   $$

   $$
   \mathbf{D}_{i}(d_i,\mathbf{\Sigma})=
   \mathbf{C}_{\boldsymbol{a},i}
   +\frac{1}{d_i^2}
   \begin{bmatrix}
   0&0&0\\
   0&&\\
   0&&\mathbf{M}_i^T\mathbf{\Sigma}\mathbf{M}_i
   \end{bmatrix},
   \qquad
   \mathbf{M}_i=[\boldsymbol{p}_i,\boldsymbol{q}_i].
   $$

   径向速度观测作为额外似然项加入：

   $$
   \bar v_{r,i}=\boldsymbol{r}_i^T\boldsymbol{v}_i,
   \qquad
   v_{r,i}\sim
   \mathcal{N}\left(
   \boldsymbol{r}_i^T\boldsymbol{v}_{0,\rm cl/bg},
   \sigma_{\rm RV}^{2}+\boldsymbol{r}_i^T\mathbf{\Sigma}_{\rm cl/bg}\boldsymbol{r}_i
   \right).
   $$

   应用于 Hyades 时，以约 10 pc 潮汐半径区分核心星团和潮汐尾。核心速度弥散接近各向同性，没有明显旋转；潮汐尾速度椭球明显拉长，主轴指向银心方向。核心在银道方位和垂直方向存在约 $2\sigma$ 水平的膨胀或收缩信号，潮汐尾显示强剪切，超过太阳邻域 Oort 常数预期的银河剪切，说明尾部恒星正在更快损失角动量，可能很快被银河潮汐进一步拉离或变形。
   
1. [Periodic Radio and X-ray Emission from an Accreting White Dwarf Binary](https://arxiv.org/abs/2606.04232)

   > Radio Transient, White Dwarf, X Ray, Observation

   ASKAP J174508.9−505149 是一个长周期射电暂现源，射电脉冲具有相干、偏振、窄带和间歇特征。ASKAP 发现圆偏振射电源后，MeerKAT 精确定位到 Gaia 光学对应体；SOAR、Magellan 光谱显示蓝色连续谱、强 Balmer 和 He I/He II 发射线，结合 Swift 和 Einstein Probe 的紫外及 X 射线观测，指向一个吸积磁白矮星双星系统。

   光谱给出约 1.3 小时轨道周期，射电爆发和 X 射线辐射都随轨道相位调制。射电脉冲在不同观测中集中于接近轨道合相的相位，但相位可相差半个轨道；没有发现类似 AR Sco 的秒级白矮星自转周期。该源把一类长周期射电暂现源与吸积白矮星双星直接联系起来，说明至少部分 LPT 可以由白矮星吸积环境中的等离子体过程产生。
   
   <img src="./Figures/image-20260604211905685.png" alt="image-20260604211905685" width="680px" />
   
3. [Full Nonlinear Velocity Reconstruction With Transformer and Ensemble Tree Machine Learning](https://arxiv.org/abs/2606.05047)

   > Cosmology, Deep Learning, Large Scale Structure, kSZ

   面向星系大尺度结构中的本动速度重建，将线性理论速度估计作为基线，再用机器学习预测真实速度与线性重建之间的非线性残差。模型包括 GBDT 和 Transformer，输入为多尺度星系密度与环境特征，输出视向和横向速度修正；训练和测试基于 AbacusSummit 模拟，并构造接近 DESI LRG、ELG 观测的周期盒和光锥样本，同时考察类似 Rubin LSST 光度红移误差的影响。

   两类模型都能改善线性速度重建，Transformer 表现最好，在 LRG 和 ELG 样本中提高速度相关系数、降低归一化残差方差，并在更宽空间尺度上恢复更准确的速度功率谱及与真实速度场的互相关。该方法对 kSZ 相关应用尤其有用，例如星系团成对速度相关和堆叠星系团密度剖面，可作为从未来巡天中提取非线性速度信息的工具。

   <img src="./Figures/image-20260604212025279.png" alt="image-20260604212025279" width="680px" />

## 2026-06-05

1. [Toward decision-aware AI for LSST-scale time-domain astronomy](https://arxiv.org/abs/2606.05285)

   > Astronomy, AI, LSST, Time Domain, Method

   LSST 每晚约产生 $10^7$ 个 alerts，早期光变通常稀疏、类别不确定、后续观测资源有限，单纯把每个 alert 当作静态分类问题会丢掉真正关键的决策信息。更合适的框架是部分可观测的动态环境：每次光谱、多波段测光、ToO 触发或延迟观测都会改变之后能学到的信息。

   提出的架构把 foundation model 作为源状态表示层，用异质时域数据学习类别概率、不确定性、异常度、宿主星系上下文和未来观测预测；再用 POMDP、信息增益估计、分层 triage 或仿真训练策略，把这些 belief states 转化为可审计的后续观测建议。已有 broker 不再只输出分类排名，而是接入持续更新的状态层和显式 utility function。关键要求是决策日志、可解释 utility、人类 override 和治理机制；评估指标也应从分类准确率扩展到累计科学收益、资源效率和群体参数恢复。

   <img src="./Figures/image-20260605164758830.png" alt="image-20260605164758830" width="680px" />

2. [A Decade to Map the Diffuse Universe: FRB-QSO Pairs with HST/COS Spectroscopy](https://arxiv.org/abs/2606.05310)

   > Fast Radio Burst, QSO, CGM, HST

   利用角秒定位 FRB 和近邻投影的紫外亮 QSO 视线配对，把 FRB 的 $DM$、$RM$、散射约束和 QSO 的 HST/COS 吸收线红移、柱密度、相态信息结合起来，用于分解 CGM、IGM、银河系和 M31 halo 中的电离气体与磁场贡献。FRB 提供与气体相态无关的自由电子柱密度，QSO 光谱提供逐红移、逐相态的吸收结构，两者配对后才能把特定 $DM$ 或 $RM$ 贡献关联到同一片气体。

   样本预测使用 $N(<\theta)=N_{\rm FRB}\Sigma_{\rm QSO}\pi\theta^2$，在约 20,000 deg$^2$ 公共天区内，采用 Milliquas v8 与 GALEX 选出的 FUV $<19$、$z<1$ QSO 面密度 $\Sigma_{\rm QSO}\approx0.46\,{\rm deg^{-2}}$。当前约 100 个 $z<1$ 角秒定位 FRB 几乎无法形成统计样本；到 2035 年，若下一代干涉阵列提供约 $10^5$ 个定位 FRB，静态 QSO 目录下可得到约 16–64 个 $\theta<1'$ 配对和数千个 $\theta<10'$ 配对。HST/COS 的 G130M+G160M 可在 $\lesssim15$ orbits 内达到 $S/N\gtrsim10$，覆盖低红移 CGM/IGM 的 Ly$\alpha$ 和金属线；2030 年代仍需要 HST/COS 支撑这类 UV 计划，直到 HWO 进入下一阶段。

   <img src="./Figures/image-20260605164843803.png" alt="image-20260605164843803" width="680px" />

3. [The X-ray emission of the long-period transient and accreting cataclysmic variable ASKAP J174508.9-505149](https://arxiv.org/abs/2606.05842)

   > Radio Transient, White Dwarf, X Ray, Observation

   ASKAP J174508.9-505149 是已被识别为吸积激变变星的长周期射电暂现源。基于 2025 年 9 月到 2026 年 5 月的 XMM-Newton 和 Einstein Probe X 射线观测，并结合同时的 ASKAP 射电和 XMM-Newton/OM B 波段数据，检测到 $P=4868(22)$ s 的 X 射线周期，与射电和光学周期一致；XMM-Newton 硬度比也有同样周期，并在流量调制最低处变硬。XMM 与 EP 的 X 射线 pulsed fraction 分别约为 23% 和 22%，还存在约 52 ks 的长时标调制，但受观测时长限制仍不稳健。

   X 射线谱用局部吸收、热等离子体和黑体成分描述，包含 $kT_{\rm apec}\sim15$ keV 的碰撞电离等离子体、$kT_{\rm bb}\sim0.14$ keV 的软黑体，以及 0.77 keV 附近可能来自 O VII 的吸收特征。周期性 X 射线、硬度比随相位变化和磁 CV 型谱结构共同指向磁化白矮星吸积；该源是第三个有 X 射线探测的 LPT，也是第一个被明确识别为吸积磁 CV 的 LPT。现有数据支持 intermediate polar 或 asynchronous polar 两种解释，仍需要更长、连续的 X 射线和高 cadence 光学观测来区分。

   <img src="./Figures/image-20260605164903834.png" alt="image-20260605164903834" width="680px" />

4. [A micronova burst in the intermediate polar IGR J17014-4306](https://arxiv.org/abs/2606.06305)

   > White Dwarf, Micronova, Cataclysmic Variable, Observation

   在 TESS sector 93 中检测到 IGR J17014-4306 的短时光学爆发。该源是食双星型 intermediate polar，并具有很长的轨道周期。分析使用 TESS 120 s cadence 数据，并用 ASAS-SN 光度和 Gaia 距离把 TESS flux 标定为 luminosity；长期搜索还结合 Gaia、ASAS-SN 和 AAVSO 光变。爆发持续 1.56 d，呈多峰结构，两个主峰相隔 0.26 d，峰值光学光度为 $(9.3\pm0.2)\times10^{33}\,{\rm erg\,s^{-1}}$，总辐射能量为 $(3.25\pm0.01)\times10^{38}$ erg，这些数值因未作 bolometric correction 可视为下限。

   按能量、峰值光度、持续时间和发生频率放到经验诊断图上，该事件落在已知 micronova 区域，明显偏离 dwarf nova、magnetic gating burst 和 donor flare。若按磁约束吸积柱中的局部热核 runaway 解释，燃烧柱质量约为 $1.6\times10^{-11}\,M_\odot$，结合质量转移率得到约 20 d 的复发时间；长期光变中还找到 16 个可能的快速增亮事件，最短间隔约 26 d。TESS 时序显示白矮星自转周期 $P_{\rm spin}\simeq1859$ s 在爆发前后保持稳定，爆发期间功率谱变复杂并出现多个峰，可能对应 micronova oscillations。该系统使已确认 micronova 系统增至 8 个，并因长轨道周期和食几何成为检验磁约束白矮星热核燃烧的样本。
   
   <img src="./Figures/image-20260605164952777.png" alt="image-20260605164952777" width="680px" />

## 2026-06-08

