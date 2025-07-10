class Matriz:
    def __init__(self):
        self.filas = int(input("Número de filas: "))
        self.columnas = int(input("Número de columnas: "))
        print("Ingresa los valores de cada fila separados por espacios o comas:")
        self.datos = []
        for i in range(self.filas):
            entrada = input(f"Fila {i+1}: ").replace(',', ' ').split()
            if len(entrada) != self.columnas:
                raise ValueError("Número de elementos no coincide con las columnas.")
            self.datos.append(entrada)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, fila)) for fila in self.datos])

    def _verificar_dimensiones(self, otra):
        return self.filas == otra.filas and self.columnas == otra.columnas

    def sumar(self, otra):
        if not self._verificar_dimensiones(otra):
            print("❌ No se pueden sumar matrices con diferentes dimensiones.")
            return
        print("\n✅ Suma de matrices:")
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                try:
                    fila.append(float(self.datos[i][j]) + float(otra.datos[i][j]))
                except:
                    fila.append(str(self.datos[i][j]) + str(otra.datos[i][j]))
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def restar(self, otra):
        if not self._verificar_dimensiones(otra):
            print("❌ No se pueden restar matrices con diferentes dimensiones.")
            return
        print("\n✅ Resta de matrices:")
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                try:
                    fila.append(float(self.datos[i][j]) - float(otra.datos[i][j]))
                except:
                    fila.append("ERROR")
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def multiplicar(self, otra):
        if self.columnas != otra.filas:
            print("❌ No se pueden multiplicar: columnas de A ≠ filas de B.")
            return
        print("\n✅ Producto de matrices:")
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(otra.columnas):
                suma = 0
                for k in range(self.columnas):
                    try:
                        suma += float(self.datos[i][k]) * float(otra.datos[k][j])
                    except:
                        suma = "ERROR"
                        break
                fila.append(suma)
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def dividir(self, otra):
        if not self._verificar_dimensiones(otra):
            print("❌ No se pueden dividir matrices con diferentes dimensiones.")
            return
        print("\n✅ División elemento a elemento:")
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                try:
                    num = float(self.datos[i][j])
                    den = float(otra.datos[i][j])
                    fila.append(num / den if den != 0 else "∞")
                except:
                    fila.append("ERROR")
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def escalar(self, esc):
        print(f"\n✅ Multiplicación por escalar ({esc}):")
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                try:
                    fila.append(float(self.datos[i][j]) * esc)
                except:
                    fila.append(str(self.datos[i][j]) * int(esc))
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def transpuesta(self):
        print("\n✅ Transpuesta:")
        resultado = []
        for j in range(self.columnas):
            fila = []
            for i in range(self.filas):
                fila.append(self.datos[i][j])
            resultado.append(fila)
        self._imprimir_resultado(resultado)

    def _imprimir_resultado(self, resultado):
        for fila in resultado:
            print('\t'.join(map(str, fila)))


# ====== USO DE LA CLASE ======

print("📥 Matriz A:")
A = Matriz()
print("\n📥 Matriz B:")
B = Matriz()

print("\n🧾 Matriz A:")
print(A)
print("\n🧾 Matriz B:")
print(B)

# Operaciones
A.sumar(B)
A.restar(B)
A.multiplicar(B)
A.dividir(B)
A.escalar(3)
A.transpuesta()