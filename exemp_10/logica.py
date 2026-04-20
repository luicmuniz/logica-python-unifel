from decimal import Decimal

#Simulador de Aprovação de Crédito
# Objetivo: Desenvolver um algoritimo de decisão lógica para um banco digital 
# que determina se um cliente pode ou não receber um emprestimo.

# Tarefas:
# Criar variáveis para armazenar os dados do cliente (Renda, Nome Limpo, Fiador e Idade)
# Aplicar as Regras de Negocio usando operadores lógicos e relacionais.
# Exibir o veredito final (true ou false) sobre a decisão de dar ou não o crédito.
# Regras de Negócio (Obrigatórias):

# Regra 1 (Saúde Financeira): O cliente deve ter renda acima de R$ 3.000,00 E o nome
# deve estar limpo (não negativado).
# Regra 2 (Garantia Alternativa): Se o cliente não passar na Regra 1, ele ainda pode
# ser aprovado se tiver um Fiador).
# Regra 3 (Restrição Etária): Em qualquer um dos casos acima, o cliente NÃO pode ter
# menos de 18 anos e maior que 65.

print("-" * 30)
print("--- SISTEMA DE CRÉDITO | LÓGICA COM PYTHON 2026.3 ---")
print("-" * 30)

#ENTRADA DE DADOS
#Renda, Nome Limpo, Fiador e Idade

renda = Decimal(input("Digite a renda mensal: "))
sem_restricao = input("O nome está limpo? (sim/não)").lower() == "sim" #== sim, quer dizer se sim
tem_fiador = input("Possui fiador? (sim/nao)").lower() =="sim"
idade = int(input("Digite a idade: "))

#Regra.A 3 (Tem que ser a primeira regra pois ela é obrigatoria)
criterio_idade = 18 <= idade <= 65 #A idade entre 18 e 65
#print("Crédito Reprovado. Motivo: O cliente é menor de idade ou tem mais de 65 anos! ")


#Regra.C 2
criterio_renda = tem_fiador == True

#Regra.B 1
saude_financeira = (renda > 3000) and sem_restricao

#Regra.C 2 Coloquei antes de saude_financeira
# criterio_renda = saude_financeira or tem_fiador
# criterio_renda = tem_fiador == True

aprovado = criterio_idade and (saude_financeira or criterio_renda)


#Regra. 3
# criterio_idade = 18 <= idade <= 65 #A idade entre 18 e 65
# regra 3 tem que ser a primeira

#Saída:
mensagem = aprovado and "PARABÉNS: Crédito aprovado!" or "Crédito negado."
print(f"RESULTADO DA ANÁLISE: {mensagem}")
print("-" * 40)