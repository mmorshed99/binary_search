#Implement int sqrt(int x).
#
#Compute and return the square root of x.
#
#If x is not a perfect square, return floor(sqrt(x))
#
#Example :
#
#Input : 11
#Output : 3
#
#
double find_val(int A, double G){
    double H = A / G;
    double new_val = (G+H)/2;
    return new_val;
}

int sq_rt(int A){
    if (A == 1)   {
        return 1;  }
    if (A ==0)    {
        return 0;  }
    double i = 1.0;
    double diff = A;
    int num = 0;
    while(1) {   
      if (std::abs(i*i -A)< diff){
                num = i;
                diff = std::abs(i*i -A);
                i++;
                                }
      else {
                i--;
                break;
           }
              }
    double new_val = i;
    while(1){
        new_val	= find_val(A,new_val);
        if (std::abs(new_val * new_val - A ) <= 0.1) {
            break;
                                                     }
            }
    new_val = floor(new_val);
    return (int) new_val;
}
int Solution::sqrt(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    return sq_rt(A);
}
