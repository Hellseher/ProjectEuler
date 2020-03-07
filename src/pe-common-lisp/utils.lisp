;;;; pe-utils.lisp
;;;; Created  : <2020-02-09 Sun 21:39:50 GMT>
;;;; Modified : <2020-3-07 Sat 20:46:58 gmt>

(in-package :peh-utils)

(defun compute-cache-path ()
  "Computes the directory where accumulated cache should reside."
  (merge-pathnames
   (make-pathname :directory '(:relative "cache"))
   (make-pathname :directory
                  (pathname-directory
                   (truename (asdf:system-source-directory :peh))))))

(defun cache-save (sequence file)
  "Save acumulated cache under local source to the cache/FILE"

  (let* ((cache-path (compute-cache-path))
         (cache-file (merge-pathnames cache-path file)))
    (ensure-directories-exist cache-path)
    (with-open-file (stream cache-file
                            :direction :output
                            :if-exists :supersede)
      (with-standard-io-syntax
        (print sequence stream)))))

(defun cache-load (file)
  (let ((cache-path (compute-cache-path)))
    cache-path
    file
    cache-path))

(defun load-as-list (filename)
  (with-open-file (stream filename)
    (loop
       :for line = (read-line stream nil)
       :while line
       :collect line)))

;;; TODO
;; + add caching of sequences
;; + add load/save functionality
;; + load from cache when exists or save first to cache if not
;; + key or option to use cache

(defparameter +phi+ (/ (1+ (sqrt 5)) 2))

;;; Numbers predicates

(defun primep (n)
  "Primality test of the N by trial division."
  (check-type n (integer 0 *))
  (cond ((= n 0) nil)
        ((= n 1) nil)
        ((< n 4) t)
        ((zerop (mod n 2)) nil)
        ((< n 9) t)
        ((zerop (mod n 3)) nil)
        (t (loop :for i :from 5 :upto (sqrt n) :by 2
              :do (when (zerop (mod n i))
                   (return-from primep nil)))
           t)))

(defun fibonaccip (n)
  "Check if the given number N is a Fibonacci number."
  (check-type n (integer 0 *))
  (or (fig-square-p (+ (* 5 (expt n 2)) 4))
      (fig-square-p (- (* 5 (expt n 2)) 4))))

(defun palindromep (n)
  "Check if the given number N is polindrome."
  (check-type n (integer 0 *))
  (cond ((< n 10) nil)
        (t (= n (reverse-digits n)))))

(defun perfectp (n)
  "Check if N is perfect number. It is a sum of all positive divisors
of N which is equal to N."
  (check-type n (integer 0 *))
  (= (aliquot-sum n) n))

(defun deficientp (n)
  "Check if N is deficient number. It less then sum of it's proper
  divisors."
  (check-type n (integer 0 *))
  (< (aliquot-sum n) n))


(defun nth-fibonacci (n)
  "Compute N's Fibonacci number."
  (check-type n (integer 0 *))
  (loop :for f1 = 0 :then f2
     :and f2 = 1 :then (+ f1 f2)
     :repeat n :finally (return f1)))

;;; Sequences

(defun aliquot-sum (n)
  "Return the sum of all proper devisors of N."
  (check-type n (integer 0 *))
  (reduce #'+ (seq-factors n)))

;;; Digits

(defun digits->number (digits)
  "Return a number represented by list of DIGITS.
Add check-type a list of integers."
  (let* ((reversed-digits (reverse digits)))
    (reduce
     (lambda (digit number)
       (+ digit (* 10 number)))
     reversed-digits
     :from-end t)))

(defun reverse-digits (n &optional (base 10))
  "Return an intger with reversed digits of N.
https://codereview.stackexchange.com/questions/1219"
  (check-type n (integer 0 *))
  (labels ((next (n v)
             (if (zerop n) v
                 (multiple-value-bind (q r)
                     (truncate n base)
                   (next q (+ (* v base) r))))))
    (next n 0)))

(defun number->list (n)
  "Coercing N to list of digits."
  (map 'list #'digit-char-p (prin1-to-string n)))

(defun digits-sum (n)
  "Return a sum of digits for a given number N."
  (reduce #'+ (number->list n)))

(defun factorial (n)
  "Return factorial of N."
  (check-type n (integer 0 *))
  (apply #'* (loop :for i :from 1 :to n :collect i)))

(defun ! (n)
  "Aliace to `factorial'"
  (check-type n (integer 0 *))
  (factorial n))

(defun sum-of-numbers (n)
  "Return a resulting sum for the integers sequence up to N."
  (/ (+ (expt n 2) n) 2))

(defun square-pyramidal-number (n)
  "Return Nth pyramidal number."
  (/ (+ (* (expt n 3) 2)
        (* (expt n 2) 3)
        n)
     6))

;;; Figurate Numbers

(defun fig-square-p (n)
  "Check if the given N is a perfect square number.
https://oeis.org/A000290"
  (check-type n (integer 0 *))
  (let ((sqrt (isqrt n)))
    (= n (* sqrt sqrt))))

(defun fig-three-num (n)
  "Return computed N triangular number."
  (check-type n (integer 0 *))
  (if (= n 1)
      1
      (/ (* n (+ n 1)) 2)))

(defun fig-three-num-p (n)
  "Check whether N is a triangular number."
    (= (sqrt (+ (* 8 n) 1))
     (isqrt (+ (* 8 n) 1))))

(defun fig-three-num-set (n)
  "Return a list of triangular numbers up to N."
  (check-type n (integer 0 *))
  (loop :for i :from 1 :to n
     :collect (fig-three-num n)))

(defun fig-four-num (n)
  "Return computed Nth figurative number four."
  (check-type n (integer 0 *))
  n)

(defun fig-four-num-p (n)
  "Check whether N is a figurative number four."
  n)

(defun fig-four-num-set (n)
  "Return a list of figurative numbers of four."
  (check-type n (integer 0 *))
  n)

;;; Strings

;; Not working with UNICODE only Enlish alphabet.
(defun word-to-alpha-pos (word)
  "Return a list of numbers for each letter in the WORD corresponding to its
  alphabetical position."
  (mapcar (lambda (char) (+ (- char (char-code #\A)) 1))
          (mapcar #'char-code (coerce (string-upcase word) 'list))))

;;; End of project-euler.lisp
