# 决策树

## 熵
熵：表示随机变量的不确定性。  
[信息熵](https://zhuanlan.zhihu.com/p/89958871)：一个表征符号系统中单位符号平均信息量的指标。  
[条件熵](https://zhuanlan.zhihu.com/p/26551798)：在一个条件下，随机变量的不确定性。  
[信息增益](https://zhuanlan.zhihu.com/p/26596036)：熵 - 条件熵。表示在一个条件下，信息不确定性减少的程度。  

*通俗地讲，X(明天下雨)是一个随机变量，X的熵可以算出来， Y(明天阴天)也是随机变量，在阴天情况下下雨的信息
熵我们如果也知道的话（此处需要知道其联合概率分布或是通过数据估计）即是条件熵。
X的熵减去Y条件下X的熵，就是信息增益。具体解释：原本明天下雨的信息熵是2，条件熵是0.01（因为如果知道明
天是阴天，那么下雨的概率很大，信息量少），这样相减后为1.99。在获得阴天这个信息后，下雨信息不确定性减少
了1.99，不确定减少了很多，所以信息增益大。也就是说，阴天这个信息对明天下午这一推断来说非常重要。*

## DT
所以在特征选择的时候常常用信息增益，如果IG（信息增益大）的话那么这个特征对于分类来说很关键，决策树就是
这样来找特征的。  

[]()
[决策树](https://zhuanlan.zhihu.com/p/26703300)
[基于信息与信息增益的ID3及C4.5决策树](https://www.cnblogs.com/pinard/p/6050306.html)
[基尼指数（基尼不纯度,信息熵的1阶泰勒展开）](https://www.zhihu.com/question/296781126/answer/508112100)
[CART树](https://www.cnblogs.com/pinard/p/6053344.html)

## Ensemble learning
[bagging模型集成与随机森岭](https://www.cnblogs.com/pinard/p/6156009.html)
[随机森林参数](https://zhuanlan.zhihu.com/p/56940098)

[模型融合](https://zhuanlan.zhihu.com/p/25836678)
[预测偏差、方差与模型融合](https://github.com/azusakou/studynote_ML/blob/master/DT/Lecture_10_Ensemble.pdf)









