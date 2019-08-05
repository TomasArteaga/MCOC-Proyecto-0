INTRODUCCION
=====

Se va a mostrar un ejemplo particular con la funcion tangente con respecto a la perdida de significancia.

EJEMPLO
========

Se entregan 3 numeros pequeños 
1) 12*10e-10
2) 25*10e-10
3) 57*10e-10

Por lo que se va aplicar la funcion tangente a cada uno de los numeros para observar la perdida de significancia con la comparacion del float 32 y el float 64 con la funcion tangente de los numeros originales.


RESULTADO
======
Imagen mostrada inicialmente

Output de la consola:

```
[1.2e-09, 2.5e-09, 5.7000000000000006e-09]  numeros iniciales 
[-0.63585992866158081, -0.13352640702153587, 0.48469922679209587] datos transformado por la funcion tangente
[9.7782143796892125e-09, 6.0774709918447105e-09, -4.8299832039075033e-09] error32
[0.0, 0.0, 0.0] error64
```



