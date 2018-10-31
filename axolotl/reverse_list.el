; A program to reverse a given list ex. a, b, c -> c, b, a
; Used to show the difference between the same program in LISP and Axolotl

;LISP
(defun rev (l)
  (cond
   ((null l) '())
   (T (append (rev (cdr l)) (list (car l))))))
