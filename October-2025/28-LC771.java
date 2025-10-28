class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < stones.length(); i++) {
            char ch = stones.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        int fin = 0;
        for (int j = 0; j < jewels.length(); j++) {
            char c = jewels.charAt(j);
            if (map.containsKey(c)) {
                fin += map.get(c);
            }
        }

        return fin;
    }
}
