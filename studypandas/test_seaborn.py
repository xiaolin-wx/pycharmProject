import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt #导入

import seaborn as sns
sns.set(color_codes=True)#导入seaborn包设定颜色

np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size=100)
# sns.distplot(x, kde=False, rug=True);#kde=False关闭核密度分布,rug表示在x轴上每个观测上生成的小细条（边际毛毯）
# sns.distplot(x, bins=20, kde=False, rug=True);#设置了20个矩形条
# sns.distplot(x, hist=False, rug=True);#关闭直方图，开启rug细条
# sns.kdeplot(x, shade=True);#shade控制阴影

# x = np.random.gamma(6, size=200)#生成gamma分布的数据
# sns.distplot(x, kde=False, fit=stats.gamma);#fit拟合

sns.set(style="dark", palette="muted", color_codes=True)
rs = np.random.RandomState(10)

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)  #前面两个控制行，列  中间控制长宽  最后控制x轴是否显示 true不显示
sns.despine(left=True)

# Generate a random univariate dataset
d = rs.normal(size=100)  #获取随机数

# Plot a simple histogram with binsize determined automatically
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])   #ax 图标显示位置 以二维数组方式排列

# Plot a kernel density estimate and rug plot
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])

# Plot a filled kernel density estimate
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

# Plot a historgram and kernel density estimate
sns.distplot(d, color="m", ax=axes[1, 1])

plt.setp(axes, yticks=[])
plt.tight_layout()  #图标的布局结构

#显示图形
plt.show()

