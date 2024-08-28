(define (fit total n)
  (define (f total n k)
      (if (and (= n 0) (= total 0))
      #t
      (if (< total (* k k))
      #f
      (or (f total n (+ k 1)) (f (- total (* k k)) (+ k 1)))
      )))
  (f total n 1))

(define with-list
  (list (list 'a 'b) 'c 'd (list 'd) )
)
; (draw with-list) ; Uncomment this line to draw with-list