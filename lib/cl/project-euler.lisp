;;; project-euler.lisp -- Library for solvin problems.
;;; Author   : Sharlatan <sharlatan@protonmail.com>
;;; Created  : <2017-4-01 Sat 21:42:13 BST> sharlatan
;;; Modified : <2017-5-16 Tue 00:34:01 BST> sharlatan


;; PRIME NUMBERS

(defun prime-p (num)
  "Test the NUM on primiriaty."
  (cond ((= num 1) nil)
        ((< num 4) t)
        ((zerop (mod num 2)) nil)
        ((< num 9) t)
        ((zerop (mod num 3)) nil)
        (t (loop for i from 5 upto (sqrt num) by 2
              do (when (zerop (mod num i))
                   (return-from prime-p nil)))
           t)))

(defun prime-set (num)
  "Return a set of prime numberes up to NUM."
  (let ((prime-list ()))
    (loop for i from 1 upto num
       do (when (prime-p i)
            (push i prime-list)))
    prime-list))

;;; FACTORING

(defun factors-set (num)
  "Return a set of all positive factors of NUM."
  (if (<= num 1)
      '()
      (let ((divs (list 1)))
        (loop for i from 2 upto (isqrt num)
           do (when (zerop (mod num i))
                (push i divs)
                (let ((j (/ num i)))
                  (when (/= j i)
                    (push j divs)))))
        divs)))

(defun prime-factors-set (num)
  "Return a set of all prime proper devisors of NUM."
  (let ((prime-divs ()))
    (loop for i from 2 upto (sqrt num)
       do (when (and (prime-p i)
                     (zerop (mod num i)))
            (push i prime-divs)))
    prime-divs))

(defun aliquot-sum (num)
  "Return the sum of all proper devisors of NUM."
  (reduce #'+ (factors-set num)))

(defun perfect-p (num)
  "Test NUM for perfectness."
  (if (= (aliquot-sum num) num)
      t
      nil))

(defun perfects-set (num)
  "Return a set of perfect numbers upto NUM.
WARNING: Slow after 1000000"
  (let ((perfets ()))
    (loop for i from 1 upto num
       do (when (perfect-p i)
            (push i perfets)))
    perfets))


;;; DIGITS

(defun %num-to-list (num)
  "Coercing NUM to list."
  (map 'list #'digit-char-p (prin1-to-string num)))

(defun digit-sum (num)
  "Return a sum of digits for NUM."
  (reduce #'+ (%num-to-list num)))

(defun factorial (num)
  "Return factorial of NUM."
  (reduce #'* (loop for i from 1 to num collect i)))


;;; FIGURATE NUMBERS

(defun 3-nth-num (nth)
  "Return computed NTH triangular number."
  (if (= nth 1)
      1
      (/ (* nth (+ nth 1)) 2)))

(defun 3-num-p (num)
  "Check whether NUM is a triangular number."
  (= (sqrt (+ (* 8 num) 1))
     (isqrt (+ (* 8 num) 1))))

(defun 3-num-set (num)
  "Return a list of triangular numbers up to NUM."
  (loop for i from 1 to num
     collect (3-nth-num num)))

;;; STRINGS

;; Not working with UNICODE only Enlish alphabet.
(defun word-to-alpha-pos (word)
  "Return a list of numbers for each letter in the WORD corresponding to its
  alphabetical position."
  (mapcar (lambda (char) (+ (- char (char-code #\A)) 1))
          (mapcar #'char-code (coerce (string-upcase word) 'list))))
;;; End of project-euler.lisp
