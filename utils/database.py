# Manejo de conexiones y consultas a la bd
import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG

def init_connection():
    return psycopg2.connect(**DB_CONFIG)

def check_credentials(username, password):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute(
            "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s",
            (username, password)
        )
        user = cur.fetchone()
        return user
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return None
    finally:
        if conn:
            conn.close()

def check_gender(username):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute(
            "SELECT genero FROM usuarios WHERE usuario = %s",
            (username,)
        )
        result = cur.fetchone()
        
        if result:
            return "Bienvenido" if result['genero'] == 'masculino' else "Bienvenida"
        return "Bienvenido/a"
        
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return "Bienvenido/a"
    finally:
        if conn:
            conn.close()

def check_energia_generada_por_tipo_tecnologia_bd():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("SELECT * FROM energia_generada_por_tipo_tecnologia")
        result = cur.fetchall()
        
        return result
        
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return None
    finally:
        if conn:
            conn.close()