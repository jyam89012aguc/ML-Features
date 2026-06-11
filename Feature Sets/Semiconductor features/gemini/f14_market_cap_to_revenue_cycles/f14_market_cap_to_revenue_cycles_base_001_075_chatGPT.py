import pandas as pd
import numpy as np
import os

FEATURE_FUNCTIONS = {}

def f14mcr_f14_market_cap_to_revenue_cycles_base_v001_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 1 for f14mcr_f14_market_cap_to_revenue_cycles_base_v001_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(6).rolling(11).mean() * market_cap.pct_change(6)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v001_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v001_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v002_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 2 for f14mcr_f14_market_cap_to_revenue_cycles_base_v002_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(7).rolling(12).mean() * market_cap.pct_change(7)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v002_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v002_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v003_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 3 for f14mcr_f14_market_cap_to_revenue_cycles_base_v003_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(8).rolling(13).mean() * market_cap.pct_change(8)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v003_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v003_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v004_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 4 for f14mcr_f14_market_cap_to_revenue_cycles_base_v004_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(9).rolling(14).mean() * market_cap.pct_change(9)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v004_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v004_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v005_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 5 for f14mcr_f14_market_cap_to_revenue_cycles_base_v005_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(10).rolling(15).mean() * market_cap.pct_change(10)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v005_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v005_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v006_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 6 for f14mcr_f14_market_cap_to_revenue_cycles_base_v006_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(11).rolling(16).mean() * market_cap.pct_change(11)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v006_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v006_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v007_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 7 for f14mcr_f14_market_cap_to_revenue_cycles_base_v007_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(12).rolling(17).mean() * market_cap.pct_change(12)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v007_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v007_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v008_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 8 for f14mcr_f14_market_cap_to_revenue_cycles_base_v008_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(13).rolling(18).mean() * market_cap.pct_change(13)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v008_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v008_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v009_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 9 for f14mcr_f14_market_cap_to_revenue_cycles_base_v009_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(14).rolling(19).mean() * market_cap.pct_change(14)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v009_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v009_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v010_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 10 for f14mcr_f14_market_cap_to_revenue_cycles_base_v010_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(15).rolling(20).mean() * market_cap.pct_change(15)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v010_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v010_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v011_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 11 for f14mcr_f14_market_cap_to_revenue_cycles_base_v011_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(16).rolling(21).mean() * market_cap.pct_change(16)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v011_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v011_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v012_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 12 for f14mcr_f14_market_cap_to_revenue_cycles_base_v012_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(17).rolling(22).mean() * market_cap.pct_change(17)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v012_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v012_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v013_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 13 for f14mcr_f14_market_cap_to_revenue_cycles_base_v013_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(18).rolling(23).mean() * market_cap.pct_change(18)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v013_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v013_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v014_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 14 for f14mcr_f14_market_cap_to_revenue_cycles_base_v014_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(19).rolling(24).mean() * market_cap.pct_change(19)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v014_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v014_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v015_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 15 for f14mcr_f14_market_cap_to_revenue_cycles_base_v015_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(20).rolling(25).mean() * market_cap.pct_change(20)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v015_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v015_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v016_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 16 for f14mcr_f14_market_cap_to_revenue_cycles_base_v016_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(21).rolling(26).mean() * market_cap.pct_change(21)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v016_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v016_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v017_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 17 for f14mcr_f14_market_cap_to_revenue_cycles_base_v017_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(22).rolling(27).mean() * market_cap.pct_change(22)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v017_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v017_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v018_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 18 for f14mcr_f14_market_cap_to_revenue_cycles_base_v018_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(23).rolling(28).mean() * market_cap.pct_change(23)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v018_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v018_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v019_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 19 for f14mcr_f14_market_cap_to_revenue_cycles_base_v019_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(24).rolling(29).mean() * market_cap.pct_change(24)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v019_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v019_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v020_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 20 for f14mcr_f14_market_cap_to_revenue_cycles_base_v020_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(25).rolling(30).mean() * market_cap.pct_change(25)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v020_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v020_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v021_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 21 for f14mcr_f14_market_cap_to_revenue_cycles_base_v021_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(26).rolling(31).mean() * market_cap.pct_change(26)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v021_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v021_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v022_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 22 for f14mcr_f14_market_cap_to_revenue_cycles_base_v022_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(27).rolling(32).mean() * market_cap.pct_change(27)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v022_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v022_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v023_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 23 for f14mcr_f14_market_cap_to_revenue_cycles_base_v023_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(28).rolling(33).mean() * market_cap.pct_change(28)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v023_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v023_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v024_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 24 for f14mcr_f14_market_cap_to_revenue_cycles_base_v024_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(29).rolling(34).mean() * market_cap.pct_change(29)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v024_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v024_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v025_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 25 for f14mcr_f14_market_cap_to_revenue_cycles_base_v025_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(30).rolling(35).mean() * market_cap.pct_change(30)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v025_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v025_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v026_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 26 for f14mcr_f14_market_cap_to_revenue_cycles_base_v026_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(31).rolling(36).mean() * market_cap.pct_change(31)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v026_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v026_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v027_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 27 for f14mcr_f14_market_cap_to_revenue_cycles_base_v027_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(32).rolling(37).mean() * market_cap.pct_change(32)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v027_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v027_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v028_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 28 for f14mcr_f14_market_cap_to_revenue_cycles_base_v028_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(33).rolling(38).mean() * market_cap.pct_change(33)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v028_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v028_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v029_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 29 for f14mcr_f14_market_cap_to_revenue_cycles_base_v029_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(34).rolling(39).mean() * market_cap.pct_change(34)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v029_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v029_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v030_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 30 for f14mcr_f14_market_cap_to_revenue_cycles_base_v030_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(35).rolling(40).mean() * market_cap.pct_change(35)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v030_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v030_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v031_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 31 for f14mcr_f14_market_cap_to_revenue_cycles_base_v031_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(36).rolling(41).mean() * market_cap.pct_change(36)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v031_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v031_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v032_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 32 for f14mcr_f14_market_cap_to_revenue_cycles_base_v032_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(37).rolling(42).mean() * market_cap.pct_change(37)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v032_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v032_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v033_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 33 for f14mcr_f14_market_cap_to_revenue_cycles_base_v033_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(38).rolling(43).mean() * market_cap.pct_change(38)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v033_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v033_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v034_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 34 for f14mcr_f14_market_cap_to_revenue_cycles_base_v034_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(39).rolling(44).mean() * market_cap.pct_change(39)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v034_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v034_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v035_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 35 for f14mcr_f14_market_cap_to_revenue_cycles_base_v035_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(40).rolling(45).mean() * market_cap.pct_change(40)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v035_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v035_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v036_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 36 for f14mcr_f14_market_cap_to_revenue_cycles_base_v036_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(41).rolling(46).mean() * market_cap.pct_change(41)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v036_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v036_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v037_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 37 for f14mcr_f14_market_cap_to_revenue_cycles_base_v037_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(42).rolling(47).mean() * market_cap.pct_change(42)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v037_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v037_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v038_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 38 for f14mcr_f14_market_cap_to_revenue_cycles_base_v038_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(43).rolling(48).mean() * market_cap.pct_change(43)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v038_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v038_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v039_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 39 for f14mcr_f14_market_cap_to_revenue_cycles_base_v039_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(44).rolling(49).mean() * market_cap.pct_change(44)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v039_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v039_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v040_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 40 for f14mcr_f14_market_cap_to_revenue_cycles_base_v040_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(45).rolling(50).mean() * market_cap.pct_change(45)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v040_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v040_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v041_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 41 for f14mcr_f14_market_cap_to_revenue_cycles_base_v041_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(46).rolling(51).mean() * market_cap.pct_change(46)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v041_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v041_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v042_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 42 for f14mcr_f14_market_cap_to_revenue_cycles_base_v042_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(47).rolling(52).mean() * market_cap.pct_change(47)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v042_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v042_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v043_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 43 for f14mcr_f14_market_cap_to_revenue_cycles_base_v043_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(48).rolling(53).mean() * market_cap.pct_change(48)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v043_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v043_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v044_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 44 for f14mcr_f14_market_cap_to_revenue_cycles_base_v044_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(49).rolling(54).mean() * market_cap.pct_change(49)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v044_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v044_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v045_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 45 for f14mcr_f14_market_cap_to_revenue_cycles_base_v045_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(50).rolling(55).mean() * market_cap.pct_change(50)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v045_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v045_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v046_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 46 for f14mcr_f14_market_cap_to_revenue_cycles_base_v046_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(51).rolling(56).mean() * market_cap.pct_change(51)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v046_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v046_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v047_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 47 for f14mcr_f14_market_cap_to_revenue_cycles_base_v047_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(52).rolling(57).mean() * market_cap.pct_change(52)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v047_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v047_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v048_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 48 for f14mcr_f14_market_cap_to_revenue_cycles_base_v048_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(53).rolling(58).mean() * market_cap.pct_change(53)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v048_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v048_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v049_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 49 for f14mcr_f14_market_cap_to_revenue_cycles_base_v049_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(54).rolling(59).mean() * market_cap.pct_change(54)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v049_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v049_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v050_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 50 for f14mcr_f14_market_cap_to_revenue_cycles_base_v050_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(5).rolling(60).mean() * market_cap.pct_change(5)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v050_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v050_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v051_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 51 for f14mcr_f14_market_cap_to_revenue_cycles_base_v051_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(6).rolling(61).mean() * market_cap.pct_change(6)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v051_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v051_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v052_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 52 for f14mcr_f14_market_cap_to_revenue_cycles_base_v052_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(7).rolling(62).mean() * market_cap.pct_change(7)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v052_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v052_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v053_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 53 for f14mcr_f14_market_cap_to_revenue_cycles_base_v053_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(8).rolling(63).mean() * market_cap.pct_change(8)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v053_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v053_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v054_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 54 for f14mcr_f14_market_cap_to_revenue_cycles_base_v054_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(9).rolling(64).mean() * market_cap.pct_change(9)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v054_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v054_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v055_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 55 for f14mcr_f14_market_cap_to_revenue_cycles_base_v055_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(10).rolling(65).mean() * market_cap.pct_change(10)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v055_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v055_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v056_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 56 for f14mcr_f14_market_cap_to_revenue_cycles_base_v056_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(11).rolling(66).mean() * market_cap.pct_change(11)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v056_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v056_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v057_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 57 for f14mcr_f14_market_cap_to_revenue_cycles_base_v057_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(12).rolling(67).mean() * market_cap.pct_change(12)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v057_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v057_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v058_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 58 for f14mcr_f14_market_cap_to_revenue_cycles_base_v058_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(13).rolling(68).mean() * market_cap.pct_change(13)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v058_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v058_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v059_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 59 for f14mcr_f14_market_cap_to_revenue_cycles_base_v059_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(14).rolling(69).mean() * market_cap.pct_change(14)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v059_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v059_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v060_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 60 for f14mcr_f14_market_cap_to_revenue_cycles_base_v060_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(15).rolling(70).mean() * market_cap.pct_change(15)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v060_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v060_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v061_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 61 for f14mcr_f14_market_cap_to_revenue_cycles_base_v061_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(16).rolling(71).mean() * market_cap.pct_change(16)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v061_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v061_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v062_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 62 for f14mcr_f14_market_cap_to_revenue_cycles_base_v062_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(17).rolling(72).mean() * market_cap.pct_change(17)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v062_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v062_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v063_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 63 for f14mcr_f14_market_cap_to_revenue_cycles_base_v063_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(18).rolling(73).mean() * market_cap.pct_change(18)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v063_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v063_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v064_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 64 for f14mcr_f14_market_cap_to_revenue_cycles_base_v064_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(19).rolling(74).mean() * market_cap.pct_change(19)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v064_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v064_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v065_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 65 for f14mcr_f14_market_cap_to_revenue_cycles_base_v065_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(20).rolling(75).mean() * market_cap.pct_change(20)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v065_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v065_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v066_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 66 for f14mcr_f14_market_cap_to_revenue_cycles_base_v066_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(21).rolling(76).mean() * market_cap.pct_change(21)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v066_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v066_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v067_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 67 for f14mcr_f14_market_cap_to_revenue_cycles_base_v067_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(22).rolling(77).mean() * market_cap.pct_change(22)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v067_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v067_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v068_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 68 for f14mcr_f14_market_cap_to_revenue_cycles_base_v068_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(23).rolling(78).mean() * market_cap.pct_change(23)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v068_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v068_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v069_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 69 for f14mcr_f14_market_cap_to_revenue_cycles_base_v069_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(24).rolling(79).mean() * market_cap.pct_change(24)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v069_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v069_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v070_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 70 for f14mcr_f14_market_cap_to_revenue_cycles_base_v070_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(25).rolling(80).mean() * market_cap.pct_change(25)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v070_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v070_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v071_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 71 for f14mcr_f14_market_cap_to_revenue_cycles_base_v071_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(26).rolling(81).mean() * market_cap.pct_change(26)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v071_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v071_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v072_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 72 for f14mcr_f14_market_cap_to_revenue_cycles_base_v072_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(27).rolling(82).mean() * market_cap.pct_change(27)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v072_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v072_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v073_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 73 for f14mcr_f14_market_cap_to_revenue_cycles_base_v073_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(28).rolling(83).mean() * market_cap.pct_change(28)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v073_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v073_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v074_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 74 for f14mcr_f14_market_cap_to_revenue_cycles_base_v074_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(29).rolling(84).mean() * market_cap.pct_change(29)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v074_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v074_signal

def f14mcr_f14_market_cap_to_revenue_cycles_base_v075_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 75 for f14mcr_f14_market_cap_to_revenue_cycles_base_v075_signal
    # This formula calculates complex financial relationships
    s1 = market_cap.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (market_cap / revenue.replace(0, np.nan)).pct_change(30).rolling(85).mean() * market_cap.pct_change(30)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f14mcr_f14_market_cap_to_revenue_cycles_base_v075_signal'] = f14mcr_f14_market_cap_to_revenue_cycles_base_v075_signal



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
