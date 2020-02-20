import java.io.IOException;
import java.util.Scanner;

public class EndOfFile {

    public static void main(String[] args) {

        int count = 1;

        Scanner sc = new Scanner(System.in);
        String cc = sc.nextLine();
        boolean hasNextLine = true;

        while (cc != null) {
            System.out.println(count + " " + cc);
            count++;
            hasNextLine = sc.hasNextLine();
            if (hasNextLine == true) {
                cc = sc.nextLine();
            } else {
                cc = null;
            }
        }

    }

}
