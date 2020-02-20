import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class InitializerBlock extends Exception {
    // https://www.hackerrank.com/challenges/java-static-initializer-block/problem?h_r=next-challenge&h_v=zen

    protected static Scanner sc = new Scanner(System.in);
    protected static int B = sc.nextInt();
    protected static int H = sc.nextInt();
    protected static boolean flag = true;

    static {
        try {
            if (B <= 0 || H <= 0) {
                flag = false;
                throw new Exception("Breadth and height must be positive");
            }
        } catch(Exception e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) throws Exception {

        if (flag) {
            int area = B * H;
            System.out.print(area);
        }

    }//end of main

}//end of class