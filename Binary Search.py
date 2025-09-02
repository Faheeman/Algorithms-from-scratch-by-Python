def is_sorted(lis):
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            lis.sort()
            return lis
    return lis

def Bin_search_all(sorted_list, low, high, element): 
    if low <= high:
        mid = (low + high) // 2   
        if sorted_list[mid] == element:
            positions = [mid]
            
            left = mid - 1
            while left >= 0 and sorted_list[left] == element:
                positions.append(left)
                left -= 1
            
            right = mid + 1
            while right < len(sorted_list) and sorted_list[right] == element:
                positions.append(right)
                right += 1
            
            positions.sort()
            print(f"The number {element} is found at positions {[p+1 for p in positions]}")
            return
        elif element < sorted_list[mid]:
            Bin_search_all(sorted_list, low, mid-1, element)
        else:
            Bin_search_all(sorted_list, mid+1, high, element)
    else:
        print("Element not found")

if __name__ == "__main__":
    lis = [2, 2, 3, 4,5,8,9,34]
    sorted_list = is_sorted(lis)
    element = int(input("Which number you want to search: "))
    Bin_search_all(sorted_list, 0, len(sorted_list)-1, element)
