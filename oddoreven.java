import java.util.Scanner;
public class oddoreven {
	public static void main(String args[])
	{
	Scanner reader = new Scanner(System.in);
	System.out.println("Enter an Integer number:");
	int num = reader.nextInt();
	if ( num % 2 == 0 )
	System.out.println("Entered number is even");
	else
	System.out.println("Entered number is odd");
	}

}
