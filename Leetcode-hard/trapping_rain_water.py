def calculate_trapped_rain_water(height) -> int:
        n = len(height)
        i = 0
        j = n - 1
        total = 0
        while i < j:
            if i == 0:
                left_high = height[0]
                right_high = height[-1]
                i += 1
                continue
            if height[i] >= left_high:
                left_high = height[i]
                i += 1
                continue
            if height[i] < left_high and height[i] < right_high and left_high <= right_high:
                total += min(left_high, right_high) - height[i]
                i += 1
                continue
            else:
                if j == n-1:
                    j-=1
                    if i == j:
                        if height[i] < left_high and height[i] < right_high:
                            total += min(left_high, right_high) - height[i]
                    if height[j] > right_high:
                        right_high = height[j]
                    continue
                if height[j] < left_high and height[j] < right_high:
                    total += min(left_high, right_high) - height[j]
                    j -= 1
                    if i == j:
                        if height[i] < left_high and height[i] < right_high:
                            total += min(left_high, right_high) - height[i]
                    if height[j] > right_high:
                        right_high = height[j]
                    continue
                else:
                    j -= 1
                    if i == j:
                        if height[i] < left_high and height[i] < right_high:
                            total += min(left_high, right_high) - height[i]
                    if height[j] > right_high:
                        right_high = height[j]
                    continue

        return total

print(calculate_trapped_rain_water([5, 1, 3, 1, 4]))