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
    
    # Mostrar tabla principal
    mostrar_tabla_libros(libros_db)
    
    # Sección de Edición y Eliminación
    st.divider()
    st.subheader("🛠️ Acciones de Gestión")
    
    if libros_db:
        # Selector de libro para acciones
        opciones = {f"{l.sku} - {l.titulo}": l for l in libros_db}
        seleccion = st.selectbox("Seleccione un libro para Editar o Eliminar:", ["-- Seleccionar --"] + list(opciones.keys()))
        
        if seleccion != "-- Seleccionar --":
            libro_sel = opciones[seleccion]
            
            col_ed, col_el = st.columns(2)
            
            # Formulario de Edición
            with col_ed.expander(f"📝 Editar: {libro_sel.titulo}"):
                with st.form(f"form_edit_{libro_sel.id}"):
                    new_sku = st.text_input("SKU", value=libro_sel.sku)
                    new_titulo = st.text_input("Título", value=libro_sel.titulo)
                    new_autor = st.text_input("Autor", value=libro_sel.autor)
                    new_p_costo = st.number_input("Precio Costo", value=float(libro_sel.precio_costo))
                    new_p_venta = st.number_input("Precio Venta", value=float(libro_sel.precio_venta))
                    new_stock = st.number_input("Stock", value=int(libro_sel.stock))
                    
                    if st.form_submit_button("Actualizar Cambios"):
                        libro_upd = Libro(new_titulo, new_autor, new_p_costo, new_p_venta, new_stock, sku=new_sku)
                        LibroService.actualizar_libro(libro_sel.id, libro_upd)
                        st.success("¡Libro actualizado!")
                        st.rerun()
            
            # Botón de Eliminación
            with col_el.expander("⚠️ Zona de Peligro"):
                st.warning(f"¿Está seguro de eliminar '{libro_sel.titulo}'?")
                if st.button(f"Confirmar Eliminación de {libro_sel.sku}", type="primary"):
                    LibroService.eliminar_libro(libro_sel.id)
                    st.success("Libro eliminado correctamente")
                    st.rerun()

except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.info("Asegúrate de haber configurado los Secrets en Streamlit Cloud o el archivo .env local.")
