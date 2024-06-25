import csv
import matplotlib.pyplot as plt
import sys
import re
import argparse
import os
import numpy as np

def parse_damage_dice(damage_dice):
    """Parse dice notation to calculate average damage."""
    dice_parts = re.findall(r'(\d+d\d+)', damage_dice)
    bonus_parts = re.findall(r'\+(\d+)', damage_dice)
    total_average_damage = 0
    for dice in dice_parts:
        num_dice, die_type = map(int, dice.split('d'))
        total_average_damage += num_dice * (die_type + 1) / 2
    total_bonus = sum(int(bonus) for bonus in bonus_parts)
    return total_average_damage + total_bonus

def calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage_str, advantage):
    """Calculate DPR including effect of advantage."""
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

def read_csv_and_calculate_dpr(filepath):
    """Read CSV and calculate DPR for each character, considering multi-attacks."""
    results = {}
    results_ac_range = {ac: {} for ac in range(10, 31)}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            character = row['Character']
            attack_bonus = int(row['Attack Bonus'])
            enemy_ac = int(row['Enemy AC'])
            damage_dice = row['Damage Dice']
            bonus_damage = int(row['Bonus Damage'])
            crit_chance = float(row['Critical Hit Chance'])
            crit_bonus_damage_str = row['Critical Bonus Damage']
            advantage = row['Advantage']
            
            # Calculate DPR for this attack
            dpr = calculate_dpr(attack_bonus, enemy_ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage_str, advantage)
            
            # Accumulate DPR for each character's attacks
            if character not in results:
                results[character] = {}
            if enemy_ac not in results[character]:
                results[character][enemy_ac] = 0
            results[character][enemy_ac] += dpr

            # Calculate DPR for fixed AC range
            for ac in range(10, 31):
                dpr_ac = calculate_dpr(attack_bonus, ac, damage_dice, bonus_damage, crit_chance, crit_bonus_damage_str, advantage)
                if character not in results_ac_range[ac]:
                    results_ac_range[ac][character] = 0
                results_ac_range[ac][character] += dpr_ac

    return results, results_ac_range

def plot_dpr_vs_ac(results, output_directory):
    """Plot DPR vs. AC based on the CSV data."""
    fig, ax = plt.subplots(figsize=(20, 6))
    for character, data in results.items():
        acs = sorted(data.keys())
        dprs = [data[ac] for ac in acs]
        total_dpr = sum(dprs)
        ax.plot(acs, dprs, label=f'{character} (DPR: {total_dpr:.2f})')
    ax.set_xlabel('Enemy AC')
    ax.set_ylabel('Damage Per Round (DPR)')
    ax.set_title('DPR vs. Enemy AC for Each Character (from CSV)')
    ax.legend()
    plt.savefig(os.path.join(output_directory, 'dpr_vs_ac_csv.png'))
    plt.close(fig)

def plot_dpr_vs_ac_array(results_ac_range, output_directory):
    """Plot DPR vs. AC array from 10 to 30."""
    fig, ax = plt.subplots(figsize=(20, 6))
    for character in results_ac_range[10].keys():  # Assuming all characters have data for the range 10 to 30
        acs = sorted(results_ac_range.keys())
        dprs = [results_ac_range[ac][character] for ac in acs]
        total_dpr = sum(dprs)
        ax.plot(acs, dprs, label=f'{character}')
    ax.set_xlabel('Enemy AC')
    ax.set_ylabel('Damage Per Round (DPR)')
    ax.set_title('DPR vs. Enemy AC Array (10-30) for Each Character')
    ax.legend()
    plt.savefig(os.path.join(output_directory, 'dpr_vs_ac_array.png'))
    plt.close(fig)

def plot_total_damage_per_round(results, turns=5, output_directory='output_plots', include_total=False):
    """Plot Total Damage per Round for each character."""
    fig, ax = plt.subplots(figsize=(20, 6))
    total_dpr_per_turn = np.zeros(turns)
    for character, data in results.items():
        total_dpr = sum([dpr for ac in data for dpr in [data[ac]]])
        cumulative_damage = np.cumsum(np.tile([dpr for ac in data for dpr in [data[ac]]], turns))
        ax.plot(np.arange(1, len(cumulative_damage) + 1), cumulative_damage, label=f"{character} (Total DPR: {total_dpr:.2f})")
        if include_total:
            total_dpr_per_turn += cumulative_damage[:turns]
    if include_total:
        ax.plot(np.arange(1, turns + 1), total_dpr_per_turn, label="Total Damage", linestyle='--', color='black')
    ax.set_xlabel('Turn')
    ax.set_ylabel('Cumulative Damage')
    ax.set_title('Cumulative Damage Per Turn for Each Character' + (' and Total' if include_total else ''))
    ax.legend()
    plt.savefig(os.path.join(output_directory, 'total_damage_per_round.png'))
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate and plot DPR for D&D characters.")
    parser.add_argument("csv_file", help="CSV file with character data")
    parser.add_argument("--total", action="store_true", help="Include total cumulative damage")
    args = parser.parse_args()
    
    csv_file_path = args.csv_file
    include_total = args.total

    # Create output directory based on the input file name
    base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    output_directory = os.path.join(os.getcwd(), base_name)

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Generate DPR curves
    results, results_ac_range = read_csv_and_calculate_dpr(csv_file_path)
    
    # Plot the results
    plot_dpr_vs_ac_array(results_ac_range, output_directory)
    plot_total_damage_per_round(results, turns=5, output_directory=output_directory, include_total=include_total)
    print(f"Graphs saved in {output_directory}")
