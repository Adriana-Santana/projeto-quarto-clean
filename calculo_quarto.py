import sqlite3

# 1. Conectando ao seu banco de dados
conexao = sqlite3.connect('meu_quarto.db')
cursor = conexao.cursor()

# 2. Buscando as larguras dos móveis na tabela
# (Usei 'moveis' com letra minúscula conforme estava na sua foto)
cursor.execute("SELECT largura FROM moveis")
resultados = cursor.fetchall()

# 3. Fazendo as contas
largura_total_ocupada = 0
for linha in resultados:
    largura_total_ocupada += linha[0]

parede_disponivel = 2.90
espaco_restante = parede_disponivel - largura_total_ocupada

# 4. Mostrando o resultado na tela
print("-" * 30)
print(f"Total ocupado pelos móveis: {largura_total_ocupada:.2f}m")
print(f"Espaço que sobra na parede: {espaco_restante:.2f}m")

if espaco_restante >= 0:
    print("✅ Sucesso! Os móveis cabem na parede.")
else:
    print("❌ Cuidado! Os móveis ultrapassam o limite da parede.")
print("-" * 30)

# Fechando a conexão
conexao.close()