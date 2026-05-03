import streamlit as st
from models.libro import Libro

class LibroService:
    @staticmethod
    def inicializar_inventario():
        if 'inventario' not in st.session_state:
            st.session_state.inventario = []

    @staticmethod
    def registrar_libro(id, titulo, autor, precio_costo, precio_venta, stock):
        nuevo_libro = Libro(id, titulo, autor, precio_costo, precio_venta, stock)
        st.session_state.inventario.append(nuevo_libro)
        return nuevo_libro

    @staticmethod
    def listar_libros():
        return st.session_state.inventario

    @staticmethod
    def calcular_resumen_costos():
        total_inversion = sum(libro.valor_inventario() for libro in st.session_state.inventario)
        total_items = sum(libro.stock for libro in st.session_state.inventario)
        return {
            "total_inversion": total_inversion,
            "total_items": total_items
        }
