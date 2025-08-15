result=""
        if(strs!=None and len(strs)>1):
            for i in range(0,len(strs[0])):
                is_equal=True
                for j in range(1,len(strs)):
                    if((len(strs[j]))<=i or strs[0][i]!=strs[j][i]):
                        is_equal=False
                        break
                if(is_equal):
                    result=result+strs[0][i]
                else:
                    break
        elif (strs!=None):
            result=strs[0]
        else:
            result=None
        return result
        
