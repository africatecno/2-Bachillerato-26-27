python
# --- PRÁCTICA 1: CONVERSOR DIGITAL ---
print("====================================")
print("  BIENVENIDO AL CONVERSOR DIGITAL   ")
print("====================================")

euros = float(input("Introduce una cantidad en Euros (€): "))
gigabytes = float(input("Introduce una cantidad de datos en Gigabytes (GB): "))

tasa_dolar = 1.09      
megabytes_por_gb = 1024  

dolares = euros * tasa_dolar
megabytes = gigabytes * megabytes_por_gb

print("\n====================================")
print("       RESULTADOS DEL CÁLCULO       ")
print("====================================")
print(f"💰 Finanzas: {euros} € equivalen a {dolares:.2f} $ Dólares.")
print(f"💾 Almacenamiento: {gigabytes} GB equivalen a {megabytes:.0f} MB.")
print("====================================")
