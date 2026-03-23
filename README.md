# 📊 Análisis de Ventas Retail - Proyecto de Portafolio

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0-green.svg)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completo-success.svg)]()

Análisis completo de datos de ventas retail para identificar patrones de rentabilidad, optimizar estrategias comerciales y desarrollar modelo predictivo de Machine Learning.

---

## > Resumen Ejecutivo

### El Problema
Una empresa retail genera **$2.3M en ventas** pero solo **$286K en ganancias** (margen del 12.47%). Casi **1 de cada 5 pedidos (19.4%) genera pérdidas**, eliminando $156K de ganancias potenciales.

### Hallazgo Principal
**El descuento es el factor dominante:** Los descuentos están destruyendo el 54.5% de las ganancias potenciales del negocio.

### Oportunidad Identificada
Implementando las recomendaciones del análisis, el negocio puede **aumentar ganancias entre 27-50%** sin incrementar ventas.

---

## > Resultados Clave

### 1. Análisis por Categoría

| Categoría | Ventas | Ganancias | Margen | Estado |
|-----------|--------|-----------|--------|--------|
| **Technology** | $836K | $145K (50.8%) | 17.4% | Mejor categoría |
| **Office Supplies** | $719K | $122K (42.8%) | 17.0% | Mejor volumen |
| **Furniture** | $742K | $18K (6.4%) | **2.5%** | Categoría en crisis |

**Insight Crítico:**
- **Tables (subcategoría):** Pérdidas de $17,725 en 319 pedidos (margen -8.56%)
- **Acción requerida:** Suspender ventas de Tables y revisar toda la estrategia de Furniture

---

### 2. Impacto de Descuentos
```
- Margen SIN descuento: 34.02% (saludable)
- Margen CON descuento: -8.27% (pérdidas)
```

**Datos Alarmantes:**
- 52% de pedidos tienen descuento
- 1,850 pedidos con descuento generan pérdidas directas
- Furniture con descuento tiene margen de **-30.88%** (pérdidas garantizadas)

**Recomendación:**
Implementar límites estrictos:
- Furniture: Máximo 5% (actualmente promedio 28.71%)
- Office Supplies: Máximo 15%
- Technology: Máximo 20%

---

### 3. Análisis de Clientes

| Segmento | Ventas | Ganancias | Margen | Pedidos No Rentables |
|----------|--------|-----------|--------|----------------------|
| Consumer | $1,161K | $134K | 11.6% | **19.32%** |
| Corporate | $706K | $92K | 13.0% | 18.41% |
| Home Office | $430K | $60K | **14.0%** | 17.50% |

**Top 10 clientes** generan $45K (15.8% del total) - alta concentración de valor.
**Acción:** Programa de fidelización para top clientes + revisar política de descuentos en Consumer.

---

### 4. Modelo Predictivo de Machine Learning

**Desempeño del Modelo:**
- **Accuracy: 94%** - predice correctamente 94 de cada 100 pedidos
- Detecta el **99.7% de pedidos rentables** (recall alto)
- Cuando predice "no rentable", acierta el **98.2%** (precision alta)

**Variable Más Importante:**
- **Discount: 69.8%** - el descuento es el factor dominante para predecir rentabilidad
- Las siguientes variables (Price_per_unit: 8.8%, Sales: 5%) tienen impacto mucho menor

**Aplicación Práctica:**
Sistema de alertas automático para pedidos con descuento > 15%. El modelo puede reducir significativamente los 1,936 pedidos no rentables identificados.

---

## > Recomendaciones Estratégicas

### Acciones Inmediatas:

1. **Suspender pedidos de Tables**
   - Pérdidas de $17,725 en 319 pedidos
   - Revisar estructura de costos antes de reanudar

2. **Implementar límites estrictos de descuentos**
   - Furniture: Máximo 5%
   - Office Supplies: Máximo 15%
   - Technology: Máximo 20%
   - Sistema de alertas para descuentos fuera de rango

3. **Revisión de Furniture**
   - Aumentar precios 8-10% O reducir costos operativos
   - Margen actual de 2.49% no es sostenible

---

### Acciones de Corto Plazo:

4. **Optimización de categorías**
   - Incrementar inventario de Technology (50.8% de ganancias)
   - Promocionar Copiers, Phones, Accessories (márgenes 13-37%)
   - Enfocar 80% del presupuesto de marketing en Technology y Office Supplies

5. **Programa de clientes**
   - Fidelización para top 10 clientes (generan 15.8% de ganancias)
   - Revisar política de descuentos en segmento Consumer (19.32% de pérdidas)

6. **Implementar modelo predictivo (ML)**
   - 94% de accuracy en predicción de rentabilidad
   - Sistema de alertas automáticas para pedidos de alto riesgo
   - Pre-aprobación requerida para pedidos con descuento > 15%

---

### Acciones de Mediano Plazo:

7. **Reestructuración de Furniture**
   - Evaluar si descontinuar línea completa o cambiar proveedor
   - Considerar modelo de dropshipping para reducir costos
   - Enfoque solo en productos con margen > 10%

8. **Análisis de costos detallado**
   - Identificar por qué Furniture tiene márgenes tan bajos
   - Negociar con proveedores o encontrar alternativas
   - Incluir costos de envío en el pricing

---

## > Tecnologías Utilizadas

### Stack de Análisis
- **Python 3.14** - Lenguaje principal
- **Pandas 3.0** - Manipulación y análisis de datos
- **NumPy 1.24** - Cálculos numéricos
- **Matplotlib 3.10 & Seaborn 0.13** - Visualizaciones

### Machine Learning
- **Scikit-learn 1.8** - Modelado predictivo
- **Random Forest Classifier** - Algoritmo seleccionado

### Entorno
- **Jupyter Notebook 1.1** - Análisis interactivo
- **VS Code** - Desarrollo
- **Git & GitHub** - Control de versiones

---

## > Estructura del Proyecto
```
analisis-ventas-retail/
│
├── data/
│   └── raw/
│       └── superstore_sales_utf8.csv    
│
├── notebooks/
│   └── analisis_ventas_retail.ipynb    
│
├── images/                              
│   ├── categoria_ventas_ganancias.png
│   ├── top_subcategorias.png
│   ├── analisis_regional.png
│   ├── estacionalidad_mensual.png
│   ├── top_10_customers.png
│   ├── distribucion_descuentos.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## > Configuración del Proyecto

### Requisitos Previos
- Python 3.9 o superior
- Git instalado

### Instalación Rápida

#### Windows & Mac/Linux
```bash
# Clonar repositorio
git clone https://github.com/BCrown7/analisis-ventas-retail.git
cd analisis-ventas-retail

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Abrir VS Code
code .
```

### Ejecutar Análisis
1. Abrir `notebooks/analisis_ventas_retail.ipynb` en VS Code
2. Seleccionar kernel: Python (analisis-ventas-retail)
3. Ejecutar todas las celdas: `Run All`

---

## > Dataset

### Fuente
- **Origen:** [Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Período:** 2014-2017
- **Registros:** 9,994 pedidos
- **Variables:** 21 columnas

### Columnas Principales
- **Order Date, Ship Date** - Temporalidad
- **Segment** - Consumer, Corporate, Home Office
- **Category, Sub-Category** - Clasificación de productos
- **Sales, Profit, Discount** - Métricas financieras
- **Region, State** - Geografía

---

## > Metodología

### 1. Exploración de Datos (EDA)
- Análisis por categoría y subcategoría
- Análisis geográfico (región y estado)
- Análisis temporal (anual, mensual, semanal)
- Análisis de clientes (segmentos y top clientes)
- Análisis de descuentos e impacto en rentabilidad

### 2. Feature Engineering
- Creación de variable objetivo: `Profitable` (1 = rentable, 0 = no rentable)
- Features temporales: Year, Month, Quarter, Day_of_Week, Shipping_Days
- Features derivadas: Price_per_Unit, High_Value_Order, Is_Weekend
- Encoding de categóricas: Segment, Category, Region, Ship Mode

### 3. Modelado de Machine Learning
- Algoritmo: **Random Forest Classifier**
- División: 80% train / 20% test
- Métricas: Accuracy, Precision, Recall, F1-Score
- Interpretabilidad: Feature Importance

---

## > Aprendizajes y Desarrollo

### Mi Rol
Este proyecto fue desarrollado como parte de mi portafolio de análisis de datos, con énfasis en:
- **Análisis Exploratorio de Datos (EDA)** - Desarrollado completamente por mí
- **Visualizaciones** - Diseño y generación propios
- **Insights de Negocio** - Interpretación y recomendaciones propias
- **Feature Engineering** - Selección y creación de variables

### Asistencia de IA
Para la sección de Machine Learning (Sección 6), utilicé asistencia de IA (Claude) como herramienta de:
- Aprendizaje de algoritmos de clasificación
- Comprensión de métricas de evaluación (Precision, Recall, F1-Score)
- Interpretación de Feature Importance

**El diseño del problema, selección de variables, interpretación de resultados y conexión con decisiones de negocio fueron desarrollados por mí.**

---

## > Estado del Proyecto

### COMPLETADO
- [x] Análisis exploratorio completo (EDA)
- [x] Visualizaciones profesionales (15+ gráficos)
- [x] Feature Engineering
- [x] Modelo predictivo (94% accuracy)
- [x] Insights y recomendaciones estratégicas
- [x] Documentación completa

---

## 👤 Autor

**Bryan Coronado**
- 📧 Email: bryancoronadog@gmail.com
- 💼 GitHub: [@BCrown7](https://github.com/BCrown7)
- 🔗 LinkedIn: https://www.linkedin.com/in/bryancoronado-dataanalyst/

---

## 📄 Licencia

Este proyecto es de código abierto para fines educativos y de portafolio.

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

[⬆ Volver arriba](#-análisis-de-ventas-retail---proyecto-de-portafolio)

</div>