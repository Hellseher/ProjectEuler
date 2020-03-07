;;;; pe.lisp --- Project Euler Handbook

#-asdf3.1
(error "It requres ASDF at least version 3.1.")

(defsystem "peh"
  :long-name "Project Euler Handbook"
  :version "0.1.0"
  :description "Collection of utilities to solve problems on
  https://projecteuler.net"
  :author "Oleg Bocharov <oleg.bocharov@ipec.co.uk>"
  :maintainer ("Oleg Bocharov")
  :license ""
  :long-description ""
  :homepage ""
  :source-control (:git "https://github.com/Hellseher/peh")
  :encoding :utf-8
  :serial t
  :components
  ((:file "packages")
   (:file "utils" :depends-on ("packages"))
   (:file "sequences" :depends-on ("packages" "utils"))
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
