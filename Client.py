import sys
import time
import rpyc


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
    
server = sys.argv[1]

# pede ao usuário o tamanho do vetor
n = int(input("Digite o tamanho do vetor: "))

# cria o vetor com elementos variando de 0 a n-1
vetor = list(range(n))
# imprime o vetor
# print(vetor)
start = time.time()
# conecta ao servidor localmente
conn = rpyc.connect(server, 18861)
conn._config['sync_request_timeout'] = 100
# chama o método remoto para calcular a soma do vetor
soma = conn.root.soma_vetor(vetor)
end = time.time()
print(end-start)

# imprime a soma
print("A soma dos elementos do vetor é:", soma)