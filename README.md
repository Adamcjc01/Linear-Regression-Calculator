# Linear-Regression-Calculator
## A python code to estimate the b0 and b1 co-efficients of a linear regression using least squares.

The aim is to create a linear regression  model from first principles and only using the in-built packages in Python 3.7.

A linear regression equation can be defined as:

> h(xi) = b0 + b1 * xi

where:

> h(xi) is the **predicted response value**

> b0 is the **y-intercept** of the line 

> b1 is the **slope** of the line

In order to find the coefficients b0 and b1 that have the best fit we need to minimise the residual error. This is done using the **Least Squares Technique**. 

The residual error (ei) can be defined as:

> ei = yi - h(xi)

> yi is the **actual value** of y for a given x

For example, if the predicted response value h(xi) is equal to the actual value of yi then the ouput of the equation is 0. This would mean our regression line fits perfectly. This is the hypothetical that we are aiming for, in reality we will usually have some error but we want the **lowest possible residual error**. 

We can define a **cost function** which has the lowest possible values for the residual error. This can be defined as:

> J(b0,b1) = 1/2n * sum (ei^2)

substituting ei with the equation above gives us:

> J(b0,b1) = 1/2n * sum ((yi - h(xi))^2)

From here there is a fairly long process of algebraic manipulation to get to an equation for the estimated least squares error b0 and b1. (the full form of which can be found [here](https://www.amherst.edu/system/files/media/1287/SLR_Leastsquares.pdf)). Those two equations are:

> b1 = sum(yi * xi - n * m_x * m_x) / sum(xi^2 - n * (m_x)^2)

> b0 = m_y - b1 * m_x

> n is **number of observations** in the data

> xi and yi are **ith values** of a vector x and y respectively

> m_x and m_y are the **mean values** of vector x and y respectively

This is the output of the function *calculate_linear_coefficients* in the code. It only uses the in-built statistics package. note: the function can be done quicker with Numpy arrays.

The *main* function creates x and y vectors to test the function with. It also generates a plot to show that the function works correctly.




