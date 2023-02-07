function findSumEvenFibo(limit){
    let fibo = 0, a1 = 0, a2 = 1, total = 0

    while (fibo <= limit){
        fibo = a1 + a2
        if(fibo % 2 == 0){
            total = total + fibo
        }
        a1 = a2
        a2 = fibo
    }

    return total
}

console.log(findSumEvenFibo(4000000))