class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int i = 0;
        int len = operations.length;
        for(int j=0; j<len; j++){
            switch(operations[j]){
                case "--X":
                    i = i-1;
                    break;
                case "X--":
                    i = i-1;
                    break;
                case "++X":
                    i = i+1;
                    break;
                case "X++":
                    i = i+1;
                    break;
            }
        }
        return i;
    }
}
