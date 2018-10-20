from no_signalling import no_signalling
from inequalities import *
import matplotlib.pyplot as plt
import sys
from itertools import cycle
lines = ["-","--","-.",":"]
linecycler = cycle(lines)
# For plotting monogamy relation (chsh_game_AB vs. chsh_game_BC) given svetlichny game value

def __main__():   
  # first the outer look for fixing obejective svetlichny game value
  step = 0.025 # incremental steps for the constraint
  lim = 1.025 # upper limit for the constraint
  conv = 1 # division for the objective
  dx = 0.75 # initialization of the constraint
  x=[]
  while dx <= lim:
    P = no_signalling()
    # enter objective function
    P.create_objective(P.change_sign((chsh_game_AB(),0)))

    # add constraints
    temp = svetlichny_game()
    P.add_inequality((temp,dx))
    P.add_inequality(P.change_sign((temp,dx)))

    # now the inner loop for chsh_game_AB() chsh_game BC() value
    step_y = 0.01 # incremental steps for the constraint
    lim_y = 1.01 # upper limit for the constraint
    dy = 0 # initialization of the constraint
    y = []
    z = []


    while dy <= lim_y:
    # add constraints
      temp_y = chsh_game_BC()
      P.add_inequality((temp,dy))
      P.add_inequality(P.change_sign((temp_y,dy)))

      solutions = P.linear_prog();

      if not solutions :
        print "Infeasible solution found for variable ( exiting )", dx
        break;

      result = P.print_sol(solutions)/conv * -1
      print result , " for dy = " , dy
#        P.print_tabs(solutions)
#        P.print_ineq()

      y.append(dy)
      z.append(result)
        # incerement inner counter
      dy = dy + step_y
      # add to plot
    if dx + step > lim:
      plt.plot(y,z, marker='o',ms=4,mew=4)
    else:
      plt.plot(y,z,linewidth=4,ls=next(linecycler))
  # increment outer counter
    x.append(dx)
    dx=dx + step
  plt.rc('text', usetex=True)
# create list of lengends, awww yeah 
  list_of_labels=['$p_(S_3)=$'+str(i) for i in x]
# display/save the graph 
  plt.xlim(0.5,1.09)
  plt.ylim(0.5,1.09)
  plt.ylabel('$\max_{NS}\{p_{A_1A_3}(S_2)\}$',size=16)
  plt.xlabel('$p_{A_1A_2}(S_2)$',size=16)
  plt.legend((list_of_labels))
  plt.tick_params(axis='x', labelsize=14)
  plt.tick_params(axis='y', labelsize=14)

  plt.grid()
  plt.savefig('../../../graphs/chsh_chsh_sn.pdf',bbox_inches='tight')
  plt.show()


if __name__=="__main__":
  __main__()


