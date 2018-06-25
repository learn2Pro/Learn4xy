# 理论
# nn https://www.nature.com/articles/nature14539 这篇论文综述了10年神经网络的几个重要节点，可以先了解下(由3巨头编写)
# 1.cnn 几种网络结构 简单了解即可 Lenet,googlenet,resnet,capsule-net
# 2.重点 gan papers https://github.com/learn2Pro/AdversarialNetsPapers
## gen high-quality image

1. 图片聚类 

:white_check_mark: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1511.06434)[[Code]](https://github.com/jacobgil/keras-dcgan)(Gan with convolutional networks)(ICLR)

2. 文本合成图片 文本向量-->特征-->图片 就是找对应关系

:white_check_mark: [Generative Adversarial Text to Image Synthesis] [[Paper]](https://arxiv.org/abs/1605.05396)[[Code]](https://github.com/reedscot/icml2016)[[code]](https://github.com/paarthneekhara/text-to-image)

3.更快的方式训练gan，不用了解，工程上的提升

:white_check_mark: [Improved Techniques for Training GANs] [[Paper]](https://arxiv.org/abs/1606.03498)[[Code]](https://github.com/openai/improved-gan)(Goodfellow's paper)

:white_check_mark: [Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space] [[Paper]](https://arxiv.org/abs/1612.00005v1)[[Code]](https://github.com/Evolving-AI-Lab/ppgn)

:white_check_mark: [StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks] [[Paper]](https://arxiv.org/pdf/1612.03242v1.pdf)[[Code]](https://github.com/hanzhanggit/StackGAN)

:white_check_mark: [Improved Training of Wasserstein GANs] [[Paper]](https://arxiv.org/abs/1704.00028)[[Code]](https://github.com/igul222/improved_wgan_training)

:white_check_mark: [Boundary Equibilibrium Generative Adversarial Networks Implementation in Tensorflow] [[Paper]](https://arxiv.org/abs/1703.10717)[[Code]](https://github.com/artcg/BEGAN)

:white_check_mark: [Progressive Growing of GANs for Improved Quality, Stability, and Variation ] [[Paper]](http://research.nvidia.com/publication/2017-10_Progressive-Growing-of)[[Code]](https://github.com/tkarras/progressive_growing_of_gans)[[Tensorflow Code]](https://github.com/zhangqianhui/PGGAN-tensorflow)

## Image blending

1.提升画质

:white_check_mark: [GP-GAN: Towards Realistic High-Resolution Image Blending] [[Paper]](https://arxiv.org/abs/1703.07195)[[Code]](https://github.com/wuhuikai/GP-GAN)

## 工程
### 1.部署环境 1-2d
### 2.开发第一个程序 mnist 1-2d 了解流程
### 3.学习gan，给出方案 2-3d
### 4.获取训练数据，训练模型，验证效果 4-5d
### 5.提升方案 10d