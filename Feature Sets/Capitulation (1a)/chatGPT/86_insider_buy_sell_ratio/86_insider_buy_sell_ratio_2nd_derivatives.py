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


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


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



def ibr_151_ibr_001_insider_buy_cluster_21_roc_1(ibr_001_insider_buy_cluster_21):
    feature = _s(ibr_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def ibr_152_ibr_007_insider_silence_252_roc_42(ibr_007_insider_silence_252):
    feature = _s(ibr_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def ibr_153_ibr_013_insider_conviction_1512_roc_126(ibr_013_insider_conviction_1512):
    feature = _s(ibr_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def ibr_154_ibr_019_insider_activity_accel_1_roc_378(ibr_019_insider_activity_accel_1):
    feature = _s(ibr_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4(ibr_025_ceo_cfo_buy_weight_756):
    feature = _s(ibr_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_BUY_SELL_RATIO_REGISTRY_2ND_DERIVATIVES = {
    'ibr_151_ibr_001_insider_buy_cluster_21_roc_1': {'inputs': ['ibr_001_insider_buy_cluster_21'], 'func': ibr_151_ibr_001_insider_buy_cluster_21_roc_1},
    'ibr_152_ibr_007_insider_silence_252_roc_42': {'inputs': ['ibr_007_insider_silence_252'], 'func': ibr_152_ibr_007_insider_silence_252_roc_42},
    'ibr_153_ibr_013_insider_conviction_1512_roc_126': {'inputs': ['ibr_013_insider_conviction_1512'], 'func': ibr_153_ibr_013_insider_conviction_1512_roc_126},
    'ibr_154_ibr_019_insider_activity_accel_1_roc_378': {'inputs': ['ibr_019_insider_activity_accel_1'], 'func': ibr_154_ibr_019_insider_activity_accel_1_roc_378},
    'ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['ibr_025_ceo_cfo_buy_weight_756'], 'func': ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ibsr_replacement_d2_001(ibr_019_insider_activity_accel_1):
    feature = _clean(ibr_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_001'] = {'inputs': ['ibr_019_insider_activity_accel_1'], 'func': ibsr_replacement_d2_001}


def ibsr_replacement_d2_002(ibsr_replacement_001):
    feature = _clean(ibsr_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_002'] = {'inputs': ['ibsr_replacement_001'], 'func': ibsr_replacement_d2_002}


def ibsr_replacement_d2_003(ibsr_replacement_002):
    feature = _clean(ibsr_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_003'] = {'inputs': ['ibsr_replacement_002'], 'func': ibsr_replacement_d2_003}


def ibsr_replacement_d2_004(ibsr_replacement_003):
    feature = _clean(ibsr_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_004'] = {'inputs': ['ibsr_replacement_003'], 'func': ibsr_replacement_d2_004}


def ibsr_replacement_d2_005(ibsr_replacement_004):
    feature = _clean(ibsr_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_005'] = {'inputs': ['ibsr_replacement_004'], 'func': ibsr_replacement_d2_005}


def ibsr_replacement_d2_006(ibsr_replacement_005):
    feature = _clean(ibsr_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_006'] = {'inputs': ['ibsr_replacement_005'], 'func': ibsr_replacement_d2_006}


def ibsr_replacement_d2_007(ibsr_replacement_006):
    feature = _clean(ibsr_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_007'] = {'inputs': ['ibsr_replacement_006'], 'func': ibsr_replacement_d2_007}


def ibsr_replacement_d2_008(ibsr_replacement_007):
    feature = _clean(ibsr_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_008'] = {'inputs': ['ibsr_replacement_007'], 'func': ibsr_replacement_d2_008}


def ibsr_replacement_d2_009(ibsr_replacement_008):
    feature = _clean(ibsr_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_009'] = {'inputs': ['ibsr_replacement_008'], 'func': ibsr_replacement_d2_009}


def ibsr_replacement_d2_010(ibsr_replacement_009):
    feature = _clean(ibsr_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_010'] = {'inputs': ['ibsr_replacement_009'], 'func': ibsr_replacement_d2_010}


def ibsr_replacement_d2_011(ibsr_replacement_010):
    feature = _clean(ibsr_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_011'] = {'inputs': ['ibsr_replacement_010'], 'func': ibsr_replacement_d2_011}


def ibsr_replacement_d2_012(ibsr_replacement_011):
    feature = _clean(ibsr_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_012'] = {'inputs': ['ibsr_replacement_011'], 'func': ibsr_replacement_d2_012}


def ibsr_replacement_d2_013(ibsr_replacement_012):
    feature = _clean(ibsr_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_013'] = {'inputs': ['ibsr_replacement_012'], 'func': ibsr_replacement_d2_013}


def ibsr_replacement_d2_014(ibsr_replacement_013):
    feature = _clean(ibsr_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_014'] = {'inputs': ['ibsr_replacement_013'], 'func': ibsr_replacement_d2_014}


def ibsr_replacement_d2_015(ibsr_replacement_014):
    feature = _clean(ibsr_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_015'] = {'inputs': ['ibsr_replacement_014'], 'func': ibsr_replacement_d2_015}


def ibsr_replacement_d2_016(ibsr_replacement_015):
    feature = _clean(ibsr_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_016'] = {'inputs': ['ibsr_replacement_015'], 'func': ibsr_replacement_d2_016}


def ibsr_replacement_d2_017(ibsr_replacement_016):
    feature = _clean(ibsr_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_017'] = {'inputs': ['ibsr_replacement_016'], 'func': ibsr_replacement_d2_017}


def ibsr_replacement_d2_018(ibsr_replacement_017):
    feature = _clean(ibsr_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_018'] = {'inputs': ['ibsr_replacement_017'], 'func': ibsr_replacement_d2_018}


def ibsr_replacement_d2_019(ibsr_replacement_018):
    feature = _clean(ibsr_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_019'] = {'inputs': ['ibsr_replacement_018'], 'func': ibsr_replacement_d2_019}


def ibsr_replacement_d2_020(ibsr_replacement_019):
    feature = _clean(ibsr_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_020'] = {'inputs': ['ibsr_replacement_019'], 'func': ibsr_replacement_d2_020}


def ibsr_replacement_d2_021(ibsr_replacement_020):
    feature = _clean(ibsr_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_021'] = {'inputs': ['ibsr_replacement_020'], 'func': ibsr_replacement_d2_021}


def ibsr_replacement_d2_022(ibsr_replacement_021):
    feature = _clean(ibsr_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_022'] = {'inputs': ['ibsr_replacement_021'], 'func': ibsr_replacement_d2_022}


def ibsr_replacement_d2_023(ibsr_replacement_022):
    feature = _clean(ibsr_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_023'] = {'inputs': ['ibsr_replacement_022'], 'func': ibsr_replacement_d2_023}


def ibsr_replacement_d2_024(ibsr_replacement_023):
    feature = _clean(ibsr_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_024'] = {'inputs': ['ibsr_replacement_023'], 'func': ibsr_replacement_d2_024}


def ibsr_replacement_d2_025(ibsr_replacement_024):
    feature = _clean(ibsr_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_025'] = {'inputs': ['ibsr_replacement_024'], 'func': ibsr_replacement_d2_025}


def ibsr_replacement_d2_026(ibsr_replacement_025):
    feature = _clean(ibsr_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_026'] = {'inputs': ['ibsr_replacement_025'], 'func': ibsr_replacement_d2_026}


def ibsr_replacement_d2_027(ibsr_replacement_026):
    feature = _clean(ibsr_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_027'] = {'inputs': ['ibsr_replacement_026'], 'func': ibsr_replacement_d2_027}


def ibsr_replacement_d2_028(ibsr_replacement_027):
    feature = _clean(ibsr_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_028'] = {'inputs': ['ibsr_replacement_027'], 'func': ibsr_replacement_d2_028}


def ibsr_replacement_d2_029(ibsr_replacement_028):
    feature = _clean(ibsr_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_029'] = {'inputs': ['ibsr_replacement_028'], 'func': ibsr_replacement_d2_029}


def ibsr_replacement_d2_030(ibsr_replacement_029):
    feature = _clean(ibsr_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_030'] = {'inputs': ['ibsr_replacement_029'], 'func': ibsr_replacement_d2_030}


def ibsr_replacement_d2_031(ibsr_replacement_030):
    feature = _clean(ibsr_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_031'] = {'inputs': ['ibsr_replacement_030'], 'func': ibsr_replacement_d2_031}


def ibsr_replacement_d2_032(ibsr_replacement_031):
    feature = _clean(ibsr_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_032'] = {'inputs': ['ibsr_replacement_031'], 'func': ibsr_replacement_d2_032}


def ibsr_replacement_d2_033(ibsr_replacement_032):
    feature = _clean(ibsr_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_033'] = {'inputs': ['ibsr_replacement_032'], 'func': ibsr_replacement_d2_033}


def ibsr_replacement_d2_034(ibsr_replacement_033):
    feature = _clean(ibsr_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_034'] = {'inputs': ['ibsr_replacement_033'], 'func': ibsr_replacement_d2_034}


def ibsr_replacement_d2_035(ibsr_replacement_034):
    feature = _clean(ibsr_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_035'] = {'inputs': ['ibsr_replacement_034'], 'func': ibsr_replacement_d2_035}


def ibsr_replacement_d2_036(ibsr_replacement_035):
    feature = _clean(ibsr_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_036'] = {'inputs': ['ibsr_replacement_035'], 'func': ibsr_replacement_d2_036}


def ibsr_replacement_d2_037(ibsr_replacement_036):
    feature = _clean(ibsr_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_037'] = {'inputs': ['ibsr_replacement_036'], 'func': ibsr_replacement_d2_037}


def ibsr_replacement_d2_038(ibsr_replacement_037):
    feature = _clean(ibsr_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_038'] = {'inputs': ['ibsr_replacement_037'], 'func': ibsr_replacement_d2_038}


def ibsr_replacement_d2_039(ibsr_replacement_038):
    feature = _clean(ibsr_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_039'] = {'inputs': ['ibsr_replacement_038'], 'func': ibsr_replacement_d2_039}


def ibsr_replacement_d2_040(ibsr_replacement_039):
    feature = _clean(ibsr_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_040'] = {'inputs': ['ibsr_replacement_039'], 'func': ibsr_replacement_d2_040}


def ibsr_replacement_d2_041(ibsr_replacement_040):
    feature = _clean(ibsr_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_041'] = {'inputs': ['ibsr_replacement_040'], 'func': ibsr_replacement_d2_041}


def ibsr_replacement_d2_042(ibsr_replacement_041):
    feature = _clean(ibsr_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_042'] = {'inputs': ['ibsr_replacement_041'], 'func': ibsr_replacement_d2_042}


def ibsr_replacement_d2_043(ibsr_replacement_042):
    feature = _clean(ibsr_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_043'] = {'inputs': ['ibsr_replacement_042'], 'func': ibsr_replacement_d2_043}


def ibsr_replacement_d2_044(ibsr_replacement_043):
    feature = _clean(ibsr_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_044'] = {'inputs': ['ibsr_replacement_043'], 'func': ibsr_replacement_d2_044}


def ibsr_replacement_d2_045(ibsr_replacement_044):
    feature = _clean(ibsr_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_045'] = {'inputs': ['ibsr_replacement_044'], 'func': ibsr_replacement_d2_045}


def ibsr_replacement_d2_046(ibsr_replacement_045):
    feature = _clean(ibsr_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_046'] = {'inputs': ['ibsr_replacement_045'], 'func': ibsr_replacement_d2_046}


def ibsr_replacement_d2_047(ibsr_replacement_046):
    feature = _clean(ibsr_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_047'] = {'inputs': ['ibsr_replacement_046'], 'func': ibsr_replacement_d2_047}


def ibsr_replacement_d2_048(ibsr_replacement_047):
    feature = _clean(ibsr_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_048'] = {'inputs': ['ibsr_replacement_047'], 'func': ibsr_replacement_d2_048}


def ibsr_replacement_d2_049(ibsr_replacement_048):
    feature = _clean(ibsr_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_049'] = {'inputs': ['ibsr_replacement_048'], 'func': ibsr_replacement_d2_049}


def ibsr_replacement_d2_050(ibsr_replacement_049):
    feature = _clean(ibsr_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_050'] = {'inputs': ['ibsr_replacement_049'], 'func': ibsr_replacement_d2_050}


def ibsr_replacement_d2_051(ibsr_replacement_050):
    feature = _clean(ibsr_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_051'] = {'inputs': ['ibsr_replacement_050'], 'func': ibsr_replacement_d2_051}


def ibsr_replacement_d2_052(ibsr_replacement_051):
    feature = _clean(ibsr_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_052'] = {'inputs': ['ibsr_replacement_051'], 'func': ibsr_replacement_d2_052}


def ibsr_replacement_d2_053(ibsr_replacement_052):
    feature = _clean(ibsr_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_053'] = {'inputs': ['ibsr_replacement_052'], 'func': ibsr_replacement_d2_053}


def ibsr_replacement_d2_054(ibsr_replacement_053):
    feature = _clean(ibsr_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_054'] = {'inputs': ['ibsr_replacement_053'], 'func': ibsr_replacement_d2_054}


def ibsr_replacement_d2_055(ibsr_replacement_054):
    feature = _clean(ibsr_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_055'] = {'inputs': ['ibsr_replacement_054'], 'func': ibsr_replacement_d2_055}


def ibsr_replacement_d2_056(ibsr_replacement_055):
    feature = _clean(ibsr_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_056'] = {'inputs': ['ibsr_replacement_055'], 'func': ibsr_replacement_d2_056}


def ibsr_replacement_d2_057(ibsr_replacement_056):
    feature = _clean(ibsr_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_057'] = {'inputs': ['ibsr_replacement_056'], 'func': ibsr_replacement_d2_057}


def ibsr_replacement_d2_058(ibsr_replacement_057):
    feature = _clean(ibsr_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_058'] = {'inputs': ['ibsr_replacement_057'], 'func': ibsr_replacement_d2_058}


def ibsr_replacement_d2_059(ibsr_replacement_058):
    feature = _clean(ibsr_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_059'] = {'inputs': ['ibsr_replacement_058'], 'func': ibsr_replacement_d2_059}


def ibsr_replacement_d2_060(ibsr_replacement_059):
    feature = _clean(ibsr_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_060'] = {'inputs': ['ibsr_replacement_059'], 'func': ibsr_replacement_d2_060}


def ibsr_replacement_d2_061(ibsr_replacement_060):
    feature = _clean(ibsr_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_061'] = {'inputs': ['ibsr_replacement_060'], 'func': ibsr_replacement_d2_061}


def ibsr_replacement_d2_062(ibsr_replacement_061):
    feature = _clean(ibsr_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_062'] = {'inputs': ['ibsr_replacement_061'], 'func': ibsr_replacement_d2_062}


def ibsr_replacement_d2_063(ibsr_replacement_062):
    feature = _clean(ibsr_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_063'] = {'inputs': ['ibsr_replacement_062'], 'func': ibsr_replacement_d2_063}


def ibsr_replacement_d2_064(ibsr_replacement_063):
    feature = _clean(ibsr_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_064'] = {'inputs': ['ibsr_replacement_063'], 'func': ibsr_replacement_d2_064}


def ibsr_replacement_d2_065(ibsr_replacement_064):
    feature = _clean(ibsr_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_065'] = {'inputs': ['ibsr_replacement_064'], 'func': ibsr_replacement_d2_065}


def ibsr_replacement_d2_066(ibsr_replacement_065):
    feature = _clean(ibsr_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_066'] = {'inputs': ['ibsr_replacement_065'], 'func': ibsr_replacement_d2_066}


def ibsr_replacement_d2_067(ibsr_replacement_066):
    feature = _clean(ibsr_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_067'] = {'inputs': ['ibsr_replacement_066'], 'func': ibsr_replacement_d2_067}


def ibsr_replacement_d2_068(ibsr_replacement_067):
    feature = _clean(ibsr_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_068'] = {'inputs': ['ibsr_replacement_067'], 'func': ibsr_replacement_d2_068}


def ibsr_replacement_d2_069(ibsr_replacement_068):
    feature = _clean(ibsr_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_069'] = {'inputs': ['ibsr_replacement_068'], 'func': ibsr_replacement_d2_069}


def ibsr_replacement_d2_070(ibsr_replacement_069):
    feature = _clean(ibsr_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_070'] = {'inputs': ['ibsr_replacement_069'], 'func': ibsr_replacement_d2_070}


def ibsr_replacement_d2_071(ibsr_replacement_070):
    feature = _clean(ibsr_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_071'] = {'inputs': ['ibsr_replacement_070'], 'func': ibsr_replacement_d2_071}


def ibsr_replacement_d2_072(ibsr_replacement_071):
    feature = _clean(ibsr_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_072'] = {'inputs': ['ibsr_replacement_071'], 'func': ibsr_replacement_d2_072}


def ibsr_replacement_d2_073(ibsr_replacement_072):
    feature = _clean(ibsr_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_073'] = {'inputs': ['ibsr_replacement_072'], 'func': ibsr_replacement_d2_073}


def ibsr_replacement_d2_074(ibsr_replacement_073):
    feature = _clean(ibsr_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_074'] = {'inputs': ['ibsr_replacement_073'], 'func': ibsr_replacement_d2_074}


def ibsr_replacement_d2_075(ibsr_replacement_074):
    feature = _clean(ibsr_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_075'] = {'inputs': ['ibsr_replacement_074'], 'func': ibsr_replacement_d2_075}


def ibsr_replacement_d2_076(ibsr_replacement_075):
    feature = _clean(ibsr_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_076'] = {'inputs': ['ibsr_replacement_075'], 'func': ibsr_replacement_d2_076}


def ibsr_replacement_d2_077(ibsr_replacement_076):
    feature = _clean(ibsr_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_077'] = {'inputs': ['ibsr_replacement_076'], 'func': ibsr_replacement_d2_077}


def ibsr_replacement_d2_078(ibsr_replacement_077):
    feature = _clean(ibsr_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_078'] = {'inputs': ['ibsr_replacement_077'], 'func': ibsr_replacement_d2_078}


def ibsr_replacement_d2_079(ibsr_replacement_078):
    feature = _clean(ibsr_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_079'] = {'inputs': ['ibsr_replacement_078'], 'func': ibsr_replacement_d2_079}


def ibsr_replacement_d2_080(ibsr_replacement_079):
    feature = _clean(ibsr_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_080'] = {'inputs': ['ibsr_replacement_079'], 'func': ibsr_replacement_d2_080}


def ibsr_replacement_d2_081(ibsr_replacement_080):
    feature = _clean(ibsr_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_081'] = {'inputs': ['ibsr_replacement_080'], 'func': ibsr_replacement_d2_081}


def ibsr_replacement_d2_082(ibsr_replacement_081):
    feature = _clean(ibsr_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_082'] = {'inputs': ['ibsr_replacement_081'], 'func': ibsr_replacement_d2_082}


def ibsr_replacement_d2_083(ibsr_replacement_082):
    feature = _clean(ibsr_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_083'] = {'inputs': ['ibsr_replacement_082'], 'func': ibsr_replacement_d2_083}


def ibsr_replacement_d2_084(ibsr_replacement_083):
    feature = _clean(ibsr_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_084'] = {'inputs': ['ibsr_replacement_083'], 'func': ibsr_replacement_d2_084}


def ibsr_replacement_d2_085(ibsr_replacement_084):
    feature = _clean(ibsr_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_085'] = {'inputs': ['ibsr_replacement_084'], 'func': ibsr_replacement_d2_085}


def ibsr_replacement_d2_086(ibsr_replacement_085):
    feature = _clean(ibsr_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_086'] = {'inputs': ['ibsr_replacement_085'], 'func': ibsr_replacement_d2_086}


def ibsr_replacement_d2_087(ibsr_replacement_086):
    feature = _clean(ibsr_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_087'] = {'inputs': ['ibsr_replacement_086'], 'func': ibsr_replacement_d2_087}


def ibsr_replacement_d2_088(ibsr_replacement_087):
    feature = _clean(ibsr_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_088'] = {'inputs': ['ibsr_replacement_087'], 'func': ibsr_replacement_d2_088}


def ibsr_replacement_d2_089(ibsr_replacement_088):
    feature = _clean(ibsr_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_089'] = {'inputs': ['ibsr_replacement_088'], 'func': ibsr_replacement_d2_089}


def ibsr_replacement_d2_090(ibsr_replacement_089):
    feature = _clean(ibsr_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_090'] = {'inputs': ['ibsr_replacement_089'], 'func': ibsr_replacement_d2_090}


def ibsr_replacement_d2_091(ibsr_replacement_090):
    feature = _clean(ibsr_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_091'] = {'inputs': ['ibsr_replacement_090'], 'func': ibsr_replacement_d2_091}


def ibsr_replacement_d2_092(ibsr_replacement_091):
    feature = _clean(ibsr_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_092'] = {'inputs': ['ibsr_replacement_091'], 'func': ibsr_replacement_d2_092}


def ibsr_replacement_d2_093(ibsr_replacement_092):
    feature = _clean(ibsr_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_093'] = {'inputs': ['ibsr_replacement_092'], 'func': ibsr_replacement_d2_093}


def ibsr_replacement_d2_094(ibsr_replacement_093):
    feature = _clean(ibsr_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_094'] = {'inputs': ['ibsr_replacement_093'], 'func': ibsr_replacement_d2_094}


def ibsr_replacement_d2_095(ibsr_replacement_094):
    feature = _clean(ibsr_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_095'] = {'inputs': ['ibsr_replacement_094'], 'func': ibsr_replacement_d2_095}


def ibsr_replacement_d2_096(ibsr_replacement_095):
    feature = _clean(ibsr_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_096'] = {'inputs': ['ibsr_replacement_095'], 'func': ibsr_replacement_d2_096}


def ibsr_replacement_d2_097(ibsr_replacement_096):
    feature = _clean(ibsr_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_097'] = {'inputs': ['ibsr_replacement_096'], 'func': ibsr_replacement_d2_097}


def ibsr_replacement_d2_098(ibsr_replacement_097):
    feature = _clean(ibsr_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_098'] = {'inputs': ['ibsr_replacement_097'], 'func': ibsr_replacement_d2_098}


def ibsr_replacement_d2_099(ibsr_replacement_098):
    feature = _clean(ibsr_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_099'] = {'inputs': ['ibsr_replacement_098'], 'func': ibsr_replacement_d2_099}


def ibsr_replacement_d2_100(ibsr_replacement_099):
    feature = _clean(ibsr_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_100'] = {'inputs': ['ibsr_replacement_099'], 'func': ibsr_replacement_d2_100}


def ibsr_replacement_d2_101(ibsr_replacement_100):
    feature = _clean(ibsr_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_101'] = {'inputs': ['ibsr_replacement_100'], 'func': ibsr_replacement_d2_101}


def ibsr_replacement_d2_102(ibsr_replacement_101):
    feature = _clean(ibsr_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_102'] = {'inputs': ['ibsr_replacement_101'], 'func': ibsr_replacement_d2_102}


def ibsr_replacement_d2_103(ibsr_replacement_102):
    feature = _clean(ibsr_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_103'] = {'inputs': ['ibsr_replacement_102'], 'func': ibsr_replacement_d2_103}


def ibsr_replacement_d2_104(ibsr_replacement_103):
    feature = _clean(ibsr_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_104'] = {'inputs': ['ibsr_replacement_103'], 'func': ibsr_replacement_d2_104}


def ibsr_replacement_d2_105(ibsr_replacement_104):
    feature = _clean(ibsr_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_105'] = {'inputs': ['ibsr_replacement_104'], 'func': ibsr_replacement_d2_105}


def ibsr_replacement_d2_106(ibsr_replacement_105):
    feature = _clean(ibsr_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_106'] = {'inputs': ['ibsr_replacement_105'], 'func': ibsr_replacement_d2_106}


def ibsr_replacement_d2_107(ibsr_replacement_106):
    feature = _clean(ibsr_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_107'] = {'inputs': ['ibsr_replacement_106'], 'func': ibsr_replacement_d2_107}


def ibsr_replacement_d2_108(ibsr_replacement_107):
    feature = _clean(ibsr_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_108'] = {'inputs': ['ibsr_replacement_107'], 'func': ibsr_replacement_d2_108}


def ibsr_replacement_d2_109(ibsr_replacement_108):
    feature = _clean(ibsr_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_109'] = {'inputs': ['ibsr_replacement_108'], 'func': ibsr_replacement_d2_109}


def ibsr_replacement_d2_110(ibsr_replacement_109):
    feature = _clean(ibsr_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_110'] = {'inputs': ['ibsr_replacement_109'], 'func': ibsr_replacement_d2_110}


def ibsr_replacement_d2_111(ibsr_replacement_110):
    feature = _clean(ibsr_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_111'] = {'inputs': ['ibsr_replacement_110'], 'func': ibsr_replacement_d2_111}


def ibsr_replacement_d2_112(ibsr_replacement_111):
    feature = _clean(ibsr_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IBSR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibsr_replacement_d2_112'] = {'inputs': ['ibsr_replacement_111'], 'func': ibsr_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42(ibr_002_insider_net_buy_ratio_42):
    return _base_universe_d2(ibr_002_insider_net_buy_ratio_42, 1)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42'] = {'inputs': ['ibr_002_insider_net_buy_ratio_42'], 'func': ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42}


def ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63(ibr_003_insider_value_ratio_63):
    return _base_universe_d2(ibr_003_insider_value_ratio_63, 2)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63'] = {'inputs': ['ibr_003_insider_value_ratio_63'], 'func': ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63}


def ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84(ibr_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(ibr_004_ceo_cfo_buy_weight_84, 3)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibr_004_ceo_cfo_buy_weight_84'], 'func': ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84}


def ibr_base_universe_d2_004_ibr_006_insider_conviction_189(ibr_006_insider_conviction_189):
    return _base_universe_d2(ibr_006_insider_conviction_189, 4)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_004_ibr_006_insider_conviction_189'] = {'inputs': ['ibr_006_insider_conviction_189'], 'func': ibr_base_universe_d2_004_ibr_006_insider_conviction_189}


def ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378(ibr_008_insider_buy_cluster_378):
    return _base_universe_d2(ibr_008_insider_buy_cluster_378, 5)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378'] = {'inputs': ['ibr_008_insider_buy_cluster_378'], 'func': ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378}


def ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504(ibr_009_insider_net_buy_ratio_504):
    return _base_universe_d2(ibr_009_insider_net_buy_ratio_504, 6)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504'] = {'inputs': ['ibr_009_insider_net_buy_ratio_504'], 'func': ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504}


def ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756(ibr_010_insider_value_ratio_756):
    return _base_universe_d2(ibr_010_insider_value_ratio_756, 7)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756'] = {'inputs': ['ibr_010_insider_value_ratio_756'], 'func': ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756}


def ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008(ibr_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(ibr_011_ceo_cfo_buy_weight_1008, 8)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibr_011_ceo_cfo_buy_weight_1008'], 'func': ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008}


def ibr_base_universe_d2_009_ibr_014_insider_silence_63(ibr_014_insider_silence_63):
    return _base_universe_d2(ibr_014_insider_silence_63, 9)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_009_ibr_014_insider_silence_63'] = {'inputs': ['ibr_014_insider_silence_63'], 'func': ibr_base_universe_d2_009_ibr_014_insider_silence_63}


def ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252(ibr_015_insider_buy_cluster_252):
    return _base_universe_d2(ibr_015_insider_buy_cluster_252, 10)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252'] = {'inputs': ['ibr_015_insider_buy_cluster_252'], 'func': ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252}


def ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21(ibr_016_insider_net_buy_ratio_21):
    return _base_universe_d2(ibr_016_insider_net_buy_ratio_21, 11)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21'] = {'inputs': ['ibr_016_insider_net_buy_ratio_21'], 'func': ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21}


def ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42(ibr_017_insider_value_ratio_42):
    return _base_universe_d2(ibr_017_insider_value_ratio_42, 12)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42'] = {'inputs': ['ibr_017_insider_value_ratio_42'], 'func': ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42}


def ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63(ibr_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(ibr_018_ceo_cfo_buy_weight_63, 13)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibr_018_ceo_cfo_buy_weight_63'], 'func': ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63}


def ibr_base_universe_d2_014_ibr_020_insider_conviction_126(ibr_020_insider_conviction_126):
    return _base_universe_d2(ibr_020_insider_conviction_126, 14)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_014_ibr_020_insider_conviction_126'] = {'inputs': ['ibr_020_insider_conviction_126'], 'func': ibr_base_universe_d2_014_ibr_020_insider_conviction_126}


def ibr_base_universe_d2_015_ibr_021_insider_silence_189(ibr_021_insider_silence_189):
    return _base_universe_d2(ibr_021_insider_silence_189, 15)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_015_ibr_021_insider_silence_189'] = {'inputs': ['ibr_021_insider_silence_189'], 'func': ibr_base_universe_d2_015_ibr_021_insider_silence_189}


def ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378(ibr_023_insider_net_buy_ratio_378):
    return _base_universe_d2(ibr_023_insider_net_buy_ratio_378, 16)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378'] = {'inputs': ['ibr_023_insider_net_buy_ratio_378'], 'func': ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378}


def ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504(ibr_024_insider_value_ratio_504):
    return _base_universe_d2(ibr_024_insider_value_ratio_504, 17)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504'] = {'inputs': ['ibr_024_insider_value_ratio_504'], 'func': ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504}


def ibr_base_universe_d2_018_ibr_027_insider_conviction_1260(ibr_027_insider_conviction_1260):
    return _base_universe_d2(ibr_027_insider_conviction_1260, 18)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_018_ibr_027_insider_conviction_1260'] = {'inputs': ['ibr_027_insider_conviction_1260'], 'func': ibr_base_universe_d2_018_ibr_027_insider_conviction_1260}


def ibr_base_universe_d2_019_ibr_028_insider_silence_1512(ibr_028_insider_silence_1512):
    return _base_universe_d2(ibr_028_insider_silence_1512, 19)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_019_ibr_028_insider_silence_1512'] = {'inputs': ['ibr_028_insider_silence_1512'], 'func': ibr_base_universe_d2_019_ibr_028_insider_silence_1512}


def ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63(ibr_029_insider_buy_cluster_63):
    return _base_universe_d2(ibr_029_insider_buy_cluster_63, 20)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63'] = {'inputs': ['ibr_029_insider_buy_cluster_63'], 'func': ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63}


def ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252(ibr_030_insider_net_buy_ratio_252):
    return _base_universe_d2(ibr_030_insider_net_buy_ratio_252, 21)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252'] = {'inputs': ['ibr_030_insider_net_buy_ratio_252'], 'func': ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252}


def ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21(ibr_031_insider_value_ratio_21):
    return _base_universe_d2(ibr_031_insider_value_ratio_21, 22)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21'] = {'inputs': ['ibr_031_insider_value_ratio_21'], 'func': ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21}


def ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42(ibr_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(ibr_032_ceo_cfo_buy_weight_42, 23)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibr_032_ceo_cfo_buy_weight_42'], 'func': ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42}


def ibr_base_universe_d2_024_ibr_034_insider_conviction_84(ibr_034_insider_conviction_84):
    return _base_universe_d2(ibr_034_insider_conviction_84, 24)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_024_ibr_034_insider_conviction_84'] = {'inputs': ['ibr_034_insider_conviction_84'], 'func': ibr_base_universe_d2_024_ibr_034_insider_conviction_84}


def ibr_base_universe_d2_025_ibr_035_insider_silence_126(ibr_035_insider_silence_126):
    return _base_universe_d2(ibr_035_insider_silence_126, 25)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_025_ibr_035_insider_silence_126'] = {'inputs': ['ibr_035_insider_silence_126'], 'func': ibr_base_universe_d2_025_ibr_035_insider_silence_126}


def ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189(ibr_036_insider_buy_cluster_189):
    return _base_universe_d2(ibr_036_insider_buy_cluster_189, 26)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189'] = {'inputs': ['ibr_036_insider_buy_cluster_189'], 'func': ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189}


def ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378(ibr_038_insider_value_ratio_378):
    return _base_universe_d2(ibr_038_insider_value_ratio_378, 27)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378'] = {'inputs': ['ibr_038_insider_value_ratio_378'], 'func': ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378}


def ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504(ibr_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(ibr_039_ceo_cfo_buy_weight_504, 28)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibr_039_ceo_cfo_buy_weight_504'], 'func': ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504}


def ibr_base_universe_d2_029_ibr_041_insider_conviction_1008(ibr_041_insider_conviction_1008):
    return _base_universe_d2(ibr_041_insider_conviction_1008, 29)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_029_ibr_041_insider_conviction_1008'] = {'inputs': ['ibr_041_insider_conviction_1008'], 'func': ibr_base_universe_d2_029_ibr_041_insider_conviction_1008}


def ibr_base_universe_d2_030_ibr_042_insider_silence_1260(ibr_042_insider_silence_1260):
    return _base_universe_d2(ibr_042_insider_silence_1260, 30)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_030_ibr_042_insider_silence_1260'] = {'inputs': ['ibr_042_insider_silence_1260'], 'func': ibr_base_universe_d2_030_ibr_042_insider_silence_1260}


def ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512(ibr_043_insider_buy_cluster_1512):
    return _base_universe_d2(ibr_043_insider_buy_cluster_1512, 31)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512'] = {'inputs': ['ibr_043_insider_buy_cluster_1512'], 'func': ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512}


def ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63(ibr_044_insider_net_buy_ratio_63):
    return _base_universe_d2(ibr_044_insider_net_buy_ratio_63, 32)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63'] = {'inputs': ['ibr_044_insider_net_buy_ratio_63'], 'func': ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63}


def ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252(ibr_045_insider_value_ratio_252):
    return _base_universe_d2(ibr_045_insider_value_ratio_252, 33)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252'] = {'inputs': ['ibr_045_insider_value_ratio_252'], 'func': ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252}


def ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21(ibr_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(ibr_046_ceo_cfo_buy_weight_21, 34)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibr_046_ceo_cfo_buy_weight_21'], 'func': ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21}


def ibr_base_universe_d2_035_ibr_048_insider_conviction_63(ibr_048_insider_conviction_63):
    return _base_universe_d2(ibr_048_insider_conviction_63, 35)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_035_ibr_048_insider_conviction_63'] = {'inputs': ['ibr_048_insider_conviction_63'], 'func': ibr_base_universe_d2_035_ibr_048_insider_conviction_63}


def ibr_base_universe_d2_036_ibr_049_insider_silence_84(ibr_049_insider_silence_84):
    return _base_universe_d2(ibr_049_insider_silence_84, 36)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_036_ibr_049_insider_silence_84'] = {'inputs': ['ibr_049_insider_silence_84'], 'func': ibr_base_universe_d2_036_ibr_049_insider_silence_84}


def ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126(ibr_050_insider_buy_cluster_126):
    return _base_universe_d2(ibr_050_insider_buy_cluster_126, 37)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126'] = {'inputs': ['ibr_050_insider_buy_cluster_126'], 'func': ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126}


def ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189(ibr_051_insider_net_buy_ratio_189):
    return _base_universe_d2(ibr_051_insider_net_buy_ratio_189, 38)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189'] = {'inputs': ['ibr_051_insider_net_buy_ratio_189'], 'func': ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189}


def ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378(ibr_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(ibr_053_ceo_cfo_buy_weight_378, 39)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibr_053_ceo_cfo_buy_weight_378'], 'func': ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378}


def ibr_base_universe_d2_040_ibr_055_insider_conviction_756(ibr_055_insider_conviction_756):
    return _base_universe_d2(ibr_055_insider_conviction_756, 40)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_040_ibr_055_insider_conviction_756'] = {'inputs': ['ibr_055_insider_conviction_756'], 'func': ibr_base_universe_d2_040_ibr_055_insider_conviction_756}


def ibr_base_universe_d2_041_ibr_056_insider_silence_1008(ibr_056_insider_silence_1008):
    return _base_universe_d2(ibr_056_insider_silence_1008, 41)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_041_ibr_056_insider_silence_1008'] = {'inputs': ['ibr_056_insider_silence_1008'], 'func': ibr_base_universe_d2_041_ibr_056_insider_silence_1008}


def ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260(ibr_057_insider_buy_cluster_1260):
    return _base_universe_d2(ibr_057_insider_buy_cluster_1260, 42)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260'] = {'inputs': ['ibr_057_insider_buy_cluster_1260'], 'func': ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260}


def ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512(ibr_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(ibr_058_insider_net_buy_ratio_1512, 43)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibr_058_insider_net_buy_ratio_1512'], 'func': ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512}


def ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252(ibr_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(ibr_060_ceo_cfo_buy_weight_252, 44)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibr_060_ceo_cfo_buy_weight_252'], 'func': ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252}


def ibr_base_universe_d2_045_ibr_062_insider_conviction_42(ibr_062_insider_conviction_42):
    return _base_universe_d2(ibr_062_insider_conviction_42, 45)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_045_ibr_062_insider_conviction_42'] = {'inputs': ['ibr_062_insider_conviction_42'], 'func': ibr_base_universe_d2_045_ibr_062_insider_conviction_42}


def ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84(ibr_064_insider_buy_cluster_84):
    return _base_universe_d2(ibr_064_insider_buy_cluster_84, 46)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84'] = {'inputs': ['ibr_064_insider_buy_cluster_84'], 'func': ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84}


def ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126(ibr_065_insider_net_buy_ratio_126):
    return _base_universe_d2(ibr_065_insider_net_buy_ratio_126, 47)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126'] = {'inputs': ['ibr_065_insider_net_buy_ratio_126'], 'func': ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126}


def ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189(ibr_066_insider_value_ratio_189):
    return _base_universe_d2(ibr_066_insider_value_ratio_189, 48)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189'] = {'inputs': ['ibr_066_insider_value_ratio_189'], 'func': ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189}


def ibr_base_universe_d2_049_ibr_069_insider_conviction_504(ibr_069_insider_conviction_504):
    return _base_universe_d2(ibr_069_insider_conviction_504, 49)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_049_ibr_069_insider_conviction_504'] = {'inputs': ['ibr_069_insider_conviction_504'], 'func': ibr_base_universe_d2_049_ibr_069_insider_conviction_504}


def ibr_base_universe_d2_050_ibr_070_insider_silence_756(ibr_070_insider_silence_756):
    return _base_universe_d2(ibr_070_insider_silence_756, 50)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_050_ibr_070_insider_silence_756'] = {'inputs': ['ibr_070_insider_silence_756'], 'func': ibr_base_universe_d2_050_ibr_070_insider_silence_756}


def ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008(ibr_071_insider_buy_cluster_1008):
    return _base_universe_d2(ibr_071_insider_buy_cluster_1008, 51)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008'] = {'inputs': ['ibr_071_insider_buy_cluster_1008'], 'func': ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008}


def ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260(ibr_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(ibr_072_insider_net_buy_ratio_1260, 52)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibr_072_insider_net_buy_ratio_1260'], 'func': ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260}


def ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512(ibr_073_insider_value_ratio_1512):
    return _base_universe_d2(ibr_073_insider_value_ratio_1512, 53)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512'] = {'inputs': ['ibr_073_insider_value_ratio_1512'], 'func': ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512}


def ibr_base_universe_d2_054_ibr_basefill_005(ibr_basefill_005):
    return _base_universe_d2(ibr_basefill_005, 54)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_054_ibr_basefill_005'] = {'inputs': ['ibr_basefill_005'], 'func': ibr_base_universe_d2_054_ibr_basefill_005}


def ibr_base_universe_d2_055_ibr_basefill_012(ibr_basefill_012):
    return _base_universe_d2(ibr_basefill_012, 55)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_055_ibr_basefill_012'] = {'inputs': ['ibr_basefill_012'], 'func': ibr_base_universe_d2_055_ibr_basefill_012}


def ibr_base_universe_d2_056_ibr_basefill_019(ibr_basefill_019):
    return _base_universe_d2(ibr_basefill_019, 56)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_056_ibr_basefill_019'] = {'inputs': ['ibr_basefill_019'], 'func': ibr_base_universe_d2_056_ibr_basefill_019}


def ibr_base_universe_d2_057_ibr_basefill_022(ibr_basefill_022):
    return _base_universe_d2(ibr_basefill_022, 57)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_057_ibr_basefill_022'] = {'inputs': ['ibr_basefill_022'], 'func': ibr_base_universe_d2_057_ibr_basefill_022}


def ibr_base_universe_d2_058_ibr_basefill_026(ibr_basefill_026):
    return _base_universe_d2(ibr_basefill_026, 58)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_058_ibr_basefill_026'] = {'inputs': ['ibr_basefill_026'], 'func': ibr_base_universe_d2_058_ibr_basefill_026}


def ibr_base_universe_d2_059_ibr_basefill_033(ibr_basefill_033):
    return _base_universe_d2(ibr_basefill_033, 59)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_059_ibr_basefill_033'] = {'inputs': ['ibr_basefill_033'], 'func': ibr_base_universe_d2_059_ibr_basefill_033}


def ibr_base_universe_d2_060_ibr_basefill_037(ibr_basefill_037):
    return _base_universe_d2(ibr_basefill_037, 60)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_060_ibr_basefill_037'] = {'inputs': ['ibr_basefill_037'], 'func': ibr_base_universe_d2_060_ibr_basefill_037}


def ibr_base_universe_d2_061_ibr_basefill_040(ibr_basefill_040):
    return _base_universe_d2(ibr_basefill_040, 61)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_061_ibr_basefill_040'] = {'inputs': ['ibr_basefill_040'], 'func': ibr_base_universe_d2_061_ibr_basefill_040}


def ibr_base_universe_d2_062_ibr_basefill_047(ibr_basefill_047):
    return _base_universe_d2(ibr_basefill_047, 62)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_062_ibr_basefill_047'] = {'inputs': ['ibr_basefill_047'], 'func': ibr_base_universe_d2_062_ibr_basefill_047}


def ibr_base_universe_d2_063_ibr_basefill_052(ibr_basefill_052):
    return _base_universe_d2(ibr_basefill_052, 63)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_063_ibr_basefill_052'] = {'inputs': ['ibr_basefill_052'], 'func': ibr_base_universe_d2_063_ibr_basefill_052}


def ibr_base_universe_d2_064_ibr_basefill_054(ibr_basefill_054):
    return _base_universe_d2(ibr_basefill_054, 64)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_064_ibr_basefill_054'] = {'inputs': ['ibr_basefill_054'], 'func': ibr_base_universe_d2_064_ibr_basefill_054}


def ibr_base_universe_d2_065_ibr_basefill_059(ibr_basefill_059):
    return _base_universe_d2(ibr_basefill_059, 65)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_065_ibr_basefill_059'] = {'inputs': ['ibr_basefill_059'], 'func': ibr_base_universe_d2_065_ibr_basefill_059}


def ibr_base_universe_d2_066_ibr_basefill_061(ibr_basefill_061):
    return _base_universe_d2(ibr_basefill_061, 66)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_066_ibr_basefill_061'] = {'inputs': ['ibr_basefill_061'], 'func': ibr_base_universe_d2_066_ibr_basefill_061}


def ibr_base_universe_d2_067_ibr_basefill_063(ibr_basefill_063):
    return _base_universe_d2(ibr_basefill_063, 67)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_067_ibr_basefill_063'] = {'inputs': ['ibr_basefill_063'], 'func': ibr_base_universe_d2_067_ibr_basefill_063}


def ibr_base_universe_d2_068_ibr_basefill_067(ibr_basefill_067):
    return _base_universe_d2(ibr_basefill_067, 68)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_068_ibr_basefill_067'] = {'inputs': ['ibr_basefill_067'], 'func': ibr_base_universe_d2_068_ibr_basefill_067}


def ibr_base_universe_d2_069_ibr_basefill_068(ibr_basefill_068):
    return _base_universe_d2(ibr_basefill_068, 69)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_069_ibr_basefill_068'] = {'inputs': ['ibr_basefill_068'], 'func': ibr_base_universe_d2_069_ibr_basefill_068}


def ibr_base_universe_d2_070_ibr_basefill_074(ibr_basefill_074):
    return _base_universe_d2(ibr_basefill_074, 70)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_070_ibr_basefill_074'] = {'inputs': ['ibr_basefill_074'], 'func': ibr_base_universe_d2_070_ibr_basefill_074}


def ibr_base_universe_d2_071_ibr_basefill_075(ibr_basefill_075):
    return _base_universe_d2(ibr_basefill_075, 71)
IBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibr_base_universe_d2_071_ibr_basefill_075'] = {'inputs': ['ibr_basefill_075'], 'func': ibr_base_universe_d2_071_ibr_basefill_075}
