class Solution {
    public String mergeAlternately(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        StringBuilder sb = new StringBuilder();
        int i = 0 , j = 0;
        while(i<len1 && j<len2){
            char c = word1.charAt(i);
            char d = word2.charAt(j);
            sb.append(c);
            sb.append(d);
            i++;
            j++;
        }

        while(i<len1){
            char c = word1.charAt(i);
            sb.append(c);
            i++;
        }

        while(j<len2){
            char d = word2.charAt(j);
            sb.append(d);
            j++;
        }

        return sb.toString();
    }
}
