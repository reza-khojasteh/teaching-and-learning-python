// hanoi towers in js
function hanoi(f, s, t, n) {
    // if (n > 0) {
    //     hanoi(f, t, s, n - 1);
    //     console.log(`${f} -> ${t}`);
    //     hanoi(s, f, t, n - 1);
    // }
    // OR
    // Base cases:
    if (n <= 0) {
        return;
    }
    if (n === 1) {
        console.log(`${f} -> ${t}`);
        return;
    }
    // general case:
    hanoi(f, t, s, n - 1);
    console.log(`${f} -> ${t}`);
    hanoi(s, f, t, n - 1);
}

hanoi('f', 's', 't', 3);
