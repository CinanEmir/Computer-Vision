# 🎨 Görüntü İşleme: Matematiksel Sentez ve Jigsaw Bulmaca

Bu proje, temel görüntü işleme algoritmalarını ve matris manipülasyonlarını pratik etmek amacıyla Python ile geliştirilmiş iki aşamalı bir bilgisayarlı görü (computer vision) çalışmasıdır.

## 🚀 Proje İçeriği ve Özellikler

* **1. Matematiksel RGB Görüntü Sentezi:** Herhangi bir rastgelelik (random) fonksiyonu kullanılmadan, tamamen X ve Y uzamsal koordinatlarına bağlı trigonometrik ve üstel fonksiyonlar (sinüs, kosinüs) yardımıyla yapay RGB görüntüler elde edilir. Renk kanallarının (Z ekseni yoğunluğunun) matematiksel karşılıkları 3 Boyutlu Yüzey (Mesh) grafikleriyle görselleştirilir.

* **2. Matris Tabanlı Jigsaw Bulmaca Üretimi:** Girdi olarak alınan herhangi bir görüntü, dinamik olarak kare formata getirilip 3x3'lük (9 parça) matrislere bölünür (slicing). Parçaların indeksleri karıştırılarak, orijinal görüntünün rastgele dağıtılmış çoklu bulmaca varyasyonları sentezlenir ve ekranda yan yana sergilenir.

## 🛠️ Kullanılan Teknolojiler
* **Python**
* **NumPy** (Matris cebiri ve vektörel işlemler)
* **OpenCV** (Görüntü okuma, boyutlandırma ve ön işleme)
* **Matplotlib** (2D görüntü matrisleri ve 3D yüzey görselleştirmesi)

## ⚙️ Kurulum ve Kullanım

Projenin çalışması için sisteminizde Python yüklü olmalıdır. Gerekli kütüphaneleri kurmak için terminalinize aşağıdaki komutu girebilirsiniz:

```bash
pip install numpy opencv-python matplotlib
