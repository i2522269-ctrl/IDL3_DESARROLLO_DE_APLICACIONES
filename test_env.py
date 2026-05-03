import os
from dotenv import load_dotenv

print("Directorio actual:", os.getcwd())
print("¿Existe .env?:", os.path.exists(".env"))

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print(f"URL: {url}")
print(f"KEY: {key[:10]}...")
