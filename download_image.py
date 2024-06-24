import requests
from datetime import datetime
from PIL import Image
import os

# 获取当前日期
today = datetime.today().strftime('%Y%m%d')
year = datetime.today().strftime('%Y')
month_day = datetime.today().strftime('%m%d')

# 图片 URL
url = f"https://img.owspace.com/Public/uploads/Download/{year}/{month_day}.jpg"

# 保存路径
filename = f"images/{today}.jpg"
output_dir = "Wallpaper"
output_filename = os.path.join(output_dir, "today.png")

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 下载图片
response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Image saved as {filename}")
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")
    exit(1)

# 裁剪和压缩图片
try:
    with Image.open(filename) as img:
        # 原始尺寸
        original_width, original_height = img.size
        print(f"Original size: {original_width}x{original_height}")

        # 裁剪图片，保持居中
        target_width, target_height = 758, 1024
        left = (original_width - target_width) / 2
        top = (original_height - target_height) / 2
        right = (original_width + target_width) / 2
        bottom = (original_height + target_height) / 2

        cropped_img = img.crop((left, top, right, bottom))

        # 保存为 PNG
        cropped_img.save(output_filename, "PNG")
        print(f"Processed image saved as {output_filename}")
except Exception as e:
    print(f"Failed to process image: {e}")
    exit(1)
