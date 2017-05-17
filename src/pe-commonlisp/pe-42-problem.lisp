;;; pe-042-problem.lisp -- Coded triangle numbers
;;; Author   : Sharlatan <sharlatan@protonmail.com>
;;; Created  : <2017-4-02 Sun 00:09:27 BST>
;;; Modified : <2017-4-16 Sun 12:12:08 BST> sharlatan
;;; Link     : https://projecteuler.net/problem=42

;;; Commentary:

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

;;; Code:

;;; "/home/sharlatan/Projects/hack/ProjectEuler.net/txt/p042_words.txt"
(defun read-words (path)
  (with-open-file (stream path)
    (loop while (peek-char nil stream nil nil)
       collect (read stream))))

(defun split (chars str &optional (lst nil) (accm ""))
  (cond
    ((= (length str) 0) (reverse (cons accm lst)))
    (t
     (let ((c (char str 0)))
       (if (member c chars)
           (split chars (subseq str 1) (cons accm lst) "")
           (split chars (subseq str 1)
                  lst
                  (concatenate 'string
                               accm
                               (string c))))
       ))))

(defun split2 (delim line)
  "Return a list of subsequences separated by a one character delimiter, delim itself is not returned"
  (loop :for mark = 0 :then (1+ point)
     :for point = (position delim line :start mark)
     :collect (subseq line mark point)
     :while point))

(defun make-list-from-text (fn)
  "assemble list of lists of numbers parsed from file, posed by drkrause on cll 2009-01-16"
  (with-open-file (stream fn)
    (loop :for line = (read-line stream nil nil)
       :while line
       :collect (mapcar #'alpha-char-p (split2 #\, line)))))
;;; End of pe-42-problem.lisp
