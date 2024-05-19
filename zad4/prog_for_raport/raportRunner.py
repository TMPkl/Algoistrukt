from dataGen.cyclic.eGen import generate_eulers_graph
from dataGen.cyclic.hGen import generate_hamiltonian_graph
from EulerR import EulerR
from HamiltonR import HamiltonR


# print("Hamilton,cykle")
# for k in range(10,511,50):
    
#     for nasycenie in range(10,91,10):
#         print(f"K={k}\tnasycenie={nasycenie}",end="\t")
#         for _ in range(10):
#             generate_hamiltonian_graph(k,nasycenie)
#             HamiltonR()
#         print()
# print("\n")

print("Euler,cykle")
for k in range(10,511,50):
    
    for nasycenie in range(10,91,10):
        print(f"K={k}\tnasycenie={nasycenie}",end="\t")
        for _ in range(10):
            generate_eulers_graph(k,nasycenie)
            EulerR()
        print()
print("\n")