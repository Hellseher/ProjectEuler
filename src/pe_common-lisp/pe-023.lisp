(dotimes (x 20)
	(dotimes (y 20)
		(format t "~3d " (* (1+ x) (1+ y))))
	(format t "~%"))
