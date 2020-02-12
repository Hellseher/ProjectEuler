;;;; pe.lisp --- Project Euler Handbook

(defsystem "peh"
  :long-name "Project Euler Handbook"
  :version "0.1.0"
  :author ("Oleg Bocharov")
  :description ""
  :long-description ""
  :homepage ""
  :serial t
  :components
  ((:file "packages")
   (:file "utils" :depends-on ("packages"))
   (:file "pe-001-to-099" :depends-on ("packages" "utils"))))

(defsystem "peh/test"
  )

;;;; peh.lisp ends here
