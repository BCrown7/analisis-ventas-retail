"""
Exploración rápida del dataset descargado & transformación a UTF-8
"""
import pandas as pd
import chardet

def detect_encoding(file_path):
    """Detecta la codificación del archivo"""
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Lee los primeros 10000 bytes
        result = chardet.detect(raw_data)
        return result['encoding']

def explore_dataset():
    """Muestra información básica del dataset"""
    
    file_path = 'data/raw/superstore_sales.csv'
    
    # Detectar codificación
    print("🔍 Detectando codificación del archivo...")
    try:
        encoding = detect_encoding(file_path)
        print(f"   Codificación detectada: {encoding}")
    except:
        encoding = 'latin-1'  # Alternativa común
        print(f"   Usando codificación por defecto: {encoding}")
    
    # Intentar cargar con diferentes codificaciones
    encodings_to_try = [encoding, 'utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    df = None
    
    for enc in encodings_to_try:
        try:
            print(f"\n📂 Intentando cargar con codificación: {enc}")
            df = pd.read_csv(file_path, encoding=enc)
            print(f"   ✅ Archivo cargado exitosamente con {enc}")
            break
        except UnicodeDecodeError:
            print(f"   ❌ Falló con {enc}")
            continue
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
    
    if df is None:
        print("\n❌ No se pudo cargar el archivo con ninguna codificación.")
        print("💡 Intenta abrir el archivo en Excel y guardarlo como CSV UTF-8")
        return
    
    print("\n" + "=" * 70)
    print("📊 EXPLORACIÓN RÁPIDA DEL DATASET")
    print("=" * 70)
    
    # Dimensiones
    print(f"\n1️⃣ DIMENSIONES:")
    print(f"   Filas: {df.shape[0]:,}")
    print(f"   Columnas: {df.shape[1]}")
    
    # Columnas
    print(f"\n2️⃣ COLUMNAS DEL DATASET:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i:2d}. {col}")
    
    # Tipos de datos
    print(f"\n3️⃣ TIPOS DE DATOS:")
    for col, dtype in df.dtypes.items():
        print(f"   {col:25s} : {dtype}")
    
    # Primeras filas
    print(f"\n4️⃣ PRIMERAS 5 FILAS:")
    print(df.head())
    
    # Información general
    print(f"\n5️⃣ INFORMACIÓN GENERAL:")
    df.info()
    
    # Estadísticas descriptivas (solo columnas numéricas)
    print(f"\n6️⃣ ESTADÍSTICAS DESCRIPTIVAS:")
    print(df.describe())
    
    # Valores nulos
    print(f"\n7️⃣ VALORES NULOS:")
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print(null_counts[null_counts > 0])
    else:
        print("   ✅ No hay valores nulos")
    
    # Valores únicos en columnas categóricas
    print(f"\n8️⃣ VALORES ÚNICOS (Columnas Categóricas):")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols[:10]:  # Primeras 10 columnas categóricas
        n_unique = df[col].nunique()
        print(f"   {col:25s} : {n_unique:,} valores únicos")
    
    print("\n" + "=" * 70)
    print("✅ Exploración completada")
    print("=" * 70)
    
    # Guardar el archivo con codificación correcta
    print("\n💾 Guardando archivo con codificación UTF-8...")
    output_path = 'data/raw/superstore_sales_utf8.csv'
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"   ✅ Archivo guardado: {output_path}")

if __name__ == "__main__":
    explore_dataset()