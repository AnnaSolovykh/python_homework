
"""
Task 5: Extending a Class
"""

import pandas as pd

# Task 5.2 & 5.3: Create DFPlus class that inherits from pandas DataFrame
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus
    
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    # Task 5.4: Method to print DataFrame with headers every 10 lines
    def print_with_headers(self):
        total_rows = len(self)
        
        print(f"DataFrame with {total_rows} rows:")
        print("=" * 60)
        
        # Loop through DataFrame in chunks of 10 rows
        for start_row in range(0, total_rows, 10):
            # Calculate end row for current chunk
            end_row = min(start_row + 10, total_rows)
            
            print(f"\nRows {start_row + 1} to {end_row}:")
            
            # Get slice of 10 rows using iloc
            chunk = super().iloc[start_row:end_row]
            
            print(chunk)
            
            # Add spacing between chunks for readability
            if end_row < total_rows:
                print("\n" + "." * 40)


# Task 5.6: Create DFPlus instance from CSV file
if __name__ == "__main__":    
    dfp = DFPlus.from_csv("../csv/products.csv")

    print("\nPRINTING WITH HEADERS EVERY 10 LINES:")
    dfp.print_with_headers()
    