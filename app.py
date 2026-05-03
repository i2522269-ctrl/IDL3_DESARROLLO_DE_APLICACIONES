import streamlit as st
from models.libro import Libro
from services.libro_service import LibroService
from utils.libro_utils import mostrar_tabla_libros, mostrar_analisis_inventario

st.set_page_config(page_title="Librería Supabase", page_icon="📚")

st.title("📚 Gestión de Librería (Python + Supabase)")

# Formulario de registro
with st.expander("📝 Registrar Nuevo Libro", expanded=True):
    with st.form("registro_libro"):
        col1, col2 = st.columns(2)
        sku = col1.text_input("SKU / ID")
        titulo = col2.text_input("Título")
        autor = st.text_input("Autor")
        
        c1, c2, c3 = st.columns(3)
        p_costo = c1.number_input("Precio Costo", min_value=0.0)
        p_venta = c2.number_input("Precio Venta", min_value=0.0)
        stock = c3.number_input("Stock", min_value=0, step=1)
        
        submitted = st.form_submit_button("Guardar en Supabase")
        
        if submitted:
            if titulo and sku:
                nuevo_libro = Libro(titulo, autor, p_costo, p_venta, stock, sku=sku)
                try:
                    LibroService.registrar_libro(nuevo_libro)
                    st.success(f"✅ Libro '{titulo}' guardado correctamente")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {e}")
            else:
                st.warning("El SKU y el Título son obligatorios")

# Listado y Análisis
st.divider()
st.subheader("📋 Inventario Actual")

try:
    libros_db = LibroService.listar_libros()
    mostrar_analisis_inventario(libros_db)
    mostrar_tabla_libros(libros_db)
except Exception as e:
    st.error("No se pudo conectar con Supabase. Verifica tus credenciales en 'services/libro_service.py'")
    st.info("Nota: Asegúrate de tener la tabla 'libros' creada en Supabase.")
