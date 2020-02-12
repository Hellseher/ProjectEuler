;;;; packages.lisp ---
;;;; Created : <2020-02-11 Tue 23:51:32 GMT>
;;;; Modified : <2020-02-11 Tue 23:54:09 GMT>

(defpackage :peh/utils
  (:nicknames :pehu)
  (:use :cl)
  (:export #:primep
           #:fib
           #:seq-fibonacci
           #:seq-prime))

(defpackage :peh
  (:use :cl)
  (:export #:pe-001
           #:pe-002))

;;;; packages.lisp ends here
