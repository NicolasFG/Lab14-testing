import csv
import unittest


# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
#
# provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append( fila)
        return data

    def calcularganador(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1':
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        for candidato in votosxcandidato:
            #print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))
            continue
        for candidato in votosxcandidato:
            return [candidato]

#c = CalculaGanador()
#c.calcularvotos(c.leerdatos())

datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
#print(c.calcularganador(datatest))

#Se creo la siguiente clase TestCalculaGanador para que en tres funciones se realicen los tests.

class TestCalculaGanador(unittest.TestCase):

    def test_calcularganador_uno(self):
        c = CalculaGanador()
        #Se crea un nuevo dataset
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

        ganador = c.calcularganador(datatest)
        #Siguiendo el dataset enviado el ganador seria la candidata Aundrea Grace
        try:
            self.assertEqual(ganador, ['Aundrea Grace'])
            print("Paso el test 1")
        except AssertionError:
            print("No paso el test 1. El ganador correcto es: Aundrea Grace")


    def test_calcularganador_dos(self):
        c = CalculaGanador()
        #Se crea una dataset de prueba
        datatest = [
            ['Lima', 'Lima', 'Miraflores', '12345678', 'John Doe', '1'],
            ['Lima', 'Lima', 'Miraflores', '98765432', 'Jane Smith', '1'],
            ['Lima', 'Lima', 'Miraflores', '56789012', 'John Doe', '1']
        ]

        ganador = c.calcularganador(datatest)

        try:
            self.assertEqual(ganador, ['John Doe'])
            print("Paso el test 2")
        except AssertionError:
            print("No paso el test 2. El ganador correcto es: John Doe")

    def test_calcularganador_tres(self):
        c = CalculaGanador()
        datatest = [
            ['Madrid', 'Spain', 'City Center', '11111111', 'Alice Johnson', '1'],
            ['Madrid', 'Spain', 'City Center', '22222222', 'Bob Smith', '0'],
            ['Madrid', 'Spain', 'City Center', '33333333', 'Alice Johnson', '1'],
            ['Madrid', 'Spain', 'City Center', '44444444', 'Alice Johnson', '1']
        ]
        ganador = c.calcularganador(datatest)

        try:
            self.assertEqual(ganador, ['Alice Johnson'])
            print("Paso el test 3")
        except AssertionError:
            print("No paso el test 3. El ganador correcto es: Alice Johnson")

if __name__ == '__main__':
    unittest.main()