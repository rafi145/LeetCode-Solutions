/*Problem Description:
Given two sorted arrays nums1 and nums2, merge them into a single sorted array.
The merged result should be stored in the array nums1.
Approach:
We use a two-pointer technique, starting from the end of both arrays,
and place the bigger at the end of nums1*/

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1; // Index of last element in nums1
    int j = n - 1; // Index of last element in nums2
    int k = nums1Size - 1; // Index of last position in merged array
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k] = nums1[i];
            i--;
        }
        else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }
}
