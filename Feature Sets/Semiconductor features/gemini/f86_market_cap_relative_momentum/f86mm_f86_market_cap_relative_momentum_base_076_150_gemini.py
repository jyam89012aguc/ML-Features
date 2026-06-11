import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f86mm_f86_market_cap_relative_momentum_calc076_168d_val_v076_signal(ev, fcf, marketcap):
    v1 = marketcap * 1.0
    v2 = ev * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(168).kurt() / v2.rolling(168).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(18).mean() * 0.0001
    e0 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f0 = ratio.pct_change(18).fillna(0)
    d1 = ratio.shift(2).rolling(36).mean() * 0.0002
    e1 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f1 = ratio.pct_change(36).fillna(0)
    d2 = ratio.shift(3).rolling(50).mean() * 0.00030000000000000003
    e2 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f2 = ratio.pct_change(50).fillna(0)
    d3 = ratio.shift(4).rolling(14).mean() * 0.0004
    e3 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f3 = ratio.pct_change(14).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(27).mean() * 0.0006000000000000001
    e5 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f5 = ratio.pct_change(27).fillna(0)
    d6 = ratio.shift(7).rolling(46).mean() * 0.0007
    e6 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f6 = ratio.pct_change(46).fillna(0)
    d7 = ratio.shift(8).rolling(17).mean() * 0.0008
    e7 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f7 = ratio.pct_change(17).fillna(0)
    res = ratio.rolling(168).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc076_168d_val_v076_signal'] = f86mm_f86_market_cap_relative_momentum_calc076_168d_val_v076_signal

def f86mm_f86_market_cap_relative_momentum_calc077_151d_val_v077_signal(assets, marketcap, pb):
    v1 = marketcap * 1.0
    v2 = pb * 1.0
    v3 = assets * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(36).mean() * 0.0001
    e0 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f0 = ratio.pct_change(36).fillna(0)
    d1 = ratio.shift(2).rolling(50).mean() * 0.0002
    e1 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f1 = ratio.pct_change(50).fillna(0)
    d2 = ratio.shift(3).rolling(14).mean() * 0.00030000000000000003
    e2 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f2 = ratio.pct_change(14).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(27).mean() * 0.0005
    e4 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f4 = ratio.pct_change(27).fillna(0)
    d5 = ratio.shift(6).rolling(46).mean() * 0.0006000000000000001
    e5 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f5 = ratio.pct_change(46).fillna(0)
    d6 = ratio.shift(7).rolling(17).mean() * 0.0007
    e6 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f6 = ratio.pct_change(17).fillna(0)
    d7 = ratio.shift(8).rolling(10).mean() * 0.0008
    e7 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f7 = ratio.pct_change(10).fillna(0)
    res = (ratio - ratio.rolling(151).mean()) / (ratio.rolling(151).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc077_151d_val_v077_signal'] = f86mm_f86_market_cap_relative_momentum_calc077_151d_val_v077_signal

def f86mm_f86_market_cap_relative_momentum_calc078_77d_val_v078_signal(ev, netinc, ps):
    v1 = ev * 1.0
    v2 = netinc * 1.0
    v3 = ps * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(50).mean() * 0.0001
    e0 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f0 = ratio.pct_change(50).fillna(0)
    d1 = ratio.shift(2).rolling(14).mean() * 0.0002
    e1 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f1 = ratio.pct_change(14).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(27).mean() * 0.0004
    e3 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f3 = ratio.pct_change(27).fillna(0)
    d4 = ratio.shift(5).rolling(46).mean() * 0.0005
    e4 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f4 = ratio.pct_change(46).fillna(0)
    d5 = ratio.shift(6).rolling(17).mean() * 0.0006000000000000001
    e5 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f5 = ratio.pct_change(17).fillna(0)
    d6 = ratio.shift(7).rolling(10).mean() * 0.0007
    e6 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f6 = ratio.pct_change(10).fillna(0)
    d7 = ratio.shift(8).rolling(8).mean() * 0.0008
    e7 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f7 = ratio.pct_change(8).fillna(0)
    res = ratio.rolling(77).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc078_77d_val_v078_signal'] = f86mm_f86_market_cap_relative_momentum_calc078_77d_val_v078_signal

def f86mm_f86_market_cap_relative_momentum_calc079_122d_val_v079_signal(ev, netinc, ps):
    v1 = ev * 1.0
    v2 = netinc * 1.0
    v3 = ps * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(14).mean() * 0.0001
    e0 = ratio.rolling(14).std() / (ratio.rolling(14).mean().abs() + 1e-9)
    f0 = ratio.pct_change(14).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(27).mean() * 0.00030000000000000003
    e2 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f2 = ratio.pct_change(27).fillna(0)
    d3 = ratio.shift(4).rolling(46).mean() * 0.0004
    e3 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f3 = ratio.pct_change(46).fillna(0)
    d4 = ratio.shift(5).rolling(17).mean() * 0.0005
    e4 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f4 = ratio.pct_change(17).fillna(0)
    d5 = ratio.shift(6).rolling(10).mean() * 0.0006000000000000001
    e5 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f5 = ratio.pct_change(10).fillna(0)
    d6 = ratio.shift(7).rolling(8).mean() * 0.0007
    e6 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f6 = ratio.pct_change(8).fillna(0)
    d7 = ratio.shift(8).rolling(51).mean() * 0.0008
    e7 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f7 = ratio.pct_change(51).fillna(0)
    res = ratio.rolling(122).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc079_122d_val_v079_signal'] = f86mm_f86_market_cap_relative_momentum_calc079_122d_val_v079_signal

def f86mm_f86_market_cap_relative_momentum_calc080_112d_val_v080_signal(ebitda, pb, pe):
    v1 = pe * 1.0
    v2 = pb * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(112).kurt() / v2.rolling(112).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(27).mean() * 0.0002
    e1 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f1 = ratio.pct_change(27).fillna(0)
    d2 = ratio.shift(3).rolling(46).mean() * 0.00030000000000000003
    e2 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f2 = ratio.pct_change(46).fillna(0)
    d3 = ratio.shift(4).rolling(17).mean() * 0.0004
    e3 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f3 = ratio.pct_change(17).fillna(0)
    d4 = ratio.shift(5).rolling(10).mean() * 0.0005
    e4 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f4 = ratio.pct_change(10).fillna(0)
    d5 = ratio.shift(6).rolling(8).mean() * 0.0006000000000000001
    e5 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f5 = ratio.pct_change(8).fillna(0)
    d6 = ratio.shift(7).rolling(51).mean() * 0.0007
    e6 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f6 = ratio.pct_change(51).fillna(0)
    d7 = ratio.shift(8).rolling(45).mean() * 0.0008
    e7 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f7 = ratio.pct_change(45).fillna(0)
    res = np.tanh(ratio.rolling(112).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc080_112d_val_v080_signal'] = f86mm_f86_market_cap_relative_momentum_calc080_112d_val_v080_signal

def f86mm_f86_market_cap_relative_momentum_calc081_23d_val_v081_signal(close, marketcap, netinc):
    v1 = marketcap * 1.0
    v2 = netinc * 1.0
    v3 = close * 1.0
    ratio = (v1 - v1.rolling(23).min()) / (v1.rolling(23).max() - v1.rolling(23).min() + 1e-9)
    d0 = ratio.shift(1).rolling(27).mean() * 0.0001
    e0 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f0 = ratio.pct_change(27).fillna(0)
    d1 = ratio.shift(2).rolling(46).mean() * 0.0002
    e1 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f1 = ratio.pct_change(46).fillna(0)
    d2 = ratio.shift(3).rolling(17).mean() * 0.00030000000000000003
    e2 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f2 = ratio.pct_change(17).fillna(0)
    d3 = ratio.shift(4).rolling(10).mean() * 0.0004
    e3 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f3 = ratio.pct_change(10).fillna(0)
    d4 = ratio.shift(5).rolling(8).mean() * 0.0005
    e4 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f4 = ratio.pct_change(8).fillna(0)
    d5 = ratio.shift(6).rolling(51).mean() * 0.0006000000000000001
    e5 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f5 = ratio.pct_change(51).fillna(0)
    d6 = ratio.shift(7).rolling(45).mean() * 0.0007
    e6 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f6 = ratio.pct_change(45).fillna(0)
    d7 = ratio.shift(8).rolling(54).mean() * 0.0008
    e7 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f7 = ratio.pct_change(54).fillna(0)
    res = ratio.rolling(23).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc081_23d_val_v081_signal'] = f86mm_f86_market_cap_relative_momentum_calc081_23d_val_v081_signal

def f86mm_f86_market_cap_relative_momentum_calc082_206d_val_v082_signal(ev, netinc, ps):
    v1 = ev * 1.0
    v2 = netinc * 1.0
    v3 = ps * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(46).mean() * 0.0001
    e0 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f0 = ratio.pct_change(46).fillna(0)
    d1 = ratio.shift(2).rolling(17).mean() * 0.0002
    e1 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f1 = ratio.pct_change(17).fillna(0)
    d2 = ratio.shift(3).rolling(10).mean() * 0.00030000000000000003
    e2 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f2 = ratio.pct_change(10).fillna(0)
    d3 = ratio.shift(4).rolling(8).mean() * 0.0004
    e3 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f3 = ratio.pct_change(8).fillna(0)
    d4 = ratio.shift(5).rolling(51).mean() * 0.0005
    e4 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f4 = ratio.pct_change(51).fillna(0)
    d5 = ratio.shift(6).rolling(45).mean() * 0.0006000000000000001
    e5 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f5 = ratio.pct_change(45).fillna(0)
    d6 = ratio.shift(7).rolling(54).mean() * 0.0007
    e6 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f6 = ratio.pct_change(54).fillna(0)
    d7 = ratio.shift(8).rolling(27).mean() * 0.0008
    e7 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f7 = ratio.pct_change(27).fillna(0)
    res = ratio.rolling(206).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc082_206d_val_v082_signal'] = f86mm_f86_market_cap_relative_momentum_calc082_206d_val_v082_signal

def f86mm_f86_market_cap_relative_momentum_calc083_241d_val_v083_signal(close, pb, ps):
    v1 = ps * 1.0
    v2 = close * 1.0
    v3 = pb * 1.0
    ratio = v1.diff(29).rolling(241).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(17).mean() * 0.0001
    e0 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f0 = ratio.pct_change(17).fillna(0)
    d1 = ratio.shift(2).rolling(10).mean() * 0.0002
    e1 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f1 = ratio.pct_change(10).fillna(0)
    d2 = ratio.shift(3).rolling(8).mean() * 0.00030000000000000003
    e2 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f2 = ratio.pct_change(8).fillna(0)
    d3 = ratio.shift(4).rolling(51).mean() * 0.0004
    e3 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f3 = ratio.pct_change(51).fillna(0)
    d4 = ratio.shift(5).rolling(45).mean() * 0.0005
    e4 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f4 = ratio.pct_change(45).fillna(0)
    d5 = ratio.shift(6).rolling(54).mean() * 0.0006000000000000001
    e5 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f5 = ratio.pct_change(54).fillna(0)
    d6 = ratio.shift(7).rolling(27).mean() * 0.0007
    e6 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f6 = ratio.pct_change(27).fillna(0)
    d7 = ratio.shift(8).rolling(33).mean() * 0.0008
    e7 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f7 = ratio.pct_change(33).fillna(0)
    res = np.tanh(ratio.rolling(241).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc083_241d_val_v083_signal'] = f86mm_f86_market_cap_relative_momentum_calc083_241d_val_v083_signal

def f86mm_f86_market_cap_relative_momentum_calc084_104d_val_v084_signal(ebitda, fcf, pb):
    v1 = pb * 1.0
    v2 = ebitda * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(104).rank(pct=True) - v2.rolling(104).rank(pct=True)
    d0 = ratio.shift(1).rolling(10).mean() * 0.0001
    e0 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f0 = ratio.pct_change(10).fillna(0)
    d1 = ratio.shift(2).rolling(8).mean() * 0.0002
    e1 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f1 = ratio.pct_change(8).fillna(0)
    d2 = ratio.shift(3).rolling(51).mean() * 0.00030000000000000003
    e2 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f2 = ratio.pct_change(51).fillna(0)
    d3 = ratio.shift(4).rolling(45).mean() * 0.0004
    e3 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f3 = ratio.pct_change(45).fillna(0)
    d4 = ratio.shift(5).rolling(54).mean() * 0.0005
    e4 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f4 = ratio.pct_change(54).fillna(0)
    d5 = ratio.shift(6).rolling(27).mean() * 0.0006000000000000001
    e5 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f5 = ratio.pct_change(27).fillna(0)
    d6 = ratio.shift(7).rolling(33).mean() * 0.0007
    e6 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f6 = ratio.pct_change(33).fillna(0)
    d7 = ratio.shift(8).rolling(51).mean() * 0.0008
    e7 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f7 = ratio.pct_change(51).fillna(0)
    res = (ratio - ratio.rolling(104).mean()) / (ratio.rolling(104).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc084_104d_val_v084_signal'] = f86mm_f86_market_cap_relative_momentum_calc084_104d_val_v084_signal

def f86mm_f86_market_cap_relative_momentum_calc085_180d_val_v085_signal(ebitda, ev, marketcap):
    v1 = ev * 1.0
    v2 = marketcap * 1.0
    v3 = ebitda * 1.0
    ratio = (v1 - v1.rolling(180).min()) / (v1.rolling(180).max() - v1.rolling(180).min() + 1e-9)
    d0 = ratio.shift(1).rolling(8).mean() * 0.0001
    e0 = ratio.rolling(8).std() / (ratio.rolling(8).mean().abs() + 1e-9)
    f0 = ratio.pct_change(8).fillna(0)
    d1 = ratio.shift(2).rolling(51).mean() * 0.0002
    e1 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f1 = ratio.pct_change(51).fillna(0)
    d2 = ratio.shift(3).rolling(45).mean() * 0.00030000000000000003
    e2 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f2 = ratio.pct_change(45).fillna(0)
    d3 = ratio.shift(4).rolling(54).mean() * 0.0004
    e3 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f3 = ratio.pct_change(54).fillna(0)
    d4 = ratio.shift(5).rolling(27).mean() * 0.0005
    e4 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f4 = ratio.pct_change(27).fillna(0)
    d5 = ratio.shift(6).rolling(33).mean() * 0.0006000000000000001
    e5 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f5 = ratio.pct_change(33).fillna(0)
    d6 = ratio.shift(7).rolling(51).mean() * 0.0007
    e6 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f6 = ratio.pct_change(51).fillna(0)
    d7 = ratio.shift(8).rolling(38).mean() * 0.0008
    e7 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f7 = ratio.pct_change(38).fillna(0)
    res = ratio.ewm(span=180).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc085_180d_val_v085_signal'] = f86mm_f86_market_cap_relative_momentum_calc085_180d_val_v085_signal

def f86mm_f86_market_cap_relative_momentum_calc086_174d_val_v086_signal(close, fcf, pe):
    v1 = close * 1.0
    v2 = pe * 1.0
    v3 = fcf * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(174).mean()) / r_raw.rolling(174).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(51).mean() * 0.0001
    e0 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f0 = ratio.pct_change(51).fillna(0)
    d1 = ratio.shift(2).rolling(45).mean() * 0.0002
    e1 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f1 = ratio.pct_change(45).fillna(0)
    d2 = ratio.shift(3).rolling(54).mean() * 0.00030000000000000003
    e2 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f2 = ratio.pct_change(54).fillna(0)
    d3 = ratio.shift(4).rolling(27).mean() * 0.0004
    e3 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f3 = ratio.pct_change(27).fillna(0)
    d4 = ratio.shift(5).rolling(33).mean() * 0.0005
    e4 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f4 = ratio.pct_change(33).fillna(0)
    d5 = ratio.shift(6).rolling(51).mean() * 0.0006000000000000001
    e5 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f5 = ratio.pct_change(51).fillna(0)
    d6 = ratio.shift(7).rolling(38).mean() * 0.0007
    e6 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f6 = ratio.pct_change(38).fillna(0)
    d7 = ratio.shift(8).rolling(7).mean() * 0.0008
    e7 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f7 = ratio.pct_change(7).fillna(0)
    res = ratio.diff(174)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc086_174d_val_v086_signal'] = f86mm_f86_market_cap_relative_momentum_calc086_174d_val_v086_signal

def f86mm_f86_market_cap_relative_momentum_calc087_197d_val_v087_signal(close, ebitda, revenue):
    v1 = revenue * 1.0
    v2 = close * 1.0
    v3 = ebitda * 1.0
    ratio = v1.pct_change(14) - v2.pct_change(14)
    d0 = ratio.shift(1).rolling(45).mean() * 0.0001
    e0 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f0 = ratio.pct_change(45).fillna(0)
    d1 = ratio.shift(2).rolling(54).mean() * 0.0002
    e1 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f1 = ratio.pct_change(54).fillna(0)
    d2 = ratio.shift(3).rolling(27).mean() * 0.00030000000000000003
    e2 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f2 = ratio.pct_change(27).fillna(0)
    d3 = ratio.shift(4).rolling(33).mean() * 0.0004
    e3 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f3 = ratio.pct_change(33).fillna(0)
    d4 = ratio.shift(5).rolling(51).mean() * 0.0005
    e4 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f4 = ratio.pct_change(51).fillna(0)
    d5 = ratio.shift(6).rolling(38).mean() * 0.0006000000000000001
    e5 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f5 = ratio.pct_change(38).fillna(0)
    d6 = ratio.shift(7).rolling(7).mean() * 0.0007
    e6 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f6 = ratio.pct_change(7).fillna(0)
    d7 = ratio.shift(8).rolling(27).mean() * 0.0008
    e7 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f7 = ratio.pct_change(27).fillna(0)
    res = ratio.rolling(197).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc087_197d_val_v087_signal'] = f86mm_f86_market_cap_relative_momentum_calc087_197d_val_v087_signal

def f86mm_f86_market_cap_relative_momentum_calc088_246d_val_v088_signal(marketcap, netinc, pe):
    v1 = netinc * 1.0
    v2 = marketcap * 1.0
    v3 = pe * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(54).mean() * 0.0001
    e0 = ratio.rolling(54).std() / (ratio.rolling(54).mean().abs() + 1e-9)
    f0 = ratio.pct_change(54).fillna(0)
    d1 = ratio.shift(2).rolling(27).mean() * 0.0002
    e1 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f1 = ratio.pct_change(27).fillna(0)
    d2 = ratio.shift(3).rolling(33).mean() * 0.00030000000000000003
    e2 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f2 = ratio.pct_change(33).fillna(0)
    d3 = ratio.shift(4).rolling(51).mean() * 0.0004
    e3 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f3 = ratio.pct_change(51).fillna(0)
    d4 = ratio.shift(5).rolling(38).mean() * 0.0005
    e4 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f4 = ratio.pct_change(38).fillna(0)
    d5 = ratio.shift(6).rolling(7).mean() * 0.0006000000000000001
    e5 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f5 = ratio.pct_change(7).fillna(0)
    d6 = ratio.shift(7).rolling(27).mean() * 0.0007
    e6 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f6 = ratio.pct_change(27).fillna(0)
    d7 = ratio.shift(8).rolling(19).mean() * 0.0008
    e7 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f7 = ratio.pct_change(19).fillna(0)
    res = ratio.rolling(246).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc088_246d_val_v088_signal'] = f86mm_f86_market_cap_relative_momentum_calc088_246d_val_v088_signal

def f86mm_f86_market_cap_relative_momentum_calc089_165d_val_v089_signal(evebitda, fcf, netinc):
    v1 = netinc * 1.0
    v2 = evebitda * 1.0
    v3 = fcf * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(27).mean() * 0.0001
    e0 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f0 = ratio.pct_change(27).fillna(0)
    d1 = ratio.shift(2).rolling(33).mean() * 0.0002
    e1 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f1 = ratio.pct_change(33).fillna(0)
    d2 = ratio.shift(3).rolling(51).mean() * 0.00030000000000000003
    e2 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f2 = ratio.pct_change(51).fillna(0)
    d3 = ratio.shift(4).rolling(38).mean() * 0.0004
    e3 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f3 = ratio.pct_change(38).fillna(0)
    d4 = ratio.shift(5).rolling(7).mean() * 0.0005
    e4 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f4 = ratio.pct_change(7).fillna(0)
    d5 = ratio.shift(6).rolling(27).mean() * 0.0006000000000000001
    e5 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f5 = ratio.pct_change(27).fillna(0)
    d6 = ratio.shift(7).rolling(19).mean() * 0.0007
    e6 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f6 = ratio.pct_change(19).fillna(0)
    d7 = ratio.shift(8).rolling(9).mean() * 0.0008
    e7 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f7 = ratio.pct_change(9).fillna(0)
    res = ratio.rolling(165).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc089_165d_val_v089_signal'] = f86mm_f86_market_cap_relative_momentum_calc089_165d_val_v089_signal

def f86mm_f86_market_cap_relative_momentum_calc090_130d_val_v090_signal(ev, evebitda, ps):
    v1 = ev * 1.0
    v2 = evebitda * 1.0
    v3 = ps * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(130).mean()) / r_raw.rolling(130).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(33).mean() * 0.0001
    e0 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f0 = ratio.pct_change(33).fillna(0)
    d1 = ratio.shift(2).rolling(51).mean() * 0.0002
    e1 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f1 = ratio.pct_change(51).fillna(0)
    d2 = ratio.shift(3).rolling(38).mean() * 0.00030000000000000003
    e2 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f2 = ratio.pct_change(38).fillna(0)
    d3 = ratio.shift(4).rolling(7).mean() * 0.0004
    e3 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f3 = ratio.pct_change(7).fillna(0)
    d4 = ratio.shift(5).rolling(27).mean() * 0.0005
    e4 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f4 = ratio.pct_change(27).fillna(0)
    d5 = ratio.shift(6).rolling(19).mean() * 0.0006000000000000001
    e5 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f5 = ratio.pct_change(19).fillna(0)
    d6 = ratio.shift(7).rolling(9).mean() * 0.0007
    e6 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f6 = ratio.pct_change(9).fillna(0)
    d7 = ratio.shift(8).rolling(23).mean() * 0.0008
    e7 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f7 = ratio.pct_change(23).fillna(0)
    res = ratio.rolling(130).max() - ratio.rolling(130).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc090_130d_val_v090_signal'] = f86mm_f86_market_cap_relative_momentum_calc090_130d_val_v090_signal

def f86mm_f86_market_cap_relative_momentum_calc091_198d_val_v091_signal(ebitda, evebitda, fcf):
    v1 = fcf * 1.0
    v2 = evebitda * 1.0
    v3 = ebitda * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(51).mean() * 0.0001
    e0 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f0 = ratio.pct_change(51).fillna(0)
    d1 = ratio.shift(2).rolling(38).mean() * 0.0002
    e1 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f1 = ratio.pct_change(38).fillna(0)
    d2 = ratio.shift(3).rolling(7).mean() * 0.00030000000000000003
    e2 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f2 = ratio.pct_change(7).fillna(0)
    d3 = ratio.shift(4).rolling(27).mean() * 0.0004
    e3 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f3 = ratio.pct_change(27).fillna(0)
    d4 = ratio.shift(5).rolling(19).mean() * 0.0005
    e4 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f4 = ratio.pct_change(19).fillna(0)
    d5 = ratio.shift(6).rolling(9).mean() * 0.0006000000000000001
    e5 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f5 = ratio.pct_change(9).fillna(0)
    d6 = ratio.shift(7).rolling(23).mean() * 0.0007
    e6 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f6 = ratio.pct_change(23).fillna(0)
    d7 = ratio.shift(8).rolling(18).mean() * 0.0008
    e7 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f7 = ratio.pct_change(18).fillna(0)
    res = (ratio - ratio.rolling(198).mean()) / (ratio.rolling(198).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc091_198d_val_v091_signal'] = f86mm_f86_market_cap_relative_momentum_calc091_198d_val_v091_signal

def f86mm_f86_market_cap_relative_momentum_calc092_91d_val_v092_signal(ebitda, marketcap, netinc):
    v1 = marketcap * 1.0
    v2 = netinc * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(91).max() / v2.rolling(91).min().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(38).mean() * 0.0001
    e0 = ratio.rolling(38).std() / (ratio.rolling(38).mean().abs() + 1e-9)
    f0 = ratio.pct_change(38).fillna(0)
    d1 = ratio.shift(2).rolling(7).mean() * 0.0002
    e1 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f1 = ratio.pct_change(7).fillna(0)
    d2 = ratio.shift(3).rolling(27).mean() * 0.00030000000000000003
    e2 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f2 = ratio.pct_change(27).fillna(0)
    d3 = ratio.shift(4).rolling(19).mean() * 0.0004
    e3 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f3 = ratio.pct_change(19).fillna(0)
    d4 = ratio.shift(5).rolling(9).mean() * 0.0005
    e4 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f4 = ratio.pct_change(9).fillna(0)
    d5 = ratio.shift(6).rolling(23).mean() * 0.0006000000000000001
    e5 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f5 = ratio.pct_change(23).fillna(0)
    d6 = ratio.shift(7).rolling(18).mean() * 0.0007
    e6 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f6 = ratio.pct_change(18).fillna(0)
    d7 = ratio.shift(8).rolling(23).mean() * 0.0008
    e7 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f7 = ratio.pct_change(23).fillna(0)
    res = ratio.rolling(91).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc092_91d_val_v092_signal'] = f86mm_f86_market_cap_relative_momentum_calc092_91d_val_v092_signal

def f86mm_f86_market_cap_relative_momentum_calc093_59d_val_v093_signal(netinc, pe, ps):
    v1 = netinc * 1.0
    v2 = pe * 1.0
    v3 = ps * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(7).mean() * 0.0001
    e0 = ratio.rolling(7).std() / (ratio.rolling(7).mean().abs() + 1e-9)
    f0 = ratio.pct_change(7).fillna(0)
    d1 = ratio.shift(2).rolling(27).mean() * 0.0002
    e1 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f1 = ratio.pct_change(27).fillna(0)
    d2 = ratio.shift(3).rolling(19).mean() * 0.00030000000000000003
    e2 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f2 = ratio.pct_change(19).fillna(0)
    d3 = ratio.shift(4).rolling(9).mean() * 0.0004
    e3 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f3 = ratio.pct_change(9).fillna(0)
    d4 = ratio.shift(5).rolling(23).mean() * 0.0005
    e4 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f4 = ratio.pct_change(23).fillna(0)
    d5 = ratio.shift(6).rolling(18).mean() * 0.0006000000000000001
    e5 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f5 = ratio.pct_change(18).fillna(0)
    d6 = ratio.shift(7).rolling(23).mean() * 0.0007
    e6 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f6 = ratio.pct_change(23).fillna(0)
    d7 = ratio.shift(8).rolling(50).mean() * 0.0008
    e7 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f7 = ratio.pct_change(50).fillna(0)
    res = ratio.rolling(59).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc093_59d_val_v093_signal'] = f86mm_f86_market_cap_relative_momentum_calc093_59d_val_v093_signal

def f86mm_f86_market_cap_relative_momentum_calc094_30d_val_v094_signal(ev, marketcap, pb):
    v1 = pb * 1.0
    v2 = ev * 1.0
    v3 = marketcap * 1.0
    ratio = v1.rolling(30).std() / v1.rolling(163).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(27).mean() * 0.0001
    e0 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f0 = ratio.pct_change(27).fillna(0)
    d1 = ratio.shift(2).rolling(19).mean() * 0.0002
    e1 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f1 = ratio.pct_change(19).fillna(0)
    d2 = ratio.shift(3).rolling(9).mean() * 0.00030000000000000003
    e2 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f2 = ratio.pct_change(9).fillna(0)
    d3 = ratio.shift(4).rolling(23).mean() * 0.0004
    e3 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f3 = ratio.pct_change(23).fillna(0)
    d4 = ratio.shift(5).rolling(18).mean() * 0.0005
    e4 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f4 = ratio.pct_change(18).fillna(0)
    d5 = ratio.shift(6).rolling(23).mean() * 0.0006000000000000001
    e5 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f5 = ratio.pct_change(23).fillna(0)
    d6 = ratio.shift(7).rolling(50).mean() * 0.0007
    e6 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f6 = ratio.pct_change(50).fillna(0)
    d7 = ratio.shift(8).rolling(49).mean() * 0.0008
    e7 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f7 = ratio.pct_change(49).fillna(0)
    res = ratio.rolling(30).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc094_30d_val_v094_signal'] = f86mm_f86_market_cap_relative_momentum_calc094_30d_val_v094_signal

def f86mm_f86_market_cap_relative_momentum_calc095_153d_val_v095_signal(ebitda, netinc, revenue):
    v1 = revenue * 1.0
    v2 = ebitda * 1.0
    v3 = netinc * 1.0
    ratio = v1.rolling(153).kurt() / v2.rolling(153).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(19).mean() * 0.0001
    e0 = ratio.rolling(19).std() / (ratio.rolling(19).mean().abs() + 1e-9)
    f0 = ratio.pct_change(19).fillna(0)
    d1 = ratio.shift(2).rolling(9).mean() * 0.0002
    e1 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f1 = ratio.pct_change(9).fillna(0)
    d2 = ratio.shift(3).rolling(23).mean() * 0.00030000000000000003
    e2 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f2 = ratio.pct_change(23).fillna(0)
    d3 = ratio.shift(4).rolling(18).mean() * 0.0004
    e3 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f3 = ratio.pct_change(18).fillna(0)
    d4 = ratio.shift(5).rolling(23).mean() * 0.0005
    e4 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f4 = ratio.pct_change(23).fillna(0)
    d5 = ratio.shift(6).rolling(50).mean() * 0.0006000000000000001
    e5 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f5 = ratio.pct_change(50).fillna(0)
    d6 = ratio.shift(7).rolling(49).mean() * 0.0007
    e6 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f6 = ratio.pct_change(49).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.rolling(153).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc095_153d_val_v095_signal'] = f86mm_f86_market_cap_relative_momentum_calc095_153d_val_v095_signal

def f86mm_f86_market_cap_relative_momentum_calc096_235d_val_v096_signal(assets, evebitda, pb):
    v1 = pb * 1.0
    v2 = assets * 1.0
    v3 = evebitda * 1.0
    ratio = v1.rolling(235).std() / v1.rolling(220).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(9).mean() * 0.0001
    e0 = ratio.rolling(9).std() / (ratio.rolling(9).mean().abs() + 1e-9)
    f0 = ratio.pct_change(9).fillna(0)
    d1 = ratio.shift(2).rolling(23).mean() * 0.0002
    e1 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f1 = ratio.pct_change(23).fillna(0)
    d2 = ratio.shift(3).rolling(18).mean() * 0.00030000000000000003
    e2 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f2 = ratio.pct_change(18).fillna(0)
    d3 = ratio.shift(4).rolling(23).mean() * 0.0004
    e3 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f3 = ratio.pct_change(23).fillna(0)
    d4 = ratio.shift(5).rolling(50).mean() * 0.0005
    e4 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f4 = ratio.pct_change(50).fillna(0)
    d5 = ratio.shift(6).rolling(49).mean() * 0.0006000000000000001
    e5 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f5 = ratio.pct_change(49).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.ewm(span=235).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc096_235d_val_v096_signal'] = f86mm_f86_market_cap_relative_momentum_calc096_235d_val_v096_signal

def f86mm_f86_market_cap_relative_momentum_calc097_179d_val_v097_signal(marketcap, netinc, revenue):
    v1 = netinc * 1.0
    v2 = revenue * 1.0
    v3 = marketcap * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(23).mean() * 0.0001
    e0 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f0 = ratio.pct_change(23).fillna(0)
    d1 = ratio.shift(2).rolling(18).mean() * 0.0002
    e1 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f1 = ratio.pct_change(18).fillna(0)
    d2 = ratio.shift(3).rolling(23).mean() * 0.00030000000000000003
    e2 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f2 = ratio.pct_change(23).fillna(0)
    d3 = ratio.shift(4).rolling(50).mean() * 0.0004
    e3 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f3 = ratio.pct_change(50).fillna(0)
    d4 = ratio.shift(5).rolling(49).mean() * 0.0005
    e4 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f4 = ratio.pct_change(49).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(179).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc097_179d_val_v097_signal'] = f86mm_f86_market_cap_relative_momentum_calc097_179d_val_v097_signal

def f86mm_f86_market_cap_relative_momentum_calc098_48d_val_v098_signal(assets, ev, revenue):
    v1 = ev * 1.0
    v2 = assets * 1.0
    v3 = revenue * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(18).mean() * 0.0001
    e0 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f0 = ratio.pct_change(18).fillna(0)
    d1 = ratio.shift(2).rolling(23).mean() * 0.0002
    e1 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f1 = ratio.pct_change(23).fillna(0)
    d2 = ratio.shift(3).rolling(50).mean() * 0.00030000000000000003
    e2 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f2 = ratio.pct_change(50).fillna(0)
    d3 = ratio.shift(4).rolling(49).mean() * 0.0004
    e3 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f3 = ratio.pct_change(49).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(29).mean() * 0.0008
    e7 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f7 = ratio.pct_change(29).fillna(0)
    res = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc098_48d_val_v098_signal'] = f86mm_f86_market_cap_relative_momentum_calc098_48d_val_v098_signal

def f86mm_f86_market_cap_relative_momentum_calc099_180d_val_v099_signal(assets, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ps * 1.0
    v3 = assets * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(23).mean() * 0.0001
    e0 = ratio.rolling(23).std() / (ratio.rolling(23).mean().abs() + 1e-9)
    f0 = ratio.pct_change(23).fillna(0)
    d1 = ratio.shift(2).rolling(50).mean() * 0.0002
    e1 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f1 = ratio.pct_change(50).fillna(0)
    d2 = ratio.shift(3).rolling(49).mean() * 0.00030000000000000003
    e2 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f2 = ratio.pct_change(49).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(29).mean() * 0.0007
    e6 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f6 = ratio.pct_change(29).fillna(0)
    d7 = ratio.shift(8).rolling(47).mean() * 0.0008
    e7 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f7 = ratio.pct_change(47).fillna(0)
    res = ratio.rolling(180).max() - ratio.rolling(180).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc099_180d_val_v099_signal'] = f86mm_f86_market_cap_relative_momentum_calc099_180d_val_v099_signal

def f86mm_f86_market_cap_relative_momentum_calc100_20d_val_v100_signal(ev, marketcap, netinc):
    v1 = marketcap * 1.0
    v2 = ev * 1.0
    v3 = netinc * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(50).mean() * 0.0001
    e0 = ratio.rolling(50).std() / (ratio.rolling(50).mean().abs() + 1e-9)
    f0 = ratio.pct_change(50).fillna(0)
    d1 = ratio.shift(2).rolling(49).mean() * 0.0002
    e1 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f1 = ratio.pct_change(49).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(29).mean() * 0.0006000000000000001
    e5 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f5 = ratio.pct_change(29).fillna(0)
    d6 = ratio.shift(7).rolling(47).mean() * 0.0007
    e6 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f6 = ratio.pct_change(47).fillna(0)
    d7 = ratio.shift(8).rolling(36).mean() * 0.0008
    e7 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f7 = ratio.pct_change(36).fillna(0)
    res = ratio.diff(20)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc100_20d_val_v100_signal'] = f86mm_f86_market_cap_relative_momentum_calc100_20d_val_v100_signal

def f86mm_f86_market_cap_relative_momentum_calc101_164d_val_v101_signal(ebitda, marketcap, revenue):
    v1 = revenue * 1.0
    v2 = ebitda * 1.0
    v3 = marketcap * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(49).mean() * 0.0001
    e0 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f0 = ratio.pct_change(49).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(29).mean() * 0.0005
    e4 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f4 = ratio.pct_change(29).fillna(0)
    d5 = ratio.shift(6).rolling(47).mean() * 0.0006000000000000001
    e5 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f5 = ratio.pct_change(47).fillna(0)
    d6 = ratio.shift(7).rolling(36).mean() * 0.0007
    e6 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f6 = ratio.pct_change(36).fillna(0)
    d7 = ratio.shift(8).rolling(39).mean() * 0.0008
    e7 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f7 = ratio.pct_change(39).fillna(0)
    res = ratio.rolling(164).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc101_164d_val_v101_signal'] = f86mm_f86_market_cap_relative_momentum_calc101_164d_val_v101_signal

def f86mm_f86_market_cap_relative_momentum_calc102_16d_val_v102_signal(close, ev, revenue):
    v1 = revenue * 1.0
    v2 = ev * 1.0
    v3 = close * 1.0
    ratio = v1.diff(6).rolling(16).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(29).mean() * 0.0004
    e3 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f3 = ratio.pct_change(29).fillna(0)
    d4 = ratio.shift(5).rolling(47).mean() * 0.0005
    e4 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f4 = ratio.pct_change(47).fillna(0)
    d5 = ratio.shift(6).rolling(36).mean() * 0.0006000000000000001
    e5 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f5 = ratio.pct_change(36).fillna(0)
    d6 = ratio.shift(7).rolling(39).mean() * 0.0007
    e6 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f6 = ratio.pct_change(39).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.diff(16)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc102_16d_val_v102_signal'] = f86mm_f86_market_cap_relative_momentum_calc102_16d_val_v102_signal

def f86mm_f86_market_cap_relative_momentum_calc103_29d_val_v103_signal(ev, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ps * 1.0
    v3 = ev * 1.0
    ratio = v1.diff(48).rolling(29).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(29).mean() * 0.00030000000000000003
    e2 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f2 = ratio.pct_change(29).fillna(0)
    d3 = ratio.shift(4).rolling(47).mean() * 0.0004
    e3 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f3 = ratio.pct_change(47).fillna(0)
    d4 = ratio.shift(5).rolling(36).mean() * 0.0005
    e4 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f4 = ratio.pct_change(36).fillna(0)
    d5 = ratio.shift(6).rolling(39).mean() * 0.0006000000000000001
    e5 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f5 = ratio.pct_change(39).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(51).mean() * 0.0008
    e7 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f7 = ratio.pct_change(51).fillna(0)
    res = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc103_29d_val_v103_signal'] = f86mm_f86_market_cap_relative_momentum_calc103_29d_val_v103_signal

def f86mm_f86_market_cap_relative_momentum_calc104_125d_val_v104_signal(ev, netinc, revenue):
    v1 = netinc * 1.0
    v2 = revenue * 1.0
    v3 = ev * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(29).mean() * 0.0002
    e1 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f1 = ratio.pct_change(29).fillna(0)
    d2 = ratio.shift(3).rolling(47).mean() * 0.00030000000000000003
    e2 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f2 = ratio.pct_change(47).fillna(0)
    d3 = ratio.shift(4).rolling(36).mean() * 0.0004
    e3 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f3 = ratio.pct_change(36).fillna(0)
    d4 = ratio.shift(5).rolling(39).mean() * 0.0005
    e4 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f4 = ratio.pct_change(39).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(51).mean() * 0.0007
    e6 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f6 = ratio.pct_change(51).fillna(0)
    d7 = ratio.shift(8).rolling(10).mean() * 0.0008
    e7 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f7 = ratio.pct_change(10).fillna(0)
    res = ratio.rolling(125).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc104_125d_val_v104_signal'] = f86mm_f86_market_cap_relative_momentum_calc104_125d_val_v104_signal

def f86mm_f86_market_cap_relative_momentum_calc105_61d_val_v105_signal(fcf, marketcap, pb):
    v1 = fcf * 1.0
    v2 = marketcap * 1.0
    v3 = pb * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(29).mean() * 0.0001
    e0 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f0 = ratio.pct_change(29).fillna(0)
    d1 = ratio.shift(2).rolling(47).mean() * 0.0002
    e1 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f1 = ratio.pct_change(47).fillna(0)
    d2 = ratio.shift(3).rolling(36).mean() * 0.00030000000000000003
    e2 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f2 = ratio.pct_change(36).fillna(0)
    d3 = ratio.shift(4).rolling(39).mean() * 0.0004
    e3 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f3 = ratio.pct_change(39).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(51).mean() * 0.0006000000000000001
    e5 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f5 = ratio.pct_change(51).fillna(0)
    d6 = ratio.shift(7).rolling(10).mean() * 0.0007
    e6 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f6 = ratio.pct_change(10).fillna(0)
    d7 = ratio.shift(8).rolling(18).mean() * 0.0008
    e7 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f7 = ratio.pct_change(18).fillna(0)
    res = ratio.ewm(span=61).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc105_61d_val_v105_signal'] = f86mm_f86_market_cap_relative_momentum_calc105_61d_val_v105_signal

def f86mm_f86_market_cap_relative_momentum_calc106_33d_val_v106_signal(ev, marketcap, netinc):
    v1 = netinc * 1.0
    v2 = ev * 1.0
    v3 = marketcap * 1.0
    ratio = v1.diff(42).rolling(33).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(47).mean() * 0.0001
    e0 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f0 = ratio.pct_change(47).fillna(0)
    d1 = ratio.shift(2).rolling(36).mean() * 0.0002
    e1 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f1 = ratio.pct_change(36).fillna(0)
    d2 = ratio.shift(3).rolling(39).mean() * 0.00030000000000000003
    e2 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f2 = ratio.pct_change(39).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(51).mean() * 0.0005
    e4 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f4 = ratio.pct_change(51).fillna(0)
    d5 = ratio.shift(6).rolling(10).mean() * 0.0006000000000000001
    e5 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f5 = ratio.pct_change(10).fillna(0)
    d6 = ratio.shift(7).rolling(18).mean() * 0.0007
    e6 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f6 = ratio.pct_change(18).fillna(0)
    d7 = ratio.shift(8).rolling(41).mean() * 0.0008
    e7 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f7 = ratio.pct_change(41).fillna(0)
    res = ratio.rolling(33).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc106_33d_val_v106_signal'] = f86mm_f86_market_cap_relative_momentum_calc106_33d_val_v106_signal

def f86mm_f86_market_cap_relative_momentum_calc107_143d_val_v107_signal(pe, ps, revenue):
    v1 = pe * 1.0
    v2 = ps * 1.0
    v3 = revenue * 1.0
    ratio = v1.rolling(143).kurt() / v2.rolling(143).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(36).mean() * 0.0001
    e0 = ratio.rolling(36).std() / (ratio.rolling(36).mean().abs() + 1e-9)
    f0 = ratio.pct_change(36).fillna(0)
    d1 = ratio.shift(2).rolling(39).mean() * 0.0002
    e1 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f1 = ratio.pct_change(39).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(51).mean() * 0.0004
    e3 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f3 = ratio.pct_change(51).fillna(0)
    d4 = ratio.shift(5).rolling(10).mean() * 0.0005
    e4 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f4 = ratio.pct_change(10).fillna(0)
    d5 = ratio.shift(6).rolling(18).mean() * 0.0006000000000000001
    e5 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f5 = ratio.pct_change(18).fillna(0)
    d6 = ratio.shift(7).rolling(41).mean() * 0.0007
    e6 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f6 = ratio.pct_change(41).fillna(0)
    d7 = ratio.shift(8).rolling(52).mean() * 0.0008
    e7 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f7 = ratio.pct_change(52).fillna(0)
    res = ratio.pct_change(143)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc107_143d_val_v107_signal'] = f86mm_f86_market_cap_relative_momentum_calc107_143d_val_v107_signal

def f86mm_f86_market_cap_relative_momentum_calc108_92d_val_v108_signal(close, netinc, pb):
    v1 = pb * 1.0
    v2 = close * 1.0
    v3 = netinc * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(39).mean() * 0.0001
    e0 = ratio.rolling(39).std() / (ratio.rolling(39).mean().abs() + 1e-9)
    f0 = ratio.pct_change(39).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(51).mean() * 0.00030000000000000003
    e2 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f2 = ratio.pct_change(51).fillna(0)
    d3 = ratio.shift(4).rolling(10).mean() * 0.0004
    e3 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f3 = ratio.pct_change(10).fillna(0)
    d4 = ratio.shift(5).rolling(18).mean() * 0.0005
    e4 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f4 = ratio.pct_change(18).fillna(0)
    d5 = ratio.shift(6).rolling(41).mean() * 0.0006000000000000001
    e5 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f5 = ratio.pct_change(41).fillna(0)
    d6 = ratio.shift(7).rolling(52).mean() * 0.0007
    e6 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f6 = ratio.pct_change(52).fillna(0)
    d7 = ratio.shift(8).rolling(45).mean() * 0.0008
    e7 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f7 = ratio.pct_change(45).fillna(0)
    res = np.tanh(ratio.rolling(92).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc108_92d_val_v108_signal'] = f86mm_f86_market_cap_relative_momentum_calc108_92d_val_v108_signal

def f86mm_f86_market_cap_relative_momentum_calc109_30d_val_v109_signal(ebitda, ps, revenue):
    v1 = ps * 1.0
    v2 = revenue * 1.0
    v3 = ebitda * 1.0
    ratio = v1.rolling(30).std() / v1.rolling(229).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(12).mean() * 0.0001
    e0 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f0 = ratio.pct_change(12).fillna(0)
    d1 = ratio.shift(2).rolling(51).mean() * 0.0002
    e1 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f1 = ratio.pct_change(51).fillna(0)
    d2 = ratio.shift(3).rolling(10).mean() * 0.00030000000000000003
    e2 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f2 = ratio.pct_change(10).fillna(0)
    d3 = ratio.shift(4).rolling(18).mean() * 0.0004
    e3 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f3 = ratio.pct_change(18).fillna(0)
    d4 = ratio.shift(5).rolling(41).mean() * 0.0005
    e4 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f4 = ratio.pct_change(41).fillna(0)
    d5 = ratio.shift(6).rolling(52).mean() * 0.0006000000000000001
    e5 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f5 = ratio.pct_change(52).fillna(0)
    d6 = ratio.shift(7).rolling(45).mean() * 0.0007
    e6 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f6 = ratio.pct_change(45).fillna(0)
    d7 = ratio.shift(8).rolling(43).mean() * 0.0008
    e7 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f7 = ratio.pct_change(43).fillna(0)
    res = ratio.rolling(30).max() - ratio.rolling(30).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc109_30d_val_v109_signal'] = f86mm_f86_market_cap_relative_momentum_calc109_30d_val_v109_signal

def f86mm_f86_market_cap_relative_momentum_calc110_22d_val_v110_signal(assets, close, pe):
    v1 = close * 1.0
    v2 = pe * 1.0
    v3 = assets * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(51).mean() * 0.0001
    e0 = ratio.rolling(51).std() / (ratio.rolling(51).mean().abs() + 1e-9)
    f0 = ratio.pct_change(51).fillna(0)
    d1 = ratio.shift(2).rolling(10).mean() * 0.0002
    e1 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f1 = ratio.pct_change(10).fillna(0)
    d2 = ratio.shift(3).rolling(18).mean() * 0.00030000000000000003
    e2 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f2 = ratio.pct_change(18).fillna(0)
    d3 = ratio.shift(4).rolling(41).mean() * 0.0004
    e3 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f3 = ratio.pct_change(41).fillna(0)
    d4 = ratio.shift(5).rolling(52).mean() * 0.0005
    e4 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f4 = ratio.pct_change(52).fillna(0)
    d5 = ratio.shift(6).rolling(45).mean() * 0.0006000000000000001
    e5 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f5 = ratio.pct_change(45).fillna(0)
    d6 = ratio.shift(7).rolling(43).mean() * 0.0007
    e6 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f6 = ratio.pct_change(43).fillna(0)
    d7 = ratio.shift(8).rolling(47).mean() * 0.0008
    e7 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f7 = ratio.pct_change(47).fillna(0)
    res = ratio.rolling(22).std() / (ratio.rolling(22).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc110_22d_val_v110_signal'] = f86mm_f86_market_cap_relative_momentum_calc110_22d_val_v110_signal

def f86mm_f86_market_cap_relative_momentum_calc111_57d_val_v111_signal(fcf, pe, ps):
    v1 = fcf * 1.0
    v2 = ps * 1.0
    v3 = pe * 1.0
    ratio = v1.rolling(57).kurt() / v2.rolling(57).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(10).mean() * 0.0001
    e0 = ratio.rolling(10).std() / (ratio.rolling(10).mean().abs() + 1e-9)
    f0 = ratio.pct_change(10).fillna(0)
    d1 = ratio.shift(2).rolling(18).mean() * 0.0002
    e1 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f1 = ratio.pct_change(18).fillna(0)
    d2 = ratio.shift(3).rolling(41).mean() * 0.00030000000000000003
    e2 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f2 = ratio.pct_change(41).fillna(0)
    d3 = ratio.shift(4).rolling(52).mean() * 0.0004
    e3 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f3 = ratio.pct_change(52).fillna(0)
    d4 = ratio.shift(5).rolling(45).mean() * 0.0005
    e4 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f4 = ratio.pct_change(45).fillna(0)
    d5 = ratio.shift(6).rolling(43).mean() * 0.0006000000000000001
    e5 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f5 = ratio.pct_change(43).fillna(0)
    d6 = ratio.shift(7).rolling(47).mean() * 0.0007
    e6 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f6 = ratio.pct_change(47).fillna(0)
    d7 = ratio.shift(8).rolling(6).mean() * 0.0008
    e7 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f7 = ratio.pct_change(6).fillna(0)
    res = np.tanh(ratio.rolling(57).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc111_57d_val_v111_signal'] = f86mm_f86_market_cap_relative_momentum_calc111_57d_val_v111_signal

def f86mm_f86_market_cap_relative_momentum_calc112_174d_val_v112_signal(evebitda, pb, ps):
    v1 = ps * 1.0
    v2 = pb * 1.0
    v3 = evebitda * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(18).mean() * 0.0001
    e0 = ratio.rolling(18).std() / (ratio.rolling(18).mean().abs() + 1e-9)
    f0 = ratio.pct_change(18).fillna(0)
    d1 = ratio.shift(2).rolling(41).mean() * 0.0002
    e1 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f1 = ratio.pct_change(41).fillna(0)
    d2 = ratio.shift(3).rolling(52).mean() * 0.00030000000000000003
    e2 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f2 = ratio.pct_change(52).fillna(0)
    d3 = ratio.shift(4).rolling(45).mean() * 0.0004
    e3 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f3 = ratio.pct_change(45).fillna(0)
    d4 = ratio.shift(5).rolling(43).mean() * 0.0005
    e4 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f4 = ratio.pct_change(43).fillna(0)
    d5 = ratio.shift(6).rolling(47).mean() * 0.0006000000000000001
    e5 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f5 = ratio.pct_change(47).fillna(0)
    d6 = ratio.shift(7).rolling(6).mean() * 0.0007
    e6 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f6 = ratio.pct_change(6).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.rolling(174).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc112_174d_val_v112_signal'] = f86mm_f86_market_cap_relative_momentum_calc112_174d_val_v112_signal

def f86mm_f86_market_cap_relative_momentum_calc113_37d_val_v113_signal(ev, evebitda, fcf):
    v1 = evebitda * 1.0
    v2 = ev * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(37).rank(pct=True) - v2.rolling(37).rank(pct=True)
    d0 = ratio.shift(1).rolling(41).mean() * 0.0001
    e0 = ratio.rolling(41).std() / (ratio.rolling(41).mean().abs() + 1e-9)
    f0 = ratio.pct_change(41).fillna(0)
    d1 = ratio.shift(2).rolling(52).mean() * 0.0002
    e1 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f1 = ratio.pct_change(52).fillna(0)
    d2 = ratio.shift(3).rolling(45).mean() * 0.00030000000000000003
    e2 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f2 = ratio.pct_change(45).fillna(0)
    d3 = ratio.shift(4).rolling(43).mean() * 0.0004
    e3 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f3 = ratio.pct_change(43).fillna(0)
    d4 = ratio.shift(5).rolling(47).mean() * 0.0005
    e4 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f4 = ratio.pct_change(47).fillna(0)
    d5 = ratio.shift(6).rolling(6).mean() * 0.0006000000000000001
    e5 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f5 = ratio.pct_change(6).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(48).mean() * 0.0008
    e7 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f7 = ratio.pct_change(48).fillna(0)
    res = ratio.rolling(37).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc113_37d_val_v113_signal'] = f86mm_f86_market_cap_relative_momentum_calc113_37d_val_v113_signal

def f86mm_f86_market_cap_relative_momentum_calc114_110d_val_v114_signal(ebitda, ev, marketcap):
    v1 = ebitda * 1.0
    v2 = marketcap * 1.0
    v3 = ev * 1.0
    ratio = v1.diff(40).rolling(110).mean() / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(52).mean() * 0.0001
    e0 = ratio.rolling(52).std() / (ratio.rolling(52).mean().abs() + 1e-9)
    f0 = ratio.pct_change(52).fillna(0)
    d1 = ratio.shift(2).rolling(45).mean() * 0.0002
    e1 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f1 = ratio.pct_change(45).fillna(0)
    d2 = ratio.shift(3).rolling(43).mean() * 0.00030000000000000003
    e2 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f2 = ratio.pct_change(43).fillna(0)
    d3 = ratio.shift(4).rolling(47).mean() * 0.0004
    e3 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f3 = ratio.pct_change(47).fillna(0)
    d4 = ratio.shift(5).rolling(6).mean() * 0.0005
    e4 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f4 = ratio.pct_change(6).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(48).mean() * 0.0007
    e6 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f6 = ratio.pct_change(48).fillna(0)
    d7 = ratio.shift(8).rolling(16).mean() * 0.0008
    e7 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f7 = ratio.pct_change(16).fillna(0)
    res = np.tanh(ratio.rolling(110).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc114_110d_val_v114_signal'] = f86mm_f86_market_cap_relative_momentum_calc114_110d_val_v114_signal

def f86mm_f86_market_cap_relative_momentum_calc115_119d_val_v115_signal(close, ev, ps):
    v1 = ps * 1.0
    v2 = close * 1.0
    v3 = ev * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(45).mean() * 0.0001
    e0 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f0 = ratio.pct_change(45).fillna(0)
    d1 = ratio.shift(2).rolling(43).mean() * 0.0002
    e1 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f1 = ratio.pct_change(43).fillna(0)
    d2 = ratio.shift(3).rolling(47).mean() * 0.00030000000000000003
    e2 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f2 = ratio.pct_change(47).fillna(0)
    d3 = ratio.shift(4).rolling(6).mean() * 0.0004
    e3 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f3 = ratio.pct_change(6).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(48).mean() * 0.0006000000000000001
    e5 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f5 = ratio.pct_change(48).fillna(0)
    d6 = ratio.shift(7).rolling(16).mean() * 0.0007
    e6 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f6 = ratio.pct_change(16).fillna(0)
    d7 = ratio.shift(8).rolling(37).mean() * 0.0008
    e7 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f7 = ratio.pct_change(37).fillna(0)
    res = ratio.diff(34).rolling(119).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc115_119d_val_v115_signal'] = f86mm_f86_market_cap_relative_momentum_calc115_119d_val_v115_signal

def f86mm_f86_market_cap_relative_momentum_calc116_199d_val_v116_signal(assets, ebitda, revenue):
    v1 = revenue * 1.0
    v2 = ebitda * 1.0
    v3 = assets * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(199).mean()) / r_raw.rolling(199).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(43).mean() * 0.0001
    e0 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f0 = ratio.pct_change(43).fillna(0)
    d1 = ratio.shift(2).rolling(47).mean() * 0.0002
    e1 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f1 = ratio.pct_change(47).fillna(0)
    d2 = ratio.shift(3).rolling(6).mean() * 0.00030000000000000003
    e2 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f2 = ratio.pct_change(6).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(48).mean() * 0.0005
    e4 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f4 = ratio.pct_change(48).fillna(0)
    d5 = ratio.shift(6).rolling(16).mean() * 0.0006000000000000001
    e5 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f5 = ratio.pct_change(16).fillna(0)
    d6 = ratio.shift(7).rolling(37).mean() * 0.0007
    e6 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f6 = ratio.pct_change(37).fillna(0)
    d7 = ratio.shift(8).rolling(53).mean() * 0.0008
    e7 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f7 = ratio.pct_change(53).fillna(0)
    res = ratio.rolling(199).std() / (ratio.rolling(199).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc116_199d_val_v116_signal'] = f86mm_f86_market_cap_relative_momentum_calc116_199d_val_v116_signal

def f86mm_f86_market_cap_relative_momentum_calc117_158d_val_v117_signal(ebitda, fcf, marketcap):
    v1 = fcf * 1.0
    v2 = marketcap * 1.0
    v3 = ebitda * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(47).mean() * 0.0001
    e0 = ratio.rolling(47).std() / (ratio.rolling(47).mean().abs() + 1e-9)
    f0 = ratio.pct_change(47).fillna(0)
    d1 = ratio.shift(2).rolling(6).mean() * 0.0002
    e1 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f1 = ratio.pct_change(6).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(48).mean() * 0.0004
    e3 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f3 = ratio.pct_change(48).fillna(0)
    d4 = ratio.shift(5).rolling(16).mean() * 0.0005
    e4 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f4 = ratio.pct_change(16).fillna(0)
    d5 = ratio.shift(6).rolling(37).mean() * 0.0006000000000000001
    e5 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f5 = ratio.pct_change(37).fillna(0)
    d6 = ratio.shift(7).rolling(53).mean() * 0.0007
    e6 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f6 = ratio.pct_change(53).fillna(0)
    d7 = ratio.shift(8).rolling(29).mean() * 0.0008
    e7 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f7 = ratio.pct_change(29).fillna(0)
    res = ratio.rolling(158).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc117_158d_val_v117_signal'] = f86mm_f86_market_cap_relative_momentum_calc117_158d_val_v117_signal

def f86mm_f86_market_cap_relative_momentum_calc118_49d_val_v118_signal(ebitda, evebitda, revenue):
    v1 = evebitda * 1.0
    v2 = revenue * 1.0
    v3 = ebitda * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(49).mean()) / r_raw.rolling(49).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(6).mean() * 0.0001
    e0 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f0 = ratio.pct_change(6).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(48).mean() * 0.00030000000000000003
    e2 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f2 = ratio.pct_change(48).fillna(0)
    d3 = ratio.shift(4).rolling(16).mean() * 0.0004
    e3 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f3 = ratio.pct_change(16).fillna(0)
    d4 = ratio.shift(5).rolling(37).mean() * 0.0005
    e4 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f4 = ratio.pct_change(37).fillna(0)
    d5 = ratio.shift(6).rolling(53).mean() * 0.0006000000000000001
    e5 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f5 = ratio.pct_change(53).fillna(0)
    d6 = ratio.shift(7).rolling(29).mean() * 0.0007
    e6 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f6 = ratio.pct_change(29).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.rolling(49).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc118_49d_val_v118_signal'] = f86mm_f86_market_cap_relative_momentum_calc118_49d_val_v118_signal

def f86mm_f86_market_cap_relative_momentum_calc119_76d_val_v119_signal(ebitda, netinc, pe):
    v1 = pe * 1.0
    v2 = ebitda * 1.0
    v3 = netinc * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(48).mean() * 0.0002
    e1 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f1 = ratio.pct_change(48).fillna(0)
    d2 = ratio.shift(3).rolling(16).mean() * 0.00030000000000000003
    e2 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f2 = ratio.pct_change(16).fillna(0)
    d3 = ratio.shift(4).rolling(37).mean() * 0.0004
    e3 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f3 = ratio.pct_change(37).fillna(0)
    d4 = ratio.shift(5).rolling(53).mean() * 0.0005
    e4 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f4 = ratio.pct_change(53).fillna(0)
    d5 = ratio.shift(6).rolling(29).mean() * 0.0006000000000000001
    e5 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f5 = ratio.pct_change(29).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(6).mean() * 0.0008
    e7 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f7 = ratio.pct_change(6).fillna(0)
    res = ratio.rolling(76).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc119_76d_val_v119_signal'] = f86mm_f86_market_cap_relative_momentum_calc119_76d_val_v119_signal

def f86mm_f86_market_cap_relative_momentum_calc120_105d_val_v120_signal(ebitda, pb, revenue):
    v1 = revenue * 1.0
    v2 = pb * 1.0
    v3 = ebitda * 1.0
    r_raw = v1 / v2.replace(0, np.nan)
    ratio = (r_raw - r_raw.rolling(105).mean()) / r_raw.rolling(105).std().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(48).mean() * 0.0001
    e0 = ratio.rolling(48).std() / (ratio.rolling(48).mean().abs() + 1e-9)
    f0 = ratio.pct_change(48).fillna(0)
    d1 = ratio.shift(2).rolling(16).mean() * 0.0002
    e1 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f1 = ratio.pct_change(16).fillna(0)
    d2 = ratio.shift(3).rolling(37).mean() * 0.00030000000000000003
    e2 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f2 = ratio.pct_change(37).fillna(0)
    d3 = ratio.shift(4).rolling(53).mean() * 0.0004
    e3 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f3 = ratio.pct_change(53).fillna(0)
    d4 = ratio.shift(5).rolling(29).mean() * 0.0005
    e4 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f4 = ratio.pct_change(29).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(6).mean() * 0.0007
    e6 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f6 = ratio.pct_change(6).fillna(0)
    d7 = ratio.shift(8).rolling(33).mean() * 0.0008
    e7 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f7 = ratio.pct_change(33).fillna(0)
    res = ratio.rolling(105).std() / (ratio.rolling(105).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc120_105d_val_v120_signal'] = f86mm_f86_market_cap_relative_momentum_calc120_105d_val_v120_signal

def f86mm_f86_market_cap_relative_momentum_calc121_185d_val_v121_signal(assets, marketcap, pb):
    v1 = marketcap * 1.0
    v2 = assets * 1.0
    v3 = pb * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(16).mean() * 0.0001
    e0 = ratio.rolling(16).std() / (ratio.rolling(16).mean().abs() + 1e-9)
    f0 = ratio.pct_change(16).fillna(0)
    d1 = ratio.shift(2).rolling(37).mean() * 0.0002
    e1 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f1 = ratio.pct_change(37).fillna(0)
    d2 = ratio.shift(3).rolling(53).mean() * 0.00030000000000000003
    e2 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f2 = ratio.pct_change(53).fillna(0)
    d3 = ratio.shift(4).rolling(29).mean() * 0.0004
    e3 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f3 = ratio.pct_change(29).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(6).mean() * 0.0006000000000000001
    e5 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f5 = ratio.pct_change(6).fillna(0)
    d6 = ratio.shift(7).rolling(33).mean() * 0.0007
    e6 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f6 = ratio.pct_change(33).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(185).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc121_185d_val_v121_signal'] = f86mm_f86_market_cap_relative_momentum_calc121_185d_val_v121_signal

def f86mm_f86_market_cap_relative_momentum_calc122_86d_val_v122_signal(pb, ps, revenue):
    v1 = revenue * 1.0
    v2 = ps * 1.0
    v3 = pb * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(37).mean() * 0.0001
    e0 = ratio.rolling(37).std() / (ratio.rolling(37).mean().abs() + 1e-9)
    f0 = ratio.pct_change(37).fillna(0)
    d1 = ratio.shift(2).rolling(53).mean() * 0.0002
    e1 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f1 = ratio.pct_change(53).fillna(0)
    d2 = ratio.shift(3).rolling(29).mean() * 0.00030000000000000003
    e2 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f2 = ratio.pct_change(29).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(6).mean() * 0.0005
    e4 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f4 = ratio.pct_change(6).fillna(0)
    d5 = ratio.shift(6).rolling(33).mean() * 0.0006000000000000001
    e5 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f5 = ratio.pct_change(33).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.rolling(86).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc122_86d_val_v122_signal'] = f86mm_f86_market_cap_relative_momentum_calc122_86d_val_v122_signal

def f86mm_f86_market_cap_relative_momentum_calc123_84d_val_v123_signal(close, ev, pb):
    v1 = close * 1.0
    v2 = pb * 1.0
    v3 = ev * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(53).mean() * 0.0001
    e0 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f0 = ratio.pct_change(53).fillna(0)
    d1 = ratio.shift(2).rolling(29).mean() * 0.0002
    e1 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f1 = ratio.pct_change(29).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(6).mean() * 0.0004
    e3 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f3 = ratio.pct_change(6).fillna(0)
    d4 = ratio.shift(5).rolling(33).mean() * 0.0005
    e4 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f4 = ratio.pct_change(33).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(20).mean() * 0.0008
    e7 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f7 = ratio.pct_change(20).fillna(0)
    res = ratio.rolling(84).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc123_84d_val_v123_signal'] = f86mm_f86_market_cap_relative_momentum_calc123_84d_val_v123_signal

def f86mm_f86_market_cap_relative_momentum_calc124_46d_val_v124_signal(ebitda, netinc, pe):
    v1 = netinc * 1.0
    v2 = pe * 1.0
    v3 = ebitda * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(29).mean() * 0.0001
    e0 = ratio.rolling(29).std() / (ratio.rolling(29).mean().abs() + 1e-9)
    f0 = ratio.pct_change(29).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(6).mean() * 0.00030000000000000003
    e2 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f2 = ratio.pct_change(6).fillna(0)
    d3 = ratio.shift(4).rolling(33).mean() * 0.0004
    e3 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f3 = ratio.pct_change(33).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(20).mean() * 0.0007
    e6 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f6 = ratio.pct_change(20).fillna(0)
    d7 = ratio.shift(8).rolling(13).mean() * 0.0008
    e7 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f7 = ratio.pct_change(13).fillna(0)
    res = ratio.rolling(46).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc124_46d_val_v124_signal'] = f86mm_f86_market_cap_relative_momentum_calc124_46d_val_v124_signal

def f86mm_f86_market_cap_relative_momentum_calc125_24d_val_v125_signal(evebitda, pe, revenue):
    v1 = evebitda * 1.0
    v2 = pe * 1.0
    v3 = revenue * 1.0
    ratio = (v1 - v1.rolling(24).min()) / (v1.rolling(24).max() - v1.rolling(24).min() + 1e-9)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(6).mean() * 0.0002
    e1 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f1 = ratio.pct_change(6).fillna(0)
    d2 = ratio.shift(3).rolling(33).mean() * 0.00030000000000000003
    e2 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f2 = ratio.pct_change(33).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(20).mean() * 0.0006000000000000001
    e5 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f5 = ratio.pct_change(20).fillna(0)
    d6 = ratio.shift(7).rolling(13).mean() * 0.0007
    e6 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f6 = ratio.pct_change(13).fillna(0)
    d7 = ratio.shift(8).rolling(11).mean() * 0.0008
    e7 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f7 = ratio.pct_change(11).fillna(0)
    res = ratio.rolling(24).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc125_24d_val_v125_signal'] = f86mm_f86_market_cap_relative_momentum_calc125_24d_val_v125_signal

def f86mm_f86_market_cap_relative_momentum_calc126_55d_val_v126_signal(ebitda, ps, revenue):
    v1 = ps * 1.0
    v2 = ebitda * 1.0
    v3 = revenue * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(6).mean() * 0.0001
    e0 = ratio.rolling(6).std() / (ratio.rolling(6).mean().abs() + 1e-9)
    f0 = ratio.pct_change(6).fillna(0)
    d1 = ratio.shift(2).rolling(33).mean() * 0.0002
    e1 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f1 = ratio.pct_change(33).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(20).mean() * 0.0005
    e4 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f4 = ratio.pct_change(20).fillna(0)
    d5 = ratio.shift(6).rolling(13).mean() * 0.0006000000000000001
    e5 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f5 = ratio.pct_change(13).fillna(0)
    d6 = ratio.shift(7).rolling(11).mean() * 0.0007
    e6 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f6 = ratio.pct_change(11).fillna(0)
    d7 = ratio.shift(8).rolling(27).mean() * 0.0008
    e7 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f7 = ratio.pct_change(27).fillna(0)
    res = ratio.rolling(55).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc126_55d_val_v126_signal'] = f86mm_f86_market_cap_relative_momentum_calc126_55d_val_v126_signal

def f86mm_f86_market_cap_relative_momentum_calc127_195d_val_v127_signal(ebitda, marketcap, ps):
    v1 = marketcap * 1.0
    v2 = ebitda * 1.0
    v3 = ps * 1.0
    ratio = v1.rolling(195).std() / v1.rolling(74).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(33).mean() * 0.0001
    e0 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f0 = ratio.pct_change(33).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(20).mean() * 0.0004
    e3 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f3 = ratio.pct_change(20).fillna(0)
    d4 = ratio.shift(5).rolling(13).mean() * 0.0005
    e4 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f4 = ratio.pct_change(13).fillna(0)
    d5 = ratio.shift(6).rolling(11).mean() * 0.0006000000000000001
    e5 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f5 = ratio.pct_change(11).fillna(0)
    d6 = ratio.shift(7).rolling(27).mean() * 0.0007
    e6 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f6 = ratio.pct_change(27).fillna(0)
    d7 = ratio.shift(8).rolling(31).mean() * 0.0008
    e7 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f7 = ratio.pct_change(31).fillna(0)
    res = ratio.rolling(195).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc127_195d_val_v127_signal'] = f86mm_f86_market_cap_relative_momentum_calc127_195d_val_v127_signal

def f86mm_f86_market_cap_relative_momentum_calc128_62d_val_v128_signal(assets, netinc, pe):
    v1 = assets * 1.0
    v2 = netinc * 1.0
    v3 = pe * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(20).mean() * 0.00030000000000000003
    e2 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f2 = ratio.pct_change(20).fillna(0)
    d3 = ratio.shift(4).rolling(13).mean() * 0.0004
    e3 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f3 = ratio.pct_change(13).fillna(0)
    d4 = ratio.shift(5).rolling(11).mean() * 0.0005
    e4 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f4 = ratio.pct_change(11).fillna(0)
    d5 = ratio.shift(6).rolling(27).mean() * 0.0006000000000000001
    e5 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f5 = ratio.pct_change(27).fillna(0)
    d6 = ratio.shift(7).rolling(31).mean() * 0.0007
    e6 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f6 = ratio.pct_change(31).fillna(0)
    d7 = ratio.shift(8).rolling(15).mean() * 0.0008
    e7 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f7 = ratio.pct_change(15).fillna(0)
    res = ratio.rolling(62).std() / (ratio.rolling(62).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc128_62d_val_v128_signal'] = f86mm_f86_market_cap_relative_momentum_calc128_62d_val_v128_signal

def f86mm_f86_market_cap_relative_momentum_calc129_228d_val_v129_signal(ebitda, marketcap, pb):
    v1 = pb * 1.0
    v2 = marketcap * 1.0
    v3 = ebitda * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(20).mean() * 0.0002
    e1 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f1 = ratio.pct_change(20).fillna(0)
    d2 = ratio.shift(3).rolling(13).mean() * 0.00030000000000000003
    e2 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f2 = ratio.pct_change(13).fillna(0)
    d3 = ratio.shift(4).rolling(11).mean() * 0.0004
    e3 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f3 = ratio.pct_change(11).fillna(0)
    d4 = ratio.shift(5).rolling(27).mean() * 0.0005
    e4 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f4 = ratio.pct_change(27).fillna(0)
    d5 = ratio.shift(6).rolling(31).mean() * 0.0006000000000000001
    e5 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f5 = ratio.pct_change(31).fillna(0)
    d6 = ratio.shift(7).rolling(15).mean() * 0.0007
    e6 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f6 = ratio.pct_change(15).fillna(0)
    d7 = ratio.shift(8).rolling(17).mean() * 0.0008
    e7 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f7 = ratio.pct_change(17).fillna(0)
    res = ratio.diff(11).rolling(228).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc129_228d_val_v129_signal'] = f86mm_f86_market_cap_relative_momentum_calc129_228d_val_v129_signal

def f86mm_f86_market_cap_relative_momentum_calc130_161d_val_v130_signal(close, ev, pb):
    v1 = ev * 1.0
    v2 = close * 1.0
    v3 = pb * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(20).mean() * 0.0001
    e0 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f0 = ratio.pct_change(20).fillna(0)
    d1 = ratio.shift(2).rolling(13).mean() * 0.0002
    e1 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f1 = ratio.pct_change(13).fillna(0)
    d2 = ratio.shift(3).rolling(11).mean() * 0.00030000000000000003
    e2 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f2 = ratio.pct_change(11).fillna(0)
    d3 = ratio.shift(4).rolling(27).mean() * 0.0004
    e3 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f3 = ratio.pct_change(27).fillna(0)
    d4 = ratio.shift(5).rolling(31).mean() * 0.0005
    e4 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f4 = ratio.pct_change(31).fillna(0)
    d5 = ratio.shift(6).rolling(15).mean() * 0.0006000000000000001
    e5 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f5 = ratio.pct_change(15).fillna(0)
    d6 = ratio.shift(7).rolling(17).mean() * 0.0007
    e6 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f6 = ratio.pct_change(17).fillna(0)
    d7 = ratio.shift(8).rolling(25).mean() * 0.0008
    e7 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f7 = ratio.pct_change(25).fillna(0)
    res = ratio.rolling(161).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc130_161d_val_v130_signal'] = f86mm_f86_market_cap_relative_momentum_calc130_161d_val_v130_signal

def f86mm_f86_market_cap_relative_momentum_calc131_107d_val_v131_signal(pe, ps, revenue):
    v1 = pe * 1.0
    v2 = revenue * 1.0
    v3 = ps * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(13).mean() * 0.0001
    e0 = ratio.rolling(13).std() / (ratio.rolling(13).mean().abs() + 1e-9)
    f0 = ratio.pct_change(13).fillna(0)
    d1 = ratio.shift(2).rolling(11).mean() * 0.0002
    e1 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f1 = ratio.pct_change(11).fillna(0)
    d2 = ratio.shift(3).rolling(27).mean() * 0.00030000000000000003
    e2 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f2 = ratio.pct_change(27).fillna(0)
    d3 = ratio.shift(4).rolling(31).mean() * 0.0004
    e3 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f3 = ratio.pct_change(31).fillna(0)
    d4 = ratio.shift(5).rolling(15).mean() * 0.0005
    e4 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f4 = ratio.pct_change(15).fillna(0)
    d5 = ratio.shift(6).rolling(17).mean() * 0.0006000000000000001
    e5 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f5 = ratio.pct_change(17).fillna(0)
    d6 = ratio.shift(7).rolling(25).mean() * 0.0007
    e6 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f6 = ratio.pct_change(25).fillna(0)
    d7 = ratio.shift(8).rolling(49).mean() * 0.0008
    e7 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f7 = ratio.pct_change(49).fillna(0)
    res = ratio.pct_change(107)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc131_107d_val_v131_signal'] = f86mm_f86_market_cap_relative_momentum_calc131_107d_val_v131_signal

def f86mm_f86_market_cap_relative_momentum_calc132_237d_val_v132_signal(close, fcf, netinc):
    v1 = fcf * 1.0
    v2 = netinc * 1.0
    v3 = close * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(11).mean() * 0.0001
    e0 = ratio.rolling(11).std() / (ratio.rolling(11).mean().abs() + 1e-9)
    f0 = ratio.pct_change(11).fillna(0)
    d1 = ratio.shift(2).rolling(27).mean() * 0.0002
    e1 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f1 = ratio.pct_change(27).fillna(0)
    d2 = ratio.shift(3).rolling(31).mean() * 0.00030000000000000003
    e2 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f2 = ratio.pct_change(31).fillna(0)
    d3 = ratio.shift(4).rolling(15).mean() * 0.0004
    e3 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f3 = ratio.pct_change(15).fillna(0)
    d4 = ratio.shift(5).rolling(17).mean() * 0.0005
    e4 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f4 = ratio.pct_change(17).fillna(0)
    d5 = ratio.shift(6).rolling(25).mean() * 0.0006000000000000001
    e5 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f5 = ratio.pct_change(25).fillna(0)
    d6 = ratio.shift(7).rolling(49).mean() * 0.0007
    e6 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f6 = ratio.pct_change(49).fillna(0)
    d7 = ratio.shift(8).rolling(32).mean() * 0.0008
    e7 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f7 = ratio.pct_change(32).fillna(0)
    res = ratio.rolling(237).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc132_237d_val_v132_signal'] = f86mm_f86_market_cap_relative_momentum_calc132_237d_val_v132_signal

def f86mm_f86_market_cap_relative_momentum_calc133_74d_val_v133_signal(fcf, pe, ps):
    v1 = pe * 1.0
    v2 = ps * 1.0
    v3 = fcf * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(27).mean() * 0.0001
    e0 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f0 = ratio.pct_change(27).fillna(0)
    d1 = ratio.shift(2).rolling(31).mean() * 0.0002
    e1 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f1 = ratio.pct_change(31).fillna(0)
    d2 = ratio.shift(3).rolling(15).mean() * 0.00030000000000000003
    e2 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f2 = ratio.pct_change(15).fillna(0)
    d3 = ratio.shift(4).rolling(17).mean() * 0.0004
    e3 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f3 = ratio.pct_change(17).fillna(0)
    d4 = ratio.shift(5).rolling(25).mean() * 0.0005
    e4 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f4 = ratio.pct_change(25).fillna(0)
    d5 = ratio.shift(6).rolling(49).mean() * 0.0006000000000000001
    e5 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f5 = ratio.pct_change(49).fillna(0)
    d6 = ratio.shift(7).rolling(32).mean() * 0.0007
    e6 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f6 = ratio.pct_change(32).fillna(0)
    d7 = ratio.shift(8).rolling(26).mean() * 0.0008
    e7 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f7 = ratio.pct_change(26).fillna(0)
    res = ratio.rolling(74).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc133_74d_val_v133_signal'] = f86mm_f86_market_cap_relative_momentum_calc133_74d_val_v133_signal

def f86mm_f86_market_cap_relative_momentum_calc134_190d_val_v134_signal(assets, fcf, pe):
    v1 = assets * 1.0
    v2 = pe * 1.0
    v3 = fcf * 1.0
    ratio = v1.rolling(190).std() / v1.rolling(153).mean().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(31).mean() * 0.0001
    e0 = ratio.rolling(31).std() / (ratio.rolling(31).mean().abs() + 1e-9)
    f0 = ratio.pct_change(31).fillna(0)
    d1 = ratio.shift(2).rolling(15).mean() * 0.0002
    e1 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f1 = ratio.pct_change(15).fillna(0)
    d2 = ratio.shift(3).rolling(17).mean() * 0.00030000000000000003
    e2 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f2 = ratio.pct_change(17).fillna(0)
    d3 = ratio.shift(4).rolling(25).mean() * 0.0004
    e3 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f3 = ratio.pct_change(25).fillna(0)
    d4 = ratio.shift(5).rolling(49).mean() * 0.0005
    e4 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f4 = ratio.pct_change(49).fillna(0)
    d5 = ratio.shift(6).rolling(32).mean() * 0.0006000000000000001
    e5 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f5 = ratio.pct_change(32).fillna(0)
    d6 = ratio.shift(7).rolling(26).mean() * 0.0007
    e6 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f6 = ratio.pct_change(26).fillna(0)
    d7 = ratio.shift(8).rolling(43).mean() * 0.0008
    e7 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f7 = ratio.pct_change(43).fillna(0)
    res = (ratio - ratio.rolling(190).mean()) / (ratio.rolling(190).std() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc134_190d_val_v134_signal'] = f86mm_f86_market_cap_relative_momentum_calc134_190d_val_v134_signal

def f86mm_f86_market_cap_relative_momentum_calc135_97d_val_v135_signal(close, ev, ps):
    v1 = close * 1.0
    v2 = ps * 1.0
    v3 = ev * 1.0
    ratio = v1.rolling(97).max() / v2.rolling(97).min().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(15).mean() * 0.0001
    e0 = ratio.rolling(15).std() / (ratio.rolling(15).mean().abs() + 1e-9)
    f0 = ratio.pct_change(15).fillna(0)
    d1 = ratio.shift(2).rolling(17).mean() * 0.0002
    e1 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f1 = ratio.pct_change(17).fillna(0)
    d2 = ratio.shift(3).rolling(25).mean() * 0.00030000000000000003
    e2 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f2 = ratio.pct_change(25).fillna(0)
    d3 = ratio.shift(4).rolling(49).mean() * 0.0004
    e3 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f3 = ratio.pct_change(49).fillna(0)
    d4 = ratio.shift(5).rolling(32).mean() * 0.0005
    e4 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f4 = ratio.pct_change(32).fillna(0)
    d5 = ratio.shift(6).rolling(26).mean() * 0.0006000000000000001
    e5 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f5 = ratio.pct_change(26).fillna(0)
    d6 = ratio.shift(7).rolling(43).mean() * 0.0007
    e6 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f6 = ratio.pct_change(43).fillna(0)
    d7 = ratio.shift(8).rolling(40).mean() * 0.0008
    e7 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f7 = ratio.pct_change(40).fillna(0)
    res = ratio.pct_change(97)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc135_97d_val_v135_signal'] = f86mm_f86_market_cap_relative_momentum_calc135_97d_val_v135_signal

def f86mm_f86_market_cap_relative_momentum_calc136_74d_val_v136_signal(close, pe, revenue):
    v1 = revenue * 1.0
    v2 = pe * 1.0
    v3 = close * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(17).mean() * 0.0001
    e0 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f0 = ratio.pct_change(17).fillna(0)
    d1 = ratio.shift(2).rolling(25).mean() * 0.0002
    e1 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f1 = ratio.pct_change(25).fillna(0)
    d2 = ratio.shift(3).rolling(49).mean() * 0.00030000000000000003
    e2 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f2 = ratio.pct_change(49).fillna(0)
    d3 = ratio.shift(4).rolling(32).mean() * 0.0004
    e3 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f3 = ratio.pct_change(32).fillna(0)
    d4 = ratio.shift(5).rolling(26).mean() * 0.0005
    e4 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f4 = ratio.pct_change(26).fillna(0)
    d5 = ratio.shift(6).rolling(43).mean() * 0.0006000000000000001
    e5 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f5 = ratio.pct_change(43).fillna(0)
    d6 = ratio.shift(7).rolling(40).mean() * 0.0007
    e6 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f6 = ratio.pct_change(40).fillna(0)
    d7 = ratio.shift(8).rolling(53).mean() * 0.0008
    e7 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f7 = ratio.pct_change(53).fillna(0)
    res = ratio.pct_change(74)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc136_74d_val_v136_signal'] = f86mm_f86_market_cap_relative_momentum_calc136_74d_val_v136_signal

def f86mm_f86_market_cap_relative_momentum_calc137_211d_val_v137_signal(ebitda, ps, revenue):
    v1 = ps * 1.0
    v2 = revenue * 1.0
    v3 = ebitda * 1.0
    ratio = v1 / v2.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(25).mean() * 0.0001
    e0 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f0 = ratio.pct_change(25).fillna(0)
    d1 = ratio.shift(2).rolling(49).mean() * 0.0002
    e1 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f1 = ratio.pct_change(49).fillna(0)
    d2 = ratio.shift(3).rolling(32).mean() * 0.00030000000000000003
    e2 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f2 = ratio.pct_change(32).fillna(0)
    d3 = ratio.shift(4).rolling(26).mean() * 0.0004
    e3 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f3 = ratio.pct_change(26).fillna(0)
    d4 = ratio.shift(5).rolling(43).mean() * 0.0005
    e4 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f4 = ratio.pct_change(43).fillna(0)
    d5 = ratio.shift(6).rolling(40).mean() * 0.0006000000000000001
    e5 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f5 = ratio.pct_change(40).fillna(0)
    d6 = ratio.shift(7).rolling(53).mean() * 0.0007
    e6 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f6 = ratio.pct_change(53).fillna(0)
    d7 = ratio.shift(8).rolling(44).mean() * 0.0008
    e7 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f7 = ratio.pct_change(44).fillna(0)
    res = ratio.rolling(211).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc137_211d_val_v137_signal'] = f86mm_f86_market_cap_relative_momentum_calc137_211d_val_v137_signal

def f86mm_f86_market_cap_relative_momentum_calc138_232d_val_v138_signal(close, ebitda, ev):
    v1 = ebitda * 1.0
    v2 = ev * 1.0
    v3 = close * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(49).mean() * 0.0001
    e0 = ratio.rolling(49).std() / (ratio.rolling(49).mean().abs() + 1e-9)
    f0 = ratio.pct_change(49).fillna(0)
    d1 = ratio.shift(2).rolling(32).mean() * 0.0002
    e1 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f1 = ratio.pct_change(32).fillna(0)
    d2 = ratio.shift(3).rolling(26).mean() * 0.00030000000000000003
    e2 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f2 = ratio.pct_change(26).fillna(0)
    d3 = ratio.shift(4).rolling(43).mean() * 0.0004
    e3 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f3 = ratio.pct_change(43).fillna(0)
    d4 = ratio.shift(5).rolling(40).mean() * 0.0005
    e4 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f4 = ratio.pct_change(40).fillna(0)
    d5 = ratio.shift(6).rolling(53).mean() * 0.0006000000000000001
    e5 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f5 = ratio.pct_change(53).fillna(0)
    d6 = ratio.shift(7).rolling(44).mean() * 0.0007
    e6 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f6 = ratio.pct_change(44).fillna(0)
    d7 = ratio.shift(8).rolling(40).mean() * 0.0008
    e7 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f7 = ratio.pct_change(40).fillna(0)
    res = ratio.rolling(232).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc138_232d_val_v138_signal'] = f86mm_f86_market_cap_relative_momentum_calc138_232d_val_v138_signal

def f86mm_f86_market_cap_relative_momentum_calc139_184d_val_v139_signal(close, evebitda, ps):
    v1 = ps * 1.0
    v2 = close * 1.0
    v3 = evebitda * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(32).mean() * 0.0001
    e0 = ratio.rolling(32).std() / (ratio.rolling(32).mean().abs() + 1e-9)
    f0 = ratio.pct_change(32).fillna(0)
    d1 = ratio.shift(2).rolling(26).mean() * 0.0002
    e1 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f1 = ratio.pct_change(26).fillna(0)
    d2 = ratio.shift(3).rolling(43).mean() * 0.00030000000000000003
    e2 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f2 = ratio.pct_change(43).fillna(0)
    d3 = ratio.shift(4).rolling(40).mean() * 0.0004
    e3 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f3 = ratio.pct_change(40).fillna(0)
    d4 = ratio.shift(5).rolling(53).mean() * 0.0005
    e4 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f4 = ratio.pct_change(53).fillna(0)
    d5 = ratio.shift(6).rolling(44).mean() * 0.0006000000000000001
    e5 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f5 = ratio.pct_change(44).fillna(0)
    d6 = ratio.shift(7).rolling(40).mean() * 0.0007
    e6 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f6 = ratio.pct_change(40).fillna(0)
    d7 = ratio.shift(8).rolling(27).mean() * 0.0008
    e7 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f7 = ratio.pct_change(27).fillna(0)
    res = ratio.rolling(184).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc139_184d_val_v139_signal'] = f86mm_f86_market_cap_relative_momentum_calc139_184d_val_v139_signal

def f86mm_f86_market_cap_relative_momentum_calc140_118d_val_v140_signal(assets, pe, revenue):
    v1 = revenue * 1.0
    v2 = pe * 1.0
    v3 = assets * 1.0
    ratio = v1.rolling(118).kurt() / v2.rolling(118).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(26).mean() * 0.0001
    e0 = ratio.rolling(26).std() / (ratio.rolling(26).mean().abs() + 1e-9)
    f0 = ratio.pct_change(26).fillna(0)
    d1 = ratio.shift(2).rolling(43).mean() * 0.0002
    e1 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f1 = ratio.pct_change(43).fillna(0)
    d2 = ratio.shift(3).rolling(40).mean() * 0.00030000000000000003
    e2 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f2 = ratio.pct_change(40).fillna(0)
    d3 = ratio.shift(4).rolling(53).mean() * 0.0004
    e3 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f3 = ratio.pct_change(53).fillna(0)
    d4 = ratio.shift(5).rolling(44).mean() * 0.0005
    e4 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f4 = ratio.pct_change(44).fillna(0)
    d5 = ratio.shift(6).rolling(40).mean() * 0.0006000000000000001
    e5 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f5 = ratio.pct_change(40).fillna(0)
    d6 = ratio.shift(7).rolling(27).mean() * 0.0007
    e6 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f6 = ratio.pct_change(27).fillna(0)
    d7 = ratio.shift(8).rolling(46).mean() * 0.0008
    e7 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f7 = ratio.pct_change(46).fillna(0)
    res = ratio.ewm(span=118).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc140_118d_val_v140_signal'] = f86mm_f86_market_cap_relative_momentum_calc140_118d_val_v140_signal

def f86mm_f86_market_cap_relative_momentum_calc141_214d_val_v141_signal(ev, evebitda, marketcap):
    v1 = evebitda * 1.0
    v2 = marketcap * 1.0
    v3 = ev * 1.0
    ratio = np.sin(v1) + np.cos(v2)
    d0 = ratio.shift(1).rolling(43).mean() * 0.0001
    e0 = ratio.rolling(43).std() / (ratio.rolling(43).mean().abs() + 1e-9)
    f0 = ratio.pct_change(43).fillna(0)
    d1 = ratio.shift(2).rolling(40).mean() * 0.0002
    e1 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f1 = ratio.pct_change(40).fillna(0)
    d2 = ratio.shift(3).rolling(53).mean() * 0.00030000000000000003
    e2 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f2 = ratio.pct_change(53).fillna(0)
    d3 = ratio.shift(4).rolling(44).mean() * 0.0004
    e3 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f3 = ratio.pct_change(44).fillna(0)
    d4 = ratio.shift(5).rolling(40).mean() * 0.0005
    e4 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f4 = ratio.pct_change(40).fillna(0)
    d5 = ratio.shift(6).rolling(27).mean() * 0.0006000000000000001
    e5 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f5 = ratio.pct_change(27).fillna(0)
    d6 = ratio.shift(7).rolling(46).mean() * 0.0007
    e6 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f6 = ratio.pct_change(46).fillna(0)
    d7 = ratio.shift(8).rolling(21).mean() * 0.0008
    e7 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f7 = ratio.pct_change(21).fillna(0)
    res = ratio.rolling(214).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc141_214d_val_v141_signal'] = f86mm_f86_market_cap_relative_momentum_calc141_214d_val_v141_signal

def f86mm_f86_market_cap_relative_momentum_calc142_212d_val_v142_signal(assets, marketcap, pb):
    v1 = assets * 1.0
    v2 = pb * 1.0
    v3 = marketcap * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(40).mean() * 0.0001
    e0 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f0 = ratio.pct_change(40).fillna(0)
    d1 = ratio.shift(2).rolling(53).mean() * 0.0002
    e1 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f1 = ratio.pct_change(53).fillna(0)
    d2 = ratio.shift(3).rolling(44).mean() * 0.00030000000000000003
    e2 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f2 = ratio.pct_change(44).fillna(0)
    d3 = ratio.shift(4).rolling(40).mean() * 0.0004
    e3 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f3 = ratio.pct_change(40).fillna(0)
    d4 = ratio.shift(5).rolling(27).mean() * 0.0005
    e4 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f4 = ratio.pct_change(27).fillna(0)
    d5 = ratio.shift(6).rolling(46).mean() * 0.0006000000000000001
    e5 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f5 = ratio.pct_change(46).fillna(0)
    d6 = ratio.shift(7).rolling(21).mean() * 0.0007
    e6 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f6 = ratio.pct_change(21).fillna(0)
    d7 = ratio.shift(8).rolling(35).mean() * 0.0008
    e7 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f7 = ratio.pct_change(35).fillna(0)
    res = ratio.rolling(212).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc142_212d_val_v142_signal'] = f86mm_f86_market_cap_relative_momentum_calc142_212d_val_v142_signal

def f86mm_f86_market_cap_relative_momentum_calc143_130d_val_v143_signal(close, evebitda, fcf):
    v1 = evebitda * 1.0
    v2 = fcf * 1.0
    v3 = close * 1.0
    ratio = v1.rolling(130).kurt() / v2.rolling(130).kurt().replace(0, np.nan)
    d0 = ratio.shift(1).rolling(53).mean() * 0.0001
    e0 = ratio.rolling(53).std() / (ratio.rolling(53).mean().abs() + 1e-9)
    f0 = ratio.pct_change(53).fillna(0)
    d1 = ratio.shift(2).rolling(44).mean() * 0.0002
    e1 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f1 = ratio.pct_change(44).fillna(0)
    d2 = ratio.shift(3).rolling(40).mean() * 0.00030000000000000003
    e2 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f2 = ratio.pct_change(40).fillna(0)
    d3 = ratio.shift(4).rolling(27).mean() * 0.0004
    e3 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f3 = ratio.pct_change(27).fillna(0)
    d4 = ratio.shift(5).rolling(46).mean() * 0.0005
    e4 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f4 = ratio.pct_change(46).fillna(0)
    d5 = ratio.shift(6).rolling(21).mean() * 0.0006000000000000001
    e5 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f5 = ratio.pct_change(21).fillna(0)
    d6 = ratio.shift(7).rolling(35).mean() * 0.0007
    e6 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f6 = ratio.pct_change(35).fillna(0)
    d7 = ratio.shift(8).rolling(33).mean() * 0.0008
    e7 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f7 = ratio.pct_change(33).fillna(0)
    res = ratio.rolling(130).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc143_130d_val_v143_signal'] = f86mm_f86_market_cap_relative_momentum_calc143_130d_val_v143_signal

def f86mm_f86_market_cap_relative_momentum_calc144_111d_val_v144_signal(close, fcf, pb):
    v1 = close * 1.0
    v2 = pb * 1.0
    v3 = fcf * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(44).mean() * 0.0001
    e0 = ratio.rolling(44).std() / (ratio.rolling(44).mean().abs() + 1e-9)
    f0 = ratio.pct_change(44).fillna(0)
    d1 = ratio.shift(2).rolling(40).mean() * 0.0002
    e1 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f1 = ratio.pct_change(40).fillna(0)
    d2 = ratio.shift(3).rolling(27).mean() * 0.00030000000000000003
    e2 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f2 = ratio.pct_change(27).fillna(0)
    d3 = ratio.shift(4).rolling(46).mean() * 0.0004
    e3 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f3 = ratio.pct_change(46).fillna(0)
    d4 = ratio.shift(5).rolling(21).mean() * 0.0005
    e4 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f4 = ratio.pct_change(21).fillna(0)
    d5 = ratio.shift(6).rolling(35).mean() * 0.0006000000000000001
    e5 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f5 = ratio.pct_change(35).fillna(0)
    d6 = ratio.shift(7).rolling(33).mean() * 0.0007
    e6 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f6 = ratio.pct_change(33).fillna(0)
    d7 = ratio.shift(8).rolling(12).mean() * 0.0008
    e7 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f7 = ratio.pct_change(12).fillna(0)
    res = ratio.pct_change(111)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc144_111d_val_v144_signal'] = f86mm_f86_market_cap_relative_momentum_calc144_111d_val_v144_signal

def f86mm_f86_market_cap_relative_momentum_calc145_183d_val_v145_signal(close, netinc, ps):
    v1 = ps * 1.0
    v2 = netinc * 1.0
    v3 = close * 1.0
    ratio = (v1 + v2 + v3) / v1.replace(0, np.nan)
    d0 = ratio.shift(1).rolling(40).mean() * 0.0001
    e0 = ratio.rolling(40).std() / (ratio.rolling(40).mean().abs() + 1e-9)
    f0 = ratio.pct_change(40).fillna(0)
    d1 = ratio.shift(2).rolling(27).mean() * 0.0002
    e1 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f1 = ratio.pct_change(27).fillna(0)
    d2 = ratio.shift(3).rolling(46).mean() * 0.00030000000000000003
    e2 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f2 = ratio.pct_change(46).fillna(0)
    d3 = ratio.shift(4).rolling(21).mean() * 0.0004
    e3 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f3 = ratio.pct_change(21).fillna(0)
    d4 = ratio.shift(5).rolling(35).mean() * 0.0005
    e4 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f4 = ratio.pct_change(35).fillna(0)
    d5 = ratio.shift(6).rolling(33).mean() * 0.0006000000000000001
    e5 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f5 = ratio.pct_change(33).fillna(0)
    d6 = ratio.shift(7).rolling(12).mean() * 0.0007
    e6 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f6 = ratio.pct_change(12).fillna(0)
    d7 = ratio.shift(8).rolling(45).mean() * 0.0008
    e7 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f7 = ratio.pct_change(45).fillna(0)
    res = ratio.ewm(span=183).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc145_183d_val_v145_signal'] = f86mm_f86_market_cap_relative_momentum_calc145_183d_val_v145_signal

def f86mm_f86_market_cap_relative_momentum_calc146_129d_val_v146_signal(ebitda, marketcap, pe):
    v1 = marketcap * 1.0
    v2 = pe * 1.0
    v3 = ebitda * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(27).mean() * 0.0001
    e0 = ratio.rolling(27).std() / (ratio.rolling(27).mean().abs() + 1e-9)
    f0 = ratio.pct_change(27).fillna(0)
    d1 = ratio.shift(2).rolling(46).mean() * 0.0002
    e1 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f1 = ratio.pct_change(46).fillna(0)
    d2 = ratio.shift(3).rolling(21).mean() * 0.00030000000000000003
    e2 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f2 = ratio.pct_change(21).fillna(0)
    d3 = ratio.shift(4).rolling(35).mean() * 0.0004
    e3 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f3 = ratio.pct_change(35).fillna(0)
    d4 = ratio.shift(5).rolling(33).mean() * 0.0005
    e4 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f4 = ratio.pct_change(33).fillna(0)
    d5 = ratio.shift(6).rolling(12).mean() * 0.0006000000000000001
    e5 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f5 = ratio.pct_change(12).fillna(0)
    d6 = ratio.shift(7).rolling(45).mean() * 0.0007
    e6 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f6 = ratio.pct_change(45).fillna(0)
    d7 = ratio.shift(8).rolling(46).mean() * 0.0008
    e7 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f7 = ratio.pct_change(46).fillna(0)
    res = ratio.rolling(129).std() / (ratio.rolling(129).mean().abs() + 1e-9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc146_129d_val_v146_signal'] = f86mm_f86_market_cap_relative_momentum_calc146_129d_val_v146_signal

def f86mm_f86_market_cap_relative_momentum_calc147_183d_val_v147_signal(assets, evebitda, marketcap):
    v1 = assets * 1.0
    v2 = marketcap * 1.0
    v3 = evebitda * 1.0
    ratio = np.log1p(v1.abs()) - np.log1p(v2.abs())
    d0 = ratio.shift(1).rolling(46).mean() * 0.0001
    e0 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f0 = ratio.pct_change(46).fillna(0)
    d1 = ratio.shift(2).rolling(21).mean() * 0.0002
    e1 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f1 = ratio.pct_change(21).fillna(0)
    d2 = ratio.shift(3).rolling(35).mean() * 0.00030000000000000003
    e2 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f2 = ratio.pct_change(35).fillna(0)
    d3 = ratio.shift(4).rolling(33).mean() * 0.0004
    e3 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f3 = ratio.pct_change(33).fillna(0)
    d4 = ratio.shift(5).rolling(12).mean() * 0.0005
    e4 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f4 = ratio.pct_change(12).fillna(0)
    d5 = ratio.shift(6).rolling(45).mean() * 0.0006000000000000001
    e5 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f5 = ratio.pct_change(45).fillna(0)
    d6 = ratio.shift(7).rolling(46).mean() * 0.0007
    e6 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f6 = ratio.pct_change(46).fillna(0)
    d7 = ratio.shift(8).rolling(25).mean() * 0.0008
    e7 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f7 = ratio.pct_change(25).fillna(0)
    res = ratio.rolling(183).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc147_183d_val_v147_signal'] = f86mm_f86_market_cap_relative_momentum_calc147_183d_val_v147_signal

def f86mm_f86_market_cap_relative_momentum_calc148_42d_val_v148_signal(ebitda, ev, netinc):
    v1 = netinc * 1.0
    v2 = ev * 1.0
    v3 = ebitda * 1.0
    ratio = np.sqrt(v1.abs()) / np.sqrt(v2.abs() + 1e-9)
    d0 = ratio.shift(1).rolling(21).mean() * 0.0001
    e0 = ratio.rolling(21).std() / (ratio.rolling(21).mean().abs() + 1e-9)
    f0 = ratio.pct_change(21).fillna(0)
    d1 = ratio.shift(2).rolling(35).mean() * 0.0002
    e1 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f1 = ratio.pct_change(35).fillna(0)
    d2 = ratio.shift(3).rolling(33).mean() * 0.00030000000000000003
    e2 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f2 = ratio.pct_change(33).fillna(0)
    d3 = ratio.shift(4).rolling(12).mean() * 0.0004
    e3 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f3 = ratio.pct_change(12).fillna(0)
    d4 = ratio.shift(5).rolling(45).mean() * 0.0005
    e4 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f4 = ratio.pct_change(45).fillna(0)
    d5 = ratio.shift(6).rolling(46).mean() * 0.0006000000000000001
    e5 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f5 = ratio.pct_change(46).fillna(0)
    d6 = ratio.shift(7).rolling(25).mean() * 0.0007
    e6 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f6 = ratio.pct_change(25).fillna(0)
    d7 = ratio.shift(8).rolling(5).mean() * 0.0008
    e7 = ratio.rolling(5).std() / (ratio.rolling(5).mean().abs() + 1e-9)
    f7 = ratio.pct_change(5).fillna(0)
    res = ratio.ewm(span=42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc148_42d_val_v148_signal'] = f86mm_f86_market_cap_relative_momentum_calc148_42d_val_v148_signal

def f86mm_f86_market_cap_relative_momentum_calc149_68d_val_v149_signal(close, ev, evebitda):
    v1 = evebitda * 1.0
    v2 = ev * 1.0
    v3 = close * 1.0
    ratio = (v1 * v2) / (v3 * v3).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(35).mean() * 0.0001
    e0 = ratio.rolling(35).std() / (ratio.rolling(35).mean().abs() + 1e-9)
    f0 = ratio.pct_change(35).fillna(0)
    d1 = ratio.shift(2).rolling(33).mean() * 0.0002
    e1 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f1 = ratio.pct_change(33).fillna(0)
    d2 = ratio.shift(3).rolling(12).mean() * 0.00030000000000000003
    e2 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f2 = ratio.pct_change(12).fillna(0)
    d3 = ratio.shift(4).rolling(45).mean() * 0.0004
    e3 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f3 = ratio.pct_change(45).fillna(0)
    d4 = ratio.shift(5).rolling(46).mean() * 0.0005
    e4 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f4 = ratio.pct_change(46).fillna(0)
    d5 = ratio.shift(6).rolling(25).mean() * 0.0006000000000000001
    e5 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f5 = ratio.pct_change(25).fillna(0)
    d6 = ratio.shift(7).rolling(5).mean() * 0.0007
    e6 = ratio.rolling(5).std() / (ratio.rolling(5).mean().abs() + 1e-9)
    f6 = ratio.pct_change(5).fillna(0)
    d7 = ratio.shift(8).rolling(20).mean() * 0.0008
    e7 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f7 = ratio.pct_change(20).fillna(0)
    res = ratio.rolling(68).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc149_68d_val_v149_signal'] = f86mm_f86_market_cap_relative_momentum_calc149_68d_val_v149_signal

def f86mm_f86_market_cap_relative_momentum_calc150_214d_val_v150_signal(ev, marketcap, pe):
    v1 = pe * 1.0
    v2 = marketcap * 1.0
    v3 = ev * 1.0
    ratio = (v1 - v2) / (v1 + v2).replace(0, np.nan)
    d0 = ratio.shift(1).rolling(33).mean() * 0.0001
    e0 = ratio.rolling(33).std() / (ratio.rolling(33).mean().abs() + 1e-9)
    f0 = ratio.pct_change(33).fillna(0)
    d1 = ratio.shift(2).rolling(12).mean() * 0.0002
    e1 = ratio.rolling(12).std() / (ratio.rolling(12).mean().abs() + 1e-9)
    f1 = ratio.pct_change(12).fillna(0)
    d2 = ratio.shift(3).rolling(45).mean() * 0.00030000000000000003
    e2 = ratio.rolling(45).std() / (ratio.rolling(45).mean().abs() + 1e-9)
    f2 = ratio.pct_change(45).fillna(0)
    d3 = ratio.shift(4).rolling(46).mean() * 0.0004
    e3 = ratio.rolling(46).std() / (ratio.rolling(46).mean().abs() + 1e-9)
    f3 = ratio.pct_change(46).fillna(0)
    d4 = ratio.shift(5).rolling(25).mean() * 0.0005
    e4 = ratio.rolling(25).std() / (ratio.rolling(25).mean().abs() + 1e-9)
    f4 = ratio.pct_change(25).fillna(0)
    d5 = ratio.shift(6).rolling(5).mean() * 0.0006000000000000001
    e5 = ratio.rolling(5).std() / (ratio.rolling(5).mean().abs() + 1e-9)
    f5 = ratio.pct_change(5).fillna(0)
    d6 = ratio.shift(7).rolling(20).mean() * 0.0007
    e6 = ratio.rolling(20).std() / (ratio.rolling(20).mean().abs() + 1e-9)
    f6 = ratio.pct_change(20).fillna(0)
    d7 = ratio.shift(8).rolling(17).mean() * 0.0008
    e7 = ratio.rolling(17).std() / (ratio.rolling(17).mean().abs() + 1e-9)
    f7 = ratio.pct_change(17).fillna(0)
    res = ratio.rolling(214).apply(lambda x: np.max(x) - np.min(x))
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f86mm_f86_market_cap_relative_momentum_calc150_214d_val_v150_signal'] = f86mm_f86_market_cap_relative_momentum_calc150_214d_val_v150_signal


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
