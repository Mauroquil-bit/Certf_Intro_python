// ¿Qué es Javascript Promise, async/await MicroTask queue?
// https://www.youtube.com/watch?v=QO4NXhWo_NM

// ¿Qué es Javascript Promise, async/await MicroTask queue?


const foo = () => console.log("First");
const bar = () => setTimeout(() => console.log("Second"), 500);
const baz = () => console.log("Third");

bar();
foo();
baz();

// First
// Third
// Second

// ¿Qué es Javascript Promise, async/await MicroTask queue?

const foo = () => console.log("First");
const bar = () => setTimeout(() => console.log("Second"), 0);
const baz = () => console.log("Third");

bar();
foo();
baz();

// First
// Third
// Second

// ¿Qué es Javascript Promise, async/await ?

const foo = () => console.log("First");
const bar = () => new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("Second");
        resolve();
    }, 0);
}

);
const baz = () => console.log("Third");

bar().then(foo).then(baz);

// Second
// First
// Third

// ¿Qué es Javascript Promise, async/await ?

