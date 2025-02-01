import cv2
import numpy as np
import torch

# Cargar modelo MiDaS DPT Large para mejor precisión
model = torch.hub.load("intel-isl/MiDaS", "DPT_Large", trust_repo=True)
model.eval()

# Cargar imagen original
image = cv2.imread("zeus3.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Obtener tamaño original
orig_height, orig_width = image.shape[:2]

# Redimensionar manteniendo la relación de aspecto (múltiplos de 32 para MiDaS)
new_width = (orig_width // 32) * 32
new_height = (orig_height // 32) * 32
image_resized = cv2.resize(image, (new_width, new_height))

# Preprocesar imagen para MiDaS
input_tensor = torch.from_numpy(image_resized).permute(2, 0, 1).unsqueeze(0).float() / 255.0

# Generar mapa de profundidad con el modelo
with torch.no_grad():
    depth_map = model(input_tensor)
    depth_map = torch.nn.functional.interpolate(
        depth_map.unsqueeze(1),
        size=(new_height, new_width),
        mode="bicubic",
        align_corners=False
    ).squeeze()

# Convertir a numpy
depth_map = depth_map.cpu().numpy()

# Normalizar entre 0-255
depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Aplicar filtro bilateral para suavizar sin perder bordes
depth_map = cv2.bilateralFilter(depth_map, 9, 75, 75)

# Aplicar CLAHE para mejorar contraste del mapa de profundidad
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
depth_map = clahe.apply(depth_map)

# Aplicar medianBlur para reducir artefactos
depth_map = cv2.medianBlur(depth_map, 5)

# Invertir la profundidad para Facebook (solo si es necesario)
depth_map = cv2.bitwise_not(depth_map)

# Convertir a 3 canales (Facebook a veces requiere RGB)
depth_map = cv2.cvtColor(depth_map, cv2.COLOR_GRAY2RGB)

# Redimensionar al tamaño original
depth_map = cv2.resize(depth_map, (orig_width, orig_height))
image_resized = cv2.resize(image_resized, (orig_width, orig_height))

# Guardar imágenes con la calidad más alta posible
cv2.imwrite("zeus.jpg", cv2.cvtColor(image_resized, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite("zeus_depth.jpg", depth_map, [cv2.IMWRITE_JPEG_QUALITY, 100])

print("✅ Imagen 3D y mapa de profundidad optimizados generados con éxito.")
