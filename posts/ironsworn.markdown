---
title: "Ironsworn: A Tabletop RPG of Perilous Quests"
date: 2024-01-29
topic: reviews
system: ironsworn
---

I've been playing a lot of [Ironsworn][] recently.  It's a solo roleplaying game
in a kind of low-ish fantasy frontier Viking setting, where you play someone who
undertakes perilous quests and goes on dangerous journeys, all to fulfil their
sworn vows.

Also, [it's free][], which is a hard price to beat.

In my first game I played a hunter called Delkash, from a settlement on the
outskirts of a region of dense, untamed forest called the Deep Wilds.  His
"background vow"---that is, the thing which drives the whole campaign---was to
**forge a bond of friendship with the elves of the Deep Wilds**.  Delkash had
never seen an elf before, but he'd heard legends, and he respected them as a
people who had found a way to live in harmony with this inhospitable
monster-filled forest.

The inciting incident of the campaign was a raid on his village.  He came home
from a hunt to find buildings on fire and people gone, his sister amongst them,
so his second vow (every [abbr:pc] starts with two vows: a big one and a small
one) was to **rescue my sister from the raiders**.

Unfortunately, Delkash ended up being stabbed in the gut in a fight with one of
these raiders and bleeding out on the road, after spending a few weeks living
amongst them as a hunter (after being captured himself, but proving useful
enough to not be killed or sold into slavery) trying to slowly earn their trust,
to set himself up in a position where he could challenge their leader for
supremacy.

Alas, plans don't always work out.

Beyond the free base game, which is eminently playable by itself, there's a paid
supplement adding optional rules for site-based adventuring (pointcrawls), magic
items, and "threats" (major obstacles with their own agency), and another
supplement reskinning Ironsworn for sci-fi.

[Ironsworn]: https://www.ironswornrpg.com/
[it's free]: https://www.ironswornrpg.com/buy


## How it works

![A flowchart showing the Ironsworn game loop](ironsworn/flowchart.png)

Ironsworn supports three modes of play:

- **Guided:** This is traditional [abbr:gm "GMed"] play with one player taking
  the role of the world and all of its inhabitants, with the other players each
  controlling a single [abbr:pc].

- **Co-op:** Where there are multiple players each with their own [abbr:pc], but
  there is no [abbr:gm].  Details of the world are resolved through random
  oracles and just thinking about what would be cool.

- **Solo:** Which is co-op if you have no friends to play with.

I've only tried solo.

A [abbr:pc] in Ironsworn is made up of five stats with values from +1 to +3:

- **Edge:** Quickness, agility, and prowess in ranged combat.
- **Heart:** Courage, willpower, empathy, sociability, and loyalty.
- **Iron:** Physical strength, endurance, aggressiveness, and prowess in close
  combat.
- **Shadow:** Sneakiness, deception, and cunning.
- **Wits:** Expertise, knowledge, and observation.

There are also three health tracks, which go from +0 to +5:

- **Health:** Your physical state.
- **Spirit:** Your mental state.
- **Supply:** Your food, water, ammo, etc.

Most rolls in the game are you rolling `d6 + STAT` and comparing to two `d10`
rolls: if you roll *over* both, you get a "strong hit", if you roll over only
one of them, you get a "weak hit", and if you roll equal to or under both, you
get a "miss".  There are rolls that use your Health, Spirit, or Supply, but
they're in the minority.

If both `d10` rolls show the same number, you get an extra-special outcome.

It should be readily apparent that if the stat bonuses only go up to +3 (or +5
in some cases), weak hits are the norm.  That's intentional.  Ironsworn borrows
the "move" structure of [abbr:pbta] games, with the guiding principle that rolls
should tend to introduce new elements into the narrative.  I'm generally not a
fan of moves (I prefer rules to operate at the level of the character, not at
the level of the narrative), but in this case I think they work really well.
Playing a solo game isn't like playing a regular game: you're still a player,
but also something of a writer.

![The "Face Danger" move](ironsworn/move.png)

But you've got a few
ways to improve your odds of success.

The main way is **momentum**, a resource you gain from successful rolls, and can
spend to cancel out `d10`s lower than your current momentum score.  But momentum
can also go negative, which cancels out your `d6`!  So when you're on a roll and
everything's going well and your momentum is high, you feel like you can take on
anything!  But when you're having a streak of bad luck, and your momentum is
getting lower and lower, you really feel like you need to escape to a safe place
and spend a while recuperating.

The other big lever you've got is that Ironsworn is a *narrative* game.  When
things go badly, *you* decide what that means.  Mechanical consequences, such as
taking damage, might be appropriate.  But it might be just as bad to get
disarmed, or offend an important [abbr:npc], or even just have a bad night's
sleep and be tired the following day.  It's up to you to bring these
non-mechanical consequences into the game, and let their consequences snowball:
if you've offended an important [abbr:npc], you'll need to repair that
relationship somehow before you can ask them for a favour; if you're tired from
a bad night's sleep and get into a fight, maybe you *do* start taking damage
from the get-go, as you're not able to properly defend yourself.

### Vows

Vows are the driving force behind the whole game.  Your character starts play
with two vows, and completing a vow gives you experience points you can spend to
improve your character or buy new abilities.

The book is full of inspiration.  The chapters about the world and about foes
have lots of little "quest starters" that could easily be the seed for a vow.
For example:

> An Ironlander has sided with an enemy in the heart of the Wilds, and is
> leading attacks against Ironlander settlements.  Who is this person?  Who have
> they joined forces with?  What will you do to stop these attacks?

Sounds like the basis for a great inciting incident vow to me: "save my people
from the evil so-and-so".  Or maybe even a background vow if this is some major
foe and the whole campaign is about finding a way to overcome their defenses and
thwart them.

### Pacing

How do you know when you've done enough to complete a vow?  Or when you've
finished a long journey to an uncertain endpoint?  Or beaten an enemy into
submission?  Progress trackers.

![An empty progress tracker](ironsworn/progress.png)

A progress tracker has 10 boxes and a rank, ranging from "troublesome" (the
least obstacle worth tracking) and "epic" (a campaign-defining foe), and every
time you make progress towards dealing with the obstacle you tick a number of
boxes based on the rank.  Ironsworn uses progress trackers for:

- Combat, where inflicting harm on the foe grants progress.
- Journeys, where succssfully finding waypoints gives progress.
- Vows, where progress is determined entirely narratively as you wish.

For the Ironsworn Delve supplement which adds site-based adventures, exploration
of a site gets a progress tracker too.

Now, here's the clever part.  You don't need to fill up a progress track to
successfully do the thing, in fact, filling up the progress track doesn't even
mean you did the thing.  The progress tracker represents how close you are to
your goal, but you still need to *make a move* to reach it.  These "progress
moves" are risky: you just roll two `d10`s and compare to the progress score,
with no `d6` and no modifiers.

This means you *always* have a chance to get a weak hit or a miss, since there
are only 10 boxes and you could roll 10s.  But equally, so long as you can
narratively justify it, you could try to rush towards your objective when you
don't actually have much on the progress tracker: that's risky, you're much more
likely to fail completely, but the cost of making further progress might be too
high.

### Oracles

The rules are great, but they wouldn't be worth anything without the wealth of
inspiration that this game has in the form of random oracles.

The base game has oracles for:

- Actions and themes: when you want to just get some high-level inspiration like
  "Summon Enemy" or "Explore Danger"
- Regions, land-based locations, coastal locations, and location descriptors:
  when you want to put something somewhere random, or come up with some detail
  of where you find yourself or what you find there.
- Settlement names and troubles: every settlement has a trouble (and can solving
  that trouble become a vow?)
- Character names (for a variety of races), goals, descriptors, and roles: maybe
  you meet a hot-tempered guard called Masias who is trying to avenge a wrong
  (maybe that can be tied into a nearby settlement's trouble? or can they become
  a recurring character?)
- Combat actions, magical side-effects, and major plot twists: when you just
  want the narrative to do *something* unexpected.
- Challenge rank: when you're not sure just how difficult crossing the
  monster-filled forest should be.

Of course, oracles don't automate the game for you.  You still need a human
brain to see what the oracle gives you and work that into the narrative somehow,
maybe even disregarding the result and coming up with something more fitting.
The oracles give you inspiration, they're not the [abbr:gm] and they're not a
straightjacket.


## Sabine, witch-hopeful

Let's play a session of Ironsworn together.  Here's the state of my current
game:

![A screenshot of my Ironsworn Miro board](ironsworn/sabine.png)

I'm using Miro as a virtual tabletop.  Open the image in a new tab to make it
bigger.

My character is called **Sabine**.  She's "intelligent, fanatically craves lost
lore, and isn't above using deceit to get it."  Her background vow is to
**become a witch**.  I decided that magic is generally thought to be folklore
and myth in this world, but Sabine thinks there's some truth to those old
stories.

She has three **assets**, which you freely pick at character creation and then
have to buy or upgrade with experience points.  Her assets are: **Lorekeeper**,
she's the keeper of some sort of mystical archive (I've not yet decided what
form that takes, it might just be a house full of books); **Trickster**,
representing her willingness to lie to get what she wants; and a companion, a
**Raven** called Miskunn, who can carry messages.

She has three **bonds** too, important NPCs which you also get for free in
character creation, but new bonds have to be won over with the *Forge a Bond*
move.  They are: **Eleri**, a pilgrim to forgotten holy places, more comfortable
in the wilds than a settlement; **Ranna**, an ex-raider seeking absolution for
her sins; and **Chandra**, an outcast who hunts dangerous beasts to keep the
roads safe.

I rolled up all these character descriptions.  Obviously the oracles weren't as
specific as that, but inspiration struck.

I've played three sessions so far, that's the different shaded blue post-its on
the board:

- **Session 1:** I set up the game and decided on the inciting incident.  A
  raven arrived from Eleri, bearing a message saying he had heard rumours of an
  abandoned druid grove in the Flooded Lands, and proposed we meet up at the
  nearby ruins of an abandoned settlement to set out in search of this grove.

- **Session 2:** We (Eleri and Sabine) journeyed through the Flooded Lands and,
  after several days, with supplies starting to run low, found our objective: a
  dense forest, on a patch of dry land rising out of the bog, surrounded by and
  spilling out beyond an old circle of rune-carven standing stones.

- **Session 3:** We went into the trees, looking for some remnant of the druids
  of old.  We were hunted by some sort of shrieking beast, but evaded it, and
  eventually arrived at the heart of the grove.  There before us we beheld an
  enormous silvery obelisk, jagged and cracked with age, covered in runes... and
  were confronted by the guardian of the obelisk, a mysterious man who called
  himself "the Audrune Bretana".  After a brief tense standoff, he said he would
  tell us "some of the lesser secrets of my people" if we would do what he could
  not: leave the grove, and destroy a "rune of hate" that attracted the
  shrieking beast and keeps it here, the beast that killed all the other druids.

So let's pick it up from there!  I am going to be referencing the non-free
Ironsworn Delve rules, but you should be able to follow along.  Here follows
stream-of-consciousness rambling as I deal with the rune of hate and learn the
secrets of the druids:

- **First of all, I want to know what time of day it is.**  I think it's
  probably evening.  We set off in the morning, we spent a long time trying to
  force our way through the dense tangled trees.

    Let's call this "likely" and roll on the oracle: 75, yes, it is evening.
    Not good light for rune-hunting but Bretana doesn't seem like he's offering
    us a place to stay.

    I'm going to make an *Escape the Depths* roll to see if Sabine and Eleri
    make it out safe.  We know there's a beast so I think we're being stealthy,
    so this is with Shadow: 7 (5+2) vs 4 and 10, a weak hit.  I think they're
    just getting tired, getting scratched and scraped by the plant life, so
    they're going to *Endure Harm*.  Just 1 harm.  That puts Sabine at 4 Health,
    and I roll a 6 vs two 6s, a miss and and a match!  I could spend Momentum
    but I'm not going to, so I'll take -1 Momentum (bringing me down to +8) and
    for the match let's just roll to *Pay the Price* which isn't normally a
    consequence of *Endure Harm*: 53, "it causes a delay or puts you at a
    disadvantage".

    I think it's full night when they finally make it out of the grove, and
    there's also thick cloud cover.  It is really dark.

    ![A post-it note summarising this bullet.](ironsworn/sabine-4.1.png)

- **Next, we need to find this rune.**  I don't even know what it is, I just
  called it a "rune of hate" because I was kind of going for a runic theme with
  these druids and it's a cool name that sprung to mind.  It must be a physical
  thing if Bretana thinks they have a chance at destroying it, but I don't think
  it's obvious, that would be too easy, I'm not even going to consult the oracle
  for that.

    I could use the journey moves for this, but I don't want to: the rune is
    nearby, Bretana said somewhere with a clear line of sight to the grove.

    Another issue comes to mind though, Sabine isn't alone.  Eleri's here.
    Eleri is a weirdo, make no mistake, but he's not quite so driven to find
    magic as Sabine.  Is he going to insist they make camp and try in the
    morning?  Let's call it 50 / 50: 29, no, he's willing to keep searching
    tonight.

    So Sabine and Eleri light torches and start searching the surrounding bog,
    shouting so they don't lose track of each other, stopping and checking their
    line of sight to the grove every now and then.  It's dark, wet, cold, they
    have scrapes and stings, this is a truly unpleasant situation.  Eleri is a
    really good friend, it should probably have been more likely than a 50 / 50
    chance, oh well...

    Searching an area is a *Gather Information* roll, which is with Wits: a weak
    hit.  So I do learn something, and get +1 Momentum, but there's a
    complication or danger.  I think it's probably trapped, that feels right, so
    let's roll on the Ironsworn Delve trap random tables: "Ambush Weapon".
    Alright, well, that sounds like an arrow trap, or a swinging blade, or just
    a pit with spikes.  Probably a pit with spikes, we're outdoors.

    I didn't roll a miss, so neither Sabine nor Eleri are caught in the trap, but
    it is in their way.

    ![A post-it note summarising this bullet.](ironsworn/sabine-4.2.png)

- **"Become a witch" is Sabine's background vow.**  She's obsessed with learning
  about magic.  She wants that rune-etched rock.  So she's going to instantly
  veto any suggestion by Eleri that they just throw rocks or something at it to
  smash it.

    Making her way across a spike-lined pit-trap and climbing a tree sounds like
    *Face Danger* with Edge, but physical agility really isn't Sabine's strong
    point.  But hey, I've got +9 momentum now; surely this is the time to burn
    it.  If she gets the rune I'll even count that as progress towards the vow.

    Let's do it!  6 vs 4 and 1, a strong hit without needing to spend any
    momentum!  She spots a fallen tree trunk or something and rolls it into the
    pit trap, letting her climb across and then get up the tree without much
    difficulty at all!  She snags that rune, and marks one tick of progress (a
    quarter of a box) towards her background vow.  Now she's at +10 Momentum.

    ![A post-it note summarising this bullet.](ironsworn/sabine-4.3.png)

- **That's definitely a complication.** Curse you, Eleri, for reminding me.  I
  think Sabine's first instinct is to keep the rune secret and lie to Bretana
  that they destroyed it.  Eleri is definitely going to object to this, so she
  needs to *Compel* him to go along with this plan.  I don't get the benefits of
  the *Trickster* asset here because Eleri knows what's going on, but I will get
  it when lying to Bretana.

    I think Sabine's got to persuade Eleri with Heart.  She's trying to convince
    him that this is ok, not trying to threaten or deceive him.  So she'll get a
    +1 from their bond.  Before we roll the dice, I'm going to decide not to
    spend Momentum on this if I fail.  If I fail Sabine will study it for a few
    hours and make careful notes on it, but then will let Eleri smash it.
    And... I get a weak hit!  Eleri is going to go along with this, but wants
    something in return.

    I think what he wants is for Sabine to at least try to make do without
    keeping the physical object intact.  There isn't really a "study an object"
    move, and while I could just ask the oracle what happens I think it's more
    interesting if there's a chance of something going badly wrong (like poking
    around with the rune calling for the beast), so I'm going to *Face Danger*
    here.  Regardless of the outcome, Sabine will be exhausted tomorrow as she's
    spending all night studying this while Eleri is sleeping.  It's a strong hit!

    One sleepless night and several pages of notes and diagrams later, Sabine
    watches stoically as Eleri smashes the rune upon a rock.  I don't think
    she'd have been willing to go through with this if it was anyone else
    asking, Eleri and Sabine have a very strong bond.  Perhaps more than a bond?
    We'll see.

    ![A post-it note summarising this bullet.](ironsworn/sabine-4.4.png)

- **I think this is nicely approaching a conclusion** so I'm going to
  fast-forward some of the ending here.  Also, I have an idea for the next step
  which I think is pretty cool, so let's just say that Sabine and Eleri
  carefully make their way back to the glade in which they met Bretana, since
  they're just retracing their steps.  There's no sign of the beast (maybe it
  shrieked really loudly and fled when they smashed the rune?  yeah, that sounds
  good).

    Bretana already said he'd tell them some of the lesser secrets in reward for
    destroying the rune, which they have, and which he knows they have because
    of the aforementioned beast-shriek.  But I don't think he's actually going
    to tell very much, I'm going to roll on the Action and Theme oracles:
    "Command Superstition".

    Well, that's fitting.

    I think Bretana says his people learned their arts from the legendary
    Firstborn: *the elves*.

    That gets some progress towards Sabine's **learn the secrets of the lost
    druid grove** vow, which is now at 8 out of 10.  Let's try to *Fulfil Your
    Vow*!  A strong hit!  Sabine gets 2 experience points and feels she's got
    some good information out of this little adventure.  But how will she go
    about finding some elves?  I guess I'll find out next time, but I think just
    learning that the elves have some knowledge of magic runes is going to give
    another tick of progress towards her **become a witch** vow, so that's now
    at half-a-box out of ten.  A long way to go yet.

    Oh, one final thing... I have an inkling that the druids are a
    pre-Ironlander civilisation, which is why they have contact with the elves,
    who are otherwise aloof and keep their distance from humanity.  Let's call
    it almost certain and ask the oracle: 56, absolutely!

    ![A post-it note summarising this bullet.](ironsworn/sabine-4.5.png)

So, you see that while the rolls determine how well things are going, what
*exactly* happens is still mostly up to the player.  Different moves have
different consequences, but there's still a lot open to interpretation.

When I start my next session I'll have to decide where Sabine goes from
here---does she try to track down the elves? how?---and also whether I'm going
to spend those experience points.  Two points is enough to upgrade one of my
existing assets, but a new asset costs three so I might want to save them.  I
also still have +10 Momentum, which is incredible, so maybe I *should* pick a
big task like **locate an elven settlement**...

Well, that's Ironsworn.  It is pretty fun, and at a price point of "free"
definitely worth checking out.
