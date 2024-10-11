class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1=sentence1.split() #Smaller sentence
        s2=sentence2.split()
        if(len(s2)<len(s1)):
            s1,s2=s2,s1
        i,j=0,0
        while (i<len(s1)) and s1[i]==s2[i]:
            i+=1
        while (j<len(s1)) and s1[-(j+1)]==s2[-(j+1)]:
            j+=1
        return i+j>=len(s1)