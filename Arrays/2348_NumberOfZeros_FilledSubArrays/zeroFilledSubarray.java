public class zeroFilledSubarray {
    public long ZeroFilledSubarray(int[] nums) {
        long count = 0;
        int result = 0;

        for (int num : nums) {
            if (num == 0) {
                count++;
                
            } else {
                count = 0;
            }
            result += count;
        }

        return result;
    }
}



