#
#Leitura de arquivo .csv do Steam
#
f = open("jogos2.csv")

gratuitos = 0
pagos = 0
jogos_por_ano = {}
maior_ano = 0

for line in f:
  lista = line.strip().split(',')
  #-------Determinar a quantidade de jogos pagos e gratuitos------
  if lista[7] == '0.0':
    gratuitos += 1
  else:
    pagos += 1
#______Ler lista de lançamentos de jogos novos e somar por ano____
  ano = lista[3]
  if ano in jogos_por_ano:
    jogos_por_ano[ano] += 1
  else:
    jogos_por_ano[ano] = 1
#------Determinar o jogo com a Idade mínima mais alta------
  if lista[6] > '0':
    ida_min= lista [6]
    nome= lista[1]
    
#-----imprimir a porventagem de jogos gratuitos e pagos------
print(gratuitos / (gratuitos + pagos) * 100, '% de jogos gratuitos')
print(pagos / (pagos + gratuitos) * 100, '% de jogos pagos')
print("A idade mínima mais alta entre os jogos: ",ida_min, nome)

#----Determinar o ano com mais jogos novos-------------------
for ano, quantidade in jogos_por_ano.items():
  maior_ano = max(jogos_por_ano.values())
  print(f"Ano {ano}: {quantidade} jogos novos")
  if maior_ano == jogos_por_ano[ano]:
    print(f"O ano com mais jogos novos é {ano}")
