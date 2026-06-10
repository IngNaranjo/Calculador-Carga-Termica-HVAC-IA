# Calculador Inteligente de Carga Térmica (HVAC) con IA

Este proyecto consiste en un sistema experto desarrollado en **Python** para el cálculo preciso de la demanda térmica en espacios residenciales y comerciales, adaptado a factores de transferencia de calor comunes en México. Cuenta con una interfaz interactiva por consola, generación de gráficos dinámicos y un módulo de diagnóstico automatizado mediante la API de **Gemini**.

## 🚀 Características del Software
* **Motor de Cálculo Estructurado:** Evalúa el aporte de calor por orientación de paredes (sol/sombra), losas/techos, ventanas expuestas, ocupantes y cargas eléctricas internas (Watts).
* **Gráfica Dinámica Automática:** Genera histogramas visuales utilizando `matplotlib`, filtrando automáticamente los componentes con valor cero para un análisis visual limpio y profesional.
* **Diagnóstico con IA:** Se conecta de forma segura con el modelo `gemini-2.5-flash` para redactar una hoja de especificación técnica, recomendando la capacidad comercial del equipo, justificando la instalación a 220V e incluyendo ingeniería de eficiencia.
* **Seguridad de Credenciales:** Implementación profesional mediante variables de entorno del sistema (`os.environ`) para proteger la API Key de Google.

## 🛠️ Tecnologías Utilizadas
* Python 3.x
* Matplotlib (Visualización y gráficas de datos)
* Google GenAI SDK (Módulo de Inteligencia Artificial)

## 📝 Operación del Programa
1. El usuario ingresa los datos de áreas, longitudes y cargas térmicas internas en la consola.
2. El software procesa las ecuaciones de transferencia y arroja la Demanda Térmica Total en BTU/h y Toneladas de Refrigeración.
3. Se despliega la gráfica de barras con el desglose del calor acumulado.
4. Gemini genera y muestra el reporte experto de especificación e instalación eléctrica.
