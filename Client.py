import rpyc

# pede ao usuário o tamanho do vetor
n = int(input("Digite o tamanho do vetor: "))

# cria o vetor com elementos variando de 0 a n-1
vetor = list(range(n))
# imprime o vetor
print(vetor)
# conecta ao servidor localmente
conn = rpyc.connect("localhost", 18861)

# chama o método remoto para calcular a soma do vetor
soma = conn.root.soma_vetor(vetor)

# imprime a soma
print("A soma dos elementos do vetor é:", soma)