(define (split-at lst n)  
  (cond 
        ((> n (length lst)) (cons lst nil))
        ((zero? n) (cons nil lst))
        (else 
        (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1))))
        )
  )
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
  (define (helper x)
      ( if (null? funcs) x
            ((compose-all (cdr funcs)) ((car funcs) x))
      )
  )
  helper
)

