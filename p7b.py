def FA(s):
    # if the length is less than 3, then it can't be accepted. Therefore, end the process.
    if len(s) < 3:
        return "Rejected"
    
    # First three characters are fixed. Therefore, checking them using index
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                # Continue checking for characters beyond the first three
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"
    
    return "Rejected"

# Test cases
inputs = ['1', '10101', '101', '10111', '01010', ""]
for i in inputs:
    print(FA(i))
