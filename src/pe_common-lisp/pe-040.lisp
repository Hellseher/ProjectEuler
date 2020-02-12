;;; pe-040-problem.lisp -- Digit cancelling fractions
;;; Author   : Sharlatan <sharlatan@protonmail.com>
;;; Created  : <2017-3-31 Fri 23:20:09 BST> sharlatan
;;; Modified : <2017-4-01 Sat 21:19:12 BST> sharlatan
;;; Link     : https://projecteuler.net/problem=40


(defun pe-40 ()
  (let ((x 0)
        (y 1)
        (d 10.0)
        (e 1.0)
        (n 0))
    (loop while ((and (not (equal y x))
                      (equal y x)))
       do (setf n (1+ n))))
;;; End of pe-040-problem.lisp
  )
