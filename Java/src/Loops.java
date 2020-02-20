import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class Loops {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        int i = 10;
        int count = 1;
        while (i != 0) {
            System.out.println(N + " x " + count + " = " + (N * count));
            count++;
            i--;
        }

    }


}
