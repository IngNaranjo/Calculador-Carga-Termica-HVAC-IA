# =============================================================================
# PROYECTO: Calculador de Carga Térmica (BTU) y Selección de Equipos de Aire Acondicionado
# VERSION: Definitiva (Seguridad por CMD, Gráfica Dinámica e IA)
# ENTORNO: Spyder (Python)
# =============================================================================

import os
import matplotlib.pyplot as plt
from google import genai

print("="*60)
print("  CALCULADOR DE CARGA TÉRMICA (BTU) Y SELECCIÓN DE EQUIPOS")
print("="*60)

# 1. VERIFICACIÓN DE SEGURIDAD (Lee la clave que guardaste en el CMD)
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Error: No se encontró la variable de entorno GEMINI_API_KEY. Si ya la pusiste en el CMD, recuerda cerrar y volver a abrir Spyder para que la detecte.")

# Inicializar cliente oficial de Gemini
client = genai.Client(api_key=api_key)

# 2. INGRESO DE DATOS INTERACTIVOS (Basados en Planilla de Ingeniería)
print("\n--- 1. VENTANAS Y PAREDES ---")
m2_ventana = float(input("Metros cuadrados de ventanas expuestas al Noroeste (m²): "))
m_pared_sol = float(input("Metros lineales de pared pesada expuesta al sol (m): "))
m_pared_sombra = float(input("Metros lineales de pared en la sombra (m): "))

print("\n--- 2. ESTRUCTURA (TECHO Y PISO) ---")
m2_techo = float(input("Metros cuadrados de loza entre pisos o techo (m²): "))

print("\n--- 3. CARGAS INTERNAS (PERSONAS Y EQUIPOS) ---")
personas = int(input("Número de personas que ocupan el lugar: "))
watts_equipos = float(input("Potencia total de aparatos eléctricos en uso (en Watts): "))

# 3. CÁLCULOS MATEMÁTICOS DE INGENIERÍA TÉRMICA (Planilla México)
btu_ventanas = m2_ventana * 650
btu_paredes = (m_pared_sol * 160) + (m_pared_sombra * 100)
btu_techo = m2_techo * 32
btu_personas = personas * 500
btu_equipos = watts_equipos * 3.4

btu_totales = btu_ventanas + btu_paredes + btu_techo + btu_personas + btu_equipos
toneladas = btu_totales / 12000

# 4. IMPRESIÓN DE RESULTADOS EN CONSOLA
print("\n" + "="*40)
print("         HOJA DE RESULTADOS ACUMULADOS")
print("="*40)
print(f"-> Calor por Ventanas:   {btu_ventanas:,.0f} BTU/h")
print(f"-> Calor por Paredes:    {btu_paredes:,.0f} BTU/h")
print(f"-> Calor por Techo:      {btu_techo:,.0f} BTU/h")
print(f"-> Calor por Personas:   {btu_personas:,.0f} BTU/h")
print(f"-> Calor por Equipos:    {btu_equipos:,.0f} BTU/h")
print("-"*40)
print(f"DEMANDA TÉRMICA TOTAL:  {btu_totales:,.0f} BTU/h")
print(f"CAPACIDAD TEÓRICA:      {toneladas:.2f} Toneladas")
print("="*40)

# 5. FILTRADO DINÁMICO PARA LA GRÁFICA
componentes_todos = ['Ventanas', 'Paredes', 'Techo', 'Personas', 'Equipos Eléc.']
valores_todos = [btu_ventanas, btu_paredes, btu_techo, btu_personas, btu_equipos]
colores_todos = ['#e74c3c', '#e67e22', '#95a5a6', '#2ecc71', '#f1c40f']

componentes_graficar = []
valores_graficar = []
colores_graficar = []

for i in range(len(valores_todos)):
    if valores_todos[i] > 0:
        componentes_graficar.append(componentes_todos[i])
        valores_graficar.append(valores_todos[i])
        colores_graficar.append(colores_todos[i])

plt.figure(figsize=(9, 5))
barras = plt.bar(componentes_graficar, valores_graficar, color=colores_graficar, edgecolor='black')

for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval + 100, f'{yval:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.title(f'Análisis de Carga Térmica por Componente\nTotal Requerido: {btu_totales:,.0f} BTU/h', fontsize=12, fontweight='bold')
plt.ylabel('Aporte de Calor (BTU/h)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 6. CONSULTA EXPERTA A LA API DE GEMINI
prompt = f"""
Actúa como un Ingeniero Mecánico Eléctrico especialista en sistemas HVAC y eficiencia energética en México.
Hemos calculated la carga térmica real de un espacio basándonos en una planilla técnica estructurada, obteniendo los siguientes resultados:

- Demanda Térmica Total Calculada por el Software: {btu_totales:,.2f} BTU/h
- Capacidad Teórica Requerida: {toneladas:.2f} Toneladas de refrigeración.
- Carga por equipos eléctricos internos: {btu_equipos:,.2f} BTU/h (Derivada de {watts_equipos} Watts comerciales en uso).
- Aporte por ocupantes: {btu_personas:,.2f} BTU/h ({personas} personas).

Por favor, genera un reporte técnico de especificación directo y realista:
1. SELECCIÓN COMERCIAL: Indica la capacidad nominal en BTU/h o Toneladas del equipo comercial estándar más adecuado para este espacio (ej. 24,000 BTU/h o similar) justificando si cubre la demanda de forma segura.
2. ANÁLISIS ELÉCTRICO CRÍTICO: Explica por qué para la capacidad requerida ({toneladas:.2f} Toneladas) es técnicamente obligatorio realizar una instalación a 220 V en lugar de 110 V, detallando el impacto en el amperaje (corriente) y calibre de los conductores.
3. INGENIERÍA DE EFICIENCIA: Al notar que la mayor carga térmica proviene de los aparatos eléctricos instalados ({watts_equipos} W), ofrece un consejo práctico de diseño o uso para mitigar este impacto sin sobredimensionar el consumo eléctrico general.
"""

try:
    print("\n[INFO] Gráfica generada con éxito.")
    print("[INFO] Conectando con Gemini para generar el reporte de ingeniería...")
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    print("\n" + "="*60)
    print("HOJA DE ESPECIFICACIÓN TÉCNICA Y ELÉCTRICA (ANÁLISIS IA)")
    print("="*60)
    print(response.text)
except Exception as e:
    print(f"\nError al conectar con la API de IA: {e}")