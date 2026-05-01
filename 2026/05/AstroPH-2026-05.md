## 2026-05-01

1. [The Solar System Notification Alert Processing System (SNAPS): Public access to SNAPS data and products](https://arxiv.org/abs/2604.27420)

   > Solar System, Asteroid, Tool, Database

   [SNAPS](https://snaps.nau.edu/) 是面向太阳系移动天体的下游 alert broker，用于接收 ZTF 和未来 LSST 经 ANTARES 转发的已知移动天体警报，并公开对象观测、轨道信息、邮票图像和派生性质。系统只处理已知小行星、彗星等移动源，不负责新天体发现或轨道链接。

   当前网页支持按编号、临时编号或 packed designation 查询对象，返回 ZTF/LSST 观测、MPC 轨道参数、$H$ 星等、相位曲线、光变周期、振幅和颜色等产品；观测较多的目标还可在浏览器中查看图像、运行 Lomb Scargle 周期搜索、保存收藏和笔记。后续接口计划包括批量 API、异常天体 Kafka 流、跨目录查询和按物理性质筛选。

2. [First Detection of Faraday Rotation in a Gamma-Ray Burst Afterglow: Low Polarization and High Rotation Measure in GRB 260310A Reveal Jet Magnetic Structure and Environment](https://arxiv.org/abs/2604.27480)

   > Gamma Ray Burst, Polarization, Faraday Rotation, Observation

   GRB 260310A 的 VLA 11–25 GHz 偏振观测给出了首个厘米波 GRB 余辉偏振探测和首个 GRB 环境中的RM测量。观测发生在触发后约 19.2 天，结合公开多波段 GCN 测光，正向激波用于解释光学和 X 射线，射电部分用结构化喷流反向激波模型 [rsjetstruct](https://github.com/rohdog2003/rsjetstruct) 拟合。

   偏振度从 25 GHz 的约 $3.18\%$ 降到 11 GHz 的约 $0.69\%$，低频去偏振更符合同步自吸收影响。观测RM为 $RM=-6250\pm70\ {\rm rad\ m^{-2}}$，换算到 GRB 红移为 $RM_{\rm int}=-8300\pm90\ {\rm rad\ m^{-2}}$；银河系和星系际介质贡献不足以解释该值，更可能来自大质量恒星前身周围的致密磁化 HII 区。较低的高频偏振度也指向小尺度斑块状磁场，而非全局有序喷流磁场。

   <img src="./Figures/image-20260501211730926.png" alt="image-20260501211730926" width="680px" />

3. [An Extended Evaluation Split for DeepSpaceYoloDataset](https://arxiv.org/abs/2604.27593)

   > Astronomy, Deep Learning, Dataset, Object Detection

   DeepSpaceYoloDataset 新增 `test2026` 评估集，用于检验深空天体检测模型在智能望远镜图像上的泛化能力；数据集在 [Zenodo](https://doi.org/10.5281/zenodo.8387070) 发布。新增部分包含 335 张高分辨率 RGB 图像，来自 Stellina 和 Vespera 在法国、比利时、卢森堡的观测，目标包括星系、星云和星团。

   图像通过 Python、OpenCV、Pillow 和 Astroalign 对齐叠加，并用 MakeSense 以 YOLO 格式标注。完整数据集扩展到 5031 张图像；YOLO5m、YOLO8m、YOLO11m、YOLO12m 在原测试集和 `test2026` 上的 mAP 排名发生变化，说明新增测试集包含更复杂的分辨率、视场和观测条件，更适合作为深空目标检测的稳健性基准。

   <img src="./Figures/image-20260501211826423.png" alt="image-20260501211826423" width="680px" />

4. [The Large Array Survey Telescope—Pipeline. II. Image Subtraction and Transient Detection](https://arxiv.org/abs/2604.27921)

   > Transient, Survey, Pipeline, Image Subtraction

   LAST 巡天管线的第二部分负责从 Pipeline I 产生的 $20\times20$ 秒合并图像中进行实时差分成像和暂现源检测，相关软件生态使用 [AstroPack](https://github.com/EranOfek/AstroPack)。流程包括参考图像配准、ZOGY 差分、显著性图像构建、$|S|\ge5\sigma$ 候选提取、孔径和 PSF 测光，以及对坏像素、条纹、傅里叶振铃、PSF 异常、已知变星、恒星和太阳系天体的确定性过滤。

   调试数据和注入测试显示，标准参考图像下单历元极限星等约 20.3 mag，深参考图像可到约 20.7 mag。约 $4\times10^7$ 个初始检测经过过滤后降到约 $0.01\ {\rm deg^{-2}}$ 的候选密度，$S\ge7.5\sigma$ 时纯度超过 90%；单历元效率约 80%，较好条件下约 87%。主要损失来自配准裁剪和 PSF 重建限制，后续改进集中在参考图像配准、PSF 建模和可能的机器学习分类。

5. [On the polarization position angle jumps in FRB 20240114A](https://arxiv.org/abs/2604.28012)

   > Fast Radio Burst, Polarization, Observation

   FRB 20240114A 的 190 个爆发被用于研究偏振位置角在毫秒到小时尺度上的跳变。数据来自 Nançay Radio Telescope 的 1.1–1.8 GHz 全 Stokes 高时间分辨率观测和 Effelsberg 100 m 望远镜的 1.3–1.5 GHz 观测，覆盖约一年和 12 个历元，并测量 RM、线偏振、圆偏振和时间分辨位置角。

   RM 整体稳定，典型值在约 340–387 ${\rm rad\ m^{-2}}$ 范围内，未显示明显内禀 RM 演化；约 81% 的爆发具有 $L/I>0.8$ 的高线偏振，圆偏振通常较弱。位置角可在 10–15 ms 到数小时内随机变化，跳变量可接近 $90^\circ$，但没有明显偏好正负方向或精确正交跳变。稳定 RM 与随机 PPA 跳变的组合不支持单一固定磁层发射区，更倾向于多个活动发射区或双折射模式耦合、广义法拉第旋转、磁层传播、等离子体透镜等传播效应。
   
   <img src="./Figures/image-20260501212004897.png" alt="image-20260501212004897" width="680px" />

## 2026-05-04

