(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond
        ((= num 0) 0)
        ((> num 0) 1)
        (else -1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond 
        ((zero? y) 1)
        ((even? y) (pow (square x) (quotient y 2)))
        (else (* (pow x (- y 1)) x))
  )
)
