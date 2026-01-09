from app.db.session import engine

try:
    conn = engine.connect()
    print("✅ Conexión a PostgreSQL exitosa")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
