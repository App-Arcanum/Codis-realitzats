import firebase_admin
from firebase_admin import credentials, firestore

# Inicialización de Firebase solo si aún no ha sido inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("diffie-hellman-db-49794e21735d.json")
    firebase_admin.initialize_app(cred)

# Inicializar cliente de Firestore
db = firestore.client()

def readPublicKey():
    try:
        print("Leyendo...")
        docs = db.collection("Public_Keys").limit(1).stream()
        for doc in docs:
            data = doc.to_dict()
            return data.get('Key_P'), data.get('Key_Q')
        print("No se encontró ninguna clave pública.")
        return None, None
    except Exception as e:
        print(f"Error al leer la clave pública: {e}")
        return None, None

def writePublicKey(key_P: int, key_Q: int):
    try:
        print("Guardando...")
        new_data = {"Key_P": key_P, "Key_Q": key_Q}
        db.collection("Public_Keys").add(new_data)
        print("Información guardada con éxito.")
    except Exception as e:
        print(f"Error al guardar la clave pública: {e}")

def writeMezcla(usuari: str, M: int): 
    try:
        print("Guardando...")
        new_data = {"Mezcla": M}
        db.collection("Mezclas").document(usuari).set(new_data)
        print("Información guardada con éxito.")
    except Exception as e:
        print(f"Error al guardar la mezcla: {e}")

def readMezclaKey(usuari: str):
    try:
        print("Leyendo...")
        doc = db.collection("Mezclas").document(usuari).get()
        if doc.exists:
            return doc.to_dict().get('Mezcla')
        else:
            print("Usuario no encontrado.")
            return None
    except Exception as e:
        print(f"Error al leer la mezcla: {e}")
        return None

def borrar_todo():
    try:
        print("Borrando Base de Datos...")

        # Borrar documentos de Mezclas
        mezclas = db.collection("Mezclas").stream()
        for doc in mezclas:
            db.collection("Mezclas").document(doc.id).delete()

        # Borrar documentos de Public_Keys
        public_keys = db.collection("Public_Keys").stream()
        for doc in public_keys:
            db.collection("Public_Keys").document(doc.id).delete()

        print("Todos los documentos han sido eliminados.")
    except Exception as e:
        print(f"Error al borrar los datos: {e}")
