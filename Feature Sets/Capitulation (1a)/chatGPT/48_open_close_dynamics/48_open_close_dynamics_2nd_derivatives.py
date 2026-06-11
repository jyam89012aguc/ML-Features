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



def ocd_151_ocd_001_gap_down_frequency_5_001_roc_1(ocd_001_gap_down_frequency_5_001):
    feature = _s(ocd_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def ocd_152_ocd_007_gap_down_frequency_126_007_roc_5(ocd_007_gap_down_frequency_126_007):
    feature = _s(ocd_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42(ocd_013_gap_down_frequency_1008_013):
    feature = _s(ocd_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def ocd_154_ocd_019_gap_down_frequency_42_019_roc_126(ocd_019_gap_down_frequency_42_019):
    feature = _s(ocd_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def ocd_155_ocd_025_gap_down_frequency_378_025_roc_378(ocd_025_gap_down_frequency_378_025):
    feature = _s(ocd_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















OPEN_CLOSE_DYNAMICS_REGISTRY_2ND_DERIVATIVES = {
    'ocd_151_ocd_001_gap_down_frequency_5_001_roc_1': {'inputs': ['ocd_001_gap_down_frequency_5_001'], 'func': ocd_151_ocd_001_gap_down_frequency_5_001_roc_1},
    'ocd_152_ocd_007_gap_down_frequency_126_007_roc_5': {'inputs': ['ocd_007_gap_down_frequency_126_007'], 'func': ocd_152_ocd_007_gap_down_frequency_126_007_roc_5},
    'ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['ocd_013_gap_down_frequency_1008_013'], 'func': ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42},
    'ocd_154_ocd_019_gap_down_frequency_42_019_roc_126': {'inputs': ['ocd_019_gap_down_frequency_42_019'], 'func': ocd_154_ocd_019_gap_down_frequency_42_019_roc_126},
    'ocd_155_ocd_025_gap_down_frequency_378_025_roc_378': {'inputs': ['ocd_025_gap_down_frequency_378_025'], 'func': ocd_155_ocd_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ocd_replacement_d2_001(ocd_replacement_001):
    feature = _clean(ocd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_001'] = {'inputs': ['ocd_replacement_001'], 'func': ocd_replacement_d2_001}


def ocd_replacement_d2_002(ocd_replacement_002):
    feature = _clean(ocd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_002'] = {'inputs': ['ocd_replacement_002'], 'func': ocd_replacement_d2_002}


def ocd_replacement_d2_003(ocd_replacement_003):
    feature = _clean(ocd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_003'] = {'inputs': ['ocd_replacement_003'], 'func': ocd_replacement_d2_003}


def ocd_replacement_d2_004(ocd_replacement_004):
    feature = _clean(ocd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_004'] = {'inputs': ['ocd_replacement_004'], 'func': ocd_replacement_d2_004}


def ocd_replacement_d2_005(ocd_replacement_005):
    feature = _clean(ocd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_005'] = {'inputs': ['ocd_replacement_005'], 'func': ocd_replacement_d2_005}


def ocd_replacement_d2_006(ocd_replacement_006):
    feature = _clean(ocd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_006'] = {'inputs': ['ocd_replacement_006'], 'func': ocd_replacement_d2_006}


def ocd_replacement_d2_007(ocd_replacement_007):
    feature = _clean(ocd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_007'] = {'inputs': ['ocd_replacement_007'], 'func': ocd_replacement_d2_007}


def ocd_replacement_d2_008(ocd_replacement_008):
    feature = _clean(ocd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_008'] = {'inputs': ['ocd_replacement_008'], 'func': ocd_replacement_d2_008}


def ocd_replacement_d2_009(ocd_replacement_009):
    feature = _clean(ocd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_009'] = {'inputs': ['ocd_replacement_009'], 'func': ocd_replacement_d2_009}


def ocd_replacement_d2_010(ocd_replacement_010):
    feature = _clean(ocd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_010'] = {'inputs': ['ocd_replacement_010'], 'func': ocd_replacement_d2_010}


def ocd_replacement_d2_011(ocd_replacement_011):
    feature = _clean(ocd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_011'] = {'inputs': ['ocd_replacement_011'], 'func': ocd_replacement_d2_011}


def ocd_replacement_d2_012(ocd_replacement_012):
    feature = _clean(ocd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_012'] = {'inputs': ['ocd_replacement_012'], 'func': ocd_replacement_d2_012}


def ocd_replacement_d2_013(ocd_replacement_013):
    feature = _clean(ocd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_013'] = {'inputs': ['ocd_replacement_013'], 'func': ocd_replacement_d2_013}


def ocd_replacement_d2_014(ocd_replacement_014):
    feature = _clean(ocd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_014'] = {'inputs': ['ocd_replacement_014'], 'func': ocd_replacement_d2_014}


def ocd_replacement_d2_015(ocd_replacement_015):
    feature = _clean(ocd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_015'] = {'inputs': ['ocd_replacement_015'], 'func': ocd_replacement_d2_015}


def ocd_replacement_d2_016(ocd_replacement_016):
    feature = _clean(ocd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_016'] = {'inputs': ['ocd_replacement_016'], 'func': ocd_replacement_d2_016}


def ocd_replacement_d2_017(ocd_replacement_017):
    feature = _clean(ocd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_017'] = {'inputs': ['ocd_replacement_017'], 'func': ocd_replacement_d2_017}


def ocd_replacement_d2_018(ocd_replacement_018):
    feature = _clean(ocd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_018'] = {'inputs': ['ocd_replacement_018'], 'func': ocd_replacement_d2_018}


def ocd_replacement_d2_019(ocd_replacement_019):
    feature = _clean(ocd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_019'] = {'inputs': ['ocd_replacement_019'], 'func': ocd_replacement_d2_019}


def ocd_replacement_d2_020(ocd_replacement_020):
    feature = _clean(ocd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_020'] = {'inputs': ['ocd_replacement_020'], 'func': ocd_replacement_d2_020}


def ocd_replacement_d2_021(ocd_replacement_021):
    feature = _clean(ocd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_021'] = {'inputs': ['ocd_replacement_021'], 'func': ocd_replacement_d2_021}


def ocd_replacement_d2_022(ocd_replacement_022):
    feature = _clean(ocd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_022'] = {'inputs': ['ocd_replacement_022'], 'func': ocd_replacement_d2_022}


def ocd_replacement_d2_023(ocd_replacement_023):
    feature = _clean(ocd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_023'] = {'inputs': ['ocd_replacement_023'], 'func': ocd_replacement_d2_023}


def ocd_replacement_d2_024(ocd_replacement_024):
    feature = _clean(ocd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_024'] = {'inputs': ['ocd_replacement_024'], 'func': ocd_replacement_d2_024}


def ocd_replacement_d2_025(ocd_replacement_025):
    feature = _clean(ocd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_025'] = {'inputs': ['ocd_replacement_025'], 'func': ocd_replacement_d2_025}


def ocd_replacement_d2_026(ocd_replacement_026):
    feature = _clean(ocd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_026'] = {'inputs': ['ocd_replacement_026'], 'func': ocd_replacement_d2_026}


def ocd_replacement_d2_027(ocd_replacement_027):
    feature = _clean(ocd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_027'] = {'inputs': ['ocd_replacement_027'], 'func': ocd_replacement_d2_027}


def ocd_replacement_d2_028(ocd_replacement_028):
    feature = _clean(ocd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_028'] = {'inputs': ['ocd_replacement_028'], 'func': ocd_replacement_d2_028}


def ocd_replacement_d2_029(ocd_replacement_029):
    feature = _clean(ocd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_029'] = {'inputs': ['ocd_replacement_029'], 'func': ocd_replacement_d2_029}


def ocd_replacement_d2_030(ocd_replacement_030):
    feature = _clean(ocd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_030'] = {'inputs': ['ocd_replacement_030'], 'func': ocd_replacement_d2_030}


def ocd_replacement_d2_031(ocd_replacement_031):
    feature = _clean(ocd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_031'] = {'inputs': ['ocd_replacement_031'], 'func': ocd_replacement_d2_031}


def ocd_replacement_d2_032(ocd_replacement_032):
    feature = _clean(ocd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_032'] = {'inputs': ['ocd_replacement_032'], 'func': ocd_replacement_d2_032}


def ocd_replacement_d2_033(ocd_replacement_033):
    feature = _clean(ocd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_033'] = {'inputs': ['ocd_replacement_033'], 'func': ocd_replacement_d2_033}


def ocd_replacement_d2_034(ocd_replacement_034):
    feature = _clean(ocd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_034'] = {'inputs': ['ocd_replacement_034'], 'func': ocd_replacement_d2_034}


def ocd_replacement_d2_035(ocd_replacement_035):
    feature = _clean(ocd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_035'] = {'inputs': ['ocd_replacement_035'], 'func': ocd_replacement_d2_035}


def ocd_replacement_d2_036(ocd_replacement_036):
    feature = _clean(ocd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_036'] = {'inputs': ['ocd_replacement_036'], 'func': ocd_replacement_d2_036}


def ocd_replacement_d2_037(ocd_replacement_037):
    feature = _clean(ocd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_037'] = {'inputs': ['ocd_replacement_037'], 'func': ocd_replacement_d2_037}


def ocd_replacement_d2_038(ocd_replacement_038):
    feature = _clean(ocd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_038'] = {'inputs': ['ocd_replacement_038'], 'func': ocd_replacement_d2_038}


def ocd_replacement_d2_039(ocd_replacement_039):
    feature = _clean(ocd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_039'] = {'inputs': ['ocd_replacement_039'], 'func': ocd_replacement_d2_039}


def ocd_replacement_d2_040(ocd_replacement_040):
    feature = _clean(ocd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_040'] = {'inputs': ['ocd_replacement_040'], 'func': ocd_replacement_d2_040}


def ocd_replacement_d2_041(ocd_replacement_041):
    feature = _clean(ocd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_041'] = {'inputs': ['ocd_replacement_041'], 'func': ocd_replacement_d2_041}


def ocd_replacement_d2_042(ocd_replacement_042):
    feature = _clean(ocd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_042'] = {'inputs': ['ocd_replacement_042'], 'func': ocd_replacement_d2_042}


def ocd_replacement_d2_043(ocd_replacement_043):
    feature = _clean(ocd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_043'] = {'inputs': ['ocd_replacement_043'], 'func': ocd_replacement_d2_043}


def ocd_replacement_d2_044(ocd_replacement_044):
    feature = _clean(ocd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_044'] = {'inputs': ['ocd_replacement_044'], 'func': ocd_replacement_d2_044}


def ocd_replacement_d2_045(ocd_replacement_045):
    feature = _clean(ocd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_045'] = {'inputs': ['ocd_replacement_045'], 'func': ocd_replacement_d2_045}


def ocd_replacement_d2_046(ocd_replacement_046):
    feature = _clean(ocd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_046'] = {'inputs': ['ocd_replacement_046'], 'func': ocd_replacement_d2_046}


def ocd_replacement_d2_047(ocd_replacement_047):
    feature = _clean(ocd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_047'] = {'inputs': ['ocd_replacement_047'], 'func': ocd_replacement_d2_047}


def ocd_replacement_d2_048(ocd_replacement_048):
    feature = _clean(ocd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_048'] = {'inputs': ['ocd_replacement_048'], 'func': ocd_replacement_d2_048}


def ocd_replacement_d2_049(ocd_replacement_049):
    feature = _clean(ocd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_049'] = {'inputs': ['ocd_replacement_049'], 'func': ocd_replacement_d2_049}


def ocd_replacement_d2_050(ocd_replacement_050):
    feature = _clean(ocd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_050'] = {'inputs': ['ocd_replacement_050'], 'func': ocd_replacement_d2_050}


def ocd_replacement_d2_051(ocd_replacement_051):
    feature = _clean(ocd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_051'] = {'inputs': ['ocd_replacement_051'], 'func': ocd_replacement_d2_051}


def ocd_replacement_d2_052(ocd_replacement_052):
    feature = _clean(ocd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_052'] = {'inputs': ['ocd_replacement_052'], 'func': ocd_replacement_d2_052}


def ocd_replacement_d2_053(ocd_replacement_053):
    feature = _clean(ocd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_053'] = {'inputs': ['ocd_replacement_053'], 'func': ocd_replacement_d2_053}


def ocd_replacement_d2_054(ocd_replacement_054):
    feature = _clean(ocd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_054'] = {'inputs': ['ocd_replacement_054'], 'func': ocd_replacement_d2_054}


def ocd_replacement_d2_055(ocd_replacement_055):
    feature = _clean(ocd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_055'] = {'inputs': ['ocd_replacement_055'], 'func': ocd_replacement_d2_055}


def ocd_replacement_d2_056(ocd_replacement_056):
    feature = _clean(ocd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_056'] = {'inputs': ['ocd_replacement_056'], 'func': ocd_replacement_d2_056}


def ocd_replacement_d2_057(ocd_replacement_057):
    feature = _clean(ocd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_057'] = {'inputs': ['ocd_replacement_057'], 'func': ocd_replacement_d2_057}


def ocd_replacement_d2_058(ocd_replacement_058):
    feature = _clean(ocd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_058'] = {'inputs': ['ocd_replacement_058'], 'func': ocd_replacement_d2_058}


def ocd_replacement_d2_059(ocd_replacement_059):
    feature = _clean(ocd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_059'] = {'inputs': ['ocd_replacement_059'], 'func': ocd_replacement_d2_059}


def ocd_replacement_d2_060(ocd_replacement_060):
    feature = _clean(ocd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_060'] = {'inputs': ['ocd_replacement_060'], 'func': ocd_replacement_d2_060}


def ocd_replacement_d2_061(ocd_replacement_061):
    feature = _clean(ocd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_061'] = {'inputs': ['ocd_replacement_061'], 'func': ocd_replacement_d2_061}


def ocd_replacement_d2_062(ocd_replacement_062):
    feature = _clean(ocd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_062'] = {'inputs': ['ocd_replacement_062'], 'func': ocd_replacement_d2_062}


def ocd_replacement_d2_063(ocd_replacement_063):
    feature = _clean(ocd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_063'] = {'inputs': ['ocd_replacement_063'], 'func': ocd_replacement_d2_063}


def ocd_replacement_d2_064(ocd_replacement_064):
    feature = _clean(ocd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_064'] = {'inputs': ['ocd_replacement_064'], 'func': ocd_replacement_d2_064}


def ocd_replacement_d2_065(ocd_replacement_065):
    feature = _clean(ocd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_065'] = {'inputs': ['ocd_replacement_065'], 'func': ocd_replacement_d2_065}


def ocd_replacement_d2_066(ocd_replacement_066):
    feature = _clean(ocd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_066'] = {'inputs': ['ocd_replacement_066'], 'func': ocd_replacement_d2_066}


def ocd_replacement_d2_067(ocd_replacement_067):
    feature = _clean(ocd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_067'] = {'inputs': ['ocd_replacement_067'], 'func': ocd_replacement_d2_067}


def ocd_replacement_d2_068(ocd_replacement_068):
    feature = _clean(ocd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_068'] = {'inputs': ['ocd_replacement_068'], 'func': ocd_replacement_d2_068}


def ocd_replacement_d2_069(ocd_replacement_069):
    feature = _clean(ocd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_069'] = {'inputs': ['ocd_replacement_069'], 'func': ocd_replacement_d2_069}


def ocd_replacement_d2_070(ocd_replacement_070):
    feature = _clean(ocd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_070'] = {'inputs': ['ocd_replacement_070'], 'func': ocd_replacement_d2_070}


def ocd_replacement_d2_071(ocd_replacement_071):
    feature = _clean(ocd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_071'] = {'inputs': ['ocd_replacement_071'], 'func': ocd_replacement_d2_071}


def ocd_replacement_d2_072(ocd_replacement_072):
    feature = _clean(ocd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_072'] = {'inputs': ['ocd_replacement_072'], 'func': ocd_replacement_d2_072}


def ocd_replacement_d2_073(ocd_replacement_073):
    feature = _clean(ocd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_073'] = {'inputs': ['ocd_replacement_073'], 'func': ocd_replacement_d2_073}


def ocd_replacement_d2_074(ocd_replacement_074):
    feature = _clean(ocd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_074'] = {'inputs': ['ocd_replacement_074'], 'func': ocd_replacement_d2_074}


def ocd_replacement_d2_075(ocd_replacement_075):
    feature = _clean(ocd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_075'] = {'inputs': ['ocd_replacement_075'], 'func': ocd_replacement_d2_075}


def ocd_replacement_d2_076(ocd_replacement_076):
    feature = _clean(ocd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_076'] = {'inputs': ['ocd_replacement_076'], 'func': ocd_replacement_d2_076}


def ocd_replacement_d2_077(ocd_replacement_077):
    feature = _clean(ocd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_077'] = {'inputs': ['ocd_replacement_077'], 'func': ocd_replacement_d2_077}


def ocd_replacement_d2_078(ocd_replacement_078):
    feature = _clean(ocd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_078'] = {'inputs': ['ocd_replacement_078'], 'func': ocd_replacement_d2_078}


def ocd_replacement_d2_079(ocd_replacement_079):
    feature = _clean(ocd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_079'] = {'inputs': ['ocd_replacement_079'], 'func': ocd_replacement_d2_079}


def ocd_replacement_d2_080(ocd_replacement_080):
    feature = _clean(ocd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_080'] = {'inputs': ['ocd_replacement_080'], 'func': ocd_replacement_d2_080}


def ocd_replacement_d2_081(ocd_replacement_081):
    feature = _clean(ocd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_081'] = {'inputs': ['ocd_replacement_081'], 'func': ocd_replacement_d2_081}


def ocd_replacement_d2_082(ocd_replacement_082):
    feature = _clean(ocd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_082'] = {'inputs': ['ocd_replacement_082'], 'func': ocd_replacement_d2_082}


def ocd_replacement_d2_083(ocd_replacement_083):
    feature = _clean(ocd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_083'] = {'inputs': ['ocd_replacement_083'], 'func': ocd_replacement_d2_083}


def ocd_replacement_d2_084(ocd_replacement_084):
    feature = _clean(ocd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_084'] = {'inputs': ['ocd_replacement_084'], 'func': ocd_replacement_d2_084}


def ocd_replacement_d2_085(ocd_replacement_085):
    feature = _clean(ocd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_085'] = {'inputs': ['ocd_replacement_085'], 'func': ocd_replacement_d2_085}


def ocd_replacement_d2_086(ocd_replacement_086):
    feature = _clean(ocd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_086'] = {'inputs': ['ocd_replacement_086'], 'func': ocd_replacement_d2_086}


def ocd_replacement_d2_087(ocd_replacement_087):
    feature = _clean(ocd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_087'] = {'inputs': ['ocd_replacement_087'], 'func': ocd_replacement_d2_087}


def ocd_replacement_d2_088(ocd_replacement_088):
    feature = _clean(ocd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_088'] = {'inputs': ['ocd_replacement_088'], 'func': ocd_replacement_d2_088}


def ocd_replacement_d2_089(ocd_replacement_089):
    feature = _clean(ocd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_089'] = {'inputs': ['ocd_replacement_089'], 'func': ocd_replacement_d2_089}


def ocd_replacement_d2_090(ocd_replacement_090):
    feature = _clean(ocd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_090'] = {'inputs': ['ocd_replacement_090'], 'func': ocd_replacement_d2_090}


def ocd_replacement_d2_091(ocd_replacement_091):
    feature = _clean(ocd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_091'] = {'inputs': ['ocd_replacement_091'], 'func': ocd_replacement_d2_091}


def ocd_replacement_d2_092(ocd_replacement_092):
    feature = _clean(ocd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_092'] = {'inputs': ['ocd_replacement_092'], 'func': ocd_replacement_d2_092}


def ocd_replacement_d2_093(ocd_replacement_093):
    feature = _clean(ocd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_093'] = {'inputs': ['ocd_replacement_093'], 'func': ocd_replacement_d2_093}


def ocd_replacement_d2_094(ocd_replacement_094):
    feature = _clean(ocd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_094'] = {'inputs': ['ocd_replacement_094'], 'func': ocd_replacement_d2_094}


def ocd_replacement_d2_095(ocd_replacement_095):
    feature = _clean(ocd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_095'] = {'inputs': ['ocd_replacement_095'], 'func': ocd_replacement_d2_095}


def ocd_replacement_d2_096(ocd_replacement_096):
    feature = _clean(ocd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_096'] = {'inputs': ['ocd_replacement_096'], 'func': ocd_replacement_d2_096}


def ocd_replacement_d2_097(ocd_replacement_097):
    feature = _clean(ocd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_097'] = {'inputs': ['ocd_replacement_097'], 'func': ocd_replacement_d2_097}


def ocd_replacement_d2_098(ocd_replacement_098):
    feature = _clean(ocd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_098'] = {'inputs': ['ocd_replacement_098'], 'func': ocd_replacement_d2_098}


def ocd_replacement_d2_099(ocd_replacement_099):
    feature = _clean(ocd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_099'] = {'inputs': ['ocd_replacement_099'], 'func': ocd_replacement_d2_099}


def ocd_replacement_d2_100(ocd_replacement_100):
    feature = _clean(ocd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_100'] = {'inputs': ['ocd_replacement_100'], 'func': ocd_replacement_d2_100}


def ocd_replacement_d2_101(ocd_replacement_101):
    feature = _clean(ocd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_101'] = {'inputs': ['ocd_replacement_101'], 'func': ocd_replacement_d2_101}


def ocd_replacement_d2_102(ocd_replacement_102):
    feature = _clean(ocd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_102'] = {'inputs': ['ocd_replacement_102'], 'func': ocd_replacement_d2_102}


def ocd_replacement_d2_103(ocd_replacement_103):
    feature = _clean(ocd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_103'] = {'inputs': ['ocd_replacement_103'], 'func': ocd_replacement_d2_103}


def ocd_replacement_d2_104(ocd_replacement_104):
    feature = _clean(ocd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_104'] = {'inputs': ['ocd_replacement_104'], 'func': ocd_replacement_d2_104}


def ocd_replacement_d2_105(ocd_replacement_105):
    feature = _clean(ocd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_105'] = {'inputs': ['ocd_replacement_105'], 'func': ocd_replacement_d2_105}


def ocd_replacement_d2_106(ocd_replacement_106):
    feature = _clean(ocd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_106'] = {'inputs': ['ocd_replacement_106'], 'func': ocd_replacement_d2_106}


def ocd_replacement_d2_107(ocd_replacement_107):
    feature = _clean(ocd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_107'] = {'inputs': ['ocd_replacement_107'], 'func': ocd_replacement_d2_107}


def ocd_replacement_d2_108(ocd_replacement_108):
    feature = _clean(ocd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_108'] = {'inputs': ['ocd_replacement_108'], 'func': ocd_replacement_d2_108}


def ocd_replacement_d2_109(ocd_replacement_109):
    feature = _clean(ocd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_109'] = {'inputs': ['ocd_replacement_109'], 'func': ocd_replacement_d2_109}


def ocd_replacement_d2_110(ocd_replacement_110):
    feature = _clean(ocd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_110'] = {'inputs': ['ocd_replacement_110'], 'func': ocd_replacement_d2_110}


def ocd_replacement_d2_111(ocd_replacement_111):
    feature = _clean(ocd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_111'] = {'inputs': ['ocd_replacement_111'], 'func': ocd_replacement_d2_111}


def ocd_replacement_d2_112(ocd_replacement_112):
    feature = _clean(ocd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_112'] = {'inputs': ['ocd_replacement_112'], 'func': ocd_replacement_d2_112}


def ocd_replacement_d2_113(ocd_replacement_113):
    feature = _clean(ocd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_113'] = {'inputs': ['ocd_replacement_113'], 'func': ocd_replacement_d2_113}


def ocd_replacement_d2_114(ocd_replacement_114):
    feature = _clean(ocd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_114'] = {'inputs': ['ocd_replacement_114'], 'func': ocd_replacement_d2_114}


def ocd_replacement_d2_115(ocd_replacement_115):
    feature = _clean(ocd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_115'] = {'inputs': ['ocd_replacement_115'], 'func': ocd_replacement_d2_115}


def ocd_replacement_d2_116(ocd_replacement_116):
    feature = _clean(ocd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_116'] = {'inputs': ['ocd_replacement_116'], 'func': ocd_replacement_d2_116}


def ocd_replacement_d2_117(ocd_replacement_117):
    feature = _clean(ocd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_117'] = {'inputs': ['ocd_replacement_117'], 'func': ocd_replacement_d2_117}


def ocd_replacement_d2_118(ocd_replacement_118):
    feature = _clean(ocd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_118'] = {'inputs': ['ocd_replacement_118'], 'func': ocd_replacement_d2_118}


def ocd_replacement_d2_119(ocd_replacement_119):
    feature = _clean(ocd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_119'] = {'inputs': ['ocd_replacement_119'], 'func': ocd_replacement_d2_119}


def ocd_replacement_d2_120(ocd_replacement_120):
    feature = _clean(ocd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_120'] = {'inputs': ['ocd_replacement_120'], 'func': ocd_replacement_d2_120}


def ocd_replacement_d2_121(ocd_replacement_121):
    feature = _clean(ocd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_121'] = {'inputs': ['ocd_replacement_121'], 'func': ocd_replacement_d2_121}


def ocd_replacement_d2_122(ocd_replacement_122):
    feature = _clean(ocd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_122'] = {'inputs': ['ocd_replacement_122'], 'func': ocd_replacement_d2_122}


def ocd_replacement_d2_123(ocd_replacement_123):
    feature = _clean(ocd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_123'] = {'inputs': ['ocd_replacement_123'], 'func': ocd_replacement_d2_123}


def ocd_replacement_d2_124(ocd_replacement_124):
    feature = _clean(ocd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_124'] = {'inputs': ['ocd_replacement_124'], 'func': ocd_replacement_d2_124}


def ocd_replacement_d2_125(ocd_replacement_125):
    feature = _clean(ocd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_125'] = {'inputs': ['ocd_replacement_125'], 'func': ocd_replacement_d2_125}


def ocd_replacement_d2_126(ocd_replacement_126):
    feature = _clean(ocd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_126'] = {'inputs': ['ocd_replacement_126'], 'func': ocd_replacement_d2_126}


def ocd_replacement_d2_127(ocd_replacement_127):
    feature = _clean(ocd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_127'] = {'inputs': ['ocd_replacement_127'], 'func': ocd_replacement_d2_127}


def ocd_replacement_d2_128(ocd_replacement_128):
    feature = _clean(ocd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_128'] = {'inputs': ['ocd_replacement_128'], 'func': ocd_replacement_d2_128}


def ocd_replacement_d2_129(ocd_replacement_129):
    feature = _clean(ocd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_129'] = {'inputs': ['ocd_replacement_129'], 'func': ocd_replacement_d2_129}


def ocd_replacement_d2_130(ocd_replacement_130):
    feature = _clean(ocd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_130'] = {'inputs': ['ocd_replacement_130'], 'func': ocd_replacement_d2_130}


def ocd_replacement_d2_131(ocd_replacement_131):
    feature = _clean(ocd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_131'] = {'inputs': ['ocd_replacement_131'], 'func': ocd_replacement_d2_131}


def ocd_replacement_d2_132(ocd_replacement_132):
    feature = _clean(ocd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_132'] = {'inputs': ['ocd_replacement_132'], 'func': ocd_replacement_d2_132}


def ocd_replacement_d2_133(ocd_replacement_133):
    feature = _clean(ocd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_133'] = {'inputs': ['ocd_replacement_133'], 'func': ocd_replacement_d2_133}


def ocd_replacement_d2_134(ocd_replacement_134):
    feature = _clean(ocd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_134'] = {'inputs': ['ocd_replacement_134'], 'func': ocd_replacement_d2_134}


def ocd_replacement_d2_135(ocd_replacement_135):
    feature = _clean(ocd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_135'] = {'inputs': ['ocd_replacement_135'], 'func': ocd_replacement_d2_135}


def ocd_replacement_d2_136(ocd_replacement_136):
    feature = _clean(ocd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_136'] = {'inputs': ['ocd_replacement_136'], 'func': ocd_replacement_d2_136}


def ocd_replacement_d2_137(ocd_replacement_137):
    feature = _clean(ocd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_137'] = {'inputs': ['ocd_replacement_137'], 'func': ocd_replacement_d2_137}


def ocd_replacement_d2_138(ocd_replacement_138):
    feature = _clean(ocd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_138'] = {'inputs': ['ocd_replacement_138'], 'func': ocd_replacement_d2_138}


def ocd_replacement_d2_139(ocd_replacement_139):
    feature = _clean(ocd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_139'] = {'inputs': ['ocd_replacement_139'], 'func': ocd_replacement_d2_139}


def ocd_replacement_d2_140(ocd_replacement_140):
    feature = _clean(ocd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_140'] = {'inputs': ['ocd_replacement_140'], 'func': ocd_replacement_d2_140}


def ocd_replacement_d2_141(ocd_replacement_141):
    feature = _clean(ocd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_141'] = {'inputs': ['ocd_replacement_141'], 'func': ocd_replacement_d2_141}


def ocd_replacement_d2_142(ocd_replacement_142):
    feature = _clean(ocd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_142'] = {'inputs': ['ocd_replacement_142'], 'func': ocd_replacement_d2_142}


def ocd_replacement_d2_143(ocd_replacement_143):
    feature = _clean(ocd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_143'] = {'inputs': ['ocd_replacement_143'], 'func': ocd_replacement_d2_143}


def ocd_replacement_d2_144(ocd_replacement_144):
    feature = _clean(ocd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_144'] = {'inputs': ['ocd_replacement_144'], 'func': ocd_replacement_d2_144}


def ocd_replacement_d2_145(ocd_replacement_145):
    feature = _clean(ocd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_145'] = {'inputs': ['ocd_replacement_145'], 'func': ocd_replacement_d2_145}


def ocd_replacement_d2_146(ocd_replacement_146):
    feature = _clean(ocd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_146'] = {'inputs': ['ocd_replacement_146'], 'func': ocd_replacement_d2_146}


def ocd_replacement_d2_147(ocd_replacement_147):
    feature = _clean(ocd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_147'] = {'inputs': ['ocd_replacement_147'], 'func': ocd_replacement_d2_147}


def ocd_replacement_d2_148(ocd_replacement_148):
    feature = _clean(ocd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_148'] = {'inputs': ['ocd_replacement_148'], 'func': ocd_replacement_d2_148}


def ocd_replacement_d2_149(ocd_replacement_149):
    feature = _clean(ocd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_149'] = {'inputs': ['ocd_replacement_149'], 'func': ocd_replacement_d2_149}


def ocd_replacement_d2_150(ocd_replacement_150):
    feature = _clean(ocd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_150'] = {'inputs': ['ocd_replacement_150'], 'func': ocd_replacement_d2_150}


def ocd_replacement_d2_151(ocd_replacement_151):
    feature = _clean(ocd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_151'] = {'inputs': ['ocd_replacement_151'], 'func': ocd_replacement_d2_151}


def ocd_replacement_d2_152(ocd_replacement_152):
    feature = _clean(ocd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_152'] = {'inputs': ['ocd_replacement_152'], 'func': ocd_replacement_d2_152}


def ocd_replacement_d2_153(ocd_replacement_153):
    feature = _clean(ocd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_153'] = {'inputs': ['ocd_replacement_153'], 'func': ocd_replacement_d2_153}


def ocd_replacement_d2_154(ocd_replacement_154):
    feature = _clean(ocd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_154'] = {'inputs': ['ocd_replacement_154'], 'func': ocd_replacement_d2_154}


def ocd_replacement_d2_155(ocd_replacement_155):
    feature = _clean(ocd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_155'] = {'inputs': ['ocd_replacement_155'], 'func': ocd_replacement_d2_155}


def ocd_replacement_d2_156(ocd_replacement_156):
    feature = _clean(ocd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_156'] = {'inputs': ['ocd_replacement_156'], 'func': ocd_replacement_d2_156}


def ocd_replacement_d2_157(ocd_replacement_157):
    feature = _clean(ocd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_157'] = {'inputs': ['ocd_replacement_157'], 'func': ocd_replacement_d2_157}


def ocd_replacement_d2_158(ocd_replacement_158):
    feature = _clean(ocd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_158'] = {'inputs': ['ocd_replacement_158'], 'func': ocd_replacement_d2_158}


def ocd_replacement_d2_159(ocd_replacement_159):
    feature = _clean(ocd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_159'] = {'inputs': ['ocd_replacement_159'], 'func': ocd_replacement_d2_159}


def ocd_replacement_d2_160(ocd_replacement_160):
    feature = _clean(ocd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
OCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ocd_replacement_d2_160'] = {'inputs': ['ocd_replacement_160'], 'func': ocd_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002(ocd_002_gap_magnitude_10_002):
    return _base_universe_d2(ocd_002_gap_magnitude_10_002, 1)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002'] = {'inputs': ['ocd_002_gap_magnitude_10_002'], 'func': ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002}


def ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003(ocd_003_open_close_pressure_21_003):
    return _base_universe_d2(ocd_003_open_close_pressure_21_003, 2)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003'] = {'inputs': ['ocd_003_open_close_pressure_21_003'], 'func': ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003}


def ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004(ocd_004_lower_wick_ratio_42_004):
    return _base_universe_d2(ocd_004_lower_wick_ratio_42_004, 3)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004'] = {'inputs': ['ocd_004_lower_wick_ratio_42_004'], 'func': ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004}


def ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005(ocd_005_upper_wick_ratio_63_005):
    return _base_universe_d2(ocd_005_upper_wick_ratio_63_005, 4)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005'] = {'inputs': ['ocd_005_upper_wick_ratio_63_005'], 'func': ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005}


def ocd_base_universe_d2_005_ocd_006_body_to_range_84_006(ocd_006_body_to_range_84_006):
    return _base_universe_d2(ocd_006_body_to_range_84_006, 5)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_005_ocd_006_body_to_range_84_006'] = {'inputs': ['ocd_006_body_to_range_84_006'], 'func': ocd_base_universe_d2_005_ocd_006_body_to_range_84_006}


def ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008(ocd_008_gap_magnitude_189_008):
    return _base_universe_d2(ocd_008_gap_magnitude_189_008, 6)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008'] = {'inputs': ['ocd_008_gap_magnitude_189_008'], 'func': ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008}


def ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009(ocd_009_open_close_pressure_252_009):
    return _base_universe_d2(ocd_009_open_close_pressure_252_009, 7)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009'] = {'inputs': ['ocd_009_open_close_pressure_252_009'], 'func': ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009}


def ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010(ocd_010_lower_wick_ratio_378_010):
    return _base_universe_d2(ocd_010_lower_wick_ratio_378_010, 8)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010'] = {'inputs': ['ocd_010_lower_wick_ratio_378_010'], 'func': ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010}


def ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011(ocd_011_upper_wick_ratio_504_011):
    return _base_universe_d2(ocd_011_upper_wick_ratio_504_011, 9)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011'] = {'inputs': ['ocd_011_upper_wick_ratio_504_011'], 'func': ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011}


def ocd_base_universe_d2_010_ocd_012_body_to_range_756_012(ocd_012_body_to_range_756_012):
    return _base_universe_d2(ocd_012_body_to_range_756_012, 10)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_010_ocd_012_body_to_range_756_012'] = {'inputs': ['ocd_012_body_to_range_756_012'], 'func': ocd_base_universe_d2_010_ocd_012_body_to_range_756_012}


def ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014(ocd_014_gap_magnitude_1260_014):
    return _base_universe_d2(ocd_014_gap_magnitude_1260_014, 11)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014'] = {'inputs': ['ocd_014_gap_magnitude_1260_014'], 'func': ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014}


def ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015(ocd_015_open_close_pressure_1512_015):
    return _base_universe_d2(ocd_015_open_close_pressure_1512_015, 12)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015'] = {'inputs': ['ocd_015_open_close_pressure_1512_015'], 'func': ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015}


def ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016(ocd_016_lower_wick_ratio_5_016):
    return _base_universe_d2(ocd_016_lower_wick_ratio_5_016, 13)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016'] = {'inputs': ['ocd_016_lower_wick_ratio_5_016'], 'func': ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016}


def ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017(ocd_017_upper_wick_ratio_10_017):
    return _base_universe_d2(ocd_017_upper_wick_ratio_10_017, 14)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017'] = {'inputs': ['ocd_017_upper_wick_ratio_10_017'], 'func': ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017}


def ocd_base_universe_d2_015_ocd_018_body_to_range_21_018(ocd_018_body_to_range_21_018):
    return _base_universe_d2(ocd_018_body_to_range_21_018, 15)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_015_ocd_018_body_to_range_21_018'] = {'inputs': ['ocd_018_body_to_range_21_018'], 'func': ocd_base_universe_d2_015_ocd_018_body_to_range_21_018}


def ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020(ocd_020_gap_magnitude_63_020):
    return _base_universe_d2(ocd_020_gap_magnitude_63_020, 16)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020'] = {'inputs': ['ocd_020_gap_magnitude_63_020'], 'func': ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020}


def ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021(ocd_021_open_close_pressure_84_021):
    return _base_universe_d2(ocd_021_open_close_pressure_84_021, 17)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021'] = {'inputs': ['ocd_021_open_close_pressure_84_021'], 'func': ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021}


def ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022(ocd_022_lower_wick_ratio_126_022):
    return _base_universe_d2(ocd_022_lower_wick_ratio_126_022, 18)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022'] = {'inputs': ['ocd_022_lower_wick_ratio_126_022'], 'func': ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022}


def ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023(ocd_023_upper_wick_ratio_189_023):
    return _base_universe_d2(ocd_023_upper_wick_ratio_189_023, 19)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023'] = {'inputs': ['ocd_023_upper_wick_ratio_189_023'], 'func': ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023}


def ocd_base_universe_d2_020_ocd_024_body_to_range_252_024(ocd_024_body_to_range_252_024):
    return _base_universe_d2(ocd_024_body_to_range_252_024, 20)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_020_ocd_024_body_to_range_252_024'] = {'inputs': ['ocd_024_body_to_range_252_024'], 'func': ocd_base_universe_d2_020_ocd_024_body_to_range_252_024}


def ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026(ocd_026_gap_magnitude_504_026):
    return _base_universe_d2(ocd_026_gap_magnitude_504_026, 21)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026'] = {'inputs': ['ocd_026_gap_magnitude_504_026'], 'func': ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026}


def ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027(ocd_027_open_close_pressure_756_027):
    return _base_universe_d2(ocd_027_open_close_pressure_756_027, 22)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027'] = {'inputs': ['ocd_027_open_close_pressure_756_027'], 'func': ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027}


def ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028(ocd_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(ocd_028_lower_wick_ratio_1008_028, 23)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028'] = {'inputs': ['ocd_028_lower_wick_ratio_1008_028'], 'func': ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028}


def ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029(ocd_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(ocd_029_upper_wick_ratio_1260_029, 24)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029'] = {'inputs': ['ocd_029_upper_wick_ratio_1260_029'], 'func': ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029}


def ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030(ocd_030_body_to_range_1512_030):
    return _base_universe_d2(ocd_030_body_to_range_1512_030, 25)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030'] = {'inputs': ['ocd_030_body_to_range_1512_030'], 'func': ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030}


def ocd_base_universe_d2_026_ocd_basefill_031(ocd_basefill_031):
    return _base_universe_d2(ocd_basefill_031, 26)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_026_ocd_basefill_031'] = {'inputs': ['ocd_basefill_031'], 'func': ocd_base_universe_d2_026_ocd_basefill_031}


def ocd_base_universe_d2_027_ocd_basefill_032(ocd_basefill_032):
    return _base_universe_d2(ocd_basefill_032, 27)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_027_ocd_basefill_032'] = {'inputs': ['ocd_basefill_032'], 'func': ocd_base_universe_d2_027_ocd_basefill_032}


def ocd_base_universe_d2_028_ocd_basefill_033(ocd_basefill_033):
    return _base_universe_d2(ocd_basefill_033, 28)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_028_ocd_basefill_033'] = {'inputs': ['ocd_basefill_033'], 'func': ocd_base_universe_d2_028_ocd_basefill_033}


def ocd_base_universe_d2_029_ocd_basefill_034(ocd_basefill_034):
    return _base_universe_d2(ocd_basefill_034, 29)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_029_ocd_basefill_034'] = {'inputs': ['ocd_basefill_034'], 'func': ocd_base_universe_d2_029_ocd_basefill_034}


def ocd_base_universe_d2_030_ocd_basefill_035(ocd_basefill_035):
    return _base_universe_d2(ocd_basefill_035, 30)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_030_ocd_basefill_035'] = {'inputs': ['ocd_basefill_035'], 'func': ocd_base_universe_d2_030_ocd_basefill_035}


def ocd_base_universe_d2_031_ocd_basefill_036(ocd_basefill_036):
    return _base_universe_d2(ocd_basefill_036, 31)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_031_ocd_basefill_036'] = {'inputs': ['ocd_basefill_036'], 'func': ocd_base_universe_d2_031_ocd_basefill_036}


def ocd_base_universe_d2_032_ocd_basefill_037(ocd_basefill_037):
    return _base_universe_d2(ocd_basefill_037, 32)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_032_ocd_basefill_037'] = {'inputs': ['ocd_basefill_037'], 'func': ocd_base_universe_d2_032_ocd_basefill_037}


def ocd_base_universe_d2_033_ocd_basefill_038(ocd_basefill_038):
    return _base_universe_d2(ocd_basefill_038, 33)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_033_ocd_basefill_038'] = {'inputs': ['ocd_basefill_038'], 'func': ocd_base_universe_d2_033_ocd_basefill_038}


def ocd_base_universe_d2_034_ocd_basefill_039(ocd_basefill_039):
    return _base_universe_d2(ocd_basefill_039, 34)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_034_ocd_basefill_039'] = {'inputs': ['ocd_basefill_039'], 'func': ocd_base_universe_d2_034_ocd_basefill_039}


def ocd_base_universe_d2_035_ocd_basefill_040(ocd_basefill_040):
    return _base_universe_d2(ocd_basefill_040, 35)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_035_ocd_basefill_040'] = {'inputs': ['ocd_basefill_040'], 'func': ocd_base_universe_d2_035_ocd_basefill_040}


def ocd_base_universe_d2_036_ocd_basefill_041(ocd_basefill_041):
    return _base_universe_d2(ocd_basefill_041, 36)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_036_ocd_basefill_041'] = {'inputs': ['ocd_basefill_041'], 'func': ocd_base_universe_d2_036_ocd_basefill_041}


def ocd_base_universe_d2_037_ocd_basefill_042(ocd_basefill_042):
    return _base_universe_d2(ocd_basefill_042, 37)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_037_ocd_basefill_042'] = {'inputs': ['ocd_basefill_042'], 'func': ocd_base_universe_d2_037_ocd_basefill_042}


def ocd_base_universe_d2_038_ocd_basefill_043(ocd_basefill_043):
    return _base_universe_d2(ocd_basefill_043, 38)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_038_ocd_basefill_043'] = {'inputs': ['ocd_basefill_043'], 'func': ocd_base_universe_d2_038_ocd_basefill_043}


def ocd_base_universe_d2_039_ocd_basefill_044(ocd_basefill_044):
    return _base_universe_d2(ocd_basefill_044, 39)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_039_ocd_basefill_044'] = {'inputs': ['ocd_basefill_044'], 'func': ocd_base_universe_d2_039_ocd_basefill_044}


def ocd_base_universe_d2_040_ocd_basefill_045(ocd_basefill_045):
    return _base_universe_d2(ocd_basefill_045, 40)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_040_ocd_basefill_045'] = {'inputs': ['ocd_basefill_045'], 'func': ocd_base_universe_d2_040_ocd_basefill_045}


def ocd_base_universe_d2_041_ocd_basefill_046(ocd_basefill_046):
    return _base_universe_d2(ocd_basefill_046, 41)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_041_ocd_basefill_046'] = {'inputs': ['ocd_basefill_046'], 'func': ocd_base_universe_d2_041_ocd_basefill_046}


def ocd_base_universe_d2_042_ocd_basefill_047(ocd_basefill_047):
    return _base_universe_d2(ocd_basefill_047, 42)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_042_ocd_basefill_047'] = {'inputs': ['ocd_basefill_047'], 'func': ocd_base_universe_d2_042_ocd_basefill_047}


def ocd_base_universe_d2_043_ocd_basefill_048(ocd_basefill_048):
    return _base_universe_d2(ocd_basefill_048, 43)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_043_ocd_basefill_048'] = {'inputs': ['ocd_basefill_048'], 'func': ocd_base_universe_d2_043_ocd_basefill_048}


def ocd_base_universe_d2_044_ocd_basefill_049(ocd_basefill_049):
    return _base_universe_d2(ocd_basefill_049, 44)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_044_ocd_basefill_049'] = {'inputs': ['ocd_basefill_049'], 'func': ocd_base_universe_d2_044_ocd_basefill_049}


def ocd_base_universe_d2_045_ocd_basefill_050(ocd_basefill_050):
    return _base_universe_d2(ocd_basefill_050, 45)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_045_ocd_basefill_050'] = {'inputs': ['ocd_basefill_050'], 'func': ocd_base_universe_d2_045_ocd_basefill_050}


def ocd_base_universe_d2_046_ocd_basefill_051(ocd_basefill_051):
    return _base_universe_d2(ocd_basefill_051, 46)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_046_ocd_basefill_051'] = {'inputs': ['ocd_basefill_051'], 'func': ocd_base_universe_d2_046_ocd_basefill_051}


def ocd_base_universe_d2_047_ocd_basefill_052(ocd_basefill_052):
    return _base_universe_d2(ocd_basefill_052, 47)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_047_ocd_basefill_052'] = {'inputs': ['ocd_basefill_052'], 'func': ocd_base_universe_d2_047_ocd_basefill_052}


def ocd_base_universe_d2_048_ocd_basefill_053(ocd_basefill_053):
    return _base_universe_d2(ocd_basefill_053, 48)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_048_ocd_basefill_053'] = {'inputs': ['ocd_basefill_053'], 'func': ocd_base_universe_d2_048_ocd_basefill_053}


def ocd_base_universe_d2_049_ocd_basefill_054(ocd_basefill_054):
    return _base_universe_d2(ocd_basefill_054, 49)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_049_ocd_basefill_054'] = {'inputs': ['ocd_basefill_054'], 'func': ocd_base_universe_d2_049_ocd_basefill_054}


def ocd_base_universe_d2_050_ocd_basefill_055(ocd_basefill_055):
    return _base_universe_d2(ocd_basefill_055, 50)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_050_ocd_basefill_055'] = {'inputs': ['ocd_basefill_055'], 'func': ocd_base_universe_d2_050_ocd_basefill_055}


def ocd_base_universe_d2_051_ocd_basefill_056(ocd_basefill_056):
    return _base_universe_d2(ocd_basefill_056, 51)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_051_ocd_basefill_056'] = {'inputs': ['ocd_basefill_056'], 'func': ocd_base_universe_d2_051_ocd_basefill_056}


def ocd_base_universe_d2_052_ocd_basefill_057(ocd_basefill_057):
    return _base_universe_d2(ocd_basefill_057, 52)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_052_ocd_basefill_057'] = {'inputs': ['ocd_basefill_057'], 'func': ocd_base_universe_d2_052_ocd_basefill_057}


def ocd_base_universe_d2_053_ocd_basefill_058(ocd_basefill_058):
    return _base_universe_d2(ocd_basefill_058, 53)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_053_ocd_basefill_058'] = {'inputs': ['ocd_basefill_058'], 'func': ocd_base_universe_d2_053_ocd_basefill_058}


def ocd_base_universe_d2_054_ocd_basefill_059(ocd_basefill_059):
    return _base_universe_d2(ocd_basefill_059, 54)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_054_ocd_basefill_059'] = {'inputs': ['ocd_basefill_059'], 'func': ocd_base_universe_d2_054_ocd_basefill_059}


def ocd_base_universe_d2_055_ocd_basefill_060(ocd_basefill_060):
    return _base_universe_d2(ocd_basefill_060, 55)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_055_ocd_basefill_060'] = {'inputs': ['ocd_basefill_060'], 'func': ocd_base_universe_d2_055_ocd_basefill_060}


def ocd_base_universe_d2_056_ocd_basefill_061(ocd_basefill_061):
    return _base_universe_d2(ocd_basefill_061, 56)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_056_ocd_basefill_061'] = {'inputs': ['ocd_basefill_061'], 'func': ocd_base_universe_d2_056_ocd_basefill_061}


def ocd_base_universe_d2_057_ocd_basefill_062(ocd_basefill_062):
    return _base_universe_d2(ocd_basefill_062, 57)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_057_ocd_basefill_062'] = {'inputs': ['ocd_basefill_062'], 'func': ocd_base_universe_d2_057_ocd_basefill_062}


def ocd_base_universe_d2_058_ocd_basefill_063(ocd_basefill_063):
    return _base_universe_d2(ocd_basefill_063, 58)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_058_ocd_basefill_063'] = {'inputs': ['ocd_basefill_063'], 'func': ocd_base_universe_d2_058_ocd_basefill_063}


def ocd_base_universe_d2_059_ocd_basefill_064(ocd_basefill_064):
    return _base_universe_d2(ocd_basefill_064, 59)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_059_ocd_basefill_064'] = {'inputs': ['ocd_basefill_064'], 'func': ocd_base_universe_d2_059_ocd_basefill_064}


def ocd_base_universe_d2_060_ocd_basefill_065(ocd_basefill_065):
    return _base_universe_d2(ocd_basefill_065, 60)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_060_ocd_basefill_065'] = {'inputs': ['ocd_basefill_065'], 'func': ocd_base_universe_d2_060_ocd_basefill_065}


def ocd_base_universe_d2_061_ocd_basefill_066(ocd_basefill_066):
    return _base_universe_d2(ocd_basefill_066, 61)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_061_ocd_basefill_066'] = {'inputs': ['ocd_basefill_066'], 'func': ocd_base_universe_d2_061_ocd_basefill_066}


def ocd_base_universe_d2_062_ocd_basefill_067(ocd_basefill_067):
    return _base_universe_d2(ocd_basefill_067, 62)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_062_ocd_basefill_067'] = {'inputs': ['ocd_basefill_067'], 'func': ocd_base_universe_d2_062_ocd_basefill_067}


def ocd_base_universe_d2_063_ocd_basefill_068(ocd_basefill_068):
    return _base_universe_d2(ocd_basefill_068, 63)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_063_ocd_basefill_068'] = {'inputs': ['ocd_basefill_068'], 'func': ocd_base_universe_d2_063_ocd_basefill_068}


def ocd_base_universe_d2_064_ocd_basefill_069(ocd_basefill_069):
    return _base_universe_d2(ocd_basefill_069, 64)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_064_ocd_basefill_069'] = {'inputs': ['ocd_basefill_069'], 'func': ocd_base_universe_d2_064_ocd_basefill_069}


def ocd_base_universe_d2_065_ocd_basefill_070(ocd_basefill_070):
    return _base_universe_d2(ocd_basefill_070, 65)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_065_ocd_basefill_070'] = {'inputs': ['ocd_basefill_070'], 'func': ocd_base_universe_d2_065_ocd_basefill_070}


def ocd_base_universe_d2_066_ocd_basefill_071(ocd_basefill_071):
    return _base_universe_d2(ocd_basefill_071, 66)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_066_ocd_basefill_071'] = {'inputs': ['ocd_basefill_071'], 'func': ocd_base_universe_d2_066_ocd_basefill_071}


def ocd_base_universe_d2_067_ocd_basefill_072(ocd_basefill_072):
    return _base_universe_d2(ocd_basefill_072, 67)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_067_ocd_basefill_072'] = {'inputs': ['ocd_basefill_072'], 'func': ocd_base_universe_d2_067_ocd_basefill_072}


def ocd_base_universe_d2_068_ocd_basefill_073(ocd_basefill_073):
    return _base_universe_d2(ocd_basefill_073, 68)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_068_ocd_basefill_073'] = {'inputs': ['ocd_basefill_073'], 'func': ocd_base_universe_d2_068_ocd_basefill_073}


def ocd_base_universe_d2_069_ocd_basefill_074(ocd_basefill_074):
    return _base_universe_d2(ocd_basefill_074, 69)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_069_ocd_basefill_074'] = {'inputs': ['ocd_basefill_074'], 'func': ocd_base_universe_d2_069_ocd_basefill_074}


def ocd_base_universe_d2_070_ocd_basefill_075(ocd_basefill_075):
    return _base_universe_d2(ocd_basefill_075, 70)
OCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocd_base_universe_d2_070_ocd_basefill_075'] = {'inputs': ['ocd_basefill_075'], 'func': ocd_base_universe_d2_070_ocd_basefill_075}
