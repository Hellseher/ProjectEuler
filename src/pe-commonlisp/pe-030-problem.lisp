;;; 030-problem.lisp -- Digit cancelling fractions
;;; Author   : Sharlatan <sharlatan@protonmail.com>
;;; Created  : <2017-3-27 Mon 20:33:29 BST>
;;; Modified : <2017-4-01 Sat 21:19:12 BST> sharlatan
;;; Link     : https://projecteuler.net/problem=30

;;; Comments:

;; Surprisingly there are only three numbers that can be written as the sum of
;; fourth powers of their digits:
;;
;; 1634 = 1^4 + 6^4 + 3^4 + 4^4
;; 8208 = 8^4 + 2^4 + 0^4 + 8^4
;; 9474 = 9^4 + 44 + 7^4 + 4^4
;;
;; As 1 = 1^4 is not a sum it is not included.
;;
;; The sum of these numbers is 1634 + 8208 + 9474 = 19316.
;; Find the sum of all the numbers that can be written as the sum of fifth
;; powers of their digits.

;;; Code:

(defun list-to-disimal (dlist)
  "Return a disimal digit combined from a DLIST each memember represents disimal
  position."
  (reduce (lambda (x y) (+ (* 10 x) y))
          dlist))

(defun pe-30 ()
  (let ((good ()))
    (loop for i from 0 upto 9 do
         (loop for j from 0 upto 9 do
              (loop for k from 0 upto 9 do
                   (loop for l from 0 upto 9 do
                        (loop for m from 0 upto 9 do
                             (loop for n from 0 upto 9 do
                                  (when (and (equal (list-to-disimal (list i j k l m n))
                                                    (+ (expt i 5)
                                                       (expt j 5)
                                                       (expt k 5)
                                                       (expt l 5)
                                                       (expt m 5)
                                                       (expt n 5)))
                                             (> (list-to-disimal (list i j k l m n)) 9))
                                    (push (list-to-disimal (list i j k l m n)) good))))))))
    (reduce #'+ good)))
;;; End of 030-problem.lisp
