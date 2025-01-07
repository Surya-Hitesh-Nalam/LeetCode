class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        # Initialize an array of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
    
    # Traverse through the string and place characters in corresponding rows
        for char in s:
            rows[current_row] += char
        
        # Change direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
        
        # Move up or down depending on the direction
            current_row += 1 if going_down else -1
    
    # Concatenate all rows to form the final result
        return ''.join(rows)
        