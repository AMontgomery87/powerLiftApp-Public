from math import*

squat_max = float(input("Squat Max: "))
deadlift_max = float(input("Deadlift Max: "))
benchpress_max = float(input("Bench Press Max: "))
ohp_max = float(input("Overhead Press Max: "))
pullup_max = float(input("Maximum number of bodyweight pullups: "))
barbellrow_Max = float(input("Barbell row max: "))

squat_work = floor(squat_max * 0.80)
deadlift_work = floor(deadlift_max * 0.80)
benchpress_work = floor(benchpress_max * 0.80)
ohp_work = floor(ohp_max * 0.80)
pullup_work = floor(pullup_max * 0.80)
barbellrow_work = floor(barbellrow_Max * 0.80)

squat_pass = floor(squat_work + 5.00)
deadlift_pass = floor(deadlift_work + 5.00)
benchpress_pass = floor(benchpress_work + 5.00)
ohp_pass = floor(ohp_work + 5.00)
pullup_pass = floor(pullup_work + 5.00)
barbellrow_pass = floor(barbellrow_work + 5.00)

squat_fail = floor(squat_work - 5.00)
deadlift_fail = floor(deadlift_work - 5.00)
benchpress_fail = floor(benchpress_work - 5.00)
ohp_fail = floor(ohp_work - 5.00)
pullup_fail = floor(pullup_work - 5.00)
barbellrow_fail = floor(barbellrow_work - 5.00)

failure_count = 0
failure_swap = 3
swap_program = False


