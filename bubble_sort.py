def bubble_sort(arr):
    """
    冒泡排序：重复地比较相邻元素，若顺序错误则交换，
    每一轮把当前未排序部分的最大值“冒泡”到末尾。

    时间复杂度: 最坏/平均 O(n^2)，最好 O(n)（已有序时）
    空间复杂度: O(1)（原地排序）
    稳定性: 稳定排序

    :param arr: 待排序的列表
    :return: 排序后的列表（原地排序，同时返回引用）
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # 优化：若某一轮没有发生交换，说明已经有序
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    print("排序后:", bubble_sort(data))
