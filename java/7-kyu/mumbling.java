public class mumbling{
    public static String accum(String s){
        String out = "";
        for(int i=0; i < s.length(); i++){

            String aux = "" + Character.toUpperCase(s.charAt(i));

            for(int j = 1; j <= i; j++) {
                aux += Character.toLowerCase(s.charAt(i));
            }

            out = out + aux + "-";
      }
     return out.substring(0, out.length() - 1);
     
    }



    public static void main(String[] args) {
        System.out.println(accum("ZpglnRxqenU"));
    }

}
