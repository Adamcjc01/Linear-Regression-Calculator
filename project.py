import statistics 
import matplotlib.pyplot as plt 

def calculate_linear_coefficients(x,y):
	#Calculate the linear regression coefs using
	#the ordinary least squares method
	#the output coefficients are b_0 and b_1

	#number of observations
	n_x = len(x)

	#calulate mean of each vector
	mean_x, mean_y = statistics.mean(x), statistics.mean(y)

	#calculate yi*xi and xi*xi
	x_y = [x_i * y_i for x_i, y_i in zip(x, y)]
	x_x = [x_i_1 * x_i_2 for x_i_1, x_i_2 in zip(x, x)]

	#calculate cross-deviation (xy) and deviation (xx)
	ss_xy = sum(x_y) - n_x*mean_x*mean_y
	ss_xx = sum(x_x) - n_x*mean_x*mean_x

	#calculate the regression coefficients
	b_1 = ss_xy / ss_xx
	b_0 = mean_y - b_1 * mean_x 

	return b_0, b_1

def plot_regression_line(x, y, b_0, b_1): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = [b_0 + b_1*x_i for x_i in x]
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 

def main(): 
    # observations 
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [32, 35, 27, 21, 15, 10, 12, 6, 3, -1]
  
    # estimating coefficients 
    b_0,b_1 = calculate_coefficients(x, y) 
    print(f"Coefficients of the Regression:\nb0 == {b_0}\nb1 == {b_1}")
  
    # plotting regression line 
    plot_regression_line(x, y, b_0, b_1) 
  
if __name__ == "__main__": 
    main() 


