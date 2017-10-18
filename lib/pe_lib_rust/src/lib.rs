//use std::f64;

// ------------------------------------------------------------------------------
/// # BEGIN-PRIME-NUMBERS
pub mod primes {
    /// Primality test of the NUM by trail divison.
    pub fn prime_p(num: u64) -> bool {
        if num == 1 {
            return false;
        }
        if num == 2 {
            return true;
        }

        let sqrt_lim: u64 = (num as f64).sqrt() as u64 + 1;

        let mut i: u64 = 2;
        while &i < &sqrt_lim {
            if num % &i == 0 {
                return false;
            }
            i = i + 2;
        }
        return true;
    }
    // Return a vector from 2 till NUM.
    // pub fn prime_set(num: u64) -> Option<Vec> {
    //     let mut p_set: Vec<u64> = Vec::new();
    //     let mut i: u64 = 2;

    //     while &i < &num {
    //         if prime_p(i) {
    //             p_set.push(i);
    //         }
    //         i = i + 1;
    //     }
    //     return Some(p_set)
    // }
}

// API

// fn primve_p
// fn prime_set

// FACTORING
// fn factors_set
// fn prime_factors_set
// fn aliquot_sum
// fn perfect_p
// fn perfect_set

// DIGITS
// fn digits_sum
