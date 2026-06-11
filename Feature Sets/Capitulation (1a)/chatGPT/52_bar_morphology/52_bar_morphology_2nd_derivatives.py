import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def bmf_151_bmf_001_gap_down_frequency_5_001_roc_1(bmf_001_gap_down_frequency_5_001):
    feature = _s(bmf_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def bmf_152_bmf_007_gap_down_frequency_126_007_roc_5(bmf_007_gap_down_frequency_126_007):
    feature = _s(bmf_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42(bmf_013_gap_down_frequency_1008_013):
    feature = _s(bmf_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def bmf_154_bmf_019_gap_down_frequency_42_019_roc_126(bmf_019_gap_down_frequency_42_019):
    feature = _s(bmf_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def bmf_155_bmf_025_gap_down_frequency_378_025_roc_378(bmf_025_gap_down_frequency_378_025):
    feature = _s(bmf_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















BAR_MORPHOLOGY_REGISTRY_2ND_DERIVATIVES = {
    'bmf_151_bmf_001_gap_down_frequency_5_001_roc_1': {'inputs': ['bmf_001_gap_down_frequency_5_001'], 'func': bmf_151_bmf_001_gap_down_frequency_5_001_roc_1},
    'bmf_152_bmf_007_gap_down_frequency_126_007_roc_5': {'inputs': ['bmf_007_gap_down_frequency_126_007'], 'func': bmf_152_bmf_007_gap_down_frequency_126_007_roc_5},
    'bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['bmf_013_gap_down_frequency_1008_013'], 'func': bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42},
    'bmf_154_bmf_019_gap_down_frequency_42_019_roc_126': {'inputs': ['bmf_019_gap_down_frequency_42_019'], 'func': bmf_154_bmf_019_gap_down_frequency_42_019_roc_126},
    'bmf_155_bmf_025_gap_down_frequency_378_025_roc_378': {'inputs': ['bmf_025_gap_down_frequency_378_025'], 'func': bmf_155_bmf_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def bm_replacement_d2_001(bm_replacement_001):
    feature = _clean(bm_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_001'] = {'inputs': ['bm_replacement_001'], 'func': bm_replacement_d2_001}


def bm_replacement_d2_002(bm_replacement_002):
    feature = _clean(bm_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_002'] = {'inputs': ['bm_replacement_002'], 'func': bm_replacement_d2_002}


def bm_replacement_d2_003(bm_replacement_003):
    feature = _clean(bm_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_003'] = {'inputs': ['bm_replacement_003'], 'func': bm_replacement_d2_003}


def bm_replacement_d2_004(bm_replacement_004):
    feature = _clean(bm_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_004'] = {'inputs': ['bm_replacement_004'], 'func': bm_replacement_d2_004}


def bm_replacement_d2_005(bm_replacement_005):
    feature = _clean(bm_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_005'] = {'inputs': ['bm_replacement_005'], 'func': bm_replacement_d2_005}


def bm_replacement_d2_006(bm_replacement_006):
    feature = _clean(bm_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_006'] = {'inputs': ['bm_replacement_006'], 'func': bm_replacement_d2_006}


def bm_replacement_d2_007(bm_replacement_007):
    feature = _clean(bm_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_007'] = {'inputs': ['bm_replacement_007'], 'func': bm_replacement_d2_007}


def bm_replacement_d2_008(bm_replacement_008):
    feature = _clean(bm_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_008'] = {'inputs': ['bm_replacement_008'], 'func': bm_replacement_d2_008}


def bm_replacement_d2_009(bm_replacement_009):
    feature = _clean(bm_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_009'] = {'inputs': ['bm_replacement_009'], 'func': bm_replacement_d2_009}


def bm_replacement_d2_010(bm_replacement_010):
    feature = _clean(bm_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_010'] = {'inputs': ['bm_replacement_010'], 'func': bm_replacement_d2_010}


def bm_replacement_d2_011(bm_replacement_011):
    feature = _clean(bm_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_011'] = {'inputs': ['bm_replacement_011'], 'func': bm_replacement_d2_011}


def bm_replacement_d2_012(bm_replacement_012):
    feature = _clean(bm_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_012'] = {'inputs': ['bm_replacement_012'], 'func': bm_replacement_d2_012}


def bm_replacement_d2_013(bm_replacement_013):
    feature = _clean(bm_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_013'] = {'inputs': ['bm_replacement_013'], 'func': bm_replacement_d2_013}


def bm_replacement_d2_014(bm_replacement_014):
    feature = _clean(bm_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_014'] = {'inputs': ['bm_replacement_014'], 'func': bm_replacement_d2_014}


def bm_replacement_d2_015(bm_replacement_015):
    feature = _clean(bm_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_015'] = {'inputs': ['bm_replacement_015'], 'func': bm_replacement_d2_015}


def bm_replacement_d2_016(bm_replacement_016):
    feature = _clean(bm_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_016'] = {'inputs': ['bm_replacement_016'], 'func': bm_replacement_d2_016}


def bm_replacement_d2_017(bm_replacement_017):
    feature = _clean(bm_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_017'] = {'inputs': ['bm_replacement_017'], 'func': bm_replacement_d2_017}


def bm_replacement_d2_018(bm_replacement_018):
    feature = _clean(bm_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_018'] = {'inputs': ['bm_replacement_018'], 'func': bm_replacement_d2_018}


def bm_replacement_d2_019(bm_replacement_019):
    feature = _clean(bm_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_019'] = {'inputs': ['bm_replacement_019'], 'func': bm_replacement_d2_019}


def bm_replacement_d2_020(bm_replacement_020):
    feature = _clean(bm_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_020'] = {'inputs': ['bm_replacement_020'], 'func': bm_replacement_d2_020}


def bm_replacement_d2_021(bm_replacement_021):
    feature = _clean(bm_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_021'] = {'inputs': ['bm_replacement_021'], 'func': bm_replacement_d2_021}


def bm_replacement_d2_022(bm_replacement_022):
    feature = _clean(bm_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_022'] = {'inputs': ['bm_replacement_022'], 'func': bm_replacement_d2_022}


def bm_replacement_d2_023(bm_replacement_023):
    feature = _clean(bm_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_023'] = {'inputs': ['bm_replacement_023'], 'func': bm_replacement_d2_023}


def bm_replacement_d2_024(bm_replacement_024):
    feature = _clean(bm_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_024'] = {'inputs': ['bm_replacement_024'], 'func': bm_replacement_d2_024}


def bm_replacement_d2_025(bm_replacement_025):
    feature = _clean(bm_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_025'] = {'inputs': ['bm_replacement_025'], 'func': bm_replacement_d2_025}


def bm_replacement_d2_026(bm_replacement_026):
    feature = _clean(bm_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_026'] = {'inputs': ['bm_replacement_026'], 'func': bm_replacement_d2_026}


def bm_replacement_d2_027(bm_replacement_027):
    feature = _clean(bm_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_027'] = {'inputs': ['bm_replacement_027'], 'func': bm_replacement_d2_027}


def bm_replacement_d2_028(bm_replacement_028):
    feature = _clean(bm_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_028'] = {'inputs': ['bm_replacement_028'], 'func': bm_replacement_d2_028}


def bm_replacement_d2_029(bm_replacement_029):
    feature = _clean(bm_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_029'] = {'inputs': ['bm_replacement_029'], 'func': bm_replacement_d2_029}


def bm_replacement_d2_030(bm_replacement_030):
    feature = _clean(bm_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_030'] = {'inputs': ['bm_replacement_030'], 'func': bm_replacement_d2_030}


def bm_replacement_d2_031(bm_replacement_031):
    feature = _clean(bm_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_031'] = {'inputs': ['bm_replacement_031'], 'func': bm_replacement_d2_031}


def bm_replacement_d2_032(bm_replacement_032):
    feature = _clean(bm_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_032'] = {'inputs': ['bm_replacement_032'], 'func': bm_replacement_d2_032}


def bm_replacement_d2_033(bm_replacement_033):
    feature = _clean(bm_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_033'] = {'inputs': ['bm_replacement_033'], 'func': bm_replacement_d2_033}


def bm_replacement_d2_034(bm_replacement_034):
    feature = _clean(bm_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_034'] = {'inputs': ['bm_replacement_034'], 'func': bm_replacement_d2_034}


def bm_replacement_d2_035(bm_replacement_035):
    feature = _clean(bm_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_035'] = {'inputs': ['bm_replacement_035'], 'func': bm_replacement_d2_035}


def bm_replacement_d2_036(bm_replacement_036):
    feature = _clean(bm_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_036'] = {'inputs': ['bm_replacement_036'], 'func': bm_replacement_d2_036}


def bm_replacement_d2_037(bm_replacement_037):
    feature = _clean(bm_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_037'] = {'inputs': ['bm_replacement_037'], 'func': bm_replacement_d2_037}


def bm_replacement_d2_038(bm_replacement_038):
    feature = _clean(bm_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_038'] = {'inputs': ['bm_replacement_038'], 'func': bm_replacement_d2_038}


def bm_replacement_d2_039(bm_replacement_039):
    feature = _clean(bm_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_039'] = {'inputs': ['bm_replacement_039'], 'func': bm_replacement_d2_039}


def bm_replacement_d2_040(bm_replacement_040):
    feature = _clean(bm_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_040'] = {'inputs': ['bm_replacement_040'], 'func': bm_replacement_d2_040}


def bm_replacement_d2_041(bm_replacement_041):
    feature = _clean(bm_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_041'] = {'inputs': ['bm_replacement_041'], 'func': bm_replacement_d2_041}


def bm_replacement_d2_042(bm_replacement_042):
    feature = _clean(bm_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_042'] = {'inputs': ['bm_replacement_042'], 'func': bm_replacement_d2_042}


def bm_replacement_d2_043(bm_replacement_043):
    feature = _clean(bm_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_043'] = {'inputs': ['bm_replacement_043'], 'func': bm_replacement_d2_043}


def bm_replacement_d2_044(bm_replacement_044):
    feature = _clean(bm_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_044'] = {'inputs': ['bm_replacement_044'], 'func': bm_replacement_d2_044}


def bm_replacement_d2_045(bm_replacement_045):
    feature = _clean(bm_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_045'] = {'inputs': ['bm_replacement_045'], 'func': bm_replacement_d2_045}


def bm_replacement_d2_046(bm_replacement_046):
    feature = _clean(bm_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_046'] = {'inputs': ['bm_replacement_046'], 'func': bm_replacement_d2_046}


def bm_replacement_d2_047(bm_replacement_047):
    feature = _clean(bm_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_047'] = {'inputs': ['bm_replacement_047'], 'func': bm_replacement_d2_047}


def bm_replacement_d2_048(bm_replacement_048):
    feature = _clean(bm_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_048'] = {'inputs': ['bm_replacement_048'], 'func': bm_replacement_d2_048}


def bm_replacement_d2_049(bm_replacement_049):
    feature = _clean(bm_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_049'] = {'inputs': ['bm_replacement_049'], 'func': bm_replacement_d2_049}


def bm_replacement_d2_050(bm_replacement_050):
    feature = _clean(bm_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_050'] = {'inputs': ['bm_replacement_050'], 'func': bm_replacement_d2_050}


def bm_replacement_d2_051(bm_replacement_051):
    feature = _clean(bm_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_051'] = {'inputs': ['bm_replacement_051'], 'func': bm_replacement_d2_051}


def bm_replacement_d2_052(bm_replacement_052):
    feature = _clean(bm_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_052'] = {'inputs': ['bm_replacement_052'], 'func': bm_replacement_d2_052}


def bm_replacement_d2_053(bm_replacement_053):
    feature = _clean(bm_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_053'] = {'inputs': ['bm_replacement_053'], 'func': bm_replacement_d2_053}


def bm_replacement_d2_054(bm_replacement_054):
    feature = _clean(bm_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_054'] = {'inputs': ['bm_replacement_054'], 'func': bm_replacement_d2_054}


def bm_replacement_d2_055(bm_replacement_055):
    feature = _clean(bm_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_055'] = {'inputs': ['bm_replacement_055'], 'func': bm_replacement_d2_055}


def bm_replacement_d2_056(bm_replacement_056):
    feature = _clean(bm_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_056'] = {'inputs': ['bm_replacement_056'], 'func': bm_replacement_d2_056}


def bm_replacement_d2_057(bm_replacement_057):
    feature = _clean(bm_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_057'] = {'inputs': ['bm_replacement_057'], 'func': bm_replacement_d2_057}


def bm_replacement_d2_058(bm_replacement_058):
    feature = _clean(bm_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_058'] = {'inputs': ['bm_replacement_058'], 'func': bm_replacement_d2_058}


def bm_replacement_d2_059(bm_replacement_059):
    feature = _clean(bm_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_059'] = {'inputs': ['bm_replacement_059'], 'func': bm_replacement_d2_059}


def bm_replacement_d2_060(bm_replacement_060):
    feature = _clean(bm_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_060'] = {'inputs': ['bm_replacement_060'], 'func': bm_replacement_d2_060}


def bm_replacement_d2_061(bm_replacement_061):
    feature = _clean(bm_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_061'] = {'inputs': ['bm_replacement_061'], 'func': bm_replacement_d2_061}


def bm_replacement_d2_062(bm_replacement_062):
    feature = _clean(bm_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_062'] = {'inputs': ['bm_replacement_062'], 'func': bm_replacement_d2_062}


def bm_replacement_d2_063(bm_replacement_063):
    feature = _clean(bm_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_063'] = {'inputs': ['bm_replacement_063'], 'func': bm_replacement_d2_063}


def bm_replacement_d2_064(bm_replacement_064):
    feature = _clean(bm_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_064'] = {'inputs': ['bm_replacement_064'], 'func': bm_replacement_d2_064}


def bm_replacement_d2_065(bm_replacement_065):
    feature = _clean(bm_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_065'] = {'inputs': ['bm_replacement_065'], 'func': bm_replacement_d2_065}


def bm_replacement_d2_066(bm_replacement_066):
    feature = _clean(bm_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_066'] = {'inputs': ['bm_replacement_066'], 'func': bm_replacement_d2_066}


def bm_replacement_d2_067(bm_replacement_067):
    feature = _clean(bm_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_067'] = {'inputs': ['bm_replacement_067'], 'func': bm_replacement_d2_067}


def bm_replacement_d2_068(bm_replacement_068):
    feature = _clean(bm_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_068'] = {'inputs': ['bm_replacement_068'], 'func': bm_replacement_d2_068}


def bm_replacement_d2_069(bm_replacement_069):
    feature = _clean(bm_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_069'] = {'inputs': ['bm_replacement_069'], 'func': bm_replacement_d2_069}


def bm_replacement_d2_070(bm_replacement_070):
    feature = _clean(bm_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_070'] = {'inputs': ['bm_replacement_070'], 'func': bm_replacement_d2_070}


def bm_replacement_d2_071(bm_replacement_071):
    feature = _clean(bm_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_071'] = {'inputs': ['bm_replacement_071'], 'func': bm_replacement_d2_071}


def bm_replacement_d2_072(bm_replacement_072):
    feature = _clean(bm_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_072'] = {'inputs': ['bm_replacement_072'], 'func': bm_replacement_d2_072}


def bm_replacement_d2_073(bm_replacement_073):
    feature = _clean(bm_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_073'] = {'inputs': ['bm_replacement_073'], 'func': bm_replacement_d2_073}


def bm_replacement_d2_074(bm_replacement_074):
    feature = _clean(bm_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_074'] = {'inputs': ['bm_replacement_074'], 'func': bm_replacement_d2_074}


def bm_replacement_d2_075(bm_replacement_075):
    feature = _clean(bm_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_075'] = {'inputs': ['bm_replacement_075'], 'func': bm_replacement_d2_075}


def bm_replacement_d2_076(bm_replacement_076):
    feature = _clean(bm_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_076'] = {'inputs': ['bm_replacement_076'], 'func': bm_replacement_d2_076}


def bm_replacement_d2_077(bm_replacement_077):
    feature = _clean(bm_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_077'] = {'inputs': ['bm_replacement_077'], 'func': bm_replacement_d2_077}


def bm_replacement_d2_078(bm_replacement_078):
    feature = _clean(bm_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_078'] = {'inputs': ['bm_replacement_078'], 'func': bm_replacement_d2_078}


def bm_replacement_d2_079(bm_replacement_079):
    feature = _clean(bm_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_079'] = {'inputs': ['bm_replacement_079'], 'func': bm_replacement_d2_079}


def bm_replacement_d2_080(bm_replacement_080):
    feature = _clean(bm_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_080'] = {'inputs': ['bm_replacement_080'], 'func': bm_replacement_d2_080}


def bm_replacement_d2_081(bm_replacement_081):
    feature = _clean(bm_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_081'] = {'inputs': ['bm_replacement_081'], 'func': bm_replacement_d2_081}


def bm_replacement_d2_082(bm_replacement_082):
    feature = _clean(bm_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_082'] = {'inputs': ['bm_replacement_082'], 'func': bm_replacement_d2_082}


def bm_replacement_d2_083(bm_replacement_083):
    feature = _clean(bm_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_083'] = {'inputs': ['bm_replacement_083'], 'func': bm_replacement_d2_083}


def bm_replacement_d2_084(bm_replacement_084):
    feature = _clean(bm_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_084'] = {'inputs': ['bm_replacement_084'], 'func': bm_replacement_d2_084}


def bm_replacement_d2_085(bm_replacement_085):
    feature = _clean(bm_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_085'] = {'inputs': ['bm_replacement_085'], 'func': bm_replacement_d2_085}


def bm_replacement_d2_086(bm_replacement_086):
    feature = _clean(bm_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_086'] = {'inputs': ['bm_replacement_086'], 'func': bm_replacement_d2_086}


def bm_replacement_d2_087(bm_replacement_087):
    feature = _clean(bm_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_087'] = {'inputs': ['bm_replacement_087'], 'func': bm_replacement_d2_087}


def bm_replacement_d2_088(bm_replacement_088):
    feature = _clean(bm_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_088'] = {'inputs': ['bm_replacement_088'], 'func': bm_replacement_d2_088}


def bm_replacement_d2_089(bm_replacement_089):
    feature = _clean(bm_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_089'] = {'inputs': ['bm_replacement_089'], 'func': bm_replacement_d2_089}


def bm_replacement_d2_090(bm_replacement_090):
    feature = _clean(bm_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_090'] = {'inputs': ['bm_replacement_090'], 'func': bm_replacement_d2_090}


def bm_replacement_d2_091(bm_replacement_091):
    feature = _clean(bm_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_091'] = {'inputs': ['bm_replacement_091'], 'func': bm_replacement_d2_091}


def bm_replacement_d2_092(bm_replacement_092):
    feature = _clean(bm_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_092'] = {'inputs': ['bm_replacement_092'], 'func': bm_replacement_d2_092}


def bm_replacement_d2_093(bm_replacement_093):
    feature = _clean(bm_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_093'] = {'inputs': ['bm_replacement_093'], 'func': bm_replacement_d2_093}


def bm_replacement_d2_094(bm_replacement_094):
    feature = _clean(bm_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_094'] = {'inputs': ['bm_replacement_094'], 'func': bm_replacement_d2_094}


def bm_replacement_d2_095(bm_replacement_095):
    feature = _clean(bm_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_095'] = {'inputs': ['bm_replacement_095'], 'func': bm_replacement_d2_095}


def bm_replacement_d2_096(bm_replacement_096):
    feature = _clean(bm_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_096'] = {'inputs': ['bm_replacement_096'], 'func': bm_replacement_d2_096}


def bm_replacement_d2_097(bm_replacement_097):
    feature = _clean(bm_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_097'] = {'inputs': ['bm_replacement_097'], 'func': bm_replacement_d2_097}


def bm_replacement_d2_098(bm_replacement_098):
    feature = _clean(bm_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_098'] = {'inputs': ['bm_replacement_098'], 'func': bm_replacement_d2_098}


def bm_replacement_d2_099(bm_replacement_099):
    feature = _clean(bm_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_099'] = {'inputs': ['bm_replacement_099'], 'func': bm_replacement_d2_099}


def bm_replacement_d2_100(bm_replacement_100):
    feature = _clean(bm_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_100'] = {'inputs': ['bm_replacement_100'], 'func': bm_replacement_d2_100}


def bm_replacement_d2_101(bm_replacement_101):
    feature = _clean(bm_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_101'] = {'inputs': ['bm_replacement_101'], 'func': bm_replacement_d2_101}


def bm_replacement_d2_102(bm_replacement_102):
    feature = _clean(bm_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_102'] = {'inputs': ['bm_replacement_102'], 'func': bm_replacement_d2_102}


def bm_replacement_d2_103(bm_replacement_103):
    feature = _clean(bm_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_103'] = {'inputs': ['bm_replacement_103'], 'func': bm_replacement_d2_103}


def bm_replacement_d2_104(bm_replacement_104):
    feature = _clean(bm_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_104'] = {'inputs': ['bm_replacement_104'], 'func': bm_replacement_d2_104}


def bm_replacement_d2_105(bm_replacement_105):
    feature = _clean(bm_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_105'] = {'inputs': ['bm_replacement_105'], 'func': bm_replacement_d2_105}


def bm_replacement_d2_106(bm_replacement_106):
    feature = _clean(bm_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_106'] = {'inputs': ['bm_replacement_106'], 'func': bm_replacement_d2_106}


def bm_replacement_d2_107(bm_replacement_107):
    feature = _clean(bm_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_107'] = {'inputs': ['bm_replacement_107'], 'func': bm_replacement_d2_107}


def bm_replacement_d2_108(bm_replacement_108):
    feature = _clean(bm_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_108'] = {'inputs': ['bm_replacement_108'], 'func': bm_replacement_d2_108}


def bm_replacement_d2_109(bm_replacement_109):
    feature = _clean(bm_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_109'] = {'inputs': ['bm_replacement_109'], 'func': bm_replacement_d2_109}


def bm_replacement_d2_110(bm_replacement_110):
    feature = _clean(bm_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_110'] = {'inputs': ['bm_replacement_110'], 'func': bm_replacement_d2_110}


def bm_replacement_d2_111(bm_replacement_111):
    feature = _clean(bm_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_111'] = {'inputs': ['bm_replacement_111'], 'func': bm_replacement_d2_111}


def bm_replacement_d2_112(bm_replacement_112):
    feature = _clean(bm_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_112'] = {'inputs': ['bm_replacement_112'], 'func': bm_replacement_d2_112}


def bm_replacement_d2_113(bm_replacement_113):
    feature = _clean(bm_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_113'] = {'inputs': ['bm_replacement_113'], 'func': bm_replacement_d2_113}


def bm_replacement_d2_114(bm_replacement_114):
    feature = _clean(bm_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_114'] = {'inputs': ['bm_replacement_114'], 'func': bm_replacement_d2_114}


def bm_replacement_d2_115(bm_replacement_115):
    feature = _clean(bm_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_115'] = {'inputs': ['bm_replacement_115'], 'func': bm_replacement_d2_115}


def bm_replacement_d2_116(bm_replacement_116):
    feature = _clean(bm_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_116'] = {'inputs': ['bm_replacement_116'], 'func': bm_replacement_d2_116}


def bm_replacement_d2_117(bm_replacement_117):
    feature = _clean(bm_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_117'] = {'inputs': ['bm_replacement_117'], 'func': bm_replacement_d2_117}


def bm_replacement_d2_118(bm_replacement_118):
    feature = _clean(bm_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_118'] = {'inputs': ['bm_replacement_118'], 'func': bm_replacement_d2_118}


def bm_replacement_d2_119(bm_replacement_119):
    feature = _clean(bm_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_119'] = {'inputs': ['bm_replacement_119'], 'func': bm_replacement_d2_119}


def bm_replacement_d2_120(bm_replacement_120):
    feature = _clean(bm_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_120'] = {'inputs': ['bm_replacement_120'], 'func': bm_replacement_d2_120}


def bm_replacement_d2_121(bm_replacement_121):
    feature = _clean(bm_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_121'] = {'inputs': ['bm_replacement_121'], 'func': bm_replacement_d2_121}


def bm_replacement_d2_122(bm_replacement_122):
    feature = _clean(bm_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_122'] = {'inputs': ['bm_replacement_122'], 'func': bm_replacement_d2_122}


def bm_replacement_d2_123(bm_replacement_123):
    feature = _clean(bm_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_123'] = {'inputs': ['bm_replacement_123'], 'func': bm_replacement_d2_123}


def bm_replacement_d2_124(bm_replacement_124):
    feature = _clean(bm_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_124'] = {'inputs': ['bm_replacement_124'], 'func': bm_replacement_d2_124}


def bm_replacement_d2_125(bm_replacement_125):
    feature = _clean(bm_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_125'] = {'inputs': ['bm_replacement_125'], 'func': bm_replacement_d2_125}


def bm_replacement_d2_126(bm_replacement_126):
    feature = _clean(bm_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_126'] = {'inputs': ['bm_replacement_126'], 'func': bm_replacement_d2_126}


def bm_replacement_d2_127(bm_replacement_127):
    feature = _clean(bm_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_127'] = {'inputs': ['bm_replacement_127'], 'func': bm_replacement_d2_127}


def bm_replacement_d2_128(bm_replacement_128):
    feature = _clean(bm_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_128'] = {'inputs': ['bm_replacement_128'], 'func': bm_replacement_d2_128}


def bm_replacement_d2_129(bm_replacement_129):
    feature = _clean(bm_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_129'] = {'inputs': ['bm_replacement_129'], 'func': bm_replacement_d2_129}


def bm_replacement_d2_130(bm_replacement_130):
    feature = _clean(bm_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_130'] = {'inputs': ['bm_replacement_130'], 'func': bm_replacement_d2_130}


def bm_replacement_d2_131(bm_replacement_131):
    feature = _clean(bm_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_131'] = {'inputs': ['bm_replacement_131'], 'func': bm_replacement_d2_131}


def bm_replacement_d2_132(bm_replacement_132):
    feature = _clean(bm_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_132'] = {'inputs': ['bm_replacement_132'], 'func': bm_replacement_d2_132}


def bm_replacement_d2_133(bm_replacement_133):
    feature = _clean(bm_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_133'] = {'inputs': ['bm_replacement_133'], 'func': bm_replacement_d2_133}


def bm_replacement_d2_134(bm_replacement_134):
    feature = _clean(bm_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_134'] = {'inputs': ['bm_replacement_134'], 'func': bm_replacement_d2_134}


def bm_replacement_d2_135(bm_replacement_135):
    feature = _clean(bm_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_135'] = {'inputs': ['bm_replacement_135'], 'func': bm_replacement_d2_135}


def bm_replacement_d2_136(bm_replacement_136):
    feature = _clean(bm_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_136'] = {'inputs': ['bm_replacement_136'], 'func': bm_replacement_d2_136}


def bm_replacement_d2_137(bm_replacement_137):
    feature = _clean(bm_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_137'] = {'inputs': ['bm_replacement_137'], 'func': bm_replacement_d2_137}


def bm_replacement_d2_138(bm_replacement_138):
    feature = _clean(bm_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_138'] = {'inputs': ['bm_replacement_138'], 'func': bm_replacement_d2_138}


def bm_replacement_d2_139(bm_replacement_139):
    feature = _clean(bm_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_139'] = {'inputs': ['bm_replacement_139'], 'func': bm_replacement_d2_139}


def bm_replacement_d2_140(bm_replacement_140):
    feature = _clean(bm_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_140'] = {'inputs': ['bm_replacement_140'], 'func': bm_replacement_d2_140}


def bm_replacement_d2_141(bm_replacement_141):
    feature = _clean(bm_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_141'] = {'inputs': ['bm_replacement_141'], 'func': bm_replacement_d2_141}


def bm_replacement_d2_142(bm_replacement_142):
    feature = _clean(bm_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_142'] = {'inputs': ['bm_replacement_142'], 'func': bm_replacement_d2_142}


def bm_replacement_d2_143(bm_replacement_143):
    feature = _clean(bm_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_143'] = {'inputs': ['bm_replacement_143'], 'func': bm_replacement_d2_143}


def bm_replacement_d2_144(bm_replacement_144):
    feature = _clean(bm_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_144'] = {'inputs': ['bm_replacement_144'], 'func': bm_replacement_d2_144}


def bm_replacement_d2_145(bm_replacement_145):
    feature = _clean(bm_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_145'] = {'inputs': ['bm_replacement_145'], 'func': bm_replacement_d2_145}


def bm_replacement_d2_146(bm_replacement_146):
    feature = _clean(bm_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_146'] = {'inputs': ['bm_replacement_146'], 'func': bm_replacement_d2_146}


def bm_replacement_d2_147(bm_replacement_147):
    feature = _clean(bm_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_147'] = {'inputs': ['bm_replacement_147'], 'func': bm_replacement_d2_147}


def bm_replacement_d2_148(bm_replacement_148):
    feature = _clean(bm_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_148'] = {'inputs': ['bm_replacement_148'], 'func': bm_replacement_d2_148}


def bm_replacement_d2_149(bm_replacement_149):
    feature = _clean(bm_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_149'] = {'inputs': ['bm_replacement_149'], 'func': bm_replacement_d2_149}


def bm_replacement_d2_150(bm_replacement_150):
    feature = _clean(bm_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_150'] = {'inputs': ['bm_replacement_150'], 'func': bm_replacement_d2_150}


def bm_replacement_d2_151(bm_replacement_151):
    feature = _clean(bm_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_151'] = {'inputs': ['bm_replacement_151'], 'func': bm_replacement_d2_151}


def bm_replacement_d2_152(bm_replacement_152):
    feature = _clean(bm_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_152'] = {'inputs': ['bm_replacement_152'], 'func': bm_replacement_d2_152}


def bm_replacement_d2_153(bm_replacement_153):
    feature = _clean(bm_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_153'] = {'inputs': ['bm_replacement_153'], 'func': bm_replacement_d2_153}


def bm_replacement_d2_154(bm_replacement_154):
    feature = _clean(bm_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_154'] = {'inputs': ['bm_replacement_154'], 'func': bm_replacement_d2_154}


def bm_replacement_d2_155(bm_replacement_155):
    feature = _clean(bm_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_155'] = {'inputs': ['bm_replacement_155'], 'func': bm_replacement_d2_155}


def bm_replacement_d2_156(bm_replacement_156):
    feature = _clean(bm_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_156'] = {'inputs': ['bm_replacement_156'], 'func': bm_replacement_d2_156}


def bm_replacement_d2_157(bm_replacement_157):
    feature = _clean(bm_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_157'] = {'inputs': ['bm_replacement_157'], 'func': bm_replacement_d2_157}


def bm_replacement_d2_158(bm_replacement_158):
    feature = _clean(bm_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_158'] = {'inputs': ['bm_replacement_158'], 'func': bm_replacement_d2_158}


def bm_replacement_d2_159(bm_replacement_159):
    feature = _clean(bm_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_159'] = {'inputs': ['bm_replacement_159'], 'func': bm_replacement_d2_159}


def bm_replacement_d2_160(bm_replacement_160):
    feature = _clean(bm_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
BM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bm_replacement_d2_160'] = {'inputs': ['bm_replacement_160'], 'func': bm_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002(bmf_002_gap_magnitude_10_002):
    return _base_universe_d2(bmf_002_gap_magnitude_10_002, 1)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002'] = {'inputs': ['bmf_002_gap_magnitude_10_002'], 'func': bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002}


def bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003(bmf_003_open_close_pressure_21_003):
    return _base_universe_d2(bmf_003_open_close_pressure_21_003, 2)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003'] = {'inputs': ['bmf_003_open_close_pressure_21_003'], 'func': bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003}


def bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004(bmf_004_lower_wick_ratio_42_004):
    return _base_universe_d2(bmf_004_lower_wick_ratio_42_004, 3)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004'] = {'inputs': ['bmf_004_lower_wick_ratio_42_004'], 'func': bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004}


def bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005(bmf_005_upper_wick_ratio_63_005):
    return _base_universe_d2(bmf_005_upper_wick_ratio_63_005, 4)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005'] = {'inputs': ['bmf_005_upper_wick_ratio_63_005'], 'func': bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005}


def bmf_base_universe_d2_005_bmf_006_body_to_range_84_006(bmf_006_body_to_range_84_006):
    return _base_universe_d2(bmf_006_body_to_range_84_006, 5)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_005_bmf_006_body_to_range_84_006'] = {'inputs': ['bmf_006_body_to_range_84_006'], 'func': bmf_base_universe_d2_005_bmf_006_body_to_range_84_006}


def bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008(bmf_008_gap_magnitude_189_008):
    return _base_universe_d2(bmf_008_gap_magnitude_189_008, 6)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008'] = {'inputs': ['bmf_008_gap_magnitude_189_008'], 'func': bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008}


def bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009(bmf_009_open_close_pressure_252_009):
    return _base_universe_d2(bmf_009_open_close_pressure_252_009, 7)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009'] = {'inputs': ['bmf_009_open_close_pressure_252_009'], 'func': bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009}


def bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010(bmf_010_lower_wick_ratio_378_010):
    return _base_universe_d2(bmf_010_lower_wick_ratio_378_010, 8)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010'] = {'inputs': ['bmf_010_lower_wick_ratio_378_010'], 'func': bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010}


def bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011(bmf_011_upper_wick_ratio_504_011):
    return _base_universe_d2(bmf_011_upper_wick_ratio_504_011, 9)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011'] = {'inputs': ['bmf_011_upper_wick_ratio_504_011'], 'func': bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011}


def bmf_base_universe_d2_010_bmf_012_body_to_range_756_012(bmf_012_body_to_range_756_012):
    return _base_universe_d2(bmf_012_body_to_range_756_012, 10)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_010_bmf_012_body_to_range_756_012'] = {'inputs': ['bmf_012_body_to_range_756_012'], 'func': bmf_base_universe_d2_010_bmf_012_body_to_range_756_012}


def bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014(bmf_014_gap_magnitude_1260_014):
    return _base_universe_d2(bmf_014_gap_magnitude_1260_014, 11)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014'] = {'inputs': ['bmf_014_gap_magnitude_1260_014'], 'func': bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014}


def bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015(bmf_015_open_close_pressure_1512_015):
    return _base_universe_d2(bmf_015_open_close_pressure_1512_015, 12)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015'] = {'inputs': ['bmf_015_open_close_pressure_1512_015'], 'func': bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015}


def bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016(bmf_016_lower_wick_ratio_5_016):
    return _base_universe_d2(bmf_016_lower_wick_ratio_5_016, 13)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016'] = {'inputs': ['bmf_016_lower_wick_ratio_5_016'], 'func': bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016}


def bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017(bmf_017_upper_wick_ratio_10_017):
    return _base_universe_d2(bmf_017_upper_wick_ratio_10_017, 14)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017'] = {'inputs': ['bmf_017_upper_wick_ratio_10_017'], 'func': bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017}


def bmf_base_universe_d2_015_bmf_018_body_to_range_21_018(bmf_018_body_to_range_21_018):
    return _base_universe_d2(bmf_018_body_to_range_21_018, 15)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_015_bmf_018_body_to_range_21_018'] = {'inputs': ['bmf_018_body_to_range_21_018'], 'func': bmf_base_universe_d2_015_bmf_018_body_to_range_21_018}


def bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020(bmf_020_gap_magnitude_63_020):
    return _base_universe_d2(bmf_020_gap_magnitude_63_020, 16)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020'] = {'inputs': ['bmf_020_gap_magnitude_63_020'], 'func': bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020}


def bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021(bmf_021_open_close_pressure_84_021):
    return _base_universe_d2(bmf_021_open_close_pressure_84_021, 17)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021'] = {'inputs': ['bmf_021_open_close_pressure_84_021'], 'func': bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021}


def bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022(bmf_022_lower_wick_ratio_126_022):
    return _base_universe_d2(bmf_022_lower_wick_ratio_126_022, 18)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022'] = {'inputs': ['bmf_022_lower_wick_ratio_126_022'], 'func': bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022}


def bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023(bmf_023_upper_wick_ratio_189_023):
    return _base_universe_d2(bmf_023_upper_wick_ratio_189_023, 19)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023'] = {'inputs': ['bmf_023_upper_wick_ratio_189_023'], 'func': bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023}


def bmf_base_universe_d2_020_bmf_024_body_to_range_252_024(bmf_024_body_to_range_252_024):
    return _base_universe_d2(bmf_024_body_to_range_252_024, 20)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_020_bmf_024_body_to_range_252_024'] = {'inputs': ['bmf_024_body_to_range_252_024'], 'func': bmf_base_universe_d2_020_bmf_024_body_to_range_252_024}


def bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026(bmf_026_gap_magnitude_504_026):
    return _base_universe_d2(bmf_026_gap_magnitude_504_026, 21)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026'] = {'inputs': ['bmf_026_gap_magnitude_504_026'], 'func': bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026}


def bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027(bmf_027_open_close_pressure_756_027):
    return _base_universe_d2(bmf_027_open_close_pressure_756_027, 22)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027'] = {'inputs': ['bmf_027_open_close_pressure_756_027'], 'func': bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027}


def bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028(bmf_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(bmf_028_lower_wick_ratio_1008_028, 23)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028'] = {'inputs': ['bmf_028_lower_wick_ratio_1008_028'], 'func': bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028}


def bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029(bmf_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(bmf_029_upper_wick_ratio_1260_029, 24)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029'] = {'inputs': ['bmf_029_upper_wick_ratio_1260_029'], 'func': bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029}


def bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030(bmf_030_body_to_range_1512_030):
    return _base_universe_d2(bmf_030_body_to_range_1512_030, 25)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030'] = {'inputs': ['bmf_030_body_to_range_1512_030'], 'func': bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030}


def bmf_base_universe_d2_026_bmf_basefill_031(bmf_basefill_031):
    return _base_universe_d2(bmf_basefill_031, 26)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_026_bmf_basefill_031'] = {'inputs': ['bmf_basefill_031'], 'func': bmf_base_universe_d2_026_bmf_basefill_031}


def bmf_base_universe_d2_027_bmf_basefill_032(bmf_basefill_032):
    return _base_universe_d2(bmf_basefill_032, 27)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_027_bmf_basefill_032'] = {'inputs': ['bmf_basefill_032'], 'func': bmf_base_universe_d2_027_bmf_basefill_032}


def bmf_base_universe_d2_028_bmf_basefill_033(bmf_basefill_033):
    return _base_universe_d2(bmf_basefill_033, 28)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_028_bmf_basefill_033'] = {'inputs': ['bmf_basefill_033'], 'func': bmf_base_universe_d2_028_bmf_basefill_033}


def bmf_base_universe_d2_029_bmf_basefill_034(bmf_basefill_034):
    return _base_universe_d2(bmf_basefill_034, 29)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_029_bmf_basefill_034'] = {'inputs': ['bmf_basefill_034'], 'func': bmf_base_universe_d2_029_bmf_basefill_034}


def bmf_base_universe_d2_030_bmf_basefill_035(bmf_basefill_035):
    return _base_universe_d2(bmf_basefill_035, 30)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_030_bmf_basefill_035'] = {'inputs': ['bmf_basefill_035'], 'func': bmf_base_universe_d2_030_bmf_basefill_035}


def bmf_base_universe_d2_031_bmf_basefill_036(bmf_basefill_036):
    return _base_universe_d2(bmf_basefill_036, 31)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_031_bmf_basefill_036'] = {'inputs': ['bmf_basefill_036'], 'func': bmf_base_universe_d2_031_bmf_basefill_036}


def bmf_base_universe_d2_032_bmf_basefill_037(bmf_basefill_037):
    return _base_universe_d2(bmf_basefill_037, 32)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_032_bmf_basefill_037'] = {'inputs': ['bmf_basefill_037'], 'func': bmf_base_universe_d2_032_bmf_basefill_037}


def bmf_base_universe_d2_033_bmf_basefill_038(bmf_basefill_038):
    return _base_universe_d2(bmf_basefill_038, 33)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_033_bmf_basefill_038'] = {'inputs': ['bmf_basefill_038'], 'func': bmf_base_universe_d2_033_bmf_basefill_038}


def bmf_base_universe_d2_034_bmf_basefill_039(bmf_basefill_039):
    return _base_universe_d2(bmf_basefill_039, 34)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_034_bmf_basefill_039'] = {'inputs': ['bmf_basefill_039'], 'func': bmf_base_universe_d2_034_bmf_basefill_039}


def bmf_base_universe_d2_035_bmf_basefill_040(bmf_basefill_040):
    return _base_universe_d2(bmf_basefill_040, 35)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_035_bmf_basefill_040'] = {'inputs': ['bmf_basefill_040'], 'func': bmf_base_universe_d2_035_bmf_basefill_040}


def bmf_base_universe_d2_036_bmf_basefill_041(bmf_basefill_041):
    return _base_universe_d2(bmf_basefill_041, 36)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_036_bmf_basefill_041'] = {'inputs': ['bmf_basefill_041'], 'func': bmf_base_universe_d2_036_bmf_basefill_041}


def bmf_base_universe_d2_037_bmf_basefill_042(bmf_basefill_042):
    return _base_universe_d2(bmf_basefill_042, 37)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_037_bmf_basefill_042'] = {'inputs': ['bmf_basefill_042'], 'func': bmf_base_universe_d2_037_bmf_basefill_042}


def bmf_base_universe_d2_038_bmf_basefill_043(bmf_basefill_043):
    return _base_universe_d2(bmf_basefill_043, 38)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_038_bmf_basefill_043'] = {'inputs': ['bmf_basefill_043'], 'func': bmf_base_universe_d2_038_bmf_basefill_043}


def bmf_base_universe_d2_039_bmf_basefill_044(bmf_basefill_044):
    return _base_universe_d2(bmf_basefill_044, 39)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_039_bmf_basefill_044'] = {'inputs': ['bmf_basefill_044'], 'func': bmf_base_universe_d2_039_bmf_basefill_044}


def bmf_base_universe_d2_040_bmf_basefill_045(bmf_basefill_045):
    return _base_universe_d2(bmf_basefill_045, 40)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_040_bmf_basefill_045'] = {'inputs': ['bmf_basefill_045'], 'func': bmf_base_universe_d2_040_bmf_basefill_045}


def bmf_base_universe_d2_041_bmf_basefill_046(bmf_basefill_046):
    return _base_universe_d2(bmf_basefill_046, 41)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_041_bmf_basefill_046'] = {'inputs': ['bmf_basefill_046'], 'func': bmf_base_universe_d2_041_bmf_basefill_046}


def bmf_base_universe_d2_042_bmf_basefill_047(bmf_basefill_047):
    return _base_universe_d2(bmf_basefill_047, 42)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_042_bmf_basefill_047'] = {'inputs': ['bmf_basefill_047'], 'func': bmf_base_universe_d2_042_bmf_basefill_047}


def bmf_base_universe_d2_043_bmf_basefill_048(bmf_basefill_048):
    return _base_universe_d2(bmf_basefill_048, 43)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_043_bmf_basefill_048'] = {'inputs': ['bmf_basefill_048'], 'func': bmf_base_universe_d2_043_bmf_basefill_048}


def bmf_base_universe_d2_044_bmf_basefill_049(bmf_basefill_049):
    return _base_universe_d2(bmf_basefill_049, 44)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_044_bmf_basefill_049'] = {'inputs': ['bmf_basefill_049'], 'func': bmf_base_universe_d2_044_bmf_basefill_049}


def bmf_base_universe_d2_045_bmf_basefill_050(bmf_basefill_050):
    return _base_universe_d2(bmf_basefill_050, 45)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_045_bmf_basefill_050'] = {'inputs': ['bmf_basefill_050'], 'func': bmf_base_universe_d2_045_bmf_basefill_050}


def bmf_base_universe_d2_046_bmf_basefill_051(bmf_basefill_051):
    return _base_universe_d2(bmf_basefill_051, 46)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_046_bmf_basefill_051'] = {'inputs': ['bmf_basefill_051'], 'func': bmf_base_universe_d2_046_bmf_basefill_051}


def bmf_base_universe_d2_047_bmf_basefill_052(bmf_basefill_052):
    return _base_universe_d2(bmf_basefill_052, 47)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_047_bmf_basefill_052'] = {'inputs': ['bmf_basefill_052'], 'func': bmf_base_universe_d2_047_bmf_basefill_052}


def bmf_base_universe_d2_048_bmf_basefill_053(bmf_basefill_053):
    return _base_universe_d2(bmf_basefill_053, 48)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_048_bmf_basefill_053'] = {'inputs': ['bmf_basefill_053'], 'func': bmf_base_universe_d2_048_bmf_basefill_053}


def bmf_base_universe_d2_049_bmf_basefill_054(bmf_basefill_054):
    return _base_universe_d2(bmf_basefill_054, 49)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_049_bmf_basefill_054'] = {'inputs': ['bmf_basefill_054'], 'func': bmf_base_universe_d2_049_bmf_basefill_054}


def bmf_base_universe_d2_050_bmf_basefill_055(bmf_basefill_055):
    return _base_universe_d2(bmf_basefill_055, 50)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_050_bmf_basefill_055'] = {'inputs': ['bmf_basefill_055'], 'func': bmf_base_universe_d2_050_bmf_basefill_055}


def bmf_base_universe_d2_051_bmf_basefill_056(bmf_basefill_056):
    return _base_universe_d2(bmf_basefill_056, 51)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_051_bmf_basefill_056'] = {'inputs': ['bmf_basefill_056'], 'func': bmf_base_universe_d2_051_bmf_basefill_056}


def bmf_base_universe_d2_052_bmf_basefill_057(bmf_basefill_057):
    return _base_universe_d2(bmf_basefill_057, 52)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_052_bmf_basefill_057'] = {'inputs': ['bmf_basefill_057'], 'func': bmf_base_universe_d2_052_bmf_basefill_057}


def bmf_base_universe_d2_053_bmf_basefill_058(bmf_basefill_058):
    return _base_universe_d2(bmf_basefill_058, 53)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_053_bmf_basefill_058'] = {'inputs': ['bmf_basefill_058'], 'func': bmf_base_universe_d2_053_bmf_basefill_058}


def bmf_base_universe_d2_054_bmf_basefill_059(bmf_basefill_059):
    return _base_universe_d2(bmf_basefill_059, 54)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_054_bmf_basefill_059'] = {'inputs': ['bmf_basefill_059'], 'func': bmf_base_universe_d2_054_bmf_basefill_059}


def bmf_base_universe_d2_055_bmf_basefill_060(bmf_basefill_060):
    return _base_universe_d2(bmf_basefill_060, 55)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_055_bmf_basefill_060'] = {'inputs': ['bmf_basefill_060'], 'func': bmf_base_universe_d2_055_bmf_basefill_060}


def bmf_base_universe_d2_056_bmf_basefill_061(bmf_basefill_061):
    return _base_universe_d2(bmf_basefill_061, 56)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_056_bmf_basefill_061'] = {'inputs': ['bmf_basefill_061'], 'func': bmf_base_universe_d2_056_bmf_basefill_061}


def bmf_base_universe_d2_057_bmf_basefill_062(bmf_basefill_062):
    return _base_universe_d2(bmf_basefill_062, 57)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_057_bmf_basefill_062'] = {'inputs': ['bmf_basefill_062'], 'func': bmf_base_universe_d2_057_bmf_basefill_062}


def bmf_base_universe_d2_058_bmf_basefill_063(bmf_basefill_063):
    return _base_universe_d2(bmf_basefill_063, 58)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_058_bmf_basefill_063'] = {'inputs': ['bmf_basefill_063'], 'func': bmf_base_universe_d2_058_bmf_basefill_063}


def bmf_base_universe_d2_059_bmf_basefill_064(bmf_basefill_064):
    return _base_universe_d2(bmf_basefill_064, 59)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_059_bmf_basefill_064'] = {'inputs': ['bmf_basefill_064'], 'func': bmf_base_universe_d2_059_bmf_basefill_064}


def bmf_base_universe_d2_060_bmf_basefill_065(bmf_basefill_065):
    return _base_universe_d2(bmf_basefill_065, 60)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_060_bmf_basefill_065'] = {'inputs': ['bmf_basefill_065'], 'func': bmf_base_universe_d2_060_bmf_basefill_065}


def bmf_base_universe_d2_061_bmf_basefill_066(bmf_basefill_066):
    return _base_universe_d2(bmf_basefill_066, 61)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_061_bmf_basefill_066'] = {'inputs': ['bmf_basefill_066'], 'func': bmf_base_universe_d2_061_bmf_basefill_066}


def bmf_base_universe_d2_062_bmf_basefill_067(bmf_basefill_067):
    return _base_universe_d2(bmf_basefill_067, 62)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_062_bmf_basefill_067'] = {'inputs': ['bmf_basefill_067'], 'func': bmf_base_universe_d2_062_bmf_basefill_067}


def bmf_base_universe_d2_063_bmf_basefill_068(bmf_basefill_068):
    return _base_universe_d2(bmf_basefill_068, 63)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_063_bmf_basefill_068'] = {'inputs': ['bmf_basefill_068'], 'func': bmf_base_universe_d2_063_bmf_basefill_068}


def bmf_base_universe_d2_064_bmf_basefill_069(bmf_basefill_069):
    return _base_universe_d2(bmf_basefill_069, 64)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_064_bmf_basefill_069'] = {'inputs': ['bmf_basefill_069'], 'func': bmf_base_universe_d2_064_bmf_basefill_069}


def bmf_base_universe_d2_065_bmf_basefill_070(bmf_basefill_070):
    return _base_universe_d2(bmf_basefill_070, 65)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_065_bmf_basefill_070'] = {'inputs': ['bmf_basefill_070'], 'func': bmf_base_universe_d2_065_bmf_basefill_070}


def bmf_base_universe_d2_066_bmf_basefill_071(bmf_basefill_071):
    return _base_universe_d2(bmf_basefill_071, 66)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_066_bmf_basefill_071'] = {'inputs': ['bmf_basefill_071'], 'func': bmf_base_universe_d2_066_bmf_basefill_071}


def bmf_base_universe_d2_067_bmf_basefill_072(bmf_basefill_072):
    return _base_universe_d2(bmf_basefill_072, 67)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_067_bmf_basefill_072'] = {'inputs': ['bmf_basefill_072'], 'func': bmf_base_universe_d2_067_bmf_basefill_072}


def bmf_base_universe_d2_068_bmf_basefill_073(bmf_basefill_073):
    return _base_universe_d2(bmf_basefill_073, 68)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_068_bmf_basefill_073'] = {'inputs': ['bmf_basefill_073'], 'func': bmf_base_universe_d2_068_bmf_basefill_073}


def bmf_base_universe_d2_069_bmf_basefill_074(bmf_basefill_074):
    return _base_universe_d2(bmf_basefill_074, 69)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_069_bmf_basefill_074'] = {'inputs': ['bmf_basefill_074'], 'func': bmf_base_universe_d2_069_bmf_basefill_074}


def bmf_base_universe_d2_070_bmf_basefill_075(bmf_basefill_075):
    return _base_universe_d2(bmf_basefill_075, 70)
BMF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bmf_base_universe_d2_070_bmf_basefill_075'] = {'inputs': ['bmf_basefill_075'], 'func': bmf_base_universe_d2_070_bmf_basefill_075}
