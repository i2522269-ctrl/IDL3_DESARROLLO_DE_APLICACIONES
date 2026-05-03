import os
from dotenv import load_dotenv
from services.libro_service import LibroService
from models.libro import Libro

def test_funcional():
    print("--- INICIANDO PRUEBA FUNCIONAL ---")
    
    # 1. Intentar listar libros
    try:
        print("Intentando conectar con Supabase...")
        libros = LibroService.listar_libros()
        print(f"Conexión exitosa. Libros encontrados: {len(libros)}")
        
        # 2. Intentar registrar un libro de prueba
        sku_test = "TEST-001"
        print(f"Intentando registrar libro de prueba ({sku_test})...")
        
        # Eliminar si ya existe para que la prueba no falle por SKU único
        LibroService.eliminar_libro_por_sku(sku_test) 
        
        test_libro = Libro(
            titulo="Libro de Prueba",
            autor="Bot de Prueba",
            precio_costo=10.0,
            precio_venta=20.0,
            stock=100,
            sku=sku_test
        )
        
        LibroService.registrar_libro(test_libro)
        print("OK: Registro exitoso.")
        
        # 3. Verificar que aparezca en la lista
        libros_final = LibroService.listar_libros()
        encontrado = any(l.sku == sku_test for l in libros_final)
        
        if encontrado:
            print("OK: Verificación exitosa: El libro aparece en la base de datos.")
        else:
            print("ERROR: El libro no se encontró tras el registro.")
            
    except Exception as e:
        print(f"ERROR DURANTE LA PRUEBA: {e}")

if __name__ == "__main__":
    test_funcional()
