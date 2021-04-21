# 梯度提升树
[]()


## 知识点
通俗易懂理解——Adaboost算法原理  
[AdaBoost](https://zhuanlan.zhihu.com/p/41536315)（Adaptive Boosting，自适应增强），其自适应在于：**前一个基本分类器分错的样本会得到加强，加权后的全体样本再次被用来训练下一个基本分类器。同时，在每一轮中加入一个新的弱分类器，直到达到某个预定的足够小的错误率或达到预先指定的最大迭代次数。**  

Adaboost 迭代算法有三步：  
1. 初始化训练样本的权值分布，每个样本具有相同权重；  
2. 训练弱分类器，如果样本分类正确，则在构造下一个训练集中，它的权值就会被降低；反之提高。用更新过的样本集去训练下一个分类器；  
3. 将所有弱分类组合成强分类器，各个弱分类器的训练过程结束后，加大分类误差率小的弱分类器的权重，降低分类误差率大的弱分类器的权重。  

[GBDT原理](https://zhuanlan.zhihu.com/p/29765582)
[拓展阅读:Random Forest、Adaboost、GBDT](https://zhuanlan.zhihu.com/p/86263786)
[XGBoost、LightGBM原理](https://zhuanlan.zhihu.com/p/87885678)
[XGBoost、LightGBM对比](https://zhuanlan.zhihu.com/p/35645973)

