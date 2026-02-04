import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Kameradan gelmiş gibi SAHTE bir RGB görüntü üret
# 100x100 boyutunda, 3 kanallı (RGB)
image = np.random.randint(
    low=0,
    high=256,
    size=(100, 100, 3),
    dtype=np.uint8
)

print("Shape:", image.shape)
print("Dtype:", image.dtype)
print("Min pixel:", image.min())
print("Max pixel:", image.max())

# 2️⃣ Görüntüyü göster
plt.imshow(image)
plt.title("Original Image (uint8)")
plt.axis("off")
plt.show()

# 3️⃣ AI için NORMALIZE et (0–255 → 0–1)
image_normalized = image.astype(np.float32) / 255.0

print("\nAfter normalization:")
print("Dtype:", image_normalized.dtype)
print("Min pixel:", image_normalized.min())
print("Max pixel:", image_normalized.max())

# 4️⃣ Kanal sırasını değiştir (HWC → CHW)
# CNN'ler genelde bunu ister
image_chw = np.transpose(image_normalized, (2, 0, 1))

print("\nAfter transpose:")
print("New shape:", image_chw.shape)

# 5️⃣ Batch dimension ekle (model input gibi)
# (C, H, W) → (1, C, H, W)
image_batch = np.expand_dims(image_chw, axis=0)

print("\nFinal model input shape:", image_batch.shape)
