#5- Un agricultor que se dedica al cultivo ecológico de naranjas y limones, quiere calcular los beneficios que obtiene
#anualmente por la venta de los mismos. Por este motivo vamos a diseñar una aplicación que solicite las ventas (en kilos)
#de cada semestre para cada fruta. La aplicación mostrará el importe total sabiendo que el precio del kilo de naranjas está
#fijado en 1.25€ y el kilo de limones en 1.90€.

print("introduzca la venta de naranjas del primer semestre")
venta_naranja_1=int(input())
print("introduzca la venta de naranjas del segundo semestre")
venta_naranja_2=int(input())

print("introduzca la venta de limones del primer semestre")
venta_limones_1=int(input())
print("introduzca la venta de limones del segundo semestre")
venta_limones_2=int(input())

beneficios_totales= 1.9*(venta_limones_1+venta_limones_2) + 1.25*(venta_naranja_1+venta_naranja_2)

print(f"los beneficios totales de ambas ventas fueros: {beneficios_totales} €")