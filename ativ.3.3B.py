departamento = input('Digite o departamento (financeiro , RH, Vendas, TI, Marketing): ').strip ().lower()

if departamento == 'financeiro': 
    print('recomendação: Computadores desktop de alto desempenho')
elif departamento == 'RH':
    print('recomendação: Laptops leves e softwares de gestão de pessoas')
elif departamento == "vendas":
    print("Recomendação: Tablets e smartphones para mobilidade.")
elif departamento == "ti":
    print("Recomendação: Computadores de alta performance e servidores dedicados.")
elif departamento == "marketing":
    print("Recomendação: Laptops potentes com softwares de edição gráfica.")
else:
    print("Departamento não encontrado. Por favor, verifique o nome digitado.")