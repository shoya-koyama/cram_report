import numpy as np
import matplotlib.pyplot as plt

# データを生成する
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, 1000)
r = np.linspace(0.1, 1, 1000)
r, theta = np.meshgrid(r, theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

# プロットする
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.plot(theta, r, color='blue', linewidth=2)
ax.set_rmax(1)
ax.grid(True)
ax.set_title("A Spiral", va='bottom')
plt.show()