def find_max_sum(numbers):
    
    if len(numbers) == 0:
        return None

    if len(numbers) == 1 and numbers[0] >= 0:
        return numbers[0]

    if len(numbers) == 1 and numbers[0] < 0:
        return None

    if len(numbers) > 1:
        if max(numbers) >= 0:
            
            larger = max(numbers)
            if larger == 0:
                return 0
            
            comparador = [numbers[i] for i in range(0, len(numbers)) if numbers[i] >= 0 and numbers[i] != larger]
        
            if comparador:
                next_larger = max(comparador)
        
            if larger and next_larger:
                sum = larger + next_larger
            else:
                if larger and larger >= 0:
                    sum = larger
                else:
                    sum = None
        else:
            sum = None

        return sum
    
if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
    print(find_max_sum([5, -9, 7, -11]))
    print(find_max_sum([5]))
    print(find_max_sum([5,11]))
    print(find_max_sum([0, 5]))
    print(find_max_sum([0, -5]))
    print(find_max_sum([-1, -5]))
    print(find_max_sum([0]))
    print(find_max_sum([]))