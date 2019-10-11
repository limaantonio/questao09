import matplotlib.pyplot as plt
import random
import timeit
from math import log10

def bubbleSort(lista):
    i = j = e = 0
    for e in range(len(lista)-1):
        for j in range(len(lista)-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def insertionSort(lista):
    t = len(lista)
    for e in range(t):
        x = lista[e]
        j=e-1
    while j>=0 and lista[j]>x:
        lista[j+1]=lista[j]
        j-=1
    lista[j+1]=x

def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        E = lista[:meio]#divide o vetor em 2, E= lado esquerdo
        D = lista[meio:]#atribui o lado direito do vetor para D

        mergeSort(E)
        mergeSort(D)

        i = j = k = 0

        while i < len(E) and j < len(D):
            if E[i] < D[j]:
                lista[k] = E[i]
                i+=1
            else:
                lista[k] = D[j]
                j+=1
            k+=1

            while i < len(E):
                lista[k] = E[i]
                i+=1
                k+=1

            while j < len (D):
                lista[k] = D[j]
                j+=1
                k+=1

def countingSort(list):
    
    k = max(list)
    B = [0 for w in range(len(list))]
    C = [0 for w in range(k+1)]
   
    for j in range(0,len(list)):
        C[list[j]] = C[list[j]] + 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for j in range(len(list)-1,0,-1):
        B[C[list[j]]-1] = list[j]
        C[list[j]] = C[list[j]] - 1
    return B
    
def selectionSort(lista):
    min = aux = i = 0
    n = len(lista)
    j = i + 1

    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if lista[j] > lista[min]:
                min = j
            aux = lista[j]
            lista[j] = lista[min]
            lista[min] = aux

def quickSort(lista):
    def particao(lista,inicio,final): 
        i = ( inicio-1 )		
        pivo = lista[final]	

        for j in range(inicio , final): 
            if lista[j] <= pivo: 			
                i = i+1
                lista[i],lista[j] = lista[j],lista[i] 

        lista[i+1],lista[final] = lista[final],lista[i+1] 
        return ( i+1 ) 

    def quick(lista,inicio,final): 
        if inicio < final: 
            pi = particao(lista,inicio,final) 
            quick(lista, inicio, pi-1) 
            quick(lista, pi+1, final) 

def geraLista(tam):
    random.seed()
    i = 0
    lista = []
    while i < tam:
        lista.append(random.randint(1, tam))
        i+=1
    return lista

def shellSort(lista):
    h = 1
    t = len(lista)

    while h > 0:
        for i in range(h, t):
            c = lista[i]
            j = i
            while j >= h and c < lista[j - h]:
                lista[j] = lista[j-h]
                j = j - h
                lista[j] = c
        h = int(h/2.2)
    return lista

def bucketSort(lista): 
	arr = [] 
	slot_num = 10
	for i in range(slot_num): 
		arr.append([]) 
		
 
	for j in lista: 
		index_b = int(slot_num * j) 
		arr[index_b].append(j) 
	
	for i in range(slot_num): 
		arr[i] = insertSort(arr[i]) 
		
	k = 0
	for i in range(slot_num): 
		for j in range(len(arr[i])): 
			lista[k] = arr[i][j] 
			k += 1
	return lista

def insertSort(b): 
	for i in range(1, len(b)): 
		up = b[i] 
		j = i - 1
		while j >=0 and b[j] > up: 
			b[j + 1] = b[j] 
			j -= 1
		b[j + 1] = up	 
	return b	 
	


def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixSort(lista):
  base=10  
  passes = int(log10(max(lista))+1)
  output = [0] * len(lista)

  for pos in range(passes):
    count = [0] * base

    for i in lista:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(lista):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    lista = list(output)
  return output

#main
tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

temposBurbbleSort = []
temposInsertionSort = []
temposSelectionSort = []
temposQuickSort = []
temposMergeSort = []
temposCountingSort = []
temposShellSort = []
temposBucketSort = []
temposRadixSort = []

for tamanho in tamanhos:
    lista = geraLista(tamanho)
    lista_teste = list(lista)
    temposBurbbleSort.append(timeit.timeit("bubbleSort({})".format(lista_teste),setup="from __main__ import bubbleSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposInsertionSort.append(timeit.timeit("insertionSort({})".format(lista_teste),setup="from __main__ import insertionSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposSelectionSort.append(timeit.timeit("selectionSort({})".format(lista_teste),setup="from __main__ import selectionSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposMergeSort.append(timeit.timeit("mergeSort({})".format(lista_teste),setup="from __main__ import mergeSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposCountingSort.append(timeit.timeit("countingSort({})".format(lista_teste),setup="from __main__ import countingSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")
    
    lista_teste = list(lista)
    temposQuickSort.append(timeit.timeit("quickSort({})".format(lista_teste),setup="from __main__ import quickSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposShellSort.append(timeit.timeit("shellSort({})".format(lista_teste),setup="from __main__ import shellSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = [0.122, 0.013, 0.450, 0.454, 0.456, 0.123, 0.122, 0.013, 0.450, 0.454, 0.456, 0.122]
    temposBucketSort.append(timeit.timeit("bucketSort({})".format(lista_teste),setup="from __main__ import bucketSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")

    lista_teste = list(lista)
    temposRadixSort.append(timeit.timeit("radixSort({})".format(lista_teste),setup="from __main__ import radixSort", number=1))
    print("Lista de tamanho {}".format(tamanho),"ordenada")


fig, ax = plt.subplots()
ax.semilogx(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.semilogx(tamanhos, temposInsertionSort, label="Insertion Sort")
ax.semilogx(tamanhos, temposSelectionSort, label="Selection Sort")
ax.semilogx(tamanhos, temposMergeSort, label="Merge Sort")
ax.semilogx(tamanhos, temposCountingSort, label="Counting Sort")
ax.semilogx(tamanhos, temposQuickSort, label="Quick Sort")
ax.semilogx(tamanhos, temposShellSort, label="Shell Sort")
ax.semilogx(tamanhos, temposBucketSort, label="Bucket Sort")
ax.semilogx(tamanhos, temposRadixSort, label="Radix Sort")
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")


legend = ax.legend(loc='upper center', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.show()

