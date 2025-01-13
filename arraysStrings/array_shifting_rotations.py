# 🌟 Arrays in Python: Shifting and Rotating Arrays 🌟

# 🚚 Shifting an Array (Sliding with Zeros)
def shift_array(arr, shift_by, direction="right"):
    """
    🚚 Shifts an array by removing elements from one end 
    and adding zeroes on the opposite end.

    📦 Parameters:
    - arr (list): The input array 📊
    - shift_by (int): Number of positions to shift ➡️
    - direction (str): 'right' or 'left' 🔀

    🎁 Returns:
    - list: Shifted array with zero padding ⭕
    """
    if not arr:  # 🚫 Check for empty array
        return arr

    # 🔢 Normalize shift_by to avoid excessive shifts
    shift_by %= len(arr)

    # ✅ Shifting Logic
    if direction == "right":
        # ➡️ Shift right: Add zeros on the left side
        shifted = [0] * shift_by + arr[:-shift_by]
    elif direction == "left":
        # ⬅️ Shift left: Add zeros on the right side
        shifted = arr[shift_by:] + [0] * shift_by
    else:
        raise ValueError("⚠️ Direction must be 'right' or 'left'")

    return shifted

# 🎬 Example usage:
shifted_arr = shift_array([1, 2, 3, 4, 5], 2, "right")
print("🚚 Shifted Right with Zeros:", shifted_arr)

# 🔄 Rotating an Array (Circular Movement)

def rotate_array(arr, k):
    """
    🔄 Rotates an array to the right by k positions using modulus.

    📦 Parameters:
    - arr (list): The array to rotate
    - k (int): Number of positions to rotate

    🎁 Returns:
    - list: Rotated array
    """
    if not arr:  # 🚫 Handle empty array edge case
        return arr

    # 🔢 Normalize k using modulus to avoid redundant rotations
    k %= len(arr)  # Ensures k is within the array's length range

    # 🎯 Rotate using slicing (split and recombine)
    return arr[-k:] + arr[:-k]

# 🎬 Example usage:
arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array(arr, 7)
print("🔄 Rotated Array:", rotated_arr)  # Output: [4, 5, 1, 2, 3] (Same as rotating 2 times)

# Example usage:
arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array(arr, 2)
print("Rotated Array:", rotated_arr)  # Output: [4, 5, 1, 2, 3]