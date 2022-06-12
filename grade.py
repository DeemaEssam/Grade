# variables
eighty = 80
zero = 0
fifty = 50
twenty_5 = 25
sixty = 60
# enter and validate test scores
test_1 = float(input("Enter your Test 1 score : "))
while zero > test_1 or test_1 > twenty_5:
    print("grade should be between 0 and 25")
    test_1 = float(input("Enter your Test 1 score : "))
test_2 = float(input("Enter your Test 2 score : "))
while zero > test_2 or test_2 > twenty_5:
    print("grade should be between 0 and 25")
    test_2 = float(input("Enter your Test 2 score : "))
exam = float(input("Enter your Exam score : "))
while zero > exam or exam > fifty:
    print("grade should be between 0 and 50")
    exam = float(input("Enter your Exam score : "))
# float to int
int(test_1)
int(test_2)
int(exam)
# variables
total = test_1 + test_2 + exam
grade = (total >= fifty)
Grade = (exam >= twenty_5)
# if conditions
if grade and Grade:
    print("passed")
    if eighty > total > sixty:
        print("Credit")
    elif total < sixty:
        print("grade less than 60")
    elif total > eighty:
        print("Distinction")
else:
    print("Failed")