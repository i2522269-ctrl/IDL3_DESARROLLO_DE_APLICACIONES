import os
from supabase import create_client, Client
from models.libro import Libro

from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class LibroService:
    @staticmethod
    def get_client() -> Client:
        return create_client(SUPABASE_URL, SUPABASE_KEY)

    @staticmethod
    def listar_libros():
        supabase = LibroService.get_client()
        response = supabase.table("libros").select("*").execute()
        
        libros = []
        for item in response.data:
            libros.append(Libro(
                id=item['id'],
                sku=item.get('sku'),
                titulo=item['titulo'],
                autor=item['autor'],
                precio_costo=float(item.get('precio_costo', 0)),
                precio_venta=float(item.get('precio_venta', 0)),
                stock=int(item.get('stock', 0))
            ))
        return libros

    @staticmethod
    def registrar_libro(libro: Libro):
        supabase = LibroService.get_client()
        data = {
            "sku": libro.sku,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "precio_costo": libro.precio_costo,
            "precio_venta": libro.precio_venta,
            "stock": libro.stock
        }
        return supabase.table("libros").insert(data).execute()

    @staticmethod
    def eliminar_libro(libro_id):
        supabase = LibroService.get_client()
        return supabase.table("libros").delete().eq("id", libro_id).execute()
