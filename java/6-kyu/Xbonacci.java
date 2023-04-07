public class Xbonacci {

    public static double[] tribonacci(double[] s, int n) {
        double[] out = new double[n];
        if(n==0)
            return out;
        for(int i = 0; i < n; i++){
            if (i < 3)
                out[i] = s[i];
            else
                out[i] = out[i-1] + out[i-2] + out[i-3];
        }

        return out;
    }

    public static void main(String[] args) {
        double[] a = new double[]{1,1,1};
        System.out.println(tribonacci(a,10));

    }
}
