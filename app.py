import streamlit as st
import pandas as pd
from services.libro_service import LibroService

# Configuración de página
st.set_page_config(page_title="Librería - Gestión de Costos", page_icon="📚", layout="wide")

# Inicialización
LibroService.inicializar_inventario()

# Título y Diseño
st.title("📚 Sistema de Gestión de Mercadería (Librería)")
st.markdown("---")

# Dashboard de Costos (Resumen)
resumen = LibroService.calcular_resumen_costos()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Inversión Total", f"S/ {resumen['total_inversion']:.2f}")
with col2:
    st.metric("Libros en Stock", f"{resumen['total_items']} unidades")
with col3:
    st.metric("Productos Registrados", len(LibroService.listar_libros()))

st.markdown("---")

# Layout de dos columnas: Registro y Listado
col_form, col_list = st.columns([1, 2])

with col_form:
    st.subheader("📝 Registrar Nuevo Libro")
    with st.form("registro_libro", clear_on_submit=True):
        id_libro = st.text_input("ID / SKU")
        titulo = st.text_input("Título del Libro")
        autor = st.text_input("Autor")
        
        c1, c2 = st.columns(2)
        p_costo = c1.number_input("Precio Costo (S/)", min_value=0.0, step=0.1)
        p_venta = c2.number_input("Precio Venta (S/)", min_value=0.0, step=0.1)
        
        stock = st.number_input("Stock Inicial", min_value=0, step=1)
        
        submitted = st.form_submit_button("Guardar Producto")
        
        if submitted:
            if id_libro and titulo:
                LibroService.registrar_libro(id_libro, titulo, autor, p_costo, p_venta, stock)
                st.success(f"✅ '{titulo}' registrado correctamente")
                st.rerun()
            else:
                st.error("Por favor completa el ID y el Título")

with col_list:
    st.subheader("📋 Inventario Actual")
    libros = LibroService.listar_libros()
    
    if libros:
        data = []
        for l in libros:
            data.append({
                "ID": l.id,
                "Título": l.titulo,
                "Autor": l.autor,
                "Costo": f"S/ {l.precio_costo:.2f}",
                "Venta": f"S/ {l.precio_venta:.2f}",
                "Stock": l.stock,
                "Subtotal Costo": f"S/ {l.valor_inventario():.2f}"
            })
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay libros registrados aún.")
