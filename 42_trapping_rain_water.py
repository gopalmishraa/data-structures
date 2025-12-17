from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # 1. Fill left_max array (Prefix Max)
    # left_max[i] contains the tallest bar from the start (0) up to i
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
        
    # 2. Fill right_max array (Suffix Max)
    # right_max[i] contains the tallest bar from the end (n-1) down to i
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
        
    # 3. Calculate total accumulated water
    total_water = 0
    for i in range(n):
        # Water at current index is limited by the shorter of the two tallest neighbors
        water_level = min(left_max[i], right_max[i])
        
        # Trapped water is the water level minus the ground height at i
        # (If water_level <= height[i], the result is 0, which is correct)
        total_water += water_level - height[i]
        
    return total_water

# --- Execution Block ---
if __name__ == "__main__":
    # Example 1: Standard LeetCode Test Case
    input_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result_1 = trap(input_1)
    print(f"Input: {input_1}")
    print(f"Trapped Water: {result_1}")  # Expected: 6
    print("-" * 30)

    # Example 2: Another Common Test Case
    input_2 = [4, 2, 0, 3, 2, 5]
    result_2 = trap(input_2)
    print(f"Input: {input_2}")
    print(f"Trapped Water: {result_2}")  # Expected: 9
