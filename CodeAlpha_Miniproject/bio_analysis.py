from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

# Tell NCBI who is running the request (use any placeholder email)
Entrez.email = "intern@codealpha.com"

print("🧬 Step 1: Downloading target DNA sequence from NCBI...")
# Fetching a known standard sequence: Human Beta-Globin (HBB) mRNA
gene_id = "NM_000518.5"
handle = Entrez.efetch(db="nucleotide", id=gene_id, rettype="fasta", retmode="text")
seq_record = SeqIO.read(handle, "fasta")
handle.close()

print(f"✅ Downloaded: {seq_record.id} - {seq_record.description[:50]}...")

print("\n🚀 Step 2: Running Remote BLAST Search against NCBI servers...")
print("⏳ (This will take about 1-2 minutes while NCBI processes the alignment...)")
# Performs a nucleotide-to-nucleotide BLAST (blastn)
result_handle = NCBIWWW.qblast("blastn", "nt", seq_record.seq)
blast_record = NCBIXML.read(result_handle)
result_handle.close()

print("\n📊 Step 3: Extracting Required Metrics for CodeAlpha Report:\n" + "="*65)

# Extract and display data for the top 3 matching homologous hits
for i, alignment in enumerate(blast_record.alignments[:3]):
    print(f"\n🔥 Match #{i+1}: {alignment.title[:75]}...")
    
    for hsp in alignment.hsps[:1]:  # Get the top high-scoring alignment pair
        # Calculate precise identity percentages
        identity_pct = (hsp.identities / hsp.align_length) * 100
        
        print(f"  🔹 Alignment Score : {hsp.score}")
        print(f"  🔹 E-Value          : {hsp.expect}")
        print(f"  🔹 Sequence Identity : {hsp.identities}/{hsp.align_length} ({identity_pct:.2f}%)")
        print(f"  🔹 Alignment Length  : {hsp.align_length} base pairs")
print("="*65 + "\n✅ Analysis Complete! Copy the metrics above for your document.")