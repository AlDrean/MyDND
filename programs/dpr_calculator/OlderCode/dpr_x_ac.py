import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import re

def parse_damage_dice(damage_dice):
    dice_parts = re.findall(r'(\d+d\d+)', damage_dice)
    bonus_parts = re.findall(r'\+(\d+)', damage_dice)
    total_average_damage = 0
    for dice in dice_parts:
        num_dice, die_type = map(int, dice.split('d'))
        total_average_damage += num_dice * (die_type + 1) / 2
    total_bonus = sum(int(bonus) for bonus in bonus_parts)
    return total_average_damage + total_bonus

def calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage_str, advantage=False):
    average_dice_damage = parse_damage_dice(damage_dice)
    crit_bonus_damage = parse_damage_dice(crit_bonus_damage_str)
    average_damage = average_dice_damage + bonus_damage
    threshold = enemy_ac - attack_bonus + 1
    miss_chance = max(0, threshold / 20)
    
    if advantage == 'True':
        hit_chance = 1 - (miss_chance ** 2)
    else:
        hit_chance = 1 - miss_chance

    expected_damage = hit_chance * average_damage
    expected_crit_bonus = crit_chance * (average_damage + crit_bonus_damage)
    dpr = expected_damage + expected_crit_bonus
    return dpr

def generate_dpr_curves(filepath):
    results = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            character = row['Character']
            attack_bonus = int(row['Attack Bonus'])
            damage_dice = row['Damage Dice']
            bonus_damage = int(row['Bonus Damage'])
            crit_chance = float(row['Critical Hit Chance'])
            crit_bonus_damage_str = row['Critical Bonus Damage']
            advantage = row['Advantage']
            if character not in results:
                results[character] = []
            for enemy_ac in range(10, 25):
                dpr = calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage_str, advantage)
                results[character].append((enemy_ac, dpr))
    return results

def plot_dpr_curves(results, output_path='dpr_vs_ac_plot.png'):
    fig, ax = plt.subplots(figsize=(20, 6))
    for character, ac_dpr_pairs in results.items():
        ac_values, dpr_values = zip(*ac_dpr_pairs)
        ax.plot(ac_values, dpr_values, label=character)
    ax.set_xlabel('Enemy AC')
    ax.set_ylabel('Damage Per Round (DPR)')
    ax.set_title('DPR vs. Enemy AC for Each Character')
    ax.legend()
    plt.savefig(output_path)
    plt.close(fig)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py input.csv")
    else:
        csv_file_path = sys.argv[1]
        results = generate_dpr_curves(csv_file_path)
        output_file_path = csv_file_path.replace('.csv', '_dpr_vs_ac_plot.png')
        plot_dpr_curves(results, output_path=output_file_path)
        print(f"Graph saved as {output_file_path}")
