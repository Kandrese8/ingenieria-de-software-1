# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:10:34 2025

@author: Kevin Andres Estrada Isaza
        Kelly Saenz Ballesteroz
        
        ...Para Politecnico Grancolombiano
"""

# -*- coding: utf-8 -*-
"""
Prototipo de registro de solicitudes de recolección
Created on Mon Apr 28, 2025

@author: Kandres Estrada
"""

# Diccionario para almacenar las solicitudes
solicitudes = {}

# Función para registrar una nueva solicitud
def registrar_solicitud():
    print("\n=== Registro de Solicitud ===")
    tipo_residuo = input("Ingrese el tipo de residuo: ")
    frecuencia = input("Ingrese la frecuencia de recolección (1 o 2 veces por semana): ")
    modalidad = input("Ingrese la modalidad (programada o por demanda): ")
    
    # Generar un ID único para la solicitud
    solicitud_id = len(solicitudes) + 1
    solicitudes[solicitud_id] = {
        "tipo_residuo": tipo_residuo,
        "frecuencia": frecuencia,
        "modalidad": modalidad
    }
    print(f"\n¡Solicitud registrada con éxito! ID: {solicitud_id}")

# Función para listar todas las solicitudes
def listar_solicitudes():
    print("\n=== Listado de Solicitudes ===")
    if not solicitudes:
        print("No hay solicitudes registradas.")
    else:
        for solicitud_id, datos in solicitudes.items():
            print(f"ID: {solicitud_id} | Tipo de Residuo: {datos['tipo_residuo']} | "
                  f"Frecuencia: {datos['frecuencia']} | Modalidad: {datos['modalidad']}")

# Menú principal
def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar una nueva solicitud")
        print("2. Listar todas las solicitudes")
        print("3. Consultar una solicitud específica (por ID o fecha) [En desarrollo]")
        print("4. Modificar una solicitud registrada [En desarrollo]")
        print("5. Eliminar una solicitud [En desarrollo]")
        print("6. Generar reportes:")
        print("   - Reporte por tipo de residuo [En desarrollo]")
        print("   - Reporte por frecuencia de recolección [En desarrollo]")
        print("7. Visualizar acumulación de puntos (si aplica) [En desarrollo]")
        print("8. Configurar parámetros del sistema:")
        print("   - Modificar fórmulas de puntos [En desarrollo]")
        print("   - Configuración de notificaciones [En desarrollo]")
        print("9. Gestión de usuarios:")
        print("   - Registrar nuevos usuarios [En desarrollo]")
        print("   - Administrar roles de usuario (administrador, recolector, etc.) [En desarrollo]")
        print("10. Salir del sistema")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_solicitud()
        elif opcion == "2":
            listar_solicitudes()
        elif opcion == "10":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida o función en desarrollo. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()