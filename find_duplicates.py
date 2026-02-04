def find_duplicates(file_path):
    seen = set()
    duplicates = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Skip comment lines
            if line.startswith('#') or line.startswith('!'):
                continue
            if line in seen:
                duplicates.add(line)
            else:
                seen.add(line)
    return duplicates
