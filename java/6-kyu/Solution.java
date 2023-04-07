public class Solution
{
    public static int[] twoSum(int[] numbers, int target)
    {
        for(int i=0; i < numbers.length; i++){
            int num = numbers[i];

            for(int j=0; j < numbers.length; j++){
                if ( j != i){
                    int attempt = numbers[i] + numbers[j];
                    if (attempt == target){
                        return (new int[]{i, j});
                    }
                }
            }

        }
        return null;
    }


    public static void main(String[] args) {
        System.out.println(twoSum(new int[]{1, 2, 3}, 4));
    }
}
