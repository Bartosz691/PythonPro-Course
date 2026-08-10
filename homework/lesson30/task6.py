from multiprocessing import Process
import math

def oblicz_silnie():
    wynik = math.factorial(10)
    print(f"10! = {wynik}")
    
    
if __name__ == "__main__":
    proces = Process(target=oblicz_silnie)
    
    proces.start()
    proces.join()
    
print("Proces zakończył pracę ")