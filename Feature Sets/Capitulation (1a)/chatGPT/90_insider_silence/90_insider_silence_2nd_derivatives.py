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



def isl_151_isl_001_insider_buy_cluster_21_roc_1(isl_001_insider_buy_cluster_21):
    feature = _s(isl_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def isl_152_isl_007_insider_silence_252_roc_42(isl_007_insider_silence_252):
    feature = _s(isl_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def isl_153_isl_013_insider_conviction_1512_roc_126(isl_013_insider_conviction_1512):
    feature = _s(isl_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def isl_154_isl_019_insider_activity_accel_1_roc_378(isl_019_insider_activity_accel_1):
    feature = _s(isl_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4(isl_025_ceo_cfo_buy_weight_756):
    feature = _s(isl_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_SILENCE_REGISTRY_2ND_DERIVATIVES = {
    'isl_151_isl_001_insider_buy_cluster_21_roc_1': {'inputs': ['isl_001_insider_buy_cluster_21'], 'func': isl_151_isl_001_insider_buy_cluster_21_roc_1},
    'isl_152_isl_007_insider_silence_252_roc_42': {'inputs': ['isl_007_insider_silence_252'], 'func': isl_152_isl_007_insider_silence_252_roc_42},
    'isl_153_isl_013_insider_conviction_1512_roc_126': {'inputs': ['isl_013_insider_conviction_1512'], 'func': isl_153_isl_013_insider_conviction_1512_roc_126},
    'isl_154_isl_019_insider_activity_accel_1_roc_378': {'inputs': ['isl_019_insider_activity_accel_1'], 'func': isl_154_isl_019_insider_activity_accel_1_roc_378},
    'isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['isl_025_ceo_cfo_buy_weight_756'], 'func': isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def is_replacement_d2_001(isl_019_insider_activity_accel_1):
    feature = _clean(isl_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_001'] = {'inputs': ['isl_019_insider_activity_accel_1'], 'func': is_replacement_d2_001}


def is_replacement_d2_002(is_replacement_001):
    feature = _clean(is_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_002'] = {'inputs': ['is_replacement_001'], 'func': is_replacement_d2_002}


def is_replacement_d2_003(is_replacement_002):
    feature = _clean(is_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_003'] = {'inputs': ['is_replacement_002'], 'func': is_replacement_d2_003}


def is_replacement_d2_004(is_replacement_003):
    feature = _clean(is_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_004'] = {'inputs': ['is_replacement_003'], 'func': is_replacement_d2_004}


def is_replacement_d2_005(is_replacement_004):
    feature = _clean(is_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_005'] = {'inputs': ['is_replacement_004'], 'func': is_replacement_d2_005}


def is_replacement_d2_006(is_replacement_005):
    feature = _clean(is_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_006'] = {'inputs': ['is_replacement_005'], 'func': is_replacement_d2_006}


def is_replacement_d2_007(is_replacement_006):
    feature = _clean(is_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_007'] = {'inputs': ['is_replacement_006'], 'func': is_replacement_d2_007}


def is_replacement_d2_008(is_replacement_007):
    feature = _clean(is_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_008'] = {'inputs': ['is_replacement_007'], 'func': is_replacement_d2_008}


def is_replacement_d2_009(is_replacement_008):
    feature = _clean(is_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_009'] = {'inputs': ['is_replacement_008'], 'func': is_replacement_d2_009}


def is_replacement_d2_010(is_replacement_009):
    feature = _clean(is_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_010'] = {'inputs': ['is_replacement_009'], 'func': is_replacement_d2_010}


def is_replacement_d2_011(is_replacement_010):
    feature = _clean(is_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_011'] = {'inputs': ['is_replacement_010'], 'func': is_replacement_d2_011}


def is_replacement_d2_012(is_replacement_011):
    feature = _clean(is_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_012'] = {'inputs': ['is_replacement_011'], 'func': is_replacement_d2_012}


def is_replacement_d2_013(is_replacement_012):
    feature = _clean(is_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_013'] = {'inputs': ['is_replacement_012'], 'func': is_replacement_d2_013}


def is_replacement_d2_014(is_replacement_013):
    feature = _clean(is_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_014'] = {'inputs': ['is_replacement_013'], 'func': is_replacement_d2_014}


def is_replacement_d2_015(is_replacement_014):
    feature = _clean(is_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_015'] = {'inputs': ['is_replacement_014'], 'func': is_replacement_d2_015}


def is_replacement_d2_016(is_replacement_015):
    feature = _clean(is_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_016'] = {'inputs': ['is_replacement_015'], 'func': is_replacement_d2_016}


def is_replacement_d2_017(is_replacement_016):
    feature = _clean(is_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_017'] = {'inputs': ['is_replacement_016'], 'func': is_replacement_d2_017}


def is_replacement_d2_018(is_replacement_017):
    feature = _clean(is_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_018'] = {'inputs': ['is_replacement_017'], 'func': is_replacement_d2_018}


def is_replacement_d2_019(is_replacement_018):
    feature = _clean(is_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_019'] = {'inputs': ['is_replacement_018'], 'func': is_replacement_d2_019}


def is_replacement_d2_020(is_replacement_019):
    feature = _clean(is_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_020'] = {'inputs': ['is_replacement_019'], 'func': is_replacement_d2_020}


def is_replacement_d2_021(is_replacement_020):
    feature = _clean(is_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_021'] = {'inputs': ['is_replacement_020'], 'func': is_replacement_d2_021}


def is_replacement_d2_022(is_replacement_021):
    feature = _clean(is_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_022'] = {'inputs': ['is_replacement_021'], 'func': is_replacement_d2_022}


def is_replacement_d2_023(is_replacement_022):
    feature = _clean(is_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_023'] = {'inputs': ['is_replacement_022'], 'func': is_replacement_d2_023}


def is_replacement_d2_024(is_replacement_023):
    feature = _clean(is_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_024'] = {'inputs': ['is_replacement_023'], 'func': is_replacement_d2_024}


def is_replacement_d2_025(is_replacement_024):
    feature = _clean(is_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_025'] = {'inputs': ['is_replacement_024'], 'func': is_replacement_d2_025}


def is_replacement_d2_026(is_replacement_025):
    feature = _clean(is_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_026'] = {'inputs': ['is_replacement_025'], 'func': is_replacement_d2_026}


def is_replacement_d2_027(is_replacement_026):
    feature = _clean(is_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_027'] = {'inputs': ['is_replacement_026'], 'func': is_replacement_d2_027}


def is_replacement_d2_028(is_replacement_027):
    feature = _clean(is_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_028'] = {'inputs': ['is_replacement_027'], 'func': is_replacement_d2_028}


def is_replacement_d2_029(is_replacement_028):
    feature = _clean(is_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_029'] = {'inputs': ['is_replacement_028'], 'func': is_replacement_d2_029}


def is_replacement_d2_030(is_replacement_029):
    feature = _clean(is_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_030'] = {'inputs': ['is_replacement_029'], 'func': is_replacement_d2_030}


def is_replacement_d2_031(is_replacement_030):
    feature = _clean(is_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_031'] = {'inputs': ['is_replacement_030'], 'func': is_replacement_d2_031}


def is_replacement_d2_032(is_replacement_031):
    feature = _clean(is_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_032'] = {'inputs': ['is_replacement_031'], 'func': is_replacement_d2_032}


def is_replacement_d2_033(is_replacement_032):
    feature = _clean(is_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_033'] = {'inputs': ['is_replacement_032'], 'func': is_replacement_d2_033}


def is_replacement_d2_034(is_replacement_033):
    feature = _clean(is_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_034'] = {'inputs': ['is_replacement_033'], 'func': is_replacement_d2_034}


def is_replacement_d2_035(is_replacement_034):
    feature = _clean(is_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_035'] = {'inputs': ['is_replacement_034'], 'func': is_replacement_d2_035}


def is_replacement_d2_036(is_replacement_035):
    feature = _clean(is_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_036'] = {'inputs': ['is_replacement_035'], 'func': is_replacement_d2_036}


def is_replacement_d2_037(is_replacement_036):
    feature = _clean(is_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_037'] = {'inputs': ['is_replacement_036'], 'func': is_replacement_d2_037}


def is_replacement_d2_038(is_replacement_037):
    feature = _clean(is_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_038'] = {'inputs': ['is_replacement_037'], 'func': is_replacement_d2_038}


def is_replacement_d2_039(is_replacement_038):
    feature = _clean(is_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_039'] = {'inputs': ['is_replacement_038'], 'func': is_replacement_d2_039}


def is_replacement_d2_040(is_replacement_039):
    feature = _clean(is_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_040'] = {'inputs': ['is_replacement_039'], 'func': is_replacement_d2_040}


def is_replacement_d2_041(is_replacement_040):
    feature = _clean(is_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_041'] = {'inputs': ['is_replacement_040'], 'func': is_replacement_d2_041}


def is_replacement_d2_042(is_replacement_041):
    feature = _clean(is_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_042'] = {'inputs': ['is_replacement_041'], 'func': is_replacement_d2_042}


def is_replacement_d2_043(is_replacement_042):
    feature = _clean(is_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_043'] = {'inputs': ['is_replacement_042'], 'func': is_replacement_d2_043}


def is_replacement_d2_044(is_replacement_043):
    feature = _clean(is_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_044'] = {'inputs': ['is_replacement_043'], 'func': is_replacement_d2_044}


def is_replacement_d2_045(is_replacement_044):
    feature = _clean(is_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_045'] = {'inputs': ['is_replacement_044'], 'func': is_replacement_d2_045}


def is_replacement_d2_046(is_replacement_045):
    feature = _clean(is_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_046'] = {'inputs': ['is_replacement_045'], 'func': is_replacement_d2_046}


def is_replacement_d2_047(is_replacement_046):
    feature = _clean(is_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_047'] = {'inputs': ['is_replacement_046'], 'func': is_replacement_d2_047}


def is_replacement_d2_048(is_replacement_047):
    feature = _clean(is_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_048'] = {'inputs': ['is_replacement_047'], 'func': is_replacement_d2_048}


def is_replacement_d2_049(is_replacement_048):
    feature = _clean(is_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_049'] = {'inputs': ['is_replacement_048'], 'func': is_replacement_d2_049}


def is_replacement_d2_050(is_replacement_049):
    feature = _clean(is_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_050'] = {'inputs': ['is_replacement_049'], 'func': is_replacement_d2_050}


def is_replacement_d2_051(is_replacement_050):
    feature = _clean(is_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_051'] = {'inputs': ['is_replacement_050'], 'func': is_replacement_d2_051}


def is_replacement_d2_052(is_replacement_051):
    feature = _clean(is_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_052'] = {'inputs': ['is_replacement_051'], 'func': is_replacement_d2_052}


def is_replacement_d2_053(is_replacement_052):
    feature = _clean(is_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_053'] = {'inputs': ['is_replacement_052'], 'func': is_replacement_d2_053}


def is_replacement_d2_054(is_replacement_053):
    feature = _clean(is_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_054'] = {'inputs': ['is_replacement_053'], 'func': is_replacement_d2_054}


def is_replacement_d2_055(is_replacement_054):
    feature = _clean(is_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_055'] = {'inputs': ['is_replacement_054'], 'func': is_replacement_d2_055}


def is_replacement_d2_056(is_replacement_055):
    feature = _clean(is_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_056'] = {'inputs': ['is_replacement_055'], 'func': is_replacement_d2_056}


def is_replacement_d2_057(is_replacement_056):
    feature = _clean(is_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_057'] = {'inputs': ['is_replacement_056'], 'func': is_replacement_d2_057}


def is_replacement_d2_058(is_replacement_057):
    feature = _clean(is_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_058'] = {'inputs': ['is_replacement_057'], 'func': is_replacement_d2_058}


def is_replacement_d2_059(is_replacement_058):
    feature = _clean(is_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_059'] = {'inputs': ['is_replacement_058'], 'func': is_replacement_d2_059}


def is_replacement_d2_060(is_replacement_059):
    feature = _clean(is_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_060'] = {'inputs': ['is_replacement_059'], 'func': is_replacement_d2_060}


def is_replacement_d2_061(is_replacement_060):
    feature = _clean(is_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_061'] = {'inputs': ['is_replacement_060'], 'func': is_replacement_d2_061}


def is_replacement_d2_062(is_replacement_061):
    feature = _clean(is_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_062'] = {'inputs': ['is_replacement_061'], 'func': is_replacement_d2_062}


def is_replacement_d2_063(is_replacement_062):
    feature = _clean(is_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_063'] = {'inputs': ['is_replacement_062'], 'func': is_replacement_d2_063}


def is_replacement_d2_064(is_replacement_063):
    feature = _clean(is_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_064'] = {'inputs': ['is_replacement_063'], 'func': is_replacement_d2_064}


def is_replacement_d2_065(is_replacement_064):
    feature = _clean(is_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_065'] = {'inputs': ['is_replacement_064'], 'func': is_replacement_d2_065}


def is_replacement_d2_066(is_replacement_065):
    feature = _clean(is_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_066'] = {'inputs': ['is_replacement_065'], 'func': is_replacement_d2_066}


def is_replacement_d2_067(is_replacement_066):
    feature = _clean(is_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_067'] = {'inputs': ['is_replacement_066'], 'func': is_replacement_d2_067}


def is_replacement_d2_068(is_replacement_067):
    feature = _clean(is_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_068'] = {'inputs': ['is_replacement_067'], 'func': is_replacement_d2_068}


def is_replacement_d2_069(is_replacement_068):
    feature = _clean(is_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_069'] = {'inputs': ['is_replacement_068'], 'func': is_replacement_d2_069}


def is_replacement_d2_070(is_replacement_069):
    feature = _clean(is_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_070'] = {'inputs': ['is_replacement_069'], 'func': is_replacement_d2_070}


def is_replacement_d2_071(is_replacement_070):
    feature = _clean(is_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_071'] = {'inputs': ['is_replacement_070'], 'func': is_replacement_d2_071}


def is_replacement_d2_072(is_replacement_071):
    feature = _clean(is_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_072'] = {'inputs': ['is_replacement_071'], 'func': is_replacement_d2_072}


def is_replacement_d2_073(is_replacement_072):
    feature = _clean(is_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_073'] = {'inputs': ['is_replacement_072'], 'func': is_replacement_d2_073}


def is_replacement_d2_074(is_replacement_073):
    feature = _clean(is_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_074'] = {'inputs': ['is_replacement_073'], 'func': is_replacement_d2_074}


def is_replacement_d2_075(is_replacement_074):
    feature = _clean(is_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_075'] = {'inputs': ['is_replacement_074'], 'func': is_replacement_d2_075}


def is_replacement_d2_076(is_replacement_075):
    feature = _clean(is_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_076'] = {'inputs': ['is_replacement_075'], 'func': is_replacement_d2_076}


def is_replacement_d2_077(is_replacement_076):
    feature = _clean(is_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_077'] = {'inputs': ['is_replacement_076'], 'func': is_replacement_d2_077}


def is_replacement_d2_078(is_replacement_077):
    feature = _clean(is_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_078'] = {'inputs': ['is_replacement_077'], 'func': is_replacement_d2_078}


def is_replacement_d2_079(is_replacement_078):
    feature = _clean(is_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_079'] = {'inputs': ['is_replacement_078'], 'func': is_replacement_d2_079}


def is_replacement_d2_080(is_replacement_079):
    feature = _clean(is_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_080'] = {'inputs': ['is_replacement_079'], 'func': is_replacement_d2_080}


def is_replacement_d2_081(is_replacement_080):
    feature = _clean(is_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_081'] = {'inputs': ['is_replacement_080'], 'func': is_replacement_d2_081}


def is_replacement_d2_082(is_replacement_081):
    feature = _clean(is_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_082'] = {'inputs': ['is_replacement_081'], 'func': is_replacement_d2_082}


def is_replacement_d2_083(is_replacement_082):
    feature = _clean(is_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_083'] = {'inputs': ['is_replacement_082'], 'func': is_replacement_d2_083}


def is_replacement_d2_084(is_replacement_083):
    feature = _clean(is_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_084'] = {'inputs': ['is_replacement_083'], 'func': is_replacement_d2_084}


def is_replacement_d2_085(is_replacement_084):
    feature = _clean(is_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_085'] = {'inputs': ['is_replacement_084'], 'func': is_replacement_d2_085}


def is_replacement_d2_086(is_replacement_085):
    feature = _clean(is_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_086'] = {'inputs': ['is_replacement_085'], 'func': is_replacement_d2_086}


def is_replacement_d2_087(is_replacement_086):
    feature = _clean(is_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_087'] = {'inputs': ['is_replacement_086'], 'func': is_replacement_d2_087}


def is_replacement_d2_088(is_replacement_087):
    feature = _clean(is_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_088'] = {'inputs': ['is_replacement_087'], 'func': is_replacement_d2_088}


def is_replacement_d2_089(is_replacement_088):
    feature = _clean(is_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_089'] = {'inputs': ['is_replacement_088'], 'func': is_replacement_d2_089}


def is_replacement_d2_090(is_replacement_089):
    feature = _clean(is_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_090'] = {'inputs': ['is_replacement_089'], 'func': is_replacement_d2_090}


def is_replacement_d2_091(is_replacement_090):
    feature = _clean(is_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_091'] = {'inputs': ['is_replacement_090'], 'func': is_replacement_d2_091}


def is_replacement_d2_092(is_replacement_091):
    feature = _clean(is_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_092'] = {'inputs': ['is_replacement_091'], 'func': is_replacement_d2_092}


def is_replacement_d2_093(is_replacement_092):
    feature = _clean(is_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_093'] = {'inputs': ['is_replacement_092'], 'func': is_replacement_d2_093}


def is_replacement_d2_094(is_replacement_093):
    feature = _clean(is_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_094'] = {'inputs': ['is_replacement_093'], 'func': is_replacement_d2_094}


def is_replacement_d2_095(is_replacement_094):
    feature = _clean(is_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_095'] = {'inputs': ['is_replacement_094'], 'func': is_replacement_d2_095}


def is_replacement_d2_096(is_replacement_095):
    feature = _clean(is_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_096'] = {'inputs': ['is_replacement_095'], 'func': is_replacement_d2_096}


def is_replacement_d2_097(is_replacement_096):
    feature = _clean(is_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_097'] = {'inputs': ['is_replacement_096'], 'func': is_replacement_d2_097}


def is_replacement_d2_098(is_replacement_097):
    feature = _clean(is_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_098'] = {'inputs': ['is_replacement_097'], 'func': is_replacement_d2_098}


def is_replacement_d2_099(is_replacement_098):
    feature = _clean(is_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_099'] = {'inputs': ['is_replacement_098'], 'func': is_replacement_d2_099}


def is_replacement_d2_100(is_replacement_099):
    feature = _clean(is_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_100'] = {'inputs': ['is_replacement_099'], 'func': is_replacement_d2_100}


def is_replacement_d2_101(is_replacement_100):
    feature = _clean(is_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_101'] = {'inputs': ['is_replacement_100'], 'func': is_replacement_d2_101}


def is_replacement_d2_102(is_replacement_101):
    feature = _clean(is_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_102'] = {'inputs': ['is_replacement_101'], 'func': is_replacement_d2_102}


def is_replacement_d2_103(is_replacement_102):
    feature = _clean(is_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_103'] = {'inputs': ['is_replacement_102'], 'func': is_replacement_d2_103}


def is_replacement_d2_104(is_replacement_103):
    feature = _clean(is_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_104'] = {'inputs': ['is_replacement_103'], 'func': is_replacement_d2_104}


def is_replacement_d2_105(is_replacement_104):
    feature = _clean(is_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_105'] = {'inputs': ['is_replacement_104'], 'func': is_replacement_d2_105}


def is_replacement_d2_106(is_replacement_105):
    feature = _clean(is_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_106'] = {'inputs': ['is_replacement_105'], 'func': is_replacement_d2_106}


def is_replacement_d2_107(is_replacement_106):
    feature = _clean(is_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_107'] = {'inputs': ['is_replacement_106'], 'func': is_replacement_d2_107}


def is_replacement_d2_108(is_replacement_107):
    feature = _clean(is_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_108'] = {'inputs': ['is_replacement_107'], 'func': is_replacement_d2_108}


def is_replacement_d2_109(is_replacement_108):
    feature = _clean(is_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_109'] = {'inputs': ['is_replacement_108'], 'func': is_replacement_d2_109}


def is_replacement_d2_110(is_replacement_109):
    feature = _clean(is_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_110'] = {'inputs': ['is_replacement_109'], 'func': is_replacement_d2_110}


def is_replacement_d2_111(is_replacement_110):
    feature = _clean(is_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_111'] = {'inputs': ['is_replacement_110'], 'func': is_replacement_d2_111}


def is_replacement_d2_112(is_replacement_111):
    feature = _clean(is_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['is_replacement_d2_112'] = {'inputs': ['is_replacement_111'], 'func': is_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42(isl_002_insider_net_buy_ratio_42):
    return _base_universe_d2(isl_002_insider_net_buy_ratio_42, 1)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42'] = {'inputs': ['isl_002_insider_net_buy_ratio_42'], 'func': isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42}


def isl_base_universe_d2_002_isl_003_insider_value_ratio_63(isl_003_insider_value_ratio_63):
    return _base_universe_d2(isl_003_insider_value_ratio_63, 2)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_002_isl_003_insider_value_ratio_63'] = {'inputs': ['isl_003_insider_value_ratio_63'], 'func': isl_base_universe_d2_002_isl_003_insider_value_ratio_63}


def isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84(isl_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(isl_004_ceo_cfo_buy_weight_84, 3)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84'] = {'inputs': ['isl_004_ceo_cfo_buy_weight_84'], 'func': isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84}


def isl_base_universe_d2_004_isl_006_insider_conviction_189(isl_006_insider_conviction_189):
    return _base_universe_d2(isl_006_insider_conviction_189, 4)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_004_isl_006_insider_conviction_189'] = {'inputs': ['isl_006_insider_conviction_189'], 'func': isl_base_universe_d2_004_isl_006_insider_conviction_189}


def isl_base_universe_d2_005_isl_008_insider_buy_cluster_378(isl_008_insider_buy_cluster_378):
    return _base_universe_d2(isl_008_insider_buy_cluster_378, 5)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_005_isl_008_insider_buy_cluster_378'] = {'inputs': ['isl_008_insider_buy_cluster_378'], 'func': isl_base_universe_d2_005_isl_008_insider_buy_cluster_378}


def isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504(isl_009_insider_net_buy_ratio_504):
    return _base_universe_d2(isl_009_insider_net_buy_ratio_504, 6)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504'] = {'inputs': ['isl_009_insider_net_buy_ratio_504'], 'func': isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504}


def isl_base_universe_d2_007_isl_010_insider_value_ratio_756(isl_010_insider_value_ratio_756):
    return _base_universe_d2(isl_010_insider_value_ratio_756, 7)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_007_isl_010_insider_value_ratio_756'] = {'inputs': ['isl_010_insider_value_ratio_756'], 'func': isl_base_universe_d2_007_isl_010_insider_value_ratio_756}


def isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008(isl_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(isl_011_ceo_cfo_buy_weight_1008, 8)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['isl_011_ceo_cfo_buy_weight_1008'], 'func': isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008}


def isl_base_universe_d2_009_isl_014_insider_silence_63(isl_014_insider_silence_63):
    return _base_universe_d2(isl_014_insider_silence_63, 9)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_009_isl_014_insider_silence_63'] = {'inputs': ['isl_014_insider_silence_63'], 'func': isl_base_universe_d2_009_isl_014_insider_silence_63}


def isl_base_universe_d2_010_isl_015_insider_buy_cluster_252(isl_015_insider_buy_cluster_252):
    return _base_universe_d2(isl_015_insider_buy_cluster_252, 10)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_010_isl_015_insider_buy_cluster_252'] = {'inputs': ['isl_015_insider_buy_cluster_252'], 'func': isl_base_universe_d2_010_isl_015_insider_buy_cluster_252}


def isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21(isl_016_insider_net_buy_ratio_21):
    return _base_universe_d2(isl_016_insider_net_buy_ratio_21, 11)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21'] = {'inputs': ['isl_016_insider_net_buy_ratio_21'], 'func': isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21}


def isl_base_universe_d2_012_isl_017_insider_value_ratio_42(isl_017_insider_value_ratio_42):
    return _base_universe_d2(isl_017_insider_value_ratio_42, 12)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_012_isl_017_insider_value_ratio_42'] = {'inputs': ['isl_017_insider_value_ratio_42'], 'func': isl_base_universe_d2_012_isl_017_insider_value_ratio_42}


def isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63(isl_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(isl_018_ceo_cfo_buy_weight_63, 13)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63'] = {'inputs': ['isl_018_ceo_cfo_buy_weight_63'], 'func': isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63}


def isl_base_universe_d2_014_isl_020_insider_conviction_126(isl_020_insider_conviction_126):
    return _base_universe_d2(isl_020_insider_conviction_126, 14)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_014_isl_020_insider_conviction_126'] = {'inputs': ['isl_020_insider_conviction_126'], 'func': isl_base_universe_d2_014_isl_020_insider_conviction_126}


def isl_base_universe_d2_015_isl_021_insider_silence_189(isl_021_insider_silence_189):
    return _base_universe_d2(isl_021_insider_silence_189, 15)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_015_isl_021_insider_silence_189'] = {'inputs': ['isl_021_insider_silence_189'], 'func': isl_base_universe_d2_015_isl_021_insider_silence_189}


def isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378(isl_023_insider_net_buy_ratio_378):
    return _base_universe_d2(isl_023_insider_net_buy_ratio_378, 16)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378'] = {'inputs': ['isl_023_insider_net_buy_ratio_378'], 'func': isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378}


def isl_base_universe_d2_017_isl_024_insider_value_ratio_504(isl_024_insider_value_ratio_504):
    return _base_universe_d2(isl_024_insider_value_ratio_504, 17)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_017_isl_024_insider_value_ratio_504'] = {'inputs': ['isl_024_insider_value_ratio_504'], 'func': isl_base_universe_d2_017_isl_024_insider_value_ratio_504}


def isl_base_universe_d2_018_isl_027_insider_conviction_1260(isl_027_insider_conviction_1260):
    return _base_universe_d2(isl_027_insider_conviction_1260, 18)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_018_isl_027_insider_conviction_1260'] = {'inputs': ['isl_027_insider_conviction_1260'], 'func': isl_base_universe_d2_018_isl_027_insider_conviction_1260}


def isl_base_universe_d2_019_isl_028_insider_silence_1512(isl_028_insider_silence_1512):
    return _base_universe_d2(isl_028_insider_silence_1512, 19)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_019_isl_028_insider_silence_1512'] = {'inputs': ['isl_028_insider_silence_1512'], 'func': isl_base_universe_d2_019_isl_028_insider_silence_1512}


def isl_base_universe_d2_020_isl_029_insider_buy_cluster_63(isl_029_insider_buy_cluster_63):
    return _base_universe_d2(isl_029_insider_buy_cluster_63, 20)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_020_isl_029_insider_buy_cluster_63'] = {'inputs': ['isl_029_insider_buy_cluster_63'], 'func': isl_base_universe_d2_020_isl_029_insider_buy_cluster_63}


def isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252(isl_030_insider_net_buy_ratio_252):
    return _base_universe_d2(isl_030_insider_net_buy_ratio_252, 21)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252'] = {'inputs': ['isl_030_insider_net_buy_ratio_252'], 'func': isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252}


def isl_base_universe_d2_022_isl_031_insider_value_ratio_21(isl_031_insider_value_ratio_21):
    return _base_universe_d2(isl_031_insider_value_ratio_21, 22)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_022_isl_031_insider_value_ratio_21'] = {'inputs': ['isl_031_insider_value_ratio_21'], 'func': isl_base_universe_d2_022_isl_031_insider_value_ratio_21}


def isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42(isl_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(isl_032_ceo_cfo_buy_weight_42, 23)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42'] = {'inputs': ['isl_032_ceo_cfo_buy_weight_42'], 'func': isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42}


def isl_base_universe_d2_024_isl_034_insider_conviction_84(isl_034_insider_conviction_84):
    return _base_universe_d2(isl_034_insider_conviction_84, 24)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_024_isl_034_insider_conviction_84'] = {'inputs': ['isl_034_insider_conviction_84'], 'func': isl_base_universe_d2_024_isl_034_insider_conviction_84}


def isl_base_universe_d2_025_isl_035_insider_silence_126(isl_035_insider_silence_126):
    return _base_universe_d2(isl_035_insider_silence_126, 25)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_025_isl_035_insider_silence_126'] = {'inputs': ['isl_035_insider_silence_126'], 'func': isl_base_universe_d2_025_isl_035_insider_silence_126}


def isl_base_universe_d2_026_isl_036_insider_buy_cluster_189(isl_036_insider_buy_cluster_189):
    return _base_universe_d2(isl_036_insider_buy_cluster_189, 26)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_026_isl_036_insider_buy_cluster_189'] = {'inputs': ['isl_036_insider_buy_cluster_189'], 'func': isl_base_universe_d2_026_isl_036_insider_buy_cluster_189}


def isl_base_universe_d2_027_isl_038_insider_value_ratio_378(isl_038_insider_value_ratio_378):
    return _base_universe_d2(isl_038_insider_value_ratio_378, 27)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_027_isl_038_insider_value_ratio_378'] = {'inputs': ['isl_038_insider_value_ratio_378'], 'func': isl_base_universe_d2_027_isl_038_insider_value_ratio_378}


def isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504(isl_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(isl_039_ceo_cfo_buy_weight_504, 28)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504'] = {'inputs': ['isl_039_ceo_cfo_buy_weight_504'], 'func': isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504}


def isl_base_universe_d2_029_isl_041_insider_conviction_1008(isl_041_insider_conviction_1008):
    return _base_universe_d2(isl_041_insider_conviction_1008, 29)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_029_isl_041_insider_conviction_1008'] = {'inputs': ['isl_041_insider_conviction_1008'], 'func': isl_base_universe_d2_029_isl_041_insider_conviction_1008}


def isl_base_universe_d2_030_isl_042_insider_silence_1260(isl_042_insider_silence_1260):
    return _base_universe_d2(isl_042_insider_silence_1260, 30)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_030_isl_042_insider_silence_1260'] = {'inputs': ['isl_042_insider_silence_1260'], 'func': isl_base_universe_d2_030_isl_042_insider_silence_1260}


def isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512(isl_043_insider_buy_cluster_1512):
    return _base_universe_d2(isl_043_insider_buy_cluster_1512, 31)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512'] = {'inputs': ['isl_043_insider_buy_cluster_1512'], 'func': isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512}


def isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63(isl_044_insider_net_buy_ratio_63):
    return _base_universe_d2(isl_044_insider_net_buy_ratio_63, 32)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63'] = {'inputs': ['isl_044_insider_net_buy_ratio_63'], 'func': isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63}


def isl_base_universe_d2_033_isl_045_insider_value_ratio_252(isl_045_insider_value_ratio_252):
    return _base_universe_d2(isl_045_insider_value_ratio_252, 33)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_033_isl_045_insider_value_ratio_252'] = {'inputs': ['isl_045_insider_value_ratio_252'], 'func': isl_base_universe_d2_033_isl_045_insider_value_ratio_252}


def isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21(isl_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(isl_046_ceo_cfo_buy_weight_21, 34)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21'] = {'inputs': ['isl_046_ceo_cfo_buy_weight_21'], 'func': isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21}


def isl_base_universe_d2_035_isl_048_insider_conviction_63(isl_048_insider_conviction_63):
    return _base_universe_d2(isl_048_insider_conviction_63, 35)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_035_isl_048_insider_conviction_63'] = {'inputs': ['isl_048_insider_conviction_63'], 'func': isl_base_universe_d2_035_isl_048_insider_conviction_63}


def isl_base_universe_d2_036_isl_049_insider_silence_84(isl_049_insider_silence_84):
    return _base_universe_d2(isl_049_insider_silence_84, 36)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_036_isl_049_insider_silence_84'] = {'inputs': ['isl_049_insider_silence_84'], 'func': isl_base_universe_d2_036_isl_049_insider_silence_84}


def isl_base_universe_d2_037_isl_050_insider_buy_cluster_126(isl_050_insider_buy_cluster_126):
    return _base_universe_d2(isl_050_insider_buy_cluster_126, 37)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_037_isl_050_insider_buy_cluster_126'] = {'inputs': ['isl_050_insider_buy_cluster_126'], 'func': isl_base_universe_d2_037_isl_050_insider_buy_cluster_126}


def isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189(isl_051_insider_net_buy_ratio_189):
    return _base_universe_d2(isl_051_insider_net_buy_ratio_189, 38)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189'] = {'inputs': ['isl_051_insider_net_buy_ratio_189'], 'func': isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189}


def isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378(isl_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(isl_053_ceo_cfo_buy_weight_378, 39)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378'] = {'inputs': ['isl_053_ceo_cfo_buy_weight_378'], 'func': isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378}


def isl_base_universe_d2_040_isl_055_insider_conviction_756(isl_055_insider_conviction_756):
    return _base_universe_d2(isl_055_insider_conviction_756, 40)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_040_isl_055_insider_conviction_756'] = {'inputs': ['isl_055_insider_conviction_756'], 'func': isl_base_universe_d2_040_isl_055_insider_conviction_756}


def isl_base_universe_d2_041_isl_056_insider_silence_1008(isl_056_insider_silence_1008):
    return _base_universe_d2(isl_056_insider_silence_1008, 41)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_041_isl_056_insider_silence_1008'] = {'inputs': ['isl_056_insider_silence_1008'], 'func': isl_base_universe_d2_041_isl_056_insider_silence_1008}


def isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260(isl_057_insider_buy_cluster_1260):
    return _base_universe_d2(isl_057_insider_buy_cluster_1260, 42)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260'] = {'inputs': ['isl_057_insider_buy_cluster_1260'], 'func': isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260}


def isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512(isl_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(isl_058_insider_net_buy_ratio_1512, 43)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512'] = {'inputs': ['isl_058_insider_net_buy_ratio_1512'], 'func': isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512}


def isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252(isl_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(isl_060_ceo_cfo_buy_weight_252, 44)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252'] = {'inputs': ['isl_060_ceo_cfo_buy_weight_252'], 'func': isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252}


def isl_base_universe_d2_045_isl_062_insider_conviction_42(isl_062_insider_conviction_42):
    return _base_universe_d2(isl_062_insider_conviction_42, 45)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_045_isl_062_insider_conviction_42'] = {'inputs': ['isl_062_insider_conviction_42'], 'func': isl_base_universe_d2_045_isl_062_insider_conviction_42}


def isl_base_universe_d2_046_isl_064_insider_buy_cluster_84(isl_064_insider_buy_cluster_84):
    return _base_universe_d2(isl_064_insider_buy_cluster_84, 46)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_046_isl_064_insider_buy_cluster_84'] = {'inputs': ['isl_064_insider_buy_cluster_84'], 'func': isl_base_universe_d2_046_isl_064_insider_buy_cluster_84}


def isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126(isl_065_insider_net_buy_ratio_126):
    return _base_universe_d2(isl_065_insider_net_buy_ratio_126, 47)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126'] = {'inputs': ['isl_065_insider_net_buy_ratio_126'], 'func': isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126}


def isl_base_universe_d2_048_isl_066_insider_value_ratio_189(isl_066_insider_value_ratio_189):
    return _base_universe_d2(isl_066_insider_value_ratio_189, 48)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_048_isl_066_insider_value_ratio_189'] = {'inputs': ['isl_066_insider_value_ratio_189'], 'func': isl_base_universe_d2_048_isl_066_insider_value_ratio_189}


def isl_base_universe_d2_049_isl_069_insider_conviction_504(isl_069_insider_conviction_504):
    return _base_universe_d2(isl_069_insider_conviction_504, 49)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_049_isl_069_insider_conviction_504'] = {'inputs': ['isl_069_insider_conviction_504'], 'func': isl_base_universe_d2_049_isl_069_insider_conviction_504}


def isl_base_universe_d2_050_isl_070_insider_silence_756(isl_070_insider_silence_756):
    return _base_universe_d2(isl_070_insider_silence_756, 50)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_050_isl_070_insider_silence_756'] = {'inputs': ['isl_070_insider_silence_756'], 'func': isl_base_universe_d2_050_isl_070_insider_silence_756}


def isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008(isl_071_insider_buy_cluster_1008):
    return _base_universe_d2(isl_071_insider_buy_cluster_1008, 51)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008'] = {'inputs': ['isl_071_insider_buy_cluster_1008'], 'func': isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008}


def isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260(isl_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(isl_072_insider_net_buy_ratio_1260, 52)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260'] = {'inputs': ['isl_072_insider_net_buy_ratio_1260'], 'func': isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260}


def isl_base_universe_d2_053_isl_073_insider_value_ratio_1512(isl_073_insider_value_ratio_1512):
    return _base_universe_d2(isl_073_insider_value_ratio_1512, 53)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_053_isl_073_insider_value_ratio_1512'] = {'inputs': ['isl_073_insider_value_ratio_1512'], 'func': isl_base_universe_d2_053_isl_073_insider_value_ratio_1512}


def isl_base_universe_d2_054_isl_basefill_005(isl_basefill_005):
    return _base_universe_d2(isl_basefill_005, 54)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_054_isl_basefill_005'] = {'inputs': ['isl_basefill_005'], 'func': isl_base_universe_d2_054_isl_basefill_005}


def isl_base_universe_d2_055_isl_basefill_012(isl_basefill_012):
    return _base_universe_d2(isl_basefill_012, 55)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_055_isl_basefill_012'] = {'inputs': ['isl_basefill_012'], 'func': isl_base_universe_d2_055_isl_basefill_012}


def isl_base_universe_d2_056_isl_basefill_019(isl_basefill_019):
    return _base_universe_d2(isl_basefill_019, 56)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_056_isl_basefill_019'] = {'inputs': ['isl_basefill_019'], 'func': isl_base_universe_d2_056_isl_basefill_019}


def isl_base_universe_d2_057_isl_basefill_022(isl_basefill_022):
    return _base_universe_d2(isl_basefill_022, 57)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_057_isl_basefill_022'] = {'inputs': ['isl_basefill_022'], 'func': isl_base_universe_d2_057_isl_basefill_022}


def isl_base_universe_d2_058_isl_basefill_026(isl_basefill_026):
    return _base_universe_d2(isl_basefill_026, 58)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_058_isl_basefill_026'] = {'inputs': ['isl_basefill_026'], 'func': isl_base_universe_d2_058_isl_basefill_026}


def isl_base_universe_d2_059_isl_basefill_033(isl_basefill_033):
    return _base_universe_d2(isl_basefill_033, 59)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_059_isl_basefill_033'] = {'inputs': ['isl_basefill_033'], 'func': isl_base_universe_d2_059_isl_basefill_033}


def isl_base_universe_d2_060_isl_basefill_037(isl_basefill_037):
    return _base_universe_d2(isl_basefill_037, 60)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_060_isl_basefill_037'] = {'inputs': ['isl_basefill_037'], 'func': isl_base_universe_d2_060_isl_basefill_037}


def isl_base_universe_d2_061_isl_basefill_040(isl_basefill_040):
    return _base_universe_d2(isl_basefill_040, 61)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_061_isl_basefill_040'] = {'inputs': ['isl_basefill_040'], 'func': isl_base_universe_d2_061_isl_basefill_040}


def isl_base_universe_d2_062_isl_basefill_047(isl_basefill_047):
    return _base_universe_d2(isl_basefill_047, 62)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_062_isl_basefill_047'] = {'inputs': ['isl_basefill_047'], 'func': isl_base_universe_d2_062_isl_basefill_047}


def isl_base_universe_d2_063_isl_basefill_052(isl_basefill_052):
    return _base_universe_d2(isl_basefill_052, 63)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_063_isl_basefill_052'] = {'inputs': ['isl_basefill_052'], 'func': isl_base_universe_d2_063_isl_basefill_052}


def isl_base_universe_d2_064_isl_basefill_054(isl_basefill_054):
    return _base_universe_d2(isl_basefill_054, 64)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_064_isl_basefill_054'] = {'inputs': ['isl_basefill_054'], 'func': isl_base_universe_d2_064_isl_basefill_054}


def isl_base_universe_d2_065_isl_basefill_059(isl_basefill_059):
    return _base_universe_d2(isl_basefill_059, 65)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_065_isl_basefill_059'] = {'inputs': ['isl_basefill_059'], 'func': isl_base_universe_d2_065_isl_basefill_059}


def isl_base_universe_d2_066_isl_basefill_061(isl_basefill_061):
    return _base_universe_d2(isl_basefill_061, 66)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_066_isl_basefill_061'] = {'inputs': ['isl_basefill_061'], 'func': isl_base_universe_d2_066_isl_basefill_061}


def isl_base_universe_d2_067_isl_basefill_063(isl_basefill_063):
    return _base_universe_d2(isl_basefill_063, 67)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_067_isl_basefill_063'] = {'inputs': ['isl_basefill_063'], 'func': isl_base_universe_d2_067_isl_basefill_063}


def isl_base_universe_d2_068_isl_basefill_067(isl_basefill_067):
    return _base_universe_d2(isl_basefill_067, 68)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_068_isl_basefill_067'] = {'inputs': ['isl_basefill_067'], 'func': isl_base_universe_d2_068_isl_basefill_067}


def isl_base_universe_d2_069_isl_basefill_068(isl_basefill_068):
    return _base_universe_d2(isl_basefill_068, 69)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_069_isl_basefill_068'] = {'inputs': ['isl_basefill_068'], 'func': isl_base_universe_d2_069_isl_basefill_068}


def isl_base_universe_d2_070_isl_basefill_074(isl_basefill_074):
    return _base_universe_d2(isl_basefill_074, 70)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_070_isl_basefill_074'] = {'inputs': ['isl_basefill_074'], 'func': isl_base_universe_d2_070_isl_basefill_074}


def isl_base_universe_d2_071_isl_basefill_075(isl_basefill_075):
    return _base_universe_d2(isl_basefill_075, 71)
ISL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['isl_base_universe_d2_071_isl_basefill_075'] = {'inputs': ['isl_basefill_075'], 'func': isl_base_universe_d2_071_isl_basefill_075}
