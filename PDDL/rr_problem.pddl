;; Farmer Crosses River Riddle PDDL Problem - Justin Weigle
;; The riddle:
;; https://www.mathsisfun.com/puzzles/farmer-crosses-river-solution.html

(define (problem moveallside2)
    (:domain riverriddle)

    (:objects boat - boat
              s1 - side
              s2 - side
              cabbage - cabbage
              goat - goat
              wolf - wolf
    )

    (:init (at cabbage s1) (at goat s1) (at wolf s1) (at boat s1) (empty boat))

    (:goal (and (at cabbage s2) (at goat s2) (at wolf s2) (at boat s2)))
)
