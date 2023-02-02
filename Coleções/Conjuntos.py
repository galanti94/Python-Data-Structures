# O set não garante a ordem, somente que um elemento não se repete

set([1,2,3,5,4,3,2,2,2,1]) #{1, 2, 3, 4, 5}

linguagens = {"python", "java", "python", "c++"} #{'java', 'c++', 'python'}

# É preciso transformar o set em um lista para consumir as informações
list = list(linguagens)

a = input() 
b = input() 
c = input() 

resposta = 'erro'

if a == 'vertebrado': 
    if b == 'ave':
        if c == 'carnivoro':
            resposta = 'aguia'
        else:
            resposta = 'pomba'  
    else:
        if c == 'onivoro':
            resposta = 'homem'
        else:
          resposta = 'vaca'


elif a == 'invertebrado':
    pass
  
print(resposta)