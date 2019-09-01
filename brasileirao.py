'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirão) para estudar como acessar listas, dicionários,
e estruturas encadeadas (listas dentro de dicionários dentro de listas).

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor.

Se quiser ver os dados dentro do python, pode chamar a função
pega_dados.
'''

'''
1. Crie uma função datas_de_jogo, que procura nos dados do brasileirão
recebidas no parâmetro e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas as
informações que foram lidas do arquivo JSON que acompanha essa atividade.
'''
def datas_de_jogo(dados):
   
   datas = []

   for i in dados["fases"]["2700"]["jogos"]["data"]:
      datas.append(i)

   return datas

'''
2. Crie uma função data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como strings)
'''
def data_de_um_jogo(dados, id_jogo):
   
   if id_jogo in dados["fases"]["2700"]["jogos"]["id"]:

      return dados["fases"]["2700"]["jogos"]["id"][id_jogo]["data"]
   else:
      return "não encontrado"


'''
3. Nos nossos dados, cada time tem um id, uma identificação numérica.
(você pode consultar as identificações numéricas em dados['equipes']).

Essas ids também aparecem nos jogos (onde? dê uma procurada!)

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas em um único return.
'''
def ids_dos_times_de_um_jogo(dados, id_jogo):

   time_a = dados["fases"]["2700"]["jogos"]["id"][id_jogo]["time1"]
   time_b = dados["fases"]["2700"]["jogos"]["id"][id_jogo]["time2"]
   
   return time_a, time_b

'''
4. A próxima função recebe a id_numerica de um time e deve retornar o seu 'nome-comum'.
'''
def nome_do_time(dados, id_time):
   
   time = dados["equipes"][id_time]["nome-comum"]
   return time

'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times.
'''
def nomes_dos_times_de_um_jogo(dados, id_jogo):

   id_time_a = dados["fases"]["2700"]["jogos"]["id"][id_jogo]["time1"]
   id_time_b = dados["fases"]["2700"]["jogos"]["id"][id_jogo]["time2"]

   time_a = dados["equipes"][id_time_a]["nome-comum"]
   time_b = dados["equipes"][id_time_b]["nome-comum"]

   times = [time_a, time_b]
   
   return times

'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.

Se o nome comum não existir, retorne 'não encontrado'.
'''
def id_do_time(dados, nome_time):
   
   for i in dados["equipes"]:
      
      if nome_time in dados["equipes"][i]["nome-comum"]:

         return i

   return "não encontrado"

'''
7. Agora, façamos uma busca "fuzzy". Queremos procurar por 'Fla'
e achar o Flamengo. Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''
def busca_imprecisa_por_nome_de_time(dados, nome_time):

   resultados = []

   for i in dados["equipes"]:
      
      nome = dados["equipes"][i]["nome"]
      nome_comum = dados["equipes"][i]["nome-comum"]
      nome_slug = dados["equipes"][i]["nome-slug"]
      sigla = dados["equipes"][i]["sigla"]

      if nome.find(nome_time) != -1:
         resultados.append(i)
      elif nome_comum.find(nome_time) != -1:
         resultados.append(i)
      elif nome_slug.find(nome_time) != -1:
         resultados.append(i)
      elif sigla.find(nome_time) != -1:
         resultados.append(i)

   return resultados

'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''
def ids_de_jogos_de_um_time(dados, time_id):
    pass

'''
9. Usando as ids dos jogos em que um time participou, podemos descobrir
em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''
def datas_de_jogos_de_um_time(dados, nome_time):
    pass

'''
10. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve um dicionário, com quantos gols cada time fez.
'''
def dicionario_de_gols(dados):
    pass

'''
11. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve a id do time que fez mais gols no campeonato.
'''
def time_que_fez_mais_gols(dados):
    pass

'''
12. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    pass

'''
13. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela retorna o número de times que o brasileirão qualifica para a libertadores.
Ou seja, devolve quantos times são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e você deve pegar esse
número daí. Não basta retornar o valor correto, tem que acessar os dados
fornecidos.
'''
def qtos_libertadores(dados):
    pass

'''
14. A próxima função recebe um tamanho, e retorna uma lista
com len(lista) = tamanho, contendo as ids dos times melhor classificados.
'''
def ids_dos_melhor_classificados(dados, numero):
    pass

'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a classificação, quanto
para obter o número correto de times a retornar.

A função só recebe os dados do brasileirão.
'''
def classificados_libertadores(dados):
    pass

'''
16. Da mesma forma que podemos obter a informação dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do brasileirão,
e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''
def rebaixados(dados):
    pass

'''
17. A próxima função recebe (além do dicionario de dados do brasileirão) uma id de time.

Ela retorna a classificação desse time no campeonato.

Se a id nao for válida, ela retorna a string 'não encontrado'.
'''
def classificacao_do_time_por_id(dados, time_id):
    pass

def pega_dados():
    import json
    with open('ano2018.json') as f:
        return json.load(f)

dados = pega_dados()
#print(datas_de_jogo(dados))
#print(data_de_um_jogo(dados, "102278"))
#print(ids_dos_times_de_um_jogo(dados, "102109"))
#print(nome_do_time(dados, "695"))
#print(nomes_dos_times_de_um_jogo(dados, "102099"))
#print(id_do_time(dados, "Chapecoense"))

#print(busca_imprecisa_por_nome_de_time(dados, "Bot"))