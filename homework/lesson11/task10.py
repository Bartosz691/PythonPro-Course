class A:
    def kim_jestem(self):
        print("Jestem z klasy A")

class B(A):
    def kim_jestem(self):
        print("jestem z klasy B")
        
class C(A):
    def kim_jestem(self):
        print("jestem z klasy C")
    
class D(B):
    def kim_jestem(self):
        print("Jestem z klasy D")

class E(C):
    def kim_jestem(self):
        print("jestem z klasy E")

class F(D,E):
    def kim_jestem(self):
        print("jestem z klasy F")
        
f = F()
f.kim_jestem()

print("\nMRO dla klasy F: ")
print(F.mro())