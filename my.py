print("1. konversi celcius ke fahrenheit")
print("2. konversi fahrenheit ke reamur")
print("3. konversi reamur ke kelvin")


pilihan = int(input("anda ingin mengerjakan seperti nomor berapa? "))

if pilihan == 1:
    celcius = float(input("masukkan celcius yang akan di konvert: "))
    fahrenheit = (9 / 5) * celcius + 32
    print("nilai fahrenheitnya adalah : ", + fahrenheit)

elif pilihan == 2:
    fahrenheit = float(input("masukkan fahrenheit yang akan di konvert: "))
    reamur = 4/9 * (fahrenheit - 32)
    print("nilai reamurnya adalah : ", + reamur)
    
else:
    reamur = float(input("masukkan reamur yang akan di konvert: "))
    kelvin = (5 / 4) * reamur + 273.15
    print("nilai kelvinnya adalah : ", + kelvin)

print("terimakasih...semoga membantu!!")