def perevod2(a):
    b=str( ) # чтобы 1+1 равнялось не 2, а 11
    while a>0:
        b=str(a%2)+b
        a=a//2
    print('Ваше число в двоичной системе равняется ',b )

def perevod8(a):
    b=str( )
    while a>0:
        b=str(a%8)+b
        a=a//8
    print('Ваше число в восьмеричной системе равняется ',b )

x=int(input('Введите число, которое необходимо перевести'))
systema=int(input('В какую систему вы ходите перевести число? Введите "2" или "8"'))
if systema==2:
    perevod2(x)
if systema==8:
    perevod8(x)
if systema!=8 and systema!=2:
    print('программа переводит только в двоичную и восьмеричную систему')
