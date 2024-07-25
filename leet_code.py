import math

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

def find_max_average(nums, k):
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

def longest_ones(nums, k):
    cur_sub_len = 0
    max_sub_len = 0
    zero_num = 0
    sub_start = 0
    nums_len = len(nums)
    i = 0
    if k == 0:
        while i < nums_len:
            if nums[i] == 0:
                max_sub_len = max(max_sub_len, cur_sub_len)
                cur_sub_len = -1
            cur_sub_len += 1
            i += 1
    elif k >= nums_len:
        return nums_len
    else:
        while i < nums_len:
            if zero_num == k and nums[i] == 0:
                max_sub_len = max(max_sub_len, cur_sub_len - sub_start)
                zero_num -= 1
                while nums[sub_start] != 0:
                    sub_start += 1
                sub_start += 1
            if nums[i] == 0:
                zero_num += 1
            cur_sub_len += 1
            i += 1
    max_sub_len = max(max_sub_len, cur_sub_len - sub_start)
    return max_sub_len

def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum_list = []
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        i = nums_len - 1
        sum_el = 0
        while i >= 0:
            sum_el += nums[i]
            right_sum_list.insert(0, sum_el)
            i -= 1
        sum_el = 0
        i = 0
        while i < nums_len:
            sum_el += nums[i]
            nums[i] = sum_el
            i += 1
        i = 1
        if right_sum_list[1] == 0:
            return 0
        while i < nums_len - 1:
            if nums[i-1] == right_sum_list[i+1]:
                return i
            i += 1  
        if nums[nums_len-2] == 0:
            return nums_len - 1  
        return -1

def find_difference(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        while i < len(nums1):
            ch = nums1[i]
            if ch in nums2:
                while ch in nums1:
                    nums1.remove(ch)
                    i -= 1
                while ch in nums2:
                    nums2.remove(ch)
            i += 1
        for i in nums1:
            while nums1.count(i) > 1:
                nums1.remove(i)
        for i in nums2:
            while nums2.count(i) > 1:
                nums2.remove(i)
        return [nums1,nums2]

def equal_pairs(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        rows = []
        columns = []
        column = []
        for i in range(n):
            rows.append(grid[i])
        for i in range(n):
            for j in range(n):
                column.append(grid[j][i])
            columns.append(column)
            column = []
        count = 0
        for i in rows:
            if i in columns:
                count += columns.count(i)
        return count  


def remove_stars(s):
        """
        :type s: str
        :rtype: str
        """
        # while s.index('*') == 0:
        #     s.remove('*')
        # while '*' in s:
        #     star_index = s.index('*')
        #     s = s[:star_index-1] + s[star_index+1:]
        # return s
        stack = []
    
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        # Convert stack to string
        return ''.join(stack)

def asteroid_collision(asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for i in asteroids:
            if i > 0:
                res.append(i)
            else:
                cur = (-1)*i
                if res:
                    el = res.pop()
                    if el > 0:
                        if cur < el:
                            res.append(el)
                        elif cur > el:
                            while cur > el and res and el > 0:
                                el = res.pop()
                            if el < 0:
                                res.append(el)
                                res.append(i)
                            elif cur < el:
                                res.append(el)
                            elif cur == el:
                                continue
                            elif len(res) == 0:
                                res.append(i)
                    else:
                        res.append(el)
                        res.append(i)
                else:
                    res.append(i)
        return res


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # res = ""
        # nums = "0123456789"
        # count = ""
        # rep = True
        # while rep == True:
        #     in_len = 0
        #     str_to_repeat = ""
        #     slen = len(s)
        #     i = 0
        #     while i < slen:
        #         if s[i] in nums:
        #             while s[i] in nums:
        #                 count += s[i]
        #                 i += 1
        #             count = int(count)
        #             ind_of_close = s[i+1:].find(']') + i + 1
        #             ind_of_start = s[i+1:].find('[')
        #             if ind_of_start != -1:
        #                 ind_of_start += i + 1
        #                 if ind_of_start < ind_of_close:
        #                     while ind_of_start < ind_of_close:
        #                         in_len += 1
        #                         ind_of_close = s[i+1:].find(']') + i + 1
        #                         ind_of_start = s[i+1:].find('[') + i + 1
        #                     while in_len > 0:
        #                         ind_of_close = s[i+1:].find(']') + i + 1
        #                         in_len -= 1
        #             i += 1
        #             while i < ind_of_close:
        #                 str_to_repeat += s[i]
        #                 i += 1
        #             res += (str_to_repeat * count)
        #         else:
        #             res += s[i]
        #         i += 1
        #         str_to_repeat = ""
        #         count = ""

        #     if '[' in res:
        #         s = res
        #         res = ""
        #     else:
        #         rep = False    
        # return res

        rs = ""
        res = []
        str_to_rep = ""
        count = ""
        nums = "0123456789"
        for i in s:
            if i == ']':
                el = i
                while el != '[':
                    el = res.pop()
                    if el == '[':
                        break
                    str_to_rep = el + str_to_rep
                el = res.pop()
                count += el
                while res:
                    el = res.pop()
                    if el not in nums:
                        res.append(el)
                        break
                    count += el
                count = int(count[::-1])
                res.append(str_to_rep * count)
                str_to_rep = ""
                count = ""
            else:
                res.append(i)
        for i in res:
            rs += i
        return rs

s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")