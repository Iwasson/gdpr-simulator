from analytics import display_histogram
from database_seeder import seed_db

def most_frequent(list):
    if not list:
        return None, 0
    counts = {}
    max_occurrences = 0
    most_frequent_num = None

    for num in list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        
        if counts[num] > max_occurrences:
            max_occurrences = counts[num]
            most_frequent_num = num

    return most_frequent_num, max_occurrences

def main():
  data = seed_db(100, 10, 3)
  print(data)

  print(most_frequent(data))
  display_histogram(data)

if __name__ == '__main__':
    main()