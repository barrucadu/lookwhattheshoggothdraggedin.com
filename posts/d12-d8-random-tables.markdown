---
title: 1d12 + 1d8 Random Tables
date: 2021-05-02
topic: gm-advice
---

I [read a post][] about how [abbr:dnd] suggests `1d12 + 1d8`
for random encounter tables.  It gives a distribution from 2 to
20, where the numbers 9 to 13 are equally likely, and the others
gradually less so as you get to the extremes.

[read a post]: https://merricb.com/2020/10/12/random-encounters-1d8-1d12/

That's already pretty nice but, whenever I see a small number of dice
being rolled together, I can't help but wonder "what if you roll one
die with advantage or disadvantage"?

If we skew the `d12`, we get a gradual shift in
the distribution, making 9 or 13 the most likely numbers, and the
chance of getting a 2 or a 20 almost negligible if you're skewing the
die the other way.

!!!probability-table
2,1.99652777778,1.04166666667,0.0868055555556
3,3.81944444444,2.08333333333,0.347222222222
4,5.46875,3.125,0.78125
5,6.94444444444,4.16666666667,1.38888888889
6,8.24652777778,5.20833333333,2.17013888889
7,9.375,6.25,3.125
8,10.3298611111,7.29166666667,4.25347222222
9,11.1111111111,8.33333333333,5.55555555556
10,9.72222222222,8.33333333333,6.94444444444
11,8.33333333333,8.33333333333,8.33333333333
12,6.94444444444,8.33333333333,9.72222222222
13,5.55555555556,8.33333333333,11.1111111111
14,4.25347222222,7.29166666667,10.3298611111
15,3.125,6.25,9.375
16,2.17013888889,5.20833333333,8.24652777778
17,1.38888888889,4.16666666667,6.94444444444
18,0.78125,3.125,5.46875
19,0.347222222222,2.08333333333,3.81944444444
20,0.0868055555556,1.04166666667,1.99652777778

On the other hand, if we skew the `d8`, we keep
the equally-likely 9 to 13 range, but the edges of the distribution
change a lot:

!!!probability-table
2,1.953125,1.04166666667,0.130208333333
3,3.64583333333,2.08333333333,0.520833333333
4,5.078125,3.125,1.171875
5,6.25,4.16666666667,2.08333333333
6,7.16145833333,5.20833333333,3.25520833333
7,7.8125,6.25,4.6875
8,8.203125,7.29166666667,6.38020833333
9,8.33333333333,8.33333333333,8.33333333333
10,8.33333333333,8.33333333333,8.33333333333
11,8.33333333333,8.33333333333,8.33333333333
12,8.33333333333,8.33333333333,8.33333333333
13,8.33333333333,8.33333333333,8.33333333333
14,6.38020833333,7.29166666667,8.203125
15,4.6875,6.25,7.8125
16,3.25520833333,5.20833333333,7.16145833333
17,2.08333333333,4.16666666667,6.25
18,1.171875,3.125,5.078125
19,0.520833333333,2.08333333333,3.64583333333
20,0.130208333333,1.04166666667,1.953125

Skewing the distribution gives us more options to play with.  We can
prepare a single table which covers a variety of situations, and roll
with advantage or disadvantage depending on the situation.

To construct the table, I find it helpful to use a symmetric pattern:

!!!roll-table
`1d12+1d8` Encounters
2,Extremely rare
3,Very rare
4,Very rare
5,Rare
6,Rare
7,Uncommon
8,Uncommon
9,Common
10,Common
11,Common
12,Common
13,Common
14,Alternate version of `8`
15,Alternate version of `7`
16,Alternate version of `6`
17,Alternate version of `5`
18,Alternate version of `4`
19,Alternate version of `3`
20,Alternate version of `2`

So if, for example, your `4` is something like "unexpectedly good
weather makes it easy to navigate", then your `18` would be
"unexpectedly bad weather makes it difficult to navigate"; or if your
`7` is something like "meet a friendly NPC" then your `15` would be
"meet a hostile NPC".  But that's just for inspiration, you don't need
to stick to it religiously.

The rest of this post gives two examples of such tables, which should
work with skewing either die.  It's up to you how dramatically
different you want the two extremes to be.

## 1d12 + 1d8 encounters in a tea room

This pair of tables covers the sorts of people the party may meet, the
rumours they might overhear, and the rare teas they could find in a
tea room.  If your setting doesn't have tea rooms, it shouldn't be too
difficult to reskin as a cafe or something similar.

Skew low if the party are in a seedy area, high if they're in a rich
area.

The rare teas table is just a single die, though by rolling a smaller
die and giving it a modifier, you can apply the same sort of idea: the
teas at the extremes can be made more likely in certain outcomes on
the encounter table.

!!!roll-table
`1d12+1d8` Encounters in a Tea Room
2,You find a box of rare teas for sale.  Roll `1d6` on the Rare Teas table `1d2+1` times.
3,You recognise by certain signs that this shop has an entrance to an underground network of tunnels known as the "Thieves' Highway".
4,The shopkeeper is busy kicking in the teeth of a would-be shoplifter.  For the moment, he's distracted...
5,You find a box of rare tea for sale.  Roll `1d4` on the Rare Teas table.
6,You ask to sample some tea, which seems to take the shopkeeper aback.  He doesn't heat the water enough, steeps the leaves for too long and, on closer inspection, the leaves are dusty with age!  This shop is clearly a front for something else.
7,As you browse the shelves, a pickpocket attempts to sneakily make off with your coin purse!
8,A fortune teller sits in a corner of the shop, willing to read your future from the tea leaves, if you part with some coin.
9,You hear a rumour that the city guard have raided a fence posing as a tea room.
10,A group of travellers, who look like they've just arrived from the wilds, are sitting around a table discussing recent monster activity in the local area.
11,A travelling merchant is critically evaluating the stock, but seems to want something a bit more special.
12,A group of apprentices are sitting around a table gossiping loudly about their masters.
13,You hear a rumour that an esteemed magistrate's eldest son and heir has run off with a servant girl.
14,You learn that the shopkeeper is preparing to send a caravan to one of his remoter, and higher quality, suppliers.  He's looking to hire reliable guards and other useful sorts.
15,As you sit sipping a cup of chai, a local businessman, with whom you have had some dealings previously, strides into the room.  He spots you and approaches.
16,The shopkeeper glances up at you as you enter and says "about time, quick, get this to your master!" and hands you a small, ornate, wooden chest.  You have no idea what he's talking about.
17,You find a box of rare tea for sale.  Roll `1d4+2` on the Rare Teas table.
18,The shopkeeper is being intensely questioned by a servant of the local High Priest, a man known for his love of tea.  For the moment, he's distracted...
19,You hear some juicy gossip about recent indiscretions of the Imperial Heir.  If it hasn't spread very far yet, someone might pay well for this information.
20,You find a box of rare teas for sale.  Roll `1d6` on the Rare Teas table `1d2+1` times.

!!!roll-table
`1d6` Rare Teas
1,**Rogue's Friend.**  Made of rare and expensive herbs and steeped with a body part (hair, nails, etc) from the chosen target, tastes slightly peppery, and physically transforms the drinker into the target until the next sunrise or sunset.  The transformation is very painful.
2,**Purple Spiral Tea.**  Smells and tastes like a high-quality black tea.  Fatally toxic, unless the drinker has chewed fresh mint leaves recently.  Leaves no identifying trace.
3,**Galen's Brew.**  Allows the drinker to see in the dark, in colour, until they next go to the bathroom.  Makes the eyes glow.
4,**Shou Dark Tea.**  Smells and tastes of earth, a bit of an acquired taste.  Heals minor ailments, and accelerates healing of injuries.
5,**Amaialeth.**  A foul-tasting mushroom-based tea.  It's said that only those with noble blood can drink it without screwing their face up.
6,**Longevity Leaf.**  Delicate white leaves which must be kept perfectly dry until the moment of brewing, or they lose all potency.  Prevents the effects of ageing if drunk weekly, but all of the accumulated weeks take their toll at once if the drinker stops.

## 1d12 + 1d8 events in the distant wilds

This one is just a single table, covering the sort of places you might
trek out to in a West Marches campaign.  The wilderness, far from
civilisation, where any humans you encounter are more likely to be
criminals hiding from society or fellow adventurers, than they are
merchants or villagers.

Skew low if the party are in a relatively safe place, high if not.

The table has events, like the weather changing or the party getting
lost, as well as things they might encounter.  Think of *The Hobbit*
or *The Lord of the Rings*: as the party move from the safety of the
Shire or Rivendell out into the dangers of Mirkwood or Caradhras, the
landscape and weather become as much a danger (if not more so) than
the things they meet.

But even in a relatively safe place, there are still dangers (like Old
Man Willow lurking outside the Shire); and even in a relatively
dangerous place, it's not all bad (like finding an unexpected, though
temporary, ally in Smeagol).

!!!roll-table
`1d12+1d8` Events in the Distant Wilds
2,You find a small village, cut off from civilisation, but welcoming and safe nonetheless.
3,You encounter a small band of hostile monsters.
4,The weather takes a turn for the better, letting you make out landmarks and navigate more easily.
5,You find an adventurer's camp, you're welcome to share the fire and food.
6,You have good luck foraging and find more food than you'd hoped.
7,You see the ruins of a building in the distance.  It's not on your map.
8,You find the old tracks of a large and dangerous monster.
9,You come across a merchant / apothecarist / etc, and their guards, gathering rare materials.
10,You find some treasure.
11,You find a sheltered spot out of the weather and with good visibility, large enough to establish camp.
12,You find some booby-trapped treasure.
13,You come across the remains of an unfortunate merchant / apothecarist / etc, and their guards.
14,You find the fresh tracks of a large and dangerous monster.
15,You see the ruins of a building in the distance.  It's not on your map.
16,While skinning some animals you trapped, you're interrupted by hungry predators!
17,You find a bandit camp.  It's occupied.
18,The terrain doesn't match what you prepared for.  In dealing with it, you become lost.
19,You meet an intelligent monster in a friendly mood.
20,You find a stone stairway leading down into the Earth.
