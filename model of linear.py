ws = [1, 3, 2, -1]
vectors = [10, -1, 14, 20, 10, 4]
tests = [15, 77]
results = []

def linear_regression_solution(ws, vectors):
    e = ws[0] + ws[1] * vectors[0] + ws[2] * vectors[1] + ws[3] * vectors[2]
    d = ws[0] + ws[1] * vectors[3] + ws[2] * vectors[4] + ws[3] * vectors[5]
    results.append(e)
    results.append(d)
    
linear_regression_solution(ws, vectors)
if  results == tests:
    print('All tests are complete!')
else:
    print('ERROR')
