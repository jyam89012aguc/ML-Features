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



def swk_151_swk_001_gap_down_frequency_5_001_roc_1(swk_001_gap_down_frequency_5_001):
    feature = _s(swk_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def swk_152_swk_007_gap_down_frequency_126_007_roc_5(swk_007_gap_down_frequency_126_007):
    feature = _s(swk_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def swk_153_swk_013_gap_down_frequency_1008_013_roc_42(swk_013_gap_down_frequency_1008_013):
    feature = _s(swk_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def swk_154_swk_019_gap_down_frequency_42_019_roc_126(swk_019_gap_down_frequency_42_019):
    feature = _s(swk_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def swk_155_swk_025_gap_down_frequency_378_025_roc_378(swk_025_gap_down_frequency_378_025):
    feature = _s(swk_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















SHADOW_WICK_ANALYSIS_REGISTRY_2ND_DERIVATIVES = {
    'swk_151_swk_001_gap_down_frequency_5_001_roc_1': {'inputs': ['swk_001_gap_down_frequency_5_001'], 'func': swk_151_swk_001_gap_down_frequency_5_001_roc_1},
    'swk_152_swk_007_gap_down_frequency_126_007_roc_5': {'inputs': ['swk_007_gap_down_frequency_126_007'], 'func': swk_152_swk_007_gap_down_frequency_126_007_roc_5},
    'swk_153_swk_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['swk_013_gap_down_frequency_1008_013'], 'func': swk_153_swk_013_gap_down_frequency_1008_013_roc_42},
    'swk_154_swk_019_gap_down_frequency_42_019_roc_126': {'inputs': ['swk_019_gap_down_frequency_42_019'], 'func': swk_154_swk_019_gap_down_frequency_42_019_roc_126},
    'swk_155_swk_025_gap_down_frequency_378_025_roc_378': {'inputs': ['swk_025_gap_down_frequency_378_025'], 'func': swk_155_swk_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def swa_replacement_d2_001(swa_replacement_001):
    feature = _clean(swa_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_001'] = {'inputs': ['swa_replacement_001'], 'func': swa_replacement_d2_001}


def swa_replacement_d2_002(swa_replacement_002):
    feature = _clean(swa_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_002'] = {'inputs': ['swa_replacement_002'], 'func': swa_replacement_d2_002}


def swa_replacement_d2_003(swa_replacement_003):
    feature = _clean(swa_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_003'] = {'inputs': ['swa_replacement_003'], 'func': swa_replacement_d2_003}


def swa_replacement_d2_004(swa_replacement_004):
    feature = _clean(swa_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_004'] = {'inputs': ['swa_replacement_004'], 'func': swa_replacement_d2_004}


def swa_replacement_d2_005(swa_replacement_005):
    feature = _clean(swa_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_005'] = {'inputs': ['swa_replacement_005'], 'func': swa_replacement_d2_005}


def swa_replacement_d2_006(swa_replacement_006):
    feature = _clean(swa_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_006'] = {'inputs': ['swa_replacement_006'], 'func': swa_replacement_d2_006}


def swa_replacement_d2_007(swa_replacement_007):
    feature = _clean(swa_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_007'] = {'inputs': ['swa_replacement_007'], 'func': swa_replacement_d2_007}


def swa_replacement_d2_008(swa_replacement_008):
    feature = _clean(swa_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_008'] = {'inputs': ['swa_replacement_008'], 'func': swa_replacement_d2_008}


def swa_replacement_d2_009(swa_replacement_009):
    feature = _clean(swa_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_009'] = {'inputs': ['swa_replacement_009'], 'func': swa_replacement_d2_009}


def swa_replacement_d2_010(swa_replacement_010):
    feature = _clean(swa_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_010'] = {'inputs': ['swa_replacement_010'], 'func': swa_replacement_d2_010}


def swa_replacement_d2_011(swa_replacement_011):
    feature = _clean(swa_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_011'] = {'inputs': ['swa_replacement_011'], 'func': swa_replacement_d2_011}


def swa_replacement_d2_012(swa_replacement_012):
    feature = _clean(swa_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_012'] = {'inputs': ['swa_replacement_012'], 'func': swa_replacement_d2_012}


def swa_replacement_d2_013(swa_replacement_013):
    feature = _clean(swa_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_013'] = {'inputs': ['swa_replacement_013'], 'func': swa_replacement_d2_013}


def swa_replacement_d2_014(swa_replacement_014):
    feature = _clean(swa_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_014'] = {'inputs': ['swa_replacement_014'], 'func': swa_replacement_d2_014}


def swa_replacement_d2_015(swa_replacement_015):
    feature = _clean(swa_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_015'] = {'inputs': ['swa_replacement_015'], 'func': swa_replacement_d2_015}


def swa_replacement_d2_016(swa_replacement_016):
    feature = _clean(swa_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_016'] = {'inputs': ['swa_replacement_016'], 'func': swa_replacement_d2_016}


def swa_replacement_d2_017(swa_replacement_017):
    feature = _clean(swa_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_017'] = {'inputs': ['swa_replacement_017'], 'func': swa_replacement_d2_017}


def swa_replacement_d2_018(swa_replacement_018):
    feature = _clean(swa_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_018'] = {'inputs': ['swa_replacement_018'], 'func': swa_replacement_d2_018}


def swa_replacement_d2_019(swa_replacement_019):
    feature = _clean(swa_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_019'] = {'inputs': ['swa_replacement_019'], 'func': swa_replacement_d2_019}


def swa_replacement_d2_020(swa_replacement_020):
    feature = _clean(swa_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_020'] = {'inputs': ['swa_replacement_020'], 'func': swa_replacement_d2_020}


def swa_replacement_d2_021(swa_replacement_021):
    feature = _clean(swa_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_021'] = {'inputs': ['swa_replacement_021'], 'func': swa_replacement_d2_021}


def swa_replacement_d2_022(swa_replacement_022):
    feature = _clean(swa_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_022'] = {'inputs': ['swa_replacement_022'], 'func': swa_replacement_d2_022}


def swa_replacement_d2_023(swa_replacement_023):
    feature = _clean(swa_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_023'] = {'inputs': ['swa_replacement_023'], 'func': swa_replacement_d2_023}


def swa_replacement_d2_024(swa_replacement_024):
    feature = _clean(swa_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_024'] = {'inputs': ['swa_replacement_024'], 'func': swa_replacement_d2_024}


def swa_replacement_d2_025(swa_replacement_025):
    feature = _clean(swa_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_025'] = {'inputs': ['swa_replacement_025'], 'func': swa_replacement_d2_025}


def swa_replacement_d2_026(swa_replacement_026):
    feature = _clean(swa_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_026'] = {'inputs': ['swa_replacement_026'], 'func': swa_replacement_d2_026}


def swa_replacement_d2_027(swa_replacement_027):
    feature = _clean(swa_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_027'] = {'inputs': ['swa_replacement_027'], 'func': swa_replacement_d2_027}


def swa_replacement_d2_028(swa_replacement_028):
    feature = _clean(swa_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_028'] = {'inputs': ['swa_replacement_028'], 'func': swa_replacement_d2_028}


def swa_replacement_d2_029(swa_replacement_029):
    feature = _clean(swa_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_029'] = {'inputs': ['swa_replacement_029'], 'func': swa_replacement_d2_029}


def swa_replacement_d2_030(swa_replacement_030):
    feature = _clean(swa_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_030'] = {'inputs': ['swa_replacement_030'], 'func': swa_replacement_d2_030}


def swa_replacement_d2_031(swa_replacement_031):
    feature = _clean(swa_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_031'] = {'inputs': ['swa_replacement_031'], 'func': swa_replacement_d2_031}


def swa_replacement_d2_032(swa_replacement_032):
    feature = _clean(swa_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_032'] = {'inputs': ['swa_replacement_032'], 'func': swa_replacement_d2_032}


def swa_replacement_d2_033(swa_replacement_033):
    feature = _clean(swa_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_033'] = {'inputs': ['swa_replacement_033'], 'func': swa_replacement_d2_033}


def swa_replacement_d2_034(swa_replacement_034):
    feature = _clean(swa_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_034'] = {'inputs': ['swa_replacement_034'], 'func': swa_replacement_d2_034}


def swa_replacement_d2_035(swa_replacement_035):
    feature = _clean(swa_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_035'] = {'inputs': ['swa_replacement_035'], 'func': swa_replacement_d2_035}


def swa_replacement_d2_036(swa_replacement_036):
    feature = _clean(swa_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_036'] = {'inputs': ['swa_replacement_036'], 'func': swa_replacement_d2_036}


def swa_replacement_d2_037(swa_replacement_037):
    feature = _clean(swa_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_037'] = {'inputs': ['swa_replacement_037'], 'func': swa_replacement_d2_037}


def swa_replacement_d2_038(swa_replacement_038):
    feature = _clean(swa_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_038'] = {'inputs': ['swa_replacement_038'], 'func': swa_replacement_d2_038}


def swa_replacement_d2_039(swa_replacement_039):
    feature = _clean(swa_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_039'] = {'inputs': ['swa_replacement_039'], 'func': swa_replacement_d2_039}


def swa_replacement_d2_040(swa_replacement_040):
    feature = _clean(swa_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_040'] = {'inputs': ['swa_replacement_040'], 'func': swa_replacement_d2_040}


def swa_replacement_d2_041(swa_replacement_041):
    feature = _clean(swa_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_041'] = {'inputs': ['swa_replacement_041'], 'func': swa_replacement_d2_041}


def swa_replacement_d2_042(swa_replacement_042):
    feature = _clean(swa_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_042'] = {'inputs': ['swa_replacement_042'], 'func': swa_replacement_d2_042}


def swa_replacement_d2_043(swa_replacement_043):
    feature = _clean(swa_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_043'] = {'inputs': ['swa_replacement_043'], 'func': swa_replacement_d2_043}


def swa_replacement_d2_044(swa_replacement_044):
    feature = _clean(swa_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_044'] = {'inputs': ['swa_replacement_044'], 'func': swa_replacement_d2_044}


def swa_replacement_d2_045(swa_replacement_045):
    feature = _clean(swa_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_045'] = {'inputs': ['swa_replacement_045'], 'func': swa_replacement_d2_045}


def swa_replacement_d2_046(swa_replacement_046):
    feature = _clean(swa_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_046'] = {'inputs': ['swa_replacement_046'], 'func': swa_replacement_d2_046}


def swa_replacement_d2_047(swa_replacement_047):
    feature = _clean(swa_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_047'] = {'inputs': ['swa_replacement_047'], 'func': swa_replacement_d2_047}


def swa_replacement_d2_048(swa_replacement_048):
    feature = _clean(swa_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_048'] = {'inputs': ['swa_replacement_048'], 'func': swa_replacement_d2_048}


def swa_replacement_d2_049(swa_replacement_049):
    feature = _clean(swa_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_049'] = {'inputs': ['swa_replacement_049'], 'func': swa_replacement_d2_049}


def swa_replacement_d2_050(swa_replacement_050):
    feature = _clean(swa_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_050'] = {'inputs': ['swa_replacement_050'], 'func': swa_replacement_d2_050}


def swa_replacement_d2_051(swa_replacement_051):
    feature = _clean(swa_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_051'] = {'inputs': ['swa_replacement_051'], 'func': swa_replacement_d2_051}


def swa_replacement_d2_052(swa_replacement_052):
    feature = _clean(swa_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_052'] = {'inputs': ['swa_replacement_052'], 'func': swa_replacement_d2_052}


def swa_replacement_d2_053(swa_replacement_053):
    feature = _clean(swa_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_053'] = {'inputs': ['swa_replacement_053'], 'func': swa_replacement_d2_053}


def swa_replacement_d2_054(swa_replacement_054):
    feature = _clean(swa_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_054'] = {'inputs': ['swa_replacement_054'], 'func': swa_replacement_d2_054}


def swa_replacement_d2_055(swa_replacement_055):
    feature = _clean(swa_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_055'] = {'inputs': ['swa_replacement_055'], 'func': swa_replacement_d2_055}


def swa_replacement_d2_056(swa_replacement_056):
    feature = _clean(swa_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_056'] = {'inputs': ['swa_replacement_056'], 'func': swa_replacement_d2_056}


def swa_replacement_d2_057(swa_replacement_057):
    feature = _clean(swa_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_057'] = {'inputs': ['swa_replacement_057'], 'func': swa_replacement_d2_057}


def swa_replacement_d2_058(swa_replacement_058):
    feature = _clean(swa_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_058'] = {'inputs': ['swa_replacement_058'], 'func': swa_replacement_d2_058}


def swa_replacement_d2_059(swa_replacement_059):
    feature = _clean(swa_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_059'] = {'inputs': ['swa_replacement_059'], 'func': swa_replacement_d2_059}


def swa_replacement_d2_060(swa_replacement_060):
    feature = _clean(swa_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_060'] = {'inputs': ['swa_replacement_060'], 'func': swa_replacement_d2_060}


def swa_replacement_d2_061(swa_replacement_061):
    feature = _clean(swa_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_061'] = {'inputs': ['swa_replacement_061'], 'func': swa_replacement_d2_061}


def swa_replacement_d2_062(swa_replacement_062):
    feature = _clean(swa_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_062'] = {'inputs': ['swa_replacement_062'], 'func': swa_replacement_d2_062}


def swa_replacement_d2_063(swa_replacement_063):
    feature = _clean(swa_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_063'] = {'inputs': ['swa_replacement_063'], 'func': swa_replacement_d2_063}


def swa_replacement_d2_064(swa_replacement_064):
    feature = _clean(swa_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_064'] = {'inputs': ['swa_replacement_064'], 'func': swa_replacement_d2_064}


def swa_replacement_d2_065(swa_replacement_065):
    feature = _clean(swa_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_065'] = {'inputs': ['swa_replacement_065'], 'func': swa_replacement_d2_065}


def swa_replacement_d2_066(swa_replacement_066):
    feature = _clean(swa_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_066'] = {'inputs': ['swa_replacement_066'], 'func': swa_replacement_d2_066}


def swa_replacement_d2_067(swa_replacement_067):
    feature = _clean(swa_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_067'] = {'inputs': ['swa_replacement_067'], 'func': swa_replacement_d2_067}


def swa_replacement_d2_068(swa_replacement_068):
    feature = _clean(swa_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_068'] = {'inputs': ['swa_replacement_068'], 'func': swa_replacement_d2_068}


def swa_replacement_d2_069(swa_replacement_069):
    feature = _clean(swa_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_069'] = {'inputs': ['swa_replacement_069'], 'func': swa_replacement_d2_069}


def swa_replacement_d2_070(swa_replacement_070):
    feature = _clean(swa_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_070'] = {'inputs': ['swa_replacement_070'], 'func': swa_replacement_d2_070}


def swa_replacement_d2_071(swa_replacement_071):
    feature = _clean(swa_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_071'] = {'inputs': ['swa_replacement_071'], 'func': swa_replacement_d2_071}


def swa_replacement_d2_072(swa_replacement_072):
    feature = _clean(swa_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_072'] = {'inputs': ['swa_replacement_072'], 'func': swa_replacement_d2_072}


def swa_replacement_d2_073(swa_replacement_073):
    feature = _clean(swa_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_073'] = {'inputs': ['swa_replacement_073'], 'func': swa_replacement_d2_073}


def swa_replacement_d2_074(swa_replacement_074):
    feature = _clean(swa_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_074'] = {'inputs': ['swa_replacement_074'], 'func': swa_replacement_d2_074}


def swa_replacement_d2_075(swa_replacement_075):
    feature = _clean(swa_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_075'] = {'inputs': ['swa_replacement_075'], 'func': swa_replacement_d2_075}


def swa_replacement_d2_076(swa_replacement_076):
    feature = _clean(swa_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_076'] = {'inputs': ['swa_replacement_076'], 'func': swa_replacement_d2_076}


def swa_replacement_d2_077(swa_replacement_077):
    feature = _clean(swa_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_077'] = {'inputs': ['swa_replacement_077'], 'func': swa_replacement_d2_077}


def swa_replacement_d2_078(swa_replacement_078):
    feature = _clean(swa_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_078'] = {'inputs': ['swa_replacement_078'], 'func': swa_replacement_d2_078}


def swa_replacement_d2_079(swa_replacement_079):
    feature = _clean(swa_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_079'] = {'inputs': ['swa_replacement_079'], 'func': swa_replacement_d2_079}


def swa_replacement_d2_080(swa_replacement_080):
    feature = _clean(swa_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_080'] = {'inputs': ['swa_replacement_080'], 'func': swa_replacement_d2_080}


def swa_replacement_d2_081(swa_replacement_081):
    feature = _clean(swa_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_081'] = {'inputs': ['swa_replacement_081'], 'func': swa_replacement_d2_081}


def swa_replacement_d2_082(swa_replacement_082):
    feature = _clean(swa_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_082'] = {'inputs': ['swa_replacement_082'], 'func': swa_replacement_d2_082}


def swa_replacement_d2_083(swa_replacement_083):
    feature = _clean(swa_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_083'] = {'inputs': ['swa_replacement_083'], 'func': swa_replacement_d2_083}


def swa_replacement_d2_084(swa_replacement_084):
    feature = _clean(swa_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_084'] = {'inputs': ['swa_replacement_084'], 'func': swa_replacement_d2_084}


def swa_replacement_d2_085(swa_replacement_085):
    feature = _clean(swa_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_085'] = {'inputs': ['swa_replacement_085'], 'func': swa_replacement_d2_085}


def swa_replacement_d2_086(swa_replacement_086):
    feature = _clean(swa_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_086'] = {'inputs': ['swa_replacement_086'], 'func': swa_replacement_d2_086}


def swa_replacement_d2_087(swa_replacement_087):
    feature = _clean(swa_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_087'] = {'inputs': ['swa_replacement_087'], 'func': swa_replacement_d2_087}


def swa_replacement_d2_088(swa_replacement_088):
    feature = _clean(swa_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_088'] = {'inputs': ['swa_replacement_088'], 'func': swa_replacement_d2_088}


def swa_replacement_d2_089(swa_replacement_089):
    feature = _clean(swa_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_089'] = {'inputs': ['swa_replacement_089'], 'func': swa_replacement_d2_089}


def swa_replacement_d2_090(swa_replacement_090):
    feature = _clean(swa_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_090'] = {'inputs': ['swa_replacement_090'], 'func': swa_replacement_d2_090}


def swa_replacement_d2_091(swa_replacement_091):
    feature = _clean(swa_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_091'] = {'inputs': ['swa_replacement_091'], 'func': swa_replacement_d2_091}


def swa_replacement_d2_092(swa_replacement_092):
    feature = _clean(swa_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_092'] = {'inputs': ['swa_replacement_092'], 'func': swa_replacement_d2_092}


def swa_replacement_d2_093(swa_replacement_093):
    feature = _clean(swa_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_093'] = {'inputs': ['swa_replacement_093'], 'func': swa_replacement_d2_093}


def swa_replacement_d2_094(swa_replacement_094):
    feature = _clean(swa_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_094'] = {'inputs': ['swa_replacement_094'], 'func': swa_replacement_d2_094}


def swa_replacement_d2_095(swa_replacement_095):
    feature = _clean(swa_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_095'] = {'inputs': ['swa_replacement_095'], 'func': swa_replacement_d2_095}


def swa_replacement_d2_096(swa_replacement_096):
    feature = _clean(swa_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_096'] = {'inputs': ['swa_replacement_096'], 'func': swa_replacement_d2_096}


def swa_replacement_d2_097(swa_replacement_097):
    feature = _clean(swa_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_097'] = {'inputs': ['swa_replacement_097'], 'func': swa_replacement_d2_097}


def swa_replacement_d2_098(swa_replacement_098):
    feature = _clean(swa_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_098'] = {'inputs': ['swa_replacement_098'], 'func': swa_replacement_d2_098}


def swa_replacement_d2_099(swa_replacement_099):
    feature = _clean(swa_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_099'] = {'inputs': ['swa_replacement_099'], 'func': swa_replacement_d2_099}


def swa_replacement_d2_100(swa_replacement_100):
    feature = _clean(swa_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_100'] = {'inputs': ['swa_replacement_100'], 'func': swa_replacement_d2_100}


def swa_replacement_d2_101(swa_replacement_101):
    feature = _clean(swa_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_101'] = {'inputs': ['swa_replacement_101'], 'func': swa_replacement_d2_101}


def swa_replacement_d2_102(swa_replacement_102):
    feature = _clean(swa_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_102'] = {'inputs': ['swa_replacement_102'], 'func': swa_replacement_d2_102}


def swa_replacement_d2_103(swa_replacement_103):
    feature = _clean(swa_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_103'] = {'inputs': ['swa_replacement_103'], 'func': swa_replacement_d2_103}


def swa_replacement_d2_104(swa_replacement_104):
    feature = _clean(swa_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_104'] = {'inputs': ['swa_replacement_104'], 'func': swa_replacement_d2_104}


def swa_replacement_d2_105(swa_replacement_105):
    feature = _clean(swa_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_105'] = {'inputs': ['swa_replacement_105'], 'func': swa_replacement_d2_105}


def swa_replacement_d2_106(swa_replacement_106):
    feature = _clean(swa_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_106'] = {'inputs': ['swa_replacement_106'], 'func': swa_replacement_d2_106}


def swa_replacement_d2_107(swa_replacement_107):
    feature = _clean(swa_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_107'] = {'inputs': ['swa_replacement_107'], 'func': swa_replacement_d2_107}


def swa_replacement_d2_108(swa_replacement_108):
    feature = _clean(swa_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_108'] = {'inputs': ['swa_replacement_108'], 'func': swa_replacement_d2_108}


def swa_replacement_d2_109(swa_replacement_109):
    feature = _clean(swa_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_109'] = {'inputs': ['swa_replacement_109'], 'func': swa_replacement_d2_109}


def swa_replacement_d2_110(swa_replacement_110):
    feature = _clean(swa_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_110'] = {'inputs': ['swa_replacement_110'], 'func': swa_replacement_d2_110}


def swa_replacement_d2_111(swa_replacement_111):
    feature = _clean(swa_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_111'] = {'inputs': ['swa_replacement_111'], 'func': swa_replacement_d2_111}


def swa_replacement_d2_112(swa_replacement_112):
    feature = _clean(swa_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_112'] = {'inputs': ['swa_replacement_112'], 'func': swa_replacement_d2_112}


def swa_replacement_d2_113(swa_replacement_113):
    feature = _clean(swa_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_113'] = {'inputs': ['swa_replacement_113'], 'func': swa_replacement_d2_113}


def swa_replacement_d2_114(swa_replacement_114):
    feature = _clean(swa_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_114'] = {'inputs': ['swa_replacement_114'], 'func': swa_replacement_d2_114}


def swa_replacement_d2_115(swa_replacement_115):
    feature = _clean(swa_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_115'] = {'inputs': ['swa_replacement_115'], 'func': swa_replacement_d2_115}


def swa_replacement_d2_116(swa_replacement_116):
    feature = _clean(swa_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_116'] = {'inputs': ['swa_replacement_116'], 'func': swa_replacement_d2_116}


def swa_replacement_d2_117(swa_replacement_117):
    feature = _clean(swa_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_117'] = {'inputs': ['swa_replacement_117'], 'func': swa_replacement_d2_117}


def swa_replacement_d2_118(swa_replacement_118):
    feature = _clean(swa_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_118'] = {'inputs': ['swa_replacement_118'], 'func': swa_replacement_d2_118}


def swa_replacement_d2_119(swa_replacement_119):
    feature = _clean(swa_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_119'] = {'inputs': ['swa_replacement_119'], 'func': swa_replacement_d2_119}


def swa_replacement_d2_120(swa_replacement_120):
    feature = _clean(swa_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_120'] = {'inputs': ['swa_replacement_120'], 'func': swa_replacement_d2_120}


def swa_replacement_d2_121(swa_replacement_121):
    feature = _clean(swa_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_121'] = {'inputs': ['swa_replacement_121'], 'func': swa_replacement_d2_121}


def swa_replacement_d2_122(swa_replacement_122):
    feature = _clean(swa_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_122'] = {'inputs': ['swa_replacement_122'], 'func': swa_replacement_d2_122}


def swa_replacement_d2_123(swa_replacement_123):
    feature = _clean(swa_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_123'] = {'inputs': ['swa_replacement_123'], 'func': swa_replacement_d2_123}


def swa_replacement_d2_124(swa_replacement_124):
    feature = _clean(swa_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_124'] = {'inputs': ['swa_replacement_124'], 'func': swa_replacement_d2_124}


def swa_replacement_d2_125(swa_replacement_125):
    feature = _clean(swa_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_125'] = {'inputs': ['swa_replacement_125'], 'func': swa_replacement_d2_125}


def swa_replacement_d2_126(swa_replacement_126):
    feature = _clean(swa_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_126'] = {'inputs': ['swa_replacement_126'], 'func': swa_replacement_d2_126}


def swa_replacement_d2_127(swa_replacement_127):
    feature = _clean(swa_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_127'] = {'inputs': ['swa_replacement_127'], 'func': swa_replacement_d2_127}


def swa_replacement_d2_128(swa_replacement_128):
    feature = _clean(swa_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_128'] = {'inputs': ['swa_replacement_128'], 'func': swa_replacement_d2_128}


def swa_replacement_d2_129(swa_replacement_129):
    feature = _clean(swa_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_129'] = {'inputs': ['swa_replacement_129'], 'func': swa_replacement_d2_129}


def swa_replacement_d2_130(swa_replacement_130):
    feature = _clean(swa_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_130'] = {'inputs': ['swa_replacement_130'], 'func': swa_replacement_d2_130}


def swa_replacement_d2_131(swa_replacement_131):
    feature = _clean(swa_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_131'] = {'inputs': ['swa_replacement_131'], 'func': swa_replacement_d2_131}


def swa_replacement_d2_132(swa_replacement_132):
    feature = _clean(swa_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_132'] = {'inputs': ['swa_replacement_132'], 'func': swa_replacement_d2_132}


def swa_replacement_d2_133(swa_replacement_133):
    feature = _clean(swa_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_133'] = {'inputs': ['swa_replacement_133'], 'func': swa_replacement_d2_133}


def swa_replacement_d2_134(swa_replacement_134):
    feature = _clean(swa_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_134'] = {'inputs': ['swa_replacement_134'], 'func': swa_replacement_d2_134}


def swa_replacement_d2_135(swa_replacement_135):
    feature = _clean(swa_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_135'] = {'inputs': ['swa_replacement_135'], 'func': swa_replacement_d2_135}


def swa_replacement_d2_136(swa_replacement_136):
    feature = _clean(swa_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_136'] = {'inputs': ['swa_replacement_136'], 'func': swa_replacement_d2_136}


def swa_replacement_d2_137(swa_replacement_137):
    feature = _clean(swa_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_137'] = {'inputs': ['swa_replacement_137'], 'func': swa_replacement_d2_137}


def swa_replacement_d2_138(swa_replacement_138):
    feature = _clean(swa_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_138'] = {'inputs': ['swa_replacement_138'], 'func': swa_replacement_d2_138}


def swa_replacement_d2_139(swa_replacement_139):
    feature = _clean(swa_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_139'] = {'inputs': ['swa_replacement_139'], 'func': swa_replacement_d2_139}


def swa_replacement_d2_140(swa_replacement_140):
    feature = _clean(swa_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_140'] = {'inputs': ['swa_replacement_140'], 'func': swa_replacement_d2_140}


def swa_replacement_d2_141(swa_replacement_141):
    feature = _clean(swa_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_141'] = {'inputs': ['swa_replacement_141'], 'func': swa_replacement_d2_141}


def swa_replacement_d2_142(swa_replacement_142):
    feature = _clean(swa_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_142'] = {'inputs': ['swa_replacement_142'], 'func': swa_replacement_d2_142}


def swa_replacement_d2_143(swa_replacement_143):
    feature = _clean(swa_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_143'] = {'inputs': ['swa_replacement_143'], 'func': swa_replacement_d2_143}


def swa_replacement_d2_144(swa_replacement_144):
    feature = _clean(swa_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_144'] = {'inputs': ['swa_replacement_144'], 'func': swa_replacement_d2_144}


def swa_replacement_d2_145(swa_replacement_145):
    feature = _clean(swa_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_145'] = {'inputs': ['swa_replacement_145'], 'func': swa_replacement_d2_145}


def swa_replacement_d2_146(swa_replacement_146):
    feature = _clean(swa_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_146'] = {'inputs': ['swa_replacement_146'], 'func': swa_replacement_d2_146}


def swa_replacement_d2_147(swa_replacement_147):
    feature = _clean(swa_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_147'] = {'inputs': ['swa_replacement_147'], 'func': swa_replacement_d2_147}


def swa_replacement_d2_148(swa_replacement_148):
    feature = _clean(swa_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_148'] = {'inputs': ['swa_replacement_148'], 'func': swa_replacement_d2_148}


def swa_replacement_d2_149(swa_replacement_149):
    feature = _clean(swa_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_149'] = {'inputs': ['swa_replacement_149'], 'func': swa_replacement_d2_149}


def swa_replacement_d2_150(swa_replacement_150):
    feature = _clean(swa_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_150'] = {'inputs': ['swa_replacement_150'], 'func': swa_replacement_d2_150}


def swa_replacement_d2_151(swa_replacement_151):
    feature = _clean(swa_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_151'] = {'inputs': ['swa_replacement_151'], 'func': swa_replacement_d2_151}


def swa_replacement_d2_152(swa_replacement_152):
    feature = _clean(swa_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_152'] = {'inputs': ['swa_replacement_152'], 'func': swa_replacement_d2_152}


def swa_replacement_d2_153(swa_replacement_153):
    feature = _clean(swa_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_153'] = {'inputs': ['swa_replacement_153'], 'func': swa_replacement_d2_153}


def swa_replacement_d2_154(swa_replacement_154):
    feature = _clean(swa_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_154'] = {'inputs': ['swa_replacement_154'], 'func': swa_replacement_d2_154}


def swa_replacement_d2_155(swa_replacement_155):
    feature = _clean(swa_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_155'] = {'inputs': ['swa_replacement_155'], 'func': swa_replacement_d2_155}


def swa_replacement_d2_156(swa_replacement_156):
    feature = _clean(swa_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_156'] = {'inputs': ['swa_replacement_156'], 'func': swa_replacement_d2_156}


def swa_replacement_d2_157(swa_replacement_157):
    feature = _clean(swa_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_157'] = {'inputs': ['swa_replacement_157'], 'func': swa_replacement_d2_157}


def swa_replacement_d2_158(swa_replacement_158):
    feature = _clean(swa_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_158'] = {'inputs': ['swa_replacement_158'], 'func': swa_replacement_d2_158}


def swa_replacement_d2_159(swa_replacement_159):
    feature = _clean(swa_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_159'] = {'inputs': ['swa_replacement_159'], 'func': swa_replacement_d2_159}


def swa_replacement_d2_160(swa_replacement_160):
    feature = _clean(swa_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
SWA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['swa_replacement_d2_160'] = {'inputs': ['swa_replacement_160'], 'func': swa_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def swk_base_universe_d2_001_swk_002_gap_magnitude_10_002(swk_002_gap_magnitude_10_002):
    return _base_universe_d2(swk_002_gap_magnitude_10_002, 1)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_001_swk_002_gap_magnitude_10_002'] = {'inputs': ['swk_002_gap_magnitude_10_002'], 'func': swk_base_universe_d2_001_swk_002_gap_magnitude_10_002}


def swk_base_universe_d2_002_swk_003_open_close_pressure_21_003(swk_003_open_close_pressure_21_003):
    return _base_universe_d2(swk_003_open_close_pressure_21_003, 2)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_002_swk_003_open_close_pressure_21_003'] = {'inputs': ['swk_003_open_close_pressure_21_003'], 'func': swk_base_universe_d2_002_swk_003_open_close_pressure_21_003}


def swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004(swk_004_lower_wick_ratio_42_004):
    return _base_universe_d2(swk_004_lower_wick_ratio_42_004, 3)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004'] = {'inputs': ['swk_004_lower_wick_ratio_42_004'], 'func': swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004}


def swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005(swk_005_upper_wick_ratio_63_005):
    return _base_universe_d2(swk_005_upper_wick_ratio_63_005, 4)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005'] = {'inputs': ['swk_005_upper_wick_ratio_63_005'], 'func': swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005}


def swk_base_universe_d2_005_swk_006_body_to_range_84_006(swk_006_body_to_range_84_006):
    return _base_universe_d2(swk_006_body_to_range_84_006, 5)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_005_swk_006_body_to_range_84_006'] = {'inputs': ['swk_006_body_to_range_84_006'], 'func': swk_base_universe_d2_005_swk_006_body_to_range_84_006}


def swk_base_universe_d2_006_swk_008_gap_magnitude_189_008(swk_008_gap_magnitude_189_008):
    return _base_universe_d2(swk_008_gap_magnitude_189_008, 6)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_006_swk_008_gap_magnitude_189_008'] = {'inputs': ['swk_008_gap_magnitude_189_008'], 'func': swk_base_universe_d2_006_swk_008_gap_magnitude_189_008}


def swk_base_universe_d2_007_swk_009_open_close_pressure_252_009(swk_009_open_close_pressure_252_009):
    return _base_universe_d2(swk_009_open_close_pressure_252_009, 7)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_007_swk_009_open_close_pressure_252_009'] = {'inputs': ['swk_009_open_close_pressure_252_009'], 'func': swk_base_universe_d2_007_swk_009_open_close_pressure_252_009}


def swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010(swk_010_lower_wick_ratio_378_010):
    return _base_universe_d2(swk_010_lower_wick_ratio_378_010, 8)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010'] = {'inputs': ['swk_010_lower_wick_ratio_378_010'], 'func': swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010}


def swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011(swk_011_upper_wick_ratio_504_011):
    return _base_universe_d2(swk_011_upper_wick_ratio_504_011, 9)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011'] = {'inputs': ['swk_011_upper_wick_ratio_504_011'], 'func': swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011}


def swk_base_universe_d2_010_swk_012_body_to_range_756_012(swk_012_body_to_range_756_012):
    return _base_universe_d2(swk_012_body_to_range_756_012, 10)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_010_swk_012_body_to_range_756_012'] = {'inputs': ['swk_012_body_to_range_756_012'], 'func': swk_base_universe_d2_010_swk_012_body_to_range_756_012}


def swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014(swk_014_gap_magnitude_1260_014):
    return _base_universe_d2(swk_014_gap_magnitude_1260_014, 11)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014'] = {'inputs': ['swk_014_gap_magnitude_1260_014'], 'func': swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014}


def swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015(swk_015_open_close_pressure_1512_015):
    return _base_universe_d2(swk_015_open_close_pressure_1512_015, 12)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015'] = {'inputs': ['swk_015_open_close_pressure_1512_015'], 'func': swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015}


def swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016(swk_016_lower_wick_ratio_5_016):
    return _base_universe_d2(swk_016_lower_wick_ratio_5_016, 13)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016'] = {'inputs': ['swk_016_lower_wick_ratio_5_016'], 'func': swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016}


def swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017(swk_017_upper_wick_ratio_10_017):
    return _base_universe_d2(swk_017_upper_wick_ratio_10_017, 14)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017'] = {'inputs': ['swk_017_upper_wick_ratio_10_017'], 'func': swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017}


def swk_base_universe_d2_015_swk_018_body_to_range_21_018(swk_018_body_to_range_21_018):
    return _base_universe_d2(swk_018_body_to_range_21_018, 15)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_015_swk_018_body_to_range_21_018'] = {'inputs': ['swk_018_body_to_range_21_018'], 'func': swk_base_universe_d2_015_swk_018_body_to_range_21_018}


def swk_base_universe_d2_016_swk_020_gap_magnitude_63_020(swk_020_gap_magnitude_63_020):
    return _base_universe_d2(swk_020_gap_magnitude_63_020, 16)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_016_swk_020_gap_magnitude_63_020'] = {'inputs': ['swk_020_gap_magnitude_63_020'], 'func': swk_base_universe_d2_016_swk_020_gap_magnitude_63_020}


def swk_base_universe_d2_017_swk_021_open_close_pressure_84_021(swk_021_open_close_pressure_84_021):
    return _base_universe_d2(swk_021_open_close_pressure_84_021, 17)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_017_swk_021_open_close_pressure_84_021'] = {'inputs': ['swk_021_open_close_pressure_84_021'], 'func': swk_base_universe_d2_017_swk_021_open_close_pressure_84_021}


def swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022(swk_022_lower_wick_ratio_126_022):
    return _base_universe_d2(swk_022_lower_wick_ratio_126_022, 18)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022'] = {'inputs': ['swk_022_lower_wick_ratio_126_022'], 'func': swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022}


def swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023(swk_023_upper_wick_ratio_189_023):
    return _base_universe_d2(swk_023_upper_wick_ratio_189_023, 19)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023'] = {'inputs': ['swk_023_upper_wick_ratio_189_023'], 'func': swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023}


def swk_base_universe_d2_020_swk_024_body_to_range_252_024(swk_024_body_to_range_252_024):
    return _base_universe_d2(swk_024_body_to_range_252_024, 20)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_020_swk_024_body_to_range_252_024'] = {'inputs': ['swk_024_body_to_range_252_024'], 'func': swk_base_universe_d2_020_swk_024_body_to_range_252_024}


def swk_base_universe_d2_021_swk_026_gap_magnitude_504_026(swk_026_gap_magnitude_504_026):
    return _base_universe_d2(swk_026_gap_magnitude_504_026, 21)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_021_swk_026_gap_magnitude_504_026'] = {'inputs': ['swk_026_gap_magnitude_504_026'], 'func': swk_base_universe_d2_021_swk_026_gap_magnitude_504_026}


def swk_base_universe_d2_022_swk_027_open_close_pressure_756_027(swk_027_open_close_pressure_756_027):
    return _base_universe_d2(swk_027_open_close_pressure_756_027, 22)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_022_swk_027_open_close_pressure_756_027'] = {'inputs': ['swk_027_open_close_pressure_756_027'], 'func': swk_base_universe_d2_022_swk_027_open_close_pressure_756_027}


def swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028(swk_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(swk_028_lower_wick_ratio_1008_028, 23)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028'] = {'inputs': ['swk_028_lower_wick_ratio_1008_028'], 'func': swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028}


def swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029(swk_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(swk_029_upper_wick_ratio_1260_029, 24)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029'] = {'inputs': ['swk_029_upper_wick_ratio_1260_029'], 'func': swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029}


def swk_base_universe_d2_025_swk_030_body_to_range_1512_030(swk_030_body_to_range_1512_030):
    return _base_universe_d2(swk_030_body_to_range_1512_030, 25)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_025_swk_030_body_to_range_1512_030'] = {'inputs': ['swk_030_body_to_range_1512_030'], 'func': swk_base_universe_d2_025_swk_030_body_to_range_1512_030}


def swk_base_universe_d2_026_swk_basefill_031(swk_basefill_031):
    return _base_universe_d2(swk_basefill_031, 26)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_026_swk_basefill_031'] = {'inputs': ['swk_basefill_031'], 'func': swk_base_universe_d2_026_swk_basefill_031}


def swk_base_universe_d2_027_swk_basefill_032(swk_basefill_032):
    return _base_universe_d2(swk_basefill_032, 27)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_027_swk_basefill_032'] = {'inputs': ['swk_basefill_032'], 'func': swk_base_universe_d2_027_swk_basefill_032}


def swk_base_universe_d2_028_swk_basefill_033(swk_basefill_033):
    return _base_universe_d2(swk_basefill_033, 28)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_028_swk_basefill_033'] = {'inputs': ['swk_basefill_033'], 'func': swk_base_universe_d2_028_swk_basefill_033}


def swk_base_universe_d2_029_swk_basefill_034(swk_basefill_034):
    return _base_universe_d2(swk_basefill_034, 29)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_029_swk_basefill_034'] = {'inputs': ['swk_basefill_034'], 'func': swk_base_universe_d2_029_swk_basefill_034}


def swk_base_universe_d2_030_swk_basefill_035(swk_basefill_035):
    return _base_universe_d2(swk_basefill_035, 30)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_030_swk_basefill_035'] = {'inputs': ['swk_basefill_035'], 'func': swk_base_universe_d2_030_swk_basefill_035}


def swk_base_universe_d2_031_swk_basefill_036(swk_basefill_036):
    return _base_universe_d2(swk_basefill_036, 31)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_031_swk_basefill_036'] = {'inputs': ['swk_basefill_036'], 'func': swk_base_universe_d2_031_swk_basefill_036}


def swk_base_universe_d2_032_swk_basefill_037(swk_basefill_037):
    return _base_universe_d2(swk_basefill_037, 32)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_032_swk_basefill_037'] = {'inputs': ['swk_basefill_037'], 'func': swk_base_universe_d2_032_swk_basefill_037}


def swk_base_universe_d2_033_swk_basefill_038(swk_basefill_038):
    return _base_universe_d2(swk_basefill_038, 33)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_033_swk_basefill_038'] = {'inputs': ['swk_basefill_038'], 'func': swk_base_universe_d2_033_swk_basefill_038}


def swk_base_universe_d2_034_swk_basefill_039(swk_basefill_039):
    return _base_universe_d2(swk_basefill_039, 34)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_034_swk_basefill_039'] = {'inputs': ['swk_basefill_039'], 'func': swk_base_universe_d2_034_swk_basefill_039}


def swk_base_universe_d2_035_swk_basefill_040(swk_basefill_040):
    return _base_universe_d2(swk_basefill_040, 35)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_035_swk_basefill_040'] = {'inputs': ['swk_basefill_040'], 'func': swk_base_universe_d2_035_swk_basefill_040}


def swk_base_universe_d2_036_swk_basefill_041(swk_basefill_041):
    return _base_universe_d2(swk_basefill_041, 36)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_036_swk_basefill_041'] = {'inputs': ['swk_basefill_041'], 'func': swk_base_universe_d2_036_swk_basefill_041}


def swk_base_universe_d2_037_swk_basefill_042(swk_basefill_042):
    return _base_universe_d2(swk_basefill_042, 37)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_037_swk_basefill_042'] = {'inputs': ['swk_basefill_042'], 'func': swk_base_universe_d2_037_swk_basefill_042}


def swk_base_universe_d2_038_swk_basefill_043(swk_basefill_043):
    return _base_universe_d2(swk_basefill_043, 38)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_038_swk_basefill_043'] = {'inputs': ['swk_basefill_043'], 'func': swk_base_universe_d2_038_swk_basefill_043}


def swk_base_universe_d2_039_swk_basefill_044(swk_basefill_044):
    return _base_universe_d2(swk_basefill_044, 39)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_039_swk_basefill_044'] = {'inputs': ['swk_basefill_044'], 'func': swk_base_universe_d2_039_swk_basefill_044}


def swk_base_universe_d2_040_swk_basefill_045(swk_basefill_045):
    return _base_universe_d2(swk_basefill_045, 40)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_040_swk_basefill_045'] = {'inputs': ['swk_basefill_045'], 'func': swk_base_universe_d2_040_swk_basefill_045}


def swk_base_universe_d2_041_swk_basefill_046(swk_basefill_046):
    return _base_universe_d2(swk_basefill_046, 41)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_041_swk_basefill_046'] = {'inputs': ['swk_basefill_046'], 'func': swk_base_universe_d2_041_swk_basefill_046}


def swk_base_universe_d2_042_swk_basefill_047(swk_basefill_047):
    return _base_universe_d2(swk_basefill_047, 42)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_042_swk_basefill_047'] = {'inputs': ['swk_basefill_047'], 'func': swk_base_universe_d2_042_swk_basefill_047}


def swk_base_universe_d2_043_swk_basefill_048(swk_basefill_048):
    return _base_universe_d2(swk_basefill_048, 43)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_043_swk_basefill_048'] = {'inputs': ['swk_basefill_048'], 'func': swk_base_universe_d2_043_swk_basefill_048}


def swk_base_universe_d2_044_swk_basefill_049(swk_basefill_049):
    return _base_universe_d2(swk_basefill_049, 44)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_044_swk_basefill_049'] = {'inputs': ['swk_basefill_049'], 'func': swk_base_universe_d2_044_swk_basefill_049}


def swk_base_universe_d2_045_swk_basefill_050(swk_basefill_050):
    return _base_universe_d2(swk_basefill_050, 45)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_045_swk_basefill_050'] = {'inputs': ['swk_basefill_050'], 'func': swk_base_universe_d2_045_swk_basefill_050}


def swk_base_universe_d2_046_swk_basefill_051(swk_basefill_051):
    return _base_universe_d2(swk_basefill_051, 46)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_046_swk_basefill_051'] = {'inputs': ['swk_basefill_051'], 'func': swk_base_universe_d2_046_swk_basefill_051}


def swk_base_universe_d2_047_swk_basefill_052(swk_basefill_052):
    return _base_universe_d2(swk_basefill_052, 47)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_047_swk_basefill_052'] = {'inputs': ['swk_basefill_052'], 'func': swk_base_universe_d2_047_swk_basefill_052}


def swk_base_universe_d2_048_swk_basefill_053(swk_basefill_053):
    return _base_universe_d2(swk_basefill_053, 48)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_048_swk_basefill_053'] = {'inputs': ['swk_basefill_053'], 'func': swk_base_universe_d2_048_swk_basefill_053}


def swk_base_universe_d2_049_swk_basefill_054(swk_basefill_054):
    return _base_universe_d2(swk_basefill_054, 49)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_049_swk_basefill_054'] = {'inputs': ['swk_basefill_054'], 'func': swk_base_universe_d2_049_swk_basefill_054}


def swk_base_universe_d2_050_swk_basefill_055(swk_basefill_055):
    return _base_universe_d2(swk_basefill_055, 50)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_050_swk_basefill_055'] = {'inputs': ['swk_basefill_055'], 'func': swk_base_universe_d2_050_swk_basefill_055}


def swk_base_universe_d2_051_swk_basefill_056(swk_basefill_056):
    return _base_universe_d2(swk_basefill_056, 51)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_051_swk_basefill_056'] = {'inputs': ['swk_basefill_056'], 'func': swk_base_universe_d2_051_swk_basefill_056}


def swk_base_universe_d2_052_swk_basefill_057(swk_basefill_057):
    return _base_universe_d2(swk_basefill_057, 52)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_052_swk_basefill_057'] = {'inputs': ['swk_basefill_057'], 'func': swk_base_universe_d2_052_swk_basefill_057}


def swk_base_universe_d2_053_swk_basefill_058(swk_basefill_058):
    return _base_universe_d2(swk_basefill_058, 53)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_053_swk_basefill_058'] = {'inputs': ['swk_basefill_058'], 'func': swk_base_universe_d2_053_swk_basefill_058}


def swk_base_universe_d2_054_swk_basefill_059(swk_basefill_059):
    return _base_universe_d2(swk_basefill_059, 54)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_054_swk_basefill_059'] = {'inputs': ['swk_basefill_059'], 'func': swk_base_universe_d2_054_swk_basefill_059}


def swk_base_universe_d2_055_swk_basefill_060(swk_basefill_060):
    return _base_universe_d2(swk_basefill_060, 55)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_055_swk_basefill_060'] = {'inputs': ['swk_basefill_060'], 'func': swk_base_universe_d2_055_swk_basefill_060}


def swk_base_universe_d2_056_swk_basefill_061(swk_basefill_061):
    return _base_universe_d2(swk_basefill_061, 56)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_056_swk_basefill_061'] = {'inputs': ['swk_basefill_061'], 'func': swk_base_universe_d2_056_swk_basefill_061}


def swk_base_universe_d2_057_swk_basefill_062(swk_basefill_062):
    return _base_universe_d2(swk_basefill_062, 57)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_057_swk_basefill_062'] = {'inputs': ['swk_basefill_062'], 'func': swk_base_universe_d2_057_swk_basefill_062}


def swk_base_universe_d2_058_swk_basefill_063(swk_basefill_063):
    return _base_universe_d2(swk_basefill_063, 58)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_058_swk_basefill_063'] = {'inputs': ['swk_basefill_063'], 'func': swk_base_universe_d2_058_swk_basefill_063}


def swk_base_universe_d2_059_swk_basefill_064(swk_basefill_064):
    return _base_universe_d2(swk_basefill_064, 59)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_059_swk_basefill_064'] = {'inputs': ['swk_basefill_064'], 'func': swk_base_universe_d2_059_swk_basefill_064}


def swk_base_universe_d2_060_swk_basefill_065(swk_basefill_065):
    return _base_universe_d2(swk_basefill_065, 60)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_060_swk_basefill_065'] = {'inputs': ['swk_basefill_065'], 'func': swk_base_universe_d2_060_swk_basefill_065}


def swk_base_universe_d2_061_swk_basefill_066(swk_basefill_066):
    return _base_universe_d2(swk_basefill_066, 61)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_061_swk_basefill_066'] = {'inputs': ['swk_basefill_066'], 'func': swk_base_universe_d2_061_swk_basefill_066}


def swk_base_universe_d2_062_swk_basefill_067(swk_basefill_067):
    return _base_universe_d2(swk_basefill_067, 62)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_062_swk_basefill_067'] = {'inputs': ['swk_basefill_067'], 'func': swk_base_universe_d2_062_swk_basefill_067}


def swk_base_universe_d2_063_swk_basefill_068(swk_basefill_068):
    return _base_universe_d2(swk_basefill_068, 63)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_063_swk_basefill_068'] = {'inputs': ['swk_basefill_068'], 'func': swk_base_universe_d2_063_swk_basefill_068}


def swk_base_universe_d2_064_swk_basefill_069(swk_basefill_069):
    return _base_universe_d2(swk_basefill_069, 64)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_064_swk_basefill_069'] = {'inputs': ['swk_basefill_069'], 'func': swk_base_universe_d2_064_swk_basefill_069}


def swk_base_universe_d2_065_swk_basefill_070(swk_basefill_070):
    return _base_universe_d2(swk_basefill_070, 65)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_065_swk_basefill_070'] = {'inputs': ['swk_basefill_070'], 'func': swk_base_universe_d2_065_swk_basefill_070}


def swk_base_universe_d2_066_swk_basefill_071(swk_basefill_071):
    return _base_universe_d2(swk_basefill_071, 66)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_066_swk_basefill_071'] = {'inputs': ['swk_basefill_071'], 'func': swk_base_universe_d2_066_swk_basefill_071}


def swk_base_universe_d2_067_swk_basefill_072(swk_basefill_072):
    return _base_universe_d2(swk_basefill_072, 67)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_067_swk_basefill_072'] = {'inputs': ['swk_basefill_072'], 'func': swk_base_universe_d2_067_swk_basefill_072}


def swk_base_universe_d2_068_swk_basefill_073(swk_basefill_073):
    return _base_universe_d2(swk_basefill_073, 68)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_068_swk_basefill_073'] = {'inputs': ['swk_basefill_073'], 'func': swk_base_universe_d2_068_swk_basefill_073}


def swk_base_universe_d2_069_swk_basefill_074(swk_basefill_074):
    return _base_universe_d2(swk_basefill_074, 69)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_069_swk_basefill_074'] = {'inputs': ['swk_basefill_074'], 'func': swk_base_universe_d2_069_swk_basefill_074}


def swk_base_universe_d2_070_swk_basefill_075(swk_basefill_075):
    return _base_universe_d2(swk_basefill_075, 70)
SWK_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['swk_base_universe_d2_070_swk_basefill_075'] = {'inputs': ['swk_basefill_075'], 'func': swk_base_universe_d2_070_swk_basefill_075}
