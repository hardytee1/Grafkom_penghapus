def convert_obj_vertices(input_file, output_file):
    """Converts OBJ vertex data (with negative Z) and writes to a file."""
    vertices = []
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('v '):  # Process vertex lines
                    parts = line.strip().split()[1:]
                    try:
                        x, y, z = map(float, parts)
                        vertices.append((x, -z, y))  # Negative Z here
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping invalid vertex data: {line.strip()}")

            for vertex in vertices:
                outfile.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")


def convert_obj_texture_coords(input_file, output_file):
    """Converts OBJ texture coordinates (vt) and writes to a file."""
    texture_coords = []
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('vt '):  # Process texture coordinate lines
                    parts = line.strip().split()[1:]
                    try:
                        u, v = map(float, parts)
                        texture_coords.append((u, v))
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping invalid texture data: {line.strip()}")

            for uv in texture_coords:
                outfile.write(f"vt {uv[0]} {uv[1]}\n")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")


def convert_obj_normals(input_file, output_file):
    """Converts OBJ normal vectors (vn) and writes to a file."""
    normals = []
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('vn '):  # Process normal vector lines
                    parts = line.strip().split()[1:]
                    try:
                        nx, ny, nz = map(float, parts)
                        normals.append((nx, ny, nz))
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping invalid normal data: {line.strip()}")

            for normal in normals:
                outfile.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")


def convert_obj_indices(input_file, output_file):
    """Converts OBJ quadrilateral faces to triangulated indices (zero-based) and writes to a file."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('f '):  # Process only face lines
                    indices = []
                    vertices = line.strip().split()[1:]  # Extract vertex data

                    for v in vertices:
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


# Example usage:
input_obj_file = "input.txt"  # Replace with your input OBJ file

# Output files for each part
output_vertices_file = "vertices_output.txt"
output_texture_coords_file = "texture_coords_output.txt"
output_normals_file = "normals_output.txt"
output_indices_file = "indices_output.txt"

# Call each function to convert the respective data
convert_obj_vertices(input_obj_file, output_vertices_file)
convert_obj_texture_coords(input_obj_file, output_texture_coords_file)
convert_obj_normals(input_obj_file, output_normals_file)
convert_obj_indices(input_obj_file, output_indices_file)

print(f"Vertices written to '{output_vertices_file}'.")
print(f"Texture coordinates written to '{output_texture_coords_file}'.")
print(f"Normals written to '{output_normals_file}'.")
print(f"Indices written to '{output_indices_file}'.")
