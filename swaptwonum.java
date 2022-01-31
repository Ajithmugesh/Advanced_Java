package swapping;

public class swaptwonum {
	public static void main(String[] args) {
		int a = 96, b = 11;
		System.out.println("--Before swap--");
		System.out.println("First number = " + a);
		System.out.println("Second number = " + b);
		int temporary = a;
		a = b;
		b = temporary;
		System.out.println("--After swap--");
		System.out.println("First number = " + a);
		System.out.println("Second number = " + b);
		}

}
