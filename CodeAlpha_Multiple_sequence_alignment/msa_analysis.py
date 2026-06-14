from Bio import Align

def run_multiple_alignment():
    print("🧬 CodeAlpha Bioinformatics Task 2: Multiple Sequence Alignment")
    print("=" * 70)
    
    # 1. Define 5 protein sequences from the same family (Insulin variations across species)
    sequences = {
        "Human_Insulin": "GIVEQCCTSICSLYQLENYCN",
        "Chimp_Insulin": "GIVEQCCTSICSLYQLENYCN",
        "Pig_Insulin"  : "GIVEQCCTSICSLYQLENYCN",
        "Cow_Insulin"  : "GIVEQCCASVCSLYQLENYCN", 
        "Sheep_Insulin": "GIVEQCCAGVCSLYQLENYCN"  
    }
    
    baseline_key = "Human_Insulin"
    baseline_seq = sequences[baseline_key]
    
    print("📊 Step 1: Aligning 5 protein sequences against baseline...")
    
    # FIX: Using standard standard PairwiseAligner to avoid version attribute errors
    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'
    
    sequence_len = len(baseline_seq)
    conserved_map = [True] * sequence_len
    
    alignment_results = {}
    for name, seq in sequences.items():
        # Score the similarity matches
        score = aligner.score(baseline_seq, seq)
        alignment_results[name] = (seq, score)
        
        # Trace amino acid position tracking
        for idx in range(min(sequence_len, len(seq))):
            if seq[idx] != baseline_seq[idx]:
                conserved_map[idx] = False

    # 2. Print Alignment Output Results Matrix
    print("\n🖥️ Step 2: Sequence Alignment Display Matrix:")
    print("-" * 70)
    for name, (seq, score) in alignment_results.items():
        print(f"{name.ljust(15)} : {seq}  (Alignment Score: {score:.1f})")
    
    # Map out the visual alignment tracker string
    motif_visual = "".join(["*" if is_conserved else "." for is_conserved in conserved_map])
    print(f"{'Conserved Match'.ljust(15)} : {motif_visual}")
    print("-" * 70)
    print("💡 Legend: [*] = Fully Conserved Residue | [.] = Mutation/Variable Residue")
    
    # 3. Highlight Conserved Regions and Motifs
    print("\n🔍 Step 3: Highlighted Conserved Motifs Interpretation")
    print("=" * 70)
    
    in_motif = False
    start_idx = 0
    motifs_found = []
    
    for idx, char in enumerate(motif_visual):
        if char == "*" and not in_motif:
            in_motif = True
            start_idx = idx
        elif char == "." and in_motif:
            in_motif = False
            motifs_found.append((start_idx, idx))
    if in_motif:
        motifs_found.append((start_idx, sequence_len))
        
    for start, end in motifs_found:
        motif_seq = baseline_seq[start:end]
        if len(motif_seq) >= 3: 
            # FIX: Cleaned string formatting syntax error
            print(f"✅ Found Stable Conserved Motif: '{motif_seq}' at positions {start + 1} to {end}")

if __name__ == "__main__":
    run_multiple_alignment()