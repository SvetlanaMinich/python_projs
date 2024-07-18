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

print(move_zeroes([0,1]))    