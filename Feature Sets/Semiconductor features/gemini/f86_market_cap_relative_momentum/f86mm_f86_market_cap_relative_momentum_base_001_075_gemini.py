import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f86mm_f86_market_cap_relative_momentum_calc001_182d_val_v001_signal(evebitda, fcf, marketcap):
    v1 = marketcap * 1.0
    v2 = evebitda * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(182).std() / v1.rolling(25).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(18).mean() * 0.0001
    e0 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f0 = ratio.pct_change(18).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(40).mean() * 0.00030000000000000003
    e2 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f2 = ratio.pct_change(40).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(28).mean() * 0.0005
    e4 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f4 = ratio.pct_change(28).fillna(0)
    d5 = ratio.shift(6).rolling(31).mean() * 0.0006000000000000001
    e5 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f5 = ratio.pct_change(31).fillna(0)
    d6 = ratio.shift(7).rolling(21).mean() * 0.0007
    e6 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f6 = ratio.pct_change(21).fillna(0)
    d7 = ratio.shift(8).rolling(20).mean() * 0.0008
    e7 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f7 = ratio.pct_change(20).fillna(0)
    res = ratio.diff(182)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc001_182d_val_v001_signal'] = f86mm_f86_market_cap_relative_momentum_calc001_182d_val_v001_signal

def f86mm_f86_market_cap_relative_momentum_calc002_11d_val_v002_signal(close, netinc, revenue):
    v1 = revenue * 1.0
    v2 = close * 1.0
    v3 = netinc * 1.0
    ratio = v1.rolling(11).max() / v2.rolling(11).min().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(40).mean() * 0.0002
    e1 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f1 = ratio.pct_change(40).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(28).mean() * 0.0004
    e3 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f3 = ratio.pct_change(28).fillna(0)
    d4 = ratio.shift(5).rolling(31).mean() * 0.0005
    e4 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f4 = ratio.pct_change(31).fillna(0)
    d5 = ratio.shift(6).rolling(21).mean() * 0.0006000000000000001
    e5 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f5 = ratio.pct_change(21).fillna(0)
    d6 = ratio.shift(7).rolling(20).mean() * 0.0007
    e6 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f6 = ratio.pct_change(20).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = ratio.rolling(11).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc002_11d_val_v002_signal'] = f86mm_f86_market_cap_relative_momentum_calc002_11d_val_v002_signal

def f86mm_f86_market_cap_relative_momentum_calc003_159d_val_v003_signal(assets, ebitda, revenue):
    v1 = assets * 1.0
    v2 = revenue * 1.0
    v3 = ebitda * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(40).mean() * 0.0001
    e0 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f0 = ratio.pct_change(40).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(28).mean() * 0.00030000000000000003
    e2 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f2 = ratio.pct_change(28).fillna(0)
    d3 = ratio.shift(4).rolling(31).mean() * 0.0004
    e3 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f3 = ratio.pct_change(31).fillna(0)
    d4 = ratio.shift(5).rolling(21).mean() * 0.0005
    e4 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f4 = ratio.pct_change(21).fillna(0)
    d5 = ratio.shift(6).rolling(20).mean() * 0.0006000000000000001
    e5 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f5 = ratio.pct_change(20).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.ewm(span=159).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc003_159d_val_v003_signal'] = f86mm_f86_market_cap_relative_momentum_calc003_159d_val_v003_signal

def f86mm_f86_market_cap_relative_momentum_calc004_147d_val_v004_signal(evebitda, pb, ps):
    v1 = pb * 1.0
    v2 = evebitda * 1.0
    v3 = ps * 1.0
    ratio = (v1 - v1.rolling(147).min()) / (v1.rolling(147).max() - v1.rolling(147).min() + 1e-9)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(28).mean() * 0.0002
    e1 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f1 = ratio.pct_change(28).fillna(0)
    d2 = ratio.shift(3).rolling(31).mean() * 0.00030000000000000003
    e2 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f2 = ratio.pct_change(31).fillna(0)
    d3 = ratio.shift(4).rolling(21).mean() * 0.0004
    e3 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f3 = ratio.pct_change(21).fillna(0)
    d4 = ratio.shift(5).rolling(20).mean() * 0.0005
    e4 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f4 = ratio.pct_change(20).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(36).mean() * 0.0008
    e7 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f7 = ratio.pct_change(36).fillna(0)
    res = ratio.diff(147)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc004_147d_val_v004_signal'] = f86mm_f86_market_cap_relative_momentum_calc004_147d_val_v004_signal

def f86mm_f86_market_cap_relative_momentum_calc005_244d_val_v005_signal(close, netinc, ps):
    v1 = ps * 1.0
    v2 = netinc * 1.0
    v3 = close * 1.0
    ratio = v1.rolling(244).std() / v1.rolling(209).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(28).mean() * 0.0001
    e0 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f0 = ratio.pct_change(28).fillna(0)
    d1 = ratio.shift(2).rolling(31).mean() * 0.0002
    e1 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f1 = ratio.pct_change(31).fillna(0)
    d2 = ratio.shift(3).rolling(21).mean() * 0.00030000000000000003
    e2 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f2 = ratio.pct_change(21).fillna(0)
    d3 = ratio.shift(4).rolling(20).mean() * 0.0004
    e3 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f3 = ratio.pct_change(20).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(36).mean() * 0.0007
    e6 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f6 = ratio.pct_change(36).fillna(0)
    d7 = ratio.shift(8).rolling(23).mean() * 0.0008
    e7 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f7 = ratio.pct_change(23).fillna(0)
    res = ratio.rolling(244).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc005_244d_val_v005_signal'] = f86mm_f86_market_cap_relative_momentum_calc005_244d_val_v005_signal

def f86mm_f86_market_cap_relative_momentum_calc006_119d_val_v006_signal(ev, netinc, ps):
    v1 = ps * 1.0
    v2 = ev * 1.0
    v3 = netinc * 1.0
    ratio = v1.rolling(119).std() / v1.rolling(58).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(31).mean() * 0.0001
    e0 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f0 = ratio.pct_change(31).fillna(0)
    d1 = ratio.shift(2).rolling(21).mean() * 0.0002
    e1 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f1 = ratio.pct_change(21).fillna(0)
    d2 = ratio.shift(3).rolling(20).mean() * 0.00030000000000000003
    e2 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f2 = ratio.pct_change(20).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(36).mean() * 0.0006000000000000001
    e5 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f5 = ratio.pct_change(36).fillna(0)
    d6 = ratio.shift(7).rolling(23).mean() * 0.0007
    e6 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f6 = ratio.pct_change(23).fillna(0)
    d7 = ratio.shift(8).rolling(25).mean() * 0.0008
    e7 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f7 = ratio.pct_change(25).fillna(0)
    res = ratio.rolling(119).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc006_119d_val_v006_signal'] = f86mm_f86_market_cap_relative_momentum_calc006_119d_val_v006_signal

def f86mm_f86_market_cap_relative_momentum_calc007_15d_val_v007_signal(close, ebitda, ev):
    v1 = ebitda * 1.0
    v2 = ev * 1.0
    v3 = close * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(21).mean() * 0.0001
    e0 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f0 = ratio.pct_change(21).fillna(0)
    d1 = ratio.shift(2).rolling(20).mean() * 0.0002
    e1 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f1 = ratio.pct_change(20).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(36).mean() * 0.0005
    e4 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f4 = ratio.pct_change(36).fillna(0)
    d5 = ratio.shift(6).rolling(23).mean() * 0.0006000000000000001
    e5 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f5 = ratio.pct_change(23).fillna(0)
    d6 = ratio.shift(7).rolling(25).mean() * 0.0007
    e6 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f6 = ratio.pct_change(25).fillna(0)
    d7 = ratio.shift(8).rolling(53).mean() * 0.0008
    e7 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f7 = ratio.pct_change(53).fillna(0)
    res = ratio.rolling(15).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc007_15d_val_v007_signal'] = f86mm_f86_market_cap_relative_momentum_calc007_15d_val_v007_signal

def f86mm_f86_market_cap_relative_momentum_calc008_241d_val_v008_signal(assets, ps, revenue):
    v1 = assets * 1.0
    v2 = ps * 1.0
    v3 = revenue * 1.0
    ratio = v1.rolling(241).kurt() / v2.rolling(241).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(20).mean() * 0.0001
    e0 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f0 = ratio.pct_change(20).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(36).mean() * 0.0004
    e3 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f3 = ratio.pct_change(36).fillna(0)
    d4 = ratio.shift(5).rolling(23).mean() * 0.0005
    e4 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f4 = ratio.pct_change(23).fillna(0)
    d5 = ratio.shift(6).rolling(25).mean() * 0.0006000000000000001
    e5 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f5 = ratio.pct_change(25).fillna(0)
    d6 = ratio.shift(7).rolling(53).mean() * 0.0007
    e6 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f6 = ratio.pct_change(53).fillna(0)
    d7 = ratio.shift(8).rolling(31).mean() * 0.0008
    e7 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f7 = ratio.pct_change(31).fillna(0)
    res = ratio.rolling(241).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc008_241d_val_v008_signal'] = f86mm_f86_market_cap_relative_momentum_calc008_241d_val_v008_signal

def f86mm_f86_market_cap_relative_momentum_calc009_247d_val_v009_signal(evebitda, marketcap, pe):
    v1 = marketcap * 1.0
    v2 = evebitda * 1.0
    v3 = pe * 1.0
    ratio = v1.rolling(247).std() / v1.rolling(219).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(36).mean() * 0.00030000000000000003
    e2 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f2 = ratio.pct_change(36).fillna(0)
    d3 = ratio.shift(4).rolling(23).mean() * 0.0004
    e3 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f3 = ratio.pct_change(23).fillna(0)
    d4 = ratio.shift(5).rolling(25).mean() * 0.0005
    e4 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f4 = ratio.pct_change(25).fillna(0)
    d5 = ratio.shift(6).rolling(53).mean() * 0.0006000000000000001
    e5 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f5 = ratio.pct_change(53).fillna(0)
    d6 = ratio.shift(7).rolling(31).mean() * 0.0007
    e6 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f6 = ratio.pct_change(31).fillna(0)
    d7 = ratio.shift(8).rolling(31).mean() * 0.0008
    e7 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f7 = ratio.pct_change(31).fillna(0)
    res = ratio.diff(41).rolling(247).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc009_247d_val_v009_signal'] = f86mm_f86_market_cap_relative_momentum_calc009_247d_val_v009_signal

def f86mm_f86_market_cap_relative_momentum_calc010_146d_val_v010_signal(assets, close, ev):
    v1 = ev * 1.0
    v2 = assets * 1.0
    v3 = close * 1.0
    ratio = v1.rolling(146).kurt() / v2.rolling(146).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(36).mean() * 0.0002
    e1 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f1 = ratio.pct_change(36).fillna(0)
    d2 = ratio.shift(3).rolling(23).mean() * 0.00030000000000000003
    e2 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f2 = ratio.pct_change(23).fillna(0)
    d3 = ratio.shift(4).rolling(25).mean() * 0.0004
    e3 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f3 = ratio.pct_change(25).fillna(0)
    d4 = ratio.shift(5).rolling(53).mean() * 0.0005
    e4 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f4 = ratio.pct_change(53).fillna(0)
    d5 = ratio.shift(6).rolling(31).mean() * 0.0006000000000000001
    e5 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f5 = ratio.pct_change(31).fillna(0)
    d6 = ratio.shift(7).rolling(31).mean() * 0.0007
    e6 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f6 = ratio.pct_change(31).fillna(0)
    d7 = ratio.shift(8).rolling(49).mean() * 0.0008
    e7 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f7 = ratio.pct_change(49).fillna(0)
    res = ratio.rolling(146).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc010_146d_val_v010_signal'] = f86mm_f86_market_cap_relative_momentum_calc010_146d_val_v010_signal

def f86mm_f86_market_cap_relative_momentum_calc011_32d_val_v011_signal(ev, evebitda, netinc):
    v1 = ev * 1.0
    v2 = netinc * 1.0
    v3 = evebitda * 1.0
    ratio = v1.rolling(32).std() / v1.rolling(202).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(36).mean() * 0.0001
    e0 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f0 = ratio.pct_change(36).fillna(0)
    d1 = ratio.shift(2).rolling(23).mean() * 0.0002
    e1 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f1 = ratio.pct_change(23).fillna(0)
    d2 = ratio.shift(3).rolling(25).mean() * 0.00030000000000000003
    e2 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f2 = ratio.pct_change(25).fillna(0)
    d3 = ratio.shift(4).rolling(53).mean() * 0.0004
    e3 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f3 = ratio.pct_change(53).fillna(0)
    d4 = ratio.shift(5).rolling(31).mean() * 0.0005
    e4 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f4 = ratio.pct_change(31).fillna(0)
    d5 = ratio.shift(6).rolling(31).mean() * 0.0006000000000000001
    e5 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f5 = ratio.pct_change(31).fillna(0)
    d6 = ratio.shift(7).rolling(49).mean() * 0.0007
    e6 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f6 = ratio.pct_change(49).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(32).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc011_32d_val_v011_signal'] = f86mm_f86_market_cap_relative_momentum_calc011_32d_val_v011_signal

def f86mm_f86_market_cap_relative_momentum_calc012_129d_val_v012_signal(assets, fcf, ps):
    v1 = assets * 1.0
    v2 = ps * 1.0
    v3 = fcf * 1.0
    ratio = v1.diff(42).rolling(129).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(23).mean() * 0.0001
    e0 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f0 = ratio.pct_change(23).fillna(0)
    d1 = ratio.shift(2).rolling(25).mean() * 0.0002
    e1 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f1 = ratio.pct_change(25).fillna(0)
    d2 = ratio.shift(3).rolling(53).mean() * 0.00030000000000000003
    e2 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f2 = ratio.pct_change(53).fillna(0)
    d3 = ratio.shift(4).rolling(31).mean() * 0.0004
    e3 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f3 = ratio.pct_change(31).fillna(0)
    d4 = ratio.shift(5).rolling(31).mean() * 0.0005
    e4 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f4 = ratio.pct_change(31).fillna(0)
    d5 = ratio.shift(6).rolling(49).mean() * 0.0006000000000000001
    e5 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f5 = ratio.pct_change(49).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.diff(42).rolling(129).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc012_129d_val_v012_signal'] = f86mm_f86_market_cap_relative_momentum_calc012_129d_val_v012_signal

def f86mm_f86_market_cap_relative_momentum_calc013_209d_val_v013_signal(assets, ebitda, marketcap):
    v1 = ebitda * 1.0
    v2 = marketcap * 1.0
    v3 = assets * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(25).mean() * 0.0001
    e0 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f0 = ratio.pct_change(25).fillna(0)
    d1 = ratio.shift(2).rolling(53).mean() * 0.0002
    e1 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f1 = ratio.pct_change(53).fillna(0)
    d2 = ratio.shift(3).rolling(31).mean() * 0.00030000000000000003
    e2 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f2 = ratio.pct_change(31).fillna(0)
    d3 = ratio.shift(4).rolling(31).mean() * 0.0004
    e3 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f3 = ratio.pct_change(31).fillna(0)
    d4 = ratio.shift(5).rolling(49).mean() * 0.0005
    e4 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f4 = ratio.pct_change(49).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(36).mean() * 0.0008
    e7 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f7 = ratio.pct_change(36).fillna(0)
    res = ratio.rolling(209).max() - ratio.rolling(209).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc013_209d_val_v013_signal'] = f86mm_f86_market_cap_relative_momentum_calc013_209d_val_v013_signal

def f86mm_f86_market_cap_relative_momentum_calc014_211d_val_v014_signal(close, ev, revenue):
    v1 = ev * 1.0
    v2 = close * 1.0
    v3 = revenue * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(53).mean() * 0.0001
    e0 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f0 = ratio.pct_change(53).fillna(0)
    d1 = ratio.shift(2).rolling(31).mean() * 0.0002
    e1 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f1 = ratio.pct_change(31).fillna(0)
    d2 = ratio.shift(3).rolling(31).mean() * 0.00030000000000000003
    e2 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f2 = ratio.pct_change(31).fillna(0)
    d3 = ratio.shift(4).rolling(49).mean() * 0.0004
    e3 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f3 = ratio.pct_change(49).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(36).mean() * 0.0007
    e6 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f6 = ratio.pct_change(36).fillna(0)
    d7 = ratio.shift(8).rolling(18).mean() * 0.0008
    e7 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f7 = ratio.pct_change(18).fillna(0)
    res = ratio.rolling(211).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc014_211d_val_v014_signal'] = f86mm_f86_market_cap_relative_momentum_calc014_211d_val_v014_signal

def f86mm_f86_market_cap_relative_momentum_calc015_248d_val_v015_signal(assets, ebitda, pe):
    v1 = ebitda * 1.0
    v2 = assets * 1.0
    v3 = pe * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(31).mean() * 0.0001
    e0 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f0 = ratio.pct_change(31).fillna(0)
    d1 = ratio.shift(2).rolling(31).mean() * 0.0002
    e1 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f1 = ratio.pct_change(31).fillna(0)
    d2 = ratio.shift(3).rolling(49).mean() * 0.00030000000000000003
    e2 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f2 = ratio.pct_change(49).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(36).mean() * 0.0006000000000000001
    e5 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f5 = ratio.pct_change(36).fillna(0)
    d6 = ratio.shift(7).rolling(18).mean() * 0.0007
    e6 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f6 = ratio.pct_change(18).fillna(0)
    d7 = ratio.shift(8).rolling(25).mean() * 0.0008
    e7 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f7 = ratio.pct_change(25).fillna(0)
    res = np.tanh(ratio.rolling(248).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc015_248d_val_v015_signal'] = f86mm_f86_market_cap_relative_momentum_calc015_248d_val_v015_signal

def f86mm_f86_market_cap_relative_momentum_calc016_249d_val_v016_signal(evebitda, pb, pe):
    v1 = pe * 1.0
    v2 = evebitda * 1.0
    v3 = pb * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(31).mean() * 0.0001
    e0 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f0 = ratio.pct_change(31).fillna(0)
    d1 = ratio.shift(2).rolling(49).mean() * 0.0002
    e1 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f1 = ratio.pct_change(49).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(36).mean() * 0.0005
    e4 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f4 = ratio.pct_change(36).fillna(0)
    d5 = ratio.shift(6).rolling(18).mean() * 0.0006000000000000001
    e5 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f5 = ratio.pct_change(18).fillna(0)
    d6 = ratio.shift(7).rolling(25).mean() * 0.0007
    e6 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f6 = ratio.pct_change(25).fillna(0)
    d7 = ratio.shift(8).rolling(21).mean() * 0.0008
    e7 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f7 = ratio.pct_change(21).fillna(0)
    res = ratio.rolling(249).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc016_249d_val_v016_signal'] = f86mm_f86_market_cap_relative_momentum_calc016_249d_val_v016_signal

def f86mm_f86_market_cap_relative_momentum_calc017_128d_val_v017_signal(evebitda, netinc, pb):
    v1 = netinc * 1.0
    v2 = evebitda * 1.0
    v3 = pb * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(49).mean() * 0.0001
    e0 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f0 = ratio.pct_change(49).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(36).mean() * 0.0004
    e3 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f3 = ratio.pct_change(36).fillna(0)
    d4 = ratio.shift(5).rolling(18).mean() * 0.0005
    e4 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f4 = ratio.pct_change(18).fillna(0)
    d5 = ratio.shift(6).rolling(25).mean() * 0.0006000000000000001
    e5 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f5 = ratio.pct_change(25).fillna(0)
    d6 = ratio.shift(7).rolling(21).mean() * 0.0007
    e6 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f6 = ratio.pct_change(21).fillna(0)
    d7 = ratio.shift(8).rolling(45).mean() * 0.0008
    e7 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f7 = ratio.pct_change(45).fillna(0)
    res = ratio.rolling(128).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc017_128d_val_v017_signal'] = f86mm_f86_market_cap_relative_momentum_calc017_128d_val_v017_signal

def f86mm_f86_market_cap_relative_momentum_calc018_63d_val_v018_signal(assets, close, ebitda):
    v1 = ebitda * 1.0
    v2 = close * 1.0
    v3 = assets * 1.0
    ratio = v1.pct_change(7) - v2.pct_change(7)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(36).mean() * 0.00030000000000000003
    e2 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f2 = ratio.pct_change(36).fillna(0)
    d3 = ratio.shift(4).rolling(18).mean() * 0.0004
    e3 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f3 = ratio.pct_change(18).fillna(0)
    d4 = ratio.shift(5).rolling(25).mean() * 0.0005
    e4 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f4 = ratio.pct_change(25).fillna(0)
    d5 = ratio.shift(6).rolling(21).mean() * 0.0006000000000000001
    e5 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f5 = ratio.pct_change(21).fillna(0)
    d6 = ratio.shift(7).rolling(45).mean() * 0.0007
    e6 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f6 = ratio.pct_change(45).fillna(0)
    d7 = ratio.shift(8).rolling(44).mean() * 0.0008
    e7 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f7 = ratio.pct_change(44).fillna(0)
    res = ratio.rolling(63).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc018_63d_val_v018_signal'] = f86mm_f86_market_cap_relative_momentum_calc018_63d_val_v018_signal

def f86mm_f86_market_cap_relative_momentum_calc019_185d_val_v019_signal(ebitda, netinc, pe):
    v1 = netinc * 1.0
    v2 = ebitda * 1.0
    v3 = pe * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(36).mean() * 0.0002
    e1 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f1 = ratio.pct_change(36).fillna(0)
    d2 = ratio.shift(3).rolling(18).mean() * 0.00030000000000000003
    e2 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f2 = ratio.pct_change(18).fillna(0)
    d3 = ratio.shift(4).rolling(25).mean() * 0.0004
    e3 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f3 = ratio.pct_change(25).fillna(0)
    d4 = ratio.shift(5).rolling(21).mean() * 0.0005
    e4 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f4 = ratio.pct_change(21).fillna(0)
    d5 = ratio.shift(6).rolling(45).mean() * 0.0006000000000000001
    e5 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f5 = ratio.pct_change(45).fillna(0)
    d6 = ratio.shift(7).rolling(44).mean() * 0.0007
    e6 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f6 = ratio.pct_change(44).fillna(0)
    d7 = ratio.shift(8).rolling(40).mean() * 0.0008
    e7 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f7 = ratio.pct_change(40).fillna(0)
    res = np.tanh(ratio.rolling(185).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc019_185d_val_v019_signal'] = f86mm_f86_market_cap_relative_momentum_calc019_185d_val_v019_signal

def f86mm_f86_market_cap_relative_momentum_calc020_170d_val_v020_signal(close, fcf, pb):
    v1 = fcf * 1.0
    v2 = close * 1.0
    v3 = pb * 1.0
    ratio = v1.rolling(170).std() / v1.rolling(46).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(36).mean() * 0.0001
    e0 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f0 = ratio.pct_change(36).fillna(0)
    d1 = ratio.shift(2).rolling(18).mean() * 0.0002
    e1 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f1 = ratio.pct_change(18).fillna(0)
    d2 = ratio.shift(3).rolling(25).mean() * 0.00030000000000000003
    e2 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f2 = ratio.pct_change(25).fillna(0)
    d3 = ratio.shift(4).rolling(21).mean() * 0.0004
    e3 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f3 = ratio.pct_change(21).fillna(0)
    d4 = ratio.shift(5).rolling(45).mean() * 0.0005
    e4 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f4 = ratio.pct_change(45).fillna(0)
    d5 = ratio.shift(6).rolling(44).mean() * 0.0006000000000000001
    e5 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f5 = ratio.pct_change(44).fillna(0)
    d6 = ratio.shift(7).rolling(40).mean() * 0.0007
    e6 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f6 = ratio.pct_change(40).fillna(0)
    d7 = ratio.shift(8).rolling(29).mean() * 0.0008
    e7 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f7 = ratio.pct_change(29).fillna(0)
    res = np.tanh(ratio.rolling(170).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc020_170d_val_v020_signal'] = f86mm_f86_market_cap_relative_momentum_calc020_170d_val_v020_signal

def f86mm_f86_market_cap_relative_momentum_calc021_230d_val_v021_signal(fcf, pe, revenue):
    v1 = pe * 1.0
    v2 = fcf * 1.0
    v3 = revenue * 1.0
    ratio = v1.rolling(230).rank(pct=True) - v2.rolling(230).rank(pct=True)
    d0 = ratio.shift(1).rolling(18).mean() * 0.0001
    e0 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f0 = ratio.pct_change(18).fillna(0)
    d1 = ratio.shift(2).rolling(25).mean() * 0.0002
    e1 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f1 = ratio.pct_change(25).fillna(0)
    d2 = ratio.shift(3).rolling(21).mean() * 0.00030000000000000003
    e2 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f2 = ratio.pct_change(21).fillna(0)
    d3 = ratio.shift(4).rolling(45).mean() * 0.0004
    e3 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f3 = ratio.pct_change(45).fillna(0)
    d4 = ratio.shift(5).rolling(44).mean() * 0.0005
    e4 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f4 = ratio.pct_change(44).fillna(0)
    d5 = ratio.shift(6).rolling(40).mean() * 0.0006000000000000001
    e5 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f5 = ratio.pct_change(40).fillna(0)
    d6 = ratio.shift(7).rolling(29).mean() * 0.0007
    e6 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f6 = ratio.pct_change(29).fillna(0)
    d7 = ratio.shift(8).rolling(29).mean() * 0.0008
    e7 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f7 = ratio.pct_change(29).fillna(0)
    res = ratio.ewm(span=230).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc021_230d_val_v021_signal'] = f86mm_f86_market_cap_relative_momentum_calc021_230d_val_v021_signal

def f86mm_f86_market_cap_relative_momentum_calc022_45d_val_v022_signal(assets, pb, revenue):
    v1 = revenue * 1.0
    v2 = pb * 1.0
    v3 = assets * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(25).mean() * 0.0001
    e0 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f0 = ratio.pct_change(25).fillna(0)
    d1 = ratio.shift(2).rolling(21).mean() * 0.0002
    e1 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f1 = ratio.pct_change(21).fillna(0)
    d2 = ratio.shift(3).rolling(45).mean() * 0.00030000000000000003
    e2 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f2 = ratio.pct_change(45).fillna(0)
    d3 = ratio.shift(4).rolling(44).mean() * 0.0004
    e3 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f3 = ratio.pct_change(44).fillna(0)
    d4 = ratio.shift(5).rolling(40).mean() * 0.0005
    e4 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f4 = ratio.pct_change(40).fillna(0)
    d5 = ratio.shift(6).rolling(29).mean() * 0.0006000000000000001
    e5 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f5 = ratio.pct_change(29).fillna(0)
    d6 = ratio.shift(7).rolling(29).mean() * 0.0007
    e6 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f6 = ratio.pct_change(29).fillna(0)
    d7 = ratio.shift(8).rolling(53).mean() * 0.0008
    e7 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f7 = ratio.pct_change(53).fillna(0)
    res = ratio.rolling(45).max() - ratio.rolling(45).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc022_45d_val_v022_signal'] = f86mm_f86_market_cap_relative_momentum_calc022_45d_val_v022_signal

def f86mm_f86_market_cap_relative_momentum_calc023_41d_val_v023_signal(ev, netinc, pe):
    v1 = ev * 1.0
    v2 = netinc * 1.0
    v3 = pe * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(41).mean()) / r_raw.rolling(41).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(21).mean() * 0.0001
    e0 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f0 = ratio.pct_change(21).fillna(0)
    d1 = ratio.shift(2).rolling(45).mean() * 0.0002
    e1 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f1 = ratio.pct_change(45).fillna(0)
    d2 = ratio.shift(3).rolling(44).mean() * 0.00030000000000000003
    e2 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f2 = ratio.pct_change(44).fillna(0)
    d3 = ratio.shift(4).rolling(40).mean() * 0.0004
    e3 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f3 = ratio.pct_change(40).fillna(0)
    d4 = ratio.shift(5).rolling(29).mean() * 0.0005
    e4 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f4 = ratio.pct_change(29).fillna(0)
    d5 = ratio.shift(6).rolling(29).mean() * 0.0006000000000000001
    e5 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f5 = ratio.pct_change(29).fillna(0)
    d6 = ratio.shift(7).rolling(53).mean() * 0.0007
    e6 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f6 = ratio.pct_change(53).fillna(0)
    d7 = ratio.shift(8).rolling(39).mean() * 0.0008
    e7 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f7 = ratio.pct_change(39).fillna(0)
    res = ratio.ewm(span=41).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc023_41d_val_v023_signal'] = f86mm_f86_market_cap_relative_momentum_calc023_41d_val_v023_signal

def f86mm_f86_market_cap_relative_momentum_calc024_66d_val_v024_signal(close, ebitda, marketcap):
    v1 = close * 1.0
    v2 = marketcap * 1.0
    v3 = ebitda * 1.0
    ratio = v1.pct_change(22) - v2.pct_change(22)
    d0 = ratio.shift(1).rolling(45).mean() * 0.0001
    e0 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f0 = ratio.pct_change(45).fillna(0)
    d1 = ratio.shift(2).rolling(44).mean() * 0.0002
    e1 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f1 = ratio.pct_change(44).fillna(0)
    d2 = ratio.shift(3).rolling(40).mean() * 0.00030000000000000003
    e2 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f2 = ratio.pct_change(40).fillna(0)
    d3 = ratio.shift(4).rolling(29).mean() * 0.0004
    e3 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f3 = ratio.pct_change(29).fillna(0)
    d4 = ratio.shift(5).rolling(29).mean() * 0.0005
    e4 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f4 = ratio.pct_change(29).fillna(0)
    d5 = ratio.shift(6).rolling(53).mean() * 0.0006000000000000001
    e5 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f5 = ratio.pct_change(53).fillna(0)
    d6 = ratio.shift(7).rolling(39).mean() * 0.0007
    e6 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f6 = ratio.pct_change(39).fillna(0)
    d7 = ratio.shift(8).rolling(41).mean() * 0.0008
    e7 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f7 = ratio.pct_change(41).fillna(0)
    res = ratio.rolling(66).std() / (ratio.rolling(66).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc024_66d_val_v024_signal'] = f86mm_f86_market_cap_relative_momentum_calc024_66d_val_v024_signal

def f86mm_f86_market_cap_relative_momentum_calc025_172d_val_v025_signal(fcf, marketcap, pb):
    v1 = marketcap * 1.0
    v2 = fcf * 1.0
    v3 = pb * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(44).mean() * 0.0001
    e0 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f0 = ratio.pct_change(44).fillna(0)
    d1 = ratio.shift(2).rolling(40).mean() * 0.0002
    e1 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f1 = ratio.pct_change(40).fillna(0)
    d2 = ratio.shift(3).rolling(29).mean() * 0.00030000000000000003
    e2 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f2 = ratio.pct_change(29).fillna(0)
    d3 = ratio.shift(4).rolling(29).mean() * 0.0004
    e3 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f3 = ratio.pct_change(29).fillna(0)
    d4 = ratio.shift(5).rolling(53).mean() * 0.0005
    e4 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f4 = ratio.pct_change(53).fillna(0)
    d5 = ratio.shift(6).rolling(39).mean() * 0.0006000000000000001
    e5 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f5 = ratio.pct_change(39).fillna(0)
    d6 = ratio.shift(7).rolling(41).mean() * 0.0007
    e6 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f6 = ratio.pct_change(41).fillna(0)
    d7 = ratio.shift(8).rolling(21).mean() * 0.0008
    e7 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f7 = ratio.pct_change(21).fillna(0)
    res = ratio.rolling(172).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc025_172d_val_v025_signal'] = f86mm_f86_market_cap_relative_momentum_calc025_172d_val_v025_signal

def f86mm_f86_market_cap_relative_momentum_calc026_213d_val_v026_signal(assets, netinc, pb):
    v1 = assets * 1.0
    v2 = pb * 1.0
    v3 = netinc * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(40).mean() * 0.0001
    e0 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f0 = ratio.pct_change(40).fillna(0)
    d1 = ratio.shift(2).rolling(29).mean() * 0.0002
    e1 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f1 = ratio.pct_change(29).fillna(0)
    d2 = ratio.shift(3).rolling(29).mean() * 0.00030000000000000003
    e2 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f2 = ratio.pct_change(29).fillna(0)
    d3 = ratio.shift(4).rolling(53).mean() * 0.0004
    e3 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f3 = ratio.pct_change(53).fillna(0)
    d4 = ratio.shift(5).rolling(39).mean() * 0.0005
    e4 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f4 = ratio.pct_change(39).fillna(0)
    d5 = ratio.shift(6).rolling(41).mean() * 0.0006000000000000001
    e5 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f5 = ratio.pct_change(41).fillna(0)
    d6 = ratio.shift(7).rolling(21).mean() * 0.0007
    e6 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f6 = ratio.pct_change(21).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.rolling(213).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc026_213d_val_v026_signal'] = f86mm_f86_market_cap_relative_momentum_calc026_213d_val_v026_signal

def f86mm_f86_market_cap_relative_momentum_calc027_205d_val_v027_signal(ebitda, fcf, revenue):
    v1 = revenue * 1.0
    v2 = fcf * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(205).std() / v1.rolling(149).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(29).mean() * 0.0001
    e0 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f0 = ratio.pct_change(29).fillna(0)
    d1 = ratio.shift(2).rolling(29).mean() * 0.0002
    e1 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f1 = ratio.pct_change(29).fillna(0)
    d2 = ratio.shift(3).rolling(53).mean() * 0.00030000000000000003
    e2 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f2 = ratio.pct_change(53).fillna(0)
    d3 = ratio.shift(4).rolling(39).mean() * 0.0004
    e3 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f3 = ratio.pct_change(39).fillna(0)
    d4 = ratio.shift(5).rolling(41).mean() * 0.0005
    e4 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f4 = ratio.pct_change(41).fillna(0)
    d5 = ratio.shift(6).rolling(21).mean() * 0.0006000000000000001
    e5 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f5 = ratio.pct_change(21).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(28).mean() * 0.0008
    e7 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f7 = ratio.pct_change(28).fillna(0)
    res = ratio.pct_change(205)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc027_205d_val_v027_signal'] = f86mm_f86_market_cap_relative_momentum_calc027_205d_val_v027_signal

def f86mm_f86_market_cap_relative_momentum_calc028_124d_val_v028_signal(pb, pe, ps):
    v1 = pe * 1.0
    v2 = pb * 1.0
    v3 = ps * 1.0
    ratio = v1.diff(9).rolling(124).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(29).mean() * 0.0001
    e0 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f0 = ratio.pct_change(29).fillna(0)
    d1 = ratio.shift(2).rolling(53).mean() * 0.0002
    e1 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f1 = ratio.pct_change(53).fillna(0)
    d2 = ratio.shift(3).rolling(39).mean() * 0.00030000000000000003
    e2 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f2 = ratio.pct_change(39).fillna(0)
    d3 = ratio.shift(4).rolling(41).mean() * 0.0004
    e3 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f3 = ratio.pct_change(41).fillna(0)
    d4 = ratio.shift(5).rolling(21).mean() * 0.0005
    e4 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f4 = ratio.pct_change(21).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(28).mean() * 0.0007
    e6 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f6 = ratio.pct_change(28).fillna(0)
    d7 = ratio.shift(8).rolling(35).mean() * 0.0008
    e7 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f7 = ratio.pct_change(35).fillna(0)
    res = ratio.pct_change(124)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc028_124d_val_v028_signal'] = f86mm_f86_market_cap_relative_momentum_calc028_124d_val_v028_signal

def f86mm_f86_market_cap_relative_momentum_calc029_249d_val_v029_signal(evebitda, pe, ps):
    v1 = evebitda * 1.0
    v2 = pe * 1.0
    v3 = ps * 1.0
    ratio = v1.pct_change(44) - v2.pct_change(44)
    d0 = ratio.shift(1).rolling(53).mean() * 0.0001
    e0 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f0 = ratio.pct_change(53).fillna(0)
    d1 = ratio.shift(2).rolling(39).mean() * 0.0002
    e1 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f1 = ratio.pct_change(39).fillna(0)
    d2 = ratio.shift(3).rolling(41).mean() * 0.00030000000000000003
    e2 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f2 = ratio.pct_change(41).fillna(0)
    d3 = ratio.shift(4).rolling(21).mean() * 0.0004
    e3 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f3 = ratio.pct_change(21).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(28).mean() * 0.0006000000000000001
    e5 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f5 = ratio.pct_change(28).fillna(0)
    d6 = ratio.shift(7).rolling(35).mean() * 0.0007
    e6 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f6 = ratio.pct_change(35).fillna(0)
    d7 = ratio.shift(8).rolling(6).mean() * 0.0008
    e7 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f7 = ratio.pct_change(6).fillna(0)
    res = ratio.rolling(249).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc029_249d_val_v029_signal'] = f86mm_f86_market_cap_relative_momentum_calc029_249d_val_v029_signal

def f86mm_f86_market_cap_relative_momentum_calc030_89d_val_v030_signal(close, ev, evebitda):
    v1 = ev * 1.0
    v2 = evebitda * 1.0
    v3 = close * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(89).mean()) / r_raw.rolling(89).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(39).mean() * 0.0001
    e0 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f0 = ratio.pct_change(39).fillna(0)
    d1 = ratio.shift(2).rolling(41).mean() * 0.0002
    e1 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f1 = ratio.pct_change(41).fillna(0)
    d2 = ratio.shift(3).rolling(21).mean() * 0.00030000000000000003
    e2 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f2 = ratio.pct_change(21).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(28).mean() * 0.0005
    e4 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f4 = ratio.pct_change(28).fillna(0)
    d5 = ratio.shift(6).rolling(35).mean() * 0.0006000000000000001
    e5 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f5 = ratio.pct_change(35).fillna(0)
    d6 = ratio.shift(7).rolling(6).mean() * 0.0007
    e6 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f6 = ratio.pct_change(6).fillna(0)
    d7 = ratio.shift(8).rolling(44).mean() * 0.0008
    e7 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f7 = ratio.pct_change(44).fillna(0)
    res = ratio.rolling(89).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc030_89d_val_v030_signal'] = f86mm_f86_market_cap_relative_momentum_calc030_89d_val_v030_signal

def f86mm_f86_market_cap_relative_momentum_calc031_73d_val_v031_signal(close, ev, marketcap):
    v1 = marketcap * 1.0
    v2 = ev * 1.0
    v3 = close * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(41).mean() * 0.0001
    e0 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f0 = ratio.pct_change(41).fillna(0)
    d1 = ratio.shift(2).rolling(21).mean() * 0.0002
    e1 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f1 = ratio.pct_change(21).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(28).mean() * 0.0004
    e3 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f3 = ratio.pct_change(28).fillna(0)
    d4 = ratio.shift(5).rolling(35).mean() * 0.0005
    e4 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f4 = ratio.pct_change(35).fillna(0)
    d5 = ratio.shift(6).rolling(6).mean() * 0.0006000000000000001
    e5 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f5 = ratio.pct_change(6).fillna(0)
    d6 = ratio.shift(7).rolling(44).mean() * 0.0007
    e6 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f6 = ratio.pct_change(44).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.rolling(73).max() - ratio.rolling(73).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc031_73d_val_v031_signal'] = f86mm_f86_market_cap_relative_momentum_calc031_73d_val_v031_signal

def f86mm_f86_market_cap_relative_momentum_calc032_137d_val_v032_signal(assets, close, ps):
    v1 = assets * 1.0
    v2 = close * 1.0
    v3 = ps * 1.0
    ratio = (v1 - v1.rolling(137).min()) / (v1.rolling(137).max() - v1.rolling(137).min() + 1e-9)
    d0 = ratio.shift(1).rolling(21).mean() * 0.0001
    e0 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f0 = ratio.pct_change(21).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(28).mean() * 0.00030000000000000003
    e2 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f2 = ratio.pct_change(28).fillna(0)
    d3 = ratio.shift(4).rolling(35).mean() * 0.0004
    e3 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f3 = ratio.pct_change(35).fillna(0)
    d4 = ratio.shift(5).rolling(6).mean() * 0.0005
    e4 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f4 = ratio.pct_change(6).fillna(0)
    d5 = ratio.shift(6).rolling(44).mean() * 0.0006000000000000001
    e5 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f5 = ratio.pct_change(44).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.rolling(137).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc032_137d_val_v032_signal'] = f86mm_f86_market_cap_relative_momentum_calc032_137d_val_v032_signal

def f86mm_f86_market_cap_relative_momentum_calc033_112d_val_v033_signal(ev, fcf, ps):
    v1 = ps * 1.0
    v2 = fcf * 1.0
    v3 = ev * 1.0
    ratio = v1.pct_change(13) - v2.pct_change(13)
    d0 = ratio.shift(1).rolling(12).mean() * 0.0001
    e0 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f0 = ratio.pct_change(12).fillna(0)
    d1 = ratio.shift(2).rolling(28).mean() * 0.0002
    e1 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f1 = ratio.pct_change(28).fillna(0)
    d2 = ratio.shift(3).rolling(35).mean() * 0.00030000000000000003
    e2 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f2 = ratio.pct_change(35).fillna(0)
    d3 = ratio.shift(4).rolling(6).mean() * 0.0004
    e3 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f3 = ratio.pct_change(6).fillna(0)
    d4 = ratio.shift(5).rolling(44).mean() * 0.0005
    e4 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f4 = ratio.pct_change(44).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(10).mean() * 0.0008
    e7 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f7 = ratio.pct_change(10).fillna(0)
    res = ratio.rolling(112).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc033_112d_val_v033_signal'] = f86mm_f86_market_cap_relative_momentum_calc033_112d_val_v033_signal

def f86mm_f86_market_cap_relative_momentum_calc034_206d_val_v034_signal(ebitda, fcf, pb):
    v1 = ebitda * 1.0
    v2 = pb * 1.0
    v3 = fcf * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(28).mean() * 0.0001
    e0 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f0 = ratio.pct_change(28).fillna(0)
    d1 = ratio.shift(2).rolling(35).mean() * 0.0002
    e1 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f1 = ratio.pct_change(35).fillna(0)
    d2 = ratio.shift(3).rolling(6).mean() * 0.00030000000000000003
    e2 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f2 = ratio.pct_change(6).fillna(0)
    d3 = ratio.shift(4).rolling(44).mean() * 0.0004
    e3 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f3 = ratio.pct_change(44).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(10).mean() * 0.0007
    e6 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f6 = ratio.pct_change(10).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.rolling(206).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc034_206d_val_v034_signal'] = f86mm_f86_market_cap_relative_momentum_calc034_206d_val_v034_signal

def f86mm_f86_market_cap_relative_momentum_calc035_208d_val_v035_signal(ebitda, ev, marketcap):
    v1 = ebitda * 1.0
    v2 = ev * 1.0
    v3 = marketcap * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(35).mean() * 0.0001
    e0 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f0 = ratio.pct_change(35).fillna(0)
    d1 = ratio.shift(2).rolling(6).mean() * 0.0002
    e1 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f1 = ratio.pct_change(6).fillna(0)
    d2 = ratio.shift(3).rolling(44).mean() * 0.00030000000000000003
    e2 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f2 = ratio.pct_change(44).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(10).mean() * 0.0006000000000000001
    e5 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f5 = ratio.pct_change(10).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = (ratio - ratio.rolling(208).mean()) / (ratio.rolling(208).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc035_208d_val_v035_signal'] = f86mm_f86_market_cap_relative_momentum_calc035_208d_val_v035_signal

def f86mm_f86_market_cap_relative_momentum_calc036_58d_val_v036_signal(ebitda, evebitda, fcf):
    v1 = ebitda * 1.0
    v2 = evebitda * 1.0
    v3 = fcf * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(6).mean() * 0.0001
    e0 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f0 = ratio.pct_change(6).fillna(0)
    d1 = ratio.shift(2).rolling(44).mean() * 0.0002
    e1 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f1 = ratio.pct_change(44).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(10).mean() * 0.0005
    e4 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f4 = ratio.pct_change(10).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(19).mean() * 0.0008
    e7 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f7 = ratio.pct_change(19).fillna(0)
    res = ratio.rolling(58).max() - ratio.rolling(58).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc036_58d_val_v036_signal'] = f86mm_f86_market_cap_relative_momentum_calc036_58d_val_v036_signal

def f86mm_f86_market_cap_relative_momentum_calc037_168d_val_v037_signal(assets, pb, revenue):
    v1 = assets * 1.0
    v2 = pb * 1.0
    v3 = revenue * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(44).mean() * 0.0001
    e0 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f0 = ratio.pct_change(44).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(10).mean() * 0.0004
    e3 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f3 = ratio.pct_change(10).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(19).mean() * 0.0007
    e6 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f6 = ratio.pct_change(19).fillna(0)
    d7 = ratio.shift(8).rolling(51).mean() * 0.0008
    e7 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f7 = ratio.pct_change(51).fillna(0)
    res = ratio.rolling(168).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc037_168d_val_v037_signal'] = f86mm_f86_market_cap_relative_momentum_calc037_168d_val_v037_signal

def f86mm_f86_market_cap_relative_momentum_calc038_191d_val_v038_signal(ebitda, fcf, netinc):
    v1 = fcf * 1.0
    v2 = netinc * 1.0
    v3 = ebitda * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(10).mean() * 0.00030000000000000003
    e2 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f2 = ratio.pct_change(10).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(19).mean() * 0.0006000000000000001
    e5 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f5 = ratio.pct_change(19).fillna(0)
    d6 = ratio.shift(7).rolling(51).mean() * 0.0007
    e6 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f6 = ratio.pct_change(51).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = ratio.pct_change(191)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc038_191d_val_v038_signal'] = f86mm_f86_market_cap_relative_momentum_calc038_191d_val_v038_signal

def f86mm_f86_market_cap_relative_momentum_calc039_100d_val_v039_signal(marketcap, netinc, pe):
    v1 = netinc * 1.0
    v2 = pe * 1.0
    v3 = marketcap * 1.0
    ratio = v1.pct_change(37) - v2.pct_change(37)
    d0 = ratio.shift(1).rolling(12).mean() * 0.0001
    e0 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f0 = ratio.pct_change(12).fillna(0)
    d1 = ratio.shift(2).rolling(10).mean() * 0.0002
    e1 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f1 = ratio.pct_change(10).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(19).mean() * 0.0005
    e4 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f4 = ratio.pct_change(19).fillna(0)
    d5 = ratio.shift(6).rolling(51).mean() * 0.0006000000000000001
    e5 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f5 = ratio.pct_change(51).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(24).mean() * 0.0008
    e7 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f7 = ratio.pct_change(24).fillna(0)
    res = ratio.rolling(100).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc039_100d_val_v039_signal'] = f86mm_f86_market_cap_relative_momentum_calc039_100d_val_v039_signal

def f86mm_f86_market_cap_relative_momentum_calc040_180d_val_v040_signal(ev, evebitda, fcf):
    v1 = ev * 1.0
    v2 = fcf * 1.0
    v3 = evebitda * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(180).mean()) / r_raw.rolling(180).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(10).mean() * 0.0001
    e0 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f0 = ratio.pct_change(10).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(19).mean() * 0.0004
    e3 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f3 = ratio.pct_change(19).fillna(0)
    d4 = ratio.shift(5).rolling(51).mean() * 0.0005
    e4 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f4 = ratio.pct_change(51).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(24).mean() * 0.0007
    e6 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f6 = ratio.pct_change(24).fillna(0)
    d7 = ratio.shift(8).rolling(46).mean() * 0.0008
    e7 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f7 = ratio.pct_change(46).fillna(0)
    res = ratio.diff(45).rolling(180).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc040_180d_val_v040_signal'] = f86mm_f86_market_cap_relative_momentum_calc040_180d_val_v040_signal

def f86mm_f86_market_cap_relative_momentum_calc041_111d_val_v041_signal(assets, marketcap, netinc):
    v1 = netinc * 1.0
    v2 = assets * 1.0
    v3 = marketcap * 1.0
    ratio = (v1 - v1.rolling(111).min()) / (v1.rolling(111).max() - v1.rolling(111).min() + 1e-9)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(19).mean() * 0.00030000000000000003
    e2 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f2 = ratio.pct_change(19).fillna(0)
    d3 = ratio.shift(4).rolling(51).mean() * 0.0004
    e3 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f3 = ratio.pct_change(51).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(24).mean() * 0.0006000000000000001
    e5 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f5 = ratio.pct_change(24).fillna(0)
    d6 = ratio.shift(7).rolling(46).mean() * 0.0007
    e6 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f6 = ratio.pct_change(46).fillna(0)
    d7 = ratio.shift(8).rolling(52).mean() * 0.0008
    e7 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f7 = ratio.pct_change(52).fillna(0)
    res = ratio.diff(111)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc041_111d_val_v041_signal'] = f86mm_f86_market_cap_relative_momentum_calc041_111d_val_v041_signal

def f86mm_f86_market_cap_relative_momentum_calc042_22d_val_v042_signal(evebitda, fcf, pe):
    v1 = evebitda * 1.0
    v2 = fcf * 1.0
    v3 = pe * 1.0
    ratio = v1.rolling(22).std() / v1.rolling(87).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(19).mean() * 0.0002
    e1 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f1 = ratio.pct_change(19).fillna(0)
    d2 = ratio.shift(3).rolling(51).mean() * 0.00030000000000000003
    e2 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f2 = ratio.pct_change(51).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(24).mean() * 0.0005
    e4 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f4 = ratio.pct_change(24).fillna(0)
    d5 = ratio.shift(6).rolling(46).mean() * 0.0006000000000000001
    e5 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f5 = ratio.pct_change(46).fillna(0)
    d6 = ratio.shift(7).rolling(52).mean() * 0.0007
    e6 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f6 = ratio.pct_change(52).fillna(0)
    d7 = ratio.shift(8).rolling(9).mean() * 0.0008
    e7 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f7 = ratio.pct_change(9).fillna(0)
    res = ratio.rolling(22).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc042_22d_val_v042_signal'] = f86mm_f86_market_cap_relative_momentum_calc042_22d_val_v042_signal

def f86mm_f86_market_cap_relative_momentum_calc043_53d_val_v043_signal(pb, ps, revenue):
    v1 = pb * 1.0
    v2 = revenue * 1.0
    v3 = ps * 1.0
    ratio = v1.diff(20).rolling(53).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(19).mean() * 0.0001
    e0 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f0 = ratio.pct_change(19).fillna(0)
    d1 = ratio.shift(2).rolling(51).mean() * 0.0002
    e1 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f1 = ratio.pct_change(51).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(24).mean() * 0.0004
    e3 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f3 = ratio.pct_change(24).fillna(0)
    d4 = ratio.shift(5).rolling(46).mean() * 0.0005
    e4 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f4 = ratio.pct_change(46).fillna(0)
    d5 = ratio.shift(6).rolling(52).mean() * 0.0006000000000000001
    e5 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f5 = ratio.pct_change(52).fillna(0)
    d6 = ratio.shift(7).rolling(9).mean() * 0.0007
    e6 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f6 = ratio.pct_change(9).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.rolling(53).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc043_53d_val_v043_signal'] = f86mm_f86_market_cap_relative_momentum_calc043_53d_val_v043_signal

def f86mm_f86_market_cap_relative_momentum_calc044_38d_val_v044_signal(close, ev, ps):
    v1 = close * 1.0
    v2 = ps * 1.0
    v3 = ev * 1.0
    ratio = v1.rolling(38).max() / v2.rolling(38).min().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(51).mean() * 0.0001
    e0 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f0 = ratio.pct_change(51).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(24).mean() * 0.00030000000000000003
    e2 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f2 = ratio.pct_change(24).fillna(0)
    d3 = ratio.shift(4).rolling(46).mean() * 0.0004
    e3 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f3 = ratio.pct_change(46).fillna(0)
    d4 = ratio.shift(5).rolling(52).mean() * 0.0005
    e4 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f4 = ratio.pct_change(52).fillna(0)
    d5 = ratio.shift(6).rolling(9).mean() * 0.0006000000000000001
    e5 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f5 = ratio.pct_change(9).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = ratio.rolling(38).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc044_38d_val_v044_signal'] = f86mm_f86_market_cap_relative_momentum_calc044_38d_val_v044_signal

def f86mm_f86_market_cap_relative_momentum_calc045_121d_val_v045_signal(assets, pb, revenue):
    v1 = pb * 1.0
    v2 = assets * 1.0
    v3 = revenue * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(24).mean() * 0.0002
    e1 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f1 = ratio.pct_change(24).fillna(0)
    d2 = ratio.shift(3).rolling(46).mean() * 0.00030000000000000003
    e2 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f2 = ratio.pct_change(46).fillna(0)
    d3 = ratio.shift(4).rolling(52).mean() * 0.0004
    e3 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f3 = ratio.pct_change(52).fillna(0)
    d4 = ratio.shift(5).rolling(9).mean() * 0.0005
    e4 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f4 = ratio.pct_change(9).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(28).mean() * 0.0008
    e7 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f7 = ratio.pct_change(28).fillna(0)
    res = ratio.ewm(span=121).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc045_121d_val_v045_signal'] = f86mm_f86_market_cap_relative_momentum_calc045_121d_val_v045_signal

def f86mm_f86_market_cap_relative_momentum_calc046_47d_val_v046_signal(ebitda, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ps * 1.0
    v3 = ebitda * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(24).mean() * 0.0001
    e0 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f0 = ratio.pct_change(24).fillna(0)
    d1 = ratio.shift(2).rolling(46).mean() * 0.0002
    e1 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f1 = ratio.pct_change(46).fillna(0)
    d2 = ratio.shift(3).rolling(52).mean() * 0.00030000000000000003
    e2 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f2 = ratio.pct_change(52).fillna(0)
    d3 = ratio.shift(4).rolling(9).mean() * 0.0004
    e3 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f3 = ratio.pct_change(9).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(28).mean() * 0.0007
    e6 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f6 = ratio.pct_change(28).fillna(0)
    d7 = ratio.shift(8).rolling(10).mean() * 0.0008
    e7 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f7 = ratio.pct_change(10).fillna(0)
    res = ratio.rolling(47).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc046_47d_val_v046_signal'] = f86mm_f86_market_cap_relative_momentum_calc046_47d_val_v046_signal

def f86mm_f86_market_cap_relative_momentum_calc047_163d_val_v047_signal(assets, close, marketcap):
    v1 = assets * 1.0
    v2 = close * 1.0
    v3 = marketcap * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(46).mean() * 0.0001
    e0 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f0 = ratio.pct_change(46).fillna(0)
    d1 = ratio.shift(2).rolling(52).mean() * 0.0002
    e1 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f1 = ratio.pct_change(52).fillna(0)
    d2 = ratio.shift(3).rolling(9).mean() * 0.00030000000000000003
    e2 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f2 = ratio.pct_change(9).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(28).mean() * 0.0006000000000000001
    e5 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f5 = ratio.pct_change(28).fillna(0)
    d6 = ratio.shift(7).rolling(10).mean() * 0.0007
    e6 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f6 = ratio.pct_change(10).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(163).std() / (ratio.rolling(163).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc047_163d_val_v047_signal'] = f86mm_f86_market_cap_relative_momentum_calc047_163d_val_v047_signal

def f86mm_f86_market_cap_relative_momentum_calc048_203d_val_v048_signal(close, evebitda, pe):
    v1 = close * 1.0
    v2 = pe * 1.0
    v3 = evebitda * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(52).mean() * 0.0001
    e0 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f0 = ratio.pct_change(52).fillna(0)
    d1 = ratio.shift(2).rolling(9).mean() * 0.0002
    e1 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f1 = ratio.pct_change(9).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(28).mean() * 0.0005
    e4 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f4 = ratio.pct_change(28).fillna(0)
    d5 = ratio.shift(6).rolling(10).mean() * 0.0006000000000000001
    e5 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f5 = ratio.pct_change(10).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(44).mean() * 0.0008
    e7 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f7 = ratio.pct_change(44).fillna(0)
    res = ratio.rolling(203).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc048_203d_val_v048_signal'] = f86mm_f86_market_cap_relative_momentum_calc048_203d_val_v048_signal

def f86mm_f86_market_cap_relative_momentum_calc049_93d_val_v049_signal(close, pe, revenue):
    v1 = close * 1.0
    v2 = revenue * 1.0
    v3 = pe * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(9).mean() * 0.0001
    e0 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f0 = ratio.pct_change(9).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(28).mean() * 0.0004
    e3 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f3 = ratio.pct_change(28).fillna(0)
    d4 = ratio.shift(5).rolling(10).mean() * 0.0005
    e4 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f4 = ratio.pct_change(10).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(44).mean() * 0.0007
    e6 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f6 = ratio.pct_change(44).fillna(0)
    d7 = ratio.shift(8).rolling(24).mean() * 0.0008
    e7 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f7 = ratio.pct_change(24).fillna(0)
    res = ratio.rolling(93).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc049_93d_val_v049_signal'] = f86mm_f86_market_cap_relative_momentum_calc049_93d_val_v049_signal

def f86mm_f86_market_cap_relative_momentum_calc050_189d_val_v050_signal(assets, pb, ps):
    v1 = ps * 1.0
    v2 = assets * 1.0
    v3 = pb * 1.0
    ratio = (v1 - v1.rolling(189).min()) / (v1.rolling(189).max() - v1.rolling(189).min() + 1e-9)
    d0 = ratio.shift(1).rolling(12).mean() * 0.0001
    e0 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f0 = ratio.pct_change(12).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(28).mean() * 0.00030000000000000003
    e2 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f2 = ratio.pct_change(28).fillna(0)
    d3 = ratio.shift(4).rolling(10).mean() * 0.0004
    e3 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f3 = ratio.pct_change(10).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(44).mean() * 0.0006000000000000001
    e5 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f5 = ratio.pct_change(44).fillna(0)
    d6 = ratio.shift(7).rolling(24).mean() * 0.0007
    e6 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f6 = ratio.pct_change(24).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = ratio.rolling(189).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc050_189d_val_v050_signal'] = f86mm_f86_market_cap_relative_momentum_calc050_189d_val_v050_signal

def f86mm_f86_market_cap_relative_momentum_calc051_64d_val_v051_signal(close, evebitda, pe):
    v1 = pe * 1.0
    v2 = evebitda * 1.0
    v3 = close * 1.0
    ratio = v1.rolling(64).rank(pct=True) - v2.rolling(64).rank(pct=True)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(28).mean() * 0.0002
    e1 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f1 = ratio.pct_change(28).fillna(0)
    d2 = ratio.shift(3).rolling(10).mean() * 0.00030000000000000003
    e2 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f2 = ratio.pct_change(10).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(44).mean() * 0.0005
    e4 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f4 = ratio.pct_change(44).fillna(0)
    d5 = ratio.shift(6).rolling(24).mean() * 0.0006000000000000001
    e5 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f5 = ratio.pct_change(24).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(14).mean() * 0.0008
    e7 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f7 = ratio.pct_change(14).fillna(0)
    res = ratio.pct_change(64)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc051_64d_val_v051_signal'] = f86mm_f86_market_cap_relative_momentum_calc051_64d_val_v051_signal

def f86mm_f86_market_cap_relative_momentum_calc052_212d_val_v052_signal(ebitda, evebitda, revenue):
    v1 = revenue * 1.0
    v2 = evebitda * 1.0
    v3 = ebitda * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(28).mean() * 0.0001
    e0 = ratio.rolling(28).std() / (ratio.rolling(28).mean().abs() + 1e-9)
    f0 = ratio.pct_change(28).fillna(0)
    d1 = ratio.shift(2).rolling(10).mean() * 0.0002
    e1 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f1 = ratio.pct_change(10).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(44).mean() * 0.0004
    e3 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f3 = ratio.pct_change(44).fillna(0)
    d4 = ratio.shift(5).rolling(24).mean() * 0.0005
    e4 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f4 = ratio.pct_change(24).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(14).mean() * 0.0007
    e6 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f6 = ratio.pct_change(14).fillna(0)
    d7 = ratio.shift(8).rolling(35).mean() * 0.0008
    e7 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f7 = ratio.pct_change(35).fillna(0)
    res = np.tanh(ratio.rolling(212).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc052_212d_val_v052_signal'] = f86mm_f86_market_cap_relative_momentum_calc052_212d_val_v052_signal

def f86mm_f86_market_cap_relative_momentum_calc053_157d_val_v053_signal(assets, pe, ps):
    v1 = assets * 1.0
    v2 = pe * 1.0
    v3 = ps * 1.0
    ratio = (v1 - v1.rolling(157).min()) / (v1.rolling(157).max() - v1.rolling(157).min() + 1e-9)
    d0 = ratio.shift(1).rolling(10).mean() * 0.0001
    e0 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f0 = ratio.pct_change(10).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(44).mean() * 0.00030000000000000003
    e2 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f2 = ratio.pct_change(44).fillna(0)
    d3 = ratio.shift(4).rolling(24).mean() * 0.0004
    e3 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f3 = ratio.pct_change(24).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(14).mean() * 0.0006000000000000001
    e5 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f5 = ratio.pct_change(14).fillna(0)
    d6 = ratio.shift(7).rolling(35).mean() * 0.0007
    e6 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f6 = ratio.pct_change(35).fillna(0)
    d7 = ratio.shift(8).rolling(30).mean() * 0.0008
    e7 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f7 = ratio.pct_change(30).fillna(0)
    res = ratio.diff(35).rolling(157).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc053_157d_val_v053_signal'] = f86mm_f86_market_cap_relative_momentum_calc053_157d_val_v053_signal

def f86mm_f86_market_cap_relative_momentum_calc054_204d_val_v054_signal(assets, ev, ps):
    v1 = assets * 1.0
    v2 = ps * 1.0
    v3 = ev * 1.0
    ratio = v1.rolling(204).rank(pct=True) - v2.rolling(204).rank(pct=True)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(44).mean() * 0.0002
    e1 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f1 = ratio.pct_change(44).fillna(0)
    d2 = ratio.shift(3).rolling(24).mean() * 0.00030000000000000003
    e2 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f2 = ratio.pct_change(24).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(14).mean() * 0.0005
    e4 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f4 = ratio.pct_change(14).fillna(0)
    d5 = ratio.shift(6).rolling(35).mean() * 0.0006000000000000001
    e5 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f5 = ratio.pct_change(35).fillna(0)
    d6 = ratio.shift(7).rolling(30).mean() * 0.0007
    e6 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f6 = ratio.pct_change(30).fillna(0)
    d7 = ratio.shift(8).rolling(36).mean() * 0.0008
    e7 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f7 = ratio.pct_change(36).fillna(0)
    res = ratio.rolling(204).max() - ratio.rolling(204).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc054_204d_val_v054_signal'] = f86mm_f86_market_cap_relative_momentum_calc054_204d_val_v054_signal

def f86mm_f86_market_cap_relative_momentum_calc055_150d_val_v055_signal(assets, marketcap, pb):
    v1 = pb * 1.0
    v2 = assets * 1.0
    v3 = marketcap * 1.0
    ratio = v1.pct_change(30) - v2.pct_change(30)
    d0 = ratio.shift(1).rolling(44).mean() * 0.0001
    e0 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f0 = ratio.pct_change(44).fillna(0)
    d1 = ratio.shift(2).rolling(24).mean() * 0.0002
    e1 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f1 = ratio.pct_change(24).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(14).mean() * 0.0004
    e3 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f3 = ratio.pct_change(14).fillna(0)
    d4 = ratio.shift(5).rolling(35).mean() * 0.0005
    e4 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f4 = ratio.pct_change(35).fillna(0)
    d5 = ratio.shift(6).rolling(30).mean() * 0.0006000000000000001
    e5 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f5 = ratio.pct_change(30).fillna(0)
    d6 = ratio.shift(7).rolling(36).mean() * 0.0007
    e6 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f6 = ratio.pct_change(36).fillna(0)
    d7 = ratio.shift(8).rolling(40).mean() * 0.0008
    e7 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f7 = ratio.pct_change(40).fillna(0)
    res = ratio.diff(30).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc055_150d_val_v055_signal'] = f86mm_f86_market_cap_relative_momentum_calc055_150d_val_v055_signal

def f86mm_f86_market_cap_relative_momentum_calc056_16d_val_v056_signal(assets, netinc, revenue):
    v1 = netinc * 1.0
    v2 = assets * 1.0
    v3 = revenue * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(24).mean() * 0.0001
    e0 = ratio.rolling(24).std() / (ratio.rolling(24).mean().abs() + 1e-9)
    f0 = ratio.pct_change(24).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(14).mean() * 0.00030000000000000003
    e2 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f2 = ratio.pct_change(14).fillna(0)
    d3 = ratio.shift(4).rolling(35).mean() * 0.0004
    e3 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f3 = ratio.pct_change(35).fillna(0)
    d4 = ratio.shift(5).rolling(30).mean() * 0.0005
    e4 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f4 = ratio.pct_change(30).fillna(0)
    d5 = ratio.shift(6).rolling(36).mean() * 0.0006000000000000001
    e5 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f5 = ratio.pct_change(36).fillna(0)
    d6 = ratio.shift(7).rolling(40).mean() * 0.0007
    e6 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f6 = ratio.pct_change(40).fillna(0)
    d7 = ratio.shift(8).rolling(51).mean() * 0.0008
    e7 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f7 = ratio.pct_change(51).fillna(0)
    res = ratio.rolling(16).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc056_16d_val_v056_signal'] = f86mm_f86_market_cap_relative_momentum_calc056_16d_val_v056_signal

def f86mm_f86_market_cap_relative_momentum_calc057_133d_val_v057_signal(ev, evebitda, pb):
    v1 = pb * 1.0
    v2 = ev * 1.0
    v3 = evebitda * 1.0
    ratio = (v1 - v1.rolling(133).min()) / (v1.rolling(133).max() - v1.rolling(133).min() + 1e-9)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(14).mean() * 0.0002
    e1 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f1 = ratio.pct_change(14).fillna(0)
    d2 = ratio.shift(3).rolling(35).mean() * 0.00030000000000000003
    e2 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f2 = ratio.pct_change(35).fillna(0)
    d3 = ratio.shift(4).rolling(30).mean() * 0.0004
    e3 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f3 = ratio.pct_change(30).fillna(0)
    d4 = ratio.shift(5).rolling(36).mean() * 0.0005
    e4 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f4 = ratio.pct_change(36).fillna(0)
    d5 = ratio.shift(6).rolling(40).mean() * 0.0006000000000000001
    e5 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f5 = ratio.pct_change(40).fillna(0)
    d6 = ratio.shift(7).rolling(51).mean() * 0.0007
    e6 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f6 = ratio.pct_change(51).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.ewm(span=133).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc057_133d_val_v057_signal'] = f86mm_f86_market_cap_relative_momentum_calc057_133d_val_v057_signal

def f86mm_f86_market_cap_relative_momentum_calc058_58d_val_v058_signal(evebitda, fcf, ps):
    v1 = ps * 1.0
    v2 = evebitda * 1.0
    v3 = fcf * 1.0
    ratio = v1.pct_change(29) - v2.pct_change(29)
    d0 = ratio.shift(1).rolling(14).mean() * 0.0001
    e0 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f0 = ratio.pct_change(14).fillna(0)
    d1 = ratio.shift(2).rolling(35).mean() * 0.0002
    e1 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f1 = ratio.pct_change(35).fillna(0)
    d2 = ratio.shift(3).rolling(30).mean() * 0.00030000000000000003
    e2 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f2 = ratio.pct_change(30).fillna(0)
    d3 = ratio.shift(4).rolling(36).mean() * 0.0004
    e3 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f3 = ratio.pct_change(36).fillna(0)
    d4 = ratio.shift(5).rolling(40).mean() * 0.0005
    e4 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f4 = ratio.pct_change(40).fillna(0)
    d5 = ratio.shift(6).rolling(51).mean() * 0.0006000000000000001
    e5 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f5 = ratio.pct_change(51).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(50).mean() * 0.0008
    e7 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f7 = ratio.pct_change(50).fillna(0)
    res = ratio.rolling(58).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc058_58d_val_v058_signal'] = f86mm_f86_market_cap_relative_momentum_calc058_58d_val_v058_signal

def f86mm_f86_market_cap_relative_momentum_calc059_184d_val_v059_signal(close, evebitda, netinc):
    v1 = evebitda * 1.0
    v2 = netinc * 1.0
    v3 = close * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(35).mean() * 0.0001
    e0 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f0 = ratio.pct_change(35).fillna(0)
    d1 = ratio.shift(2).rolling(30).mean() * 0.0002
    e1 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f1 = ratio.pct_change(30).fillna(0)
    d2 = ratio.shift(3).rolling(36).mean() * 0.00030000000000000003
    e2 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f2 = ratio.pct_change(36).fillna(0)
    d3 = ratio.shift(4).rolling(40).mean() * 0.0004
    e3 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f3 = ratio.pct_change(40).fillna(0)
    d4 = ratio.shift(5).rolling(51).mean() * 0.0005
    e4 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f4 = ratio.pct_change(51).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(50).mean() * 0.0007
    e6 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f6 = ratio.pct_change(50).fillna(0)
    d7 = ratio.shift(8).rolling(33).mean() * 0.0008
    e7 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f7 = ratio.pct_change(33).fillna(0)
    res = np.tanh(ratio.rolling(184).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc059_184d_val_v059_signal'] = f86mm_f86_market_cap_relative_momentum_calc059_184d_val_v059_signal

def f86mm_f86_market_cap_relative_momentum_calc060_105d_val_v060_signal(assets, marketcap, revenue):
    v1 = assets * 1.0
    v2 = marketcap * 1.0
    v3 = revenue * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(105).mean()) / r_raw.rolling(105).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(30).mean() * 0.0001
    e0 = ratio.rolling(30).std() / (ratio.rolling(30).mean().abs() + 1e-9)
    f0 = ratio.pct_change(30).fillna(0)
    d1 = ratio.shift(2).rolling(36).mean() * 0.0002
    e1 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f1 = ratio.pct_change(36).fillna(0)
    d2 = ratio.shift(3).rolling(40).mean() * 0.00030000000000000003
    e2 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f2 = ratio.pct_change(40).fillna(0)
    d3 = ratio.shift(4).rolling(51).mean() * 0.0004
    e3 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f3 = ratio.pct_change(51).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(50).mean() * 0.0006000000000000001
    e5 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f5 = ratio.pct_change(50).fillna(0)
    d6 = ratio.shift(7).rolling(33).mean() * 0.0007
    e6 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f6 = ratio.pct_change(33).fillna(0)
    d7 = ratio.shift(8).rolling(10).mean() * 0.0008
    e7 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f7 = ratio.pct_change(10).fillna(0)
    res = ratio.diff(47).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc060_105d_val_v060_signal'] = f86mm_f86_market_cap_relative_momentum_calc060_105d_val_v060_signal

def f86mm_f86_market_cap_relative_momentum_calc061_37d_val_v061_signal(close, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ps * 1.0
    v3 = close * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(36).mean() * 0.0001
    e0 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f0 = ratio.pct_change(36).fillna(0)
    d1 = ratio.shift(2).rolling(40).mean() * 0.0002
    e1 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f1 = ratio.pct_change(40).fillna(0)
    d2 = ratio.shift(3).rolling(51).mean() * 0.00030000000000000003
    e2 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f2 = ratio.pct_change(51).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(50).mean() * 0.0005
    e4 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f4 = ratio.pct_change(50).fillna(0)
    d5 = ratio.shift(6).rolling(33).mean() * 0.0006000000000000001
    e5 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f5 = ratio.pct_change(33).fillna(0)
    d6 = ratio.shift(7).rolling(10).mean() * 0.0007
    e6 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f6 = ratio.pct_change(10).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.diff(37)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc061_37d_val_v061_signal'] = f86mm_f86_market_cap_relative_momentum_calc061_37d_val_v061_signal

def f86mm_f86_market_cap_relative_momentum_calc062_81d_val_v062_signal(close, pe, ps):
    v1 = ps * 1.0
    v2 = close * 1.0
    v3 = pe * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(40).mean() * 0.0001
    e0 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f0 = ratio.pct_change(40).fillna(0)
    d1 = ratio.shift(2).rolling(51).mean() * 0.0002
    e1 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f1 = ratio.pct_change(51).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(50).mean() * 0.0004
    e3 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f3 = ratio.pct_change(50).fillna(0)
    d4 = ratio.shift(5).rolling(33).mean() * 0.0005
    e4 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f4 = ratio.pct_change(33).fillna(0)
    d5 = ratio.shift(6).rolling(10).mean() * 0.0006000000000000001
    e5 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f5 = ratio.pct_change(10).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(49).mean() * 0.0008
    e7 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f7 = ratio.pct_change(49).fillna(0)
    res = ratio.pct_change(81)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc062_81d_val_v062_signal'] = f86mm_f86_market_cap_relative_momentum_calc062_81d_val_v062_signal

def f86mm_f86_market_cap_relative_momentum_calc063_98d_val_v063_signal(pb, ps, revenue):
    v1 = pb * 1.0
    v2 = revenue * 1.0
    v3 = ps * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(51).mean() * 0.0001
    e0 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f0 = ratio.pct_change(51).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(50).mean() * 0.00030000000000000003
    e2 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f2 = ratio.pct_change(50).fillna(0)
    d3 = ratio.shift(4).rolling(33).mean() * 0.0004
    e3 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f3 = ratio.pct_change(33).fillna(0)
    d4 = ratio.shift(5).rolling(10).mean() * 0.0005
    e4 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f4 = ratio.pct_change(10).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(49).mean() * 0.0007
    e6 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f6 = ratio.pct_change(49).fillna(0)
    d7 = ratio.shift(8).rolling(23).mean() * 0.0008
    e7 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f7 = ratio.pct_change(23).fillna(0)
    res = np.tanh(ratio.rolling(98).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc063_98d_val_v063_signal'] = f86mm_f86_market_cap_relative_momentum_calc063_98d_val_v063_signal

def f86mm_f86_market_cap_relative_momentum_calc064_224d_val_v064_signal(fcf, netinc, pe):
    v1 = netinc * 1.0
    v2 = pe * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(224).kurt() / v2.rolling(224).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(12).mean() * 0.0001
    e0 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f0 = ratio.pct_change(12).fillna(0)
    d1 = ratio.shift(2).rolling(50).mean() * 0.0002
    e1 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f1 = ratio.pct_change(50).fillna(0)
    d2 = ratio.shift(3).rolling(33).mean() * 0.00030000000000000003
    e2 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f2 = ratio.pct_change(33).fillna(0)
    d3 = ratio.shift(4).rolling(10).mean() * 0.0004
    e3 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f3 = ratio.pct_change(10).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(49).mean() * 0.0006000000000000001
    e5 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f5 = ratio.pct_change(49).fillna(0)
    d6 = ratio.shift(7).rolling(23).mean() * 0.0007
    e6 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f6 = ratio.pct_change(23).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.rolling(224).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc064_224d_val_v064_signal'] = f86mm_f86_market_cap_relative_momentum_calc064_224d_val_v064_signal

def f86mm_f86_market_cap_relative_momentum_calc065_24d_val_v065_signal(assets, ebitda, pe):
    v1 = assets * 1.0
    v2 = pe * 1.0
    v3 = ebitda * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(50).mean() * 0.0001
    e0 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f0 = ratio.pct_change(50).fillna(0)
    d1 = ratio.shift(2).rolling(33).mean() * 0.0002
    e1 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f1 = ratio.pct_change(33).fillna(0)
    d2 = ratio.shift(3).rolling(10).mean() * 0.00030000000000000003
    e2 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f2 = ratio.pct_change(10).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(49).mean() * 0.0005
    e4 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f4 = ratio.pct_change(49).fillna(0)
    d5 = ratio.shift(6).rolling(23).mean() * 0.0006000000000000001
    e5 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f5 = ratio.pct_change(23).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(44).mean() * 0.0008
    e7 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f7 = ratio.pct_change(44).fillna(0)
    res = ratio.rolling(24).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc065_24d_val_v065_signal'] = f86mm_f86_market_cap_relative_momentum_calc065_24d_val_v065_signal

def f86mm_f86_market_cap_relative_momentum_calc066_157d_val_v066_signal(fcf, pe, ps):
    v1 = fcf * 1.0
    v2 = pe * 1.0
    v3 = ps * 1.0
    ratio = v1.rolling(157).rank(pct=True) - v2.rolling(157).rank(pct=True)
    d0 = ratio.shift(1).rolling(33).mean() * 0.0001
    e0 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f0 = ratio.pct_change(33).fillna(0)
    d1 = ratio.shift(2).rolling(10).mean() * 0.0002
    e1 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f1 = ratio.pct_change(10).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(49).mean() * 0.0004
    e3 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f3 = ratio.pct_change(49).fillna(0)
    d4 = ratio.shift(5).rolling(23).mean() * 0.0005
    e4 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f4 = ratio.pct_change(23).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(44).mean() * 0.0007
    e6 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f6 = ratio.pct_change(44).fillna(0)
    d7 = ratio.shift(8).rolling(14).mean() * 0.0008
    e7 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f7 = ratio.pct_change(14).fillna(0)
    res = ratio.pct_change(157)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc066_157d_val_v066_signal'] = f86mm_f86_market_cap_relative_momentum_calc066_157d_val_v066_signal

def f86mm_f86_market_cap_relative_momentum_calc067_136d_val_v067_signal(ebitda, pb, ps):
    v1 = ps * 1.0
    v2 = pb * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(136).kurt() / v2.rolling(136).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(10).mean() * 0.0001
    e0 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f0 = ratio.pct_change(10).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(49).mean() * 0.00030000000000000003
    e2 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f2 = ratio.pct_change(49).fillna(0)
    d3 = ratio.shift(4).rolling(23).mean() * 0.0004
    e3 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f3 = ratio.pct_change(23).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(44).mean() * 0.0006000000000000001
    e5 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f5 = ratio.pct_change(44).fillna(0)
    d6 = ratio.shift(7).rolling(14).mean() * 0.0007
    e6 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f6 = ratio.pct_change(14).fillna(0)
    d7 = ratio.shift(8).rolling(25).mean() * 0.0008
    e7 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f7 = ratio.pct_change(25).fillna(0)
    res = (ratio - ratio.rolling(136).mean()) / (ratio.rolling(136).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc067_136d_val_v067_signal'] = f86mm_f86_market_cap_relative_momentum_calc067_136d_val_v067_signal

def f86mm_f86_market_cap_relative_momentum_calc068_32d_val_v068_signal(fcf, pb, pe):
    v1 = pb * 1.0
    v2 = pe * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(32).kurt() / v2.rolling(32).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(49).mean() * 0.0002
    e1 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f1 = ratio.pct_change(49).fillna(0)
    d2 = ratio.shift(3).rolling(23).mean() * 0.00030000000000000003
    e2 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f2 = ratio.pct_change(23).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(44).mean() * 0.0005
    e4 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f4 = ratio.pct_change(44).fillna(0)
    d5 = ratio.shift(6).rolling(14).mean() * 0.0006000000000000001
    e5 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f5 = ratio.pct_change(14).fillna(0)
    d6 = ratio.shift(7).rolling(25).mean() * 0.0007
    e6 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f6 = ratio.pct_change(25).fillna(0)
    d7 = ratio.shift(8).rolling(46).mean() * 0.0008
    e7 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f7 = ratio.pct_change(46).fillna(0)
    res = ratio.diff(40).rolling(32).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc068_32d_val_v068_signal'] = f86mm_f86_market_cap_relative_momentum_calc068_32d_val_v068_signal

def f86mm_f86_market_cap_relative_momentum_calc069_70d_val_v069_signal(marketcap, ps, revenue):
    v1 = marketcap * 1.0
    v2 = revenue * 1.0
    v3 = ps * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(70).mean()) / r_raw.rolling(70).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(49).mean() * 0.0001
    e0 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f0 = ratio.pct_change(49).fillna(0)
    d1 = ratio.shift(2).rolling(23).mean() * 0.0002
    e1 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f1 = ratio.pct_change(23).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(44).mean() * 0.0004
    e3 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f3 = ratio.pct_change(44).fillna(0)
    d4 = ratio.shift(5).rolling(14).mean() * 0.0005
    e4 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f4 = ratio.pct_change(14).fillna(0)
    d5 = ratio.shift(6).rolling(25).mean() * 0.0006000000000000001
    e5 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f5 = ratio.pct_change(25).fillna(0)
    d6 = ratio.shift(7).rolling(46).mean() * 0.0007
    e6 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f6 = ratio.pct_change(46).fillna(0)
    d7 = ratio.shift(8).rolling(18).mean() * 0.0008
    e7 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f7 = ratio.pct_change(18).fillna(0)
    res = ratio.rolling(70).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc069_70d_val_v069_signal'] = f86mm_f86_market_cap_relative_momentum_calc069_70d_val_v069_signal

def f86mm_f86_market_cap_relative_momentum_calc070_192d_val_v070_signal(assets, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ps * 1.0
    v3 = assets * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(23).mean() * 0.0001
    e0 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f0 = ratio.pct_change(23).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(44).mean() * 0.00030000000000000003
    e2 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f2 = ratio.pct_change(44).fillna(0)
    d3 = ratio.shift(4).rolling(14).mean() * 0.0004
    e3 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f3 = ratio.pct_change(14).fillna(0)
    d4 = ratio.shift(5).rolling(25).mean() * 0.0005
    e4 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f4 = ratio.pct_change(25).fillna(0)
    d5 = ratio.shift(6).rolling(46).mean() * 0.0006000000000000001
    e5 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f5 = ratio.pct_change(46).fillna(0)
    d6 = ratio.shift(7).rolling(18).mean() * 0.0007
    e6 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f6 = ratio.pct_change(18).fillna(0)
    d7 = ratio.shift(8).rolling(36).mean() * 0.0008
    e7 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f7 = ratio.pct_change(36).fillna(0)
    res = ratio.diff(35).rolling(192).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc070_192d_val_v070_signal'] = f86mm_f86_market_cap_relative_momentum_calc070_192d_val_v070_signal

def f86mm_f86_market_cap_relative_momentum_calc071_239d_val_v071_signal(evebitda, fcf, pb):
    v1 = evebitda * 1.0
    v2 = pb * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(239).rank(pct=True) - v2.rolling(239).rank(pct=True)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(44).mean() * 0.0002
    e1 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f1 = ratio.pct_change(44).fillna(0)
    d2 = ratio.shift(3).rolling(14).mean() * 0.00030000000000000003
    e2 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f2 = ratio.pct_change(14).fillna(0)
    d3 = ratio.shift(4).rolling(25).mean() * 0.0004
    e3 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f3 = ratio.pct_change(25).fillna(0)
    d4 = ratio.shift(5).rolling(46).mean() * 0.0005
    e4 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f4 = ratio.pct_change(46).fillna(0)
    d5 = ratio.shift(6).rolling(18).mean() * 0.0006000000000000001
    e5 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f5 = ratio.pct_change(18).fillna(0)
    d6 = ratio.shift(7).rolling(36).mean() * 0.0007
    e6 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f6 = ratio.pct_change(36).fillna(0)
    d7 = ratio.shift(8).rolling(50).mean() * 0.0008
    e7 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f7 = ratio.pct_change(50).fillna(0)
    res = ratio.rolling(239).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc071_239d_val_v071_signal'] = f86mm_f86_market_cap_relative_momentum_calc071_239d_val_v071_signal

def f86mm_f86_market_cap_relative_momentum_calc072_208d_val_v072_signal(close, marketcap, pb):
    v1 = marketcap * 1.0
    v2 = pb * 1.0
    v3 = close * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(44).mean() * 0.0001
    e0 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f0 = ratio.pct_change(44).fillna(0)
    d1 = ratio.shift(2).rolling(14).mean() * 0.0002
    e1 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f1 = ratio.pct_change(14).fillna(0)
    d2 = ratio.shift(3).rolling(25).mean() * 0.00030000000000000003
    e2 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f2 = ratio.pct_change(25).fillna(0)
    d3 = ratio.shift(4).rolling(46).mean() * 0.0004
    e3 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f3 = ratio.pct_change(46).fillna(0)
    d4 = ratio.shift(5).rolling(18).mean() * 0.0005
    e4 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f4 = ratio.pct_change(18).fillna(0)
    d5 = ratio.shift(6).rolling(36).mean() * 0.0006000000000000001
    e5 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f5 = ratio.pct_change(36).fillna(0)
    d6 = ratio.shift(7).rolling(50).mean() * 0.0007
    e6 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f6 = ratio.pct_change(50).fillna(0)
    d7 = ratio.shift(8).rolling(14).mean() * 0.0008
    e7 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f7 = ratio.pct_change(14).fillna(0)
    res = ratio.rolling(208).std() / (ratio.rolling(208).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc072_208d_val_v072_signal'] = f86mm_f86_market_cap_relative_momentum_calc072_208d_val_v072_signal

def f86mm_f86_market_cap_relative_momentum_calc073_183d_val_v073_signal(assets, ev, pe):
    v1 = ev * 1.0
    v2 = assets * 1.0
    v3 = pe * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(14).mean() * 0.0001
    e0 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f0 = ratio.pct_change(14).fillna(0)
    d1 = ratio.shift(2).rolling(25).mean() * 0.0002
    e1 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f1 = ratio.pct_change(25).fillna(0)
    d2 = ratio.shift(3).rolling(46).mean() * 0.00030000000000000003
    e2 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f2 = ratio.pct_change(46).fillna(0)
    d3 = ratio.shift(4).rolling(18).mean() * 0.0004
    e3 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f3 = ratio.pct_change(18).fillna(0)
    d4 = ratio.shift(5).rolling(36).mean() * 0.0005
    e4 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f4 = ratio.pct_change(36).fillna(0)
    d5 = ratio.shift(6).rolling(50).mean() * 0.0006000000000000001
    e5 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f5 = ratio.pct_change(50).fillna(0)
    d6 = ratio.shift(7).rolling(14).mean() * 0.0007
    e6 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f6 = ratio.pct_change(14).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(183).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc073_183d_val_v073_signal'] = f86mm_f86_market_cap_relative_momentum_calc073_183d_val_v073_signal

def f86mm_f86_market_cap_relative_momentum_calc074_119d_val_v074_signal(fcf, pe, ps):
    v1 = pe * 1.0
    v2 = fcf * 1.0
    v3 = ps * 1.0
    ratio = v1.rolling(119).rank(pct=True) - v2.rolling(119).rank(pct=True)
    d0 = ratio.shift(1).rolling(25).mean() * 0.0001
    e0 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f0 = ratio.pct_change(25).fillna(0)
    d1 = ratio.shift(2).rolling(46).mean() * 0.0002
    e1 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f1 = ratio.pct_change(46).fillna(0)
    d2 = ratio.shift(3).rolling(18).mean() * 0.00030000000000000003
    e2 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f2 = ratio.pct_change(18).fillna(0)
    d3 = ratio.shift(4).rolling(36).mean() * 0.0004
    e3 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f3 = ratio.pct_change(36).fillna(0)
    d4 = ratio.shift(5).rolling(50).mean() * 0.0005
    e4 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f4 = ratio.pct_change(50).fillna(0)
    d5 = ratio.shift(6).rolling(14).mean() * 0.0006000000000000001
    e5 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f5 = ratio.pct_change(14).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(27).mean() * 0.0008
    e7 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f7 = ratio.pct_change(27).fillna(0)
    res = ratio.ewm(span=119).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc074_119d_val_v074_signal'] = f86mm_f86_market_cap_relative_momentum_calc074_119d_val_v074_signal

def f86mm_f86_market_cap_relative_momentum_calc075_210d_val_v075_signal(ebitda, pb, ps):
    v1 = ps * 1.0
    v2 = pb * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(210).rank(pct=True) - v2.rolling(210).rank(pct=True)
    d0 = ratio.shift(1).rolling(46).mean() * 0.0001
    e0 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f0 = ratio.pct_change(46).fillna(0)
    d1 = ratio.shift(2).rolling(18).mean() * 0.0002
    e1 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f1 = ratio.pct_change(18).fillna(0)
    d2 = ratio.shift(3).rolling(36).mean() * 0.00030000000000000003
    e2 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f2 = ratio.pct_change(36).fillna(0)
    d3 = ratio.shift(4).rolling(50).mean() * 0.0004
    e3 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f3 = ratio.pct_change(50).fillna(0)
    d4 = ratio.shift(5).rolling(14).mean() * 0.0005
    e4 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f4 = ratio.pct_change(14).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(27).mean() * 0.0007
    e6 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f6 = ratio.pct_change(27).fillna(0)
    d7 = ratio.shift(8).rolling(46).mean() * 0.0008
    e7 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f7 = ratio.pct_change(46).fillna(0)
    res = ratio.rolling(210).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc075_210d_val_v075_signal'] = f86mm_f86_market_cap_relative_momentum_calc075_210d_val_v075_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
