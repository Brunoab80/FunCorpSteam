#
#Leitura de arquivo .csv do Steam
#
f= open ("jogos.csv")

for line in f:
  print (line.strip().split(','))