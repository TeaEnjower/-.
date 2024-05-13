def min_time_to_fry_cutlets(k, m, n):
    time_per_side = 2 * m
    batches_needed = (n + k - 1) // k
    total_time = batches_needed * time_per_side
    return total_time

# Input values for k, m, and n
k = int(input("Enter the number of cutlets that can fit on the pan at once (k): "))
m = int(input("Enter the time needed to fry each side of a cutlet (m): "))
n = int(input("Enter the total number of cutlets to fry (n): "))

# Calculate and output the minimum amount of time needed
print("Minimum amount of time needed to fry all cutlets: ", min_time_to_fry_cutlets(k, m, n))