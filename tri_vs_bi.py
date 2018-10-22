from no_signalling import no_signalling
from inequalities import *
import sys
import pickle
# For plotting triparty inequality vs biparty 

def __main__():
  step = 0.001 # incremental steps for the constraint
  lim = 0.501 # upper limit for the constraint
  conv = 1 # division for the objective
  x = []
  y = []
  dx = 0 # initialization of the constraint
  while dx <= lim:

    P = no_signalling()
    # enter objective function
    P.create_objective(P.change_sign((chsh_game_AB(),0)))

    # add constraints
    temp = IP()
    P.add_inequality((temp,dx))
    P.add_inequality(P.change_sign((temp,dx)))


    solutions = P.linear_prog()

    if not solutions :
      print "Infeasible solution found for variable ( exiting )", dx
      break

    result = P.print_sol(solutions)/conv * -1
#    print result , " for dx = " , dx
#    P.print_tabs(solutions)
#    P.print_ineq()

    x.append(dx)
    y.append(result)

    dx = dx + step
  with open('../PlottingMatplotlib/data/chshvsINS.plot','wb') as fp:
    pickle.dump([x,y],fp)  
if __name__=="__main__":
  __main__()


