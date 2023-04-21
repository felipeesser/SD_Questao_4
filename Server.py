import rpyc

class MyService(rpyc.Service):
    def exposed_soma_vetor(self, vetor):
        # calcula a soma dos elementos do vetor
        soma = sum(vetor)
        return soma

# inicia o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()