class Solution {
    public List<List<Integer>> groupThePeople(int[] grpSize) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        List<List<Integer>> result = new ArrayList<>();
        for(int i=0; i<grpSize.length; i++){
            int num = grpSize[i];
            if(map.containsKey(num)){
                map.get(num).add(i);
            }else{
                map.put(num,new ArrayList<Integer>());
                map.get(num).add(i);
            }

            if(map.get(num).size()== num){
                result.add(new ArrayList<>(map.get(num)));
                map.get(num).clear();
            }
        }
        return result;
    }
}
