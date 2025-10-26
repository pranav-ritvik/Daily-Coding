class Solution {
    public int scoreOfString(String s) {
        int res = 0;
        int len = s.length();
        for(int i = 0; i < (len-1); i++){
            char ch1 = s.charAt(i);
            int v1 = (int)ch1;
            char ch2 = s.charAt(i+1);
            int v2 = (int)ch2;
            int sub = Math.abs(v1 - v2);
            res += sub;
        }
        return res;
    }
}
