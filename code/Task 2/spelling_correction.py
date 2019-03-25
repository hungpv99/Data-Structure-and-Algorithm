
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 
  

def write_output(text):
    file_output = open('test_output.txt', 'a+')
    file_output.write('\n'+text)
    file_output.close()

def check_eror_and_recommendtation(arr_str):
    file_dict = open('dict_test.txt', 'r')
    arr_str_dict = file_dict.read().split('\n')
    for word_check in arr_str: # Kiểm tra từng từ trong file input
        if word_check not in arr_str_dict: # Kiểm tra xem từ đó có trong từ điển hay không
            msg_out = 'Misspelled words: ' + word_check + '   suggestions for corrections: '
            
            distance = [100,100,100]
            # Kiểm tra edit_distance
            for i in range(len(arr_str_dict)): 
                distance = editDistDP(word_check, arr_str_dict[i], len(word_check), len(arr_str_dict[i]))
            
            #lấy ra 3 từ có edit_distance nhỏ nhất và ghi vào file
            for i in range(3):
                index = distance.index(min(distance))
                msg_out += arr_str_dict[index] + ' '
                distance[index] = max(distance)+1
            write_output(msg_out)
    

if __name__ == "__main__":
    file_input = open('test_input.txt', 'r')
    arr_str = file_input.read().split(' ')
    check_eror_and_recommendtation(arr_str)
    file_input.close()
