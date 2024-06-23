# define function max_in_sliding_window (nums_list, k)
def max_in_sliding_window(nums_list, k):
    result_list = []
    # kiem tra rang buoc: so lan truot phai >= 1
    if k > len(nums_list):
        print(f"k = {k} lớn hơn độ dài của danh sách len = {
              len(nums_list)} nên không thực hiện được.")
        return
    if k < 1:
        print("k phải >= 1.")
        return
    for i in range(len(nums_list) - k + 1):
        result_list = result_list + [max(nums_list[i:i+k])]
    print(result_list)


# test function max_in_sliding_window (nums_list, k)
nums_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
max_in_sliding_window(nums_list, k)
