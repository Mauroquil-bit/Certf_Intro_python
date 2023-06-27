"""
Condiciones y listas anidadas
Imagina que tienes una lista de estudiantes y sus calificaciones para un examen:

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
Seleccione solo los estudiantes con la mejor calificación ("A") e imprima sus nombres en una lista. 
Haz todo esto en una línea. Ya hemos creado la variable con otros nombres y calificaciones.students

[PISTA] Puede crear e imprimir una lista en una línea si comienza directamente con . 
[/SUGERENCIA]print([#your condition here])


"""

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
print([s[0] for s in students if s[1] == 'A'])

# ###################################################################

