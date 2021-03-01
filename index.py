# satriadinata ratnanto 71200626
# Ada sebuah permasalahan untuk mempercepat mencari median dan mean sebuah data
# def median(data):

def median(data):
    if len(data)%2==0:
        mid=len(data)/2
        return (data[int(mid-1)]+data[int(mid)])/2
    else:
        return data[int(len(data)/2-0.5)]
def mean(data):
    return sum(data)/len(data)

x=input('Masukkan urutan data : ')
data=x.split(',')
for i in range(len(data)):
    data[i]=int(data[i])
data.sort()

loop=True
while loop==True:
    print('\nMenu :\n1. Median\n2. Mean\n3. Exit')
    pil=int(input('Pilih menu dengan mengetikan angka : '))
    if pil==1:
        print('Data terurut : ',data)
        print('Median :', median(data))
    elif pil==2:
        print('Data terurut : ',data)
        print('Mean :', mean(data))
    elif pil==3:
        print("dadadaaa..")
        loop=False
    else:
        print('Menu tidak ditemukan')