(define fact (lambda (n) (if (zero? n) 1 (* n (fact (- n 1))))))


(define-macro (trace expr) ; (trace (fact 5))
    (define operator (car expr))
`(begin 
    (define original ,operator)
    (define ,operator (lambda (n)
                        (print (list (quote ,operator) n))
                        (original n)))
    (define result ,expr)
    (define ,operator original)
    result))

(define (trace expr) ; (trace (fact 5))
    (define operator (car expr))
`(begin 
    (define original ,operator)
    (define ,operator (lambda (n)
                        (print (list (quote ,operator) n))
                        (original n)))
    (define result ,expr)
    (define ,operator original)
    result))
