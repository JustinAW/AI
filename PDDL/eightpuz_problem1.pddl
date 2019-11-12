;; Justin Weigle
;; Eight Tile Puzzle PDDL problem 1

(define (problem p1)
    (:domain eightpuzzle)

    (:objects t1 t2 t3 t4 t5 t6 t7 t8 - tile
              s1 s2 s3 s4 s5 s6 s7 s8 s9 - slot
    )

    (:init
        (at t1 s1) (at t3 s2) (at t4 s3)
        (at t8 s4) (at t6 s5) (at t2 s6)
        (at t7 s7) (empty s8) (at t5 s9)

        ; set the adjacencies
        (adj s1 s2)(adj s1 s4)
        (adj s2 s1)(adj s2 s3)(adj s2 s5)
        (adj s3 s2)(adj s3 s6)
        (adj s4 s1)(adj s4 s5)(adj s4 s7)
        (adj s5 s2)(adj s5 s4)(adj s5 s6)(adj s5 s8)
        (adj s6 s3)(adj s6 s5)(adj s6 s9)
        (adj s7 s4)(adj s7 s8)
        (adj s8 s5)(adj s8 s7)(adj s8 s9)
        (adj s9 s6)(adj s9 s8)
    )

    (:goal (and
        (at t1 s1) (at t2 s2) (at t3 s3)
        (at t8 s4)            (at t4 s6)
        (at t7 s7) (at t6 s8) (at t5 s9))
    )
)
