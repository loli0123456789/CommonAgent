import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或其他支持中文的字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 数据
labels = [
    "百万医疗", "百万自驾意外", "财富人生两全寿", "其他产品", "新定义重疾",
    "鑫如意终身寿", "意外医疗", "银保御立方", "银保御立方员工", "御如意",
    "御享人生", "重疾豁免", "住院津贴", "住院医疗", "总计"
]
before_fee = [
    11834930.15, 52854248.55, 31645044.81, 14987339.74, 18479834.39,
    100064632.07, 10778978.35, 309356957.90, 68362622.40, 210287524.76,
    329020431.58, 51738876.94, 7696816.87, 23228447.46, 1240336685.95
]
after_fee = [
    11834930.15, 52854248.55, 31645044.81, 14987339.74, 18479834.39,
    100064632.07, 10778978.35, 351281010.41, 78825495.01, 237931668.26,
    367752601.15, 51738876.94, 7696816.87, 23228447.46, 1359099924.16
]

# 设置图表
x = np.arange(len(labels))  # 标签位置
width = 0.35  # 柱子宽度

fig, ax = plt.subplots(figsize=(18, 10))  # 增大图表尺寸
rects1 = ax.bar(x - width/2, before_fee, width, label='调费前总保费', color='skyblue')
rects2 = ax.bar(x + width/2, after_fee, width, label='调费后总保费', color='orange')

# 添加标签、标题和图例
ax.set_xlabel('产品名称', fontsize=14)
ax.set_ylabel('总保费 (亿元)', fontsize=14)  # 单位改为“亿元”
ax.set_title('调费前后总保费对比', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=12)  # 调整字体大小和旋转角度
ax.legend(fontsize=12)

# 显示数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:  # 避免高度为0时标注出错
            ax.annotate(f'{height / 1e8:.2f}亿',  # 将数值转换为“亿元”单位
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 偏移量
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10)

autolabel(rects1)
autolabel(rects2)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()