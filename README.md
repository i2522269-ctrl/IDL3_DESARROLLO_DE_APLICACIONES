# 📚 IDL3 - Gestión de Librería con Supabase

Este proyecto es una aplicación web interactiva desarrollada en **Python** utilizando **Streamlit** para la gestión de inventarios, con persistencia de datos en la nube a través de **Supabase**.

## 🚀 Características
- **CRUD Completo**: Registro, listado y eliminación de libros en tiempo real con Supabase.
- **Análisis de Inventario**: Cálculo automático de inversión total y métricas de stock.
- **Arquitectura Limpia**: Separación en capas (Models, Services, Utils).
- **Seguridad**: Manejo de credenciales mediante variables de entorno (`.env`).
- **Diseño Moderno**: Interfaz interactiva y profesional.

## 📂 Estructura del Proyecto
```text
├── models/          # Definición de clases (POO)
├── services/        # Lógica de conexión a Supabase
├── utils/           # Funciones auxiliares de UI y lógica
├── .env.example     # Plantilla de configuración
├── app.py           # Punto de entrada de la aplicación
└── requirements.txt # Dependencias del proyecto
```

## 🛠️ Configuración e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/i2522269-ctrl/IDL3_DESARROLLO_DE_APLICACIONES.git
   ```

2. **Configurar el entorno virtual:**
   ```bash
   python -m venv venv_idl3_dda
   .\venv_idl3_dda\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Variables de Entorno:**
   Crea un archivo `.env` basado en `.env.example` con tu URL y Key de Supabase:
   - `SUPABASE_URL`: Tu URL del proyecto (ej: https://ayzkscicyshinzpjhzue.supabase.co)
   - `SUPABASE_KEY`: Tu Anon Public Key.

4. **Ejecutar la App:**
   ```bash
   streamlit run app.py
   ```

---
Desarrollado para el curso de **Desarrollo de Aplicaciones**.
