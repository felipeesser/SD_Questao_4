import time
import rpyc

class MyService(rpyc.Service):
    def exposed_soma_vetor(self, vetor):
        start = time.time()
        # calcula a soma dos elementos do vetor
        soma = sum(vetor)
        end = time.time()
        print(end-start)
        return soma

# inicia o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()