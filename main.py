#
#Leitura de arquivo .csv do Steam
#
f= open ("jogos.csv")

gratuitos=0
pagos=0
jogos_por_ano= {  }

for line in f:
  lista= line.strip().split(',')
#-------Determinar a Porcentagem de jogos pagos e Gratuitos------   
  if lista [7] == '0.0':
    gratuitos += 1
  else:
    pagos+=1
  print (lista)
#______Determinar os anos com mais lançamentos de jogos novos____
  ano= lista[3]
  if ano in jogos_por_ano:
    jogos_por_ano[ano] += 1
  else:
    jogos_por_ano[ano] = 1


print (gratuitos/(gratuitos+pagos)*100,'% de jogos gratuitos')
print (pagos/(pagos+gratuitos)*100,'% de jogos pagos') 
for ano, quantidade in jogos_por_ano.items():
  print(f"Ano {ano}: {quantidade} jogos novos")