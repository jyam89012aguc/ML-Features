import numpy as np
import pandas as pd
import importlib
import os
import sys
import inspect

def generate_synthetic_data(n=2500, profiles=5):
    np.random.seed(42)
    all_data = []
    
    for p in range(profiles):
        t = np.arange(n)
        
        # Profile-specific characteristics
        drift = np.random.normal(0.0001, 0.00005)
        vol = np.random.uniform(0.005, 0.02)
        
        # Price
        noise = np.random.normal(drift, vol, n)
        close = 100 * np.exp(np.cumsum(noise))
        high = close * (1 + np.random.exponential(0.01, n))
        low = close * (1 - np.random.exponential(0.01, n))
        open_p = (high + low) / 2
        volume = np.random.lognormal(10, 1, n)
        
        # Fundamentals (quarterly-like, fwd-filled)
        # We generate daily series that look like fwd-filled quarterly data
        q_noise = np.random.normal(0, 0.05, n // 63 + 1)
        
        def make_q_fwd(base_val, growth_rate, noise_amp):
            q_vals = base_val * np.exp(np.cumsum(np.random.normal(growth_rate, noise_amp, n // 63 + 1)))
            daily_vals = np.repeat(q_vals, 63)[:n]
            return pd.Series(daily_vals)

        revenue = make_q_fwd(1000, 0.02, 0.05)
        gp = revenue * make_q_fwd(0.4, 0, 0.02).clip(0.1, 0.8)
        ebitda = gp * 0.5 + np.random.normal(0, 10, n)
        ebit = ebitda * 0.8
        netinc = ebit * 0.7
        
        assets = make_q_fwd(5000, 0.01, 0.03)
        debt = assets * make_q_fwd(0.3, 0, 0.05).clip(0, 0.9)
        equity = assets - debt
        cashneq = assets * 0.1
        
        ncfo = netinc * 1.1 + np.random.normal(0, 5, n)
        capex = -assets * 0.02
        fcf = ncfo + capex
        
        shareswa = pd.Series(np.ones(n) * 100)
        sharesbas = shareswa * 0.98
        
        # Event/Status columns
        listing_status = pd.Series(np.ones(n)).map({1: 'Active'})
        going_concern = pd.Series(np.zeros(n))
        
        # Additional columns from common families
        intexp = debt * 0.05 / 252
        taxexp = ebit * 0.21
        
        p_data = {
            'open': pd.Series(open_p),
            'high': pd.Series(high),
            'low': pd.Series(low),
            'close': pd.Series(close),
            'volume': pd.Series(volume),
            'revenue': revenue,
            'gp': gp,
            'ebitda': ebitda,
            'ebit': ebit,
            'netinc': netinc,
            'assets': assets,
            'debt': debt,
            'equity': equity,
            'cashneq': cashneq,
            'ncfo': ncfo,
            'capex': capex,
            'fcf': fcf,
            'shareswa': shareswa,
            'sharesbas': sharesbas,
            'listing_status': listing_status,
            'going_concern': going_concern,
            'intexp': intexp,
            'taxexp': taxexp,
            # Common aliases
            'netinccmn': netinc,
            'opinc': ebit,
            'operating_income': ebit,
            'cor': revenue - gp,
            'sgna': gp * 0.5,
            'rnd': gp * 0.2,
            'currassets': assets * 0.6,
            'current_assets': assets * 0.6,
            'currliab': debt * 0.4,
            'current_liabilities': debt * 0.4,
            'ppnent': assets * 0.4,
            'inventory': assets * 0.1,
            'receivables': assets * 0.1,
            'payables': debt * 0.1,
            'debtnc': debt * 0.8,
            'debtc': debt * 0.2,
            'intangibles': assets * 0.05,
            'deferredrev': revenue * 0.05,
            'prefstock': equity * 0.01,
            'retainedearnings': equity * 0.5,
            'accumotherinc': equity * 0.05,
            'treasurystock': equity * 0.05,
            'ncff': -debt * 0.05,
            'ncfi': capex,
            'ncfcommon': -netinc * 0.3, # dividends
            'ncfdebt': -debt * 0.02,
            'ncfi_inv': -assets * 0.01,
            'ncfx': np.zeros(n),
            'cash': cashneq,
            'cashneq': cashneq,
            'interest_expense': intexp,
            'intexp': intexp,
            'gross_profit': gp,
            'gp': gp,
            'dividend_cut': pd.Series(np.random.choice([0, 1], n, p=[0.99, 0.01])),
            'dividend_suspension': pd.Series(np.random.choice([0, 1], n, p=[0.995, 0.005])),
            'reverse_split': pd.Series(np.random.choice([0, 1], n, p=[0.999, 0.001])),
            'event_count': pd.Series(np.random.poisson(0.1, n)),
            'going_concern_flag': pd.Series(np.random.choice([0, 1], n, p=[0.98, 0.02])),
            'delisting_notice': pd.Series(np.random.choice([0, 1], n, p=[0.997, 0.003])),
            'listing_tier_score': pd.Series(np.random.randint(1, 5, n)),
            'pe': close / (netinc / shareswa).replace(0, np.nan),
            'pb': close / (equity / shareswa).replace(0, np.nan),
            'ps': close / (revenue / shareswa).replace(0, np.nan),
            'ev': close * shareswa + debt - cashneq,
            'marketcap': close * shareswa,
            'eps': netinc / shareswa,
            'dividends': pd.Series(np.random.choice([0, 1], n, p=[0.9, 0.1])) * (netinc * 0.3 / shareswa).clip(0),
            'ps_insider_pct': pd.Series(np.ones(n) * 0.05),
            'ps_inst_pct': pd.Series(np.ones(n) * 0.6),
            'instownpct': pd.Series(np.ones(n) * 60.0),
            'insiderpct': pd.Series(np.ones(n) * 5.0),
            'instpct': pd.Series(np.ones(n) * 60.0),
            'peer_median_pe': pd.Series(np.ones(n) * 15.0),
            'peer_median_pb': pd.Series(np.ones(n) * 2.0),
            'peer_median_ps': pd.Series(np.ones(n) * 1.5),
            'peer_median_marketcap': pd.Series(np.ones(n) * 1000000000),
            'insider_buys': pd.Series(np.random.poisson(0.05, n)),
            'insider_sells': pd.Series(np.random.poisson(0.1, n)),
            'insider_buy_value': pd.Series(np.random.exponential(10000, n)),
            'insider_sell_value': pd.Series(np.random.exponential(20000, n)),
            'ceo_buys': pd.Series(np.random.poisson(0.01, n)),
            'cfo_buys': pd.Series(np.random.poisson(0.01, n)),
            'director_buys': pd.Series(np.random.poisson(0.03, n)),
            'insider_holdings': pd.Series(np.ones(n) * 1000000),
            'market_cap': close * shareswa,
            'inst_holders': pd.Series(np.ones(n) * 500),
            'inst_shares': pd.Series(np.ones(n) * 1000000),
            'peer_median_inst_holders': pd.Series(np.ones(n) * 450),
            'peer_median_inst_shares': pd.Series(np.ones(n) * 900000),
            'amihud_illiquidity': pd.Series(np.random.exponential(0.0001, n)),
            'return_decay': pd.Series(np.random.normal(0, 0.01, n)),
            'top_holder_shares': pd.Series(np.ones(n) * 100000),
            'institutional_buys': pd.Series(np.random.lognormal(10, 1, n)),
            'institutional_sells': pd.Series(np.random.lognormal(10, 1, n)),
            'institutional_buys_count': pd.Series(np.random.poisson(10, n)),
            'institutional_sells_count': pd.Series(np.random.poisson(10, n)),
        }
        all_data.append(p_data)
        
    # For now, just return the first profile to keep it simple, 
    # but we can extend to multiple profiles later if needed.
    return all_data[0]

def get_functions_from_module(module):
    registries = [v for k, v in module.__dict__.items() if k.endswith('_REGISTRY') or 'REGISTRY' in k]
    functions = {}
    if not registries:
        for k, v in module.__dict__.items():
            if callable(v) and not k.startswith('_'):
                functions[k] = {'func': v, 'inputs': list(inspect.signature(v).parameters.keys())}
    else:
        for reg in registries:
            for k, v in reg.items():
                functions[k] = v
    return functions

def audit_family(family_dir):
    data = generate_synthetic_data()
    files = [f for f in os.listdir(family_dir) if f.endswith('.py') and '__init__' not in f]
    
    # Sort files by tier
    base_files = [f for f in files if 'base' in f]
    d2_files = [f for f in files if '2nd_derivatives' in f]
    d3_files = [f for f in files if '3rd_derivatives' in f]
    
    all_outputs = {k: v for k, v in data.items()}
    results = {}
    
    def run_tier(files):
        for file in files:
            module_name = f"{family_dir}.{file[:-3]}".replace('\\', '.').replace('/', '.')
            try:
                module = importlib.import_module(module_name)
                functions = get_functions_from_module(module)
                for name, info in functions.items():
                    func = info['func']
                    inputs = info['inputs']
                    
                    try:
                        args = {}
                        missing = []
                        for inp in inputs:
                            if inp in all_outputs:
                                args[inp] = all_outputs[inp]
                            else:
                                missing.append(inp)
                        
                        if missing:
                            results[name] = f"Missing inputs: {missing}"
                            continue
                            
                        output = func(**args)
                        if output is None:
                            results[name] = "Returned None"
                            continue
                            
                        all_outputs[name] = output
                        
                        # Value hash
                        warmup = 1500 # Larger warmup for long lookbacks
                        if len(output) > warmup:
                            val_slice = output.iloc[warmup:].values
                        else:
                            val_slice = output.values
                        
                        val_hash = hash(val_slice.tobytes())
                        
                        results[name] = {
                            'hash': val_hash,
                            'is_all_nan': output.isnull().all(),
                            'is_constant': output.nunique() <= 1,
                            'mean': output.mean(),
                            'std': output.std(),
                            'tier': 'base' if 'base' in file else ('2d' if '2nd' in file else '3d')
                        }
                    except Exception as e:
                        results[name] = f"Error: {e}"
            except Exception as e:
                print(f"Error importing {module_name}: {e}")

    # Run sequentially by tier
    run_tier(base_files)
    run_tier(d2_files)
    run_tier(d3_files)
    
    # Detect duplicates
    hashes = {}
    duplicates = []
    for name, res in results.items():
        if isinstance(res, dict):
            h = res['hash']
            if h in hashes:
                duplicates.append((hashes[h], name))
            else:
                hashes[h] = name
                
    return results, duplicates

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_harness.py <family_dir>")
        sys.exit(1)
        
    family = sys.argv[1]
    res, dups = audit_family(family)
    
    print(f"--- Audit Results for {family} ---")
    print(f"Total functions: {len(res)}")
    
    errors = {k: v for k, v in res.items() if isinstance(v, str)}
    if errors:
        print(f"\nErrors ({len(errors)}):")
        # Group by error message
        grouped_errors = {}
        for k, v in errors.items():
            if v not in grouped_errors: grouped_errors[v] = []
            grouped_errors[v].append(k)
        for msg, names in grouped_errors.items():
            print(f"  {msg}: {len(names)} functions")
            if len(names) < 10:
                print(f"    {', '.join(names)}")
            else:
                print(f"    {', '.join(names[:5])} ... (+{len(names)-5} more)")
            
    all_nan = [k for k, v in res.items() if isinstance(v, dict) and v['is_all_nan']]
    if all_nan:
        print(f"\nAll-NaN functions ({len(all_nan)}):")
        print(f"  {', '.join(all_nan[:10])} ...")
        
    constants = [k for k, v in res.items() if isinstance(v, dict) and v['is_constant'] and not v['is_all_nan']]
    if constants:
        print(f"\nConstant functions ({len(constants)}):")
        print(f"  {', '.join(constants[:10])} ...")

    if dups:
        print(f"\nDuplicates ({len(dups)}):")
        # Group duplicates
        groups = {}
        for d in dups:
            master = d[0]
            if master not in groups: groups[master] = []
            groups[master].append(d[1])
            
        for master, members in groups.items():
            print(f"  {master} == {', '.join(members[:3])} ... (+{len(members)})")
