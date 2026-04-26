import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

image_path = "ornek_resim.jpg" 
img = cv2.imread(image_path)

if img is None:
    print(f"Hata: '{image_path}' bulunamadı! Resmin kod ile aynı klasörde olduğundan emin ol.")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w, _ = img.shape
    min_dim = min(h, w)
    
    start_x = w // 2 - min_dim // 2
    start_y = h // 2 - min_dim // 2
    cropped_img = img[start_y:start_y + min_dim, start_x:start_x + min_dim]

    img_resized = cv2.resize(cropped_img, (900, 900))
    piece_size = 300

    pieces = []
    for i in range(3):
        for j in range(3):
            y_start = i * piece_size
            y_end = (i + 1) * piece_size
            x_start = j * piece_size
            x_end = (j + 1) * piece_size
            
            piece = img_resized[y_start:y_end, x_start:x_end]
            pieces.append(piece)

    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    axes[0].imshow(img_resized)
    axes[0].set_title("Orijinal Resim (900x900)")
    axes[0].axis('off')

    for v in range(3): 
        indices = list(range(9))
        random.shuffle(indices)

        puzzle_canvas = np.zeros((900, 900, 3), dtype=np.uint8)

        for k, original_index in enumerate(indices):
            row_new = k // 3
            col_new = k % 3
            
            y_start = row_new * piece_size
            y_end = (row_new + 1) * piece_size
            x_start = col_new * piece_size
            x_end = (col_new + 1) * piece_size
            
            piece_with_border = pieces[original_index].copy()
            cv2.rectangle(piece_with_border, (0, 0), (piece_size-1, piece_size-1), (0, 0, 0), 3)

            puzzle_canvas[y_start:y_end, x_start:x_end] = piece_with_border

        axes[v+1].imshow(puzzle_canvas)
        axes[v+1].set_title(f"Varyasyon {v+1}")
        axes[v+1].axis('off')

    plt.tight_layout()
    plt.show()
