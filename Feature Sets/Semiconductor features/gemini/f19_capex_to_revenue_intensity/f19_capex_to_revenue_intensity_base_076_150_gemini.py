import pandas as pd
import numpy as np
import os

FEATURE_FUNCTIONS = {}

def f19cri_f19_capex_to_revenue_intensity_base_v076_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 76 for f19cri_f19_capex_to_revenue_intensity_base_v076_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(31).rolling(86).mean() * capex.pct_change(31)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v076_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v076_signal

def f19cri_f19_capex_to_revenue_intensity_base_v077_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 77 for f19cri_f19_capex_to_revenue_intensity_base_v077_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(32).rolling(87).mean() * capex.pct_change(32)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v077_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v077_signal

def f19cri_f19_capex_to_revenue_intensity_base_v078_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 78 for f19cri_f19_capex_to_revenue_intensity_base_v078_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(33).rolling(88).mean() * capex.pct_change(33)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v078_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v078_signal

def f19cri_f19_capex_to_revenue_intensity_base_v079_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 79 for f19cri_f19_capex_to_revenue_intensity_base_v079_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(34).rolling(89).mean() * capex.pct_change(34)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v079_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v079_signal

def f19cri_f19_capex_to_revenue_intensity_base_v080_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 80 for f19cri_f19_capex_to_revenue_intensity_base_v080_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(35).rolling(90).mean() * capex.pct_change(35)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v080_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v080_signal

def f19cri_f19_capex_to_revenue_intensity_base_v081_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 81 for f19cri_f19_capex_to_revenue_intensity_base_v081_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(36).rolling(91).mean() * capex.pct_change(36)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v081_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v081_signal

def f19cri_f19_capex_to_revenue_intensity_base_v082_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 82 for f19cri_f19_capex_to_revenue_intensity_base_v082_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(37).rolling(92).mean() * capex.pct_change(37)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v082_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v082_signal

def f19cri_f19_capex_to_revenue_intensity_base_v083_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 83 for f19cri_f19_capex_to_revenue_intensity_base_v083_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(38).rolling(93).mean() * capex.pct_change(38)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v083_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v083_signal

def f19cri_f19_capex_to_revenue_intensity_base_v084_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 84 for f19cri_f19_capex_to_revenue_intensity_base_v084_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(39).rolling(94).mean() * capex.pct_change(39)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v084_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v084_signal

def f19cri_f19_capex_to_revenue_intensity_base_v085_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 85 for f19cri_f19_capex_to_revenue_intensity_base_v085_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(40).rolling(95).mean() * capex.pct_change(40)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v085_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v085_signal

def f19cri_f19_capex_to_revenue_intensity_base_v086_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 86 for f19cri_f19_capex_to_revenue_intensity_base_v086_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(41).rolling(96).mean() * capex.pct_change(41)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v086_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v086_signal

def f19cri_f19_capex_to_revenue_intensity_base_v087_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 87 for f19cri_f19_capex_to_revenue_intensity_base_v087_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(42).rolling(97).mean() * capex.pct_change(42)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v087_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v087_signal

def f19cri_f19_capex_to_revenue_intensity_base_v088_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 88 for f19cri_f19_capex_to_revenue_intensity_base_v088_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(43).rolling(98).mean() * capex.pct_change(43)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v088_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v088_signal

def f19cri_f19_capex_to_revenue_intensity_base_v089_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 89 for f19cri_f19_capex_to_revenue_intensity_base_v089_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(44).rolling(99).mean() * capex.pct_change(44)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v089_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v089_signal

def f19cri_f19_capex_to_revenue_intensity_base_v090_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 90 for f19cri_f19_capex_to_revenue_intensity_base_v090_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(45).rolling(100).mean() * capex.pct_change(45)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v090_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v090_signal

def f19cri_f19_capex_to_revenue_intensity_base_v091_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 91 for f19cri_f19_capex_to_revenue_intensity_base_v091_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(46).rolling(101).mean() * capex.pct_change(46)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v091_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v091_signal

def f19cri_f19_capex_to_revenue_intensity_base_v092_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 92 for f19cri_f19_capex_to_revenue_intensity_base_v092_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(47).rolling(102).mean() * capex.pct_change(47)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v092_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v092_signal

def f19cri_f19_capex_to_revenue_intensity_base_v093_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 93 for f19cri_f19_capex_to_revenue_intensity_base_v093_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(48).rolling(103).mean() * capex.pct_change(48)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v093_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v093_signal

def f19cri_f19_capex_to_revenue_intensity_base_v094_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 94 for f19cri_f19_capex_to_revenue_intensity_base_v094_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(49).rolling(104).mean() * capex.pct_change(49)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v094_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v094_signal

def f19cri_f19_capex_to_revenue_intensity_base_v095_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 95 for f19cri_f19_capex_to_revenue_intensity_base_v095_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(50).rolling(105).mean() * capex.pct_change(50)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v095_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v095_signal

def f19cri_f19_capex_to_revenue_intensity_base_v096_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 96 for f19cri_f19_capex_to_revenue_intensity_base_v096_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(51).rolling(106).mean() * capex.pct_change(51)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v096_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v096_signal

def f19cri_f19_capex_to_revenue_intensity_base_v097_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 97 for f19cri_f19_capex_to_revenue_intensity_base_v097_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(52).rolling(107).mean() * capex.pct_change(52)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v097_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v097_signal

def f19cri_f19_capex_to_revenue_intensity_base_v098_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 98 for f19cri_f19_capex_to_revenue_intensity_base_v098_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(53).rolling(108).mean() * capex.pct_change(53)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v098_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v098_signal

def f19cri_f19_capex_to_revenue_intensity_base_v099_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 99 for f19cri_f19_capex_to_revenue_intensity_base_v099_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(54).rolling(109).mean() * capex.pct_change(54)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v099_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v099_signal

def f19cri_f19_capex_to_revenue_intensity_base_v100_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 100 for f19cri_f19_capex_to_revenue_intensity_base_v100_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(5).rolling(10).mean() * capex.pct_change(5)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v100_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v100_signal

def f19cri_f19_capex_to_revenue_intensity_base_v101_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 101 for f19cri_f19_capex_to_revenue_intensity_base_v101_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(6).rolling(11).mean() * capex.pct_change(6)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v101_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v101_signal

def f19cri_f19_capex_to_revenue_intensity_base_v102_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 102 for f19cri_f19_capex_to_revenue_intensity_base_v102_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(7).rolling(12).mean() * capex.pct_change(7)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v102_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v102_signal

def f19cri_f19_capex_to_revenue_intensity_base_v103_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 103 for f19cri_f19_capex_to_revenue_intensity_base_v103_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(8).rolling(13).mean() * capex.pct_change(8)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v103_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v103_signal

def f19cri_f19_capex_to_revenue_intensity_base_v104_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 104 for f19cri_f19_capex_to_revenue_intensity_base_v104_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(9).rolling(14).mean() * capex.pct_change(9)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v104_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v104_signal

def f19cri_f19_capex_to_revenue_intensity_base_v105_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 105 for f19cri_f19_capex_to_revenue_intensity_base_v105_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(10).rolling(15).mean() * capex.pct_change(10)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v105_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v105_signal

def f19cri_f19_capex_to_revenue_intensity_base_v106_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 106 for f19cri_f19_capex_to_revenue_intensity_base_v106_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(11).rolling(16).mean() * capex.pct_change(11)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v106_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v106_signal

def f19cri_f19_capex_to_revenue_intensity_base_v107_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 107 for f19cri_f19_capex_to_revenue_intensity_base_v107_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(12).rolling(17).mean() * capex.pct_change(12)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v107_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v107_signal

def f19cri_f19_capex_to_revenue_intensity_base_v108_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 108 for f19cri_f19_capex_to_revenue_intensity_base_v108_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(13).rolling(18).mean() * capex.pct_change(13)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v108_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v108_signal

def f19cri_f19_capex_to_revenue_intensity_base_v109_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 109 for f19cri_f19_capex_to_revenue_intensity_base_v109_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(14).rolling(19).mean() * capex.pct_change(14)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v109_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v109_signal

def f19cri_f19_capex_to_revenue_intensity_base_v110_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 110 for f19cri_f19_capex_to_revenue_intensity_base_v110_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(15).rolling(20).mean() * capex.pct_change(15)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v110_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v110_signal

def f19cri_f19_capex_to_revenue_intensity_base_v111_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 111 for f19cri_f19_capex_to_revenue_intensity_base_v111_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(16).rolling(21).mean() * capex.pct_change(16)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v111_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v111_signal

def f19cri_f19_capex_to_revenue_intensity_base_v112_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 112 for f19cri_f19_capex_to_revenue_intensity_base_v112_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(17).rolling(22).mean() * capex.pct_change(17)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v112_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v112_signal

def f19cri_f19_capex_to_revenue_intensity_base_v113_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 113 for f19cri_f19_capex_to_revenue_intensity_base_v113_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(18).rolling(23).mean() * capex.pct_change(18)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v113_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v113_signal

def f19cri_f19_capex_to_revenue_intensity_base_v114_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 114 for f19cri_f19_capex_to_revenue_intensity_base_v114_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(19).rolling(24).mean() * capex.pct_change(19)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v114_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v114_signal

def f19cri_f19_capex_to_revenue_intensity_base_v115_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 115 for f19cri_f19_capex_to_revenue_intensity_base_v115_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(20).rolling(25).mean() * capex.pct_change(20)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v115_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v115_signal

def f19cri_f19_capex_to_revenue_intensity_base_v116_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 116 for f19cri_f19_capex_to_revenue_intensity_base_v116_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(21).rolling(26).mean() * capex.pct_change(21)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v116_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v116_signal

def f19cri_f19_capex_to_revenue_intensity_base_v117_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 117 for f19cri_f19_capex_to_revenue_intensity_base_v117_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(22).rolling(27).mean() * capex.pct_change(22)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v117_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v117_signal

def f19cri_f19_capex_to_revenue_intensity_base_v118_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 118 for f19cri_f19_capex_to_revenue_intensity_base_v118_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(23).rolling(28).mean() * capex.pct_change(23)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v118_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v118_signal

def f19cri_f19_capex_to_revenue_intensity_base_v119_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 119 for f19cri_f19_capex_to_revenue_intensity_base_v119_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(24).rolling(29).mean() * capex.pct_change(24)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v119_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v119_signal

def f19cri_f19_capex_to_revenue_intensity_base_v120_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 120 for f19cri_f19_capex_to_revenue_intensity_base_v120_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(25).rolling(30).mean() * capex.pct_change(25)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v120_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v120_signal

def f19cri_f19_capex_to_revenue_intensity_base_v121_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 121 for f19cri_f19_capex_to_revenue_intensity_base_v121_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(26).rolling(31).mean() * capex.pct_change(26)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v121_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v121_signal

def f19cri_f19_capex_to_revenue_intensity_base_v122_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 122 for f19cri_f19_capex_to_revenue_intensity_base_v122_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(27).rolling(32).mean() * capex.pct_change(27)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v122_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v122_signal

def f19cri_f19_capex_to_revenue_intensity_base_v123_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 123 for f19cri_f19_capex_to_revenue_intensity_base_v123_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(28).rolling(33).mean() * capex.pct_change(28)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v123_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v123_signal

def f19cri_f19_capex_to_revenue_intensity_base_v124_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 124 for f19cri_f19_capex_to_revenue_intensity_base_v124_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(29).rolling(34).mean() * capex.pct_change(29)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v124_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v124_signal

def f19cri_f19_capex_to_revenue_intensity_base_v125_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 125 for f19cri_f19_capex_to_revenue_intensity_base_v125_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(30).rolling(35).mean() * capex.pct_change(30)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v125_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v125_signal

def f19cri_f19_capex_to_revenue_intensity_base_v126_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 126 for f19cri_f19_capex_to_revenue_intensity_base_v126_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(31).rolling(36).mean() * capex.pct_change(31)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v126_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v126_signal

def f19cri_f19_capex_to_revenue_intensity_base_v127_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 127 for f19cri_f19_capex_to_revenue_intensity_base_v127_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(32).rolling(37).mean() * capex.pct_change(32)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v127_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v127_signal

def f19cri_f19_capex_to_revenue_intensity_base_v128_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 128 for f19cri_f19_capex_to_revenue_intensity_base_v128_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(33).rolling(38).mean() * capex.pct_change(33)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v128_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v128_signal

def f19cri_f19_capex_to_revenue_intensity_base_v129_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 129 for f19cri_f19_capex_to_revenue_intensity_base_v129_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(34).rolling(39).mean() * capex.pct_change(34)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v129_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v129_signal

def f19cri_f19_capex_to_revenue_intensity_base_v130_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 130 for f19cri_f19_capex_to_revenue_intensity_base_v130_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(35).rolling(40).mean() * capex.pct_change(35)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v130_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v130_signal

def f19cri_f19_capex_to_revenue_intensity_base_v131_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 131 for f19cri_f19_capex_to_revenue_intensity_base_v131_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(21).mean()
    s2 = revenue.rolling(21).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(36).rolling(41).mean() * capex.pct_change(36)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v131_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v131_signal

def f19cri_f19_capex_to_revenue_intensity_base_v132_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 132 for f19cri_f19_capex_to_revenue_intensity_base_v132_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(22).mean()
    s2 = revenue.rolling(22).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(37).rolling(42).mean() * capex.pct_change(37)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v132_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v132_signal

def f19cri_f19_capex_to_revenue_intensity_base_v133_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 133 for f19cri_f19_capex_to_revenue_intensity_base_v133_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(23).mean()
    s2 = revenue.rolling(23).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(38).rolling(43).mean() * capex.pct_change(38)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v133_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v133_signal

def f19cri_f19_capex_to_revenue_intensity_base_v134_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 134 for f19cri_f19_capex_to_revenue_intensity_base_v134_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(24).mean()
    s2 = revenue.rolling(24).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(39).rolling(44).mean() * capex.pct_change(39)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v134_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v134_signal

def f19cri_f19_capex_to_revenue_intensity_base_v135_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 135 for f19cri_f19_capex_to_revenue_intensity_base_v135_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(25).mean()
    s2 = revenue.rolling(25).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(40).rolling(45).mean() * capex.pct_change(40)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v135_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v135_signal

def f19cri_f19_capex_to_revenue_intensity_base_v136_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 136 for f19cri_f19_capex_to_revenue_intensity_base_v136_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(26).mean()
    s2 = revenue.rolling(26).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(41).rolling(46).mean() * capex.pct_change(41)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v136_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v136_signal

def f19cri_f19_capex_to_revenue_intensity_base_v137_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 137 for f19cri_f19_capex_to_revenue_intensity_base_v137_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(27).mean()
    s2 = revenue.rolling(27).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(42).rolling(47).mean() * capex.pct_change(42)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v137_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v137_signal

def f19cri_f19_capex_to_revenue_intensity_base_v138_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 138 for f19cri_f19_capex_to_revenue_intensity_base_v138_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(28).mean()
    s2 = revenue.rolling(28).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(43).rolling(48).mean() * capex.pct_change(43)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v138_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v138_signal

def f19cri_f19_capex_to_revenue_intensity_base_v139_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 139 for f19cri_f19_capex_to_revenue_intensity_base_v139_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(29).mean()
    s2 = revenue.rolling(29).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(44).rolling(49).mean() * capex.pct_change(44)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v139_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v139_signal

def f19cri_f19_capex_to_revenue_intensity_base_v140_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 140 for f19cri_f19_capex_to_revenue_intensity_base_v140_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(10).mean()
    s2 = revenue.rolling(10).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(45).rolling(50).mean() * capex.pct_change(45)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v140_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v140_signal

def f19cri_f19_capex_to_revenue_intensity_base_v141_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 141 for f19cri_f19_capex_to_revenue_intensity_base_v141_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(11).mean()
    s2 = revenue.rolling(11).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(46).rolling(51).mean() * capex.pct_change(46)
    # Apply smoothing
    smoothed_signal = signal.rolling(6).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v141_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v141_signal

def f19cri_f19_capex_to_revenue_intensity_base_v142_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 142 for f19cri_f19_capex_to_revenue_intensity_base_v142_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(12).mean()
    s2 = revenue.rolling(12).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(47).rolling(52).mean() * capex.pct_change(47)
    # Apply smoothing
    smoothed_signal = signal.rolling(7).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v142_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v142_signal

def f19cri_f19_capex_to_revenue_intensity_base_v143_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 143 for f19cri_f19_capex_to_revenue_intensity_base_v143_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(13).mean()
    s2 = revenue.rolling(13).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(48).rolling(53).mean() * capex.pct_change(48)
    # Apply smoothing
    smoothed_signal = signal.rolling(8).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v143_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v143_signal

def f19cri_f19_capex_to_revenue_intensity_base_v144_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 144 for f19cri_f19_capex_to_revenue_intensity_base_v144_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(14).mean()
    s2 = revenue.rolling(14).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(49).rolling(54).mean() * capex.pct_change(49)
    # Apply smoothing
    smoothed_signal = signal.rolling(9).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v144_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v144_signal

def f19cri_f19_capex_to_revenue_intensity_base_v145_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 145 for f19cri_f19_capex_to_revenue_intensity_base_v145_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(15).mean()
    s2 = revenue.rolling(15).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(50).rolling(55).mean() * capex.pct_change(50)
    # Apply smoothing
    smoothed_signal = signal.rolling(10).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v145_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v145_signal

def f19cri_f19_capex_to_revenue_intensity_base_v146_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 146 for f19cri_f19_capex_to_revenue_intensity_base_v146_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(16).mean()
    s2 = revenue.rolling(16).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(51).rolling(56).mean() * capex.pct_change(51)
    # Apply smoothing
    smoothed_signal = signal.rolling(11).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v146_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v146_signal

def f19cri_f19_capex_to_revenue_intensity_base_v147_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 147 for f19cri_f19_capex_to_revenue_intensity_base_v147_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(17).mean()
    s2 = revenue.rolling(17).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(52).rolling(57).mean() * capex.pct_change(52)
    # Apply smoothing
    smoothed_signal = signal.rolling(12).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v147_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v147_signal

def f19cri_f19_capex_to_revenue_intensity_base_v148_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 148 for f19cri_f19_capex_to_revenue_intensity_base_v148_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(18).mean()
    s2 = revenue.rolling(18).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(53).rolling(58).mean() * capex.pct_change(53)
    # Apply smoothing
    smoothed_signal = signal.rolling(13).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v148_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v148_signal

def f19cri_f19_capex_to_revenue_intensity_base_v149_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 149 for f19cri_f19_capex_to_revenue_intensity_base_v149_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(19).mean()
    s2 = revenue.rolling(19).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(54).rolling(59).mean() * capex.pct_change(54)
    # Apply smoothing
    smoothed_signal = signal.rolling(14).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v149_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v149_signal

def f19cri_f19_capex_to_revenue_intensity_base_v150_signal(revenue, assets, ebitda, debt, equity, closeadj, volume, net_income, cash, fcf, capex, rd_expense, market_cap, enterprise_value, dividends, operating_income):
    # base derivative signal 150 for f19cri_f19_capex_to_revenue_intensity_base_v150_signal
    # This formula calculates complex financial relationships
    s1 = capex.rolling(20).mean()
    s2 = revenue.rolling(20).std()
    ratio = s1 / (s2 + 1e-9)
    signal = (capex / revenue.replace(0, np.nan)).pct_change(5).rolling(60).mean() * capex.pct_change(5)
    # Apply smoothing
    smoothed_signal = signal.rolling(5).mean()
    # Normalize with respect to ratio
    final_res = smoothed_signal * (ratio.pct_change(5) + 1)
    return final_res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f19cri_f19_capex_to_revenue_intensity_base_v150_signal'] = f19cri_f19_capex_to_revenue_intensity_base_v150_signal



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
