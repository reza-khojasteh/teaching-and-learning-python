// hanoi towers in js
function hanoi(f, s, t, n) {
    // if (n > 0) {
    //     hanoi(f, t, s, n - 1);
    //     console.log(`${f} -> ${t}`);
    //     hanoi(s, f, t, n - 1);
    // }
    // OR
    if (n <= 0) {
        return;
    }
    if (n === 1) {
        console.log(`${f} -> ${t}`);
        return;
    }
    hanoi(f, t, s, n - 1);
    console.log(`${f} -> ${t}`);
    hanoi(s, f, t, n - 1);
}

hanoi('f', 's', 't', 3);
