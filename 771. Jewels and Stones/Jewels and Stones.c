// Approach:Make array of counter size 52 for each letter in a-b and the
// uppercase
//          size of counter equal 20 , and another count for jewels in counter
//          ,the use of ascii code is needed.
//          if a-z ascii-97  counter[0..25] represent lowercase.
//          else if A-Z ascii-39 counter[26..51] represent upprcase.

int numJewelsInStones(char* jewels, char* stones) {
    int count = 0; // Count the number of stones that are jewels
    int counter[52] = {
        0 }; // Counter represent the letter in a-b lowercase and uppercase.
    for (int i = 0; i < strlen(stones); i++) {
        int temp = (int)stones[i];
        if (temp >= 97 && temp <= 122)
            counter[temp - 97]++;
        else if (temp >= 65 && temp <= 90)
            counter[temp - 39]++;
        else
            printf("ERROR!");
    }
    for (int j = 0; j < strlen(jewels); j++) {
        int temp = (int)jewels[j];
        if (jewels[j] >= 'a' && jewels[j] <= 'z')
            count += counter[temp - 97];
        else if (jewels[j] >= 'A' && jewels[j] <= 'Z')
            count += counter[temp - 39];
        else
            printf("ERROR!");
    }
    return count;
}