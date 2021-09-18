import os
os.system ("cls")
"""
s = str(2 ** 100)
print(s)  # 1267650600228229401496703205376
print(len(s))  # 31
a = "Hellolakasdjfasdf"
print(a[1 : 4])
print(a[1 : -1])
print(a[1 : 100])
print(a[1:])
print(a[: -1])
print(a[:])
print(a[1:4:2])

s = '\nHello'
t = s  # s y t apuntan a la misma cadena
t = s[2:4]  # ahora t apunta a la nueva cadena &#39;ll&#39;
print(s)  # imprime &#39;Hola&#39; como s no se cambia
print(t)  # imprime &#39;ll&#39;

s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])

s = 'abracadabra'
print(s.find('b'))
# 1
print(s.rfind('b'))
# 8"""


s = "23456"

a = s.replace("2", "7")
print(a[0])