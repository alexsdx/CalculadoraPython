# Calculadora
Este repositorio tiene código que cuando se ejecuta se muestra una calculadora básica en Python. La calculadora tiene una interfaz gráfica utilizando **_tkinter_**, que es ideal para crear interfaces sencillas en Python. La calculadora permite al usuario ingresar números y seleccionar una operación a través de botones, mostrando el resultado en la pantalla.

## Características
Algunas de las características de la calculadora son las siguientes:

* **Interfaz de calculadora tradicional:** Botones para dígitos (0-9), punto decimal, operaciones (+, -, *, /), y un botón "C" para limpiar.
* **Lógica mejorada:** Los números se construyen concatenando dígitos en un campo de entrada, y las operaciones se evalúan al presionar el botón correspondiente.
* **Estilo visual:** Uso de colores (fondo gris claro, botones azules para números, naranjas para operaciones, y rojo para limpiar), fuente más clara, y bordes para una apariencia moderna.
* **Diseño en cuadrícula:** Los botones están organizados en una cuadrícula similar a una calculadora física (4 columnas: 3 para números, 1 para operaciones).
* **Manejo de errores:** Validación para entradas no válidas y división por cero, con mensajes emergentes.

## Cómo usar la calculadora actualizada
1. **Ejecutar el código:** Asegúrate de tener Python con **_Tkinter_** instalado.

2. **Interfaz:**
   * Un campo de entrada en la parte superior muestra los números y resultados.
   * Botones numéricos (0-9) y punto decimal (.) para construir números.
   * Botones de operaciones (+, -, *, /) para seleccionar la operación.
   * Botón "=" para calcular el resultado.
   * Botón "C" para limpiar la entrada y reiniciar.

3. **Funcionamiento:**
   * Ingresa el primer número usando los botones numéricos.
   * Selecciona una operación (+, -, *, /).
   * Ingresa el segundo número.
   * Presiona "=" para ver el resultado.
   * El resultado se puede usar como el primer número para una nueva operación.
   * Usa "C" para reiniciar todo.

4. **Errores:** Mensajes emergentes aparecen para entradas no válidas, división por cero, o si intentas calcular sin seleccionar una operación.

## Qué aprendes
* Modificación de interfaces gráficas con **_tkinter_** para añadir nuevos elementos.
* Ajuste de la lógica de una aplicación para manejar cálculos explícitos con un botón "=".
* Reorganización de layouts en cuadrícula (**_grid_**) para mantener un diseño funcional.
* Manejo de estados en una calculadora (número, operador, resultado).

## Posibles mejoras adicionales

* **Soporte para teclado:** Permitir entrada de números y operaciones desde el teclado.
* **Historial de operaciones:** Mostrar cálculos anteriores en una etiqueta.
* **Más operaciones:** Agregar botones para potencia, raíz cuadrada, etc.
* **Ajustes de estilo:** Cambiar colores o añadir efectos al pasar el mouse sobre los botones.
