public class BackspacesInString {
	public String cleanString(String s) {	
  
		char[] result = new char[s.length()]; 	
		int n = 0;
		int n_final = 0;
		for (int i = 0; i < s.length(); i++) {
        		if (String.valueOf(s.charAt(i)).equals("#")) {
				n = n-1;
				try{	
					result[n] = ' ';
				}catch (Exception e) {
					n = 0;
				}
				n_final = n_final - 1;
			}else{
				result[n] = (s.charAt(i));
				n = n+1;
				n_final = n_final + 1;
			}
			if (n_final < 0) {
				n_final = 0;
			}
		}
		String result_string= new String(result);
		return result_string.substring(0, n_final);
	}

   	public static void main(String[] args) {
	  	BackspacesInString b = new BackspacesInString();
        	System.out.println(b.cleanString("abc#d##c").equals("ac"));
        	System.out.println(b.cleanString("v###EBf#Qs#DRs#").equals("EBQDR"));
    	}
}
