import numpy as np
precos_acoes = np.array([ 
      [150, 200, 180, 220, 170], 
      [155, 205, 185, 225, 175], 
      [160, 210, 190, 230, 180],
      [165, 215, 195, 235, 185], 
      [170, 220, 200, 240, 190], 
      [175, 225, 205, 245, 195], 
      [180, 230, 210, 250, 200] 
])
print("Média diaria dos preços das ações da empresa ao longo dos dias da semana")
media_acoes = np.mean(precos_acoes, axis=0)
print(f"Empresa A= {media_acoes[0]} Empresa B= {media_acoes[1]} Empresa C= {media_acoes[2]} Empresa D= {media_acoes[3]} Empresa E= {media_acoes[4]}")
print("\n")
print("Variação Diaria do valor dos valores das empresas")
variacao_diaria = np.max(precos_acoes, axis=0) - np.min(precos_acoes, axis=0)
print(f"Empresa A= {variacao_diaria[0]} Empresa B= {variacao_diaria[1]} Empresa C= {variacao_diaria[2]} Empresa D= {variacao_diaria[3]} Empresa E= {variacao_diaria[4]}")
preco_b = precos_acoes[:, 1]
dia_maior_preco = np.argmax(preco_b)
dia_menor_preco = np.argmin(preco_b)
print(f"O dia de B com mais valor é= {dia_maior_preco + 1}\nO dia de B com menor valor é= {dia_menor_preco + 1}\n")
aumento_acoes = precos_acoes[4] * 1.05
print(f"Novos preços das ações = {aumento_acoes}\n")
media_acoes = np.mean(precos_acoes, axis=0) 
print("Nova media diarias dos preços das ações")
print(f"Empresa A= {media_acoes[0]} Empresa B= {media_acoes[1]} Empresa C= {media_acoes[2]} Empresa D= {media_acoes[3]} Empresa E= {media_acoes[4]}")