import rpyc
import sys
if len(sys.argv) < 2:
    sys.exit("Usage {} SERVER".format(sys.argv[0]))
server = sys.argv[1]
conn = rpyc.connect(server,18861)
print(conn)
print(conn.root.exposed_get_answer())
print(conn.root.exposed_the_real_answer_though)