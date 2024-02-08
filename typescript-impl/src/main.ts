// run hello world within this fil
export function hello(who: string = 'world'): string {
     return `Hello ${who}! `;
}

// run the hello function
console.log(hello('world'));