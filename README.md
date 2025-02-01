# 📸 Convierte Fotos en 3D con Python

Este proyecto te permite transformar imágenes 2D en impresionantes **fotos 3D** utilizando Python, OpenCV y el modelo MiDaS para generar **mapas de profundidad**. Perfecto para crear imágenes listas para compartir en Facebook y redes sociales.

---

## 🚀 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) GPU NVIDIA para acelerar el procesamiento con PyTorch

---

## 🛠️ Instalación

### 1️⃣ Clonar el repositorio (si aplica)
```bash
git clone https://github.com/kiboki1234/Imagenes3D.git
cd tu-repositorio
```

### 2️⃣ (Opcional) Crear un entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux o macOS:
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

#### ✅ Para sistemas sin GPU (versión CPU)
```bash
pip install -r requirements.txt
```

#### ⚡ Para sistemas con GPU (CUDA 12.1)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

---

## 📋 Dependencias incluidas en `requirements.txt`
```txt
# Procesamiento de imágenes
opencv-python

# Manejo de arreglos numéricos
numpy

# PyTorch (CPU)
torch
torchvision
torchaudio

# Modelo MiDaS
 t imm
```

### 🔄 Actualizar las librerías (recomendado)
```bash
pip install --upgrade opencv-python numpy torch torchvision timm
```

---

## 🚀 Cómo Usar

1. Coloca la imagen que deseas convertir en la carpeta del proyecto.
2. Modifica el script para apuntar al nombre de tu imagen (`zeus3.jpg`, por ejemplo).
3. Ejecuta el script:
```bash
python script.py
```
4. Se generarán dos archivos:
   - `zeus.jpg` (imagen original procesada)
   - `zeus_depth.jpg` (mapa de profundidad)

5. **Sube ambos archivos a Facebook al mismo tiempo** para obtener el efecto 3D.

---

## 🧩 Contribuciones
¡Se aceptan mejoras, correcciones de errores y nuevas funcionalidades! 🚀

1. Haz un fork del repositorio.
2. Crea una rama para tu función (`git checkout -b nueva-funcionalidad`).
3. Haz tus cambios y realiza un commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tu rama (`git push origin nueva-funcionalidad`).
5. Abre un Pull Request.

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 📢 Contacto
- YouTube: [Enlace al tutorial](https://youtu.be/4QZAWQZ0OUE)
- GitHub: [https://github.com/tu-usuario](https://github.com/kiboki1234)
- Facebook: [@tuusuario](https://www.facebook.com/kibotech.org)
- Kibotech: [Enlace de kibotech](https://kibotech.org/)

---

¡Dale vida a tus imágenes y comparte increíbles fotos 3D! 🎉📷

