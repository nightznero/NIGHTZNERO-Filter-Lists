def find_duplicates(file_path):
    """
    Analyze a file for exact 1:1 duplicate rules.
    
    Args:
        file_path (str): The path to the file to analyze.
    """
    with open(file_path, 'r') as file:
        rules = file.readlines()
    
    duplicates = set()
    seen = set()
    
    for rule in rules:
        rule = rule.strip()  # Clean whitespace
        if rule in seen:
            duplicates.add(rule)
        else:
            seen.add(rule)
    
    return duplicates

# Example usage:
# duplicates = find_duplicates('Cosmetic-Rules')
# print(duplicates)