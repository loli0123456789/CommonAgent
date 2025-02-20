from PIL import Image

# 打开图标
image = Image.open("src/test/icon.png")
# print(image.)

# 获取像素数据
data = image.getdata()


# 替换蓝色为白色
new_data = []
for item in data:
    if item[0] < 100 and item[1] < 100 and item[2] > 100:  # 判断蓝色区域
        new_data.append((255, 255, 255, item[3]))  # 替换为白色
    else:
        new_data.append(item)

# 更新图像数据并保存
image.putdata(new_data)
image.save("src/test/white_icon.png")