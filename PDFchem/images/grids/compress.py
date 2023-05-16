from PIL import Image
import os

# 定义输入和输出文件夹路径
input_folder = "."
output_folder = "compressed"
#os.mkdir(output_folder)
# 定义压缩比例
quality = 10

# 遍历文件夹中的所有图片文件
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片文件
        with Image.open(os.path.join(input_folder, filename)) as im:
            # 压缩图片并保存到输出文件夹
            resized = im.resize((50,50))
            resized.save(os.path.join(output_folder, filename), optimize=True, quality=quality)