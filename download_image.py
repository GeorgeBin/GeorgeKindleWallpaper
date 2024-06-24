import requests
from datetime import datetime, timedelta
from PIL import Image
import os

# 获取明天的日期
tomorrow = datetime.now() + timedelta(days=1)
year = tomorrow.strftime('%Y')
month_day = tomorrow.strftime('%m%d')

# 图片 URL
url = f"https://img.owspace.com/Public/uploads/Download/{year}/{month_day}.jpg"

# 保存路径
filename = f"images/{tomorrow.strftime('%Y%m%d')}.jpg"
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
        # 剪裁图片
        left = 60
        top = 100
        right = img.width - 60
        bottom = img.height - 312
        cropped_img = img.crop((left, top, right, bottom))

        # 压缩图片
        target_width, target_height = 758, 1024
        resized_img = cropped_img.resize((target_width, target_height), Image.LANCZOS)

        # 保存为 PNG
        resized_img.save(output_filename, "PNG")
        print(f"Processed image saved as {output_filename}")
except Exception as e:
    print(f"Failed to process image: {e}")
    exit(1)
