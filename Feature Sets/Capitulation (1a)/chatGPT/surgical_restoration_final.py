import os
import re

def fix_families_36_45():
    all_dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    target_dirs = []
    for f in range(36, 46):
        prefix = f"{f}_"
        for d in all_dirs:
            if d.startswith(prefix):
                target_dirs.append(d)
                break
    
    for d in target_dirs:
        d2_file = os.path.join(d, f"{d}_2nd_derivatives.py")
        if not os.path.exists(d2_file):
            continue
            
        with open(d2_file, 'r') as f:
            content = f.read()
            
        pattern = r"def (\w+)\(realized_vol_z\):"
        funcs = re.findall(pattern, content)
        
        if not funcs:
            continue
            
        new_content = content
        for func in funcs:
            old_body_pattern = rf"def {func}\(realized_vol_z\):\n\s+feature = _s\(realized_vol_z\)"
            replacement = f"def {func}(close):\n    rv = _s(close).pct_change().rolling(21).std()\n    feature = _z(rv, 252)"
            new_content = re.sub(old_body_pattern, replacement, new_content)
        
        new_content = new_content.replace("'inputs': ['realized_vol_z']", "'inputs': ['close']")
        
        with open(d2_file, 'w') as f:
            f.write(new_content)
        print(f"Fixed {d2_file}")

def fix_families_60_100():
    all_dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    target_dirs = []
    ranges = list(range(60, 77)) + list(range(83, 94)) + list(range(95, 101))
    for r in ranges:
        prefix = f"{r}_"
        for d in all_dirs:
            if d.startswith(prefix):
                target_dirs.append(d)
                break
    
    raw_columns = [
        'open', 'high', 'low', 'close', 'volume', 'revenue', 'gp', 'ebitda', 'ebit', 'netinc', 'assets', 'debt', 'equity', 
        'cashneq', 'ncfo', 'capex', 'fcf', 'shareswa', 'sharesbas', 'listing_status', 'going_concern', 'intexp', 'taxexp', 
        'netinccmn', 'opinc', 'operating_income', 'cor', 'sgna', 'rnd', 'currassets', 'current_assets', 'currliab', 
        'current_liabilities', 'ppnent', 'inventory', 'receivables', 'payables', 'debtnc', 'debtc', 'intangibles', 
        'deferredrev', 'prefstock', 'retainedearnings', 'accumotherinc', 'treasurystock', 'ncff', 'ncfi', 'ncfcommon', 
        'ncfdebt', 'ncfi_inv', 'ncfx', 'cash', 'interest_expense', 'gross_profit', 'dividend_cut', 'dividend_suspension', 
        'reverse_split', 'event_count', 'going_concern_flag', 'delisting_notice', 'listing_tier_score', 'pe', 'pb', 'ps', 
        'ev', 'marketcap', 'eps', 'dividends', 'ps_insider_pct', 'ps_inst_pct', 'instownpct', 'insiderpct', 'instpct', 
        'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_marketcap', 'insider_buys', 'insider_sells', 
        'insider_buy_value', 'insider_sell_value', 'ceo_buys', 'cfo_buys', 'director_buys', 'insider_holdings', 
        'market_cap', 'inst_holders', 'inst_shares', 'peer_median_inst_holders', 'peer_median_inst_shares', 
        'amihud_illiquidity', 'return_decay', 'top_holder_shares', 'institutional_buys', 'institutional_sells', 
        'institutional_buys_count', 'institutional_sells_count'
    ]
    
    for d in target_dirs:
        d2_file = os.path.join(d, f"{d}_2nd_derivatives.py")
        if not os.path.exists(d2_file):
            continue
            
        base_funcs = set()
        for f in os.listdir(d):
            if 'base' in f and f.endswith('.py'):
                with open(os.path.join(d, f), 'r') as bf:
                    b_content = bf.read()
                    base_funcs.update(re.findall(r"def (\w+)\(", b_content))
        
        with open(d2_file, 'r') as f:
            content = f.read()
            
        # Refined registry search
        input_matches = re.findall(r"'inputs': \['(\w+)'\]", content)
        
        replacements = {}
        for inp in input_matches:
            if inp in raw_columns or inp in base_funcs:
                continue
            
            found_raw = None
            for raw in sorted(raw_columns, key=len, reverse=True):
                if raw in inp:
                    found_raw = raw
                    break
            
            if found_raw:
                replacements[inp] = found_raw
        
        if not replacements:
            continue
            
        new_content = content
        for old_inp, new_inp in replacements.items():
            new_content = new_content.replace(f"({old_inp}):", f"({new_inp}):")
            new_content = new_content.replace(f"_s({old_inp})", f"_s({new_inp})")
            new_content = new_content.replace(f"['{old_inp}']", f"['{new_inp}']")
            
        with open(d2_file, 'w') as f:
            f.write(new_content)
        print(f"Fixed {d2_file} (Replacements: {len(replacements)})")

if __name__ == "__main__":
    fix_families_36_45()
    fix_families_60_100()
