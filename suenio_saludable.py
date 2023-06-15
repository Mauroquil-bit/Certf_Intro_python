"""
Sueño saludable
Problema del día
Siguiente problema en: 4h 14m 29s
Ann vio un programa de televisión sobre salud y aprendió que se recomienda dormir al menos A horas por día, 
pero dormir demasiado tampoco es saludable, y no debe dormir más de B horas. 
Ahora Ann duerme H horas por día. 
Si el horario de sueño de Ann cumple con los requisitos de ese programa de televisión, 
escriba "Normal". Si Ann duerme menos de A horas, salida "Deficiencia", y si duerme más de B horas, salida "Exceso".

La entrada a este programa es de tres cadenas con variables en el siguiente orden: 

Un
Un
, 
�
B
, 
�
H
. 
Un
Un
 es siempre menor o igual que 
�
B
.

Tenga en cuenta las mayúsculas y minúsculas: 
la salida debe corresponder exactamente a lo que se requiere en el problema, es decir, 
si el programa debe generar "Exceso", los resultados como "exceso", 
"EXCESO" o "ExCeSs" no se calificarán como correctos.

Debe pensar cuidadosamente en todas las condiciones que necesita usar. 
Se debe prestar especial atención a la rigurosidad de los operadores condicionales utilizados: 
recuerde la diferencia entre  
<
<
 y 
≤
≤
; 
>
>
 y 
≥
≥
. Para entender cuáles usar, lea atentamente la declaración del problema.

"""

# put your python code here
a = int(input())
b = int(input())
h = int(input())

if h < a:
    print("Deficiency")
elif h > b:
    print("Excess")
else:
    print("Normal")


