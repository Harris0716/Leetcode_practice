class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        int max_len = prefix.length();
        
        for(int j = 1; j < strs.length; j++){
            if(strs[j].length() < max_len){
                max_len = strs[j].length();
            }
            while(!prefix.substring(0,max_len).equals(strs[j].substring(0,max_len))){
                max_len--;
            }
        }
        return prefix.substring(0, max_len);
    }
}