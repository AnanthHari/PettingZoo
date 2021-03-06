
### Combat: Biplane

This environment is part of the [Atari environments](../atari.md). Please read that page first for general information.

| Observations | Actions | Agents  | Manual Control | Action Shape | Action Values | Observation Shape | Observation Values | Num States |
|--------------|---------|---------|----------------|--------------|---------------|-------------------|--------------------|------------|
| Graphical    | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            | ?          |

`from pettingzoo.atari import combat_biplane_v0`

`agents= ["first_0", "second_0"]`

![combat_biplane gif](../../gifs/atari_combat_biplane.gif)

*AEC diagram*


*Combat*'s biplane mode is an adversarial game where timing,
positioning, and keeping track of your opponent's complex
movements are key.

The players fly around the map, able to control direction
but not speed. When your opponent is hit by your bullet,
you score a point.
Whenever you score a number of points, you are rewarded by
that number and your opponent is penalized by that number.


#### Environment parameters

Environment parameters are common to all Atari environments and are described in the [base Atari documentation](../atari.md) .

