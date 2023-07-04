"""
Situación de modelado

Su programa tendrá acceso a la función, 
que puede lanzar excepciones.exception_test()

Debe escribir código que ejecute esta función, luego capture , , 
excepciones e imprima el nombre de la excepción capturada. 
Tenga en cuenta la jerarquía de excepciones.ArithmeticErrorAssertionErrorZeroDivisionError

Una solución de ejemplo que debe enviar para su revisión:

try:
    exception_test()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")


Propina: No te olvides de la jerarquía de excepciones. 
La clave de esta tarea es elegir el orden correcto de las cláusulas exceptu.

"""

try:
    exception_test()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")

# ###################################################################

