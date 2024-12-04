// https://leetcode.com/problems/create-hello-world-function/description/

function createHelloWorld() {
  return function (...args): string {
    return "Hello World";
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
