// Recursive solution to the Towers of Hanoi problem.

// Parameters:
// f (str): Starting rod 
// s (str): Spare rod
// t (str): Ending rod
// n (int): Number of disks

// Functionality:
// Moves n disks from rod f to rod t using rod s (disk no. 1 is the topmost disk)
// If n <= 0, returns.
// If n == 1, prints the move from f to t.
// Otherwise:
// - Moves the top n-1 disks from f to s using t.
// - Prints the move from f to t. 
// - Moves all the n-1 disks from s to t using f.

function hanoi(f, s, t, n) {
    // if (n > 0) {
    //     hanoi(f, t, s, n - 1);
    //     console.log(`${f} -> ${t}`);
    //     hanoi(s, f, t, n - 1);
    // }
    // OR
    // base case (s)
    if (n <= 0)
        return;
    if (n === 1) {
        console.log(`Move disk ${n} from ${f} to ${t}`);
        return;
    }
    // recursive case
    hanoi(f, t, s, n - 1);
    console.log(`Move disk ${n} from ${f} to ${t}`);
    hanoi(s, f, t, n - 1);
}

// take some input from the user
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question('Enter the number of disks: ', (num) => {
    const n = parseInt(num);
    hanoi('f', 's', 't', n); 
    readline.close();
  });
