from PowerLiftingApp1.WLProgramData import*
from liftTestFile import*

L1()


#Two day projection based on passing or failing to meet the first day's lifts
print("Squat " +str(squat_work))
pass_fail = (input("Y/N "))
if pass_fail== "Y":
    print("Next Time "+ str(squat_pass))
elif pass_fail== "N":
    print("Next Time "+ str(squat_fail))


print(benchpress_work)
pass_fail = (input("Y/N "))
if pass_fail== "Y":
    print(benchpress_pass)
elif pass_fail== "N":
    print(benchpress_fail)


print(deadlift_work)
pass_fail = (input("Y/N "))
if pass_fail == "Y":
        print(deadlift_pass)
elif pass_fail == "N":
        print(deadlift_fail)


print(ohp_work)
pass_fail = (input("Y/N "))
if pass_fail == "Y":
    print(ohp_pass)
elif pass_fail == "N":
    print(ohp_fail)


print(pullup_work)
pass_fail = (input("Y/N "))
if pass_fail== "Y":
    print(pullup_pass)
elif pass_fail== "N":
    print(pullup_fail)


print(barbellrow_work)
pass_fail = (input("Y/N "))
if pass_fail== "Y":
    print(barbellrow_pass)
elif pass_fail== "N":
    print(barbellrow_fail)