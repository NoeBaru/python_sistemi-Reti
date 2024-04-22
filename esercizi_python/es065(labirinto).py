import random
import csv

def generate_maze(rows, cols):
    maze = [[0] * cols for _ in range(rows)]
    start_row = random.randint(0, rows - 1)
    start_col = random.randint(0, cols - 1)
    maze[start_row][start_col] = 3  # Imposta la partenza

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] != 3:  # Ignora la cella di partenza
                maze[row][col] = random.choice([0, 1])  # Imposta 0 o 1 casualmente

    return maze

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        maze_writer = csv.writer(csvfile)
        for row in maze:
            maze_writer.writerow(row)

def main():
    """
    Author: Noemi Baruffolo
    date: 18/04/2024
    es. 065
    text: far creare a chatGPT un algoritmo che generi labirinti in un file csv seguendo lo stile concordato
    """

    rows = 10
    cols = 10
    maze = generate_maze(rows, cols)
    save_maze_to_csv(maze, 'maze.csv')
    print("Labirinto generato e salvato in 'maze.csv'")

if __name__ == "__main__":
    main()