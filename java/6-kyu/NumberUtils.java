import java.lang.Math;
public class NumberUtils {

    public static boolean isNarcissistic(int number) {

        String string_number = Integer.toString(number);
        double digits_num = string_number.length();
        int n = 0;

        for (int i = 0; i < digits_num; i++) {
            double a = (double)Integer.parseInt(String.valueOf(string_number.charAt(i)));

            Double power = Math.pow(a, digits_num);
            n = n + power.intValue();
        }
        return number == n;
    }

      public static void main(String[] args) {
        System.out.println(isNarcissistic(1634));
    }
    
}