(define (ascending? s) 
    (if (or (null? s) (null? (cdr s))) #t
            (and (<= (car s) (car (cdr s))) (ascending? (cdr s)))
        )
)

(define (my-filter pred s)
    (cond
        ((null? s) nil)
        ((pred (car s)) (append (list (car s)) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 
    (cond 
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (append (list (car lst1)) (helper lst2 (cdr lst1))))))

(define (helper lst1 lst2)
    (cond 
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (append (list (car lst1)) (interleave lst2 (cdr lst1))))))

(define (no-repeats s) 
    (if (null? s) nil
        (append (list (car s)) (no-repeats (filter (lambda (x) (not(= (car s) x))) (cdr s)))))
)
