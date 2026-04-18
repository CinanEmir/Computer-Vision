import numpy as np
import matplotlib.pyplot as plt

# 1. Grid (Izgara) Oluşturma
# -5 ile 5 arasında 500'er noktalık x ve y uzayları (500x500 çözünürlük)
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

# 2. Matematiksel İfadeler (Random kullanmadan)
# R, G ve B kanalları için görsel olarak ilginç desenler (dalgalar, dairesel girişimler) oluşturan fonksiyonlar
R = np.sin(X**2 + Y**2)       # Dairesel dalgalanma (Ripple effect)
G = np.cos(X * Y)             # Çapraz hiperbolik desenler
B = np.sin(X + Y)             # Çapraz çizgisel dalgalar

# 3. Normalizasyon
# Matplotlib'in RGB resmi doğru gösterebilmesi için değerleri 0 ile 1 aralığına çekiyoruz.
R_norm = np.sin(X**2 + Y**2) * np.exp(-np.abs(X+Y)/5)
G_norm = np.cos(X * Y) + np.sin(X * Y)
B_norm = np.abs(np.sin(X) * np.cos(Y))

# RGB matrisini birleştirme (Boyut: 500 x 500 x 3)
rgb_image = np.dstack((R_norm, G_norm, B_norm))

# 4. Görselleştirme (2D Resim ve 3D Mesh)
fig = plt.figure(figsize=(15, 6))

# --- Sol Tarafa 2D RGB Resmi Çizdirme ---
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(rgb_image)
ax1.set_title("Matematiksel İfadelerle Üretilen RGB Resim")
ax1.axis('off') # Eksenleri gizle

# --- Sağ Tarafa 3D Mesh (Yüzey) Çizdirme ---
# Görsel kalabalığı önlemek için örnek olarak sadece Kırmızı (R) kanalının 3B haritasını çizdiriyoruz.
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
# plot_surface fonksiyonu ile mesh yapısı oluşturulur
surf = ax2.plot_surface(X, Y, R_norm, cmap='Reds', edgecolor='none', alpha=0.9)
ax2.set_title("Kırmızı (R) Kanalının 3B Yüzey Çizimi (Mesh)")
ax2.set_xlabel('X Ekseni')
ax2.set_ylabel('Y Ekseni')
ax2.set_zlabel('Renk Yoğunluğu (0-1)')

# Renk skalasını (colorbar) grafiğin yanına ekleme
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

# Grafikleri ekranda göster
plt.tight_layout()
plt.show()