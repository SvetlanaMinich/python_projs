def compress(chars):
    if len(chars) == 1:
        return 1
    repeat_count = 0
    start_index = 0
    i = 0
    while i < len(chars):
        while i < len(chars) - 1 and chars[i] == chars[i + 1]:
            i += 1
            repeat_count += 1
        if repeat_count == 0:
            chars[start_index] = chars[i]
            start_index += 1
            i += 1
            continue
        repeat_count += 1
        chars[start_index] = chars[i - repeat_count + 1]
        start_index += 1
        if repeat_count < 10:
            chars[start_index] = str(repeat_count)
            start_index += 1
        elif repeat_count < 100:
            chars[start_index + 1] = str(repeat_count % 10)
            chars[start_index] = str(repeat_count // 10)
            start_index += 2
        elif repeat_count < 1000:
            chars[start_index + 2] = str(repeat_count % 10)
            chars[start_index + 1] = str((repeat_count % 100) // 10)
            chars[start_index] = str(repeat_count // 100)
            start_index += 3
        elif repeat_count >= 1000:
            chars[start_index + 3] = str(repeat_count % 10)
            chars[start_index + 2] = str((repeat_count % 100) // 10)
            chars[start_index + 1] = str((repeat_count % 1000) // 100)
            chars[start_index] = str(repeat_count // 1000)
            start_index += 4
        repeat_count = 0
        i += 1
    return start_index

def move_zeroes(nums):
        if len(nums) == 1:
            return nums
        if all(x == 0 for x in nums):
            return nums
        last_el = nums[len(nums) - 1]
        nums[len(nums) - 1] = 'l'
        for i in nums:
            if i == 'l':
                nums[nums.index(i)] = last_el
                return nums
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

def max_operations(nums, k):
        if len(nums) < 2:
            return 0
        i = 0
        j = len(nums) - 1
        oper_num = 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                oper_num += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return oper_num

def findMaxAverage(nums, k):
        sum_of_k = 0
        max_avr = 0
        for i in range(len(nums)):
            if i < k:
                sum_of_k += nums[i]
                max_avr = sum_of_k / (i + 1)
                continue
            sum_of_k -= nums[i-k]
            sum_of_k += nums[i]
            max_avr = max(max_avr, sum_of_k / k)
        return max_avr

print(findMaxAverage([1,12,-5,-6,50,3],4))   