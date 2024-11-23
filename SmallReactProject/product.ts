// Task 4: TypeScript Product Interface and Function for Returns the total price of all products
interface Product {
name: string;
price: number;
}

function calculateTotalPrice(products: Product[]): number {
return products.reduce((total, product) => total + product.price, 0);
}
// Example:
const products: Product[] = [
{ name: "Laptop", price: 1000 },
{ name: "Phone", price: 500 },
{ name: "Tablet", price: 300 },
];
console.log("Total Price:", calculateTotalPrice(products));

// Task 5:function for Email validation 
function isValidEmail(email: string): boolean {
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
return emailRegex.test(email);
}
// Example:
const testEmail = "example@domain.com";
console.log("Is valid email:", isValidEmail(testEmail));

// To compile this TypeScript code, run: tsc product.ts
// It will generate a product.js file which can be run in Node.js or a browser
