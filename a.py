def get_biotype_from_transcript_id(transcript_id):
    biotypes_by_transcript_id_start = {"NM_" : "protein_coding", "NR_" : "non_coding"}
    for (start, biotype) in biotypes_by_transcript_id_start.items():
        if transcript_id.startswith(start):
            return biotype

    if "tRNA" in transcript_id:
        return "tRNA"
    return "N/A"
print get_biotype_from_transcript_id("NM_ABC")
