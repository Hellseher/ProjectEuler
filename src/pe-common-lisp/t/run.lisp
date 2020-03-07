;;;; Modified : <2020-02-25 Tue 23:58:58 GMT>

(in-package :peh-test)

(defun all-function-symbols (package-name)
  "Retrives all function symbols from a PACKAGE-NAME."
  (declare ((or package string symbol) package-name))
  (the list
       (let ((functions (list))
             (package (find-package package-name)))
         (cond (package (do-all-symbols (symb package)
                          (when (and (fboundp symb)
                                     (eql (symbol-package symb) package))
                            (push symb functions)))
                        functions)
               (t (error "~S does not disignate a package" package-name))))))

(defun run-tests ()
  (loop :for fn :in (all-function-symbols 'peh)
     :do (format t "~A: ~A~%" fn (funcall fn))))
