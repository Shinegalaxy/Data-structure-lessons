def heapify(arr, n, i):
    
    largest = i
    left = 2 * i + 1  # Left child 
    right = 2 * i + 2  # Right child 

   
    if left < n and arr[left] > arr[largest]:
        largest = left

    
    if right < n and arr[right] > arr[largest]:
        largest = right

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)  

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)  

if __name__ == "__main__":
    data = []

    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            data.append(number)
        except ValueError:
            print("Invalid input, please enter a number or 'done'.")

    print("Unsorted data:", data)

    heap_sort(data)
    print("Sorted data:", data)
