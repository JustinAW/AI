;; Farmer Crosses River Riddle PDDL Domain - Justin Weigle
;; The riddle:
;; https://www.mathsisfun.com/puzzles/farmer-crosses-river-solution.html

(define (domain riverriddle)
    (:requirements :strips :typing)

    (:types place physobj - object
            side - place
            cargo vehicle - physobj
            boat - vehicle
            wolf goat cabbage - cargo
    )

    (:predicates (at ?obj - physobj ?loc - place)
                 (in ?cgo - cargo ?veh - vehicle)
                 (empty ?b - boat)
    )

    (:action load-cargo
        :parameters (?cgo - cargo ?boat - boat ?loc - place)
        :precondition (and (at ?boat ?loc) (at ?cgo ?loc) (empty ?boat))
        :effect (and (not (at ?cgo ?loc)) (in ?cgo ?boat) (not (empty ?boat)))
    )

    (:action unload-cargo
        :parameters (?cgo - cargo ?boat - boat ?loc - place)
        :precondition (and (in ?cgo ?boat) (at ?boat ?loc) (not (empty ?boat)))
        :effect (and (not (in ?cgo ?boat)) (at ?cgo ?loc) (empty ?boat))
    )

    (:action move-boat
        :parameters (?boat - boat ?loc-from - side ?loc-to - side ?w - wolf ?g - goat ?c - cabbage)
        :precondition (and (at ?boat ?loc-from)
                           (or (not (at ?w ?loc-from)) (not (at ?g ?loc-from)))
                           (or (not (at ?g ?loc-from)) (not (at ?c ?loc-from)))
        )
        :effect (and (not (at ?boat ?loc-from)) (at ?boat ?loc-to))
    )
)
