import sqlite3

# 1. Conectando ao seu banco de dados
conexao = sqlite3.connect('meu_quarto_v2.db')
cursor = conexao.cursor()
# Atualizando as paredes de cada móvel
cursor.execute("""
CREATE TABLE IF NOT EXISTS moveis (
    nome TEXT,
    largura REAL,
    comprimento REAL,
    parede TEXT
)
""")

# Inserindo os móveis já com as paredes certas!
cursor.execute("DELETE FROM moveis")
cursor.execute("INSERT INTO moveis (nome, largura, comprimento, parede) VALUES ('guarda roupa', 1.3, 0.6, 'Parede B')")
cursor.execute("INSERT INTO moveis (nome, largura, comprimento, parede) VALUES ('cama', 1.55, 2.0, 'Parede C')")
cursor.execute("INSERT INTO moveis (nome, largura, comprimento, parede) VALUES ('televisao', 1.0, 0.2, 'Parede A')")
conexao.commit()

# 2. Buscando as larguras dos móveis na tabela
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

# --------------------------------------------------
# NOVIDADE: Buscando e mostrando as paredes no terminal
# --------------------------------------------------
print("\n--- Organização das Paredes ---")
dados_paredes = cursor.execute("SELECT nome, parede FROM moveis")

for movel in dados_paredes:
    nome_do_movel = movel[0]
    parede_do_movel = movel[1]
    print(f"📌 O móvel '{nome_do_movel}' foi alocado na: {parede_do_movel}")
    # Fechando a conexão no final de tudo
conexao.close()