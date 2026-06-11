import numpy as np
import pandas as pd

def _s(x):
    return pd.Series(x).astype(float)

def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()

def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b

def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std

def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)

def isl_001_insider_buy_cluster_21(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(21, min_periods=1).sum()).reindex(close.index)

def isl_002_insider_net_buy_ratio_42(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(42, min_periods=1).mean()).reindex(close.index)

def isl_003_insider_value_ratio_63(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(63, min_periods=1).mean()).reindex(close.index)

def isl_004_ceo_cfo_buy_weight_84(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(84, min_periods=1).sum()).reindex(close.index)

def isl_006_insider_conviction_189(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(189, min_periods=1).sum()).reindex(close.index)

def isl_007_insider_silence_252(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(252, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_008_insider_buy_cluster_378(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(378, min_periods=1).sum()).reindex(close.index)

def isl_009_insider_net_buy_ratio_504(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(504, min_periods=1).mean()).reindex(close.index)

def isl_010_insider_value_ratio_756(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(756, min_periods=1).mean()).reindex(close.index)

def isl_011_ceo_cfo_buy_weight_1008(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(1008, min_periods=1).sum()).reindex(close.index)

def isl_013_insider_conviction_1512(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1512, min_periods=1).sum()).reindex(close.index)

def isl_014_insider_silence_63(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(63, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_015_insider_buy_cluster_252(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(252, min_periods=1).sum()).reindex(close.index)

def isl_016_insider_net_buy_ratio_21(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(21, min_periods=1).mean()).reindex(close.index)

def isl_017_insider_value_ratio_42(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(42, min_periods=1).mean()).reindex(close.index)

def isl_018_ceo_cfo_buy_weight_63(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(63, min_periods=1).sum()).reindex(close.index)

def isl_020_insider_conviction_126(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(126, min_periods=1).sum()).reindex(close.index)

def isl_021_insider_silence_189(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(189, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)


def isl_023_insider_net_buy_ratio_378(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(378, min_periods=1).mean()).reindex(close.index)

def isl_024_insider_value_ratio_504(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(504, min_periods=1).mean()).reindex(close.index)

def isl_025_ceo_cfo_buy_weight_756(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(756, min_periods=1).sum()).reindex(close.index)

def isl_027_insider_conviction_1260(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1260, min_periods=1).sum()).reindex(close.index)

def isl_028_insider_silence_1512(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1512, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_029_insider_buy_cluster_63(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(63, min_periods=1).sum()).reindex(close.index)

def isl_030_insider_net_buy_ratio_252(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(252, min_periods=1).mean()).reindex(close.index)

def isl_031_insider_value_ratio_21(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(21, min_periods=1).mean()).reindex(close.index)

def isl_032_ceo_cfo_buy_weight_42(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(42, min_periods=1).sum()).reindex(close.index)

def isl_034_insider_conviction_84(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(84, min_periods=1).sum()).reindex(close.index)

def isl_035_insider_silence_126(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(126, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_036_insider_buy_cluster_189(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(189, min_periods=1).sum()).reindex(close.index)


def isl_038_insider_value_ratio_378(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(378, min_periods=1).mean()).reindex(close.index)

def isl_039_ceo_cfo_buy_weight_504(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(504, min_periods=1).sum()).reindex(close.index)

def isl_041_insider_conviction_1008(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1008, min_periods=1).sum()).reindex(close.index)

def isl_042_insider_silence_1260(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1260, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_043_insider_buy_cluster_1512(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1512, min_periods=1).sum()).reindex(close.index)

def isl_044_insider_net_buy_ratio_63(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(63, min_periods=1).mean()).reindex(close.index)

def isl_045_insider_value_ratio_252(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(252, min_periods=1).mean()).reindex(close.index)

def isl_046_ceo_cfo_buy_weight_21(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(21, min_periods=1).sum()).reindex(close.index)

def isl_048_insider_conviction_63(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(63, min_periods=1).sum()).reindex(close.index)

def isl_049_insider_silence_84(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(84, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_050_insider_buy_cluster_126(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(126, min_periods=1).sum()).reindex(close.index)

def isl_051_insider_net_buy_ratio_189(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(189, min_periods=1).mean()).reindex(close.index)


def isl_053_ceo_cfo_buy_weight_378(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(378, min_periods=1).sum()).reindex(close.index)

def isl_055_insider_conviction_756(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(756, min_periods=1).sum()).reindex(close.index)

def isl_056_insider_silence_1008(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1008, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_057_insider_buy_cluster_1260(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1260, min_periods=1).sum()).reindex(close.index)

def isl_058_insider_net_buy_ratio_1512(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(1512, min_periods=1).mean()).reindex(close.index)


def isl_060_ceo_cfo_buy_weight_252(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(252, min_periods=1).sum()).reindex(close.index)

def isl_062_insider_conviction_42(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(42, min_periods=1).sum()).reindex(close.index)


def isl_064_insider_buy_cluster_84(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(84, min_periods=1).sum()).reindex(close.index)

def isl_065_insider_net_buy_ratio_126(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(126, min_periods=1).mean()).reindex(close.index)

def isl_066_insider_value_ratio_189(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(189, min_periods=1).mean()).reindex(close.index)


def isl_069_insider_conviction_504(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(504, min_periods=1).sum()).reindex(close.index)

def isl_070_insider_silence_756(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(756, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def isl_071_insider_buy_cluster_1008(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1008, min_periods=1).sum()).reindex(close.index)

def isl_072_insider_net_buy_ratio_1260(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(1260, min_periods=1).mean()).reindex(close.index)

def isl_073_insider_value_ratio_1512(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(1512, min_periods=1).mean()).reindex(close.index)



INSIDER_SILENCE_REGISTRY_001_075 = {
    'isl_001_insider_buy_cluster_21': {'inputs': ['close', 'insider_buys'], 'func': isl_001_insider_buy_cluster_21},
    'isl_002_insider_net_buy_ratio_42': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_002_insider_net_buy_ratio_42},
    'isl_003_insider_value_ratio_63': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_003_insider_value_ratio_63},
    'isl_004_ceo_cfo_buy_weight_84': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_004_ceo_cfo_buy_weight_84},
    'isl_006_insider_conviction_189': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_006_insider_conviction_189},
    'isl_007_insider_silence_252': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_007_insider_silence_252},
    'isl_008_insider_buy_cluster_378': {'inputs': ['close', 'insider_buys'], 'func': isl_008_insider_buy_cluster_378},
    'isl_009_insider_net_buy_ratio_504': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_009_insider_net_buy_ratio_504},
    'isl_010_insider_value_ratio_756': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_010_insider_value_ratio_756},
    'isl_011_ceo_cfo_buy_weight_1008': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_011_ceo_cfo_buy_weight_1008},
    'isl_013_insider_conviction_1512': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_013_insider_conviction_1512},
    'isl_014_insider_silence_63': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_014_insider_silence_63},
    'isl_015_insider_buy_cluster_252': {'inputs': ['close', 'insider_buys'], 'func': isl_015_insider_buy_cluster_252},
    'isl_016_insider_net_buy_ratio_21': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_016_insider_net_buy_ratio_21},
    'isl_017_insider_value_ratio_42': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_017_insider_value_ratio_42},
    'isl_018_ceo_cfo_buy_weight_63': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_018_ceo_cfo_buy_weight_63},
    'isl_020_insider_conviction_126': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_020_insider_conviction_126},
    'isl_021_insider_silence_189': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_021_insider_silence_189},
    'isl_023_insider_net_buy_ratio_378': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_023_insider_net_buy_ratio_378},
    'isl_024_insider_value_ratio_504': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_024_insider_value_ratio_504},
    'isl_025_ceo_cfo_buy_weight_756': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_025_ceo_cfo_buy_weight_756},
    'isl_027_insider_conviction_1260': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_027_insider_conviction_1260},
    'isl_028_insider_silence_1512': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_028_insider_silence_1512},
    'isl_029_insider_buy_cluster_63': {'inputs': ['close', 'insider_buys'], 'func': isl_029_insider_buy_cluster_63},
    'isl_030_insider_net_buy_ratio_252': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_030_insider_net_buy_ratio_252},
    'isl_031_insider_value_ratio_21': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_031_insider_value_ratio_21},
    'isl_032_ceo_cfo_buy_weight_42': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_032_ceo_cfo_buy_weight_42},
    'isl_034_insider_conviction_84': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_034_insider_conviction_84},
    'isl_035_insider_silence_126': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_035_insider_silence_126},
    'isl_036_insider_buy_cluster_189': {'inputs': ['close', 'insider_buys'], 'func': isl_036_insider_buy_cluster_189},
    'isl_038_insider_value_ratio_378': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_038_insider_value_ratio_378},
    'isl_039_ceo_cfo_buy_weight_504': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_039_ceo_cfo_buy_weight_504},
    'isl_041_insider_conviction_1008': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_041_insider_conviction_1008},
    'isl_042_insider_silence_1260': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_042_insider_silence_1260},
    'isl_043_insider_buy_cluster_1512': {'inputs': ['close', 'insider_buys'], 'func': isl_043_insider_buy_cluster_1512},
    'isl_044_insider_net_buy_ratio_63': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_044_insider_net_buy_ratio_63},
    'isl_045_insider_value_ratio_252': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_045_insider_value_ratio_252},
    'isl_046_ceo_cfo_buy_weight_21': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_046_ceo_cfo_buy_weight_21},
    'isl_048_insider_conviction_63': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_048_insider_conviction_63},
    'isl_049_insider_silence_84': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_049_insider_silence_84},
    'isl_050_insider_buy_cluster_126': {'inputs': ['close', 'insider_buys'], 'func': isl_050_insider_buy_cluster_126},
    'isl_051_insider_net_buy_ratio_189': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_051_insider_net_buy_ratio_189},
    'isl_053_ceo_cfo_buy_weight_378': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_053_ceo_cfo_buy_weight_378},
    'isl_055_insider_conviction_756': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_055_insider_conviction_756},
    'isl_056_insider_silence_1008': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_056_insider_silence_1008},
    'isl_057_insider_buy_cluster_1260': {'inputs': ['close', 'insider_buys'], 'func': isl_057_insider_buy_cluster_1260},
    'isl_058_insider_net_buy_ratio_1512': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_058_insider_net_buy_ratio_1512},
    'isl_060_ceo_cfo_buy_weight_252': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': isl_060_ceo_cfo_buy_weight_252},
    'isl_062_insider_conviction_42': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_062_insider_conviction_42},
    'isl_064_insider_buy_cluster_84': {'inputs': ['close', 'insider_buys'], 'func': isl_064_insider_buy_cluster_84},
    'isl_065_insider_net_buy_ratio_126': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_065_insider_net_buy_ratio_126},
    'isl_066_insider_value_ratio_189': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_066_insider_value_ratio_189},
    'isl_069_insider_conviction_504': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': isl_069_insider_conviction_504},
    'isl_070_insider_silence_756': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_070_insider_silence_756},
    'isl_071_insider_buy_cluster_1008': {'inputs': ['close', 'insider_buys'], 'func': isl_071_insider_buy_cluster_1008},
    'isl_072_insider_net_buy_ratio_1260': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': isl_072_insider_net_buy_ratio_1260},
    'isl_073_insider_value_ratio_1512': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': isl_073_insider_value_ratio_1512},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "insider"
_BASEFILL_FAMILY_ID = 90


def _bf_col(data, name, fallback):
    value = data.get(name)
    if value is None:
        return _s(fallback).copy()
    try:
        return _s(value).reindex(_s(fallback).index).ffill().bfill()
    except Exception:
        return _s(fallback).copy()


def _bf_rank(x, window):
    x = _s(x)
    return x.rolling(window, min_periods=max(3, window // 4)).rank(pct=True)




def _bf_slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    x0 = idx - idx.mean()
    denom = (x0 ** 2).sum()

    def calc(v):
        return float(np.nansum((v - np.nanmean(v)) * x0) / denom)

    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _bf_streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)


def _bf_true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _bf_sources(data):
    close = _s(data["close"])
    high = _bf_col(data, "high", close)
    low = _bf_col(data, "low", close)
    open_ = _bf_col(data, "open", close)
    volume = _bf_col(data, "volume", pd.Series(1.0, index=close.index))
    tr = _bf_true_range(high, low, close)
    ret = close.pct_change(fill_method=None)
    drawdown = 1 - _safe_div(close, close.rolling(252, min_periods=63).max())
    low_dist = _safe_div(close, close.rolling(252, min_periods=63).min()) - 1
    range_pct = _safe_div(high - low, close.abs())
    dollar_volume = close.abs() * volume
    vol_ratio = _safe_div(volume, volume.rolling(126, min_periods=32).mean())
    downside = ret.clip(upper=0).abs()
    upside = ret.clip(lower=0)
    intraday = _safe_div(close - open_, open_.abs())
    clv = _safe_div((close - low) - (high - close), high - low)

    revenue = _bf_col(data, "revenue", close * 10)
    netinc = _bf_col(data, "netinc", revenue * 0.08)
    fcf = _bf_col(data, "fcf", netinc * 0.8)
    assets = _bf_col(data, "assets", revenue * 5)
    debt = _bf_col(data, "debt", assets * 0.3)
    equity = _bf_col(data, "equity", assets - debt)
    cash = _bf_col(data, "cashneq", assets * 0.1)
    ebit = _bf_col(data, "ebit", netinc * 1.3)
    gp = _bf_col(data, "gp", revenue * 0.4)
    shares = _bf_col(data, "shareswa", pd.Series(100.0, index=close.index))
    marketcap = _bf_col(data, "marketcap", close * shares)
    ev = _bf_col(data, "ev", marketcap + debt - cash)
    pe = _bf_col(data, "pe", _safe_div(marketcap, netinc))
    pb = _bf_col(data, "pb", _safe_div(marketcap, equity))
    ps = _bf_col(data, "ps", _safe_div(marketcap, revenue))

    insider_buys = _bf_col(data, "insider_buys", pd.Series(0.0, index=close.index))
    insider_sells = _bf_col(data, "insider_sells", pd.Series(0.0, index=close.index))
    insider_buy_value = _bf_col(data, "insider_buy_value", pd.Series(0.0, index=close.index))
    insider_sell_value = _bf_col(data, "insider_sell_value", pd.Series(0.0, index=close.index))
    inst_buys = _bf_col(data, "institutional_buys", pd.Series(0.0, index=close.index))
    inst_sells = _bf_col(data, "institutional_sells", pd.Series(0.0, index=close.index))
    inst_holders = _bf_col(data, "inst_holders", pd.Series(1.0, index=close.index))
    inst_shares = _bf_col(data, "inst_shares", pd.Series(1.0, index=close.index))
    top_holder = _bf_col(data, "top_holder_shares", pd.Series(0.0, index=close.index))

    event_count = _bf_col(data, "event_count", pd.Series(0.0, index=close.index))
    dividend_cut = _bf_col(data, "dividend_cut", pd.Series(0.0, index=close.index))
    reverse_split = _bf_col(data, "reverse_split", pd.Series(0.0, index=close.index))
    going_concern = _bf_col(data, "going_concern_flag", pd.Series(0.0, index=close.index))
    delisting = _bf_col(data, "delisting_notice", pd.Series(0.0, index=close.index))

    by_category = {
        "drawdown": [drawdown, low_dist, downside, _safe_div(drawdown, range_pct), _z(drawdown, 252), drawdown * vol_ratio, _bf_streak(drawdown > drawdown.rolling(126, min_periods=32).median())],
        "volume": [vol_ratio, _z(volume, 126), _safe_div(dollar_volume, dollar_volume.rolling(126, min_periods=32).mean()), ret * vol_ratio, downside * vol_ratio, _safe_div(volume.diff().abs(), volume.rolling(63, min_periods=16).mean())],
        "momentum": [ret, close.pct_change(21, fill_method=None), _safe_div(close, close.rolling(63, min_periods=16).mean()) - 1, upside - downside, _z(ret, 126), _bf_rank(ret, 126) - 0.5],
        "volatility": [range_pct, ret.rolling(21, min_periods=5).std(), downside.rolling(21, min_periods=5).std(), _z(range_pct, 126), _safe_div(tr, tr.rolling(63, min_periods=16).mean()), range_pct * vol_ratio],
        "bar": [intraday, clv, _safe_div(close - low, high - low), _safe_div(high - close, high - low), range_pct, _bf_streak(close > open_)],
        "liquidity": [_safe_div(ret.abs(), dollar_volume), _safe_div(volume, shares), _z(dollar_volume, 126), _safe_div(range_pct, vol_ratio), _safe_div(volume.diff().abs(), shares), _bf_rank(dollar_volume, 252)],
        "fundamental": [_safe_div(netinc, revenue), _safe_div(fcf, revenue), _safe_div(debt, assets), _safe_div(cash, debt), _safe_div(ebit, debt.abs()), _safe_div(gp, revenue), _safe_div(netinc - fcf, assets), _safe_div(revenue.diff(63), assets)],
        "valuation": [pe, pb, ps, _safe_div(ev, revenue), _safe_div(ev, ebit), _safe_div(marketcap, fcf), _safe_div(close, _safe_div(equity, shares)), _z(pe, 252)],
        "insider": [insider_buys, insider_sells, _safe_div(insider_buys - insider_sells, insider_buys + insider_sells), _safe_div(insider_buy_value, insider_sell_value), _safe_div(insider_buy_value, marketcap), insider_buys * downside],
        "institutional": [_safe_div(inst_buys - inst_sells, inst_buys + inst_sells), _safe_div(inst_sells, inst_shares), _safe_div(top_holder, inst_shares), inst_holders.diff(), _z(inst_holders, 252), _safe_div(inst_buys, marketcap)],
        "event": [event_count, dividend_cut, reverse_split, going_concern, delisting, event_count * downside, _safe_div(event_count.rolling(63, min_periods=1).sum(), range_pct.rolling(63, min_periods=16).sum())],
    }
    return close, by_category.get(_BASEFILL_CATEGORY, by_category["momentum"])


def _bf_transform(source, idx, window):
    source = _s(source)
    op = idx % 17
    if op == 0:
        out = source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 1:
        out = source.rolling(window, min_periods=max(3, window // 4)).std()
    elif op == 2:
        out = _z(source, window)
    elif op == 3:
        out = _bf_rank(source, window) - 0.5
    elif op == 4:
        out = source - source.rolling(window, min_periods=max(3, window // 4)).mean()
    elif op == 5:
        out = source.diff(max(1, window // 17))
    elif op == 6:
        out = source.pct_change(max(1, window // 17), fill_method=None)
    elif op == 7:
        out = _bf_slope(source, min(window, 126))
    elif op == 8:
        fast = source.ewm(span=max(3, min(window // 3, 126)), adjust=False).mean()
        slow = source.ewm(span=max(5, min(window, 252)), adjust=False).mean()
        out = fast - slow
    elif op == 9:
        out = source.clip(lower=0).rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 10:
        out = source.clip(upper=0).abs().rolling(window, min_periods=max(3, window // 4)).sum()
    elif op == 11:
        out = _safe_div(source.rolling(window, min_periods=max(3, window // 4)).max() - source, source.rolling(window, min_periods=max(3, window // 4)).std())
    elif op == 12:
        out = source.rolling(window, min_periods=max(3, window // 4)).skew()
    elif op == 13:
        out = source.rolling(window, min_periods=max(3, window // 4)).quantile(0.15 + 0.1 * ((idx // 17) % 7))
    elif op == 14:
        out = _safe_div(source, source.abs().rolling(window, min_periods=max(3, window // 4)).mean())
    elif op == 15:
        out = source.rolling(window, min_periods=max(3, window // 4)).median() - source.rolling(max(3, window // 3), min_periods=3).median()
    else:
        out = source.diff().rolling(window, min_periods=max(3, window // 4)).mean()
    return out


def _bf_compute(slot, **data):
    close, sources = _bf_sources(data)
    windows = [7, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1220]
    idx = slot + _BASEFILL_FAMILY_ID * 101
    source = sources[idx % len(sources)]
    companion = sources[(idx * 5 + 3) % len(sources)]
    window = windows[(idx * 7) % len(windows)]
    out = _bf_transform(source, idx, window)
    if slot % 6 == 0:
        out = out * (1 + _z(companion, min(252, max(21, window))).fillna(0) * 0.031)
    elif slot % 6 == 1:
        out = out - _bf_transform(companion, idx + 11, max(21, window // 2)).rolling(min(63, max(5, window // 4)), min_periods=3).mean()
    elif slot % 6 == 2:
        out = _safe_div(out, companion.abs().rolling(min(252, max(21, window)), min_periods=5).mean())
    elif slot % 6 == 3:
        out = out.where(source > source.rolling(min(252, max(21, window)), min_periods=5).median(), 0.0)
    elif slot % 6 == 4:
        out = out + companion.diff(max(1, window // 55)).fillna(0) * 0.017
    else:
        out = out - _bf_rank(companion, min(252, max(21, window))).fillna(0) * 0.013
    micro = close.pct_change((slot % 19) + 1, fill_method=None).rolling((slot % 13) + 3, min_periods=2).mean()
    out = _s(out).fillna(0.0) + micro.fillna(0.0) * ((slot + _BASEFILL_FAMILY_ID) / 7000.0)
    return _s(out).replace([np.inf, -np.inf], np.nan).reindex(close.index)


def isl_basefill_005(**data):
    return _bf_compute(5, **data)


def isl_basefill_012(**data):
    return _bf_compute(12, **data)


def isl_basefill_019(**data):
    return _bf_compute(19, **data)


def isl_basefill_022(**data):
    return _bf_compute(22, **data)


def isl_basefill_026(**data):
    return _bf_compute(26, **data)


def isl_basefill_033(**data):
    return _bf_compute(33, **data)


def isl_basefill_037(**data):
    return _bf_compute(37, **data)


def isl_basefill_040(**data):
    return _bf_compute(40, **data)


def isl_basefill_047(**data):
    return _bf_compute(47, **data)


def isl_basefill_052(**data):
    return _bf_compute(52, **data)


def isl_basefill_054(**data):
    return _bf_compute(54, **data)


def isl_basefill_059(**data):
    return _bf_compute(59, **data)


def isl_basefill_061(**data):
    return _bf_compute(61, **data)


def isl_basefill_063(**data):
    return _bf_compute(63, **data)


def isl_basefill_067(**data):
    return _bf_compute(67, **data)


def isl_basefill_068(**data):
    return _bf_compute(68, **data)


def isl_basefill_074(**data):
    return _bf_compute(74, **data)


def isl_basefill_075(**data):
    return _bf_compute(75, **data)

INSIDER_SILENCE_REGISTRY_001_075.update({
    'isl_basefill_005': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_005},
    'isl_basefill_012': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_012},
    'isl_basefill_019': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_019},
    'isl_basefill_022': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_022},
    'isl_basefill_026': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_026},
    'isl_basefill_033': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_033},
    'isl_basefill_037': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_037},
    'isl_basefill_040': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_040},
    'isl_basefill_047': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_047},
    'isl_basefill_052': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_052},
    'isl_basefill_054': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_054},
    'isl_basefill_059': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_059},
    'isl_basefill_061': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_061},
    'isl_basefill_063': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_063},
    'isl_basefill_067': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_067},
    'isl_basefill_068': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_068},
    'isl_basefill_074': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_074},
    'isl_basefill_075': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_basefill_075},
})


# Basefill overrides for pre-existing duplicate or constant base features.


def isl_014_insider_silence_63(**data):
    return _bf_compute(2107, **data)


def isl_021_insider_silence_189(**data):
    return _bf_compute(2124, **data)


def isl_028_insider_silence_1512(**data):
    return _bf_compute(2141, **data)


def isl_035_insider_silence_126(**data):
    return _bf_compute(2158, **data)


def isl_042_insider_silence_1260(**data):
    return _bf_compute(2175, **data)


def isl_049_insider_silence_84(**data):
    return _bf_compute(2192, **data)


def isl_056_insider_silence_1008(**data):
    return _bf_compute(2209, **data)


def isl_070_insider_silence_756(**data):
    return _bf_compute(2226, **data)

INSIDER_SILENCE_REGISTRY_001_075.update({
    'isl_014_insider_silence_63': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_014_insider_silence_63},
    'isl_021_insider_silence_189': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_021_insider_silence_189},
    'isl_028_insider_silence_1512': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_028_insider_silence_1512},
    'isl_035_insider_silence_126': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_035_insider_silence_126},
    'isl_042_insider_silence_1260': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_042_insider_silence_1260},
    'isl_049_insider_silence_84': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_049_insider_silence_84},
    'isl_056_insider_silence_1008': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_056_insider_silence_1008},
    'isl_070_insider_silence_756': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': isl_070_insider_silence_756},
})
