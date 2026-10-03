## 2026-10-01

1. [Learning Gaia: A Generative Model Trained on the Gaia Data Release 3 Source Catalog](https://arxiv.org/abs/2609.38326)

    > Gaia, Deep Learning

    研究以 Gaia DR3 中约 5.79 亿个源的位置、测光和天体测量参数训练条件流匹配模型，通过随机遮蔽输入学习在不同信息组合下生成模拟源或补全缺失量。模型能够重现银盘和大小麦哲伦云的大尺度分布，测光补全尤其有效，径向速度预测也利用了天空位置与运动信息。对半人马座 ω 等小而独特的子群，模型仍难以恢复其狭窄运动分布。训练目标保留星表测量误差和选择效应；具有径向速度测量的源仅占约 2%，向其余源外推时存在样本分布差异。该工作为 Gaia 数据生成模型提供了可扩展的初步方案。

    <img src="./Figures/image-202610010000001.png" alt="image-202610010000001" width="680px" />

2. [VLBI Astrometric Procedure and Performance with CHIME/FRB Outriggers](https://arxiv.org/abs/2609.38344)

    > Fast Radio Burst, Localization, VLBI

    研究建立 CHIME/FRB 外站阵列在 400–800 MHz 的快速射电暴定位流程，将多校准源联合拟合、电离层先验和迭代相关处理纳入统一分析，并处理共享目标信号带来的误差相关性。超过千次连续谱校准源与脉冲星测试定位验证了误差区间的覆盖率。明亮宽带信号的二维定位精度可达约 $10\times30$ 毫角秒，弱窄带信号的误差则明显增大。电离层色散与几何时延的简并是后一情形的重要限制，更高精度还受中性大气和校准源结构影响。结果支持对单次爆发开展宿主内部环境定位，具体精度取决于信噪比和有效带宽。

    <img src="./Figures/image-202610010000002.png" alt="image-202610010000002" width="680px" />

3. [PTED: A multi-dimensional two-sample test for scientific inference and generative machine learning](https://arxiv.org/abs/2609.38388)

    > Statistics, Software, Machine Learning

    PTED 将能量距离与置换检验结合，用于判断两组多维样本是否来自同一分布，并提供后验覆盖率和分布包含关系的检验接口。在样本满足独立性及零假设下可交换性的条件下，基础检验控制假阳性率；固定数量的参照点可使距离计算随样本量线性增长。高斯、双月牙、MNIST 和 CIFAR-10 测试显示其对多种偏差保持较高灵敏度，表现与常用 MMD 接近。双尾设置能够识别对训练样本的过度复制，MMD 也可采用这一设置。高维局部偏差和稀少离群点仍可能被漏检，检验通过只表示现有样本证据有限。[Python 软件包](https://github.com/ConnorStoneAstro/pted)已公开。

    <img src="./Figures/image-202610010000003.png" alt="image-202610010000003" width="680px" />

4. [The AI crisis for teaching: "Train your own neural network!"](https://arxiv.org/abs/2609.39433)

    > Astronomy, Education, LLM

    这篇观点文章结合天体物理教学经验，讨论学生直接采用大语言模型答案对知识理解、独立推理和作业评价的影响。作者强调，学习需要学生亲自经历计算、试错和判断，“训练自己的神经网络”指向这一思维训练过程。AI 可支持检索、反馈与辅导，其有效使用依赖学生逐步建立核查答案的能力。文章建议重新分配作业与考试权重，探索课堂无设备测验、受控终端和口试，并将部分助教时间投入直接交流。这些安排需要兼顾资源、公平性和考试压力；论证主要来自教学观察与案例，所提改革的实际效果仍需系统评估。

## 2026-10-02

1. [The star formation history of Orion is structured and episodic](https://arxiv.org/abs/2610.00481)

    > Stellar, Star Formation, Gaia

    研究利用 Gaia DR3 识别的 47 个共空间、共运动群体及统一测定的年龄，重建猎户座恒星形成历史。年龄分布出现多个间隔约 500 万年的增强期，较近两次对成员重采样和年龄拟合变化较稳定，较老峰的可靠性仍有限。同龄群体在空间上显著聚集，并形成多条具有局部年龄梯度的候选星团链，支持顺序形成与恒星反馈参与的图景。整体多峰性的统计证据较弱，恒星加权分布的单峰性检验得到 $p=0.064$；嵌入年轻星的遗漏和年龄模型系统误差也影响解释。这一时间间隔与天蝎—半人马区域相近，其物理起因仍待确认。

    <img src="./Figures/image-202610020000001.png" alt="image-202610020000001" width="680px" />

2. [Towards Retrieval Augmented Generation in High-Energy and Astroparticle Physics](https://arxiv.org/abs/2610.00891)

    > Astronomy, LLM, Software

    研究构建面向高能物理与高能天体物理文献的检索增强生成流程，将 Specter2 语义检索、BM25 关键词匹配、排序融合和交叉编码器重排结合，再由 Gemma4 筛选文献并生成带引用的短报告。合成问题基准显示，混合检索与重排显著提高来源论文的召回率，天体物理问题的前十结果召回率约为 87%–95%，宽泛探索性问题仍较难处理。相关性筛选对候选顺序敏感，多次打乱顺序后取并集可减轻这一影响。报告依据标题和摘要生成，质量验证集中于少数专家核验示例；这些结果支持文献初步导航，报告的全面性和论断准确性仍需进一步检查。

    <img src="./Figures/image-202610020000002.png" alt="image-202610020000002" width="680px" />

3. [A comprehensive simulation framework for multi-modal kilonova observations from all-sky surveys](https://arxiv.org/abs/2610.02088)

    > Kilonova, Simulation, Software

    研究建立千新星多模态观测模拟框架，以辐射转移模型及快速代理生成光谱和光变，加入 ZTF 历史观测的采样、深度与误差分布，并向真实巡天图像注入点源，形成配套测光、光谱和图像序列。独立模拟上的光变预测绝对误差中位数约为 0.32 星等，均方根误差约为 0.76 星等；图像注入自身的流量恢复检验得到约 0.05 星等的均方根误差。与 AT2017gfo 的比较支持整体光变和部分光谱演化，同时显露早晚期光谱形态偏差。近赤道视角的极暗模型精度也明显下降，训练数据用于实际参数推断时需纳入辐射转移模型的不确定性。

    <img src="./Figures/image-202610020000003.png" alt="image-202610020000003" width="680px" />
