
def PERCEPTRON_AND(x1, x2):
    w1 , w2 , b = 1, 1, -1.5
    linear_combination = w1 * x1 + w2 * x2 + b
    return 1 if linear_combination >=0 else 0


inputs = [(0,0), (0,1), (1,0), (1,1)]

for x in inputs:
    print(x, " -> " , PERCEPTRON_AND(x[0], x[1]))