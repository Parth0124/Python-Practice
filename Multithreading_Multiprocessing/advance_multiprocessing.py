from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    print(f"Square: {number*number}")

numbers=[1,2,3,4,5]

if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executer:
        results=executer.map(square_numbers, numbers)

    for result in results:
        print(result)