# [特征工程](https://www.zhihu.com/question/29316149/answer/607394337) [视频](https://www.youtube.com/watch?v=68ABAU_V8qI)

## 知识点

### 数据类型
在表格类数据建模过程中，常常需要处理的数据类型：
1. 文本_[python 字符串方法](https://zhuanlan.zhihu.com/p/80518649)
需要通过[正则表达式](https://www.cnblogs.com/shenjianping/p/11647473.html)，
做特征表示；[文本特征稀疏表示：词袋、ngram、tf-idf](https://zhuanlan.zhihu.com/p/42310942)
2. 类别变量
类别数量较少可直接onehot；  
类别数量较多可以尝试[均值编码](https://zhuanlan.zhihu.com/p/26308272)[等](https://github.com/scikit-learn-contrib/category_encoders)方案；  
lightgbm可以支持直接的[类别型特征](https://zhuanlan.zhihu.com/p/67475635)输入，xgb等其他模型需要onehot； 
3. 排序变量
一般可以按照连续性变量处理；
4. 连续变量
线性模型、逻辑回归,knn(涉及距离的模型)等需要进行标准化，缺失处理；
树模型不需要进行标准化，一般不需要处理缺失；

### 数据流程
一般在数据处理与特征工程的工作流程为：
1. 异常值处理；
2. [缺失值处理](https://zhuanlan.zhihu.com/p/137175585)；
3. 特征构造；
4. 分布调整与标准化  
在具体项目中，2，3，4可以调整顺序；

### 数据处理

[为什么要处理缺失](https://www.zhihu.com/question/58230411/answer/242037063)

数据标准化方法  
分布良好的数据可以直接进行中心标准化 (x - mu) / std  
有偏分布可以尝试做log等**非线性单调变换**后再进行**中心标准化** (x - mu) / std  
对于较为特殊的分布可以尝试RankGauss标准化；查看sklearn QuantileTransformer文档  

### 特征挖掘

#### 概念及工作原理概念：
特征构造主要是产生衍生变量，所谓衍生变量是指对原始数据进行加工、特征组合，生成有商业意义的新变量(新特征)  
优点：新构造的有效且合理的特征可提高模型的预测表现能力。  
缺点：新构造的特征不一定是对模型有正向影响作用的，也许对模型来说是没有影响的甚至是负向影响，拉低模型的性能。因此构造的新特征需要反复参与模型进行训练验证或者进行特征选择之后，才能确认特征是否是有意义的。













[CTR如何构造特征，Louis回答](https://www.zhihu.com/question/347715330/answer/849645828)  
[特征选择概览](https://zhuanlan.zhihu.com/p/30404850)  
[特征选择实战](https://zhuanlan.zhihu.com/p/32749489)  
[[阅读]特征工程概览](https://www.zhihu.com/question/28641663/answer/110165221)  
[[阅读]高阶特征工程](https://zhuanlan.zhihu.com/p/62773597)  
[顶级方案学习：kaggle-IEEE-Fraud-Prediction](https://github.com/azusakou/studynote_ML/blob/master/Feature%20Engineering/顶级方案学习：kaggle-IEEE-Fraud-Prediction.pdf)  

## QA
两个类别型变量构造笛卡尔特征组合为什么能提升模型表现？

(1)把特征通过运输到一个关系更简单的空间里面，比如说线性可分的空间就会提升，模型性能提高。  
(2)abc 3个变量，变量之间两两独立，但是变量与变量之间组成一个，就比如三个变量，是一个大的系统，就不是独立的了，所以说通过构造这个，比如说a和b的特征组合，那么这个特征组合对于预测变量是有效的，但是有可能这个a和b，这两个变量单独对于这个预测是没有什么效果的，这个时候需要去构造这样的一个特征组合
 
  
 
  
 
 
