class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        StringBuilder sb = new StringBuilder();
        sb.append(s);
        String rev = sb.reverse().toString();
        if(rev.equals(s)){
            return true;
        }
        else{
            return false;
        }
    }
}
