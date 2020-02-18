;;;; pe-001-to-099.lisp ---
;;;; Created  : <2020-02-09 Sun 22:13:59 GMT>
;;;; Modified : <2020-02-17 Mon 18:51:04 GMT>

(in-package :peh)


(defun pe-001 ()
  "MULTIPLES OF 3 AND 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."
  (loop :for n :from 1 :to 1000
     :when (or (zerop (mod n 3))
               (zerop (mod n 5)))
     :sum n))


(defun pe-002 ()
  "EVEN FIBONACCI NUMBERS
Credits: https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the
 previous two terms.  By starting with 1 and 2, the first 10 terms
 will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... , F(n-1) + F(n+1)

By considering the terms in the Fibonacci sequence whose values do not
 exceed fou million, find the sum of the even-valued terms."
  (loop :for i :from 0 :upto 4000000
     :when (and (peh-utils:fibonaccip i)
                (zerop (mod i 2)))
     :sum i))


(defun pe-003 ()
  "Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? "
  (reduce #'max (peh-utils:seq-prime-factors 600851475143)))


(defun pe-004 ()
  "Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers."
  )
;;;; pe-001-to-099.lisp