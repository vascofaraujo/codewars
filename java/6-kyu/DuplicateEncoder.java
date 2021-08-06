import java.util.HashMap;

public class DuplicateEncoder {
	static String encode(String word){
		HashMap<Character, Integer> numberOfChar = new HashMap<Character, Integer>();

		for(int i = 0; i < word.length(); i++){
			char c = Character.toLowerCase(word.charAt(i));

			if (numberOfChar.containsKey(c)){
				int num = numberOfChar.get(c) + 1;
				numberOfChar.put(c, num);
			}else{
				numberOfChar.put(c,1);
			}

		}

		char[] str_out = new char[word.length()];
		for(int i = 0; i < word.length(); i++){
			char c = Character.toLowerCase(word.charAt(i));

			if (numberOfChar.get(c) > 1){
				str_out[i] = ')';
			}else{
				str_out[i] = '(';
			}
		}

		String out = new String(str_out);

		return out;
	}

	public static void main(String[] args) {
		System.out.println(encode("Prespecialized"));
	}
}
