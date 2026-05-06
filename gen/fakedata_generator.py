import csv
from pathlib import Path
from faker import Faker
import random

def generate_fake_data():
    """
    Generate fake data 
    """
    # Initialize Faker
    fake = Faker()
    
    headers = ['First name', 'Last name', 'ID number', 
               'Email address', 'Course total (Real)']
    
    num_rows = 30
    
    # Generate the data
    data = []
     
    for _ in range(num_rows):
        # Generate realistic first and last names
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Generate 6-digit ID number
        id_number = random.randint(100000, 999999)
             
        # Generate email address based on name
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        
        # Generate course total (Real) - values between 0 and 100, with 1 decimal place
        course_total = round(random.uniform(0, 100), 1)
        
        # Add the row to our data
        data.append([
            first_name, last_name, id_number, 
            email, course_total
        ])
    
    return headers, data

def save_to_csv(headers, data, output_path):
    """
    Save generated data to a CSV file 
    """
    # Convert string path to Path object if necessary
    output_path = Path(output_path)
    
    # Create the directory if it doesn't exist (including parent directories)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to csv file
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)
    
    print(f"Fake data successfully generated and saved to: {output_path}")
    print(f"Total rows generated: {len(data)}")

def main():
    """
    Main function to generate fake data
    """
    # Define the output path using pathlib
    output_path = Path("./data/raw/fake/generated_fake_data.csv")
    
    # Generate the fake data
    headers, data = generate_fake_data()
    
    # Save to CSV
    save_to_csv(headers, data, output_path)
    
    # Print first few rows as preview
    print("\nPreview of generated data (first 5 rows):")
    print("-" * 80)
    for i, row in enumerate(data[:5]):
        print(f"Row {i+1}: {row}")
    
    # Print column statistics
    print("\n" + "-" * 80)
    print("Column Statistics:")
    course_totals = [row[4] for row in data]
    print(f"Course Total Range: {min(course_totals):.1f} - {max(course_totals):.1f}")
    print(f"Average Course Total: {sum(course_totals)/len(course_totals):.1f}")

if __name__ == "__main__":
    main()