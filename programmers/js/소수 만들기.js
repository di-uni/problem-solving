function solution(nums) {
    var res = 0;
    const prime = {};
    
    const isPrime = (n) => {                
        for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
            if (prime[n]) {
                break;
            }

            if (prime[i]) {
                continue;
            }

            for (let j = i ** 2; j <= n; j += i) {      
                prime[j] = true;
            }
      }

      return !prime[n];
    }
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (isPrime(nums[i] + nums[j] + nums[k])){
                    res++;
                }
            }   
        }
    }
    
    return res;
}