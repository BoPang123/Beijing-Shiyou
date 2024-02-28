import sys


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
    str = sys.argv[1]
    k = sys.argv[2]
    print(replaceChar("abcdefaxcqwertba",10))
    # print(replaceChar("abcdefaxcqwertba",10))