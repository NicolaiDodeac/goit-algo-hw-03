import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_towers(towers, n):
    clear_screen()
    height = n
    pegs = ['A', 'B', 'C']
    for level in reversed(range(height)):
        for peg in pegs:
            try:
                disk = towers[peg][level]
                print(draw_disk(disk, n), end=' ')
            except IndexError:
                print(draw_disk(0, n), end=' ')
        print()
    print("-" * (n * 6))  # Нижня межа

def draw_disk(size, max_size):
    if size == 0:
        return ' ' * max_size + '|' + ' ' * max_size
    return ' ' * (max_size - size) + '#' * size + '|' + '#' * size + ' ' * (max_size - size)

def move_disk(from_peg, to_peg, towers, n):
    disk = towers[from_peg].pop()
    towers[to_peg].append(disk)
    draw_towers(towers, n)
    print(f"Перемістити диск з {from_peg} на {to_peg}: {disk}")
    time.sleep(1)  # Пауза між кроками

def hanoi(n, source, target, auxiliary, towers, total_disks):
    if n == 1:
        move_disk(source, target, towers, total_disks)
    else:
        hanoi(n - 1, source, auxiliary, target, towers, total_disks)
        move_disk(source, target, towers, total_disks)
        hanoi(n - 1, auxiliary, target, source, towers, total_disks)

def main():
    n = int(input("Введіть кількість дисків (1-7): "))
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    draw_towers(towers, n)
    input("Натисніть Enter, щоб почати...")
    hanoi(n, 'A', 'C', 'B', towers, n)
    print("Завершено!")

if __name__ == "__main__":
    main()
