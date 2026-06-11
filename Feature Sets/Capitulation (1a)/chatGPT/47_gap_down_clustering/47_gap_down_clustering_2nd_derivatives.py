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



def gdc_151_gdc_001_gap_down_frequency_5_001_roc_1(gdc_001_gap_down_frequency_5_001):
    feature = _s(gdc_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def gdc_152_gdc_007_gap_down_frequency_126_007_roc_5(gdc_007_gap_down_frequency_126_007):
    feature = _s(gdc_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42(gdc_013_gap_down_frequency_1008_013):
    feature = _s(gdc_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def gdc_154_gdc_019_gap_down_frequency_42_019_roc_126(gdc_019_gap_down_frequency_42_019):
    feature = _s(gdc_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def gdc_155_gdc_025_gap_down_frequency_378_025_roc_378(gdc_025_gap_down_frequency_378_025):
    feature = _s(gdc_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















GAP_DOWN_CLUSTERING_REGISTRY_2ND_DERIVATIVES = {
    'gdc_151_gdc_001_gap_down_frequency_5_001_roc_1': {'inputs': ['gdc_001_gap_down_frequency_5_001'], 'func': gdc_151_gdc_001_gap_down_frequency_5_001_roc_1},
    'gdc_152_gdc_007_gap_down_frequency_126_007_roc_5': {'inputs': ['gdc_007_gap_down_frequency_126_007'], 'func': gdc_152_gdc_007_gap_down_frequency_126_007_roc_5},
    'gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['gdc_013_gap_down_frequency_1008_013'], 'func': gdc_153_gdc_013_gap_down_frequency_1008_013_roc_42},
    'gdc_154_gdc_019_gap_down_frequency_42_019_roc_126': {'inputs': ['gdc_019_gap_down_frequency_42_019'], 'func': gdc_154_gdc_019_gap_down_frequency_42_019_roc_126},
    'gdc_155_gdc_025_gap_down_frequency_378_025_roc_378': {'inputs': ['gdc_025_gap_down_frequency_378_025'], 'func': gdc_155_gdc_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def gdc_replacement_d2_001(gdc_replacement_001):
    feature = _clean(gdc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_001'] = {'inputs': ['gdc_replacement_001'], 'func': gdc_replacement_d2_001}


def gdc_replacement_d2_002(gdc_replacement_002):
    feature = _clean(gdc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_002'] = {'inputs': ['gdc_replacement_002'], 'func': gdc_replacement_d2_002}


def gdc_replacement_d2_003(gdc_replacement_003):
    feature = _clean(gdc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_003'] = {'inputs': ['gdc_replacement_003'], 'func': gdc_replacement_d2_003}


def gdc_replacement_d2_004(gdc_replacement_004):
    feature = _clean(gdc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_004'] = {'inputs': ['gdc_replacement_004'], 'func': gdc_replacement_d2_004}


def gdc_replacement_d2_005(gdc_replacement_005):
    feature = _clean(gdc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_005'] = {'inputs': ['gdc_replacement_005'], 'func': gdc_replacement_d2_005}


def gdc_replacement_d2_006(gdc_replacement_006):
    feature = _clean(gdc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_006'] = {'inputs': ['gdc_replacement_006'], 'func': gdc_replacement_d2_006}


def gdc_replacement_d2_007(gdc_replacement_007):
    feature = _clean(gdc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_007'] = {'inputs': ['gdc_replacement_007'], 'func': gdc_replacement_d2_007}


def gdc_replacement_d2_008(gdc_replacement_008):
    feature = _clean(gdc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_008'] = {'inputs': ['gdc_replacement_008'], 'func': gdc_replacement_d2_008}


def gdc_replacement_d2_009(gdc_replacement_009):
    feature = _clean(gdc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_009'] = {'inputs': ['gdc_replacement_009'], 'func': gdc_replacement_d2_009}


def gdc_replacement_d2_010(gdc_replacement_010):
    feature = _clean(gdc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_010'] = {'inputs': ['gdc_replacement_010'], 'func': gdc_replacement_d2_010}


def gdc_replacement_d2_011(gdc_replacement_011):
    feature = _clean(gdc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_011'] = {'inputs': ['gdc_replacement_011'], 'func': gdc_replacement_d2_011}


def gdc_replacement_d2_012(gdc_replacement_012):
    feature = _clean(gdc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_012'] = {'inputs': ['gdc_replacement_012'], 'func': gdc_replacement_d2_012}


def gdc_replacement_d2_013(gdc_replacement_013):
    feature = _clean(gdc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_013'] = {'inputs': ['gdc_replacement_013'], 'func': gdc_replacement_d2_013}


def gdc_replacement_d2_014(gdc_replacement_014):
    feature = _clean(gdc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_014'] = {'inputs': ['gdc_replacement_014'], 'func': gdc_replacement_d2_014}


def gdc_replacement_d2_015(gdc_replacement_015):
    feature = _clean(gdc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_015'] = {'inputs': ['gdc_replacement_015'], 'func': gdc_replacement_d2_015}


def gdc_replacement_d2_016(gdc_replacement_016):
    feature = _clean(gdc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_016'] = {'inputs': ['gdc_replacement_016'], 'func': gdc_replacement_d2_016}


def gdc_replacement_d2_017(gdc_replacement_017):
    feature = _clean(gdc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_017'] = {'inputs': ['gdc_replacement_017'], 'func': gdc_replacement_d2_017}


def gdc_replacement_d2_018(gdc_replacement_018):
    feature = _clean(gdc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_018'] = {'inputs': ['gdc_replacement_018'], 'func': gdc_replacement_d2_018}


def gdc_replacement_d2_019(gdc_replacement_019):
    feature = _clean(gdc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_019'] = {'inputs': ['gdc_replacement_019'], 'func': gdc_replacement_d2_019}


def gdc_replacement_d2_020(gdc_replacement_020):
    feature = _clean(gdc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_020'] = {'inputs': ['gdc_replacement_020'], 'func': gdc_replacement_d2_020}


def gdc_replacement_d2_021(gdc_replacement_021):
    feature = _clean(gdc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_021'] = {'inputs': ['gdc_replacement_021'], 'func': gdc_replacement_d2_021}


def gdc_replacement_d2_022(gdc_replacement_022):
    feature = _clean(gdc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_022'] = {'inputs': ['gdc_replacement_022'], 'func': gdc_replacement_d2_022}


def gdc_replacement_d2_023(gdc_replacement_023):
    feature = _clean(gdc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_023'] = {'inputs': ['gdc_replacement_023'], 'func': gdc_replacement_d2_023}


def gdc_replacement_d2_024(gdc_replacement_024):
    feature = _clean(gdc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_024'] = {'inputs': ['gdc_replacement_024'], 'func': gdc_replacement_d2_024}


def gdc_replacement_d2_025(gdc_replacement_025):
    feature = _clean(gdc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_025'] = {'inputs': ['gdc_replacement_025'], 'func': gdc_replacement_d2_025}


def gdc_replacement_d2_026(gdc_replacement_026):
    feature = _clean(gdc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_026'] = {'inputs': ['gdc_replacement_026'], 'func': gdc_replacement_d2_026}


def gdc_replacement_d2_027(gdc_replacement_027):
    feature = _clean(gdc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_027'] = {'inputs': ['gdc_replacement_027'], 'func': gdc_replacement_d2_027}


def gdc_replacement_d2_028(gdc_replacement_028):
    feature = _clean(gdc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_028'] = {'inputs': ['gdc_replacement_028'], 'func': gdc_replacement_d2_028}


def gdc_replacement_d2_029(gdc_replacement_029):
    feature = _clean(gdc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_029'] = {'inputs': ['gdc_replacement_029'], 'func': gdc_replacement_d2_029}


def gdc_replacement_d2_030(gdc_replacement_030):
    feature = _clean(gdc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_030'] = {'inputs': ['gdc_replacement_030'], 'func': gdc_replacement_d2_030}


def gdc_replacement_d2_031(gdc_replacement_031):
    feature = _clean(gdc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_031'] = {'inputs': ['gdc_replacement_031'], 'func': gdc_replacement_d2_031}


def gdc_replacement_d2_032(gdc_replacement_032):
    feature = _clean(gdc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_032'] = {'inputs': ['gdc_replacement_032'], 'func': gdc_replacement_d2_032}


def gdc_replacement_d2_033(gdc_replacement_033):
    feature = _clean(gdc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_033'] = {'inputs': ['gdc_replacement_033'], 'func': gdc_replacement_d2_033}


def gdc_replacement_d2_034(gdc_replacement_034):
    feature = _clean(gdc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_034'] = {'inputs': ['gdc_replacement_034'], 'func': gdc_replacement_d2_034}


def gdc_replacement_d2_035(gdc_replacement_035):
    feature = _clean(gdc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_035'] = {'inputs': ['gdc_replacement_035'], 'func': gdc_replacement_d2_035}


def gdc_replacement_d2_036(gdc_replacement_036):
    feature = _clean(gdc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_036'] = {'inputs': ['gdc_replacement_036'], 'func': gdc_replacement_d2_036}


def gdc_replacement_d2_037(gdc_replacement_037):
    feature = _clean(gdc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_037'] = {'inputs': ['gdc_replacement_037'], 'func': gdc_replacement_d2_037}


def gdc_replacement_d2_038(gdc_replacement_038):
    feature = _clean(gdc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_038'] = {'inputs': ['gdc_replacement_038'], 'func': gdc_replacement_d2_038}


def gdc_replacement_d2_039(gdc_replacement_039):
    feature = _clean(gdc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_039'] = {'inputs': ['gdc_replacement_039'], 'func': gdc_replacement_d2_039}


def gdc_replacement_d2_040(gdc_replacement_040):
    feature = _clean(gdc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_040'] = {'inputs': ['gdc_replacement_040'], 'func': gdc_replacement_d2_040}


def gdc_replacement_d2_041(gdc_replacement_041):
    feature = _clean(gdc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_041'] = {'inputs': ['gdc_replacement_041'], 'func': gdc_replacement_d2_041}


def gdc_replacement_d2_042(gdc_replacement_042):
    feature = _clean(gdc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_042'] = {'inputs': ['gdc_replacement_042'], 'func': gdc_replacement_d2_042}


def gdc_replacement_d2_043(gdc_replacement_043):
    feature = _clean(gdc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_043'] = {'inputs': ['gdc_replacement_043'], 'func': gdc_replacement_d2_043}


def gdc_replacement_d2_044(gdc_replacement_044):
    feature = _clean(gdc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_044'] = {'inputs': ['gdc_replacement_044'], 'func': gdc_replacement_d2_044}


def gdc_replacement_d2_045(gdc_replacement_045):
    feature = _clean(gdc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_045'] = {'inputs': ['gdc_replacement_045'], 'func': gdc_replacement_d2_045}


def gdc_replacement_d2_046(gdc_replacement_046):
    feature = _clean(gdc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_046'] = {'inputs': ['gdc_replacement_046'], 'func': gdc_replacement_d2_046}


def gdc_replacement_d2_047(gdc_replacement_047):
    feature = _clean(gdc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_047'] = {'inputs': ['gdc_replacement_047'], 'func': gdc_replacement_d2_047}


def gdc_replacement_d2_048(gdc_replacement_048):
    feature = _clean(gdc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_048'] = {'inputs': ['gdc_replacement_048'], 'func': gdc_replacement_d2_048}


def gdc_replacement_d2_049(gdc_replacement_049):
    feature = _clean(gdc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_049'] = {'inputs': ['gdc_replacement_049'], 'func': gdc_replacement_d2_049}


def gdc_replacement_d2_050(gdc_replacement_050):
    feature = _clean(gdc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_050'] = {'inputs': ['gdc_replacement_050'], 'func': gdc_replacement_d2_050}


def gdc_replacement_d2_051(gdc_replacement_051):
    feature = _clean(gdc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_051'] = {'inputs': ['gdc_replacement_051'], 'func': gdc_replacement_d2_051}


def gdc_replacement_d2_052(gdc_replacement_052):
    feature = _clean(gdc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_052'] = {'inputs': ['gdc_replacement_052'], 'func': gdc_replacement_d2_052}


def gdc_replacement_d2_053(gdc_replacement_053):
    feature = _clean(gdc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_053'] = {'inputs': ['gdc_replacement_053'], 'func': gdc_replacement_d2_053}


def gdc_replacement_d2_054(gdc_replacement_054):
    feature = _clean(gdc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_054'] = {'inputs': ['gdc_replacement_054'], 'func': gdc_replacement_d2_054}


def gdc_replacement_d2_055(gdc_replacement_055):
    feature = _clean(gdc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_055'] = {'inputs': ['gdc_replacement_055'], 'func': gdc_replacement_d2_055}


def gdc_replacement_d2_056(gdc_replacement_056):
    feature = _clean(gdc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_056'] = {'inputs': ['gdc_replacement_056'], 'func': gdc_replacement_d2_056}


def gdc_replacement_d2_057(gdc_replacement_057):
    feature = _clean(gdc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_057'] = {'inputs': ['gdc_replacement_057'], 'func': gdc_replacement_d2_057}


def gdc_replacement_d2_058(gdc_replacement_058):
    feature = _clean(gdc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_058'] = {'inputs': ['gdc_replacement_058'], 'func': gdc_replacement_d2_058}


def gdc_replacement_d2_059(gdc_replacement_059):
    feature = _clean(gdc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_059'] = {'inputs': ['gdc_replacement_059'], 'func': gdc_replacement_d2_059}


def gdc_replacement_d2_060(gdc_replacement_060):
    feature = _clean(gdc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_060'] = {'inputs': ['gdc_replacement_060'], 'func': gdc_replacement_d2_060}


def gdc_replacement_d2_061(gdc_replacement_061):
    feature = _clean(gdc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_061'] = {'inputs': ['gdc_replacement_061'], 'func': gdc_replacement_d2_061}


def gdc_replacement_d2_062(gdc_replacement_062):
    feature = _clean(gdc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_062'] = {'inputs': ['gdc_replacement_062'], 'func': gdc_replacement_d2_062}


def gdc_replacement_d2_063(gdc_replacement_063):
    feature = _clean(gdc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_063'] = {'inputs': ['gdc_replacement_063'], 'func': gdc_replacement_d2_063}


def gdc_replacement_d2_064(gdc_replacement_064):
    feature = _clean(gdc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_064'] = {'inputs': ['gdc_replacement_064'], 'func': gdc_replacement_d2_064}


def gdc_replacement_d2_065(gdc_replacement_065):
    feature = _clean(gdc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_065'] = {'inputs': ['gdc_replacement_065'], 'func': gdc_replacement_d2_065}


def gdc_replacement_d2_066(gdc_replacement_066):
    feature = _clean(gdc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_066'] = {'inputs': ['gdc_replacement_066'], 'func': gdc_replacement_d2_066}


def gdc_replacement_d2_067(gdc_replacement_067):
    feature = _clean(gdc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_067'] = {'inputs': ['gdc_replacement_067'], 'func': gdc_replacement_d2_067}


def gdc_replacement_d2_068(gdc_replacement_068):
    feature = _clean(gdc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_068'] = {'inputs': ['gdc_replacement_068'], 'func': gdc_replacement_d2_068}


def gdc_replacement_d2_069(gdc_replacement_069):
    feature = _clean(gdc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_069'] = {'inputs': ['gdc_replacement_069'], 'func': gdc_replacement_d2_069}


def gdc_replacement_d2_070(gdc_replacement_070):
    feature = _clean(gdc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_070'] = {'inputs': ['gdc_replacement_070'], 'func': gdc_replacement_d2_070}


def gdc_replacement_d2_071(gdc_replacement_071):
    feature = _clean(gdc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_071'] = {'inputs': ['gdc_replacement_071'], 'func': gdc_replacement_d2_071}


def gdc_replacement_d2_072(gdc_replacement_072):
    feature = _clean(gdc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_072'] = {'inputs': ['gdc_replacement_072'], 'func': gdc_replacement_d2_072}


def gdc_replacement_d2_073(gdc_replacement_073):
    feature = _clean(gdc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_073'] = {'inputs': ['gdc_replacement_073'], 'func': gdc_replacement_d2_073}


def gdc_replacement_d2_074(gdc_replacement_074):
    feature = _clean(gdc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_074'] = {'inputs': ['gdc_replacement_074'], 'func': gdc_replacement_d2_074}


def gdc_replacement_d2_075(gdc_replacement_075):
    feature = _clean(gdc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_075'] = {'inputs': ['gdc_replacement_075'], 'func': gdc_replacement_d2_075}


def gdc_replacement_d2_076(gdc_replacement_076):
    feature = _clean(gdc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_076'] = {'inputs': ['gdc_replacement_076'], 'func': gdc_replacement_d2_076}


def gdc_replacement_d2_077(gdc_replacement_077):
    feature = _clean(gdc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_077'] = {'inputs': ['gdc_replacement_077'], 'func': gdc_replacement_d2_077}


def gdc_replacement_d2_078(gdc_replacement_078):
    feature = _clean(gdc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_078'] = {'inputs': ['gdc_replacement_078'], 'func': gdc_replacement_d2_078}


def gdc_replacement_d2_079(gdc_replacement_079):
    feature = _clean(gdc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_079'] = {'inputs': ['gdc_replacement_079'], 'func': gdc_replacement_d2_079}


def gdc_replacement_d2_080(gdc_replacement_080):
    feature = _clean(gdc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_080'] = {'inputs': ['gdc_replacement_080'], 'func': gdc_replacement_d2_080}


def gdc_replacement_d2_081(gdc_replacement_081):
    feature = _clean(gdc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_081'] = {'inputs': ['gdc_replacement_081'], 'func': gdc_replacement_d2_081}


def gdc_replacement_d2_082(gdc_replacement_082):
    feature = _clean(gdc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_082'] = {'inputs': ['gdc_replacement_082'], 'func': gdc_replacement_d2_082}


def gdc_replacement_d2_083(gdc_replacement_083):
    feature = _clean(gdc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_083'] = {'inputs': ['gdc_replacement_083'], 'func': gdc_replacement_d2_083}


def gdc_replacement_d2_084(gdc_replacement_084):
    feature = _clean(gdc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_084'] = {'inputs': ['gdc_replacement_084'], 'func': gdc_replacement_d2_084}


def gdc_replacement_d2_085(gdc_replacement_085):
    feature = _clean(gdc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_085'] = {'inputs': ['gdc_replacement_085'], 'func': gdc_replacement_d2_085}


def gdc_replacement_d2_086(gdc_replacement_086):
    feature = _clean(gdc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_086'] = {'inputs': ['gdc_replacement_086'], 'func': gdc_replacement_d2_086}


def gdc_replacement_d2_087(gdc_replacement_087):
    feature = _clean(gdc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_087'] = {'inputs': ['gdc_replacement_087'], 'func': gdc_replacement_d2_087}


def gdc_replacement_d2_088(gdc_replacement_088):
    feature = _clean(gdc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_088'] = {'inputs': ['gdc_replacement_088'], 'func': gdc_replacement_d2_088}


def gdc_replacement_d2_089(gdc_replacement_089):
    feature = _clean(gdc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_089'] = {'inputs': ['gdc_replacement_089'], 'func': gdc_replacement_d2_089}


def gdc_replacement_d2_090(gdc_replacement_090):
    feature = _clean(gdc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_090'] = {'inputs': ['gdc_replacement_090'], 'func': gdc_replacement_d2_090}


def gdc_replacement_d2_091(gdc_replacement_091):
    feature = _clean(gdc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_091'] = {'inputs': ['gdc_replacement_091'], 'func': gdc_replacement_d2_091}


def gdc_replacement_d2_092(gdc_replacement_092):
    feature = _clean(gdc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_092'] = {'inputs': ['gdc_replacement_092'], 'func': gdc_replacement_d2_092}


def gdc_replacement_d2_093(gdc_replacement_093):
    feature = _clean(gdc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_093'] = {'inputs': ['gdc_replacement_093'], 'func': gdc_replacement_d2_093}


def gdc_replacement_d2_094(gdc_replacement_094):
    feature = _clean(gdc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_094'] = {'inputs': ['gdc_replacement_094'], 'func': gdc_replacement_d2_094}


def gdc_replacement_d2_095(gdc_replacement_095):
    feature = _clean(gdc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_095'] = {'inputs': ['gdc_replacement_095'], 'func': gdc_replacement_d2_095}


def gdc_replacement_d2_096(gdc_replacement_096):
    feature = _clean(gdc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_096'] = {'inputs': ['gdc_replacement_096'], 'func': gdc_replacement_d2_096}


def gdc_replacement_d2_097(gdc_replacement_097):
    feature = _clean(gdc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_097'] = {'inputs': ['gdc_replacement_097'], 'func': gdc_replacement_d2_097}


def gdc_replacement_d2_098(gdc_replacement_098):
    feature = _clean(gdc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_098'] = {'inputs': ['gdc_replacement_098'], 'func': gdc_replacement_d2_098}


def gdc_replacement_d2_099(gdc_replacement_099):
    feature = _clean(gdc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_099'] = {'inputs': ['gdc_replacement_099'], 'func': gdc_replacement_d2_099}


def gdc_replacement_d2_100(gdc_replacement_100):
    feature = _clean(gdc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_100'] = {'inputs': ['gdc_replacement_100'], 'func': gdc_replacement_d2_100}


def gdc_replacement_d2_101(gdc_replacement_101):
    feature = _clean(gdc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_101'] = {'inputs': ['gdc_replacement_101'], 'func': gdc_replacement_d2_101}


def gdc_replacement_d2_102(gdc_replacement_102):
    feature = _clean(gdc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_102'] = {'inputs': ['gdc_replacement_102'], 'func': gdc_replacement_d2_102}


def gdc_replacement_d2_103(gdc_replacement_103):
    feature = _clean(gdc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_103'] = {'inputs': ['gdc_replacement_103'], 'func': gdc_replacement_d2_103}


def gdc_replacement_d2_104(gdc_replacement_104):
    feature = _clean(gdc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_104'] = {'inputs': ['gdc_replacement_104'], 'func': gdc_replacement_d2_104}


def gdc_replacement_d2_105(gdc_replacement_105):
    feature = _clean(gdc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_105'] = {'inputs': ['gdc_replacement_105'], 'func': gdc_replacement_d2_105}


def gdc_replacement_d2_106(gdc_replacement_106):
    feature = _clean(gdc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_106'] = {'inputs': ['gdc_replacement_106'], 'func': gdc_replacement_d2_106}


def gdc_replacement_d2_107(gdc_replacement_107):
    feature = _clean(gdc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_107'] = {'inputs': ['gdc_replacement_107'], 'func': gdc_replacement_d2_107}


def gdc_replacement_d2_108(gdc_replacement_108):
    feature = _clean(gdc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_108'] = {'inputs': ['gdc_replacement_108'], 'func': gdc_replacement_d2_108}


def gdc_replacement_d2_109(gdc_replacement_109):
    feature = _clean(gdc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_109'] = {'inputs': ['gdc_replacement_109'], 'func': gdc_replacement_d2_109}


def gdc_replacement_d2_110(gdc_replacement_110):
    feature = _clean(gdc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_110'] = {'inputs': ['gdc_replacement_110'], 'func': gdc_replacement_d2_110}


def gdc_replacement_d2_111(gdc_replacement_111):
    feature = _clean(gdc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_111'] = {'inputs': ['gdc_replacement_111'], 'func': gdc_replacement_d2_111}


def gdc_replacement_d2_112(gdc_replacement_112):
    feature = _clean(gdc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_112'] = {'inputs': ['gdc_replacement_112'], 'func': gdc_replacement_d2_112}


def gdc_replacement_d2_113(gdc_replacement_113):
    feature = _clean(gdc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_113'] = {'inputs': ['gdc_replacement_113'], 'func': gdc_replacement_d2_113}


def gdc_replacement_d2_114(gdc_replacement_114):
    feature = _clean(gdc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_114'] = {'inputs': ['gdc_replacement_114'], 'func': gdc_replacement_d2_114}


def gdc_replacement_d2_115(gdc_replacement_115):
    feature = _clean(gdc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_115'] = {'inputs': ['gdc_replacement_115'], 'func': gdc_replacement_d2_115}


def gdc_replacement_d2_116(gdc_replacement_116):
    feature = _clean(gdc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_116'] = {'inputs': ['gdc_replacement_116'], 'func': gdc_replacement_d2_116}


def gdc_replacement_d2_117(gdc_replacement_117):
    feature = _clean(gdc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_117'] = {'inputs': ['gdc_replacement_117'], 'func': gdc_replacement_d2_117}


def gdc_replacement_d2_118(gdc_replacement_118):
    feature = _clean(gdc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_118'] = {'inputs': ['gdc_replacement_118'], 'func': gdc_replacement_d2_118}


def gdc_replacement_d2_119(gdc_replacement_119):
    feature = _clean(gdc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_119'] = {'inputs': ['gdc_replacement_119'], 'func': gdc_replacement_d2_119}


def gdc_replacement_d2_120(gdc_replacement_120):
    feature = _clean(gdc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_120'] = {'inputs': ['gdc_replacement_120'], 'func': gdc_replacement_d2_120}


def gdc_replacement_d2_121(gdc_replacement_121):
    feature = _clean(gdc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_121'] = {'inputs': ['gdc_replacement_121'], 'func': gdc_replacement_d2_121}


def gdc_replacement_d2_122(gdc_replacement_122):
    feature = _clean(gdc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_122'] = {'inputs': ['gdc_replacement_122'], 'func': gdc_replacement_d2_122}


def gdc_replacement_d2_123(gdc_replacement_123):
    feature = _clean(gdc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_123'] = {'inputs': ['gdc_replacement_123'], 'func': gdc_replacement_d2_123}


def gdc_replacement_d2_124(gdc_replacement_124):
    feature = _clean(gdc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_124'] = {'inputs': ['gdc_replacement_124'], 'func': gdc_replacement_d2_124}


def gdc_replacement_d2_125(gdc_replacement_125):
    feature = _clean(gdc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_125'] = {'inputs': ['gdc_replacement_125'], 'func': gdc_replacement_d2_125}


def gdc_replacement_d2_126(gdc_replacement_126):
    feature = _clean(gdc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_126'] = {'inputs': ['gdc_replacement_126'], 'func': gdc_replacement_d2_126}


def gdc_replacement_d2_127(gdc_replacement_127):
    feature = _clean(gdc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_127'] = {'inputs': ['gdc_replacement_127'], 'func': gdc_replacement_d2_127}


def gdc_replacement_d2_128(gdc_replacement_128):
    feature = _clean(gdc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_128'] = {'inputs': ['gdc_replacement_128'], 'func': gdc_replacement_d2_128}


def gdc_replacement_d2_129(gdc_replacement_129):
    feature = _clean(gdc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_129'] = {'inputs': ['gdc_replacement_129'], 'func': gdc_replacement_d2_129}


def gdc_replacement_d2_130(gdc_replacement_130):
    feature = _clean(gdc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_130'] = {'inputs': ['gdc_replacement_130'], 'func': gdc_replacement_d2_130}


def gdc_replacement_d2_131(gdc_replacement_131):
    feature = _clean(gdc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_131'] = {'inputs': ['gdc_replacement_131'], 'func': gdc_replacement_d2_131}


def gdc_replacement_d2_132(gdc_replacement_132):
    feature = _clean(gdc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_132'] = {'inputs': ['gdc_replacement_132'], 'func': gdc_replacement_d2_132}


def gdc_replacement_d2_133(gdc_replacement_133):
    feature = _clean(gdc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_133'] = {'inputs': ['gdc_replacement_133'], 'func': gdc_replacement_d2_133}


def gdc_replacement_d2_134(gdc_replacement_134):
    feature = _clean(gdc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_134'] = {'inputs': ['gdc_replacement_134'], 'func': gdc_replacement_d2_134}


def gdc_replacement_d2_135(gdc_replacement_135):
    feature = _clean(gdc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_135'] = {'inputs': ['gdc_replacement_135'], 'func': gdc_replacement_d2_135}


def gdc_replacement_d2_136(gdc_replacement_136):
    feature = _clean(gdc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_136'] = {'inputs': ['gdc_replacement_136'], 'func': gdc_replacement_d2_136}


def gdc_replacement_d2_137(gdc_replacement_137):
    feature = _clean(gdc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_137'] = {'inputs': ['gdc_replacement_137'], 'func': gdc_replacement_d2_137}


def gdc_replacement_d2_138(gdc_replacement_138):
    feature = _clean(gdc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_138'] = {'inputs': ['gdc_replacement_138'], 'func': gdc_replacement_d2_138}


def gdc_replacement_d2_139(gdc_replacement_139):
    feature = _clean(gdc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_139'] = {'inputs': ['gdc_replacement_139'], 'func': gdc_replacement_d2_139}


def gdc_replacement_d2_140(gdc_replacement_140):
    feature = _clean(gdc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_140'] = {'inputs': ['gdc_replacement_140'], 'func': gdc_replacement_d2_140}


def gdc_replacement_d2_141(gdc_replacement_141):
    feature = _clean(gdc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_141'] = {'inputs': ['gdc_replacement_141'], 'func': gdc_replacement_d2_141}


def gdc_replacement_d2_142(gdc_replacement_142):
    feature = _clean(gdc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_142'] = {'inputs': ['gdc_replacement_142'], 'func': gdc_replacement_d2_142}


def gdc_replacement_d2_143(gdc_replacement_143):
    feature = _clean(gdc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_143'] = {'inputs': ['gdc_replacement_143'], 'func': gdc_replacement_d2_143}


def gdc_replacement_d2_144(gdc_replacement_144):
    feature = _clean(gdc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_144'] = {'inputs': ['gdc_replacement_144'], 'func': gdc_replacement_d2_144}


def gdc_replacement_d2_145(gdc_replacement_145):
    feature = _clean(gdc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_145'] = {'inputs': ['gdc_replacement_145'], 'func': gdc_replacement_d2_145}


def gdc_replacement_d2_146(gdc_replacement_146):
    feature = _clean(gdc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_146'] = {'inputs': ['gdc_replacement_146'], 'func': gdc_replacement_d2_146}


def gdc_replacement_d2_147(gdc_replacement_147):
    feature = _clean(gdc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_147'] = {'inputs': ['gdc_replacement_147'], 'func': gdc_replacement_d2_147}


def gdc_replacement_d2_148(gdc_replacement_148):
    feature = _clean(gdc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_148'] = {'inputs': ['gdc_replacement_148'], 'func': gdc_replacement_d2_148}


def gdc_replacement_d2_149(gdc_replacement_149):
    feature = _clean(gdc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_149'] = {'inputs': ['gdc_replacement_149'], 'func': gdc_replacement_d2_149}


def gdc_replacement_d2_150(gdc_replacement_150):
    feature = _clean(gdc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_150'] = {'inputs': ['gdc_replacement_150'], 'func': gdc_replacement_d2_150}


def gdc_replacement_d2_151(gdc_replacement_151):
    feature = _clean(gdc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_151'] = {'inputs': ['gdc_replacement_151'], 'func': gdc_replacement_d2_151}


def gdc_replacement_d2_152(gdc_replacement_152):
    feature = _clean(gdc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_152'] = {'inputs': ['gdc_replacement_152'], 'func': gdc_replacement_d2_152}


def gdc_replacement_d2_153(gdc_replacement_153):
    feature = _clean(gdc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_153'] = {'inputs': ['gdc_replacement_153'], 'func': gdc_replacement_d2_153}


def gdc_replacement_d2_154(gdc_replacement_154):
    feature = _clean(gdc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_154'] = {'inputs': ['gdc_replacement_154'], 'func': gdc_replacement_d2_154}


def gdc_replacement_d2_155(gdc_replacement_155):
    feature = _clean(gdc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_155'] = {'inputs': ['gdc_replacement_155'], 'func': gdc_replacement_d2_155}


def gdc_replacement_d2_156(gdc_replacement_156):
    feature = _clean(gdc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_156'] = {'inputs': ['gdc_replacement_156'], 'func': gdc_replacement_d2_156}


def gdc_replacement_d2_157(gdc_replacement_157):
    feature = _clean(gdc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_157'] = {'inputs': ['gdc_replacement_157'], 'func': gdc_replacement_d2_157}


def gdc_replacement_d2_158(gdc_replacement_158):
    feature = _clean(gdc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_158'] = {'inputs': ['gdc_replacement_158'], 'func': gdc_replacement_d2_158}


def gdc_replacement_d2_159(gdc_replacement_159):
    feature = _clean(gdc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_159'] = {'inputs': ['gdc_replacement_159'], 'func': gdc_replacement_d2_159}


def gdc_replacement_d2_160(gdc_replacement_160):
    feature = _clean(gdc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
GDC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gdc_replacement_d2_160'] = {'inputs': ['gdc_replacement_160'], 'func': gdc_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002(gdc_002_gap_magnitude_10_002):
    return _base_universe_d2(gdc_002_gap_magnitude_10_002, 1)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002'] = {'inputs': ['gdc_002_gap_magnitude_10_002'], 'func': gdc_base_universe_d2_001_gdc_002_gap_magnitude_10_002}


def gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003(gdc_003_open_close_pressure_21_003):
    return _base_universe_d2(gdc_003_open_close_pressure_21_003, 2)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003'] = {'inputs': ['gdc_003_open_close_pressure_21_003'], 'func': gdc_base_universe_d2_002_gdc_003_open_close_pressure_21_003}


def gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004(gdc_004_lower_wick_ratio_42_004):
    return _base_universe_d2(gdc_004_lower_wick_ratio_42_004, 3)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004'] = {'inputs': ['gdc_004_lower_wick_ratio_42_004'], 'func': gdc_base_universe_d2_003_gdc_004_lower_wick_ratio_42_004}


def gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005(gdc_005_upper_wick_ratio_63_005):
    return _base_universe_d2(gdc_005_upper_wick_ratio_63_005, 4)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005'] = {'inputs': ['gdc_005_upper_wick_ratio_63_005'], 'func': gdc_base_universe_d2_004_gdc_005_upper_wick_ratio_63_005}


def gdc_base_universe_d2_005_gdc_006_body_to_range_84_006(gdc_006_body_to_range_84_006):
    return _base_universe_d2(gdc_006_body_to_range_84_006, 5)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_005_gdc_006_body_to_range_84_006'] = {'inputs': ['gdc_006_body_to_range_84_006'], 'func': gdc_base_universe_d2_005_gdc_006_body_to_range_84_006}


def gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008(gdc_008_gap_magnitude_189_008):
    return _base_universe_d2(gdc_008_gap_magnitude_189_008, 6)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008'] = {'inputs': ['gdc_008_gap_magnitude_189_008'], 'func': gdc_base_universe_d2_006_gdc_008_gap_magnitude_189_008}


def gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009(gdc_009_open_close_pressure_252_009):
    return _base_universe_d2(gdc_009_open_close_pressure_252_009, 7)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009'] = {'inputs': ['gdc_009_open_close_pressure_252_009'], 'func': gdc_base_universe_d2_007_gdc_009_open_close_pressure_252_009}


def gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010(gdc_010_lower_wick_ratio_378_010):
    return _base_universe_d2(gdc_010_lower_wick_ratio_378_010, 8)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010'] = {'inputs': ['gdc_010_lower_wick_ratio_378_010'], 'func': gdc_base_universe_d2_008_gdc_010_lower_wick_ratio_378_010}


def gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011(gdc_011_upper_wick_ratio_504_011):
    return _base_universe_d2(gdc_011_upper_wick_ratio_504_011, 9)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011'] = {'inputs': ['gdc_011_upper_wick_ratio_504_011'], 'func': gdc_base_universe_d2_009_gdc_011_upper_wick_ratio_504_011}


def gdc_base_universe_d2_010_gdc_012_body_to_range_756_012(gdc_012_body_to_range_756_012):
    return _base_universe_d2(gdc_012_body_to_range_756_012, 10)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_010_gdc_012_body_to_range_756_012'] = {'inputs': ['gdc_012_body_to_range_756_012'], 'func': gdc_base_universe_d2_010_gdc_012_body_to_range_756_012}


def gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014(gdc_014_gap_magnitude_1260_014):
    return _base_universe_d2(gdc_014_gap_magnitude_1260_014, 11)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014'] = {'inputs': ['gdc_014_gap_magnitude_1260_014'], 'func': gdc_base_universe_d2_011_gdc_014_gap_magnitude_1260_014}


def gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015(gdc_015_open_close_pressure_1512_015):
    return _base_universe_d2(gdc_015_open_close_pressure_1512_015, 12)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015'] = {'inputs': ['gdc_015_open_close_pressure_1512_015'], 'func': gdc_base_universe_d2_012_gdc_015_open_close_pressure_1512_015}


def gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016(gdc_016_lower_wick_ratio_5_016):
    return _base_universe_d2(gdc_016_lower_wick_ratio_5_016, 13)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016'] = {'inputs': ['gdc_016_lower_wick_ratio_5_016'], 'func': gdc_base_universe_d2_013_gdc_016_lower_wick_ratio_5_016}


def gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017(gdc_017_upper_wick_ratio_10_017):
    return _base_universe_d2(gdc_017_upper_wick_ratio_10_017, 14)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017'] = {'inputs': ['gdc_017_upper_wick_ratio_10_017'], 'func': gdc_base_universe_d2_014_gdc_017_upper_wick_ratio_10_017}


def gdc_base_universe_d2_015_gdc_018_body_to_range_21_018(gdc_018_body_to_range_21_018):
    return _base_universe_d2(gdc_018_body_to_range_21_018, 15)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_015_gdc_018_body_to_range_21_018'] = {'inputs': ['gdc_018_body_to_range_21_018'], 'func': gdc_base_universe_d2_015_gdc_018_body_to_range_21_018}


def gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020(gdc_020_gap_magnitude_63_020):
    return _base_universe_d2(gdc_020_gap_magnitude_63_020, 16)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020'] = {'inputs': ['gdc_020_gap_magnitude_63_020'], 'func': gdc_base_universe_d2_016_gdc_020_gap_magnitude_63_020}


def gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021(gdc_021_open_close_pressure_84_021):
    return _base_universe_d2(gdc_021_open_close_pressure_84_021, 17)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021'] = {'inputs': ['gdc_021_open_close_pressure_84_021'], 'func': gdc_base_universe_d2_017_gdc_021_open_close_pressure_84_021}


def gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022(gdc_022_lower_wick_ratio_126_022):
    return _base_universe_d2(gdc_022_lower_wick_ratio_126_022, 18)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022'] = {'inputs': ['gdc_022_lower_wick_ratio_126_022'], 'func': gdc_base_universe_d2_018_gdc_022_lower_wick_ratio_126_022}


def gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023(gdc_023_upper_wick_ratio_189_023):
    return _base_universe_d2(gdc_023_upper_wick_ratio_189_023, 19)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023'] = {'inputs': ['gdc_023_upper_wick_ratio_189_023'], 'func': gdc_base_universe_d2_019_gdc_023_upper_wick_ratio_189_023}


def gdc_base_universe_d2_020_gdc_024_body_to_range_252_024(gdc_024_body_to_range_252_024):
    return _base_universe_d2(gdc_024_body_to_range_252_024, 20)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_020_gdc_024_body_to_range_252_024'] = {'inputs': ['gdc_024_body_to_range_252_024'], 'func': gdc_base_universe_d2_020_gdc_024_body_to_range_252_024}


def gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026(gdc_026_gap_magnitude_504_026):
    return _base_universe_d2(gdc_026_gap_magnitude_504_026, 21)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026'] = {'inputs': ['gdc_026_gap_magnitude_504_026'], 'func': gdc_base_universe_d2_021_gdc_026_gap_magnitude_504_026}


def gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027(gdc_027_open_close_pressure_756_027):
    return _base_universe_d2(gdc_027_open_close_pressure_756_027, 22)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027'] = {'inputs': ['gdc_027_open_close_pressure_756_027'], 'func': gdc_base_universe_d2_022_gdc_027_open_close_pressure_756_027}


def gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028(gdc_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(gdc_028_lower_wick_ratio_1008_028, 23)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028'] = {'inputs': ['gdc_028_lower_wick_ratio_1008_028'], 'func': gdc_base_universe_d2_023_gdc_028_lower_wick_ratio_1008_028}


def gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029(gdc_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(gdc_029_upper_wick_ratio_1260_029, 24)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029'] = {'inputs': ['gdc_029_upper_wick_ratio_1260_029'], 'func': gdc_base_universe_d2_024_gdc_029_upper_wick_ratio_1260_029}


def gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030(gdc_030_body_to_range_1512_030):
    return _base_universe_d2(gdc_030_body_to_range_1512_030, 25)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030'] = {'inputs': ['gdc_030_body_to_range_1512_030'], 'func': gdc_base_universe_d2_025_gdc_030_body_to_range_1512_030}


def gdc_base_universe_d2_026_gdc_basefill_031(gdc_basefill_031):
    return _base_universe_d2(gdc_basefill_031, 26)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_026_gdc_basefill_031'] = {'inputs': ['gdc_basefill_031'], 'func': gdc_base_universe_d2_026_gdc_basefill_031}


def gdc_base_universe_d2_027_gdc_basefill_032(gdc_basefill_032):
    return _base_universe_d2(gdc_basefill_032, 27)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_027_gdc_basefill_032'] = {'inputs': ['gdc_basefill_032'], 'func': gdc_base_universe_d2_027_gdc_basefill_032}


def gdc_base_universe_d2_028_gdc_basefill_033(gdc_basefill_033):
    return _base_universe_d2(gdc_basefill_033, 28)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_028_gdc_basefill_033'] = {'inputs': ['gdc_basefill_033'], 'func': gdc_base_universe_d2_028_gdc_basefill_033}


def gdc_base_universe_d2_029_gdc_basefill_034(gdc_basefill_034):
    return _base_universe_d2(gdc_basefill_034, 29)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_029_gdc_basefill_034'] = {'inputs': ['gdc_basefill_034'], 'func': gdc_base_universe_d2_029_gdc_basefill_034}


def gdc_base_universe_d2_030_gdc_basefill_035(gdc_basefill_035):
    return _base_universe_d2(gdc_basefill_035, 30)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_030_gdc_basefill_035'] = {'inputs': ['gdc_basefill_035'], 'func': gdc_base_universe_d2_030_gdc_basefill_035}


def gdc_base_universe_d2_031_gdc_basefill_036(gdc_basefill_036):
    return _base_universe_d2(gdc_basefill_036, 31)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_031_gdc_basefill_036'] = {'inputs': ['gdc_basefill_036'], 'func': gdc_base_universe_d2_031_gdc_basefill_036}


def gdc_base_universe_d2_032_gdc_basefill_037(gdc_basefill_037):
    return _base_universe_d2(gdc_basefill_037, 32)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_032_gdc_basefill_037'] = {'inputs': ['gdc_basefill_037'], 'func': gdc_base_universe_d2_032_gdc_basefill_037}


def gdc_base_universe_d2_033_gdc_basefill_038(gdc_basefill_038):
    return _base_universe_d2(gdc_basefill_038, 33)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_033_gdc_basefill_038'] = {'inputs': ['gdc_basefill_038'], 'func': gdc_base_universe_d2_033_gdc_basefill_038}


def gdc_base_universe_d2_034_gdc_basefill_039(gdc_basefill_039):
    return _base_universe_d2(gdc_basefill_039, 34)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_034_gdc_basefill_039'] = {'inputs': ['gdc_basefill_039'], 'func': gdc_base_universe_d2_034_gdc_basefill_039}


def gdc_base_universe_d2_035_gdc_basefill_040(gdc_basefill_040):
    return _base_universe_d2(gdc_basefill_040, 35)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_035_gdc_basefill_040'] = {'inputs': ['gdc_basefill_040'], 'func': gdc_base_universe_d2_035_gdc_basefill_040}


def gdc_base_universe_d2_036_gdc_basefill_041(gdc_basefill_041):
    return _base_universe_d2(gdc_basefill_041, 36)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_036_gdc_basefill_041'] = {'inputs': ['gdc_basefill_041'], 'func': gdc_base_universe_d2_036_gdc_basefill_041}


def gdc_base_universe_d2_037_gdc_basefill_042(gdc_basefill_042):
    return _base_universe_d2(gdc_basefill_042, 37)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_037_gdc_basefill_042'] = {'inputs': ['gdc_basefill_042'], 'func': gdc_base_universe_d2_037_gdc_basefill_042}


def gdc_base_universe_d2_038_gdc_basefill_043(gdc_basefill_043):
    return _base_universe_d2(gdc_basefill_043, 38)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_038_gdc_basefill_043'] = {'inputs': ['gdc_basefill_043'], 'func': gdc_base_universe_d2_038_gdc_basefill_043}


def gdc_base_universe_d2_039_gdc_basefill_044(gdc_basefill_044):
    return _base_universe_d2(gdc_basefill_044, 39)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_039_gdc_basefill_044'] = {'inputs': ['gdc_basefill_044'], 'func': gdc_base_universe_d2_039_gdc_basefill_044}


def gdc_base_universe_d2_040_gdc_basefill_045(gdc_basefill_045):
    return _base_universe_d2(gdc_basefill_045, 40)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_040_gdc_basefill_045'] = {'inputs': ['gdc_basefill_045'], 'func': gdc_base_universe_d2_040_gdc_basefill_045}


def gdc_base_universe_d2_041_gdc_basefill_046(gdc_basefill_046):
    return _base_universe_d2(gdc_basefill_046, 41)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_041_gdc_basefill_046'] = {'inputs': ['gdc_basefill_046'], 'func': gdc_base_universe_d2_041_gdc_basefill_046}


def gdc_base_universe_d2_042_gdc_basefill_047(gdc_basefill_047):
    return _base_universe_d2(gdc_basefill_047, 42)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_042_gdc_basefill_047'] = {'inputs': ['gdc_basefill_047'], 'func': gdc_base_universe_d2_042_gdc_basefill_047}


def gdc_base_universe_d2_043_gdc_basefill_048(gdc_basefill_048):
    return _base_universe_d2(gdc_basefill_048, 43)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_043_gdc_basefill_048'] = {'inputs': ['gdc_basefill_048'], 'func': gdc_base_universe_d2_043_gdc_basefill_048}


def gdc_base_universe_d2_044_gdc_basefill_049(gdc_basefill_049):
    return _base_universe_d2(gdc_basefill_049, 44)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_044_gdc_basefill_049'] = {'inputs': ['gdc_basefill_049'], 'func': gdc_base_universe_d2_044_gdc_basefill_049}


def gdc_base_universe_d2_045_gdc_basefill_050(gdc_basefill_050):
    return _base_universe_d2(gdc_basefill_050, 45)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_045_gdc_basefill_050'] = {'inputs': ['gdc_basefill_050'], 'func': gdc_base_universe_d2_045_gdc_basefill_050}


def gdc_base_universe_d2_046_gdc_basefill_051(gdc_basefill_051):
    return _base_universe_d2(gdc_basefill_051, 46)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_046_gdc_basefill_051'] = {'inputs': ['gdc_basefill_051'], 'func': gdc_base_universe_d2_046_gdc_basefill_051}


def gdc_base_universe_d2_047_gdc_basefill_052(gdc_basefill_052):
    return _base_universe_d2(gdc_basefill_052, 47)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_047_gdc_basefill_052'] = {'inputs': ['gdc_basefill_052'], 'func': gdc_base_universe_d2_047_gdc_basefill_052}


def gdc_base_universe_d2_048_gdc_basefill_053(gdc_basefill_053):
    return _base_universe_d2(gdc_basefill_053, 48)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_048_gdc_basefill_053'] = {'inputs': ['gdc_basefill_053'], 'func': gdc_base_universe_d2_048_gdc_basefill_053}


def gdc_base_universe_d2_049_gdc_basefill_054(gdc_basefill_054):
    return _base_universe_d2(gdc_basefill_054, 49)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_049_gdc_basefill_054'] = {'inputs': ['gdc_basefill_054'], 'func': gdc_base_universe_d2_049_gdc_basefill_054}


def gdc_base_universe_d2_050_gdc_basefill_055(gdc_basefill_055):
    return _base_universe_d2(gdc_basefill_055, 50)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_050_gdc_basefill_055'] = {'inputs': ['gdc_basefill_055'], 'func': gdc_base_universe_d2_050_gdc_basefill_055}


def gdc_base_universe_d2_051_gdc_basefill_056(gdc_basefill_056):
    return _base_universe_d2(gdc_basefill_056, 51)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_051_gdc_basefill_056'] = {'inputs': ['gdc_basefill_056'], 'func': gdc_base_universe_d2_051_gdc_basefill_056}


def gdc_base_universe_d2_052_gdc_basefill_057(gdc_basefill_057):
    return _base_universe_d2(gdc_basefill_057, 52)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_052_gdc_basefill_057'] = {'inputs': ['gdc_basefill_057'], 'func': gdc_base_universe_d2_052_gdc_basefill_057}


def gdc_base_universe_d2_053_gdc_basefill_058(gdc_basefill_058):
    return _base_universe_d2(gdc_basefill_058, 53)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_053_gdc_basefill_058'] = {'inputs': ['gdc_basefill_058'], 'func': gdc_base_universe_d2_053_gdc_basefill_058}


def gdc_base_universe_d2_054_gdc_basefill_059(gdc_basefill_059):
    return _base_universe_d2(gdc_basefill_059, 54)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_054_gdc_basefill_059'] = {'inputs': ['gdc_basefill_059'], 'func': gdc_base_universe_d2_054_gdc_basefill_059}


def gdc_base_universe_d2_055_gdc_basefill_060(gdc_basefill_060):
    return _base_universe_d2(gdc_basefill_060, 55)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_055_gdc_basefill_060'] = {'inputs': ['gdc_basefill_060'], 'func': gdc_base_universe_d2_055_gdc_basefill_060}


def gdc_base_universe_d2_056_gdc_basefill_061(gdc_basefill_061):
    return _base_universe_d2(gdc_basefill_061, 56)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_056_gdc_basefill_061'] = {'inputs': ['gdc_basefill_061'], 'func': gdc_base_universe_d2_056_gdc_basefill_061}


def gdc_base_universe_d2_057_gdc_basefill_062(gdc_basefill_062):
    return _base_universe_d2(gdc_basefill_062, 57)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_057_gdc_basefill_062'] = {'inputs': ['gdc_basefill_062'], 'func': gdc_base_universe_d2_057_gdc_basefill_062}


def gdc_base_universe_d2_058_gdc_basefill_063(gdc_basefill_063):
    return _base_universe_d2(gdc_basefill_063, 58)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_058_gdc_basefill_063'] = {'inputs': ['gdc_basefill_063'], 'func': gdc_base_universe_d2_058_gdc_basefill_063}


def gdc_base_universe_d2_059_gdc_basefill_064(gdc_basefill_064):
    return _base_universe_d2(gdc_basefill_064, 59)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_059_gdc_basefill_064'] = {'inputs': ['gdc_basefill_064'], 'func': gdc_base_universe_d2_059_gdc_basefill_064}


def gdc_base_universe_d2_060_gdc_basefill_065(gdc_basefill_065):
    return _base_universe_d2(gdc_basefill_065, 60)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_060_gdc_basefill_065'] = {'inputs': ['gdc_basefill_065'], 'func': gdc_base_universe_d2_060_gdc_basefill_065}


def gdc_base_universe_d2_061_gdc_basefill_066(gdc_basefill_066):
    return _base_universe_d2(gdc_basefill_066, 61)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_061_gdc_basefill_066'] = {'inputs': ['gdc_basefill_066'], 'func': gdc_base_universe_d2_061_gdc_basefill_066}


def gdc_base_universe_d2_062_gdc_basefill_067(gdc_basefill_067):
    return _base_universe_d2(gdc_basefill_067, 62)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_062_gdc_basefill_067'] = {'inputs': ['gdc_basefill_067'], 'func': gdc_base_universe_d2_062_gdc_basefill_067}


def gdc_base_universe_d2_063_gdc_basefill_068(gdc_basefill_068):
    return _base_universe_d2(gdc_basefill_068, 63)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_063_gdc_basefill_068'] = {'inputs': ['gdc_basefill_068'], 'func': gdc_base_universe_d2_063_gdc_basefill_068}


def gdc_base_universe_d2_064_gdc_basefill_069(gdc_basefill_069):
    return _base_universe_d2(gdc_basefill_069, 64)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_064_gdc_basefill_069'] = {'inputs': ['gdc_basefill_069'], 'func': gdc_base_universe_d2_064_gdc_basefill_069}


def gdc_base_universe_d2_065_gdc_basefill_070(gdc_basefill_070):
    return _base_universe_d2(gdc_basefill_070, 65)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_065_gdc_basefill_070'] = {'inputs': ['gdc_basefill_070'], 'func': gdc_base_universe_d2_065_gdc_basefill_070}


def gdc_base_universe_d2_066_gdc_basefill_071(gdc_basefill_071):
    return _base_universe_d2(gdc_basefill_071, 66)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_066_gdc_basefill_071'] = {'inputs': ['gdc_basefill_071'], 'func': gdc_base_universe_d2_066_gdc_basefill_071}


def gdc_base_universe_d2_067_gdc_basefill_072(gdc_basefill_072):
    return _base_universe_d2(gdc_basefill_072, 67)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_067_gdc_basefill_072'] = {'inputs': ['gdc_basefill_072'], 'func': gdc_base_universe_d2_067_gdc_basefill_072}


def gdc_base_universe_d2_068_gdc_basefill_073(gdc_basefill_073):
    return _base_universe_d2(gdc_basefill_073, 68)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_068_gdc_basefill_073'] = {'inputs': ['gdc_basefill_073'], 'func': gdc_base_universe_d2_068_gdc_basefill_073}


def gdc_base_universe_d2_069_gdc_basefill_074(gdc_basefill_074):
    return _base_universe_d2(gdc_basefill_074, 69)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_069_gdc_basefill_074'] = {'inputs': ['gdc_basefill_074'], 'func': gdc_base_universe_d2_069_gdc_basefill_074}


def gdc_base_universe_d2_070_gdc_basefill_075(gdc_basefill_075):
    return _base_universe_d2(gdc_basefill_075, 70)
GDC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gdc_base_universe_d2_070_gdc_basefill_075'] = {'inputs': ['gdc_basefill_075'], 'func': gdc_base_universe_d2_070_gdc_basefill_075}
