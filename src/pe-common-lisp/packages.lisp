;;;; packages.lisp ---
;;;; Created : <2020-02-11 Tue 23:51:32 GMT>
;;;; Modified : <2020-3-07 Sat 20:50:34 gmt>

(in-package :cl-user)

(defpackage #:peh-utils
  (:nicknames #:pehu)
  (:use :cl)
  (:export +phi+ #:primep #:fibonaccip #:palindromep #:seq-fibonaccis
  #:seq-factors #:seq-prime-factors #:seq-primes #:sum-of-numbers
  #:seq-square-pyramidal-numbers #:square-pyramidal-number #:seq-prime-numbers
  #:max-product-subseq #:max-sum-subseq #:seq-primes-below #:slide-list
  #:number->list #:load-as-list))

(defpackage #:peh
  (:use :cl)
  (:export #:pe-001 #:pe-002 #:pe-003 #:pe-004 #:pe-005 #:pe-006
  #:pe-007 #:pe-008 #:pe-010))

;;;; packages.lisp ends here
