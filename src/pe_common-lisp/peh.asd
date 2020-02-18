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
  :description "Run all `pe-N' functions, which accept no arguments
  and only return result as ingeger."
  :components ((:module "t"
                        :serial t
                        :components ((:file "packages")
                                     (:file "run" :depends-on ("packages")))))
  :depends-on (:peh))

;;;; peh.lisp ends here
