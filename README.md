# 理论
# nn https://www.nature.com/articles/nature14539 这篇论文综述了10年神经网络的几个重要节点，可以先了解下(由3巨头编写)
# 1.cnn 几种网络结构 简单了解即可 Lenet,googlenet,resnet,capsule-net
# 2.重点 gan papers 

:white_check_mark: [Generative Adversarial Nets] [[Paper]](https://arxiv.org/abs/1406.2661)
[[Code]](https://github.com/goodfeli/adversarial)(the First paper of GAN)

# 3.Tutorial
:white_check_mark: http://www.iangoodfellow.com/slides/2016-12-04-NIPS.pdf (NIPS Goodfellow Slides)[[Chinese Trans]](http://c.m.163.com/news/a/C7UE2MLT0511AQHO.html?spss=newsapp&spsw=1)[[details]](https://arxiv.org/pdf/1701.00160v1.pdf)

## Super-Resolution

:white_check_mark: [Image super-resolution through deep learning ][[Code]](https://github.com/david-gpu/srez)(Just for face dataset)

2.重点关注下这篇，超分辨率 

:white_check_mark: [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network] [[Paper]](https://arxiv.org/abs/1609.04802)[[Code]](https://github.com/leehomyc/Photo-Realistic-Super-Resoluton)（Using Deep residual network）

:white_check_mark: [EnhanceGAN] [[Docs]](https://medium.com/@richardherbert/faces-from-noise-super-enhancing-8x8-images-with-enhancegan-ebda015bb5e0#.io6pskvin)[[Code]]

## gen high-quality image

1. 图片聚类 

:white_check_mark: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1511.06434)[[Code]](https://github.com/jacobgil/keras-dcgan)(Gan with convolutional networks)(ICLR)

2. 文本合成图片 文本向量-->特征-->图片 就是找对应关系

:white_check_mark: [Generative Adversarial Text to Image Synthesis] [[Paper]](https://arxiv.org/abs/1605.05396)[[Code]](https://github.com/reedscot/icml2016)[[code]](https://github.com/paarthneekhara/text-to-image)

3.更快的方式训练gan

:white_check_mark: [Improved Techniques for Training GANs] [[Paper]](https://arxiv.org/abs/1606.03498)[[Code]](https://github.com/openai/improved-gan)(Goodfellow's paper)

:white_check_mark: [Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space] [[Paper]](https://arxiv.org/abs/1612.00005v1)[[Code]](https://github.com/Evolving-AI-Lab/ppgn)

:white_check_mark: [StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks] [[Paper]](https://arxiv.org/pdf/1612.03242v1.pdf)[[Code]](https://github.com/hanzhanggit/StackGAN)

:white_check_mark: [Improved Training of Wasserstein GANs] [[Paper]](https://arxiv.org/abs/1704.00028)[[Code]](https://github.com/igul222/improved_wgan_training)

:white_check_mark: [Boundary Equibilibrium Generative Adversarial Networks Implementation in Tensorflow] [[Paper]](https://arxiv.org/abs/1703.10717)[[Code]](https://github.com/artcg/BEGAN)

:white_check_mark: [Progressive Growing of GANs for Improved Quality, Stability, and Variation ] [[Paper]](http://research.nvidia.com/publication/2017-10_Progressive-Growing-of)[[Code]](https://github.com/tkarras/progressive_growing_of_gans)[[Tensorflow Code]](https://github.com/zhangqianhui/PGGAN-tensorflow)

## Image blending

1.提升画质

:white_check_mark: [GP-GAN: Towards Realistic High-Resolution Image Blending] [[Paper]](https://arxiv.org/abs/1703.07195)[[Code]](https://github.com/wuhuikai/GP-GAN)

## Image Inpainting

:white_check_mark: [Semantic Image Inpainting with Perceptual and Contextual Losses] [[Paper]](https://arxiv.org/abs/1607.07539)[[Code]](https://github.com/bamos/dcgan-completion.tensorflow)(CVPR 2017)

:white_check_mark: [Context Encoders: Feature Learning by Inpainting] [[Paper]](https://arxiv.org/abs/1604.07379)[[Code]](https://github.com/jazzsaxmafia/Inpainting)

:white_check_mark: [Semi-Supervised Learning with Context-Conditional Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1611.06430v1)

:white_check_mark: [Generative face completion] [[Paper]](https://drive.google.com/file/d/0B8_MZ8a8aoSeenVrYkpCdnFRVms/edit)[[code]](https://github.com/Yijunmaverick/GenerativeFaceCompletion)(CVPR2017)

:white_check_mark: [Globally and Locally Consistent Image Completion] [[MainPAGE]](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/en/)(SIGGRAPH 2017)

## Object Detection

:white_check_mark: [Perceptual generative adversarial networks for small object detection] [[Paper]](https://arxiv.org/abs/1706.05274v2)(CVPR 2017)

:white_check_mark: [A-Fast-RCNN: Hard Positive Generation via Adversary for Object Detection] [[Paper]](http://abhinavsh.info/papers/pdfs/adversarial_object_detection.pdf)[[code]](https://github.com/xiaolonw/adversarial-frcnn)(CVPR2017)

# Image translation 

:white_check_mark: [UNSUPERVISED CROSS-DOMAIN IMAGE GENERATION] [[Paper]](https://arxiv.org/abs/1611.02200)[[Code]](https://github.com/yunjey/domain-transfer-network)

:white_check_mark: [Image-to-image translation using conditional adversarial nets] [[Paper]](https://arxiv.org/pdf/1611.07004v1.pdf)[[Code]](https://github.com/phillipi/pix2pix)[[Code]](https://github.com/yenchenlin/pix2pix-tensorflow)

:white_check_mark: [Learning to Discover Cross-Domain Relations with Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1703.05192)[[Code]](https://github.com/carpedm20/DiscoGAN-pytorch)

:white_check_mark: [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks] [[Paper]](https://junyanz.github.io/CycleGAN/)[[Code]](https://github.com/junyanz/CycleGAN)

:white_check_mark: [CoGAN: Coupled Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1606.07536)[[Code]](https://github.com/andrewliao11/CoGAN-tensorflow)(NIPS 2016)

:white_check_mark: [Unsupervised Image-to-Image Translation with Generative Adversarial Networks] [[Paper]](https://arxiv.org/pdf/1701.02676.pdf)(NIPS 2017)

:white_check_mark: [Unsupervised Image-to-Image Translation Networks] [[Paper]](https://arxiv.org/abs/1703.00848)

:white_check_mark: [Triangle Generative Adversarial Networks] [[Paper]](https://arxiv.org/abs/1709.06548)

:white_check_mark: [ST-GAN: Unsupervised Facial Image Semantic Transformation Using Generative Adversarial Networks] [[Paper]](http://proceedings.mlr.press/v77/zhang17c.html)

:white_check_mark: [High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs] [[Paper]](https://arxiv.org/abs/1711.11585)[[code]](https://github.com/NVIDIA/pix2pixHD)

:white_check_mark: [XGAN: Unsupervised Image-to-Image Translation for Many-to-Many Mappings] [[Paper]](https://arxiv.org/abs/1711.05139)(Reviewed)

:white_check_mark: [UNIT: UNsupervised Image-to-image Translation Networks] [[Paper]](https://arxiv.org/abs/1703.00848)[[Code]](https://github.com/mingyuliutw/UNIT)(NIPS 2017)

:white_check_mark: [Toward Multimodal Image-to-Image Translation] [[Paper]](https://arxiv.org/abs/1711.11586)[[Code]](https://github.com/junyanz/BicycleGAN)(NIPS 2017)

:white_check_mark: [Multimodal Unsupervised Image-to-Image Translation] [[Paper]](https://arxiv.org/abs/1804.04732)[[Code]](https://github.com/nvlabs/MUNIt)

## Facial Attribute Manipulation

:white_check_mark: [Autoencoding beyond pixels using a learned similarity metric] [[Paper]](https://arxiv.org/abs/1512.09300)[[code]](https://github.com/andersbll/autoencoding_beyond_pixels)[[Tensorflow code]](https://github.com/zhangqianhui/vae-gan-tensorflow)

:white_check_mark: [Coupled Generative Adversarial Networks] [[Paper]](http://mingyuliu.net/)[[Caffe Code]](https://github.com/mingyuliutw/CoGAN)[[Tensorflow Code]](https://github.com/andrewliao11/CoGAN-tensorflow)（NIPS）

:white_check_mark: [Invertible Conditional GANs for image editing] [[Paper]](https://drive.google.com/file/d/0B48XS5sLi1OlRkRIbkZWUmdoQmM/view)[[Code]](https://github.com/Guim3/IcGAN)

:white_check_mark: [Learning Residual Images for Face Attribute Manipulation] [[Paper]](https://arxiv.org/abs/1612.05363)[[code]](https://github.com/Zhongdao/FaceAttributeManipulation)(CVPR 2017)

:white_check_mark: [Neural Photo Editing with Introspective Adversarial Networks] [[Paper]](https://arxiv.org/abs/1609.07093)[[Code]](https://github.com/ajbrock/Neural-Photo-Editor)(ICLR 2017)

:white_check_mark: [Neural Face Editing with Intrinsic Image Disentangling] [[Paper]](https://arxiv.org/abs/1704.04131)(CVPR 2017)

:white_check_mark: [GeneGAN: Learning Object Transfiguration and Attribute Subspace from Unpaired Data ] [[Paper]](https://arxiv.org/abs/1705.04932)(BMVC 2017)[[code]](https://github.com/Prinsphield/GeneGAN)

:white_check_mark: [Beyond Face Rotation: Global and Local Perception GAN for Photorealistic and Identity Preserving Frontal View Synthesis] [[Paper]](https://arxiv.org/abs/1704.04086)(ICCV 2017)

:white_check_mark: [StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation] [[Paper]](https://arxiv.org/abs/1711.09020)[[code]](https://github.com/yunjey/StarGAN)(CVPR 2018)

:white_check_mark: [LEGANT: Exchanging Latent Encodings with GAN for Transferring Multiple Face Attributes ] [[Paper]](https://arxiv.org/abs/1803.10562)[[code]](https://github.com/Prinsphield/ELEGANT)

## 工程
### 1.部署环境 1-2d
### 2.开发第一个程序 mnist 1-2d 了解流程
### 3.学习gan，给出方案 2-3d
### 4.获取训练数据，训练模型，验证效果 4-5d
### 5.提升方案 10d