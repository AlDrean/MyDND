import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import re

def parse_damage_dice(damage_dice):
    dice_parts = re.findall(r'(\d+d\d+)', damage_dice)
    bonus_part = re.findall(r'\+(\d+)', damage_dice)
    total_average_damage = 0
    for dice in dice_parts:
        num_dice, die_type = map(int, dice.split('d'))
        total_average_damage += num_dice * (die_type + 1) / 2
    if bonus_part:
        total_average_damage += int(bonus_part[0])
    return total_average_damage

def calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage):
    average_damage = parse_damage_dice(damage_dice) + bonus_damage
    hit_chance = max(0, min(1, (21 - max(enemy_ac - attack_bonus, 0)) / 20))
    dpr = hit_chance * average_damage + crit_chance * (average_damage + crit_bonus_damage)
    return dpr

def read_csv_and_calculate_dpr(filepath):
    results = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            character = row['Character']
            attack_bonus = int(row['Attack Bonus'])
            enemy_ac = int(row['Enemy AC'])
            damage_dice = row['Damage Dice']
            bonus_damage = int(row['Bonus Damage'])
            crit_chance = float(row['Critical Hit Chance'])
            crit_bonus_damage = int(row['Critical Bonus Damage'])
            dpr = calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage)
            if character in results:
                results[character] += dpr
            else:
                results[character] = dpr
    return list(results.items())

def plot_dpr(results, turns=5, output_path='dpr_plot.png', include_total=False):
    fig, ax = plt.subplots()
    total_dpr_per_turn = np.zeros(turns)
    for character, dpr in results:
        cumulative_damage = np.arange(start=dpr, stop=dpr*turns+dpr, step=dpr)
        ax.plot(cumulative_damage, label=f"{character} (Total DPR: {dpr:.2f})")
        if include_total:
            total_dpr_per_turn += cumulative_damage
    if include_total:
        ax.plot(total_dpr_per_turn, label="Total Damage", linestyle='--', color='black')
    ax.set_xlabel('Turn')
    ax.set_ylabel('Cumulative Damage')
    ax.set_title('Cumulative Damage Per Turn for Each Character' + (' and Total' if include_total else ''))
    ax.legend()
    plt.savefig(output_path)
    plt.close(fig)  # Close the figure to free memory

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dpr_graph.py input.csv [--total]")
    else:
        csv_file_path = sys.argv[1]
        include_total = '--total' in sys.argv
        results = read_csv_and_calculate_dpr(csv_file_path)
        output_file_path = csv_file_path.replace('.csv', '_dpr_plot.png')
        plot_dpr(results, output_path=output_file_path, include_total=include_total)
        print(f"Graph saved as {output_file_path}")
