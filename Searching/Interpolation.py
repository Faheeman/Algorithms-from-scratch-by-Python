def is_sorted(lis):
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            lis.sort()
            return lis
    return lis

def interpolation_search(sorted_list, Lo, X, Hi):
    
    if Lo > Hi or X < sorted_list[Lo] or X > sorted_list[Hi]:
        return -1
    
    if Lo == Hi:
        if sorted_list[Lo] == X:
            return Lo
        else:
            return -1
    
    if sorted_list[Hi] == sorted_list[Lo]:
        for i in range(Lo, Hi + 1):
            if sorted_list[i] == X:
                return i
        return -1
    
    Mid = Lo + int(((X - sorted_list[Lo]) / (sorted_list[Hi] - sorted_list[Lo])) * (Hi - Lo))
    
    if Mid < Lo:
        Mid = Lo
    elif Mid > Hi:
        Mid = Hi
    
    if sorted_list[Mid] == X:
        return Mid
    elif X < sorted_list[Mid]:
        return interpolation_search(sorted_list, Lo, X, Mid - 1)
    else:
        return interpolation_search(sorted_list, Mid + 1, X, Hi)

def interpolation_search_iterative(sorted_list, X):
    
    Lo = 0
    Hi = len(sorted_list) - 1
    
    while Lo <= Hi and X >= sorted_list[Lo] and X <= sorted_list[Hi]:
        if Lo == Hi:
            if sorted_list[Lo] == X:
                return Lo
            else:
                return -1
        
        if sorted_list[Hi] == sorted_list[Lo]:
            for i in range(Lo, Hi + 1):
                if sorted_list[i] == X:
                    return i
            return -1
        
        Mid = Lo + int(((X - sorted_list[Lo]) / (sorted_list[Hi] - sorted_list[Lo])) * (Hi - Lo))
        
        if Mid < Lo:
            Mid = Lo
        elif Mid > Hi:
            Mid = Hi
        
        if sorted_list[Mid] == X:
            return Mid
        elif X < sorted_list[Mid]:
            Hi = Mid - 1
        else:
            Lo = Mid + 1
    
    return -1

def find_all_occurrences(sorted_list, X):
    
    first_found = interpolation_search_iterative(sorted_list, X)
    
    if first_found == -1:
        return []
    
    indices = [first_found]
    
    left_idx = first_found - 1
    while left_idx >= 0 and sorted_list[left_idx] == X:
        indices.insert(0, left_idx)
        left_idx -= 1
    
    right_idx = first_found + 1
    while right_idx < len(sorted_list) and sorted_list[right_idx] == X:
        indices.append(right_idx)
        right_idx += 1
    
    return indices

def count_duplicates(sorted_list):
    
    if not sorted_list:
        return {}
    
    duplicates = {}
    i = 0
    
    while i < len(sorted_list):
        count = 1
        current_value = sorted_list[i]
        
        while i + count < len(sorted_list) and sorted_list[i + count] == current_value:
            count += 1
        
        if count > 1:
            duplicates[current_value] = count
        
        i += count
    
    return duplicates

def test_interpolation_search():
    """Test function to verify the implementation works correctly"""
    test_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10]
    print("Test list:", test_list)
    
    test_cases = [1, 2, 4, 7, 10, 11, 0]
    
    for x in test_cases:
        result = interpolation_search_iterative(test_list, x)
        all_occurrences = find_all_occurrences(test_list, x)
        print(f"Search {x}: Single result = {result}, All occurrences = {all_occurrences}")

if __name__ == "__main__":
    print("=== Testing the implementation ===")
    test_interpolation_search()
    print("\n" + "="*50 + "\n")
    
    lis = [2, 3, 4, 5, 2, 4, 6, 8, 9, 36, 47, 3, 24, 89, 7, 54, 34, 123, 34, 67, 9847]
    sorted_list = is_sorted(lis)
    
    print("Original list:", lis)
    print("Sorted list:", sorted_list)
    print()
    
    duplicates = count_duplicates(sorted_list)
    if duplicates:
        print("Duplicate values found:")
        for value, count in duplicates.items():
            print(f"  Value {value} appears {count} times")
        print()
    else:
        print("No duplicates found in the list")
        print()
    
    try:
        X = int(input("Which number you want to search: "))
        
        all_indices = find_all_occurrences(sorted_list, X)
        
        if all_indices:
            if len(all_indices) == 1:
                print(f"Item {X} found at index {all_indices[0]}")
            else:
                print(f"Item {X} found at {len(all_indices)} positions:")
                for i, idx in enumerate(all_indices):
                    print(f"  Occurrence {i+1}: index {idx}")
        else:
            print(f"Item {X} not found in the list")
        
        print()
        
        print("Using recursive interpolation search:")
        result = interpolation_search(sorted_list, 0, X, len(sorted_list) - 1)
        
        if result != -1:
            print(f"Item {X} found at index {result}")
        else:
            print(f"Item {X} not found in the list")
        
        print("\nUsing iterative interpolation search:")
        result_iterative = interpolation_search_iterative(sorted_list, X)
        
        if result_iterative != -1:
            print(f"Item {X} found at index {result_iterative}")
        else:
            print(f"Item {X} not found in the list")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")