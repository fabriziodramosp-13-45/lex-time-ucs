"""
LexTime Perú: Asistente de Plazos Procesales
Desarrollado para: Universidad Científica del Sur
Descripción: Calcula fechas de vencimiento legal omitiendo fines de semana y feriados.
Librerías: pandas, datetime
"""

import pandas as pd
from datetime import datetime

def calcular_plazo_procesal():
    print("--- LexTime Peru: Asistente de Plazos Procesales ---")
    
    # 1. Base de datos de recursos y sus plazos (según el CPC peruano)
    recursos = {
        "1": {"nombre": "Tacha u Oposición", "dias": 5},
        "2": {"nombre": "Excepciones o Defensas Previas", "dias": 10},
        "3": {"nombre": "Contestación de demanda (Abreviado)", "dias": 10},
        "4": {"nombre": "Apelación de sentencia (Abreviado)", "dias": 5},
        "5": {"nombre": "Apelación de sentencia (Conocimiento)", "dias": 10},
        "6": {"nombre": "Recurso de Casación", "dias": 10}
    }

    # 2. Entrada de datos
    print("\nSeleccione el tipo de recurso:")
    for k, v in recursos.items():
        print(f"{k}. {v['nombre']} ({v['dias']} días útiles)")
    
    opcion = input("\nIngrese el número del recurso: ")
    
    if opcion not in recursos:
        print("Opción no válida.")
        return

    fecha_str = input("Ingrese la fecha de notificación (DD/MM/AAAA): ")
    
    try:
        # Convertir texto a objeto de fecha
        fecha_inicio = pd.to_datetime(fecha_str, dayfirst=True)
        
        # 3. Lógica de cálculo
        # Definimos los días de plazo
        dias_plazo = recursos[opcion]["dias"]
        
        # El conteo procesal empieza al día siguiente de la notificación
        # 'B' representa Business Days (Lunes a Viernes)
        fecha_vencimiento = fecha_inicio + pd.offsets.BusinessDay(n=dias_plazo)

        # 4. Resultado
        print("\n" + "="*40)
        print(f"RECURSO: {recursos[opcion]['nombre']}")
        print(f"FECHA NOTIFICACIÓN: {fecha_inicio.strftime('%d/%m/%Y')}")
        print(f"PLAZO: {dias_plazo} días hábiles")
        print(f"VENCIMIENTO: {fecha_vencimiento.strftime('%d/%m/%Y')}")
        print("="*40)
        print("Nota: El cálculo omite Sábados y Domingos. Verifique feriados locales.")

    except ValueError:
        print("Formato de fecha incorrecto. Use DD/MM/AAAA.")

if __name__ == "__main__":
    calcular_plazo_procesal()
    import pandas as pd
from datetime import datetime

def calcular_lextime_peru():
    print("="*50)
    print("   LEXTIME PERÚ: ASISTENTE DE PLAZOS PROCESALES")
    print("="*50)

    # 1. Base de datos de plazos (Código Procesal Civil)
    recursos = {
        "1": {"nombre": "Tacha u Oposición", "dias": 5},
        "2": {"nombre": "Excepciones o Defensas Previas", "dias": 10},
        "3": {"nombre": "Contestación de demanda (Abreviado)", "dias": 10},
        "4": {"nombre": "Apelación de sentencia (Abreviado)", "dias": 5},
        "5": {"nombre": "Apelación de sentencia (Conocimiento)", "dias": 10},
        "6": {"nombre": "Recurso de Casación", "dias": 10}
    }

    # 2. Configuración de Feriados Perú 2026 (Días no laborables judiciales)
    feriados_2026 = [
        '2026-01-01', '2026-04-02', '2026-04-03', '2026-05-01',
        '2026-06-29', '2026-07-28', '2026-07-29', '2026-08-06',
        '2026-08-30', '2026-10-08', '2026-11-01', '2026-12-08',
        '2026-12-09', '2026-12-25'
    ]
    
    # Creamos un calendario personalizado que ignore fines de semana y feriados
    calendario_judicial = pd.offsets.CustomBusinessDay(holidays=feriados_2026)

    # 3. Interacción con el usuario
    print("\nSeleccione el recurso procesal:")
    for k, v in recursos.items():
        print(f"{k}. {v['nombre']} ({v['dias']} días útiles)")
    
    opcion = input("\nNúmero de opción: ")
    if opcion not in recursos:
        print("Error: Opción no válida.")
        return

    fecha_input = input("Fecha de notificación (DD/MM/AAAA): ")

    try:
        # Convertir entrada a fecha
        fecha_notificacion = pd.to_datetime(fecha_input, dayfirst=True)
        
        # El plazo empieza a correr al día siguiente de la notificación
        dias_a_contar = recursos[opcion]["dias"]
        
        # CÁLCULO AUTOMÁTICO
        fecha_vencimiento = fecha_notificacion + (dias_a_contar * calendario_judicial)

        # 4. Entrega de resultados
        print("\n" + "—"*45)
        print(f"📌 RECURSO: {recursos[opcion]['nombre']}")
        print(f"📅 FECHA NOTIFICACIÓN: {fecha_notificacion.strftime('%d/%m/%Y')}")
        print(f"⏳ PLAZO LEGAL: {dias_a_contar} días hábiles")
        print(f"🚨 VENCIMIENTO FINAL: {fecha_vencimiento.strftime('%d/%m/%Y')}")
        print("—"*45)
        print("✅ El sistema ha omitido sábados, domingos y feriados nacionales.")

    except Exception as e:
        print(f"Error: Asegúrate de usar el formato DD/MM/AAAA. (Detalle: {e})")

if __name__ == "__main__":
    calcular_lextime_peru()
