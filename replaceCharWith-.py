def replaceChar(str,k):
    c={}
    for i in range(len(str)):
        if str[i] in c:
            if i-c[str[i]]<=k:
                c.update({str[i]: i})
                str=str[:i]+'-'+str[i+1:]

        else:
            c.update({str[i]:i})
    return str
if __name__ == '__main__':
    print(replaceChar("abcdefaxcqwertba",10))