import streamlit as st
import pandas as pd

def mostrar_tabla_libros(libros):
    if not libros:
        st.info("No hay libros registrados.")
        return

    data = []
    for l in libros:
        data.append({
            "SKU": l.sku,
            "Título": l.titulo,
            "Autor": l.autor,
            "Venta": f"S/ {l.precio_venta:.2f}",
            "Stock": l.stock,
            "Subtotal Costo": f"S/ {l.calcular_subtotal_costo():.2f}"
        })
    
    df = pd.DataFrame(data)
    st.table(df)

def mostrar_analisis_inventario(libros):
    if not libros:
        return
        
    total_items = sum(l.stock for l in libros)
    inversion_total = sum(l.calcular_subtotal_costo() for l in libros)
    
    col1, col2 = st.columns(2)
    col1.metric("Total Unidades", f"{total_items}")
    col2.metric("Inversión Total", f"S/ {inversion_total:.2f}")
