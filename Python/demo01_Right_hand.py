import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建3D图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 设置坐标轴原点
origin = [0, 0, 0]

# 定义坐标轴向量
X = [1, 0, 0]  # X轴方向
Y = [0, 1, 0]  # Y轴方向
Z = [0, 0, 1]  # Z轴方向

# 绘制坐标轴
ax.quiver(origin[0], origin[1], origin[2], X[0], X[1], X[2], 
          color='red', arrow_length_ratio=0.1, linewidth=3, label='X轴')
ax.quiver(origin[0], origin[1], origin[2], Y[0], Y[1], Y[2], 
          color='green', arrow_length_ratio=0.1, linewidth=3, label='Y轴')
ax.quiver(origin[0], origin[1], origin[2], Z[0], Z[1], Z[2], 
          color='blue', arrow_length_ratio=0.1, linewidth=3, label='Z轴')

# 添加坐标轴标签
ax.text(1.1, 0, 0, 'X', fontsize=16, color='red', fontweight='bold')
ax.text(0, 1.1, 0, 'Y', fontsize=16, color='green', fontweight='bold')
ax.text(0, 0, 1.1, 'Z', fontsize=16, color='blue', fontweight='bold')

# 绘制右手示意
# 拇指指向X轴
thumb_x = np.array([0.3, 0.5])
thumb_y = np.array([0, 0])
thumb_z = np.array([0, 0])
ax.plot(thumb_x, thumb_y, thumb_z, 'r-', linewidth=4, alpha=0.7)

# 食指指向Y轴
finger_x = np.array([0, 0])
finger_y = np.array([0.3, 0.5])
finger_z = np.array([0, 0])
ax.plot(finger_x, finger_y, finger_z, 'g-', linewidth=4, alpha=0.7)

# 中指指向Z轴
middle_x = np.array([0, 0])
middle_y = np.array([0, 0])
middle_z = np.array([0.3, 0.5])
ax.plot(middle_x, middle_y, middle_z, 'b-', linewidth=4, alpha=0.7)

# 添加右手法则说明文字
ax.text(0.6, 0, 0, '食指(X)', fontsize=12, color='red')
ax.text(0, 0.6, 0, '中指(Y)', fontsize=12, color='green')
ax.text(0, 0, 0.6, '拇指(Z)', fontsize=12, color='blue')

# 设置坐标轴范围
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-0.5, 1.5])

# 设置坐标轴标签
ax.set_xlabel('X轴', fontsize=14)
ax.set_ylabel('Y轴', fontsize=14)
ax.set_zlabel('Z轴', fontsize=14)

# 设置标题
ax.set_title('右手坐标系\n(Right-Hand Coordinate System)', fontsize=16, fontweight='bold')

# 添加网格
ax.grid(True, alpha=0.3)

# 设置视角
ax.view_init(elev=20, azim=45)

# 添加图例
ax.legend(loc='upper left')

# 添加说明文字
fig.text(0.02, 0.02, '右手法则：食指指向X轴，中指指向Y轴，拇指指向Z轴', 
         fontsize=12, ha='left')

# 创建与文件同名的文件夹
script_name = os.path.splitext(os.path.basename(__file__))[0]
output_dir = os.path.join(os.path.dirname(__file__), script_name)
os.makedirs(output_dir, exist_ok=True)

# 保存图片到文件夹中
plt.tight_layout()
png_path = os.path.join(output_dir, 'right_hand_coordinate_system.png')
svg_path = os.path.join(output_dir, 'right_hand_coordinate_system.svg')
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.savefig(svg_path, format='svg', bbox_inches='tight')

# 显示图片
plt.show()

print(f"右手坐标系图片已生成到文件夹: {output_dir}")
print(f"- {png_path}")
print(f"- {svg_path}")