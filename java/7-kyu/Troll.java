public class Troll {
    public static String disemvowel(String str) {
        String vowels = "aeiou";

        char[] str_out = new char[str.length()];
        int num_vowels = 0;
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            char charC = Character.toLowerCase(c);
            if (!(vowels.contains(Character.toString(charC)))){
                str_out[num_vowels] = c;
                num_vowels++;
            }
        }

        String out = new String(str_out);
        out = out.substring(0, num_vowels);

        return out;
    }

    public static void main(String[] args) {

        System.out.println(Troll.disemvowel("This website is for losers LOL!"));
    }
}
