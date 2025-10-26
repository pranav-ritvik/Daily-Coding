class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> para = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(' || ch == '[' || ch == '{') {
                para.add(ch);
            } 
            else {
                if (para.isEmpty()) {
                    return false;
                }

                char top = para.get(para.size() - 1);

                if ((ch == ')' && top == '(') ||
                    (ch == ']' && top == '[') ||
                    (ch == '}' && top == '{')) {
                    para.remove(para.size() - 1);
                } else {
                    return false;
                }
            }
        }

        return para.isEmpty();
    }
}
