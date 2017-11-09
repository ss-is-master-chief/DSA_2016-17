d = 256 # number of characters in input alphabet
def search(pattern,text,prime):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for text
    h = 1
 
    for i in range(M-1):
        h = (h*d) % prime
 
    for i in range(M):
        p = (d*p + ord(pattern[i])) % prime
        t = (d*t + ord(text[i])) % prime
 
    for i in range(N-M+1):
        '''Check the hash values of current window of text and
           pattern if the hash values match then only check
           for characters on by one '''
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            j+=1
            if j==M:
                print("Pattern found at index " + str(i))
                
        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % prime
            # negative values of t converted into positive
            if t < 0:
                t = t+prime
 
text = "MACADDAKUSAMURAI" # text from which we find the pattern
pattern = "AKU" # pattern we wish to find
prime = 101 # A prime number
search(pattern,text,prime)
 

