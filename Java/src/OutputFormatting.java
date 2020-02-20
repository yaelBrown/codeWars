import java.util.Scanner;

class OutputFormatting {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
//            int x=sc.nextInt();
            //Complete this line
            String xStr = sc.next();

            if (xStr.length() == 2 ) {
                xStr = 0 + xStr;
            }

            if (xStr.length() == 1 ) {
                xStr = "00" + xStr;
            }

            if (i != 2) System.out.printf("%-10s %s \n", s1,xStr);
            else System.out.printf("%-10s %s \n", s1,xStr);
        }
        System.out.println("================================");

    }
}