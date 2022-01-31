package multiply;
import java.util.Scanner;
public class mult {
	public static void main(String[] args) 
	{
		Scanner scan=new Scanner(System.in);
		System.out.println("Enter value for A:");
		int a=scan.nextInt();
		System.out.println("Enter value for B:");
		int b=scan.nextInt();
		int mul=a*b;
		System.out.println("The Multiplication of A and B is..:"+mul);
	}
}
