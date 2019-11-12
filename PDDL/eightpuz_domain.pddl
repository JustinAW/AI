(define (domain eightpuzzle)
    (:requirements :strips :typing)

    (:types place physobj - object
            slot - place
            tile - physobj
    )

    (:predicates (at ?tile - tile ?slot - slot)
                 (adj ?s1 - slot ?s2 - slot)
                 (empty ?slot - slot)
    )

    (:action move-tile
        :parameters (?tile - tile ?loc-from - slot ?loc-to - slot)
        :precondition (and (at ?tile ?loc-from)
                           (empty ?loc-to)
                           (adj ?loc-from ?loc-to))
        :effect (and (not (at ?tile ?loc-from))
                     (at ?tile ?loc-to)
                     (not (empty ?loc-to))
                     (empty ?loc-from))
    )
)