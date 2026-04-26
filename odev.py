import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

R = np.sin(X**2 + Y**2)
G = np.cos(X * Y)
B = np.sin(X + Y)

R_norm = np.sin(X**2 + Y**2) * np.exp(-np.abs(X+Y)/5)
G_norm = np.cos(X * Y) + np.sin(X * Y)
B_norm = np.abs(np.sin(X) * np.cos(Y))

rgb_image = np.dstack((R_norm, G_norm, B_norm))

fig = plt.figure(figsize=(15, 6))

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(rgb_image)
ax1.set_title("Matematiksel İfadelerle Üretilen RGB Resim")
ax1.axis('off')

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf = ax2.plot_surface(X, Y, R_norm, cmap='Reds', edgecolor='none', alpha=0.9)
ax2.set_title("Kırmızı (R) Kanalının 3B Yüzey Çizimi (Mesh)")
ax2.set_xlabel('X Ekseni')
ax2.set_ylabel('Y Ekseni')
ax2.set_zlabel('Renk Yoğunluğu (0-1)')

fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()
