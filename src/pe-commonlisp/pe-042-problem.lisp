;;; pe-042-problem.lisp -- Coded triangle numbers
;;; Author   : Sharlatan <sharlatan@protonmail.com>
;;; Created  : <2017-5-14 Sun 00:24:07 BST>
;;; Modified : <2017-5-17 Wed 23:32:11 BST> sharlatan
;;; Link     : https://projecteuler.net/problem=42

;;;
;; The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
;; so the first ten triangle numbers are:

;; 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

;; By converting each letter in a word to a number corresponding to its
;; alphabetical position and adding these values we form a word value. For
;; example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
;; is a triangle number then we shall call the word a triangle word.

;; Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
;; containing nearly two-thousand common English words, how many are triangle
;; words?

(load "pe.lisp")

(defun opener (file-path)
  (with-open-file (streem file-path)
    (loop for line = (read-line streem nil)
          while line do (format t "~a~%" line))))

(loop for i from 1 to 100000 do
  (format t "~d: ~d~%" i (3-num-p i)))

;;; End of pe-042-problem.lisp
