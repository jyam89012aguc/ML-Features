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



def ibc_151_ibc_001_insider_buy_cluster_21_roc_1(ibc_001_insider_buy_cluster_21):
    feature = _s(ibc_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def ibc_152_ibc_007_insider_silence_252_roc_42(ibc_007_insider_silence_252):
    feature = _s(ibc_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def ibc_153_ibc_013_insider_conviction_1512_roc_126(ibc_013_insider_conviction_1512):
    feature = _s(ibc_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def ibc_154_ibc_019_insider_activity_accel_1_roc_378(ibc_019_insider_activity_accel_1):
    feature = _s(ibc_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4(ibc_025_ceo_cfo_buy_weight_756):
    feature = _s(ibc_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_BUY_CLUSTER_REGISTRY_2ND_DERIVATIVES = {
    'ibc_151_ibc_001_insider_buy_cluster_21_roc_1': {'inputs': ['ibc_001_insider_buy_cluster_21'], 'func': ibc_151_ibc_001_insider_buy_cluster_21_roc_1},
    'ibc_152_ibc_007_insider_silence_252_roc_42': {'inputs': ['ibc_007_insider_silence_252'], 'func': ibc_152_ibc_007_insider_silence_252_roc_42},
    'ibc_153_ibc_013_insider_conviction_1512_roc_126': {'inputs': ['ibc_013_insider_conviction_1512'], 'func': ibc_153_ibc_013_insider_conviction_1512_roc_126},
    'ibc_154_ibc_019_insider_activity_accel_1_roc_378': {'inputs': ['ibc_019_insider_activity_accel_1'], 'func': ibc_154_ibc_019_insider_activity_accel_1_roc_378},
    'ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['ibc_025_ceo_cfo_buy_weight_756'], 'func': ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ibc_replacement_d2_001(ibc_019_insider_activity_accel_1):
    feature = _clean(ibc_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_001'] = {'inputs': ['ibc_019_insider_activity_accel_1'], 'func': ibc_replacement_d2_001}


def ibc_replacement_d2_002(ibc_replacement_001):
    feature = _clean(ibc_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_002'] = {'inputs': ['ibc_replacement_001'], 'func': ibc_replacement_d2_002}


def ibc_replacement_d2_003(ibc_replacement_002):
    feature = _clean(ibc_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_003'] = {'inputs': ['ibc_replacement_002'], 'func': ibc_replacement_d2_003}


def ibc_replacement_d2_004(ibc_replacement_003):
    feature = _clean(ibc_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_004'] = {'inputs': ['ibc_replacement_003'], 'func': ibc_replacement_d2_004}


def ibc_replacement_d2_005(ibc_replacement_004):
    feature = _clean(ibc_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_005'] = {'inputs': ['ibc_replacement_004'], 'func': ibc_replacement_d2_005}


def ibc_replacement_d2_006(ibc_replacement_005):
    feature = _clean(ibc_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_006'] = {'inputs': ['ibc_replacement_005'], 'func': ibc_replacement_d2_006}


def ibc_replacement_d2_007(ibc_replacement_006):
    feature = _clean(ibc_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_007'] = {'inputs': ['ibc_replacement_006'], 'func': ibc_replacement_d2_007}


def ibc_replacement_d2_008(ibc_replacement_007):
    feature = _clean(ibc_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_008'] = {'inputs': ['ibc_replacement_007'], 'func': ibc_replacement_d2_008}


def ibc_replacement_d2_009(ibc_replacement_008):
    feature = _clean(ibc_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_009'] = {'inputs': ['ibc_replacement_008'], 'func': ibc_replacement_d2_009}


def ibc_replacement_d2_010(ibc_replacement_009):
    feature = _clean(ibc_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_010'] = {'inputs': ['ibc_replacement_009'], 'func': ibc_replacement_d2_010}


def ibc_replacement_d2_011(ibc_replacement_010):
    feature = _clean(ibc_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_011'] = {'inputs': ['ibc_replacement_010'], 'func': ibc_replacement_d2_011}


def ibc_replacement_d2_012(ibc_replacement_011):
    feature = _clean(ibc_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_012'] = {'inputs': ['ibc_replacement_011'], 'func': ibc_replacement_d2_012}


def ibc_replacement_d2_013(ibc_replacement_012):
    feature = _clean(ibc_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_013'] = {'inputs': ['ibc_replacement_012'], 'func': ibc_replacement_d2_013}


def ibc_replacement_d2_014(ibc_replacement_013):
    feature = _clean(ibc_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_014'] = {'inputs': ['ibc_replacement_013'], 'func': ibc_replacement_d2_014}


def ibc_replacement_d2_015(ibc_replacement_014):
    feature = _clean(ibc_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_015'] = {'inputs': ['ibc_replacement_014'], 'func': ibc_replacement_d2_015}


def ibc_replacement_d2_016(ibc_replacement_015):
    feature = _clean(ibc_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_016'] = {'inputs': ['ibc_replacement_015'], 'func': ibc_replacement_d2_016}


def ibc_replacement_d2_017(ibc_replacement_016):
    feature = _clean(ibc_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_017'] = {'inputs': ['ibc_replacement_016'], 'func': ibc_replacement_d2_017}


def ibc_replacement_d2_018(ibc_replacement_017):
    feature = _clean(ibc_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_018'] = {'inputs': ['ibc_replacement_017'], 'func': ibc_replacement_d2_018}


def ibc_replacement_d2_019(ibc_replacement_018):
    feature = _clean(ibc_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_019'] = {'inputs': ['ibc_replacement_018'], 'func': ibc_replacement_d2_019}


def ibc_replacement_d2_020(ibc_replacement_019):
    feature = _clean(ibc_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_020'] = {'inputs': ['ibc_replacement_019'], 'func': ibc_replacement_d2_020}


def ibc_replacement_d2_021(ibc_replacement_020):
    feature = _clean(ibc_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_021'] = {'inputs': ['ibc_replacement_020'], 'func': ibc_replacement_d2_021}


def ibc_replacement_d2_022(ibc_replacement_021):
    feature = _clean(ibc_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_022'] = {'inputs': ['ibc_replacement_021'], 'func': ibc_replacement_d2_022}


def ibc_replacement_d2_023(ibc_replacement_022):
    feature = _clean(ibc_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_023'] = {'inputs': ['ibc_replacement_022'], 'func': ibc_replacement_d2_023}


def ibc_replacement_d2_024(ibc_replacement_023):
    feature = _clean(ibc_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_024'] = {'inputs': ['ibc_replacement_023'], 'func': ibc_replacement_d2_024}


def ibc_replacement_d2_025(ibc_replacement_024):
    feature = _clean(ibc_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_025'] = {'inputs': ['ibc_replacement_024'], 'func': ibc_replacement_d2_025}


def ibc_replacement_d2_026(ibc_replacement_025):
    feature = _clean(ibc_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_026'] = {'inputs': ['ibc_replacement_025'], 'func': ibc_replacement_d2_026}


def ibc_replacement_d2_027(ibc_replacement_026):
    feature = _clean(ibc_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_027'] = {'inputs': ['ibc_replacement_026'], 'func': ibc_replacement_d2_027}


def ibc_replacement_d2_028(ibc_replacement_027):
    feature = _clean(ibc_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_028'] = {'inputs': ['ibc_replacement_027'], 'func': ibc_replacement_d2_028}


def ibc_replacement_d2_029(ibc_replacement_028):
    feature = _clean(ibc_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_029'] = {'inputs': ['ibc_replacement_028'], 'func': ibc_replacement_d2_029}


def ibc_replacement_d2_030(ibc_replacement_029):
    feature = _clean(ibc_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_030'] = {'inputs': ['ibc_replacement_029'], 'func': ibc_replacement_d2_030}


def ibc_replacement_d2_031(ibc_replacement_030):
    feature = _clean(ibc_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_031'] = {'inputs': ['ibc_replacement_030'], 'func': ibc_replacement_d2_031}


def ibc_replacement_d2_032(ibc_replacement_031):
    feature = _clean(ibc_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_032'] = {'inputs': ['ibc_replacement_031'], 'func': ibc_replacement_d2_032}


def ibc_replacement_d2_033(ibc_replacement_032):
    feature = _clean(ibc_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_033'] = {'inputs': ['ibc_replacement_032'], 'func': ibc_replacement_d2_033}


def ibc_replacement_d2_034(ibc_replacement_033):
    feature = _clean(ibc_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_034'] = {'inputs': ['ibc_replacement_033'], 'func': ibc_replacement_d2_034}


def ibc_replacement_d2_035(ibc_replacement_034):
    feature = _clean(ibc_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_035'] = {'inputs': ['ibc_replacement_034'], 'func': ibc_replacement_d2_035}


def ibc_replacement_d2_036(ibc_replacement_035):
    feature = _clean(ibc_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_036'] = {'inputs': ['ibc_replacement_035'], 'func': ibc_replacement_d2_036}


def ibc_replacement_d2_037(ibc_replacement_036):
    feature = _clean(ibc_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_037'] = {'inputs': ['ibc_replacement_036'], 'func': ibc_replacement_d2_037}


def ibc_replacement_d2_038(ibc_replacement_037):
    feature = _clean(ibc_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_038'] = {'inputs': ['ibc_replacement_037'], 'func': ibc_replacement_d2_038}


def ibc_replacement_d2_039(ibc_replacement_038):
    feature = _clean(ibc_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_039'] = {'inputs': ['ibc_replacement_038'], 'func': ibc_replacement_d2_039}


def ibc_replacement_d2_040(ibc_replacement_039):
    feature = _clean(ibc_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_040'] = {'inputs': ['ibc_replacement_039'], 'func': ibc_replacement_d2_040}


def ibc_replacement_d2_041(ibc_replacement_040):
    feature = _clean(ibc_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_041'] = {'inputs': ['ibc_replacement_040'], 'func': ibc_replacement_d2_041}


def ibc_replacement_d2_042(ibc_replacement_041):
    feature = _clean(ibc_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_042'] = {'inputs': ['ibc_replacement_041'], 'func': ibc_replacement_d2_042}


def ibc_replacement_d2_043(ibc_replacement_042):
    feature = _clean(ibc_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_043'] = {'inputs': ['ibc_replacement_042'], 'func': ibc_replacement_d2_043}


def ibc_replacement_d2_044(ibc_replacement_043):
    feature = _clean(ibc_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_044'] = {'inputs': ['ibc_replacement_043'], 'func': ibc_replacement_d2_044}


def ibc_replacement_d2_045(ibc_replacement_044):
    feature = _clean(ibc_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_045'] = {'inputs': ['ibc_replacement_044'], 'func': ibc_replacement_d2_045}


def ibc_replacement_d2_046(ibc_replacement_045):
    feature = _clean(ibc_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_046'] = {'inputs': ['ibc_replacement_045'], 'func': ibc_replacement_d2_046}


def ibc_replacement_d2_047(ibc_replacement_046):
    feature = _clean(ibc_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_047'] = {'inputs': ['ibc_replacement_046'], 'func': ibc_replacement_d2_047}


def ibc_replacement_d2_048(ibc_replacement_047):
    feature = _clean(ibc_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_048'] = {'inputs': ['ibc_replacement_047'], 'func': ibc_replacement_d2_048}


def ibc_replacement_d2_049(ibc_replacement_048):
    feature = _clean(ibc_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_049'] = {'inputs': ['ibc_replacement_048'], 'func': ibc_replacement_d2_049}


def ibc_replacement_d2_050(ibc_replacement_049):
    feature = _clean(ibc_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_050'] = {'inputs': ['ibc_replacement_049'], 'func': ibc_replacement_d2_050}


def ibc_replacement_d2_051(ibc_replacement_050):
    feature = _clean(ibc_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_051'] = {'inputs': ['ibc_replacement_050'], 'func': ibc_replacement_d2_051}


def ibc_replacement_d2_052(ibc_replacement_051):
    feature = _clean(ibc_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_052'] = {'inputs': ['ibc_replacement_051'], 'func': ibc_replacement_d2_052}


def ibc_replacement_d2_053(ibc_replacement_052):
    feature = _clean(ibc_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_053'] = {'inputs': ['ibc_replacement_052'], 'func': ibc_replacement_d2_053}


def ibc_replacement_d2_054(ibc_replacement_053):
    feature = _clean(ibc_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_054'] = {'inputs': ['ibc_replacement_053'], 'func': ibc_replacement_d2_054}


def ibc_replacement_d2_055(ibc_replacement_054):
    feature = _clean(ibc_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_055'] = {'inputs': ['ibc_replacement_054'], 'func': ibc_replacement_d2_055}


def ibc_replacement_d2_056(ibc_replacement_055):
    feature = _clean(ibc_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_056'] = {'inputs': ['ibc_replacement_055'], 'func': ibc_replacement_d2_056}


def ibc_replacement_d2_057(ibc_replacement_056):
    feature = _clean(ibc_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_057'] = {'inputs': ['ibc_replacement_056'], 'func': ibc_replacement_d2_057}


def ibc_replacement_d2_058(ibc_replacement_057):
    feature = _clean(ibc_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_058'] = {'inputs': ['ibc_replacement_057'], 'func': ibc_replacement_d2_058}


def ibc_replacement_d2_059(ibc_replacement_058):
    feature = _clean(ibc_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_059'] = {'inputs': ['ibc_replacement_058'], 'func': ibc_replacement_d2_059}


def ibc_replacement_d2_060(ibc_replacement_059):
    feature = _clean(ibc_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_060'] = {'inputs': ['ibc_replacement_059'], 'func': ibc_replacement_d2_060}


def ibc_replacement_d2_061(ibc_replacement_060):
    feature = _clean(ibc_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_061'] = {'inputs': ['ibc_replacement_060'], 'func': ibc_replacement_d2_061}


def ibc_replacement_d2_062(ibc_replacement_061):
    feature = _clean(ibc_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_062'] = {'inputs': ['ibc_replacement_061'], 'func': ibc_replacement_d2_062}


def ibc_replacement_d2_063(ibc_replacement_062):
    feature = _clean(ibc_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_063'] = {'inputs': ['ibc_replacement_062'], 'func': ibc_replacement_d2_063}


def ibc_replacement_d2_064(ibc_replacement_063):
    feature = _clean(ibc_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_064'] = {'inputs': ['ibc_replacement_063'], 'func': ibc_replacement_d2_064}


def ibc_replacement_d2_065(ibc_replacement_064):
    feature = _clean(ibc_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_065'] = {'inputs': ['ibc_replacement_064'], 'func': ibc_replacement_d2_065}


def ibc_replacement_d2_066(ibc_replacement_065):
    feature = _clean(ibc_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_066'] = {'inputs': ['ibc_replacement_065'], 'func': ibc_replacement_d2_066}


def ibc_replacement_d2_067(ibc_replacement_066):
    feature = _clean(ibc_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_067'] = {'inputs': ['ibc_replacement_066'], 'func': ibc_replacement_d2_067}


def ibc_replacement_d2_068(ibc_replacement_067):
    feature = _clean(ibc_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_068'] = {'inputs': ['ibc_replacement_067'], 'func': ibc_replacement_d2_068}


def ibc_replacement_d2_069(ibc_replacement_068):
    feature = _clean(ibc_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_069'] = {'inputs': ['ibc_replacement_068'], 'func': ibc_replacement_d2_069}


def ibc_replacement_d2_070(ibc_replacement_069):
    feature = _clean(ibc_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_070'] = {'inputs': ['ibc_replacement_069'], 'func': ibc_replacement_d2_070}


def ibc_replacement_d2_071(ibc_replacement_070):
    feature = _clean(ibc_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_071'] = {'inputs': ['ibc_replacement_070'], 'func': ibc_replacement_d2_071}


def ibc_replacement_d2_072(ibc_replacement_071):
    feature = _clean(ibc_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_072'] = {'inputs': ['ibc_replacement_071'], 'func': ibc_replacement_d2_072}


def ibc_replacement_d2_073(ibc_replacement_072):
    feature = _clean(ibc_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_073'] = {'inputs': ['ibc_replacement_072'], 'func': ibc_replacement_d2_073}


def ibc_replacement_d2_074(ibc_replacement_073):
    feature = _clean(ibc_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_074'] = {'inputs': ['ibc_replacement_073'], 'func': ibc_replacement_d2_074}


def ibc_replacement_d2_075(ibc_replacement_074):
    feature = _clean(ibc_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_075'] = {'inputs': ['ibc_replacement_074'], 'func': ibc_replacement_d2_075}


def ibc_replacement_d2_076(ibc_replacement_075):
    feature = _clean(ibc_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_076'] = {'inputs': ['ibc_replacement_075'], 'func': ibc_replacement_d2_076}


def ibc_replacement_d2_077(ibc_replacement_076):
    feature = _clean(ibc_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_077'] = {'inputs': ['ibc_replacement_076'], 'func': ibc_replacement_d2_077}


def ibc_replacement_d2_078(ibc_replacement_077):
    feature = _clean(ibc_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_078'] = {'inputs': ['ibc_replacement_077'], 'func': ibc_replacement_d2_078}


def ibc_replacement_d2_079(ibc_replacement_078):
    feature = _clean(ibc_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_079'] = {'inputs': ['ibc_replacement_078'], 'func': ibc_replacement_d2_079}


def ibc_replacement_d2_080(ibc_replacement_079):
    feature = _clean(ibc_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_080'] = {'inputs': ['ibc_replacement_079'], 'func': ibc_replacement_d2_080}


def ibc_replacement_d2_081(ibc_replacement_080):
    feature = _clean(ibc_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_081'] = {'inputs': ['ibc_replacement_080'], 'func': ibc_replacement_d2_081}


def ibc_replacement_d2_082(ibc_replacement_081):
    feature = _clean(ibc_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_082'] = {'inputs': ['ibc_replacement_081'], 'func': ibc_replacement_d2_082}


def ibc_replacement_d2_083(ibc_replacement_082):
    feature = _clean(ibc_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_083'] = {'inputs': ['ibc_replacement_082'], 'func': ibc_replacement_d2_083}


def ibc_replacement_d2_084(ibc_replacement_083):
    feature = _clean(ibc_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_084'] = {'inputs': ['ibc_replacement_083'], 'func': ibc_replacement_d2_084}


def ibc_replacement_d2_085(ibc_replacement_084):
    feature = _clean(ibc_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_085'] = {'inputs': ['ibc_replacement_084'], 'func': ibc_replacement_d2_085}


def ibc_replacement_d2_086(ibc_replacement_085):
    feature = _clean(ibc_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_086'] = {'inputs': ['ibc_replacement_085'], 'func': ibc_replacement_d2_086}


def ibc_replacement_d2_087(ibc_replacement_086):
    feature = _clean(ibc_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_087'] = {'inputs': ['ibc_replacement_086'], 'func': ibc_replacement_d2_087}


def ibc_replacement_d2_088(ibc_replacement_087):
    feature = _clean(ibc_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_088'] = {'inputs': ['ibc_replacement_087'], 'func': ibc_replacement_d2_088}


def ibc_replacement_d2_089(ibc_replacement_088):
    feature = _clean(ibc_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_089'] = {'inputs': ['ibc_replacement_088'], 'func': ibc_replacement_d2_089}


def ibc_replacement_d2_090(ibc_replacement_089):
    feature = _clean(ibc_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_090'] = {'inputs': ['ibc_replacement_089'], 'func': ibc_replacement_d2_090}


def ibc_replacement_d2_091(ibc_replacement_090):
    feature = _clean(ibc_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_091'] = {'inputs': ['ibc_replacement_090'], 'func': ibc_replacement_d2_091}


def ibc_replacement_d2_092(ibc_replacement_091):
    feature = _clean(ibc_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_092'] = {'inputs': ['ibc_replacement_091'], 'func': ibc_replacement_d2_092}


def ibc_replacement_d2_093(ibc_replacement_092):
    feature = _clean(ibc_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_093'] = {'inputs': ['ibc_replacement_092'], 'func': ibc_replacement_d2_093}


def ibc_replacement_d2_094(ibc_replacement_093):
    feature = _clean(ibc_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_094'] = {'inputs': ['ibc_replacement_093'], 'func': ibc_replacement_d2_094}


def ibc_replacement_d2_095(ibc_replacement_094):
    feature = _clean(ibc_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_095'] = {'inputs': ['ibc_replacement_094'], 'func': ibc_replacement_d2_095}


def ibc_replacement_d2_096(ibc_replacement_095):
    feature = _clean(ibc_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_096'] = {'inputs': ['ibc_replacement_095'], 'func': ibc_replacement_d2_096}


def ibc_replacement_d2_097(ibc_replacement_096):
    feature = _clean(ibc_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_097'] = {'inputs': ['ibc_replacement_096'], 'func': ibc_replacement_d2_097}


def ibc_replacement_d2_098(ibc_replacement_097):
    feature = _clean(ibc_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_098'] = {'inputs': ['ibc_replacement_097'], 'func': ibc_replacement_d2_098}


def ibc_replacement_d2_099(ibc_replacement_098):
    feature = _clean(ibc_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_099'] = {'inputs': ['ibc_replacement_098'], 'func': ibc_replacement_d2_099}


def ibc_replacement_d2_100(ibc_replacement_099):
    feature = _clean(ibc_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_100'] = {'inputs': ['ibc_replacement_099'], 'func': ibc_replacement_d2_100}


def ibc_replacement_d2_101(ibc_replacement_100):
    feature = _clean(ibc_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_101'] = {'inputs': ['ibc_replacement_100'], 'func': ibc_replacement_d2_101}


def ibc_replacement_d2_102(ibc_replacement_101):
    feature = _clean(ibc_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_102'] = {'inputs': ['ibc_replacement_101'], 'func': ibc_replacement_d2_102}


def ibc_replacement_d2_103(ibc_replacement_102):
    feature = _clean(ibc_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_103'] = {'inputs': ['ibc_replacement_102'], 'func': ibc_replacement_d2_103}


def ibc_replacement_d2_104(ibc_replacement_103):
    feature = _clean(ibc_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_104'] = {'inputs': ['ibc_replacement_103'], 'func': ibc_replacement_d2_104}


def ibc_replacement_d2_105(ibc_replacement_104):
    feature = _clean(ibc_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_105'] = {'inputs': ['ibc_replacement_104'], 'func': ibc_replacement_d2_105}


def ibc_replacement_d2_106(ibc_replacement_105):
    feature = _clean(ibc_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_106'] = {'inputs': ['ibc_replacement_105'], 'func': ibc_replacement_d2_106}


def ibc_replacement_d2_107(ibc_replacement_106):
    feature = _clean(ibc_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_107'] = {'inputs': ['ibc_replacement_106'], 'func': ibc_replacement_d2_107}


def ibc_replacement_d2_108(ibc_replacement_107):
    feature = _clean(ibc_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_108'] = {'inputs': ['ibc_replacement_107'], 'func': ibc_replacement_d2_108}


def ibc_replacement_d2_109(ibc_replacement_108):
    feature = _clean(ibc_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_109'] = {'inputs': ['ibc_replacement_108'], 'func': ibc_replacement_d2_109}


def ibc_replacement_d2_110(ibc_replacement_109):
    feature = _clean(ibc_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_110'] = {'inputs': ['ibc_replacement_109'], 'func': ibc_replacement_d2_110}


def ibc_replacement_d2_111(ibc_replacement_110):
    feature = _clean(ibc_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_111'] = {'inputs': ['ibc_replacement_110'], 'func': ibc_replacement_d2_111}


def ibc_replacement_d2_112(ibc_replacement_111):
    feature = _clean(ibc_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IBC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibc_replacement_d2_112'] = {'inputs': ['ibc_replacement_111'], 'func': ibc_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42(ibc_002_insider_net_buy_ratio_42):
    return _base_universe_d2(ibc_002_insider_net_buy_ratio_42, 1)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42'] = {'inputs': ['ibc_002_insider_net_buy_ratio_42'], 'func': ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42}


def ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63(ibc_003_insider_value_ratio_63):
    return _base_universe_d2(ibc_003_insider_value_ratio_63, 2)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63'] = {'inputs': ['ibc_003_insider_value_ratio_63'], 'func': ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63}


def ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84(ibc_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(ibc_004_ceo_cfo_buy_weight_84, 3)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibc_004_ceo_cfo_buy_weight_84'], 'func': ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84}


def ibc_base_universe_d2_004_ibc_006_insider_conviction_189(ibc_006_insider_conviction_189):
    return _base_universe_d2(ibc_006_insider_conviction_189, 4)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_004_ibc_006_insider_conviction_189'] = {'inputs': ['ibc_006_insider_conviction_189'], 'func': ibc_base_universe_d2_004_ibc_006_insider_conviction_189}


def ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378(ibc_008_insider_buy_cluster_378):
    return _base_universe_d2(ibc_008_insider_buy_cluster_378, 5)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378'] = {'inputs': ['ibc_008_insider_buy_cluster_378'], 'func': ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378}


def ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504(ibc_009_insider_net_buy_ratio_504):
    return _base_universe_d2(ibc_009_insider_net_buy_ratio_504, 6)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504'] = {'inputs': ['ibc_009_insider_net_buy_ratio_504'], 'func': ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504}


def ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756(ibc_010_insider_value_ratio_756):
    return _base_universe_d2(ibc_010_insider_value_ratio_756, 7)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756'] = {'inputs': ['ibc_010_insider_value_ratio_756'], 'func': ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756}


def ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008(ibc_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(ibc_011_ceo_cfo_buy_weight_1008, 8)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibc_011_ceo_cfo_buy_weight_1008'], 'func': ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008}


def ibc_base_universe_d2_009_ibc_014_insider_silence_63(ibc_014_insider_silence_63):
    return _base_universe_d2(ibc_014_insider_silence_63, 9)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_009_ibc_014_insider_silence_63'] = {'inputs': ['ibc_014_insider_silence_63'], 'func': ibc_base_universe_d2_009_ibc_014_insider_silence_63}


def ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252(ibc_015_insider_buy_cluster_252):
    return _base_universe_d2(ibc_015_insider_buy_cluster_252, 10)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252'] = {'inputs': ['ibc_015_insider_buy_cluster_252'], 'func': ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252}


def ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21(ibc_016_insider_net_buy_ratio_21):
    return _base_universe_d2(ibc_016_insider_net_buy_ratio_21, 11)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21'] = {'inputs': ['ibc_016_insider_net_buy_ratio_21'], 'func': ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21}


def ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42(ibc_017_insider_value_ratio_42):
    return _base_universe_d2(ibc_017_insider_value_ratio_42, 12)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42'] = {'inputs': ['ibc_017_insider_value_ratio_42'], 'func': ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42}


def ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63(ibc_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(ibc_018_ceo_cfo_buy_weight_63, 13)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibc_018_ceo_cfo_buy_weight_63'], 'func': ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63}


def ibc_base_universe_d2_014_ibc_020_insider_conviction_126(ibc_020_insider_conviction_126):
    return _base_universe_d2(ibc_020_insider_conviction_126, 14)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_014_ibc_020_insider_conviction_126'] = {'inputs': ['ibc_020_insider_conviction_126'], 'func': ibc_base_universe_d2_014_ibc_020_insider_conviction_126}


def ibc_base_universe_d2_015_ibc_021_insider_silence_189(ibc_021_insider_silence_189):
    return _base_universe_d2(ibc_021_insider_silence_189, 15)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_015_ibc_021_insider_silence_189'] = {'inputs': ['ibc_021_insider_silence_189'], 'func': ibc_base_universe_d2_015_ibc_021_insider_silence_189}


def ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378(ibc_023_insider_net_buy_ratio_378):
    return _base_universe_d2(ibc_023_insider_net_buy_ratio_378, 16)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378'] = {'inputs': ['ibc_023_insider_net_buy_ratio_378'], 'func': ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378}


def ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504(ibc_024_insider_value_ratio_504):
    return _base_universe_d2(ibc_024_insider_value_ratio_504, 17)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504'] = {'inputs': ['ibc_024_insider_value_ratio_504'], 'func': ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504}


def ibc_base_universe_d2_018_ibc_027_insider_conviction_1260(ibc_027_insider_conviction_1260):
    return _base_universe_d2(ibc_027_insider_conviction_1260, 18)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_018_ibc_027_insider_conviction_1260'] = {'inputs': ['ibc_027_insider_conviction_1260'], 'func': ibc_base_universe_d2_018_ibc_027_insider_conviction_1260}


def ibc_base_universe_d2_019_ibc_028_insider_silence_1512(ibc_028_insider_silence_1512):
    return _base_universe_d2(ibc_028_insider_silence_1512, 19)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_019_ibc_028_insider_silence_1512'] = {'inputs': ['ibc_028_insider_silence_1512'], 'func': ibc_base_universe_d2_019_ibc_028_insider_silence_1512}


def ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63(ibc_029_insider_buy_cluster_63):
    return _base_universe_d2(ibc_029_insider_buy_cluster_63, 20)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63'] = {'inputs': ['ibc_029_insider_buy_cluster_63'], 'func': ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63}


def ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252(ibc_030_insider_net_buy_ratio_252):
    return _base_universe_d2(ibc_030_insider_net_buy_ratio_252, 21)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252'] = {'inputs': ['ibc_030_insider_net_buy_ratio_252'], 'func': ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252}


def ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21(ibc_031_insider_value_ratio_21):
    return _base_universe_d2(ibc_031_insider_value_ratio_21, 22)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21'] = {'inputs': ['ibc_031_insider_value_ratio_21'], 'func': ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21}


def ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42(ibc_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(ibc_032_ceo_cfo_buy_weight_42, 23)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibc_032_ceo_cfo_buy_weight_42'], 'func': ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42}


def ibc_base_universe_d2_024_ibc_034_insider_conviction_84(ibc_034_insider_conviction_84):
    return _base_universe_d2(ibc_034_insider_conviction_84, 24)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_024_ibc_034_insider_conviction_84'] = {'inputs': ['ibc_034_insider_conviction_84'], 'func': ibc_base_universe_d2_024_ibc_034_insider_conviction_84}


def ibc_base_universe_d2_025_ibc_035_insider_silence_126(ibc_035_insider_silence_126):
    return _base_universe_d2(ibc_035_insider_silence_126, 25)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_025_ibc_035_insider_silence_126'] = {'inputs': ['ibc_035_insider_silence_126'], 'func': ibc_base_universe_d2_025_ibc_035_insider_silence_126}


def ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189(ibc_036_insider_buy_cluster_189):
    return _base_universe_d2(ibc_036_insider_buy_cluster_189, 26)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189'] = {'inputs': ['ibc_036_insider_buy_cluster_189'], 'func': ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189}


def ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378(ibc_038_insider_value_ratio_378):
    return _base_universe_d2(ibc_038_insider_value_ratio_378, 27)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378'] = {'inputs': ['ibc_038_insider_value_ratio_378'], 'func': ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378}


def ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504(ibc_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(ibc_039_ceo_cfo_buy_weight_504, 28)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibc_039_ceo_cfo_buy_weight_504'], 'func': ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504}


def ibc_base_universe_d2_029_ibc_041_insider_conviction_1008(ibc_041_insider_conviction_1008):
    return _base_universe_d2(ibc_041_insider_conviction_1008, 29)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_029_ibc_041_insider_conviction_1008'] = {'inputs': ['ibc_041_insider_conviction_1008'], 'func': ibc_base_universe_d2_029_ibc_041_insider_conviction_1008}


def ibc_base_universe_d2_030_ibc_042_insider_silence_1260(ibc_042_insider_silence_1260):
    return _base_universe_d2(ibc_042_insider_silence_1260, 30)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_030_ibc_042_insider_silence_1260'] = {'inputs': ['ibc_042_insider_silence_1260'], 'func': ibc_base_universe_d2_030_ibc_042_insider_silence_1260}


def ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512(ibc_043_insider_buy_cluster_1512):
    return _base_universe_d2(ibc_043_insider_buy_cluster_1512, 31)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512'] = {'inputs': ['ibc_043_insider_buy_cluster_1512'], 'func': ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512}


def ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63(ibc_044_insider_net_buy_ratio_63):
    return _base_universe_d2(ibc_044_insider_net_buy_ratio_63, 32)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63'] = {'inputs': ['ibc_044_insider_net_buy_ratio_63'], 'func': ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63}


def ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252(ibc_045_insider_value_ratio_252):
    return _base_universe_d2(ibc_045_insider_value_ratio_252, 33)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252'] = {'inputs': ['ibc_045_insider_value_ratio_252'], 'func': ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252}


def ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21(ibc_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(ibc_046_ceo_cfo_buy_weight_21, 34)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibc_046_ceo_cfo_buy_weight_21'], 'func': ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21}


def ibc_base_universe_d2_035_ibc_048_insider_conviction_63(ibc_048_insider_conviction_63):
    return _base_universe_d2(ibc_048_insider_conviction_63, 35)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_035_ibc_048_insider_conviction_63'] = {'inputs': ['ibc_048_insider_conviction_63'], 'func': ibc_base_universe_d2_035_ibc_048_insider_conviction_63}


def ibc_base_universe_d2_036_ibc_049_insider_silence_84(ibc_049_insider_silence_84):
    return _base_universe_d2(ibc_049_insider_silence_84, 36)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_036_ibc_049_insider_silence_84'] = {'inputs': ['ibc_049_insider_silence_84'], 'func': ibc_base_universe_d2_036_ibc_049_insider_silence_84}


def ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126(ibc_050_insider_buy_cluster_126):
    return _base_universe_d2(ibc_050_insider_buy_cluster_126, 37)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126'] = {'inputs': ['ibc_050_insider_buy_cluster_126'], 'func': ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126}


def ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189(ibc_051_insider_net_buy_ratio_189):
    return _base_universe_d2(ibc_051_insider_net_buy_ratio_189, 38)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189'] = {'inputs': ['ibc_051_insider_net_buy_ratio_189'], 'func': ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189}


def ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378(ibc_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(ibc_053_ceo_cfo_buy_weight_378, 39)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibc_053_ceo_cfo_buy_weight_378'], 'func': ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378}


def ibc_base_universe_d2_040_ibc_055_insider_conviction_756(ibc_055_insider_conviction_756):
    return _base_universe_d2(ibc_055_insider_conviction_756, 40)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_040_ibc_055_insider_conviction_756'] = {'inputs': ['ibc_055_insider_conviction_756'], 'func': ibc_base_universe_d2_040_ibc_055_insider_conviction_756}


def ibc_base_universe_d2_041_ibc_056_insider_silence_1008(ibc_056_insider_silence_1008):
    return _base_universe_d2(ibc_056_insider_silence_1008, 41)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_041_ibc_056_insider_silence_1008'] = {'inputs': ['ibc_056_insider_silence_1008'], 'func': ibc_base_universe_d2_041_ibc_056_insider_silence_1008}


def ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260(ibc_057_insider_buy_cluster_1260):
    return _base_universe_d2(ibc_057_insider_buy_cluster_1260, 42)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260'] = {'inputs': ['ibc_057_insider_buy_cluster_1260'], 'func': ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260}


def ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512(ibc_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(ibc_058_insider_net_buy_ratio_1512, 43)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibc_058_insider_net_buy_ratio_1512'], 'func': ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512}


def ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252(ibc_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(ibc_060_ceo_cfo_buy_weight_252, 44)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibc_060_ceo_cfo_buy_weight_252'], 'func': ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252}


def ibc_base_universe_d2_045_ibc_062_insider_conviction_42(ibc_062_insider_conviction_42):
    return _base_universe_d2(ibc_062_insider_conviction_42, 45)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_045_ibc_062_insider_conviction_42'] = {'inputs': ['ibc_062_insider_conviction_42'], 'func': ibc_base_universe_d2_045_ibc_062_insider_conviction_42}


def ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84(ibc_064_insider_buy_cluster_84):
    return _base_universe_d2(ibc_064_insider_buy_cluster_84, 46)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84'] = {'inputs': ['ibc_064_insider_buy_cluster_84'], 'func': ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84}


def ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126(ibc_065_insider_net_buy_ratio_126):
    return _base_universe_d2(ibc_065_insider_net_buy_ratio_126, 47)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126'] = {'inputs': ['ibc_065_insider_net_buy_ratio_126'], 'func': ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126}


def ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189(ibc_066_insider_value_ratio_189):
    return _base_universe_d2(ibc_066_insider_value_ratio_189, 48)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189'] = {'inputs': ['ibc_066_insider_value_ratio_189'], 'func': ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189}


def ibc_base_universe_d2_049_ibc_069_insider_conviction_504(ibc_069_insider_conviction_504):
    return _base_universe_d2(ibc_069_insider_conviction_504, 49)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_049_ibc_069_insider_conviction_504'] = {'inputs': ['ibc_069_insider_conviction_504'], 'func': ibc_base_universe_d2_049_ibc_069_insider_conviction_504}


def ibc_base_universe_d2_050_ibc_070_insider_silence_756(ibc_070_insider_silence_756):
    return _base_universe_d2(ibc_070_insider_silence_756, 50)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_050_ibc_070_insider_silence_756'] = {'inputs': ['ibc_070_insider_silence_756'], 'func': ibc_base_universe_d2_050_ibc_070_insider_silence_756}


def ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008(ibc_071_insider_buy_cluster_1008):
    return _base_universe_d2(ibc_071_insider_buy_cluster_1008, 51)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008'] = {'inputs': ['ibc_071_insider_buy_cluster_1008'], 'func': ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008}


def ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260(ibc_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(ibc_072_insider_net_buy_ratio_1260, 52)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibc_072_insider_net_buy_ratio_1260'], 'func': ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260}


def ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512(ibc_073_insider_value_ratio_1512):
    return _base_universe_d2(ibc_073_insider_value_ratio_1512, 53)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512'] = {'inputs': ['ibc_073_insider_value_ratio_1512'], 'func': ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512}


def ibc_base_universe_d2_054_ibc_basefill_005(ibc_basefill_005):
    return _base_universe_d2(ibc_basefill_005, 54)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_054_ibc_basefill_005'] = {'inputs': ['ibc_basefill_005'], 'func': ibc_base_universe_d2_054_ibc_basefill_005}


def ibc_base_universe_d2_055_ibc_basefill_012(ibc_basefill_012):
    return _base_universe_d2(ibc_basefill_012, 55)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_055_ibc_basefill_012'] = {'inputs': ['ibc_basefill_012'], 'func': ibc_base_universe_d2_055_ibc_basefill_012}


def ibc_base_universe_d2_056_ibc_basefill_019(ibc_basefill_019):
    return _base_universe_d2(ibc_basefill_019, 56)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_056_ibc_basefill_019'] = {'inputs': ['ibc_basefill_019'], 'func': ibc_base_universe_d2_056_ibc_basefill_019}


def ibc_base_universe_d2_057_ibc_basefill_022(ibc_basefill_022):
    return _base_universe_d2(ibc_basefill_022, 57)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_057_ibc_basefill_022'] = {'inputs': ['ibc_basefill_022'], 'func': ibc_base_universe_d2_057_ibc_basefill_022}


def ibc_base_universe_d2_058_ibc_basefill_026(ibc_basefill_026):
    return _base_universe_d2(ibc_basefill_026, 58)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_058_ibc_basefill_026'] = {'inputs': ['ibc_basefill_026'], 'func': ibc_base_universe_d2_058_ibc_basefill_026}


def ibc_base_universe_d2_059_ibc_basefill_033(ibc_basefill_033):
    return _base_universe_d2(ibc_basefill_033, 59)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_059_ibc_basefill_033'] = {'inputs': ['ibc_basefill_033'], 'func': ibc_base_universe_d2_059_ibc_basefill_033}


def ibc_base_universe_d2_060_ibc_basefill_037(ibc_basefill_037):
    return _base_universe_d2(ibc_basefill_037, 60)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_060_ibc_basefill_037'] = {'inputs': ['ibc_basefill_037'], 'func': ibc_base_universe_d2_060_ibc_basefill_037}


def ibc_base_universe_d2_061_ibc_basefill_040(ibc_basefill_040):
    return _base_universe_d2(ibc_basefill_040, 61)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_061_ibc_basefill_040'] = {'inputs': ['ibc_basefill_040'], 'func': ibc_base_universe_d2_061_ibc_basefill_040}


def ibc_base_universe_d2_062_ibc_basefill_047(ibc_basefill_047):
    return _base_universe_d2(ibc_basefill_047, 62)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_062_ibc_basefill_047'] = {'inputs': ['ibc_basefill_047'], 'func': ibc_base_universe_d2_062_ibc_basefill_047}


def ibc_base_universe_d2_063_ibc_basefill_052(ibc_basefill_052):
    return _base_universe_d2(ibc_basefill_052, 63)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_063_ibc_basefill_052'] = {'inputs': ['ibc_basefill_052'], 'func': ibc_base_universe_d2_063_ibc_basefill_052}


def ibc_base_universe_d2_064_ibc_basefill_054(ibc_basefill_054):
    return _base_universe_d2(ibc_basefill_054, 64)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_064_ibc_basefill_054'] = {'inputs': ['ibc_basefill_054'], 'func': ibc_base_universe_d2_064_ibc_basefill_054}


def ibc_base_universe_d2_065_ibc_basefill_059(ibc_basefill_059):
    return _base_universe_d2(ibc_basefill_059, 65)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_065_ibc_basefill_059'] = {'inputs': ['ibc_basefill_059'], 'func': ibc_base_universe_d2_065_ibc_basefill_059}


def ibc_base_universe_d2_066_ibc_basefill_061(ibc_basefill_061):
    return _base_universe_d2(ibc_basefill_061, 66)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_066_ibc_basefill_061'] = {'inputs': ['ibc_basefill_061'], 'func': ibc_base_universe_d2_066_ibc_basefill_061}


def ibc_base_universe_d2_067_ibc_basefill_063(ibc_basefill_063):
    return _base_universe_d2(ibc_basefill_063, 67)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_067_ibc_basefill_063'] = {'inputs': ['ibc_basefill_063'], 'func': ibc_base_universe_d2_067_ibc_basefill_063}


def ibc_base_universe_d2_068_ibc_basefill_067(ibc_basefill_067):
    return _base_universe_d2(ibc_basefill_067, 68)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_068_ibc_basefill_067'] = {'inputs': ['ibc_basefill_067'], 'func': ibc_base_universe_d2_068_ibc_basefill_067}


def ibc_base_universe_d2_069_ibc_basefill_068(ibc_basefill_068):
    return _base_universe_d2(ibc_basefill_068, 69)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_069_ibc_basefill_068'] = {'inputs': ['ibc_basefill_068'], 'func': ibc_base_universe_d2_069_ibc_basefill_068}


def ibc_base_universe_d2_070_ibc_basefill_074(ibc_basefill_074):
    return _base_universe_d2(ibc_basefill_074, 70)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_070_ibc_basefill_074'] = {'inputs': ['ibc_basefill_074'], 'func': ibc_base_universe_d2_070_ibc_basefill_074}


def ibc_base_universe_d2_071_ibc_basefill_075(ibc_basefill_075):
    return _base_universe_d2(ibc_basefill_075, 71)
IBC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibc_base_universe_d2_071_ibc_basefill_075'] = {'inputs': ['ibc_basefill_075'], 'func': ibc_base_universe_d2_071_ibc_basefill_075}
