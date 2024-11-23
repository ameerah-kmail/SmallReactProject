function calculateTotalPrice(products) {
    return products.reduce(function (total, product) { return total + product.price; }, 0);
}
var products = [
    { name: "Laptop", price: 1000 },
    { name: "Phone", price: 500 },
    { name: "Tablet", price: 300 },
];
var totalPrice = calculateTotalPrice(products);
console.log("Total Price:", totalPrice);
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
var testEmail = "example@domain.com";
console.log("Is valid email:", isValidEmail(testEmail));
