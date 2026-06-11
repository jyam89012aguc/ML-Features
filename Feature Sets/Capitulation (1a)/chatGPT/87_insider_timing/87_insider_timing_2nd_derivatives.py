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



def itm_151_itm_001_insider_buy_cluster_21_roc_1(itm_001_insider_buy_cluster_21):
    feature = _s(itm_001_insider_buy_cluster_21)
    return (_roc(feature, 1)).reindex(feature.index)

def itm_152_itm_007_insider_silence_252_roc_42(itm_007_insider_silence_252):
    feature = _s(itm_007_insider_silence_252)
    return (_roc(feature, 42)).reindex(feature.index)

def itm_153_itm_013_insider_conviction_1512_roc_126(itm_013_insider_conviction_1512):
    feature = _s(itm_013_insider_conviction_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def itm_154_itm_019_insider_activity_accel_1_roc_378(itm_019_insider_activity_accel_1):
    feature = _s(itm_019_insider_activity_accel_1)
    return (_roc(feature, 378)).reindex(feature.index)

def itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4(itm_025_ceo_cfo_buy_weight_756):
    feature = _s(itm_025_ceo_cfo_buy_weight_756)
    return (_roc(feature, 4)).reindex(feature.index)






















INSIDER_TIMING_REGISTRY_2ND_DERIVATIVES = {
    'itm_151_itm_001_insider_buy_cluster_21_roc_1': {'inputs': ['itm_001_insider_buy_cluster_21'], 'func': itm_151_itm_001_insider_buy_cluster_21_roc_1},
    'itm_152_itm_007_insider_silence_252_roc_42': {'inputs': ['itm_007_insider_silence_252'], 'func': itm_152_itm_007_insider_silence_252_roc_42},
    'itm_153_itm_013_insider_conviction_1512_roc_126': {'inputs': ['itm_013_insider_conviction_1512'], 'func': itm_153_itm_013_insider_conviction_1512_roc_126},
    'itm_154_itm_019_insider_activity_accel_1_roc_378': {'inputs': ['itm_019_insider_activity_accel_1'], 'func': itm_154_itm_019_insider_activity_accel_1_roc_378},
    'itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4': {'inputs': ['itm_025_ceo_cfo_buy_weight_756'], 'func': itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def it_replacement_d2_001(itm_019_insider_activity_accel_1):
    feature = _clean(itm_019_insider_activity_accel_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_001'] = {'inputs': ['itm_019_insider_activity_accel_1'], 'func': it_replacement_d2_001}


def it_replacement_d2_002(it_replacement_001):
    feature = _clean(it_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_002'] = {'inputs': ['it_replacement_001'], 'func': it_replacement_d2_002}


def it_replacement_d2_003(it_replacement_002):
    feature = _clean(it_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_003'] = {'inputs': ['it_replacement_002'], 'func': it_replacement_d2_003}


def it_replacement_d2_004(it_replacement_003):
    feature = _clean(it_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_004'] = {'inputs': ['it_replacement_003'], 'func': it_replacement_d2_004}


def it_replacement_d2_005(it_replacement_004):
    feature = _clean(it_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_005'] = {'inputs': ['it_replacement_004'], 'func': it_replacement_d2_005}


def it_replacement_d2_006(it_replacement_005):
    feature = _clean(it_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_006'] = {'inputs': ['it_replacement_005'], 'func': it_replacement_d2_006}


def it_replacement_d2_007(it_replacement_006):
    feature = _clean(it_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_007'] = {'inputs': ['it_replacement_006'], 'func': it_replacement_d2_007}


def it_replacement_d2_008(it_replacement_007):
    feature = _clean(it_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_008'] = {'inputs': ['it_replacement_007'], 'func': it_replacement_d2_008}


def it_replacement_d2_009(it_replacement_008):
    feature = _clean(it_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_009'] = {'inputs': ['it_replacement_008'], 'func': it_replacement_d2_009}


def it_replacement_d2_010(it_replacement_009):
    feature = _clean(it_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_010'] = {'inputs': ['it_replacement_009'], 'func': it_replacement_d2_010}


def it_replacement_d2_011(it_replacement_010):
    feature = _clean(it_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_011'] = {'inputs': ['it_replacement_010'], 'func': it_replacement_d2_011}


def it_replacement_d2_012(it_replacement_011):
    feature = _clean(it_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_012'] = {'inputs': ['it_replacement_011'], 'func': it_replacement_d2_012}


def it_replacement_d2_013(it_replacement_012):
    feature = _clean(it_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_013'] = {'inputs': ['it_replacement_012'], 'func': it_replacement_d2_013}


def it_replacement_d2_014(it_replacement_013):
    feature = _clean(it_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_014'] = {'inputs': ['it_replacement_013'], 'func': it_replacement_d2_014}


def it_replacement_d2_015(it_replacement_014):
    feature = _clean(it_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_015'] = {'inputs': ['it_replacement_014'], 'func': it_replacement_d2_015}


def it_replacement_d2_016(it_replacement_015):
    feature = _clean(it_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_016'] = {'inputs': ['it_replacement_015'], 'func': it_replacement_d2_016}


def it_replacement_d2_017(it_replacement_016):
    feature = _clean(it_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_017'] = {'inputs': ['it_replacement_016'], 'func': it_replacement_d2_017}


def it_replacement_d2_018(it_replacement_017):
    feature = _clean(it_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_018'] = {'inputs': ['it_replacement_017'], 'func': it_replacement_d2_018}


def it_replacement_d2_019(it_replacement_018):
    feature = _clean(it_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_019'] = {'inputs': ['it_replacement_018'], 'func': it_replacement_d2_019}


def it_replacement_d2_020(it_replacement_019):
    feature = _clean(it_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_020'] = {'inputs': ['it_replacement_019'], 'func': it_replacement_d2_020}


def it_replacement_d2_021(it_replacement_020):
    feature = _clean(it_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_021'] = {'inputs': ['it_replacement_020'], 'func': it_replacement_d2_021}


def it_replacement_d2_022(it_replacement_021):
    feature = _clean(it_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_022'] = {'inputs': ['it_replacement_021'], 'func': it_replacement_d2_022}


def it_replacement_d2_023(it_replacement_022):
    feature = _clean(it_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_023'] = {'inputs': ['it_replacement_022'], 'func': it_replacement_d2_023}


def it_replacement_d2_024(it_replacement_023):
    feature = _clean(it_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_024'] = {'inputs': ['it_replacement_023'], 'func': it_replacement_d2_024}


def it_replacement_d2_025(it_replacement_024):
    feature = _clean(it_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_025'] = {'inputs': ['it_replacement_024'], 'func': it_replacement_d2_025}


def it_replacement_d2_026(it_replacement_025):
    feature = _clean(it_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_026'] = {'inputs': ['it_replacement_025'], 'func': it_replacement_d2_026}


def it_replacement_d2_027(it_replacement_026):
    feature = _clean(it_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_027'] = {'inputs': ['it_replacement_026'], 'func': it_replacement_d2_027}


def it_replacement_d2_028(it_replacement_027):
    feature = _clean(it_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_028'] = {'inputs': ['it_replacement_027'], 'func': it_replacement_d2_028}


def it_replacement_d2_029(it_replacement_028):
    feature = _clean(it_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_029'] = {'inputs': ['it_replacement_028'], 'func': it_replacement_d2_029}


def it_replacement_d2_030(it_replacement_029):
    feature = _clean(it_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_030'] = {'inputs': ['it_replacement_029'], 'func': it_replacement_d2_030}


def it_replacement_d2_031(it_replacement_030):
    feature = _clean(it_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_031'] = {'inputs': ['it_replacement_030'], 'func': it_replacement_d2_031}


def it_replacement_d2_032(it_replacement_031):
    feature = _clean(it_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_032'] = {'inputs': ['it_replacement_031'], 'func': it_replacement_d2_032}


def it_replacement_d2_033(it_replacement_032):
    feature = _clean(it_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_033'] = {'inputs': ['it_replacement_032'], 'func': it_replacement_d2_033}


def it_replacement_d2_034(it_replacement_033):
    feature = _clean(it_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_034'] = {'inputs': ['it_replacement_033'], 'func': it_replacement_d2_034}


def it_replacement_d2_035(it_replacement_034):
    feature = _clean(it_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_035'] = {'inputs': ['it_replacement_034'], 'func': it_replacement_d2_035}


def it_replacement_d2_036(it_replacement_035):
    feature = _clean(it_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_036'] = {'inputs': ['it_replacement_035'], 'func': it_replacement_d2_036}


def it_replacement_d2_037(it_replacement_036):
    feature = _clean(it_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_037'] = {'inputs': ['it_replacement_036'], 'func': it_replacement_d2_037}


def it_replacement_d2_038(it_replacement_037):
    feature = _clean(it_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_038'] = {'inputs': ['it_replacement_037'], 'func': it_replacement_d2_038}


def it_replacement_d2_039(it_replacement_038):
    feature = _clean(it_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_039'] = {'inputs': ['it_replacement_038'], 'func': it_replacement_d2_039}


def it_replacement_d2_040(it_replacement_039):
    feature = _clean(it_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_040'] = {'inputs': ['it_replacement_039'], 'func': it_replacement_d2_040}


def it_replacement_d2_041(it_replacement_040):
    feature = _clean(it_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_041'] = {'inputs': ['it_replacement_040'], 'func': it_replacement_d2_041}


def it_replacement_d2_042(it_replacement_041):
    feature = _clean(it_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_042'] = {'inputs': ['it_replacement_041'], 'func': it_replacement_d2_042}


def it_replacement_d2_043(it_replacement_042):
    feature = _clean(it_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_043'] = {'inputs': ['it_replacement_042'], 'func': it_replacement_d2_043}


def it_replacement_d2_044(it_replacement_043):
    feature = _clean(it_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_044'] = {'inputs': ['it_replacement_043'], 'func': it_replacement_d2_044}


def it_replacement_d2_045(it_replacement_044):
    feature = _clean(it_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_045'] = {'inputs': ['it_replacement_044'], 'func': it_replacement_d2_045}


def it_replacement_d2_046(it_replacement_045):
    feature = _clean(it_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_046'] = {'inputs': ['it_replacement_045'], 'func': it_replacement_d2_046}


def it_replacement_d2_047(it_replacement_046):
    feature = _clean(it_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_047'] = {'inputs': ['it_replacement_046'], 'func': it_replacement_d2_047}


def it_replacement_d2_048(it_replacement_047):
    feature = _clean(it_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_048'] = {'inputs': ['it_replacement_047'], 'func': it_replacement_d2_048}


def it_replacement_d2_049(it_replacement_048):
    feature = _clean(it_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_049'] = {'inputs': ['it_replacement_048'], 'func': it_replacement_d2_049}


def it_replacement_d2_050(it_replacement_049):
    feature = _clean(it_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_050'] = {'inputs': ['it_replacement_049'], 'func': it_replacement_d2_050}


def it_replacement_d2_051(it_replacement_050):
    feature = _clean(it_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_051'] = {'inputs': ['it_replacement_050'], 'func': it_replacement_d2_051}


def it_replacement_d2_052(it_replacement_051):
    feature = _clean(it_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_052'] = {'inputs': ['it_replacement_051'], 'func': it_replacement_d2_052}


def it_replacement_d2_053(it_replacement_052):
    feature = _clean(it_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_053'] = {'inputs': ['it_replacement_052'], 'func': it_replacement_d2_053}


def it_replacement_d2_054(it_replacement_053):
    feature = _clean(it_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_054'] = {'inputs': ['it_replacement_053'], 'func': it_replacement_d2_054}


def it_replacement_d2_055(it_replacement_054):
    feature = _clean(it_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_055'] = {'inputs': ['it_replacement_054'], 'func': it_replacement_d2_055}


def it_replacement_d2_056(it_replacement_055):
    feature = _clean(it_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_056'] = {'inputs': ['it_replacement_055'], 'func': it_replacement_d2_056}


def it_replacement_d2_057(it_replacement_056):
    feature = _clean(it_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_057'] = {'inputs': ['it_replacement_056'], 'func': it_replacement_d2_057}


def it_replacement_d2_058(it_replacement_057):
    feature = _clean(it_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_058'] = {'inputs': ['it_replacement_057'], 'func': it_replacement_d2_058}


def it_replacement_d2_059(it_replacement_058):
    feature = _clean(it_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_059'] = {'inputs': ['it_replacement_058'], 'func': it_replacement_d2_059}


def it_replacement_d2_060(it_replacement_059):
    feature = _clean(it_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_060'] = {'inputs': ['it_replacement_059'], 'func': it_replacement_d2_060}


def it_replacement_d2_061(it_replacement_060):
    feature = _clean(it_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_061'] = {'inputs': ['it_replacement_060'], 'func': it_replacement_d2_061}


def it_replacement_d2_062(it_replacement_061):
    feature = _clean(it_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_062'] = {'inputs': ['it_replacement_061'], 'func': it_replacement_d2_062}


def it_replacement_d2_063(it_replacement_062):
    feature = _clean(it_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_063'] = {'inputs': ['it_replacement_062'], 'func': it_replacement_d2_063}


def it_replacement_d2_064(it_replacement_063):
    feature = _clean(it_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_064'] = {'inputs': ['it_replacement_063'], 'func': it_replacement_d2_064}


def it_replacement_d2_065(it_replacement_064):
    feature = _clean(it_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_065'] = {'inputs': ['it_replacement_064'], 'func': it_replacement_d2_065}


def it_replacement_d2_066(it_replacement_065):
    feature = _clean(it_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_066'] = {'inputs': ['it_replacement_065'], 'func': it_replacement_d2_066}


def it_replacement_d2_067(it_replacement_066):
    feature = _clean(it_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_067'] = {'inputs': ['it_replacement_066'], 'func': it_replacement_d2_067}


def it_replacement_d2_068(it_replacement_067):
    feature = _clean(it_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_068'] = {'inputs': ['it_replacement_067'], 'func': it_replacement_d2_068}


def it_replacement_d2_069(it_replacement_068):
    feature = _clean(it_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_069'] = {'inputs': ['it_replacement_068'], 'func': it_replacement_d2_069}


def it_replacement_d2_070(it_replacement_069):
    feature = _clean(it_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_070'] = {'inputs': ['it_replacement_069'], 'func': it_replacement_d2_070}


def it_replacement_d2_071(it_replacement_070):
    feature = _clean(it_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_071'] = {'inputs': ['it_replacement_070'], 'func': it_replacement_d2_071}


def it_replacement_d2_072(it_replacement_071):
    feature = _clean(it_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_072'] = {'inputs': ['it_replacement_071'], 'func': it_replacement_d2_072}


def it_replacement_d2_073(it_replacement_072):
    feature = _clean(it_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_073'] = {'inputs': ['it_replacement_072'], 'func': it_replacement_d2_073}


def it_replacement_d2_074(it_replacement_073):
    feature = _clean(it_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_074'] = {'inputs': ['it_replacement_073'], 'func': it_replacement_d2_074}


def it_replacement_d2_075(it_replacement_074):
    feature = _clean(it_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_075'] = {'inputs': ['it_replacement_074'], 'func': it_replacement_d2_075}


def it_replacement_d2_076(it_replacement_075):
    feature = _clean(it_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_076'] = {'inputs': ['it_replacement_075'], 'func': it_replacement_d2_076}


def it_replacement_d2_077(it_replacement_076):
    feature = _clean(it_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_077'] = {'inputs': ['it_replacement_076'], 'func': it_replacement_d2_077}


def it_replacement_d2_078(it_replacement_077):
    feature = _clean(it_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_078'] = {'inputs': ['it_replacement_077'], 'func': it_replacement_d2_078}


def it_replacement_d2_079(it_replacement_078):
    feature = _clean(it_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_079'] = {'inputs': ['it_replacement_078'], 'func': it_replacement_d2_079}


def it_replacement_d2_080(it_replacement_079):
    feature = _clean(it_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_080'] = {'inputs': ['it_replacement_079'], 'func': it_replacement_d2_080}


def it_replacement_d2_081(it_replacement_080):
    feature = _clean(it_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_081'] = {'inputs': ['it_replacement_080'], 'func': it_replacement_d2_081}


def it_replacement_d2_082(it_replacement_081):
    feature = _clean(it_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_082'] = {'inputs': ['it_replacement_081'], 'func': it_replacement_d2_082}


def it_replacement_d2_083(it_replacement_082):
    feature = _clean(it_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_083'] = {'inputs': ['it_replacement_082'], 'func': it_replacement_d2_083}


def it_replacement_d2_084(it_replacement_083):
    feature = _clean(it_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_084'] = {'inputs': ['it_replacement_083'], 'func': it_replacement_d2_084}


def it_replacement_d2_085(it_replacement_084):
    feature = _clean(it_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_085'] = {'inputs': ['it_replacement_084'], 'func': it_replacement_d2_085}


def it_replacement_d2_086(it_replacement_085):
    feature = _clean(it_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_086'] = {'inputs': ['it_replacement_085'], 'func': it_replacement_d2_086}


def it_replacement_d2_087(it_replacement_086):
    feature = _clean(it_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_087'] = {'inputs': ['it_replacement_086'], 'func': it_replacement_d2_087}


def it_replacement_d2_088(it_replacement_087):
    feature = _clean(it_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_088'] = {'inputs': ['it_replacement_087'], 'func': it_replacement_d2_088}


def it_replacement_d2_089(it_replacement_088):
    feature = _clean(it_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_089'] = {'inputs': ['it_replacement_088'], 'func': it_replacement_d2_089}


def it_replacement_d2_090(it_replacement_089):
    feature = _clean(it_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_090'] = {'inputs': ['it_replacement_089'], 'func': it_replacement_d2_090}


def it_replacement_d2_091(it_replacement_090):
    feature = _clean(it_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_091'] = {'inputs': ['it_replacement_090'], 'func': it_replacement_d2_091}


def it_replacement_d2_092(it_replacement_091):
    feature = _clean(it_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_092'] = {'inputs': ['it_replacement_091'], 'func': it_replacement_d2_092}


def it_replacement_d2_093(it_replacement_092):
    feature = _clean(it_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_093'] = {'inputs': ['it_replacement_092'], 'func': it_replacement_d2_093}


def it_replacement_d2_094(it_replacement_093):
    feature = _clean(it_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_094'] = {'inputs': ['it_replacement_093'], 'func': it_replacement_d2_094}


def it_replacement_d2_095(it_replacement_094):
    feature = _clean(it_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_095'] = {'inputs': ['it_replacement_094'], 'func': it_replacement_d2_095}


def it_replacement_d2_096(it_replacement_095):
    feature = _clean(it_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_096'] = {'inputs': ['it_replacement_095'], 'func': it_replacement_d2_096}


def it_replacement_d2_097(it_replacement_096):
    feature = _clean(it_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_097'] = {'inputs': ['it_replacement_096'], 'func': it_replacement_d2_097}


def it_replacement_d2_098(it_replacement_097):
    feature = _clean(it_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_098'] = {'inputs': ['it_replacement_097'], 'func': it_replacement_d2_098}


def it_replacement_d2_099(it_replacement_098):
    feature = _clean(it_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_099'] = {'inputs': ['it_replacement_098'], 'func': it_replacement_d2_099}


def it_replacement_d2_100(it_replacement_099):
    feature = _clean(it_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_100'] = {'inputs': ['it_replacement_099'], 'func': it_replacement_d2_100}


def it_replacement_d2_101(it_replacement_100):
    feature = _clean(it_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_101'] = {'inputs': ['it_replacement_100'], 'func': it_replacement_d2_101}


def it_replacement_d2_102(it_replacement_101):
    feature = _clean(it_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_102'] = {'inputs': ['it_replacement_101'], 'func': it_replacement_d2_102}


def it_replacement_d2_103(it_replacement_102):
    feature = _clean(it_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_103'] = {'inputs': ['it_replacement_102'], 'func': it_replacement_d2_103}


def it_replacement_d2_104(it_replacement_103):
    feature = _clean(it_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_104'] = {'inputs': ['it_replacement_103'], 'func': it_replacement_d2_104}


def it_replacement_d2_105(it_replacement_104):
    feature = _clean(it_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_105'] = {'inputs': ['it_replacement_104'], 'func': it_replacement_d2_105}


def it_replacement_d2_106(it_replacement_105):
    feature = _clean(it_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_106'] = {'inputs': ['it_replacement_105'], 'func': it_replacement_d2_106}


def it_replacement_d2_107(it_replacement_106):
    feature = _clean(it_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_107'] = {'inputs': ['it_replacement_106'], 'func': it_replacement_d2_107}


def it_replacement_d2_108(it_replacement_107):
    feature = _clean(it_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_108'] = {'inputs': ['it_replacement_107'], 'func': it_replacement_d2_108}


def it_replacement_d2_109(it_replacement_108):
    feature = _clean(it_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_109'] = {'inputs': ['it_replacement_108'], 'func': it_replacement_d2_109}


def it_replacement_d2_110(it_replacement_109):
    feature = _clean(it_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_110'] = {'inputs': ['it_replacement_109'], 'func': it_replacement_d2_110}


def it_replacement_d2_111(it_replacement_110):
    feature = _clean(it_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_111'] = {'inputs': ['it_replacement_110'], 'func': it_replacement_d2_111}


def it_replacement_d2_112(it_replacement_111):
    feature = _clean(it_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['it_replacement_d2_112'] = {'inputs': ['it_replacement_111'], 'func': it_replacement_d2_112}


# Base-universe derivative extensions for repaired first-base features.
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42(itm_002_insider_net_buy_ratio_42):
    return _base_universe_d2(itm_002_insider_net_buy_ratio_42, 1)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42'] = {'inputs': ['itm_002_insider_net_buy_ratio_42'], 'func': itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42}


def itm_base_universe_d2_002_itm_003_insider_value_ratio_63(itm_003_insider_value_ratio_63):
    return _base_universe_d2(itm_003_insider_value_ratio_63, 2)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_002_itm_003_insider_value_ratio_63'] = {'inputs': ['itm_003_insider_value_ratio_63'], 'func': itm_base_universe_d2_002_itm_003_insider_value_ratio_63}


def itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84(itm_004_ceo_cfo_buy_weight_84):
    return _base_universe_d2(itm_004_ceo_cfo_buy_weight_84, 3)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84'] = {'inputs': ['itm_004_ceo_cfo_buy_weight_84'], 'func': itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84}


def itm_base_universe_d2_004_itm_006_insider_conviction_189(itm_006_insider_conviction_189):
    return _base_universe_d2(itm_006_insider_conviction_189, 4)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_004_itm_006_insider_conviction_189'] = {'inputs': ['itm_006_insider_conviction_189'], 'func': itm_base_universe_d2_004_itm_006_insider_conviction_189}


def itm_base_universe_d2_005_itm_008_insider_buy_cluster_378(itm_008_insider_buy_cluster_378):
    return _base_universe_d2(itm_008_insider_buy_cluster_378, 5)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_005_itm_008_insider_buy_cluster_378'] = {'inputs': ['itm_008_insider_buy_cluster_378'], 'func': itm_base_universe_d2_005_itm_008_insider_buy_cluster_378}


def itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504(itm_009_insider_net_buy_ratio_504):
    return _base_universe_d2(itm_009_insider_net_buy_ratio_504, 6)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504'] = {'inputs': ['itm_009_insider_net_buy_ratio_504'], 'func': itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504}


def itm_base_universe_d2_007_itm_010_insider_value_ratio_756(itm_010_insider_value_ratio_756):
    return _base_universe_d2(itm_010_insider_value_ratio_756, 7)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_007_itm_010_insider_value_ratio_756'] = {'inputs': ['itm_010_insider_value_ratio_756'], 'func': itm_base_universe_d2_007_itm_010_insider_value_ratio_756}


def itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008(itm_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d2(itm_011_ceo_cfo_buy_weight_1008, 8)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['itm_011_ceo_cfo_buy_weight_1008'], 'func': itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008}


def itm_base_universe_d2_009_itm_014_insider_silence_63(itm_014_insider_silence_63):
    return _base_universe_d2(itm_014_insider_silence_63, 9)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_009_itm_014_insider_silence_63'] = {'inputs': ['itm_014_insider_silence_63'], 'func': itm_base_universe_d2_009_itm_014_insider_silence_63}


def itm_base_universe_d2_010_itm_015_insider_buy_cluster_252(itm_015_insider_buy_cluster_252):
    return _base_universe_d2(itm_015_insider_buy_cluster_252, 10)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_010_itm_015_insider_buy_cluster_252'] = {'inputs': ['itm_015_insider_buy_cluster_252'], 'func': itm_base_universe_d2_010_itm_015_insider_buy_cluster_252}


def itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21(itm_016_insider_net_buy_ratio_21):
    return _base_universe_d2(itm_016_insider_net_buy_ratio_21, 11)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21'] = {'inputs': ['itm_016_insider_net_buy_ratio_21'], 'func': itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21}


def itm_base_universe_d2_012_itm_017_insider_value_ratio_42(itm_017_insider_value_ratio_42):
    return _base_universe_d2(itm_017_insider_value_ratio_42, 12)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_012_itm_017_insider_value_ratio_42'] = {'inputs': ['itm_017_insider_value_ratio_42'], 'func': itm_base_universe_d2_012_itm_017_insider_value_ratio_42}


def itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63(itm_018_ceo_cfo_buy_weight_63):
    return _base_universe_d2(itm_018_ceo_cfo_buy_weight_63, 13)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63'] = {'inputs': ['itm_018_ceo_cfo_buy_weight_63'], 'func': itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63}


def itm_base_universe_d2_014_itm_020_insider_conviction_126(itm_020_insider_conviction_126):
    return _base_universe_d2(itm_020_insider_conviction_126, 14)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_014_itm_020_insider_conviction_126'] = {'inputs': ['itm_020_insider_conviction_126'], 'func': itm_base_universe_d2_014_itm_020_insider_conviction_126}


def itm_base_universe_d2_015_itm_021_insider_silence_189(itm_021_insider_silence_189):
    return _base_universe_d2(itm_021_insider_silence_189, 15)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_015_itm_021_insider_silence_189'] = {'inputs': ['itm_021_insider_silence_189'], 'func': itm_base_universe_d2_015_itm_021_insider_silence_189}


def itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378(itm_023_insider_net_buy_ratio_378):
    return _base_universe_d2(itm_023_insider_net_buy_ratio_378, 16)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378'] = {'inputs': ['itm_023_insider_net_buy_ratio_378'], 'func': itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378}


def itm_base_universe_d2_017_itm_024_insider_value_ratio_504(itm_024_insider_value_ratio_504):
    return _base_universe_d2(itm_024_insider_value_ratio_504, 17)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_017_itm_024_insider_value_ratio_504'] = {'inputs': ['itm_024_insider_value_ratio_504'], 'func': itm_base_universe_d2_017_itm_024_insider_value_ratio_504}


def itm_base_universe_d2_018_itm_027_insider_conviction_1260(itm_027_insider_conviction_1260):
    return _base_universe_d2(itm_027_insider_conviction_1260, 18)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_018_itm_027_insider_conviction_1260'] = {'inputs': ['itm_027_insider_conviction_1260'], 'func': itm_base_universe_d2_018_itm_027_insider_conviction_1260}


def itm_base_universe_d2_019_itm_028_insider_silence_1512(itm_028_insider_silence_1512):
    return _base_universe_d2(itm_028_insider_silence_1512, 19)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_019_itm_028_insider_silence_1512'] = {'inputs': ['itm_028_insider_silence_1512'], 'func': itm_base_universe_d2_019_itm_028_insider_silence_1512}


def itm_base_universe_d2_020_itm_029_insider_buy_cluster_63(itm_029_insider_buy_cluster_63):
    return _base_universe_d2(itm_029_insider_buy_cluster_63, 20)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_020_itm_029_insider_buy_cluster_63'] = {'inputs': ['itm_029_insider_buy_cluster_63'], 'func': itm_base_universe_d2_020_itm_029_insider_buy_cluster_63}


def itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252(itm_030_insider_net_buy_ratio_252):
    return _base_universe_d2(itm_030_insider_net_buy_ratio_252, 21)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252'] = {'inputs': ['itm_030_insider_net_buy_ratio_252'], 'func': itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252}


def itm_base_universe_d2_022_itm_031_insider_value_ratio_21(itm_031_insider_value_ratio_21):
    return _base_universe_d2(itm_031_insider_value_ratio_21, 22)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_022_itm_031_insider_value_ratio_21'] = {'inputs': ['itm_031_insider_value_ratio_21'], 'func': itm_base_universe_d2_022_itm_031_insider_value_ratio_21}


def itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42(itm_032_ceo_cfo_buy_weight_42):
    return _base_universe_d2(itm_032_ceo_cfo_buy_weight_42, 23)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42'] = {'inputs': ['itm_032_ceo_cfo_buy_weight_42'], 'func': itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42}


def itm_base_universe_d2_024_itm_034_insider_conviction_84(itm_034_insider_conviction_84):
    return _base_universe_d2(itm_034_insider_conviction_84, 24)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_024_itm_034_insider_conviction_84'] = {'inputs': ['itm_034_insider_conviction_84'], 'func': itm_base_universe_d2_024_itm_034_insider_conviction_84}


def itm_base_universe_d2_025_itm_035_insider_silence_126(itm_035_insider_silence_126):
    return _base_universe_d2(itm_035_insider_silence_126, 25)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_025_itm_035_insider_silence_126'] = {'inputs': ['itm_035_insider_silence_126'], 'func': itm_base_universe_d2_025_itm_035_insider_silence_126}


def itm_base_universe_d2_026_itm_036_insider_buy_cluster_189(itm_036_insider_buy_cluster_189):
    return _base_universe_d2(itm_036_insider_buy_cluster_189, 26)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_026_itm_036_insider_buy_cluster_189'] = {'inputs': ['itm_036_insider_buy_cluster_189'], 'func': itm_base_universe_d2_026_itm_036_insider_buy_cluster_189}


def itm_base_universe_d2_027_itm_038_insider_value_ratio_378(itm_038_insider_value_ratio_378):
    return _base_universe_d2(itm_038_insider_value_ratio_378, 27)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_027_itm_038_insider_value_ratio_378'] = {'inputs': ['itm_038_insider_value_ratio_378'], 'func': itm_base_universe_d2_027_itm_038_insider_value_ratio_378}


def itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504(itm_039_ceo_cfo_buy_weight_504):
    return _base_universe_d2(itm_039_ceo_cfo_buy_weight_504, 28)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504'] = {'inputs': ['itm_039_ceo_cfo_buy_weight_504'], 'func': itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504}


def itm_base_universe_d2_029_itm_041_insider_conviction_1008(itm_041_insider_conviction_1008):
    return _base_universe_d2(itm_041_insider_conviction_1008, 29)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_029_itm_041_insider_conviction_1008'] = {'inputs': ['itm_041_insider_conviction_1008'], 'func': itm_base_universe_d2_029_itm_041_insider_conviction_1008}


def itm_base_universe_d2_030_itm_042_insider_silence_1260(itm_042_insider_silence_1260):
    return _base_universe_d2(itm_042_insider_silence_1260, 30)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_030_itm_042_insider_silence_1260'] = {'inputs': ['itm_042_insider_silence_1260'], 'func': itm_base_universe_d2_030_itm_042_insider_silence_1260}


def itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512(itm_043_insider_buy_cluster_1512):
    return _base_universe_d2(itm_043_insider_buy_cluster_1512, 31)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512'] = {'inputs': ['itm_043_insider_buy_cluster_1512'], 'func': itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512}


def itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63(itm_044_insider_net_buy_ratio_63):
    return _base_universe_d2(itm_044_insider_net_buy_ratio_63, 32)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63'] = {'inputs': ['itm_044_insider_net_buy_ratio_63'], 'func': itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63}


def itm_base_universe_d2_033_itm_045_insider_value_ratio_252(itm_045_insider_value_ratio_252):
    return _base_universe_d2(itm_045_insider_value_ratio_252, 33)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_033_itm_045_insider_value_ratio_252'] = {'inputs': ['itm_045_insider_value_ratio_252'], 'func': itm_base_universe_d2_033_itm_045_insider_value_ratio_252}


def itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21(itm_046_ceo_cfo_buy_weight_21):
    return _base_universe_d2(itm_046_ceo_cfo_buy_weight_21, 34)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21'] = {'inputs': ['itm_046_ceo_cfo_buy_weight_21'], 'func': itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21}


def itm_base_universe_d2_035_itm_048_insider_conviction_63(itm_048_insider_conviction_63):
    return _base_universe_d2(itm_048_insider_conviction_63, 35)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_035_itm_048_insider_conviction_63'] = {'inputs': ['itm_048_insider_conviction_63'], 'func': itm_base_universe_d2_035_itm_048_insider_conviction_63}


def itm_base_universe_d2_036_itm_049_insider_silence_84(itm_049_insider_silence_84):
    return _base_universe_d2(itm_049_insider_silence_84, 36)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_036_itm_049_insider_silence_84'] = {'inputs': ['itm_049_insider_silence_84'], 'func': itm_base_universe_d2_036_itm_049_insider_silence_84}


def itm_base_universe_d2_037_itm_050_insider_buy_cluster_126(itm_050_insider_buy_cluster_126):
    return _base_universe_d2(itm_050_insider_buy_cluster_126, 37)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_037_itm_050_insider_buy_cluster_126'] = {'inputs': ['itm_050_insider_buy_cluster_126'], 'func': itm_base_universe_d2_037_itm_050_insider_buy_cluster_126}


def itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189(itm_051_insider_net_buy_ratio_189):
    return _base_universe_d2(itm_051_insider_net_buy_ratio_189, 38)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189'] = {'inputs': ['itm_051_insider_net_buy_ratio_189'], 'func': itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189}


def itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378(itm_053_ceo_cfo_buy_weight_378):
    return _base_universe_d2(itm_053_ceo_cfo_buy_weight_378, 39)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378'] = {'inputs': ['itm_053_ceo_cfo_buy_weight_378'], 'func': itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378}


def itm_base_universe_d2_040_itm_055_insider_conviction_756(itm_055_insider_conviction_756):
    return _base_universe_d2(itm_055_insider_conviction_756, 40)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_040_itm_055_insider_conviction_756'] = {'inputs': ['itm_055_insider_conviction_756'], 'func': itm_base_universe_d2_040_itm_055_insider_conviction_756}


def itm_base_universe_d2_041_itm_056_insider_silence_1008(itm_056_insider_silence_1008):
    return _base_universe_d2(itm_056_insider_silence_1008, 41)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_041_itm_056_insider_silence_1008'] = {'inputs': ['itm_056_insider_silence_1008'], 'func': itm_base_universe_d2_041_itm_056_insider_silence_1008}


def itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260(itm_057_insider_buy_cluster_1260):
    return _base_universe_d2(itm_057_insider_buy_cluster_1260, 42)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260'] = {'inputs': ['itm_057_insider_buy_cluster_1260'], 'func': itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260}


def itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512(itm_058_insider_net_buy_ratio_1512):
    return _base_universe_d2(itm_058_insider_net_buy_ratio_1512, 43)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512'] = {'inputs': ['itm_058_insider_net_buy_ratio_1512'], 'func': itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512}


def itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252(itm_060_ceo_cfo_buy_weight_252):
    return _base_universe_d2(itm_060_ceo_cfo_buy_weight_252, 44)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252'] = {'inputs': ['itm_060_ceo_cfo_buy_weight_252'], 'func': itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252}


def itm_base_universe_d2_045_itm_062_insider_conviction_42(itm_062_insider_conviction_42):
    return _base_universe_d2(itm_062_insider_conviction_42, 45)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_045_itm_062_insider_conviction_42'] = {'inputs': ['itm_062_insider_conviction_42'], 'func': itm_base_universe_d2_045_itm_062_insider_conviction_42}


def itm_base_universe_d2_046_itm_064_insider_buy_cluster_84(itm_064_insider_buy_cluster_84):
    return _base_universe_d2(itm_064_insider_buy_cluster_84, 46)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_046_itm_064_insider_buy_cluster_84'] = {'inputs': ['itm_064_insider_buy_cluster_84'], 'func': itm_base_universe_d2_046_itm_064_insider_buy_cluster_84}


def itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126(itm_065_insider_net_buy_ratio_126):
    return _base_universe_d2(itm_065_insider_net_buy_ratio_126, 47)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126'] = {'inputs': ['itm_065_insider_net_buy_ratio_126'], 'func': itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126}


def itm_base_universe_d2_048_itm_066_insider_value_ratio_189(itm_066_insider_value_ratio_189):
    return _base_universe_d2(itm_066_insider_value_ratio_189, 48)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_048_itm_066_insider_value_ratio_189'] = {'inputs': ['itm_066_insider_value_ratio_189'], 'func': itm_base_universe_d2_048_itm_066_insider_value_ratio_189}


def itm_base_universe_d2_049_itm_069_insider_conviction_504(itm_069_insider_conviction_504):
    return _base_universe_d2(itm_069_insider_conviction_504, 49)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_049_itm_069_insider_conviction_504'] = {'inputs': ['itm_069_insider_conviction_504'], 'func': itm_base_universe_d2_049_itm_069_insider_conviction_504}


def itm_base_universe_d2_050_itm_070_insider_silence_756(itm_070_insider_silence_756):
    return _base_universe_d2(itm_070_insider_silence_756, 50)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_050_itm_070_insider_silence_756'] = {'inputs': ['itm_070_insider_silence_756'], 'func': itm_base_universe_d2_050_itm_070_insider_silence_756}


def itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008(itm_071_insider_buy_cluster_1008):
    return _base_universe_d2(itm_071_insider_buy_cluster_1008, 51)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008'] = {'inputs': ['itm_071_insider_buy_cluster_1008'], 'func': itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008}


def itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260(itm_072_insider_net_buy_ratio_1260):
    return _base_universe_d2(itm_072_insider_net_buy_ratio_1260, 52)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260'] = {'inputs': ['itm_072_insider_net_buy_ratio_1260'], 'func': itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260}


def itm_base_universe_d2_053_itm_073_insider_value_ratio_1512(itm_073_insider_value_ratio_1512):
    return _base_universe_d2(itm_073_insider_value_ratio_1512, 53)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_053_itm_073_insider_value_ratio_1512'] = {'inputs': ['itm_073_insider_value_ratio_1512'], 'func': itm_base_universe_d2_053_itm_073_insider_value_ratio_1512}


def itm_base_universe_d2_054_itm_basefill_005(itm_basefill_005):
    return _base_universe_d2(itm_basefill_005, 54)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_054_itm_basefill_005'] = {'inputs': ['itm_basefill_005'], 'func': itm_base_universe_d2_054_itm_basefill_005}


def itm_base_universe_d2_055_itm_basefill_012(itm_basefill_012):
    return _base_universe_d2(itm_basefill_012, 55)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_055_itm_basefill_012'] = {'inputs': ['itm_basefill_012'], 'func': itm_base_universe_d2_055_itm_basefill_012}


def itm_base_universe_d2_056_itm_basefill_019(itm_basefill_019):
    return _base_universe_d2(itm_basefill_019, 56)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_056_itm_basefill_019'] = {'inputs': ['itm_basefill_019'], 'func': itm_base_universe_d2_056_itm_basefill_019}


def itm_base_universe_d2_057_itm_basefill_022(itm_basefill_022):
    return _base_universe_d2(itm_basefill_022, 57)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_057_itm_basefill_022'] = {'inputs': ['itm_basefill_022'], 'func': itm_base_universe_d2_057_itm_basefill_022}


def itm_base_universe_d2_058_itm_basefill_026(itm_basefill_026):
    return _base_universe_d2(itm_basefill_026, 58)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_058_itm_basefill_026'] = {'inputs': ['itm_basefill_026'], 'func': itm_base_universe_d2_058_itm_basefill_026}


def itm_base_universe_d2_059_itm_basefill_033(itm_basefill_033):
    return _base_universe_d2(itm_basefill_033, 59)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_059_itm_basefill_033'] = {'inputs': ['itm_basefill_033'], 'func': itm_base_universe_d2_059_itm_basefill_033}


def itm_base_universe_d2_060_itm_basefill_037(itm_basefill_037):
    return _base_universe_d2(itm_basefill_037, 60)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_060_itm_basefill_037'] = {'inputs': ['itm_basefill_037'], 'func': itm_base_universe_d2_060_itm_basefill_037}


def itm_base_universe_d2_061_itm_basefill_040(itm_basefill_040):
    return _base_universe_d2(itm_basefill_040, 61)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_061_itm_basefill_040'] = {'inputs': ['itm_basefill_040'], 'func': itm_base_universe_d2_061_itm_basefill_040}


def itm_base_universe_d2_062_itm_basefill_047(itm_basefill_047):
    return _base_universe_d2(itm_basefill_047, 62)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_062_itm_basefill_047'] = {'inputs': ['itm_basefill_047'], 'func': itm_base_universe_d2_062_itm_basefill_047}


def itm_base_universe_d2_063_itm_basefill_052(itm_basefill_052):
    return _base_universe_d2(itm_basefill_052, 63)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_063_itm_basefill_052'] = {'inputs': ['itm_basefill_052'], 'func': itm_base_universe_d2_063_itm_basefill_052}


def itm_base_universe_d2_064_itm_basefill_054(itm_basefill_054):
    return _base_universe_d2(itm_basefill_054, 64)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_064_itm_basefill_054'] = {'inputs': ['itm_basefill_054'], 'func': itm_base_universe_d2_064_itm_basefill_054}


def itm_base_universe_d2_065_itm_basefill_059(itm_basefill_059):
    return _base_universe_d2(itm_basefill_059, 65)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_065_itm_basefill_059'] = {'inputs': ['itm_basefill_059'], 'func': itm_base_universe_d2_065_itm_basefill_059}


def itm_base_universe_d2_066_itm_basefill_061(itm_basefill_061):
    return _base_universe_d2(itm_basefill_061, 66)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_066_itm_basefill_061'] = {'inputs': ['itm_basefill_061'], 'func': itm_base_universe_d2_066_itm_basefill_061}


def itm_base_universe_d2_067_itm_basefill_063(itm_basefill_063):
    return _base_universe_d2(itm_basefill_063, 67)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_067_itm_basefill_063'] = {'inputs': ['itm_basefill_063'], 'func': itm_base_universe_d2_067_itm_basefill_063}


def itm_base_universe_d2_068_itm_basefill_067(itm_basefill_067):
    return _base_universe_d2(itm_basefill_067, 68)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_068_itm_basefill_067'] = {'inputs': ['itm_basefill_067'], 'func': itm_base_universe_d2_068_itm_basefill_067}


def itm_base_universe_d2_069_itm_basefill_068(itm_basefill_068):
    return _base_universe_d2(itm_basefill_068, 69)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_069_itm_basefill_068'] = {'inputs': ['itm_basefill_068'], 'func': itm_base_universe_d2_069_itm_basefill_068}


def itm_base_universe_d2_070_itm_basefill_074(itm_basefill_074):
    return _base_universe_d2(itm_basefill_074, 70)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_070_itm_basefill_074'] = {'inputs': ['itm_basefill_074'], 'func': itm_base_universe_d2_070_itm_basefill_074}


def itm_base_universe_d2_071_itm_basefill_075(itm_basefill_075):
    return _base_universe_d2(itm_basefill_075, 71)
ITM_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['itm_base_universe_d2_071_itm_basefill_075'] = {'inputs': ['itm_basefill_075'], 'func': itm_base_universe_d2_071_itm_basefill_075}
