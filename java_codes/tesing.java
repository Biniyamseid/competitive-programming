import java.util.*;
import java.io.*;
import java.math.*;
import java.lang.Integer;
import java.util.ArrayList;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class tesing {


    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        ArrayList<Integer> number = new ArrayList<Integer>(); // Create an ArrayList object
        
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
        int X = in.nextInt();
        int num = X;
        String strNum = Integer.toString(num);
        int counter = 0;
        public int flag = 0;
        for (int k=strNum.length()-1; k >= 0 ; k--) {
            System.out.println(strNum.charAt(k));
            String num1 = strNum.charAt(k);
            if (Integer.valueOf(num1)>count){
                count = count + Integer.valueOf(num1);
                continue;
            }
            else{
            flag = 1;
            }

        }
        number.add(X);




        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");
        int max = 0;
        for(int values:number){
            if (values > max){
                max = values;
            }
            
        }
        if (flag == 1){
            System.out.println("NONE");
        }
        else{
        System.out.println(max);
        }
    }
}