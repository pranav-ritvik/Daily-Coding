class Solution {
    public int maxDepth(String s) {
        ArrayList<Character> arr = new ArrayList<>();
        int max = 0;
        for(int i =0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '('){
                arr.add(ch);
                if(arr.size() > max){
                    max = arr.size();
                }
            }else if(ch == ')'){
                arr.remove(arr.size()-1);
            }
        }
        return max;
    }
}
