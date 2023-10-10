import matrices as m

def fibonacci(N):
  A = [[0,1],[1,1]]
  B = A
  Answer = [0,1]

  for i in range(1,N):
    B = m.matrix_multiplier(A,B)
    Answer.append(B[0][1])
  return Answer
    


What = fibonacci(1000)

print(What)