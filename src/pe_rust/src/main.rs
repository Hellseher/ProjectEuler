extern crate pe_lib_rust;

use pe_lib_rust::primes;

fn main() {
    let mut i: u64 = 1;
    let limit: u64 = 10000;

    while &i < &limit {
        if primes::prime_p(i) {
            println!("{} is prime! Limit was {} ", &i, (i as f64).sqrt() as u64);
        }
        i = i + 1;
    }

    let check_iter = (1..100).filter(|x| primes::prime_p(x as u64)).collect::<Vec<usize>>();
    println!("check_iter = {:?}", check_iter);
}
