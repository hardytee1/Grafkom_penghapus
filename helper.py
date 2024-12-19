def convert_obj_indices(input_file, output_file):
    """Converts OBJ quadrilateral faces to triangulated indices (zero-based) and writes to a file."""

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('f '):  # Process only face lines
                    indices = []
                    vertices = line.strip().split()[1:]  # Extract vertex data

                    for v in vertices:
                        # Extract the vertex index (the first number before the '/')
                        try:
                            v_index = int(v.split('/')[0]) - 1  # Convert to zero-based
                            indices.append(v_index)
                        except (ValueError, IndexError):
                            print(f"Warning: Skipping invalid vertex data: {v}")


                    if len(indices) == 4:
                        # Triangulate the quadrilateral
                        outfile.write(f"{indices[0]}, {indices[1]}, {indices[2]},\n")
                        outfile.write(f"{indices[2]}, {indices[3]}, {indices[0]},\n")
                    elif len(indices) == 3:
                         outfile.write(f"{indices[0]}, {indices[1]}, {indices[2]},\n")                        
                    else:
                        print(f"Warning: Skipping face with unsupported number of vertices: {line.strip()}")



    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

def convert_obj_data(input_file, output_file):
    """
    Converts OBJ data, including vertex reordering (with negative Z) and 
    face triangulation, and writes to a file.
    """

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('v '):  # Process vertex lines
                    parts = line.strip().split()[1:]
                    try:
                        x, y, z = map(float, parts)
                        outfile.write(f"{x}, {-z}, {y},\n") # Negative Z here
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping invalid vertex data: {line.strip()}")

                elif line.startswith('f '):  # Process face lines
                    indices = []
                    vertices = line.strip().split()[1:]
                    for v in vertices:
                        try:
                            v_index = int(v.split('/')[0]) - 1
                            indices.append(v_index)
                        except (ValueError, IndexError):
                            print(f"Warning: Skipping invalid vertex data: {v}")

                    if len(indices) == 4:
                        outfile.write(f"{indices[0]}, {indices[1]}, {indices[2]},\n")
                        outfile.write(f"{indices[2]}, {indices[3]}, {indices[0]},\n")
                    elif len(indices) == 3:
                        outfile.write(f"{indices[0]}, {indices[1]}, {indices[2]},\n")                    
                    else:
                        print(f"Warning: Skipping face with unsupported number of vertices: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

# Example usage:
input_obj_file = "input.txt"  # Replace with your input OBJ / txt file
output_index_file = "outputf.txt"  # Replace with your desired output file name
output_vertice_file = "outputv.txt"  # Replace with your desired output file name
convert_obj_indices(input_obj_file, output_index_file)
convert_obj_data(input_obj_file, output_vertice_file)

print(f"Indices written to '{output_index_file}'.")
print(f"Converted data written to '{output_vertice_file}'.")