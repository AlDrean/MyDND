# Paladin Homebrew - Proposed Changes Diagram

## Core Philosophy Shift
```
┌─────────────────────────────────────────────────────────────┐
│                    CURRENT STATE (5e/5.5e)                  │
│  Primary Role: Damage Dealer                                │
│  Core Mechanic: Divine Smite Spam                           │
│  Playstyle: "Go headfirst, smite, delete foe"              │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    [TRANSFORMATION]
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  PROPOSED STATE (Homebrew)                  │
│  Primary Role: Control-Oriented Tank                        │
│  Core Mechanic: Auras, Protection, Strategic Control       │
│  Playstyle: "Hold the line, inspire allies, control field" │
│  Identity: Beacon of hope and morale                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Change Categories Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PROPOSED CHANGES                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. FLAVOR & LORE                                                   │
│     └─> Power Origin: Oath → World Recognition → Divine Blessing   │
│                                                                     │
│  2. DIVINE SMITE REWORK                                             │
│     ├─> Conditional Use (Oath/Difficulty) OR Channel Divinity     │
│     └─> Make it more epic/momentous                                │
│                                                                     │
│  3. NEW CLASS FEATURE: PROTECT FORMATION                           │
│     └─> Defensive Stance (Bonus Action)                            │
│         • Opportunity attacks without reaction                      │
│         • Possible: +AC or disadvantage vs allies                  │
│         • Possible: Built-in Sentinel aspects                      │
│                                                                     │
│  4. AURA SYSTEM OVERHAUL                                            │
│     ├─> Early Access (Level 1)                                     │
│     ├─> Charisma Scaling                                           │
│     ├─> Active Components                                          │
│     └─> Core Identity Feature                                       │
│                                                                     │
│  5. SMITE SPELLS REWORK                                             │
│     ├─> CHAR Build Path (Charisma +3)                              │
│     └─> STR Build Path (Strength +3)                              │
│                                                                     │
│  6. DIVINE BUFF (New Feature)                                       │
│     └─> Aura active component scaling with Charisma                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Level Progression Changes

```
LEVEL 1
├─ [NEW] Early Aura (Charisma-based)
│   └─ Options: Temp HP / Damage Reduction / Bonus to Tests / Saving Throws
│
├─ Divine Sense (Modified: Uses = 1 + CHA mod)
│
└─ Lay on Hands (Standard)

LEVEL 2
├─ Fighting Style
├─ Spellcasting
└─ Divine Smite (MODIFIED: Conditional or Channel Divinity)

LEVEL 3
├─ Divine Health
├─ Sacred Oath
└─ Channel Divinity

LEVEL 5
├─ [REPLACED] Extra Attack → Smite Integration
│   ├─ CHAR Path: Always attack with smite, +CHA to attack roll
│   └─ STR Path: Always attack with smite, +2 upcast
│
└─ [NEW] Protect Formation (Defensive Stance)

LEVEL 6
├─ Aura of Protection (Standard or Modified)
└─ [NEW] Aura Active Component (CHAR builds)

LEVEL 10
└─ Aura of Courage (Standard or Modified)

LEVEL 11
└─ Improved Divine Smite / Radiant Strikes (Standard or Modified)

LEVEL 14
└─ Cleansing Touch / Restoring Touch (Standard or Modified)

LEVEL 18
└─ Aura Expansion (30 feet)
```

---

## Build Path Decision Tree

```
                    LEVEL 5 DECISION POINT
                            │
                ┌───────────┴───────────┐
                │                       │
         CHARISMA BUILD          STRENGTH BUILD
         (CHA +3 or more)        (STR +3 or more)
                │                       │
    ┌───────────┼───────────┐   ┌──────┼──────┐
    │           │           │   │      │      │
    ▼           ▼           ▼   ▼      ▼      ▼
    
┌─────────────────────┐  ┌─────────────────────┐
│ CHAR BUILD FEATURES │  │ STR BUILD FEATURES  │
├─────────────────────┤  ├─────────────────────┤
│                     │  │                     │
│ • Always smite on   │  │ • Always smite on   │
│   attack (lore)     │  │   attack (lore)     │
│                     │  │                     │
│ • +CHA to attack    │  │ • Smite spells      │
│   roll              │  │   upcast +2         │
│                     │  │                     │
│ • +1 concentration  │  │ • Standard auras    │
│   slot              │  │   (as current)      │
│                     │  │                     │
│ • Upkeep: Movement  │  │                     │
│   + Bonus Action    │  │                     │
│                     │  │                     │
│ • Can drop anytime  │  │                     │
│                     │  │                     │
│ • Modified Auras    │  │                     │
│   (Charisma scaling)│  │                     │
│                     │  │                     │
│ • Upcast focus:     │  │                     │
│   Utility > Damage  │  │                     │
│                     │  │                     │
│ • Divine Smite:     │  │                     │
│   Additional effects│  │                     │
│   (moderate baseline)│  │                     │
│                     │  │                     │
│ • Aura Active       │  │                     │
│   Component         │  │                     │
│   (Oath-specific)   │  │                     │
│                     │  │                     │
└─────────────────────┘  └─────────────────────┘
```

---

## Aura System Scaling

```
CHARISMA MODIFIER → AURA POTENCY

+1 CHA  →  1d2 (Coin flip)
+2 CHA  →  1d4
+3 CHA  →  1d4 + 1d2
+4 CHA  →  Advantage roll (2d6)
+5 CHA  →  Maximum of 2d4 or 2d4 sum

APPLIES TO:
├─ Temporary Health Aura
├─ Damage Reduction Aura
├─ Bonus to Tests Aura
└─ Saving Throws Aura
```

---

## Divine Smite Modification Options

```
┌─────────────────────────────────────────────────────────┐
│              DIVINE SMITE REWORK OPTIONS                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  OPTION A: Conditional Use                             │
│  └─> Only usable against:                              │
│      • Creatures that violate your Oath                │
│      • Creatures of significant difficulty/challenge  │
│                                                         │
│  OPTION B: Channel Divinity Integration                │
│  └─> Divine Smite becomes a Channel Divinity option   │
│      • More limited uses                               │
│      • More impactful when used                        │
│                                                         │
│  CONCERN:                                               │
│  └─> Loses "epic critical smite at level 5" moment    │
│                                                         │
│  GOAL:                                                  │
│  └─> Make it more thematic and create epic moments     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Protect Formation Feature

```
┌─────────────────────────────────────────────────────────┐
│            PROTECT FORMATION (UA - Modified)            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  BASE (UA Tunnel Fighter):                              │
│  • Bonus Action: Enter defensive stance                │
│  • Duration: Until start of next turn                  │
│  • Effect: Opportunity attacks without using reaction   │
│                                                         │
│  PROPOSED ADDITIONS:                                    │
│  ├─> Bonus AC while in stance                          │
│  ├─> Disadvantage on attacks vs allies nearby          │
│  └─> Built-in Sentinel aspects (reduce feat tax)       │
│                                                         │
│  PURPOSE:                                               │
│  └─> Enable "Hold the Line" playstyle                  │
│      Support Sentinel feat functionality               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Smite Spells Comparison

```
┌─────────────────────────────────────────────────────────┐
│              SMITE SPELLS: CHAR vs STR                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CHAR BUILD (Control Focus):                            │
│  └─> Upcast increases utility, not damage               │
│                                                         │
│  STR BUILD (Damage Focus):                              │
│  └─> Upcast increases damage (+2 dice)                 │
│                                                         │
│  EXAMPLE DIFFERENCES:                                    │
│                                                         │
│  Searing Smite:                                         │
│  • CHAR: 1d6 fire + 2d4/turn (control)                 │
│  • STR:  1d10 + 1d6 fire + 1/turn x2 (damage)         │
│                                                         │
│  (See Smites_CHAR.md and Smites_str.md for details)     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Priority & Status

```
┌─────────────────────────────────────────────────────────┐
│              CHANGE STATUS & PRIORITY                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  🔴 HIGH PRIORITY / NEEDS WORK:                         │
│  ├─> Flavor & Lore (needs discussion with players)      │
│  ├─> Divine Smite rework (needs playtest)              │
│  └─> Aura system (needs balance testing)                │
│                                                         │
│  🟡 MEDIUM PRIORITY / IN PROGRESS:                      │
│  ├─> Protect Formation (needs impact testing)           │
│  ├─> CHAR build path (needs playtest)                  │
│  └─> STR build path (needs playtest)                   │
│                                                         │
│  🟢 LOW PRIORITY / FUTURE:                              │
│  └─> Divine Buff feature (conceptual)                   │
│                                                         │
│  ⚠️  CONCERNS TO ADDRESS:                               │
│  ├─> Long rest power (not accounted for)                │
│  ├─> Balance with other classes (especially casters)   │
│  └─> Maintaining epic moments while reducing spam       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Key Relationships

```
┌─────────────────────────────────────────────────────────┐
│                    CORE IDENTITY                            │
│  (Aura System)                                          │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Level 1 Aura │ │ Aura Scaling │ │ Active Aura  │
│ (Early)      │ │ (Charisma)   │ │ Component    │
└──────────────┘ └──────────────┘ └──────────────┘
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Protect      │ │ Smite Rework │ │ Build Path   │
│ Formation    │ │ (Conditional)│ │ (CHAR/STR)   │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## Notes for Development

1. **Iterative Approach**: Not all changes will be implemented at once
2. **Balance Testing**: Each change needs individual and combined testing
3. **Player Feedback**: Critical for flavor changes and epic moment preservation
4. **Lore Learning**: Acknowledged as ongoing process
5. **Long Rest Consideration**: May need to address in future iterations

---

*This diagram is a living document and will be updated as changes are refined and tested.*

