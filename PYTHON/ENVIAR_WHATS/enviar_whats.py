import pyautogui as pg, time as tm, webbrowser as web

mensaje = [input('Ingrese el mensaje a enviar mensaje\n'), int(input('Cantidad de veces que desea enviar el mensaje\n'))]
print(mensaje)

numero_whatsapp = input('Ingrese el número de la persona a quien desea enviarle el mensaje con su respectivo codigo, ej: +57XXXXXX\n')


web.open(f'https://web.whatsapp.com/send?phone={numero_whatsapp}')
tm.sleep(8)
for x in range(mensaje[1]):
    
        
    pg.write(mensaje[0])
    pg.press('enter')