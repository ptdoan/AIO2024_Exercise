#*************Exercise5 ***********
def md_nre_single_sample(y,y_hat,n,p):
  y_root = y**(1/n)
  y_hat_root = y_hat**(1/n)
  difference = y_root - y_hat_root
  loss = difference**p
  return loss

# Check the Result of Excercise 5
print(md_nre_single_sample (100 , 99.5 , 2, 1))