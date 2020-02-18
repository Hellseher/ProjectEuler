;;;; packages.lisp ---
;;;; Created : <2020-02-11 Tue 23:51:32 GMT>
;;;; Modified : <2020-02-17 Mon 22:02:20 GMT>

(in-package :cl-user)

(defpackage #:peh-utils
  (:nicknames #:pehu)
  (:use :cl)
  (:export #:primep
           #:fibonaccip
           #:seq-fibonacci
           #:seq-prime-factors
           #:seq-primes))

(defpackage #:peh
  (:use :cl)
  (:export #:pe-001
           #:pe-002
           #:pe-003
           #:pe-004))

;;;; packages.lisp ends here
