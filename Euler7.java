package Euler;

public class Euler7
{

    /**
     * @param args
     */
    public static void main(String[] args)
    {
	
		

	int count =0;
	int number =0;
	while (count!=10001){
		number = number+1;
		if (isPrime(number)){
		    count= count+1;
		    System.out.println(count+","+number);
		}		
			
			
	}
	System.out.println(number);

		
		

    }

    public static boolean isPrime(int n)
    {
	if (n <= 1)
	    return false;
	if (n == 2)
	    return true;
	if (n % 2 == 0)
	    return false;

	int m = (int) Math.sqrt(n);
	for (int i = 3; i <= m; i++)
	    if (n % i == 0)
		return false;
	return true;
    }
}
