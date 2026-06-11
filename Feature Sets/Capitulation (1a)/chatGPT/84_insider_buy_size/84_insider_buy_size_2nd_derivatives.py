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



def ibs_151_ibs_001_insider_buy_cluster_21_roc_1(ibs_001_insider_buy_cluster_21):
    feature = _s(ibs_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def ibs_152_ibs_007_insider_silence_252_roc_42(ibs_007_insider_silence_252):
    feature = _s(ibs_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def ibs_153_ibs_013_insider_conviction_1512_roc_126(ibs_013_insider_conviction_1512):
    feature = _s(ibs_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def ibs_154_ibs_019_insider_activity_accel_1_roc_378(ibs_019_insider_activity_accel_1):
    feature = _s(ibs_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4(ibs_025_ceo_cfo_buy_weight_756):
    feature = _s(ibs_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_BUY_SIZE_REGISTRY_2ND_DERIVATIVES = {
    'ibs_151_ibs_001_insider_buy_cluster_21_roc_1': {'inputs': ['ibs_001_insider_buy_cluster_21'], 'func': ibs_151_ibs_001_insider_buy_cluster_21_roc_1},
    'ibs_152_ibs_007_insider_silence_252_roc_42': {'inputs': ['ibs_007_insider_silence_252'], 'func': ibs_152_ibs_007_insider_silence_252_roc_42},
    'ibs_153_ibs_013_insider_conviction_1512_roc_126': {'inputs': ['ibs_013_insider_conviction_1512'], 'func': ibs_153_ibs_013_insider_conviction_1512_roc_126},
    'ibs_154_ibs_019_insider_activity_accel_1_roc_378': {'inputs': ['ibs_019_insider_activity_accel_1'], 'func': ibs_154_ibs_019_insider_activity_accel_1_roc_378},
    'ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['ibs_025_ceo_cfo_buy_weight_756'], 'func': ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ibs_replacement_d2_001(ibs_019_insider_activity_accel_1):
    feature = _clean(ibs_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_001'] = {'inputs': ['ibs_019_insider_activity_accel_1'], 'func': ibs_replacement_d2_001}


def ibs_replacement_d2_002(ibs_replacement_001):
    feature = _clean(ibs_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_002'] = {'inputs': ['ibs_replacement_001'], 'func': ibs_replacement_d2_002}


def ibs_replacement_d2_003(ibs_replacement_002):
    feature = _clean(ibs_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_003'] = {'inputs': ['ibs_replacement_002'], 'func': ibs_replacement_d2_003}


def ibs_replacement_d2_004(ibs_replacement_003):
    feature = _clean(ibs_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_004'] = {'inputs': ['ibs_replacement_003'], 'func': ibs_replacement_d2_004}


def ibs_replacement_d2_005(ibs_replacement_004):
    feature = _clean(ibs_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_005'] = {'inputs': ['ibs_replacement_004'], 'func': ibs_replacement_d2_005}


def ibs_replacement_d2_006(ibs_replacement_005):
    feature = _clean(ibs_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_006'] = {'inputs': ['ibs_replacement_005'], 'func': ibs_replacement_d2_006}


def ibs_replacement_d2_007(ibs_replacement_006):
    feature = _clean(ibs_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_007'] = {'inputs': ['ibs_replacement_006'], 'func': ibs_replacement_d2_007}


def ibs_replacement_d2_008(ibs_replacement_007):
    feature = _clean(ibs_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_008'] = {'inputs': ['ibs_replacement_007'], 'func': ibs_replacement_d2_008}


def ibs_replacement_d2_009(ibs_replacement_008):
    feature = _clean(ibs_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_009'] = {'inputs': ['ibs_replacement_008'], 'func': ibs_replacement_d2_009}


def ibs_replacement_d2_010(ibs_replacement_009):
    feature = _clean(ibs_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_010'] = {'inputs': ['ibs_replacement_009'], 'func': ibs_replacement_d2_010}


def ibs_replacement_d2_011(ibs_replacement_010):
    feature = _clean(ibs_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_011'] = {'inputs': ['ibs_replacement_010'], 'func': ibs_replacement_d2_011}


def ibs_replacement_d2_012(ibs_replacement_011):
    feature = _clean(ibs_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_012'] = {'inputs': ['ibs_replacement_011'], 'func': ibs_replacement_d2_012}


def ibs_replacement_d2_013(ibs_replacement_012):
    feature = _clean(ibs_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_013'] = {'inputs': ['ibs_replacement_012'], 'func': ibs_replacement_d2_013}


def ibs_replacement_d2_014(ibs_replacement_013):
    feature = _clean(ibs_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_014'] = {'inputs': ['ibs_replacement_013'], 'func': ibs_replacement_d2_014}


def ibs_replacement_d2_015(ibs_replacement_014):
    feature = _clean(ibs_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_015'] = {'inputs': ['ibs_replacement_014'], 'func': ibs_replacement_d2_015}


def ibs_replacement_d2_016(ibs_replacement_015):
    feature = _clean(ibs_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_016'] = {'inputs': ['ibs_replacement_015'], 'func': ibs_replacement_d2_016}


def ibs_replacement_d2_017(ibs_replacement_016):
    feature = _clean(ibs_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_017'] = {'inputs': ['ibs_replacement_016'], 'func': ibs_replacement_d2_017}


def ibs_replacement_d2_018(ibs_replacement_017):
    feature = _clean(ibs_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_018'] = {'inputs': ['ibs_replacement_017'], 'func': ibs_replacement_d2_018}


def ibs_replacement_d2_019(ibs_replacement_018):
    feature = _clean(ibs_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_019'] = {'inputs': ['ibs_replacement_018'], 'func': ibs_replacement_d2_019}


def ibs_replacement_d2_020(ibs_replacement_019):
    feature = _clean(ibs_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_020'] = {'inputs': ['ibs_replacement_019'], 'func': ibs_replacement_d2_020}


def ibs_replacement_d2_021(ibs_replacement_020):
    feature = _clean(ibs_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_021'] = {'inputs': ['ibs_replacement_020'], 'func': ibs_replacement_d2_021}


def ibs_replacement_d2_022(ibs_replacement_021):
    feature = _clean(ibs_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_022'] = {'inputs': ['ibs_replacement_021'], 'func': ibs_replacement_d2_022}


def ibs_replacement_d2_023(ibs_replacement_022):
    feature = _clean(ibs_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_023'] = {'inputs': ['ibs_replacement_022'], 'func': ibs_replacement_d2_023}


def ibs_replacement_d2_024(ibs_replacement_023):
    feature = _clean(ibs_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_024'] = {'inputs': ['ibs_replacement_023'], 'func': ibs_replacement_d2_024}


def ibs_replacement_d2_025(ibs_replacement_024):
    feature = _clean(ibs_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_025'] = {'inputs': ['ibs_replacement_024'], 'func': ibs_replacement_d2_025}


def ibs_replacement_d2_026(ibs_replacement_025):
    feature = _clean(ibs_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_026'] = {'inputs': ['ibs_replacement_025'], 'func': ibs_replacement_d2_026}


def ibs_replacement_d2_027(ibs_replacement_026):
    feature = _clean(ibs_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_027'] = {'inputs': ['ibs_replacement_026'], 'func': ibs_replacement_d2_027}


def ibs_replacement_d2_028(ibs_replacement_027):
    feature = _clean(ibs_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_028'] = {'inputs': ['ibs_replacement_027'], 'func': ibs_replacement_d2_028}


def ibs_replacement_d2_029(ibs_replacement_028):
    feature = _clean(ibs_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_029'] = {'inputs': ['ibs_replacement_028'], 'func': ibs_replacement_d2_029}


def ibs_replacement_d2_030(ibs_replacement_029):
    feature = _clean(ibs_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_030'] = {'inputs': ['ibs_replacement_029'], 'func': ibs_replacement_d2_030}


def ibs_replacement_d2_031(ibs_replacement_030):
    feature = _clean(ibs_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_031'] = {'inputs': ['ibs_replacement_030'], 'func': ibs_replacement_d2_031}


def ibs_replacement_d2_032(ibs_replacement_031):
    feature = _clean(ibs_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_032'] = {'inputs': ['ibs_replacement_031'], 'func': ibs_replacement_d2_032}


def ibs_replacement_d2_033(ibs_replacement_032):
    feature = _clean(ibs_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_033'] = {'inputs': ['ibs_replacement_032'], 'func': ibs_replacement_d2_033}


def ibs_replacement_d2_034(ibs_replacement_033):
    feature = _clean(ibs_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_034'] = {'inputs': ['ibs_replacement_033'], 'func': ibs_replacement_d2_034}


def ibs_replacement_d2_035(ibs_replacement_034):
    feature = _clean(ibs_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_035'] = {'inputs': ['ibs_replacement_034'], 'func': ibs_replacement_d2_035}


def ibs_replacement_d2_036(ibs_replacement_035):
    feature = _clean(ibs_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_036'] = {'inputs': ['ibs_replacement_035'], 'func': ibs_replacement_d2_036}


def ibs_replacement_d2_037(ibs_replacement_036):
    feature = _clean(ibs_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_037'] = {'inputs': ['ibs_replacement_036'], 'func': ibs_replacement_d2_037}


def ibs_replacement_d2_038(ibs_replacement_037):
    feature = _clean(ibs_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_038'] = {'inputs': ['ibs_replacement_037'], 'func': ibs_replacement_d2_038}


def ibs_replacement_d2_039(ibs_replacement_038):
    feature = _clean(ibs_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_039'] = {'inputs': ['ibs_replacement_038'], 'func': ibs_replacement_d2_039}


def ibs_replacement_d2_040(ibs_replacement_039):
    feature = _clean(ibs_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_040'] = {'inputs': ['ibs_replacement_039'], 'func': ibs_replacement_d2_040}


def ibs_replacement_d2_041(ibs_replacement_040):
    feature = _clean(ibs_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_041'] = {'inputs': ['ibs_replacement_040'], 'func': ibs_replacement_d2_041}


def ibs_replacement_d2_042(ibs_replacement_041):
    feature = _clean(ibs_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_042'] = {'inputs': ['ibs_replacement_041'], 'func': ibs_replacement_d2_042}


def ibs_replacement_d2_043(ibs_replacement_042):
    feature = _clean(ibs_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_043'] = {'inputs': ['ibs_replacement_042'], 'func': ibs_replacement_d2_043}


def ibs_replacement_d2_044(ibs_replacement_043):
    feature = _clean(ibs_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_044'] = {'inputs': ['ibs_replacement_043'], 'func': ibs_replacement_d2_044}


def ibs_replacement_d2_045(ibs_replacement_044):
    feature = _clean(ibs_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_045'] = {'inputs': ['ibs_replacement_044'], 'func': ibs_replacement_d2_045}


def ibs_replacement_d2_046(ibs_replacement_045):
    feature = _clean(ibs_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_046'] = {'inputs': ['ibs_replacement_045'], 'func': ibs_replacement_d2_046}


def ibs_replacement_d2_047(ibs_replacement_046):
    feature = _clean(ibs_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_047'] = {'inputs': ['ibs_replacement_046'], 'func': ibs_replacement_d2_047}


def ibs_replacement_d2_048(ibs_replacement_047):
    feature = _clean(ibs_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_048'] = {'inputs': ['ibs_replacement_047'], 'func': ibs_replacement_d2_048}


def ibs_replacement_d2_049(ibs_replacement_048):
    feature = _clean(ibs_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_049'] = {'inputs': ['ibs_replacement_048'], 'func': ibs_replacement_d2_049}


def ibs_replacement_d2_050(ibs_replacement_049):
    feature = _clean(ibs_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_050'] = {'inputs': ['ibs_replacement_049'], 'func': ibs_replacement_d2_050}


def ibs_replacement_d2_051(ibs_replacement_050):
    feature = _clean(ibs_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_051'] = {'inputs': ['ibs_replacement_050'], 'func': ibs_replacement_d2_051}


def ibs_replacement_d2_052(ibs_replacement_051):
    feature = _clean(ibs_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_052'] = {'inputs': ['ibs_replacement_051'], 'func': ibs_replacement_d2_052}


def ibs_replacement_d2_053(ibs_replacement_052):
    feature = _clean(ibs_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_053'] = {'inputs': ['ibs_replacement_052'], 'func': ibs_replacement_d2_053}


def ibs_replacement_d2_054(ibs_replacement_053):
    feature = _clean(ibs_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_054'] = {'inputs': ['ibs_replacement_053'], 'func': ibs_replacement_d2_054}


def ibs_replacement_d2_055(ibs_replacement_054):
    feature = _clean(ibs_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_055'] = {'inputs': ['ibs_replacement_054'], 'func': ibs_replacement_d2_055}


def ibs_replacement_d2_056(ibs_replacement_055):
    feature = _clean(ibs_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_056'] = {'inputs': ['ibs_replacement_055'], 'func': ibs_replacement_d2_056}


def ibs_replacement_d2_057(ibs_replacement_056):
    feature = _clean(ibs_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_057'] = {'inputs': ['ibs_replacement_056'], 'func': ibs_replacement_d2_057}


def ibs_replacement_d2_058(ibs_replacement_057):
    feature = _clean(ibs_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_058'] = {'inputs': ['ibs_replacement_057'], 'func': ibs_replacement_d2_058}


def ibs_replacement_d2_059(ibs_replacement_058):
    feature = _clean(ibs_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_059'] = {'inputs': ['ibs_replacement_058'], 'func': ibs_replacement_d2_059}


def ibs_replacement_d2_060(ibs_replacement_059):
    feature = _clean(ibs_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_060'] = {'inputs': ['ibs_replacement_059'], 'func': ibs_replacement_d2_060}


def ibs_replacement_d2_061(ibs_replacement_060):
    feature = _clean(ibs_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_061'] = {'inputs': ['ibs_replacement_060'], 'func': ibs_replacement_d2_061}


def ibs_replacement_d2_062(ibs_replacement_061):
    feature = _clean(ibs_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_062'] = {'inputs': ['ibs_replacement_061'], 'func': ibs_replacement_d2_062}


def ibs_replacement_d2_063(ibs_replacement_062):
    feature = _clean(ibs_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_063'] = {'inputs': ['ibs_replacement_062'], 'func': ibs_replacement_d2_063}


def ibs_replacement_d2_064(ibs_replacement_063):
    feature = _clean(ibs_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_064'] = {'inputs': ['ibs_replacement_063'], 'func': ibs_replacement_d2_064}


def ibs_replacement_d2_065(ibs_replacement_064):
    feature = _clean(ibs_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_065'] = {'inputs': ['ibs_replacement_064'], 'func': ibs_replacement_d2_065}


def ibs_replacement_d2_066(ibs_replacement_065):
    feature = _clean(ibs_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_066'] = {'inputs': ['ibs_replacement_065'], 'func': ibs_replacement_d2_066}


def ibs_replacement_d2_067(ibs_replacement_066):
    feature = _clean(ibs_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_067'] = {'inputs': ['ibs_replacement_066'], 'func': ibs_replacement_d2_067}


def ibs_replacement_d2_068(ibs_replacement_067):
    feature = _clean(ibs_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_068'] = {'inputs': ['ibs_replacement_067'], 'func': ibs_replacement_d2_068}


def ibs_replacement_d2_069(ibs_replacement_068):
    feature = _clean(ibs_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_069'] = {'inputs': ['ibs_replacement_068'], 'func': ibs_replacement_d2_069}


def ibs_replacement_d2_070(ibs_replacement_069):
    feature = _clean(ibs_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_070'] = {'inputs': ['ibs_replacement_069'], 'func': ibs_replacement_d2_070}


def ibs_replacement_d2_071(ibs_replacement_070):
    feature = _clean(ibs_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_071'] = {'inputs': ['ibs_replacement_070'], 'func': ibs_replacement_d2_071}


def ibs_replacement_d2_072(ibs_replacement_071):
    feature = _clean(ibs_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_072'] = {'inputs': ['ibs_replacement_071'], 'func': ibs_replacement_d2_072}


def ibs_replacement_d2_073(ibs_replacement_072):
    feature = _clean(ibs_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_073'] = {'inputs': ['ibs_replacement_072'], 'func': ibs_replacement_d2_073}


def ibs_replacement_d2_074(ibs_replacement_073):
    feature = _clean(ibs_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_074'] = {'inputs': ['ibs_replacement_073'], 'func': ibs_replacement_d2_074}


def ibs_replacement_d2_075(ibs_replacement_074):
    feature = _clean(ibs_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_075'] = {'inputs': ['ibs_replacement_074'], 'func': ibs_replacement_d2_075}


def ibs_replacement_d2_076(ibs_replacement_075):
    feature = _clean(ibs_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_076'] = {'inputs': ['ibs_replacement_075'], 'func': ibs_replacement_d2_076}


def ibs_replacement_d2_077(ibs_replacement_076):
    feature = _clean(ibs_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_077'] = {'inputs': ['ibs_replacement_076'], 'func': ibs_replacement_d2_077}


def ibs_replacement_d2_078(ibs_replacement_077):
    feature = _clean(ibs_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_078'] = {'inputs': ['ibs_replacement_077'], 'func': ibs_replacement_d2_078}


def ibs_replacement_d2_079(ibs_replacement_078):
    feature = _clean(ibs_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_079'] = {'inputs': ['ibs_replacement_078'], 'func': ibs_replacement_d2_079}


def ibs_replacement_d2_080(ibs_replacement_079):
    feature = _clean(ibs_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_080'] = {'inputs': ['ibs_replacement_079'], 'func': ibs_replacement_d2_080}


def ibs_replacement_d2_081(ibs_replacement_080):
    feature = _clean(ibs_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_081'] = {'inputs': ['ibs_replacement_080'], 'func': ibs_replacement_d2_081}


def ibs_replacement_d2_082(ibs_replacement_081):
    feature = _clean(ibs_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_082'] = {'inputs': ['ibs_replacement_081'], 'func': ibs_replacement_d2_082}


def ibs_replacement_d2_083(ibs_replacement_082):
    feature = _clean(ibs_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_083'] = {'inputs': ['ibs_replacement_082'], 'func': ibs_replacement_d2_083}


def ibs_replacement_d2_084(ibs_replacement_083):
    feature = _clean(ibs_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_084'] = {'inputs': ['ibs_replacement_083'], 'func': ibs_replacement_d2_084}


def ibs_replacement_d2_085(ibs_replacement_084):
    feature = _clean(ibs_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_085'] = {'inputs': ['ibs_replacement_084'], 'func': ibs_replacement_d2_085}


def ibs_replacement_d2_086(ibs_replacement_085):
    feature = _clean(ibs_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_086'] = {'inputs': ['ibs_replacement_085'], 'func': ibs_replacement_d2_086}


def ibs_replacement_d2_087(ibs_replacement_086):
    feature = _clean(ibs_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_087'] = {'inputs': ['ibs_replacement_086'], 'func': ibs_replacement_d2_087}


def ibs_replacement_d2_088(ibs_replacement_087):
    feature = _clean(ibs_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_088'] = {'inputs': ['ibs_replacement_087'], 'func': ibs_replacement_d2_088}


def ibs_replacement_d2_089(ibs_replacement_088):
    feature = _clean(ibs_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_089'] = {'inputs': ['ibs_replacement_088'], 'func': ibs_replacement_d2_089}


def ibs_replacement_d2_090(ibs_replacement_089):
    feature = _clean(ibs_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_090'] = {'inputs': ['ibs_replacement_089'], 'func': ibs_replacement_d2_090}


def ibs_replacement_d2_091(ibs_replacement_090):
    feature = _clean(ibs_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_091'] = {'inputs': ['ibs_replacement_090'], 'func': ibs_replacement_d2_091}


def ibs_replacement_d2_092(ibs_replacement_091):
    feature = _clean(ibs_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_092'] = {'inputs': ['ibs_replacement_091'], 'func': ibs_replacement_d2_092}


def ibs_replacement_d2_093(ibs_replacement_092):
    feature = _clean(ibs_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_093'] = {'inputs': ['ibs_replacement_092'], 'func': ibs_replacement_d2_093}


def ibs_replacement_d2_094(ibs_replacement_093):
    feature = _clean(ibs_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_094'] = {'inputs': ['ibs_replacement_093'], 'func': ibs_replacement_d2_094}


def ibs_replacement_d2_095(ibs_replacement_094):
    feature = _clean(ibs_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_095'] = {'inputs': ['ibs_replacement_094'], 'func': ibs_replacement_d2_095}


def ibs_replacement_d2_096(ibs_replacement_095):
    feature = _clean(ibs_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_096'] = {'inputs': ['ibs_replacement_095'], 'func': ibs_replacement_d2_096}


def ibs_replacement_d2_097(ibs_replacement_096):
    feature = _clean(ibs_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_097'] = {'inputs': ['ibs_replacement_096'], 'func': ibs_replacement_d2_097}


def ibs_replacement_d2_098(ibs_replacement_097):
    feature = _clean(ibs_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_098'] = {'inputs': ['ibs_replacement_097'], 'func': ibs_replacement_d2_098}


def ibs_replacement_d2_099(ibs_replacement_098):
    feature = _clean(ibs_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_099'] = {'inputs': ['ibs_replacement_098'], 'func': ibs_replacement_d2_099}


def ibs_replacement_d2_100(ibs_replacement_099):
    feature = _clean(ibs_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_100'] = {'inputs': ['ibs_replacement_099'], 'func': ibs_replacement_d2_100}


def ibs_replacement_d2_101(ibs_replacement_100):
    feature = _clean(ibs_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_101'] = {'inputs': ['ibs_replacement_100'], 'func': ibs_replacement_d2_101}


def ibs_replacement_d2_102(ibs_replacement_101):
    feature = _clean(ibs_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_102'] = {'inputs': ['ibs_replacement_101'], 'func': ibs_replacement_d2_102}


def ibs_replacement_d2_103(ibs_replacement_102):
    feature = _clean(ibs_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_103'] = {'inputs': ['ibs_replacement_102'], 'func': ibs_replacement_d2_103}


def ibs_replacement_d2_104(ibs_replacement_103):
    feature = _clean(ibs_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_104'] = {'inputs': ['ibs_replacement_103'], 'func': ibs_replacement_d2_104}


def ibs_replacement_d2_105(ibs_replacement_104):
    feature = _clean(ibs_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_105'] = {'inputs': ['ibs_replacement_104'], 'func': ibs_replacement_d2_105}


def ibs_replacement_d2_106(ibs_replacement_105):
    feature = _clean(ibs_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_106'] = {'inputs': ['ibs_replacement_105'], 'func': ibs_replacement_d2_106}


def ibs_replacement_d2_107(ibs_replacement_106):
    feature = _clean(ibs_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_107'] = {'inputs': ['ibs_replacement_106'], 'func': ibs_replacement_d2_107}


def ibs_replacement_d2_108(ibs_replacement_107):
    feature = _clean(ibs_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_108'] = {'inputs': ['ibs_replacement_107'], 'func': ibs_replacement_d2_108}


def ibs_replacement_d2_109(ibs_replacement_108):
    feature = _clean(ibs_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_109'] = {'inputs': ['ibs_replacement_108'], 'func': ibs_replacement_d2_109}


def ibs_replacement_d2_110(ibs_replacement_109):
    feature = _clean(ibs_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_110'] = {'inputs': ['ibs_replacement_109'], 'func': ibs_replacement_d2_110}


def ibs_replacement_d2_111(ibs_replacement_110):
    feature = _clean(ibs_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_111'] = {'inputs': ['ibs_replacement_110'], 'func': ibs_replacement_d2_111}


def ibs_replacement_d2_112(ibs_replacement_111):
    feature = _clean(ibs_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ibs_replacement_d2_112'] = {'inputs': ['ibs_replacement_111'], 'func': ibs_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42(ibs_002_insider_net_buy_ratio_42):
    return _base_universe_d2(ibs_002_insider_net_buy_ratio_42, 1)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42'] = {'inputs': ['ibs_002_insider_net_buy_ratio_42'], 'func': ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42}


def ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63(ibs_003_insider_value_ratio_63):
    return _base_universe_d2(ibs_003_insider_value_ratio_63, 2)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63'] = {'inputs': ['ibs_003_insider_value_ratio_63'], 'func': ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63}


def ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84(ibs_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(ibs_004_ceo_cfo_buy_weight_84, 3)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibs_004_ceo_cfo_buy_weight_84'], 'func': ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84}


def ibs_base_universe_d2_004_ibs_006_insider_conviction_189(ibs_006_insider_conviction_189):
    return _base_universe_d2(ibs_006_insider_conviction_189, 4)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_004_ibs_006_insider_conviction_189'] = {'inputs': ['ibs_006_insider_conviction_189'], 'func': ibs_base_universe_d2_004_ibs_006_insider_conviction_189}


def ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378(ibs_008_insider_buy_cluster_378):
    return _base_universe_d2(ibs_008_insider_buy_cluster_378, 5)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378'] = {'inputs': ['ibs_008_insider_buy_cluster_378'], 'func': ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378}


def ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504(ibs_009_insider_net_buy_ratio_504):
    return _base_universe_d2(ibs_009_insider_net_buy_ratio_504, 6)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504'] = {'inputs': ['ibs_009_insider_net_buy_ratio_504'], 'func': ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504}


def ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756(ibs_010_insider_value_ratio_756):
    return _base_universe_d2(ibs_010_insider_value_ratio_756, 7)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756'] = {'inputs': ['ibs_010_insider_value_ratio_756'], 'func': ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756}


def ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008(ibs_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(ibs_011_ceo_cfo_buy_weight_1008, 8)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibs_011_ceo_cfo_buy_weight_1008'], 'func': ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008}


def ibs_base_universe_d2_009_ibs_014_insider_silence_63(ibs_014_insider_silence_63):
    return _base_universe_d2(ibs_014_insider_silence_63, 9)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_009_ibs_014_insider_silence_63'] = {'inputs': ['ibs_014_insider_silence_63'], 'func': ibs_base_universe_d2_009_ibs_014_insider_silence_63}


def ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252(ibs_015_insider_buy_cluster_252):
    return _base_universe_d2(ibs_015_insider_buy_cluster_252, 10)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252'] = {'inputs': ['ibs_015_insider_buy_cluster_252'], 'func': ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252}


def ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21(ibs_016_insider_net_buy_ratio_21):
    return _base_universe_d2(ibs_016_insider_net_buy_ratio_21, 11)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21'] = {'inputs': ['ibs_016_insider_net_buy_ratio_21'], 'func': ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21}


def ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42(ibs_017_insider_value_ratio_42):
    return _base_universe_d2(ibs_017_insider_value_ratio_42, 12)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42'] = {'inputs': ['ibs_017_insider_value_ratio_42'], 'func': ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42}


def ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63(ibs_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(ibs_018_ceo_cfo_buy_weight_63, 13)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibs_018_ceo_cfo_buy_weight_63'], 'func': ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63}


def ibs_base_universe_d2_014_ibs_020_insider_conviction_126(ibs_020_insider_conviction_126):
    return _base_universe_d2(ibs_020_insider_conviction_126, 14)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_014_ibs_020_insider_conviction_126'] = {'inputs': ['ibs_020_insider_conviction_126'], 'func': ibs_base_universe_d2_014_ibs_020_insider_conviction_126}


def ibs_base_universe_d2_015_ibs_021_insider_silence_189(ibs_021_insider_silence_189):
    return _base_universe_d2(ibs_021_insider_silence_189, 15)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_015_ibs_021_insider_silence_189'] = {'inputs': ['ibs_021_insider_silence_189'], 'func': ibs_base_universe_d2_015_ibs_021_insider_silence_189}


def ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378(ibs_023_insider_net_buy_ratio_378):
    return _base_universe_d2(ibs_023_insider_net_buy_ratio_378, 16)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378'] = {'inputs': ['ibs_023_insider_net_buy_ratio_378'], 'func': ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378}


def ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504(ibs_024_insider_value_ratio_504):
    return _base_universe_d2(ibs_024_insider_value_ratio_504, 17)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504'] = {'inputs': ['ibs_024_insider_value_ratio_504'], 'func': ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504}


def ibs_base_universe_d2_018_ibs_027_insider_conviction_1260(ibs_027_insider_conviction_1260):
    return _base_universe_d2(ibs_027_insider_conviction_1260, 18)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_018_ibs_027_insider_conviction_1260'] = {'inputs': ['ibs_027_insider_conviction_1260'], 'func': ibs_base_universe_d2_018_ibs_027_insider_conviction_1260}


def ibs_base_universe_d2_019_ibs_028_insider_silence_1512(ibs_028_insider_silence_1512):
    return _base_universe_d2(ibs_028_insider_silence_1512, 19)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_019_ibs_028_insider_silence_1512'] = {'inputs': ['ibs_028_insider_silence_1512'], 'func': ibs_base_universe_d2_019_ibs_028_insider_silence_1512}


def ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63(ibs_029_insider_buy_cluster_63):
    return _base_universe_d2(ibs_029_insider_buy_cluster_63, 20)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63'] = {'inputs': ['ibs_029_insider_buy_cluster_63'], 'func': ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63}


def ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252(ibs_030_insider_net_buy_ratio_252):
    return _base_universe_d2(ibs_030_insider_net_buy_ratio_252, 21)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252'] = {'inputs': ['ibs_030_insider_net_buy_ratio_252'], 'func': ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252}


def ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21(ibs_031_insider_value_ratio_21):
    return _base_universe_d2(ibs_031_insider_value_ratio_21, 22)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21'] = {'inputs': ['ibs_031_insider_value_ratio_21'], 'func': ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21}


def ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42(ibs_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(ibs_032_ceo_cfo_buy_weight_42, 23)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibs_032_ceo_cfo_buy_weight_42'], 'func': ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42}


def ibs_base_universe_d2_024_ibs_034_insider_conviction_84(ibs_034_insider_conviction_84):
    return _base_universe_d2(ibs_034_insider_conviction_84, 24)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_024_ibs_034_insider_conviction_84'] = {'inputs': ['ibs_034_insider_conviction_84'], 'func': ibs_base_universe_d2_024_ibs_034_insider_conviction_84}


def ibs_base_universe_d2_025_ibs_035_insider_silence_126(ibs_035_insider_silence_126):
    return _base_universe_d2(ibs_035_insider_silence_126, 25)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_025_ibs_035_insider_silence_126'] = {'inputs': ['ibs_035_insider_silence_126'], 'func': ibs_base_universe_d2_025_ibs_035_insider_silence_126}


def ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189(ibs_036_insider_buy_cluster_189):
    return _base_universe_d2(ibs_036_insider_buy_cluster_189, 26)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189'] = {'inputs': ['ibs_036_insider_buy_cluster_189'], 'func': ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189}


def ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378(ibs_038_insider_value_ratio_378):
    return _base_universe_d2(ibs_038_insider_value_ratio_378, 27)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378'] = {'inputs': ['ibs_038_insider_value_ratio_378'], 'func': ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378}


def ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504(ibs_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(ibs_039_ceo_cfo_buy_weight_504, 28)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibs_039_ceo_cfo_buy_weight_504'], 'func': ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504}


def ibs_base_universe_d2_029_ibs_041_insider_conviction_1008(ibs_041_insider_conviction_1008):
    return _base_universe_d2(ibs_041_insider_conviction_1008, 29)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_029_ibs_041_insider_conviction_1008'] = {'inputs': ['ibs_041_insider_conviction_1008'], 'func': ibs_base_universe_d2_029_ibs_041_insider_conviction_1008}


def ibs_base_universe_d2_030_ibs_042_insider_silence_1260(ibs_042_insider_silence_1260):
    return _base_universe_d2(ibs_042_insider_silence_1260, 30)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_030_ibs_042_insider_silence_1260'] = {'inputs': ['ibs_042_insider_silence_1260'], 'func': ibs_base_universe_d2_030_ibs_042_insider_silence_1260}


def ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512(ibs_043_insider_buy_cluster_1512):
    return _base_universe_d2(ibs_043_insider_buy_cluster_1512, 31)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512'] = {'inputs': ['ibs_043_insider_buy_cluster_1512'], 'func': ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512}


def ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63(ibs_044_insider_net_buy_ratio_63):
    return _base_universe_d2(ibs_044_insider_net_buy_ratio_63, 32)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63'] = {'inputs': ['ibs_044_insider_net_buy_ratio_63'], 'func': ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63}


def ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252(ibs_045_insider_value_ratio_252):
    return _base_universe_d2(ibs_045_insider_value_ratio_252, 33)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252'] = {'inputs': ['ibs_045_insider_value_ratio_252'], 'func': ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252}


def ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21(ibs_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(ibs_046_ceo_cfo_buy_weight_21, 34)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibs_046_ceo_cfo_buy_weight_21'], 'func': ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21}


def ibs_base_universe_d2_035_ibs_048_insider_conviction_63(ibs_048_insider_conviction_63):
    return _base_universe_d2(ibs_048_insider_conviction_63, 35)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_035_ibs_048_insider_conviction_63'] = {'inputs': ['ibs_048_insider_conviction_63'], 'func': ibs_base_universe_d2_035_ibs_048_insider_conviction_63}


def ibs_base_universe_d2_036_ibs_049_insider_silence_84(ibs_049_insider_silence_84):
    return _base_universe_d2(ibs_049_insider_silence_84, 36)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_036_ibs_049_insider_silence_84'] = {'inputs': ['ibs_049_insider_silence_84'], 'func': ibs_base_universe_d2_036_ibs_049_insider_silence_84}


def ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126(ibs_050_insider_buy_cluster_126):
    return _base_universe_d2(ibs_050_insider_buy_cluster_126, 37)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126'] = {'inputs': ['ibs_050_insider_buy_cluster_126'], 'func': ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126}


def ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189(ibs_051_insider_net_buy_ratio_189):
    return _base_universe_d2(ibs_051_insider_net_buy_ratio_189, 38)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189'] = {'inputs': ['ibs_051_insider_net_buy_ratio_189'], 'func': ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189}


def ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378(ibs_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(ibs_053_ceo_cfo_buy_weight_378, 39)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibs_053_ceo_cfo_buy_weight_378'], 'func': ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378}


def ibs_base_universe_d2_040_ibs_055_insider_conviction_756(ibs_055_insider_conviction_756):
    return _base_universe_d2(ibs_055_insider_conviction_756, 40)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_040_ibs_055_insider_conviction_756'] = {'inputs': ['ibs_055_insider_conviction_756'], 'func': ibs_base_universe_d2_040_ibs_055_insider_conviction_756}


def ibs_base_universe_d2_041_ibs_056_insider_silence_1008(ibs_056_insider_silence_1008):
    return _base_universe_d2(ibs_056_insider_silence_1008, 41)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_041_ibs_056_insider_silence_1008'] = {'inputs': ['ibs_056_insider_silence_1008'], 'func': ibs_base_universe_d2_041_ibs_056_insider_silence_1008}


def ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260(ibs_057_insider_buy_cluster_1260):
    return _base_universe_d2(ibs_057_insider_buy_cluster_1260, 42)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260'] = {'inputs': ['ibs_057_insider_buy_cluster_1260'], 'func': ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260}


def ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512(ibs_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(ibs_058_insider_net_buy_ratio_1512, 43)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibs_058_insider_net_buy_ratio_1512'], 'func': ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512}


def ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252(ibs_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(ibs_060_ceo_cfo_buy_weight_252, 44)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibs_060_ceo_cfo_buy_weight_252'], 'func': ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252}


def ibs_base_universe_d2_045_ibs_062_insider_conviction_42(ibs_062_insider_conviction_42):
    return _base_universe_d2(ibs_062_insider_conviction_42, 45)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_045_ibs_062_insider_conviction_42'] = {'inputs': ['ibs_062_insider_conviction_42'], 'func': ibs_base_universe_d2_045_ibs_062_insider_conviction_42}


def ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84(ibs_064_insider_buy_cluster_84):
    return _base_universe_d2(ibs_064_insider_buy_cluster_84, 46)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84'] = {'inputs': ['ibs_064_insider_buy_cluster_84'], 'func': ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84}


def ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126(ibs_065_insider_net_buy_ratio_126):
    return _base_universe_d2(ibs_065_insider_net_buy_ratio_126, 47)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126'] = {'inputs': ['ibs_065_insider_net_buy_ratio_126'], 'func': ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126}


def ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189(ibs_066_insider_value_ratio_189):
    return _base_universe_d2(ibs_066_insider_value_ratio_189, 48)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189'] = {'inputs': ['ibs_066_insider_value_ratio_189'], 'func': ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189}


def ibs_base_universe_d2_049_ibs_069_insider_conviction_504(ibs_069_insider_conviction_504):
    return _base_universe_d2(ibs_069_insider_conviction_504, 49)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_049_ibs_069_insider_conviction_504'] = {'inputs': ['ibs_069_insider_conviction_504'], 'func': ibs_base_universe_d2_049_ibs_069_insider_conviction_504}


def ibs_base_universe_d2_050_ibs_070_insider_silence_756(ibs_070_insider_silence_756):
    return _base_universe_d2(ibs_070_insider_silence_756, 50)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_050_ibs_070_insider_silence_756'] = {'inputs': ['ibs_070_insider_silence_756'], 'func': ibs_base_universe_d2_050_ibs_070_insider_silence_756}


def ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008(ibs_071_insider_buy_cluster_1008):
    return _base_universe_d2(ibs_071_insider_buy_cluster_1008, 51)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008'] = {'inputs': ['ibs_071_insider_buy_cluster_1008'], 'func': ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008}


def ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260(ibs_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(ibs_072_insider_net_buy_ratio_1260, 52)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibs_072_insider_net_buy_ratio_1260'], 'func': ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260}


def ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512(ibs_073_insider_value_ratio_1512):
    return _base_universe_d2(ibs_073_insider_value_ratio_1512, 53)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512'] = {'inputs': ['ibs_073_insider_value_ratio_1512'], 'func': ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512}


def ibs_base_universe_d2_054_ibs_basefill_005(ibs_basefill_005):
    return _base_universe_d2(ibs_basefill_005, 54)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_054_ibs_basefill_005'] = {'inputs': ['ibs_basefill_005'], 'func': ibs_base_universe_d2_054_ibs_basefill_005}


def ibs_base_universe_d2_055_ibs_basefill_012(ibs_basefill_012):
    return _base_universe_d2(ibs_basefill_012, 55)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_055_ibs_basefill_012'] = {'inputs': ['ibs_basefill_012'], 'func': ibs_base_universe_d2_055_ibs_basefill_012}


def ibs_base_universe_d2_056_ibs_basefill_019(ibs_basefill_019):
    return _base_universe_d2(ibs_basefill_019, 56)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_056_ibs_basefill_019'] = {'inputs': ['ibs_basefill_019'], 'func': ibs_base_universe_d2_056_ibs_basefill_019}


def ibs_base_universe_d2_057_ibs_basefill_022(ibs_basefill_022):
    return _base_universe_d2(ibs_basefill_022, 57)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_057_ibs_basefill_022'] = {'inputs': ['ibs_basefill_022'], 'func': ibs_base_universe_d2_057_ibs_basefill_022}


def ibs_base_universe_d2_058_ibs_basefill_026(ibs_basefill_026):
    return _base_universe_d2(ibs_basefill_026, 58)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_058_ibs_basefill_026'] = {'inputs': ['ibs_basefill_026'], 'func': ibs_base_universe_d2_058_ibs_basefill_026}


def ibs_base_universe_d2_059_ibs_basefill_033(ibs_basefill_033):
    return _base_universe_d2(ibs_basefill_033, 59)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_059_ibs_basefill_033'] = {'inputs': ['ibs_basefill_033'], 'func': ibs_base_universe_d2_059_ibs_basefill_033}


def ibs_base_universe_d2_060_ibs_basefill_037(ibs_basefill_037):
    return _base_universe_d2(ibs_basefill_037, 60)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_060_ibs_basefill_037'] = {'inputs': ['ibs_basefill_037'], 'func': ibs_base_universe_d2_060_ibs_basefill_037}


def ibs_base_universe_d2_061_ibs_basefill_040(ibs_basefill_040):
    return _base_universe_d2(ibs_basefill_040, 61)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_061_ibs_basefill_040'] = {'inputs': ['ibs_basefill_040'], 'func': ibs_base_universe_d2_061_ibs_basefill_040}


def ibs_base_universe_d2_062_ibs_basefill_047(ibs_basefill_047):
    return _base_universe_d2(ibs_basefill_047, 62)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_062_ibs_basefill_047'] = {'inputs': ['ibs_basefill_047'], 'func': ibs_base_universe_d2_062_ibs_basefill_047}


def ibs_base_universe_d2_063_ibs_basefill_052(ibs_basefill_052):
    return _base_universe_d2(ibs_basefill_052, 63)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_063_ibs_basefill_052'] = {'inputs': ['ibs_basefill_052'], 'func': ibs_base_universe_d2_063_ibs_basefill_052}


def ibs_base_universe_d2_064_ibs_basefill_054(ibs_basefill_054):
    return _base_universe_d2(ibs_basefill_054, 64)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_064_ibs_basefill_054'] = {'inputs': ['ibs_basefill_054'], 'func': ibs_base_universe_d2_064_ibs_basefill_054}


def ibs_base_universe_d2_065_ibs_basefill_059(ibs_basefill_059):
    return _base_universe_d2(ibs_basefill_059, 65)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_065_ibs_basefill_059'] = {'inputs': ['ibs_basefill_059'], 'func': ibs_base_universe_d2_065_ibs_basefill_059}


def ibs_base_universe_d2_066_ibs_basefill_061(ibs_basefill_061):
    return _base_universe_d2(ibs_basefill_061, 66)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_066_ibs_basefill_061'] = {'inputs': ['ibs_basefill_061'], 'func': ibs_base_universe_d2_066_ibs_basefill_061}


def ibs_base_universe_d2_067_ibs_basefill_063(ibs_basefill_063):
    return _base_universe_d2(ibs_basefill_063, 67)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_067_ibs_basefill_063'] = {'inputs': ['ibs_basefill_063'], 'func': ibs_base_universe_d2_067_ibs_basefill_063}


def ibs_base_universe_d2_068_ibs_basefill_067(ibs_basefill_067):
    return _base_universe_d2(ibs_basefill_067, 68)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_068_ibs_basefill_067'] = {'inputs': ['ibs_basefill_067'], 'func': ibs_base_universe_d2_068_ibs_basefill_067}


def ibs_base_universe_d2_069_ibs_basefill_068(ibs_basefill_068):
    return _base_universe_d2(ibs_basefill_068, 69)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_069_ibs_basefill_068'] = {'inputs': ['ibs_basefill_068'], 'func': ibs_base_universe_d2_069_ibs_basefill_068}


def ibs_base_universe_d2_070_ibs_basefill_074(ibs_basefill_074):
    return _base_universe_d2(ibs_basefill_074, 70)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_070_ibs_basefill_074'] = {'inputs': ['ibs_basefill_074'], 'func': ibs_base_universe_d2_070_ibs_basefill_074}


def ibs_base_universe_d2_071_ibs_basefill_075(ibs_basefill_075):
    return _base_universe_d2(ibs_basefill_075, 71)
IBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ibs_base_universe_d2_071_ibs_basefill_075'] = {'inputs': ['ibs_basefill_075'], 'func': ibs_base_universe_d2_071_ibs_basefill_075}
