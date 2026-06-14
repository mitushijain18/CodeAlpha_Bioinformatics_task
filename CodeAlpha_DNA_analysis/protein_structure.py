import urllib.request
import os

print("🧬 CodeAlpha Bioinformatics Task 3: Protein Structure Prediction Locator")
print("=" * 75)

# We use a globally recognized structural entry from the Protein Data Bank (PDB)
# 1AQL: High-resolution structure of Human Insulin
pdb_id = "1aql"
pdb_filename = f"{pdb_id}.pdb"
download_url = f"https://files.rcsb.org/download/{pdb_filename}"

print(f"📥 Step 1: Downloading 3D structural model data from RCSB PDB Database...")

try:
    # Check if the file is already downloaded locally
    if not os.path.exists(pdb_filename):
        urllib.request.urlretrieve(download_url, pdb_filename)
        print(f"✅ Successfully saved structure file locally: {pdb_filename}")
    else:
        print(f"ℹ️ Local file version '{pdb_filename}' found. Skipping download step.")
        
    print("\n📊 Step 2: Extracting 3D Spatial Atomic Coordinates for the Report...")
    print("-" * 75)
    print(f"{'ATOM TYPE'.ljust(10)} | {'RESIDUE'.ljust(8)} | {'CHAIN'.ljust(6)} | {'X-COORD'.ljust(10)} | {'Y-COORD'.ljust(10)} | {'Z-COORD'.ljust(10)}")
    print("-" * 75)
    
    atom_count = 0
    # Open and parse the standard PDB column spacing format
    with open(pdb_filename, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM"):
                atom_count += 1
                
                # Extract fixed column data standard for PDB files
                atom_name = line[12:16].strip()
                res_name = line[17:20].strip()
                chain_id = line[21].strip()
                x_coord = line[30:38].strip()
                y_coord = line[38:46].strip()
                z_coord = line[46:54].strip()
                
                # Display the first 12 spatial structural points for your report artifact
                if atom_count <= 12:
                    print(f"{atom_name.ljust(10)} | {res_name.ljust(8)} | {chain_id.ljust(6)} | {x_coord.ljust(10)} | {y_coord.ljust(10)} | {z_coord.ljust(10)}")
                    
    print("-" * 75)
    print(f"✅ Analysis Complete! Successfully parsed {atom_count} structural spatial coordinate vectors.")
    print("💡 Tip: You can now upload this downloaded 1aql.pdb file directly into SWISS-MODEL!")

except Exception as e:
    print(f"❌ Failed to process structure data: {e}")