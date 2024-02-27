def heapSort(input_list):
    def heapAdjust(input_list, parent, length):
        temp = input_list[parent]
        child = parent * 2 + 1
        
        while child < length:
            if child + 1 < length and input_list[child+1] > input_list[child]:
                child += 1
            if temp > input_list[child]:
                break
            else:
                input_list[parent] = input_list[child]
                parent = child
                child = parent * 2 + 1
        input_list[parent] = temp
        return
    
    if len(input_list) == 0:
        return []
    
    len_il = len(input_list)
    for i in range(len_il // 2 - 1, -1, -1):
        heapAdjust(input_list, i, len_il)
    
    for j in range(len_il - 1, 0, -1):
        temp = input_list[j]
        input_list[j] = input_list[0]
        input_list[0] = temp

        heapAdjust(input_list, 0, j)
    return input_list

if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print('排序前:', input_list)
    sorted_list = heapSort(input_list)
    print('排序后:', sorted_list)