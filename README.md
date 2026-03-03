# 📊 Análisis de Ventas Retail (COMPLETO ✅)

Proyecto de práctica y portafolio para análisis de datos con objetivo de identificar patrones de ventas y desarrollar modelo predictivo.

## 🎯 Objetivos del Proyecto

- Analizar patrones de ventas por categoría, región y temporalidad
- Identificar segmentos de clientes más rentables
- Desarrollar modelo predictivo de ventas futuras
- Generar insights accionables para estrategias comerciales

### 🔗 Fuente Original:
- **Kaggle:** [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
Cargada manualmente en UTF-8 para compatibilidad.

## 🛠️ Tecnologías Utilizadas

- **Python (3.14.0)**
- **Pandas (3.0.0)** - Manipulación de datos
- **NumPy (2.4.1)** - Cálculos numéricos
- **Matplotlib (3.10.8) & Seaborn (0.13.2)** - Visualizaciones Avanzadas
- **Scikit-learn (1.8.0)** - Machine Learning
- **Jupyter Notebook (1.1.1)** - Análisis interactivo
- **Visual Studio Code** - Editor de código

## 📁 Estructura del Proyecto
```
analisis-ventas-retail/
│
├── data/
│   ├── raw/                   # Datos originales
│   └── processed/             # Datos procesados
├── notebooks/                 # Jupyter Notebooks
│   └── analisis_ventas_retail.ipynb
├── images/                    # Gráficos generados
├── src/                       # Scripts de Python
├── .gitignore
├── README.md
└── requirements.txt
```

### Clonación de repositorio
```bash
git clone https://github.com/BCrown7/analisis-ventas-retail.git
cd analisis-ventas-retail
```

### Creación de ambiente virtual
```bash
python -m venv venv    # Dentro de la carpeta del proyecto
venv\Scripts\activate  # Windows
```

### Instalación de dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar análisis
```bash
jupyter notebook
# Abre notebooks/analisis_principal.ipynb
```

## 📈 Resultados Principales

Este análisis exploró **9,994 pedidos** de ventas retail (2014-2017) para identificar patrones de rentabilidad y desarrollar estrategias de optimización.

**Situación Actual:**
- Ventas totales: **$2.3M**
- Ganancias: **$286K** (margen del 12.47%)
- **Problema crítico:** 19.4% de pedidos (1,936) generan pérdidas de $156K

**Hallazgo Más Importante:**
El descuento es el factor dominante de la rentabilidad. Los descuentos están destruyendo el 54.5% de las ganancias potenciales del negocio.

## 📝 Conclusiones

Este análisis reveló que el negocio tiene **una base sólida** (Technology y Office Supplies generan 93.6% de ganancias) pero está siendo **afectado por dos factores críticos:**

1. **Estratégia de descuentos agresiva** que convierte pedidos potencialmente rentables en pérdidas
2. **Categoría Furniture mayoritariamente no rentable** con márgenes insostenibles

**Oportunidad:** Implementar controles en descuentos y reestructurando Furniture (con posibles aumentos), el negocio puede aumentar sus ganancias entre 27-50% sin necesidad de incrementar ventas.

El modelo de Machine Learning desarrollado (94% accuracy) proporciona una herramienta práctica para **prevenir pérdidas antes de que ocurran**, transformando el análisis en acción automatizada.

## Notas adicionales

A pesar de estar completo, este proyecto continuará en constante mejora estructural y estética (código, estandarización, visualizaciones, y más).

Mi perfil profesional está orientado principalmente al análisis de datos y no al desarrollo especializado de modelos avanzados de Machine Learning, para esta sección decidí apoyarme en herramientas de IA como soporte técnico, método de aprendizaje y desarrollo.
*El diseño del problema, la selección de variables, la interpretación de resultados y la conexión con decisiones de negocio fueron desarrollados por mí.*

## 👤 Autor

**[Bryan Coronado]**
- GitHub: [@BCrown7](https://github.com/BCrown7)
- Email: bryancoronadog@gmail.com

## 📄 Licencia

Este proyecto es de código abierto para fines educativos y de portafolio.