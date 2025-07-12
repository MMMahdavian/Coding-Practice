def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # آرایه‌های خالی یا تک‌عنصری مرتب‌اند
    
    pivot = arr[len(arr) // 2]  # انتخاب محور از وسط
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
    
a = [24, 52, 8, 874 ,87 ,3 ,214 ,-60 ,5 ,54 ,5 ,34 ,141 ,44]
print(quick_sort(a))