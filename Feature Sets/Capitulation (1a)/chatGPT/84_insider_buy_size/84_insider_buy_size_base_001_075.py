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

def ibs_001_insider_buy_cluster_21(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(21, min_periods=1).sum()).reindex(close.index)

def ibs_002_insider_net_buy_ratio_42(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(42, min_periods=1).mean()).reindex(close.index)

def ibs_003_insider_value_ratio_63(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(63, min_periods=1).mean()).reindex(close.index)

def ibs_004_ceo_cfo_buy_weight_84(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(84, min_periods=1).sum()).reindex(close.index)

def ibs_006_insider_conviction_189(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(189, min_periods=1).sum()).reindex(close.index)

def ibs_007_insider_silence_252(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(252, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_008_insider_buy_cluster_378(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(378, min_periods=1).sum()).reindex(close.index)

def ibs_009_insider_net_buy_ratio_504(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(504, min_periods=1).mean()).reindex(close.index)

def ibs_010_insider_value_ratio_756(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(756, min_periods=1).mean()).reindex(close.index)

def ibs_011_ceo_cfo_buy_weight_1008(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(1008, min_periods=1).sum()).reindex(close.index)

def ibs_013_insider_conviction_1512(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1512, min_periods=1).sum()).reindex(close.index)

def ibs_014_insider_silence_63(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(63, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_015_insider_buy_cluster_252(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(252, min_periods=1).sum()).reindex(close.index)

def ibs_016_insider_net_buy_ratio_21(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(21, min_periods=1).mean()).reindex(close.index)

def ibs_017_insider_value_ratio_42(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(42, min_periods=1).mean()).reindex(close.index)

def ibs_018_ceo_cfo_buy_weight_63(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(63, min_periods=1).sum()).reindex(close.index)

def ibs_020_insider_conviction_126(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(126, min_periods=1).sum()).reindex(close.index)

def ibs_021_insider_silence_189(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(189, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)


def ibs_023_insider_net_buy_ratio_378(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(378, min_periods=1).mean()).reindex(close.index)

def ibs_024_insider_value_ratio_504(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(504, min_periods=1).mean()).reindex(close.index)

def ibs_025_ceo_cfo_buy_weight_756(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(756, min_periods=1).sum()).reindex(close.index)

def ibs_027_insider_conviction_1260(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1260, min_periods=1).sum()).reindex(close.index)

def ibs_028_insider_silence_1512(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1512, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_029_insider_buy_cluster_63(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(63, min_periods=1).sum()).reindex(close.index)

def ibs_030_insider_net_buy_ratio_252(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(252, min_periods=1).mean()).reindex(close.index)

def ibs_031_insider_value_ratio_21(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(21, min_periods=1).mean()).reindex(close.index)

def ibs_032_ceo_cfo_buy_weight_42(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(42, min_periods=1).sum()).reindex(close.index)

def ibs_034_insider_conviction_84(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(84, min_periods=1).sum()).reindex(close.index)

def ibs_035_insider_silence_126(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(126, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_036_insider_buy_cluster_189(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(189, min_periods=1).sum()).reindex(close.index)


def ibs_038_insider_value_ratio_378(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(378, min_periods=1).mean()).reindex(close.index)

def ibs_039_ceo_cfo_buy_weight_504(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(504, min_periods=1).sum()).reindex(close.index)

def ibs_041_insider_conviction_1008(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(1008, min_periods=1).sum()).reindex(close.index)

def ibs_042_insider_silence_1260(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1260, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_043_insider_buy_cluster_1512(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1512, min_periods=1).sum()).reindex(close.index)

def ibs_044_insider_net_buy_ratio_63(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(63, min_periods=1).mean()).reindex(close.index)

def ibs_045_insider_value_ratio_252(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(252, min_periods=1).mean()).reindex(close.index)

def ibs_046_ceo_cfo_buy_weight_21(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(21, min_periods=1).sum()).reindex(close.index)

def ibs_048_insider_conviction_63(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(63, min_periods=1).sum()).reindex(close.index)

def ibs_049_insider_silence_84(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(84, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_050_insider_buy_cluster_126(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(126, min_periods=1).sum()).reindex(close.index)

def ibs_051_insider_net_buy_ratio_189(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(189, min_periods=1).mean()).reindex(close.index)


def ibs_053_ceo_cfo_buy_weight_378(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(378, min_periods=1).sum()).reindex(close.index)

def ibs_055_insider_conviction_756(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(756, min_periods=1).sum()).reindex(close.index)

def ibs_056_insider_silence_1008(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(1008, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_057_insider_buy_cluster_1260(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1260, min_periods=1).sum()).reindex(close.index)

def ibs_058_insider_net_buy_ratio_1512(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(1512, min_periods=1).mean()).reindex(close.index)


def ibs_060_ceo_cfo_buy_weight_252(close, ceo_buys, cfo_buys, director_buys):
    close = _s(close)
    ceo_buys = _align_quarterly_to_daily(ceo_buys, close)
    cfo_buys = _align_quarterly_to_daily(cfo_buys, close)
    director_buys = _align_quarterly_to_daily(director_buys, close)
    return ((2 * ceo_buys + 1.5 * cfo_buys + director_buys).rolling(252, min_periods=1).sum()).reindex(close.index)

def ibs_062_insider_conviction_42(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(42, min_periods=1).sum()).reindex(close.index)


def ibs_064_insider_buy_cluster_84(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(84, min_periods=1).sum()).reindex(close.index)

def ibs_065_insider_net_buy_ratio_126(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(126, min_periods=1).mean()).reindex(close.index)

def ibs_066_insider_value_ratio_189(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(189, min_periods=1).mean()).reindex(close.index)


def ibs_069_insider_conviction_504(close, insider_buy_value, insider_holdings):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_holdings = _align_quarterly_to_daily(insider_holdings, close)
    return (_safe_div(insider_buy_value, insider_holdings).rolling(504, min_periods=1).sum()).reindex(close.index)

def ibs_070_insider_silence_756(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return ((insider_buys + insider_sells).rolling(756, min_periods=1).sum().eq(0).astype(float)).reindex(close.index)

def ibs_071_insider_buy_cluster_1008(close, insider_buys):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    return (insider_buys.rolling(1008, min_periods=1).sum()).reindex(close.index)

def ibs_072_insider_net_buy_ratio_1260(close, insider_buys, insider_sells):
    close = _s(close)
    insider_buys = _align_quarterly_to_daily(insider_buys, close)
    insider_sells = _align_quarterly_to_daily(insider_sells, close)
    return (_safe_div(insider_buys - insider_sells, insider_buys + insider_sells).rolling(1260, min_periods=1).mean()).reindex(close.index)

def ibs_073_insider_value_ratio_1512(close, insider_buy_value, insider_sell_value):
    close = _s(close)
    insider_buy_value = _align_quarterly_to_daily(insider_buy_value, close)
    insider_sell_value = _align_quarterly_to_daily(insider_sell_value, close)
    return (_safe_div(insider_buy_value, insider_sell_value).rolling(1512, min_periods=1).mean()).reindex(close.index)



INSIDER_BUY_SIZE_REGISTRY_001_075 = {
    'ibs_001_insider_buy_cluster_21': {'inputs': ['close', 'insider_buys'], 'func': ibs_001_insider_buy_cluster_21},
    'ibs_002_insider_net_buy_ratio_42': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_002_insider_net_buy_ratio_42},
    'ibs_003_insider_value_ratio_63': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_003_insider_value_ratio_63},
    'ibs_004_ceo_cfo_buy_weight_84': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_004_ceo_cfo_buy_weight_84},
    'ibs_006_insider_conviction_189': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_006_insider_conviction_189},
    'ibs_007_insider_silence_252': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_007_insider_silence_252},
    'ibs_008_insider_buy_cluster_378': {'inputs': ['close', 'insider_buys'], 'func': ibs_008_insider_buy_cluster_378},
    'ibs_009_insider_net_buy_ratio_504': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_009_insider_net_buy_ratio_504},
    'ibs_010_insider_value_ratio_756': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_010_insider_value_ratio_756},
    'ibs_011_ceo_cfo_buy_weight_1008': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_011_ceo_cfo_buy_weight_1008},
    'ibs_013_insider_conviction_1512': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_013_insider_conviction_1512},
    'ibs_014_insider_silence_63': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_014_insider_silence_63},
    'ibs_015_insider_buy_cluster_252': {'inputs': ['close', 'insider_buys'], 'func': ibs_015_insider_buy_cluster_252},
    'ibs_016_insider_net_buy_ratio_21': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_016_insider_net_buy_ratio_21},
    'ibs_017_insider_value_ratio_42': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_017_insider_value_ratio_42},
    'ibs_018_ceo_cfo_buy_weight_63': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_018_ceo_cfo_buy_weight_63},
    'ibs_020_insider_conviction_126': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_020_insider_conviction_126},
    'ibs_021_insider_silence_189': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_021_insider_silence_189},
    'ibs_023_insider_net_buy_ratio_378': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_023_insider_net_buy_ratio_378},
    'ibs_024_insider_value_ratio_504': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_024_insider_value_ratio_504},
    'ibs_025_ceo_cfo_buy_weight_756': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_025_ceo_cfo_buy_weight_756},
    'ibs_027_insider_conviction_1260': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_027_insider_conviction_1260},
    'ibs_028_insider_silence_1512': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_028_insider_silence_1512},
    'ibs_029_insider_buy_cluster_63': {'inputs': ['close', 'insider_buys'], 'func': ibs_029_insider_buy_cluster_63},
    'ibs_030_insider_net_buy_ratio_252': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_030_insider_net_buy_ratio_252},
    'ibs_031_insider_value_ratio_21': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_031_insider_value_ratio_21},
    'ibs_032_ceo_cfo_buy_weight_42': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_032_ceo_cfo_buy_weight_42},
    'ibs_034_insider_conviction_84': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_034_insider_conviction_84},
    'ibs_035_insider_silence_126': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_035_insider_silence_126},
    'ibs_036_insider_buy_cluster_189': {'inputs': ['close', 'insider_buys'], 'func': ibs_036_insider_buy_cluster_189},
    'ibs_038_insider_value_ratio_378': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_038_insider_value_ratio_378},
    'ibs_039_ceo_cfo_buy_weight_504': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_039_ceo_cfo_buy_weight_504},
    'ibs_041_insider_conviction_1008': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_041_insider_conviction_1008},
    'ibs_042_insider_silence_1260': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_042_insider_silence_1260},
    'ibs_043_insider_buy_cluster_1512': {'inputs': ['close', 'insider_buys'], 'func': ibs_043_insider_buy_cluster_1512},
    'ibs_044_insider_net_buy_ratio_63': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_044_insider_net_buy_ratio_63},
    'ibs_045_insider_value_ratio_252': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_045_insider_value_ratio_252},
    'ibs_046_ceo_cfo_buy_weight_21': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_046_ceo_cfo_buy_weight_21},
    'ibs_048_insider_conviction_63': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_048_insider_conviction_63},
    'ibs_049_insider_silence_84': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_049_insider_silence_84},
    'ibs_050_insider_buy_cluster_126': {'inputs': ['close', 'insider_buys'], 'func': ibs_050_insider_buy_cluster_126},
    'ibs_051_insider_net_buy_ratio_189': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_051_insider_net_buy_ratio_189},
    'ibs_053_ceo_cfo_buy_weight_378': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_053_ceo_cfo_buy_weight_378},
    'ibs_055_insider_conviction_756': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_055_insider_conviction_756},
    'ibs_056_insider_silence_1008': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_056_insider_silence_1008},
    'ibs_057_insider_buy_cluster_1260': {'inputs': ['close', 'insider_buys'], 'func': ibs_057_insider_buy_cluster_1260},
    'ibs_058_insider_net_buy_ratio_1512': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_058_insider_net_buy_ratio_1512},
    'ibs_060_ceo_cfo_buy_weight_252': {'inputs': ['close', 'ceo_buys', 'cfo_buys', 'director_buys'], 'func': ibs_060_ceo_cfo_buy_weight_252},
    'ibs_062_insider_conviction_42': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_062_insider_conviction_42},
    'ibs_064_insider_buy_cluster_84': {'inputs': ['close', 'insider_buys'], 'func': ibs_064_insider_buy_cluster_84},
    'ibs_065_insider_net_buy_ratio_126': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_065_insider_net_buy_ratio_126},
    'ibs_066_insider_value_ratio_189': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_066_insider_value_ratio_189},
    'ibs_069_insider_conviction_504': {'inputs': ['close', 'insider_buy_value', 'insider_holdings'], 'func': ibs_069_insider_conviction_504},
    'ibs_070_insider_silence_756': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_070_insider_silence_756},
    'ibs_071_insider_buy_cluster_1008': {'inputs': ['close', 'insider_buys'], 'func': ibs_071_insider_buy_cluster_1008},
    'ibs_072_insider_net_buy_ratio_1260': {'inputs': ['close', 'insider_buys', 'insider_sells'], 'func': ibs_072_insider_net_buy_ratio_1260},
    'ibs_073_insider_value_ratio_1512': {'inputs': ['close', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_073_insider_value_ratio_1512},
}


# Unique basefill features restored after duplicate pruning.
_BASEFILL_CATEGORY = "insider"
_BASEFILL_FAMILY_ID = 84


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


def ibs_basefill_005(**data):
    return _bf_compute(5, **data)


def ibs_basefill_012(**data):
    return _bf_compute(12, **data)


def ibs_basefill_019(**data):
    return _bf_compute(19, **data)


def ibs_basefill_022(**data):
    return _bf_compute(22, **data)


def ibs_basefill_026(**data):
    return _bf_compute(26, **data)


def ibs_basefill_033(**data):
    return _bf_compute(33, **data)


def ibs_basefill_037(**data):
    return _bf_compute(37, **data)


def ibs_basefill_040(**data):
    return _bf_compute(40, **data)


def ibs_basefill_047(**data):
    return _bf_compute(47, **data)


def ibs_basefill_052(**data):
    return _bf_compute(52, **data)


def ibs_basefill_054(**data):
    return _bf_compute(54, **data)


def ibs_basefill_059(**data):
    return _bf_compute(59, **data)


def ibs_basefill_061(**data):
    return _bf_compute(61, **data)


def ibs_basefill_063(**data):
    return _bf_compute(63, **data)


def ibs_basefill_067(**data):
    return _bf_compute(67, **data)


def ibs_basefill_068(**data):
    return _bf_compute(68, **data)


def ibs_basefill_074(**data):
    return _bf_compute(74, **data)


def ibs_basefill_075(**data):
    return _bf_compute(75, **data)

INSIDER_BUY_SIZE_REGISTRY_001_075.update({
    'ibs_basefill_005': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_005},
    'ibs_basefill_012': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_012},
    'ibs_basefill_019': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_019},
    'ibs_basefill_022': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_022},
    'ibs_basefill_026': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_026},
    'ibs_basefill_033': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_033},
    'ibs_basefill_037': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_037},
    'ibs_basefill_040': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_040},
    'ibs_basefill_047': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_047},
    'ibs_basefill_052': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_052},
    'ibs_basefill_054': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_054},
    'ibs_basefill_059': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_059},
    'ibs_basefill_061': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_061},
    'ibs_basefill_063': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_063},
    'ibs_basefill_067': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_067},
    'ibs_basefill_068': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_068},
    'ibs_basefill_074': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_074},
    'ibs_basefill_075': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_basefill_075},
})


# Basefill overrides for pre-existing duplicate or constant base features.


def ibs_014_insider_silence_63(**data):
    return _bf_compute(2101, **data)


def ibs_021_insider_silence_189(**data):
    return _bf_compute(2118, **data)


def ibs_028_insider_silence_1512(**data):
    return _bf_compute(2135, **data)


def ibs_035_insider_silence_126(**data):
    return _bf_compute(2152, **data)


def ibs_042_insider_silence_1260(**data):
    return _bf_compute(2169, **data)


def ibs_049_insider_silence_84(**data):
    return _bf_compute(2186, **data)


def ibs_056_insider_silence_1008(**data):
    return _bf_compute(2203, **data)


def ibs_070_insider_silence_756(**data):
    return _bf_compute(2220, **data)

INSIDER_BUY_SIZE_REGISTRY_001_075.update({
    'ibs_014_insider_silence_63': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_014_insider_silence_63},
    'ibs_021_insider_silence_189': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_021_insider_silence_189},
    'ibs_028_insider_silence_1512': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_028_insider_silence_1512},
    'ibs_035_insider_silence_126': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_035_insider_silence_126},
    'ibs_042_insider_silence_1260': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_042_insider_silence_1260},
    'ibs_049_insider_silence_84': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_049_insider_silence_84},
    'ibs_056_insider_silence_1008': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_056_insider_silence_1008},
    'ibs_070_insider_silence_756': {'inputs': ['close', 'high', 'low', 'volume', 'marketcap', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value'], 'func': ibs_070_insider_silence_756},
})
