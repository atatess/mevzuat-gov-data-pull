import os

# Directory containing your text files
directory = "/path"
output_file = '/path.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content + "\n")  # Add a newline to separate files

print(f'All text files concatenated into {output_file}')
