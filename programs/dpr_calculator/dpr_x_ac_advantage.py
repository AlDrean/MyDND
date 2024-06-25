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
    return total_average_damage, total_bonus

def calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage, advantage=False):
    average_dice_damage, fixed_bonus_damage = parse_damage_dice(damage_dice)
    average_damage = average_dice_damage + fixed_bonus_damage + bonus_damage
    miss_chance = max(0, (enemy_ac - attack_bonus) / 20)
    if advantage:
        hit_chance = 1 - miss_chance**2  # Adjust hit chance for advantage
    else:
        hit_chance = max(0, 1 - miss_chance)
    expected_damage = hit_chance * average_damage
    expected_crit_bonus = crit_chance * (average_damage + crit_bonus_damage)
    dpr = expected_damage + expected_crit_bonus
    return dpr

def generate_dpr_curves(filepath, advantage=False):
    results = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            character = row['Character']
            attack_bonus = int(row['Attack Bonus'])
            damage_dice = row['Damage Dice']
            bonus_damage = int(row['Bonus Damage'])
            crit_chance = float(row['Critical Hit Chance'])
            crit_bonus_damage = int(row['Critical Bonus Damage'])
            if character not in results:
                results[character] = []
            for enemy_ac in range(10, 31):  # Plotting from AC 10 to AC 30 in increments of 1
                dpr = calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage, advantage)
                results[character].append((enemy_ac, dpr))
    return results

def plot_dpr_curves(results, output_path='dpr_vs_ac_plot.png'):
    fig, ax = plt.subplots(figsize=(15, 6))
    for character, ac_dpr_pairs in results.items():
        ac_values, dpr_values = zip(*ac_dpr_pairs)
        ax.plot(ac_values, dpr_values, label=f"{character} {'with Advantage' if advantage else ''}")
    ax.set_xlabel('Enemy AC')
    ax.set_ylabel('Damage Per Round (DPR)')
    ax.set_title('DPR vs. Enemy AC for Each Character' + (' with Advantage' if advantage else ''))
    ax.legend()
    plt.savefig(output_path)
    plt.close(fig)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py input.csv [--advantage]")
    else:
        csv_file_path = sys.argv[1]
        advantage_flag = '--advantage' in sys.argv
        results = generate_dpr_curves(csv_file_path, advantage=advantage_flag)
        output_file_path = csv_file_path.replace('.csv', f'_dpr_vs_ac_plot{"_adv" if advantage_flag else ""}.png')
        plot_dpr_curves(results, output_path=output_file_path)
        print(f"Graph saved as {output_file_path}")
