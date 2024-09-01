#
#Leitura de arquivo .csv do Steam
#
f= open ("jogos.csv")

gratuitos=0
pagos=0

for line in f:
  lista= line.strip().split(',')
  if lista [7] == '0.0':
    gratuitos += 1
  else:
    pagos+=1
  print (lista[7])
  
print ((gratuitos/(gratuitos+pagos))*100,'% de jogos gratuitos')
print (pagos/(pagos+gratuitos)*100,'% de jogos pagos') 