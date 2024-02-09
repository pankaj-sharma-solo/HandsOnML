def calculate_water_volume(heights):
    n = len(heights)
    if n <= 2:
        return 0  # Not enough bars to hold water

    left_max = [0] * n
    right_max = [0] * n
    water_volume = 0

    # Compute the left maximum for each bar
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Compute the right maximum for each bar
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate the water volume for each bar
    for i in range(n):
        water_volume += min(left_max[i], right_max[i]) - heights[i]

    return water_volume

# Example usage:
histogram = [2,1,0,1,4,1,0,1]
volume = calculate_water_volume(histogram)
print("Volume of water stored in the histogram is:", volume)