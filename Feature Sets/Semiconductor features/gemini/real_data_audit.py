
import duckdb
import pandas as pd
import numpy as np
import os
import sys
import importlib.util
from tqdm import tqdm

DB_PATH = r'C:\Users\jyama\Desktop\silver db\trading.duckdb'

def get_semiconductor_tickers():
    conn = duckdb.connect(DB_PATH)
    q = "SELECT ticker FROM tickers WHERE industry ILIKE '%Semiconductor%'"
    tickers = [r[0] for r in conn.execute(q).fetchall()]
    conn.close()
    return tickers

def load_data_for_ticker(ticker):
    conn = duckdb.connect(DB_PATH)
    q = f"SELECT * FROM fundamentals WHERE ticker = '{ticker}' AND dimension = 'ARQ' ORDER BY calendardate ASC"
    df = conn.execute(q).fetchdf()
    conn.close()
    return df

def run_audit():
    tickers = get_semiconductor_tickers()
    print(f"Found {len(tickers)} semiconductor tickers.")
    
    # Use a sample of 5 major tickers for the audit
    sample_tickers = ['ACMR', 'NVDA', 'AMD', 'INTC', 'TSM']
    available_tickers = [t for t in sample_tickers if t in tickers]
    
    if not available_tickers:
        available_tickers = tickers[:5]
        
    audit_results = []
    
    folders = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('f')])
    
    for folder in tqdm(folders, desc="Auditing folders"):
        folder_path = os.path.join(os.getcwd(), folder)
        files = [f for f in os.listdir(folder_path) if f.endswith('_gemini.py') and 'base' in f]
        
        if not files:
            continue
            
        # Audit the first base file in each folder
        file_to_audit = sorted(files)[0]
        file_path = os.path.join(folder_path, file_to_audit)
        
        # Dynamic import
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        foo = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(foo)
            feature_funcs = getattr(foo, 'FEATURE_FUNCTIONS', {})
        except Exception as e:
            audit_results.append({'folder': folder, 'status': 'Error', 'message': f"Import Error: {str(e)}"})
            continue

        folder_success_count = 0
        total_features = len(feature_funcs)
        
        for ticker in available_tickers:
            df = load_data_for_ticker(ticker)
            if df.empty:
                continue
            
            # Prepare data: most features expect columns like 'revenue', 'assets', etc.
            # duckdb fetchdf might have different case or names
            df.columns = [c.lower() for c in df.columns]
            
            # Simple check on one feature to see if it runs
            if feature_funcs:
                first_func_name = list(feature_funcs.keys())[0]
                first_func = feature_funcs[first_func_name]
                
                try:
                    import inspect
                    sig = inspect.signature(first_func)
                    args = sig.parameters.keys()
                    input_data = {arg: df[arg] for arg in args if arg in df.columns}
                    
                    if len(input_data) == len(args):
                        res = first_func(**input_data)
                        if not res.dropna().empty:
                            folder_success_count += 1
                except Exception:
                    pass
        
        status = "PASS" if folder_success_count > 0 else "FAIL"
        audit_results.append({
            'folder': folder, 
            'status': status, 
            'features_count': total_features,
            'ticker_coverage': f"{folder_success_count}/{len(available_tickers)}"
        })

    audit_df = pd.DataFrame(audit_results)
    audit_df.to_csv('real_data_audit_report.csv', index=False)
    print("\nAudit Complete. Report saved to 'real_data_audit_report.csv'.")
    print(audit_df['status'].value_counts())

if __name__ == "__main__":
    run_audit()
