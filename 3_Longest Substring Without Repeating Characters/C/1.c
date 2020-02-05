/* brutal search 
   In the beginning, malloc a string to record checked substring : Runtime:320 ms	Memory : 23.2 MB
   According to other's solution : use a position as an end, check the previous chars to see if repeated char existed  
*/

int lengthOfLongestSubstring(char * s){

    //int lenn = strlen(s);
    
    int max_len = 1;
    //int max_len = 0;
    //int i,j,k,sub_len;
    
    int j_start = 0;
    int cur_len = 1;
    
    if(!s[0])
        return 0;
    if(!s[1])
        return 1;
    
    for(int i = 1 ; s[i] ; i++)
    {
        for(int j = j_start ; j < i ; j++)
        {
            if(s[j] != s[i])
                cur_len++;
            else
                j_start = j + 1;
        }
        /*
    for(i =0 ; i < lenn ; i++)
        j = i + 1;
        char *sub = calloc(100, sizeof(char));
        sub[0] = s[i];
        sub[1] = '\0';
        int cur_len = 1;
        while(j < lenn)
        {
            sub_len = strlen(sub); 
            for(k = 0 ; k < sub_len ; k++)
            {
                if(sub[k] == s[j])   
                    break;
            }
            if(k < sub_len)
                break;
            else
            {
                sub[sub_len] = s[j] ; 
                sub[sub_len + 1] = '\0';
                cur_len++;
                j++;
            }
                
        }
        */
        if(cur_len > max_len) 
            max_len = cur_len;
        cur_len = 1;
            
    }
    
    return max_len;
}

