//Task 2: function calculates the total sum and the average of the numbers using the reduce method
function calculateSumAndAverage(numbers) {
const total = numbers.reduce((sum, num) => sum + num, 0);
const average = total / numbers.length;
return { total, average };
}
// Example:
const numbers = [10, 20, 30, 40, 50];
const { total, average } = calculateSumAndAverage(numbers);
console.log("Total Sum:", total, "Average:", average);

//Task 3: function removes duplicates from the array in constant time complexity and returns the array with unique values
function removeDuplicates(array) {
    const uniqueSet = new Set(array);
    return Array.from(uniqueSet);
}
// Example:
const strings = ["apple", "banana", "apple", "orange", "banana"];
const uniqueStrings = removeDuplicates(strings);
console.log("Unique Strings:", uniqueStrings);
