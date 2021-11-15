#
# # 条形图
# import numpy as np
# import matplotlib.pyplot as plt
#
# men_means= (23, 30, 30, 31, 27)
# women_means= (25, 32, 23, 20, 25)
#
# ind = np.arange(len(men_means))  # the x locations for the groups
# width = 0.35  # the width of the bars
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(ind - width/2, men_means, width,
#                 color='SkyBlue', label='Men')
# rects2 = ax.bar(ind + width/2, women_means, width,
#                 color='IndianRed', label='Women')
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(ind)
# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
# ax.legend()
#
#
# def autolabel(rects, xpos='center'):
#     """
#     Attach a text label above each bar in *rects*, displaying its height.
#
#     *xpos* indicates which side to place the text w.r.t. the center of
#     the bar. It can be one of the following {'center', 'right', 'left'}.
#     """
#
#     xpos = xpos.lower()  # normalize the case of the parameter
#     ha = {'center': 'center', 'right': 'left', 'left': 'right'}
#     offset = {'center': 0.5, 'right': 0.5, 'left': 0.5}  # x_txt = x + w*off
#
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1*height,
#                 '{}'.format(height), ha=ha[xpos], va='bottom')
#
#
# autolabel(rects1, "left")
# autolabel(rects2, "right")
#
# plt.show()

# #折线图
# import matplotlib.pyplot as plt
#
# cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
# dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
# activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
#
# fig, ax = plt.subplots()
# ax.plot(activity, dog, label="dog")
# ax.plot(activity, cat, label="cat")
# ax.legend()
#
# plt.show()
#
# 点折图
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Fixing random state for reproducibility
# np.random.seed(196808)
#
#
# x = np.arange(0.0, 50.0, 2.0)
# y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
# s = np.random.rand(*x.shape) * 800 + 500
#
# plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.show()

# 饼状图
# import matplotlib.pyplot as plt
#
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

