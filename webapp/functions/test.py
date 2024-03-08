from analytics import display_histogram
from database_seeder import seed_db

def main():
  data = seed_db(100, 10, .7)
  print(data)
  display_histogram(data)

if __name__ == '__main__':
    main()