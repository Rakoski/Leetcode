function maximumSubarrays(array: number[], k: number) {
    let maxSum = 0;
    let currentSum = 0;
    for (let i = 0; i < k; i++) {
        maxSum += array[i];
    }
    currentSum = maxSum;

    for (let i = k; i < array.length; i++) {
        currentSum = currentSum - array[i - k] + array[i];
        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
}

console.log(maximumSubarrays([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))