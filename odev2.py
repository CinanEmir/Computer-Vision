import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# 1. Resmi Yükleme
# KENDİ RESMİNİN ADINI BURAYA YAZ:
image_path = "ornek_resim.jpg" 
img = cv2.imread(image_path)

if img is None:
    print(f"Hata: '{image_path}' bulunamadı! Resmin kod ile aynı klasörde olduğundan emin ol.")
else:
    # OpenCV resimleri BGR (Blue, Green, Red) formatında okur. 
    # Matplotlib'in doğru renkleri göstermesi için bunu RGB'ye çeviriyoruz.
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 2. Ön İşlem: Kare Formatına Getirme ve Boyutlandırma
    # Resmin en ve boyundan küçük olanı bulup merkezi baz alarak tam kare kırpıyoruz.
    h, w, _ = img.shape
    min_dim = min(h, w)
    
    start_x = w // 2 - min_dim // 2
    start_y = h // 2 - min_dim // 2
    cropped_img = img[start_y:start_y + min_dim, start_x:start_x + min_dim]

    # 3x3 (9 parça) için tam bölünebilir bir boyut seçiyoruz (Örn: 900x900)
    # Böylece her parça tam 300x300 piksel olacak.
    img_resized = cv2.resize(cropped_img, (900, 900))
    piece_size = 300

    # 3. Resmi Parçalara Ayırma (Dilimleme / Slicing)
    pieces = []
    for i in range(3):       # Satırlar (Y ekseni)
        for j in range(3):   # Sütunlar (X ekseni)
            y_start = i * piece_size
            y_end = (i + 1) * piece_size
            x_start = j * piece_size
            x_end = (j + 1) * piece_size
            
            # Matrisin ilgili kısmını kesip listeye ekliyoruz
            piece = img_resized[y_start:y_end, x_start:x_end]
            pieces.append(piece)

    # 4. Görselleştirme Hazırlığı (1 Orijinal + 3 Varyasyon = Yan yana 4 grafik)
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    # İlk sütuna orijinal resmi koyalım
    axes[0].imshow(img_resized)
    axes[0].set_title("Orijinal Resim (900x900)")
    axes[0].axis('off')

    # 5. Rastgele Dağılım ve 3 Farklı Bulmaca Üretimi
    for v in range(3): 
        # 0'dan 8'e kadar indeksleri içeren bir liste oluşturup karıştırıyoruz
        indices = list(range(9))
        random.shuffle(indices)

        # Parçaları yerleştireceğimiz yeni, boş bir siyah kanvas oluşturuyoruz
        puzzle_canvas = np.zeros((900, 900, 3), dtype=np.uint8)

        # Karıştırılmış indeks sırasına göre parçaları kanvasa diziyoruz
        for k, original_index in enumerate(indices):
            # k: Kanvastaki yeni sıra (0, 1, 2... 8)
            row_new = k // 3
            col_new = k % 3
            
            y_start = row_new * piece_size
            y_end = (row_new + 1) * piece_size
            x_start = col_new * piece_size
            x_end = (col_new + 1) * piece_size
            
            # Parçanın etrafına ince siyah bir sınır çizgisi eklemek istersen (Grid efekti için):
            # Seçilen parçanın bir kopyasını alıp kenarlarına siyah çizgi çekiyoruz.
            piece_with_border = pieces[original_index].copy()
            cv2.rectangle(piece_with_border, (0, 0), (piece_size-1, piece_size-1), (0, 0, 0), 3)

            # Parçayı kanvastaki yeni yerine yapıştırıyoruz
            puzzle_canvas[y_start:y_end, x_start:x_end] = piece_with_border

        # Oluşan bulmacayı ilgili alt grafiğe (subplot) çizdir
        axes[v+1].imshow(puzzle_canvas)
        axes[v+1].set_title(f"Varyasyon {v+1}")
        axes[v+1].axis('off')

    # Ekranda Göster
    plt.tight_layout()
    plt.show()