import os
import psycopg2
from psycopg2.extras import RealDictCursor
from models.libro import Libro
from dotenv import load_dotenv

load_dotenv()

class LibroService:
    @staticmethod
    def get_connection():
        # Soporte para local (.env) y Streamlit Cloud (Secrets)
        db_url = os.getenv("DATABASE_URL")
        return psycopg2.connect(db_url)

    @staticmethod
    def listar_libros():
        conn = LibroService.get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM libros ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        libros = []
        for row in rows:
            libros.append(Libro(
                id=row['id'],
                sku=row.get('sku'),
                titulo=row['titulo'],
                autor=row['autor'],
                precio_costo=float(row.get('precio_costo', 0)),
                precio_venta=float(row.get('precio_venta', 0)),
                stock=int(row.get('stock', 0))
            ))
        return libros

    @staticmethod
    def registrar_libro(libro: Libro):
        conn = LibroService.get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO libros (sku, titulo, autor, precio_costo, precio_venta, stock)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            libro.sku, libro.titulo, libro.autor, 
            libro.precio_costo, libro.precio_venta, libro.stock
        ))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def actualizar_libro(id_libro, libro: Libro):
        conn = LibroService.get_connection()
        cur = conn.cursor()
        query = """
            UPDATE libros 
            SET sku=%s, titulo=%s, autor=%s, precio_costo=%s, precio_venta=%s, stock=%s
            WHERE id = %s
        """
        cur.execute(query, (
            libro.sku, libro.titulo, libro.autor, 
            libro.precio_costo, libro.precio_venta, libro.stock,
            id_libro
        ))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def eliminar_libro(libro_id):
        conn = LibroService.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def eliminar_libro_por_sku(sku):
        conn = LibroService.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM libros WHERE sku = %s", (sku,))
        conn.commit()
        cur.close()
        conn.close()
