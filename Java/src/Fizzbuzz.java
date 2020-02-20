import java.util.Scanner;

public class Fizzbuzz {

    public static String fizzbuzzin(int num) {
        if (num % 15 == 0) {
            return num + " FizzBuzz";
        } else if (num % 5 == 0) {
            return num + " Fizz";
        } else if (num % 3 == 0) {
            return num + " Buzz";
        } else {
            return String.valueOf(num);
        }
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("Enter the amount of number to fizzBuzz!:");
        int n = in.nextInt();

        while (n > 0) {
            System.out.println(fizzbuzzin(n));
            n--;
        }
    }

}
