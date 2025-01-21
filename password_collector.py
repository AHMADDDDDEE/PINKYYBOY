import os

# Membersihkan layar
os.system('cls' if os.name == 'nt' else 'clear')

# Warna untuk output
m = '\033[1;32m'
c = '\033[3;31m'
b = "\033[0;34m"
g = "\033[1;32m"
w = "\033[1;37m"
r = "\033[1;31m"
y = "\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

# Menampilkan informasi
print(b)
print(w)
print('########################################')
print(r)
print('    Author  : Mr.B3604')
print(cyan)
print('    Tool    : Hack Instagram v.1')
print(lgray)
print('    YouTube : GUNAWAN ID')
print(w)
print('########################################')
print('\r')

# Meminta nama file untuk menyimpan password
aaa = input('Masukkan nama file untuk menyimpan password (default: pass.txt): ') or 'pass.txt'
os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan informasi lagi
print(w)
print('########################################')
print(r)
print('    Author  : Mr.B3604')
print(cyan)
print('    Tool    : Hack Instagram v.1')
print(lgray)
print('    YouTube : GUNAWAN ID')
print(w)
print('########################################')

# Membuka file untuk menulis password
file = open(aaa, 'w')
aa = set([])
oio = set([])
kk = 1

while True:
    b = input('\033[1;33mpassword {} : '.format(kk))
    
    if b == 'save':
        print('\033[3;33m')
        file.close()
        qq = open(aaa, 'r')
        ll = len(qq.readlines())
        os.system('printf "\033[3;33m"')
        print('÷' * 40)
        print(' {} password di simpan ---> {} '.format(ll, aaa))
        print('÷' * 40)
        break
    
    if b == '':
        print("Password tidak boleh kosong!")
        continue
    
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio:
            oio.add(i)
            file.write(i + '\n')
    
    kk += 1
    print('-' * 40)
            file.write('\n')
            #for o in iio:
             #   uau='{}{}'.format(i,o)
              #  ubu='{}{}{}'.format(o,i,o)
               # ucu='{}{}{} '.format(i,o,i)
                #if len(uau)>= 6:
                   # file.write(uau)
                  #  file.write('\n')
               # if len(ubu) >= 6 and ubu != uau :
                   # file.write(ubu)
                   # file.write('\n')
                #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                  #  file.write(ucu)
                  #  file.write('\n')

        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write('\n')
        if c != d and len(d) >= 6:
            file.write(d)
            file.write('\n')
    kk=int(kk)+1
    print('-'*40)
