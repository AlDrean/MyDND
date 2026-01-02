# Paladin Homebrew Concept

## Introduction
The objective of this homebrew is to transform the Paladin class from a primary damage dealer into a control-oriented tank. This version of the Paladin aims to serve as a beacon of hope and morale on the battlefield, inspiring allies through steadfast faith and strategic control rather than sheer offensive power.

## Objectives
1. **Enhance Utility:** Improve the Paladin's utility, particularly at lower levels, to enhance gameplay experience.
2. **Faith and Inspiration:** Align the Paladin more closely with their beliefs, making them an inspirational figure to allies.
3. **Diverse Gameplay:** Allow players to choose between the utility-focused Paladin and the 4th edition Avenger-style Paladin.
4. **Roleplay Flexibility:** Increase opportunities for roleplay decisions affecting gameplay.
5. **Stat Adjustments:** Consider adjusting core stats to better fit the new class dynamics.
6. **Personal Touch:** Make Waki happy with the changes.

## Disclaimers
- **Iterative Changes:** Not all changes will be implemented simultaneously; some ideas may be discarded while others may be added over time.
- **Balance Concerns:** Adjustments to the class may indirectly enhance other classes, especially spellcasters, due to changes in dynamics like rest periods and resource recovery.
- **Long rests power:** its a known concern that the Log rests are powerfull and this is not taking it to acount in the changes;
- **I don't have deep lore knologe:** I'm trying to have fun. The learning is commig as i go
## Proposed Changes

### Change Flavor
- **Context:** The origin of the power of the paladin is oath but its kind of strange; this change tries to address this
- **Description:** The paladin is a being that have a commitment to one aspect of his life. It takes it higher than anyone, in a way that the word recognizes this as an oath of its life, and benefitis it with the power to be blesses from the Gods. Its now a tool of the world, branding a commitment that will change the word in a way or another. This will turns in a Oath, that makes a standing of your reason to live and your part at the word's will;
- **Proposed Modification:** change the origin of the powers of the paladin  
- **To Do:**
  - **Talk with more paladins players** 

### Change divine smite
- **Context:** As we are changing power from the divine smite and the lore justifying its power, i want to make a mechanical change to improve tematically the use of divine smite; this way i can increase the power and create more epic moments;
- **Proposed Modification:** Either make its calling conditional to be against your oath or difficulty, or be used on channel divinity  
- **To Do:** playtest
  - **Talk with more paladins players** It sounds like a good change, but it also takes away the 'ITS AN AMAZING MOMENT TO CRITICAL SMITE AT LVL 5'

### Class feature: Protect formation (UA)
- **Context:** As for now, the Paladin should have"Hold The line" oriented playstile. As for now, it only goes headfirst to smite and delete a foe. This will be aimed to change it to allow to muster the Sentinel feat;
- **Description:** As a bonus action, enter a defensive stance that lasts until the start of your next turn. While in this stance, make opportunity attacks without using your reaction
- **Proposed Modification:** Consider adding effects like bonus AC or disadvantage on attacks against allies when you are ready to defend. 
- **To Do:**
  - **Test Impact:** Evaluate how adding AC or imposing disadvantage affects gameplay balance, especially in conjunction with abilities like Sentinel. 
  - **Test Impact:** Evaluate giving this the sentinel aspects of the hit so the sentinel is not a must pick feat

### Aura Passiveness and Identity
- **Context:** Auras are a significant part of the Paladin's toolkit but often do not distinctly define the Paladin's identity. The goal is to rework auras so they play a more active role in the Paladin's playstyle, becoming more central to their identity. This includes making auras scale with Charisma to improve their impact and scalability.
- **Description:** Introduce "Aura of Protection" at level 1 to signify the Paladin's inspiring presence through sheer willpower, providing immediate and scaling benefits to nearby allies.

#### Proposed Modifications
- **Early Oath Auras:** See [Early Game Auras Documentation](early_auras_main.md) for detailed brainstorming and implementation ideas
- **Early Access to Auras:** Introduce a level 1 aura that provides benefits based on the Paladin's Charisma modifier.
  - **Temporary Health Aura:** Grant temporary health equal to 1d2 plus Charisma modifier (minimum of 3) to allies within the aura.
  - **Damage Reduction Aura:** Provide a damage reduction of 1d2, which increases to 1d4 if the Paladin's Charisma modifier is 3 or more.
  - **Bonus to Tests:** Offer a 1d2 bonus to attack rolls or skill checks within the aura, a lesser blessing
  - **SavingThrows:** Offer a 1d2 bonus to attack rolls or skill checks within the aura, a lesser blessing

#### Related Documents
- **[Early Auras Main Document](early_auras_main.md)** - Design philosophy, scaling system, and implementation options
- **[Early Auras Basic Concepts](early_auras_basic_concepts.md)** - The 12 foundational aura concepts with test improvements
- **[Early Auras Creative Effects](early_auras_creative_effects.md)** - World-interactive effects that go beyond simple bonuses
- **[Early Auras Deity Mapping](early_auras_deity_mapping.md)** - Complete mapping of D&D deities to auras across all pantheons

#### Scalability Based on Charisma
To ensure that the auras scale effectively with the Paladin's growth, modify the potency of the auras based on the Charisma modifier:
- **+1 Charisma:** Coin flip (1d2)
- **+2 Charisma:** d4
- **+3 Charisma:** d4 plus coin flip (1d2)
- **+4 Charisma:** Advantage roll (2d6)
- **+5 Charisma:** SumMaximum roll of 2d4 or simple 2d4

#### To Do
- **Test Impact:** Evaluate how the scalability of the auras affects gameplay balance, especially in conjunction with the Paladin's level progression.
- **Annotation:** Consider basic die scaling in function of Charisma for auras. This system will need continuous adjustment and feedback to ensure it enhances the Paladin's role without overpowering the class.

#### Notes
These changes aim to emphasize the Paladin's role as a leader and protector, making their auras a core aspect of their gameplay identity and strategy. Further adjustments may be required based on playtest results.

## Smite Changes

### The Smite for CHAR( char +3 or more)
- **Context:** Change the way smites work so i can increase the usability and nerf the overall damage; There is a Smites_CHAR.md files with the smites changes. This way we can use the controll aspect of the smites, without relying on the divine smite 
- **Proposed Modification:** Instead of multiatack, on lvl 5 you aways atack with a smite ( lore based). You get to add your charisma modifier to the atack roll; 
- **Proposed Modification:** 1 aditional slot of concentration; upkeep cost: moviment and bonus action - can be droped anytime
- **Proposed Modification:** aura changes
- **Proposed Modification:** upcasts focus on ramp up in utility and not in damage (?)
- **To Do:**
  - **Playtest:** test usage


### The Smite for STR( STR +3 or more)
- **Context:** Change the way smites work so i can increase the usability and nerf the overall damage; There is a Smites_str.md files with the smites changes. This way we can use the controll aspect of the smites, without relying on the divine smite 
- **Proposed Modification:**  Instead of multiatack, on lvl 5 you aways atack with a smite ( lore based).  The smite speels have a upcast of +2  
- **Proposed Modification:**  same auras as it is now
- **To Do:**
  - **Playtest:** test usage

#### Notes
- Either you chose 1 or other route for smites; 


### Divine buff?
- **Context:** Divine smite should be used as a breakthrought tool and as such it use should be more important. To the build with charisma, it should have addictional effects, with a moderate baseline power 
- **Proposed Modification:**  Aura gain an active component, scaling with charisma specific from the oath
- **To Do:**
  - **Playtest:** test


## Further Development
This document will continue to evolve as new ideas are tested and feedback is received. Future updates may include more detailed descriptions of new abilities, modifications to existing features, and comprehensive balancing notes.
