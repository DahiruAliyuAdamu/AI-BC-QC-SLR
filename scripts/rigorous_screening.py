"""
Rigorous SLR Screening Script
=============================
This script performs a systematic screening of academic publications in RIS format
using predefined inclusion and exclusion criteria for a Systematic Literature Review (SLR).

Inclusion/Exclusion Logic:
- E0 (Year): Excludes papers published outside the 2016-2025 range.
- E1 (Type): Excludes non-research publication types (NEWS, NOTE, LETT, ED).
- E2 (Review): Excludes survey papers, systematic reviews, and mapping studies.
- E3 (Book): Excludes book chapters/sections.
- R6 (Noise): Excludes pure quantum physics/materials papers.
- R7 (Noise): Excludes cryptocurrency price forecasting/trading strategies.
- Inclusion: Requires Blockchain AND Quantum AND AI (with an applied AI methodology).
"""

import re
import csv
import os

def parse_ris(file_path):
    """
    Parses an RIS file into a list of dictionaries representing academic papers.
    """
    records = []
    current_record = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            
            match = re.match(r'^([A-Z0-9]{2})\s*-\s*(.*)$', line)
            if match:
                tag, value = match.groups()
                if tag == 'TY':
                    if current_record: 
                        records.append(current_record)
                    current_record = {'TY': value, 'TI': '', 'AB': '', 'PY': '', 'JO': '', 'RAW': [line]}
                else:
                    current_record['RAW'].append(line)
                    if tag in ['TI', 'T1']: 
                        current_record['TI'] += " " + value
                    elif tag in ['AB', 'N2']: 
                        current_record['AB'] += " " + value
                    elif tag in ['PY', 'Y1']: 
                        current_record['PY'] = value
                    elif tag in ['JO', 'T2', 'JF']: 
                        current_record['JO'] += " " + value
            else:
                if current_record: 
                    current_record['RAW'].append(line)
                    
        if current_record: 
            records.append(current_record)
            
    return records

def screen_record(rec):
    """
    Evaluates an RIS record against exclusion and inclusion criteria.
    Returns: (Decision, ReasonCode, Rationale)
    """
    title = rec.get('TI', '').lower()
    abstract = rec.get('AB', '').lower()
    content = f"{title} {abstract}"
    year_str = rec.get('PY', '')
    type_code = rec.get('TY', '')
    
    # --- 1. HARD EXCLUSIONS ---
    # E0: Publication Year Range (2016-2025)
    year_match = re.search(r'\d{4}', year_str)
    if year_match:
        year = int(year_match.group())
        if not (2016 <= year <= 2025):
            return "EXCLUDE", "R0", f"Year out of range: {year} (Target: 2016-2025)"
    
    # E1: Non-Research Publication Types
    if type_code in ['NEWS', 'NOTE', 'LETT', 'ED']:
         return "EXCLUDE", "R2", f"Non-research publication type: {type_code}"

    # E2: Survey, Review, or Secondary Studies
    review_pattern = r'review|survey|systematic\s+review|slr|literature\s+review|mapping\s+study|scoping\s+review|state\s+of\s+the\s+art|overview|tutorial|narrative'
    if re.search(review_pattern, content):
        return "EXCLUDE", "R10", "Contains review/survey keywords (Secondary study)"

    # E3: Book Chapters and Monographs
    if type_code in ['CHAP', 'BOOK'] or "book chapter" in content:
        return "EXCLUDE", "R11", "Book chapter or book section detected"

    # --- 2. THEMATIC PILLARS ---
    ai_terms = r'artificial\s+intelligence|ai|machine\s+learning|ml|deep\s+learning|dl|reinforcement\s+learning|rl|neural\s+network|learning-based|classifier|detection|anomaly|prediction|decision\s+support|agent|qml|quantum\s+machine\s+learning'
    bc_terms = r'blockchain|distributed\s+ledger|dlt|smart\s+contract|consensus|hyperledger|ethereum|ledger'
    qc_terms = r'quantum|post-quantum|pqc|quantum-safe|quantum-resistant|lattice-based|qkd|quantum\s+key\s+distribution|qrng|quantum\s+random|quantum\s+communication|quantum\s+network|quantum\s+blockchain|vqe|qaoa|quantum\s+anneal'

    has_ai = bool(re.search(ai_terms, content))
    has_bc = bool(re.search(bc_terms, content))
    has_qc = bool(re.search(qc_terms, content))

    # --- 3. DOMAIN NOISE FILTERING ---
    # R7: Financial / Cryptocurrency speculation and price trading noise
    crypto_trading_pattern = r'bitcoin|cryptocurrency\s+price|volatility|trading\s+strategy|price\s+forecasting'
    if re.search(crypto_trading_pattern, content):
        return "EXCLUDE", "R7", "Cryptocurrency trading, financial price volatility, or market speculation"
    
    # R6: Pure Physics / Hardware / Materials Sciences (No computing/protocol focus)
    if has_qc and not (has_bc or has_ai): 
        physics_pattern = r'quantum\s+dots|quantum\s+materials|spectroscopy'
        if re.search(physics_pattern, content):
            return "EXCLUDE", "R6", "Pure quantum physics, physical materials, or hardware spectroscopy"

    # --- 4. INCLUSION / MAYBE DECISIONS ---
    # INCLUDE: Blockchain + Quantum + AI (Applied Methodology)
    if has_bc and has_qc and has_ai:
        applied_ai_pattern = r'trained|evaluated|model|accuracy|precision|recall|detection|classification|optimization|performance'
        if re.search(applied_ai_pattern, abstract):
            return "INCLUDE", "N/A", "All three core pillars present with an applied AI evaluation"
        else:
            return "MAYBE", "R12", "All three pillars present, but abstract is too vague to confirm applied AI"

    # MAYBE: Blockchain + Quantum (AI missing or needs deep-dive review)
    if has_bc and has_qc and not has_ai:
        return "MAYBE", "R5", "Blockchain and Quantum present, but AI is missing or vague"
    
    # EXCLUDE: Missing one or more core concepts
    reasons = []
    codes = []
    if not has_bc:
        codes.append("R3")
        reasons.append("Missing Blockchain pillar")
    if not has_qc:
        codes.append("R4")
        reasons.append("Missing Quantum computing pillar")
    if not has_ai:
        codes.append("R5")
        reasons.append("Missing Artificial Intelligence pillar")
    
    if codes:
        return "EXCLUDE", ",".join(codes), "; ".join(reasons)

    return "EXCLUDE", "R5", "Failed overall inclusion logic"

def main():
    # Detect running path dynamically (GitHub/User Portable)
    base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
    
    # Input paths (Expects RIS files in same folder as script)
    include_file = os.path.join(base_dir, 'include.ris')
    second_included_file = os.path.join(base_dir, 'second_included.ris')
    csv_output = os.path.join(base_dir, 'final_screened_papers.csv')
    
    records = []
    if os.path.exists(include_file): 
        print(f"Parsing: {include_file}")
        records.extend(parse_ris(include_file))
    if os.path.exists(second_included_file): 
        print(f"Parsing: {second_included_file}")
        records.extend(parse_ris(second_included_file))
        
    if not records:
        print(f"[!] Warning: No input RIS files found at: \n  - {include_file}\n  - {second_included_file}")
        print("Please place your RIS files in the same folder and try running the script again.")
        return
    
    print(f"\nTotal records loaded for screening: {len(records)}")
    
    final_data = []
    category_ris = {
        'INCLUDE': [],
        'MAYBE': [],
        'EXCLUDE': []
    }

    for rec in records:
        decision, code, rationale = screen_record(rec)
        final_data.append({
            'Title': rec.get('TI', 'N/A').strip(),
            'Year': rec.get('PY', 'N/A'),
            'Decision': decision,
            'ReasonCode': code,
            'Rationale': rationale
        })
        category_ris[decision].append(rec)

    # 1. Save Summary CSV Report
    with open(csv_output, 'w', newline='', encoding='utf-8') as f:
        keys = ['Title', 'Year', 'Decision', 'ReasonCode', 'Rationale']
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(final_data)

    # 2. Save Filtered RIS Output Collections
    for cat in ['INCLUDE', 'MAYBE', 'EXCLUDE']:
        ris_path = os.path.join(base_dir, f'final_{cat.lower()}.ris')
        with open(ris_path, 'w', encoding='utf-8') as f:
            for rec in category_ris[cat]:
                for line in rec['RAW']:
                    f.write(line + '\n')
                if not rec['RAW'][-1].strip().startswith('ER'):
                    f.write('ER  - \n')

    # Summary Output
    print(f"\n=== Rigorous Screening Complete ===")
    print(f"Saved summary CSV report to: {csv_output}")
    print(f"Total Processed: {len(records)}")
    print(f"  └─ INCLUDE: {len(category_ris['INCLUDE'])}")
    print(f"  └─ MAYBE:   {len(category_ris['MAYBE'])}")
    print(f"  └─ EXCLUDE: {len(category_ris['EXCLUDE'])}")
    print("Individual RIS files generated:")
    print(f"  - final_include.ris")
    print(f"  - final_maybe.ris")
    print(f"  - final_exclude.ris")

if __name__ == "__main__":
    main()
