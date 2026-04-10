question_1 = input("What is the Riemann Zeta function value at Re=1/2? ")

question_2 = input("What is the volume formula for a ball in N dimensions? ")

question_3 = input("What is our approx. position on the Earth at this moment?")

question_4 = input("What color will ChromoClock generate on this date and time? ")

question_5 = input("What is the permittivity of free space?")

question_6 = input("Will it be sunny on Sunday?")

question_7 = input("What was the first thing I said in my existence?")

question_8 = (input("Solve this equation: y^3 = 2(6) - (root x) + 7      Ans= "))

question_9 = input("Is this the penultimate question of this quiz? ")

question_10 = input("How do you take the logarithm of a photo? ")


answer_1 = "Unknown"
answer_2 = "[(pi^(n/2)) / (gamma(n/2+1))] * (r)^n"
answer_3 = "45.2 N 93.6 W"
answer_4 = "Yellow-green"
answer_5 = "8.85418782 x 10-12 m^-3 kg^-1 s^4 A^2"
answer_6 = "Depends"
answer_7 = "---"
answer_8 = "Y = 2.5484"
answer_9 = "Yes"
answer_10 = "There are 3 steps. First, you take the photo and put it on a coordinate grid. Next, you apply a natural logarithm. Then, you find the right value of j such that the picture becomes endlessly rotationally self similar. This only works for photos which were self-similar in the first place."


def tally_score():
    if question_1 == answer_1:
        print("Correct")
    if question_2 == answer_2:
        print("Correct")
    if  question_3 == answer_3:
        print("Correct")
    if question_4 == answer_4:
        print("Correct")
    if question_5 == answer_5:
        print("Correct")
    if question_6 == answer_6:
        print("Correct")
    if question_7 == answer_7:
        print("Correct")
    if question_8 == answer_8:
        print("Correct")
    if question_9 == answer_9:
        print("Correct")
    if question_10 == answer_10:
        print("Correct")
    
tally_score()
