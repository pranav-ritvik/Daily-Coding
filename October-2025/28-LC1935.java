class Solution {
    public int canBeTypedWords(String text, String bro) {
        HashMap<Character,Integer> broken = new HashMap<>();
        for(int i=0; i<bro.length(); i++){
            broken.put(bro.charAt(i),1);
        }
        String[] words = text.split(" ");
        int total = words.length;
        for(String word : words){
            for(int j=0; j<word.length(); j++){
                char ch = word.charAt(j);
                if(broken.containsKey(ch)){
                    total = total - 1;
                    break;
                }
            }
        }
        return total;
    }
}
