#funções:
def classificar_desempenho(pontuacao):
  if pontuacao < 50:
    return "Insuficiente"
  elif pontuacao <= 69:
    return "Regular"
  elif pontuacao <= 89:
    return "Bom"
  else:
    return "Excelente"

def calcular_score_gerencial(experiencia_anos, projetos_entregues, pontuacao_desempenho):
  score=(experiencia_anos*2)+projetos_entregues+pontuacao_desempenho
  return score
  

# calculando salário liquido
def calcular_salario_liquido(salario_base, bonus, descontos):
  salario_liquido=salario_base+bonus-descontos
  return salario_liquido


def calcular_horas_extras(valor_hora, horas_realizadas):
  valor_hora_extra=valor_hora * 1.5
  salario_adicional=valor_hora_extra * horas_realizadas
  return salario_adicional

def calcular_desconto_falta(salario_base, dias_falta):
  descontado=(salario_base/30)*dias_falta
  return descontado





opção = "s"

while opção == "s":
    print("=== PAINEL DE GESTÃO DE RECURSOS HUMANOS ===")
    print("1. Calcular Score Gerencial do Colaborador")
    print("2. Simular Salário Líquido (Horas Extras / Descontos)")
    print("3. Avaliar Nível de Desempenho")
    print("4. Sair")

    decisao=int(input("Selecione a sua opção => "))

    
    
    if decisao == 1:
        #aqui eu posso já perguntar em horas, ou fazer no def um programa que
        #transforma horas em anos. Obs: perguntar para o Victor
        tempo_casa=float(input("Qual o seu tempo em casa? (Em anos) "))
        projetos_finalizados=int(input("Quantos projetos você finalizou? "))
        pontuation = int(input("Qual o seu nivel de pontução? "))
        score_gerencial=calcular_score_gerencial(tempo_casa, projetos_finalizados, pontuation)
        
        print(f"O seu score gerencial é de {score_gerencial}")
    elif decisao == 2:
        base_money=float(input("Qual o seu salário base mensal? "))
        absents=int(input("Quantas faltas não justificadas você possui? "))
        normal_hour=float(input("Qual é o valor da hora normal? "))
        extra_hour=int(input("Quantas horas extras você possui? "))
        descontado = calcular_desconto_falta(base_money, absents)
        salario_adicional = calcular_horas_extras(normal_hour, extra_hour)
        salario_final=calcular_salario_liquido(base_money, salario_adicional, descontado)
       

        print(f"O seu salário liquído é de {salario_final} R$")
    elif decisao == 3:
        pontuation = int(input("Qual o seu nivel de pontução? "))
        nivel_desempenho = classificar_desempenho(pontuation)

        print(f"O seu nível de classificação é {nivel_desempenho}")
    elif decisao == 4:
        opção = "n"

        print("Programa encerrado")
    else:
        print("Opção inválida")
        print("Tente novamente:")