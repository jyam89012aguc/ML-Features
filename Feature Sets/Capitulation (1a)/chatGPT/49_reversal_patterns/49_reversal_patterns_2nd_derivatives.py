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



def rev_151_rev_001_gap_down_frequency_5_001_roc_1(rev_001_gap_down_frequency_5_001):
    feature = _s(rev_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def rev_152_rev_007_gap_down_frequency_126_007_roc_5(rev_007_gap_down_frequency_126_007):
    feature = _s(rev_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def rev_153_rev_013_gap_down_frequency_1008_013_roc_42(rev_013_gap_down_frequency_1008_013):
    feature = _s(rev_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def rev_154_rev_019_gap_down_frequency_42_019_roc_126(rev_019_gap_down_frequency_42_019):
    feature = _s(rev_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def rev_155_rev_025_gap_down_frequency_378_025_roc_378(rev_025_gap_down_frequency_378_025):
    feature = _s(rev_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















REVERSAL_PATTERNS_REGISTRY_2ND_DERIVATIVES = {
    'rev_151_rev_001_gap_down_frequency_5_001_roc_1': {'inputs': ['rev_001_gap_down_frequency_5_001'], 'func': rev_151_rev_001_gap_down_frequency_5_001_roc_1},
    'rev_152_rev_007_gap_down_frequency_126_007_roc_5': {'inputs': ['rev_007_gap_down_frequency_126_007'], 'func': rev_152_rev_007_gap_down_frequency_126_007_roc_5},
    'rev_153_rev_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['rev_013_gap_down_frequency_1008_013'], 'func': rev_153_rev_013_gap_down_frequency_1008_013_roc_42},
    'rev_154_rev_019_gap_down_frequency_42_019_roc_126': {'inputs': ['rev_019_gap_down_frequency_42_019'], 'func': rev_154_rev_019_gap_down_frequency_42_019_roc_126},
    'rev_155_rev_025_gap_down_frequency_378_025_roc_378': {'inputs': ['rev_025_gap_down_frequency_378_025'], 'func': rev_155_rev_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def rp_replacement_d2_001(rp_replacement_001):
    feature = _clean(rp_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_001'] = {'inputs': ['rp_replacement_001'], 'func': rp_replacement_d2_001}


def rp_replacement_d2_002(rp_replacement_002):
    feature = _clean(rp_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_002'] = {'inputs': ['rp_replacement_002'], 'func': rp_replacement_d2_002}


def rp_replacement_d2_003(rp_replacement_003):
    feature = _clean(rp_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_003'] = {'inputs': ['rp_replacement_003'], 'func': rp_replacement_d2_003}


def rp_replacement_d2_004(rp_replacement_004):
    feature = _clean(rp_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_004'] = {'inputs': ['rp_replacement_004'], 'func': rp_replacement_d2_004}


def rp_replacement_d2_005(rp_replacement_005):
    feature = _clean(rp_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_005'] = {'inputs': ['rp_replacement_005'], 'func': rp_replacement_d2_005}


def rp_replacement_d2_006(rp_replacement_006):
    feature = _clean(rp_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_006'] = {'inputs': ['rp_replacement_006'], 'func': rp_replacement_d2_006}


def rp_replacement_d2_007(rp_replacement_007):
    feature = _clean(rp_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_007'] = {'inputs': ['rp_replacement_007'], 'func': rp_replacement_d2_007}


def rp_replacement_d2_008(rp_replacement_008):
    feature = _clean(rp_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_008'] = {'inputs': ['rp_replacement_008'], 'func': rp_replacement_d2_008}


def rp_replacement_d2_009(rp_replacement_009):
    feature = _clean(rp_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_009'] = {'inputs': ['rp_replacement_009'], 'func': rp_replacement_d2_009}


def rp_replacement_d2_010(rp_replacement_010):
    feature = _clean(rp_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_010'] = {'inputs': ['rp_replacement_010'], 'func': rp_replacement_d2_010}


def rp_replacement_d2_011(rp_replacement_011):
    feature = _clean(rp_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_011'] = {'inputs': ['rp_replacement_011'], 'func': rp_replacement_d2_011}


def rp_replacement_d2_012(rp_replacement_012):
    feature = _clean(rp_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_012'] = {'inputs': ['rp_replacement_012'], 'func': rp_replacement_d2_012}


def rp_replacement_d2_013(rp_replacement_013):
    feature = _clean(rp_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_013'] = {'inputs': ['rp_replacement_013'], 'func': rp_replacement_d2_013}


def rp_replacement_d2_014(rp_replacement_014):
    feature = _clean(rp_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_014'] = {'inputs': ['rp_replacement_014'], 'func': rp_replacement_d2_014}


def rp_replacement_d2_015(rp_replacement_015):
    feature = _clean(rp_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_015'] = {'inputs': ['rp_replacement_015'], 'func': rp_replacement_d2_015}


def rp_replacement_d2_016(rp_replacement_016):
    feature = _clean(rp_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_016'] = {'inputs': ['rp_replacement_016'], 'func': rp_replacement_d2_016}


def rp_replacement_d2_017(rp_replacement_017):
    feature = _clean(rp_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_017'] = {'inputs': ['rp_replacement_017'], 'func': rp_replacement_d2_017}


def rp_replacement_d2_018(rp_replacement_018):
    feature = _clean(rp_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_018'] = {'inputs': ['rp_replacement_018'], 'func': rp_replacement_d2_018}


def rp_replacement_d2_019(rp_replacement_019):
    feature = _clean(rp_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_019'] = {'inputs': ['rp_replacement_019'], 'func': rp_replacement_d2_019}


def rp_replacement_d2_020(rp_replacement_020):
    feature = _clean(rp_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_020'] = {'inputs': ['rp_replacement_020'], 'func': rp_replacement_d2_020}


def rp_replacement_d2_021(rp_replacement_021):
    feature = _clean(rp_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_021'] = {'inputs': ['rp_replacement_021'], 'func': rp_replacement_d2_021}


def rp_replacement_d2_022(rp_replacement_022):
    feature = _clean(rp_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_022'] = {'inputs': ['rp_replacement_022'], 'func': rp_replacement_d2_022}


def rp_replacement_d2_023(rp_replacement_023):
    feature = _clean(rp_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_023'] = {'inputs': ['rp_replacement_023'], 'func': rp_replacement_d2_023}


def rp_replacement_d2_024(rp_replacement_024):
    feature = _clean(rp_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_024'] = {'inputs': ['rp_replacement_024'], 'func': rp_replacement_d2_024}


def rp_replacement_d2_025(rp_replacement_025):
    feature = _clean(rp_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_025'] = {'inputs': ['rp_replacement_025'], 'func': rp_replacement_d2_025}


def rp_replacement_d2_026(rp_replacement_026):
    feature = _clean(rp_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_026'] = {'inputs': ['rp_replacement_026'], 'func': rp_replacement_d2_026}


def rp_replacement_d2_027(rp_replacement_027):
    feature = _clean(rp_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_027'] = {'inputs': ['rp_replacement_027'], 'func': rp_replacement_d2_027}


def rp_replacement_d2_028(rp_replacement_028):
    feature = _clean(rp_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_028'] = {'inputs': ['rp_replacement_028'], 'func': rp_replacement_d2_028}


def rp_replacement_d2_029(rp_replacement_029):
    feature = _clean(rp_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_029'] = {'inputs': ['rp_replacement_029'], 'func': rp_replacement_d2_029}


def rp_replacement_d2_030(rp_replacement_030):
    feature = _clean(rp_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_030'] = {'inputs': ['rp_replacement_030'], 'func': rp_replacement_d2_030}


def rp_replacement_d2_031(rp_replacement_031):
    feature = _clean(rp_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_031'] = {'inputs': ['rp_replacement_031'], 'func': rp_replacement_d2_031}


def rp_replacement_d2_032(rp_replacement_032):
    feature = _clean(rp_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_032'] = {'inputs': ['rp_replacement_032'], 'func': rp_replacement_d2_032}


def rp_replacement_d2_033(rp_replacement_033):
    feature = _clean(rp_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_033'] = {'inputs': ['rp_replacement_033'], 'func': rp_replacement_d2_033}


def rp_replacement_d2_034(rp_replacement_034):
    feature = _clean(rp_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_034'] = {'inputs': ['rp_replacement_034'], 'func': rp_replacement_d2_034}


def rp_replacement_d2_035(rp_replacement_035):
    feature = _clean(rp_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_035'] = {'inputs': ['rp_replacement_035'], 'func': rp_replacement_d2_035}


def rp_replacement_d2_036(rp_replacement_036):
    feature = _clean(rp_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_036'] = {'inputs': ['rp_replacement_036'], 'func': rp_replacement_d2_036}


def rp_replacement_d2_037(rp_replacement_037):
    feature = _clean(rp_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_037'] = {'inputs': ['rp_replacement_037'], 'func': rp_replacement_d2_037}


def rp_replacement_d2_038(rp_replacement_038):
    feature = _clean(rp_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_038'] = {'inputs': ['rp_replacement_038'], 'func': rp_replacement_d2_038}


def rp_replacement_d2_039(rp_replacement_039):
    feature = _clean(rp_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_039'] = {'inputs': ['rp_replacement_039'], 'func': rp_replacement_d2_039}


def rp_replacement_d2_040(rp_replacement_040):
    feature = _clean(rp_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_040'] = {'inputs': ['rp_replacement_040'], 'func': rp_replacement_d2_040}


def rp_replacement_d2_041(rp_replacement_041):
    feature = _clean(rp_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_041'] = {'inputs': ['rp_replacement_041'], 'func': rp_replacement_d2_041}


def rp_replacement_d2_042(rp_replacement_042):
    feature = _clean(rp_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_042'] = {'inputs': ['rp_replacement_042'], 'func': rp_replacement_d2_042}


def rp_replacement_d2_043(rp_replacement_043):
    feature = _clean(rp_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_043'] = {'inputs': ['rp_replacement_043'], 'func': rp_replacement_d2_043}


def rp_replacement_d2_044(rp_replacement_044):
    feature = _clean(rp_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_044'] = {'inputs': ['rp_replacement_044'], 'func': rp_replacement_d2_044}


def rp_replacement_d2_045(rp_replacement_045):
    feature = _clean(rp_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_045'] = {'inputs': ['rp_replacement_045'], 'func': rp_replacement_d2_045}


def rp_replacement_d2_046(rp_replacement_046):
    feature = _clean(rp_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_046'] = {'inputs': ['rp_replacement_046'], 'func': rp_replacement_d2_046}


def rp_replacement_d2_047(rp_replacement_047):
    feature = _clean(rp_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_047'] = {'inputs': ['rp_replacement_047'], 'func': rp_replacement_d2_047}


def rp_replacement_d2_048(rp_replacement_048):
    feature = _clean(rp_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_048'] = {'inputs': ['rp_replacement_048'], 'func': rp_replacement_d2_048}


def rp_replacement_d2_049(rp_replacement_049):
    feature = _clean(rp_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_049'] = {'inputs': ['rp_replacement_049'], 'func': rp_replacement_d2_049}


def rp_replacement_d2_050(rp_replacement_050):
    feature = _clean(rp_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_050'] = {'inputs': ['rp_replacement_050'], 'func': rp_replacement_d2_050}


def rp_replacement_d2_051(rp_replacement_051):
    feature = _clean(rp_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_051'] = {'inputs': ['rp_replacement_051'], 'func': rp_replacement_d2_051}


def rp_replacement_d2_052(rp_replacement_052):
    feature = _clean(rp_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_052'] = {'inputs': ['rp_replacement_052'], 'func': rp_replacement_d2_052}


def rp_replacement_d2_053(rp_replacement_053):
    feature = _clean(rp_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_053'] = {'inputs': ['rp_replacement_053'], 'func': rp_replacement_d2_053}


def rp_replacement_d2_054(rp_replacement_054):
    feature = _clean(rp_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_054'] = {'inputs': ['rp_replacement_054'], 'func': rp_replacement_d2_054}


def rp_replacement_d2_055(rp_replacement_055):
    feature = _clean(rp_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_055'] = {'inputs': ['rp_replacement_055'], 'func': rp_replacement_d2_055}


def rp_replacement_d2_056(rp_replacement_056):
    feature = _clean(rp_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_056'] = {'inputs': ['rp_replacement_056'], 'func': rp_replacement_d2_056}


def rp_replacement_d2_057(rp_replacement_057):
    feature = _clean(rp_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_057'] = {'inputs': ['rp_replacement_057'], 'func': rp_replacement_d2_057}


def rp_replacement_d2_058(rp_replacement_058):
    feature = _clean(rp_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_058'] = {'inputs': ['rp_replacement_058'], 'func': rp_replacement_d2_058}


def rp_replacement_d2_059(rp_replacement_059):
    feature = _clean(rp_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_059'] = {'inputs': ['rp_replacement_059'], 'func': rp_replacement_d2_059}


def rp_replacement_d2_060(rp_replacement_060):
    feature = _clean(rp_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_060'] = {'inputs': ['rp_replacement_060'], 'func': rp_replacement_d2_060}


def rp_replacement_d2_061(rp_replacement_061):
    feature = _clean(rp_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_061'] = {'inputs': ['rp_replacement_061'], 'func': rp_replacement_d2_061}


def rp_replacement_d2_062(rp_replacement_062):
    feature = _clean(rp_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_062'] = {'inputs': ['rp_replacement_062'], 'func': rp_replacement_d2_062}


def rp_replacement_d2_063(rp_replacement_063):
    feature = _clean(rp_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_063'] = {'inputs': ['rp_replacement_063'], 'func': rp_replacement_d2_063}


def rp_replacement_d2_064(rp_replacement_064):
    feature = _clean(rp_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_064'] = {'inputs': ['rp_replacement_064'], 'func': rp_replacement_d2_064}


def rp_replacement_d2_065(rp_replacement_065):
    feature = _clean(rp_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_065'] = {'inputs': ['rp_replacement_065'], 'func': rp_replacement_d2_065}


def rp_replacement_d2_066(rp_replacement_066):
    feature = _clean(rp_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_066'] = {'inputs': ['rp_replacement_066'], 'func': rp_replacement_d2_066}


def rp_replacement_d2_067(rp_replacement_067):
    feature = _clean(rp_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_067'] = {'inputs': ['rp_replacement_067'], 'func': rp_replacement_d2_067}


def rp_replacement_d2_068(rp_replacement_068):
    feature = _clean(rp_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_068'] = {'inputs': ['rp_replacement_068'], 'func': rp_replacement_d2_068}


def rp_replacement_d2_069(rp_replacement_069):
    feature = _clean(rp_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_069'] = {'inputs': ['rp_replacement_069'], 'func': rp_replacement_d2_069}


def rp_replacement_d2_070(rp_replacement_070):
    feature = _clean(rp_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_070'] = {'inputs': ['rp_replacement_070'], 'func': rp_replacement_d2_070}


def rp_replacement_d2_071(rp_replacement_071):
    feature = _clean(rp_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_071'] = {'inputs': ['rp_replacement_071'], 'func': rp_replacement_d2_071}


def rp_replacement_d2_072(rp_replacement_072):
    feature = _clean(rp_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_072'] = {'inputs': ['rp_replacement_072'], 'func': rp_replacement_d2_072}


def rp_replacement_d2_073(rp_replacement_073):
    feature = _clean(rp_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_073'] = {'inputs': ['rp_replacement_073'], 'func': rp_replacement_d2_073}


def rp_replacement_d2_074(rp_replacement_074):
    feature = _clean(rp_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_074'] = {'inputs': ['rp_replacement_074'], 'func': rp_replacement_d2_074}


def rp_replacement_d2_075(rp_replacement_075):
    feature = _clean(rp_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_075'] = {'inputs': ['rp_replacement_075'], 'func': rp_replacement_d2_075}


def rp_replacement_d2_076(rp_replacement_076):
    feature = _clean(rp_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_076'] = {'inputs': ['rp_replacement_076'], 'func': rp_replacement_d2_076}


def rp_replacement_d2_077(rp_replacement_077):
    feature = _clean(rp_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_077'] = {'inputs': ['rp_replacement_077'], 'func': rp_replacement_d2_077}


def rp_replacement_d2_078(rp_replacement_078):
    feature = _clean(rp_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_078'] = {'inputs': ['rp_replacement_078'], 'func': rp_replacement_d2_078}


def rp_replacement_d2_079(rp_replacement_079):
    feature = _clean(rp_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_079'] = {'inputs': ['rp_replacement_079'], 'func': rp_replacement_d2_079}


def rp_replacement_d2_080(rp_replacement_080):
    feature = _clean(rp_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_080'] = {'inputs': ['rp_replacement_080'], 'func': rp_replacement_d2_080}


def rp_replacement_d2_081(rp_replacement_081):
    feature = _clean(rp_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_081'] = {'inputs': ['rp_replacement_081'], 'func': rp_replacement_d2_081}


def rp_replacement_d2_082(rp_replacement_082):
    feature = _clean(rp_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_082'] = {'inputs': ['rp_replacement_082'], 'func': rp_replacement_d2_082}


def rp_replacement_d2_083(rp_replacement_083):
    feature = _clean(rp_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_083'] = {'inputs': ['rp_replacement_083'], 'func': rp_replacement_d2_083}


def rp_replacement_d2_084(rp_replacement_084):
    feature = _clean(rp_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_084'] = {'inputs': ['rp_replacement_084'], 'func': rp_replacement_d2_084}


def rp_replacement_d2_085(rp_replacement_085):
    feature = _clean(rp_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_085'] = {'inputs': ['rp_replacement_085'], 'func': rp_replacement_d2_085}


def rp_replacement_d2_086(rp_replacement_086):
    feature = _clean(rp_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_086'] = {'inputs': ['rp_replacement_086'], 'func': rp_replacement_d2_086}


def rp_replacement_d2_087(rp_replacement_087):
    feature = _clean(rp_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_087'] = {'inputs': ['rp_replacement_087'], 'func': rp_replacement_d2_087}


def rp_replacement_d2_088(rp_replacement_088):
    feature = _clean(rp_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_088'] = {'inputs': ['rp_replacement_088'], 'func': rp_replacement_d2_088}


def rp_replacement_d2_089(rp_replacement_089):
    feature = _clean(rp_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_089'] = {'inputs': ['rp_replacement_089'], 'func': rp_replacement_d2_089}


def rp_replacement_d2_090(rp_replacement_090):
    feature = _clean(rp_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_090'] = {'inputs': ['rp_replacement_090'], 'func': rp_replacement_d2_090}


def rp_replacement_d2_091(rp_replacement_091):
    feature = _clean(rp_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_091'] = {'inputs': ['rp_replacement_091'], 'func': rp_replacement_d2_091}


def rp_replacement_d2_092(rp_replacement_092):
    feature = _clean(rp_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_092'] = {'inputs': ['rp_replacement_092'], 'func': rp_replacement_d2_092}


def rp_replacement_d2_093(rp_replacement_093):
    feature = _clean(rp_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_093'] = {'inputs': ['rp_replacement_093'], 'func': rp_replacement_d2_093}


def rp_replacement_d2_094(rp_replacement_094):
    feature = _clean(rp_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_094'] = {'inputs': ['rp_replacement_094'], 'func': rp_replacement_d2_094}


def rp_replacement_d2_095(rp_replacement_095):
    feature = _clean(rp_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_095'] = {'inputs': ['rp_replacement_095'], 'func': rp_replacement_d2_095}


def rp_replacement_d2_096(rp_replacement_096):
    feature = _clean(rp_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_096'] = {'inputs': ['rp_replacement_096'], 'func': rp_replacement_d2_096}


def rp_replacement_d2_097(rp_replacement_097):
    feature = _clean(rp_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_097'] = {'inputs': ['rp_replacement_097'], 'func': rp_replacement_d2_097}


def rp_replacement_d2_098(rp_replacement_098):
    feature = _clean(rp_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_098'] = {'inputs': ['rp_replacement_098'], 'func': rp_replacement_d2_098}


def rp_replacement_d2_099(rp_replacement_099):
    feature = _clean(rp_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_099'] = {'inputs': ['rp_replacement_099'], 'func': rp_replacement_d2_099}


def rp_replacement_d2_100(rp_replacement_100):
    feature = _clean(rp_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_100'] = {'inputs': ['rp_replacement_100'], 'func': rp_replacement_d2_100}


def rp_replacement_d2_101(rp_replacement_101):
    feature = _clean(rp_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_101'] = {'inputs': ['rp_replacement_101'], 'func': rp_replacement_d2_101}


def rp_replacement_d2_102(rp_replacement_102):
    feature = _clean(rp_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_102'] = {'inputs': ['rp_replacement_102'], 'func': rp_replacement_d2_102}


def rp_replacement_d2_103(rp_replacement_103):
    feature = _clean(rp_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_103'] = {'inputs': ['rp_replacement_103'], 'func': rp_replacement_d2_103}


def rp_replacement_d2_104(rp_replacement_104):
    feature = _clean(rp_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_104'] = {'inputs': ['rp_replacement_104'], 'func': rp_replacement_d2_104}


def rp_replacement_d2_105(rp_replacement_105):
    feature = _clean(rp_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_105'] = {'inputs': ['rp_replacement_105'], 'func': rp_replacement_d2_105}


def rp_replacement_d2_106(rp_replacement_106):
    feature = _clean(rp_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_106'] = {'inputs': ['rp_replacement_106'], 'func': rp_replacement_d2_106}


def rp_replacement_d2_107(rp_replacement_107):
    feature = _clean(rp_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_107'] = {'inputs': ['rp_replacement_107'], 'func': rp_replacement_d2_107}


def rp_replacement_d2_108(rp_replacement_108):
    feature = _clean(rp_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_108'] = {'inputs': ['rp_replacement_108'], 'func': rp_replacement_d2_108}


def rp_replacement_d2_109(rp_replacement_109):
    feature = _clean(rp_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_109'] = {'inputs': ['rp_replacement_109'], 'func': rp_replacement_d2_109}


def rp_replacement_d2_110(rp_replacement_110):
    feature = _clean(rp_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_110'] = {'inputs': ['rp_replacement_110'], 'func': rp_replacement_d2_110}


def rp_replacement_d2_111(rp_replacement_111):
    feature = _clean(rp_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_111'] = {'inputs': ['rp_replacement_111'], 'func': rp_replacement_d2_111}


def rp_replacement_d2_112(rp_replacement_112):
    feature = _clean(rp_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_112'] = {'inputs': ['rp_replacement_112'], 'func': rp_replacement_d2_112}


def rp_replacement_d2_113(rp_replacement_113):
    feature = _clean(rp_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_113'] = {'inputs': ['rp_replacement_113'], 'func': rp_replacement_d2_113}


def rp_replacement_d2_114(rp_replacement_114):
    feature = _clean(rp_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_114'] = {'inputs': ['rp_replacement_114'], 'func': rp_replacement_d2_114}


def rp_replacement_d2_115(rp_replacement_115):
    feature = _clean(rp_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_115'] = {'inputs': ['rp_replacement_115'], 'func': rp_replacement_d2_115}


def rp_replacement_d2_116(rp_replacement_116):
    feature = _clean(rp_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_116'] = {'inputs': ['rp_replacement_116'], 'func': rp_replacement_d2_116}


def rp_replacement_d2_117(rp_replacement_117):
    feature = _clean(rp_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_117'] = {'inputs': ['rp_replacement_117'], 'func': rp_replacement_d2_117}


def rp_replacement_d2_118(rp_replacement_118):
    feature = _clean(rp_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_118'] = {'inputs': ['rp_replacement_118'], 'func': rp_replacement_d2_118}


def rp_replacement_d2_119(rp_replacement_119):
    feature = _clean(rp_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_119'] = {'inputs': ['rp_replacement_119'], 'func': rp_replacement_d2_119}


def rp_replacement_d2_120(rp_replacement_120):
    feature = _clean(rp_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_120'] = {'inputs': ['rp_replacement_120'], 'func': rp_replacement_d2_120}


def rp_replacement_d2_121(rp_replacement_121):
    feature = _clean(rp_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_121'] = {'inputs': ['rp_replacement_121'], 'func': rp_replacement_d2_121}


def rp_replacement_d2_122(rp_replacement_122):
    feature = _clean(rp_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_122'] = {'inputs': ['rp_replacement_122'], 'func': rp_replacement_d2_122}


def rp_replacement_d2_123(rp_replacement_123):
    feature = _clean(rp_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_123'] = {'inputs': ['rp_replacement_123'], 'func': rp_replacement_d2_123}


def rp_replacement_d2_124(rp_replacement_124):
    feature = _clean(rp_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_124'] = {'inputs': ['rp_replacement_124'], 'func': rp_replacement_d2_124}


def rp_replacement_d2_125(rp_replacement_125):
    feature = _clean(rp_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_125'] = {'inputs': ['rp_replacement_125'], 'func': rp_replacement_d2_125}


def rp_replacement_d2_126(rp_replacement_126):
    feature = _clean(rp_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_126'] = {'inputs': ['rp_replacement_126'], 'func': rp_replacement_d2_126}


def rp_replacement_d2_127(rp_replacement_127):
    feature = _clean(rp_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_127'] = {'inputs': ['rp_replacement_127'], 'func': rp_replacement_d2_127}


def rp_replacement_d2_128(rp_replacement_128):
    feature = _clean(rp_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_128'] = {'inputs': ['rp_replacement_128'], 'func': rp_replacement_d2_128}


def rp_replacement_d2_129(rp_replacement_129):
    feature = _clean(rp_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_129'] = {'inputs': ['rp_replacement_129'], 'func': rp_replacement_d2_129}


def rp_replacement_d2_130(rp_replacement_130):
    feature = _clean(rp_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_130'] = {'inputs': ['rp_replacement_130'], 'func': rp_replacement_d2_130}


def rp_replacement_d2_131(rp_replacement_131):
    feature = _clean(rp_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_131'] = {'inputs': ['rp_replacement_131'], 'func': rp_replacement_d2_131}


def rp_replacement_d2_132(rp_replacement_132):
    feature = _clean(rp_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_132'] = {'inputs': ['rp_replacement_132'], 'func': rp_replacement_d2_132}


def rp_replacement_d2_133(rp_replacement_133):
    feature = _clean(rp_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_133'] = {'inputs': ['rp_replacement_133'], 'func': rp_replacement_d2_133}


def rp_replacement_d2_134(rp_replacement_134):
    feature = _clean(rp_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_134'] = {'inputs': ['rp_replacement_134'], 'func': rp_replacement_d2_134}


def rp_replacement_d2_135(rp_replacement_135):
    feature = _clean(rp_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_135'] = {'inputs': ['rp_replacement_135'], 'func': rp_replacement_d2_135}


def rp_replacement_d2_136(rp_replacement_136):
    feature = _clean(rp_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_136'] = {'inputs': ['rp_replacement_136'], 'func': rp_replacement_d2_136}


def rp_replacement_d2_137(rp_replacement_137):
    feature = _clean(rp_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_137'] = {'inputs': ['rp_replacement_137'], 'func': rp_replacement_d2_137}


def rp_replacement_d2_138(rp_replacement_138):
    feature = _clean(rp_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_138'] = {'inputs': ['rp_replacement_138'], 'func': rp_replacement_d2_138}


def rp_replacement_d2_139(rp_replacement_139):
    feature = _clean(rp_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_139'] = {'inputs': ['rp_replacement_139'], 'func': rp_replacement_d2_139}


def rp_replacement_d2_140(rp_replacement_140):
    feature = _clean(rp_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_140'] = {'inputs': ['rp_replacement_140'], 'func': rp_replacement_d2_140}


def rp_replacement_d2_141(rp_replacement_141):
    feature = _clean(rp_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_141'] = {'inputs': ['rp_replacement_141'], 'func': rp_replacement_d2_141}


def rp_replacement_d2_142(rp_replacement_142):
    feature = _clean(rp_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_142'] = {'inputs': ['rp_replacement_142'], 'func': rp_replacement_d2_142}


def rp_replacement_d2_143(rp_replacement_143):
    feature = _clean(rp_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_143'] = {'inputs': ['rp_replacement_143'], 'func': rp_replacement_d2_143}


def rp_replacement_d2_144(rp_replacement_144):
    feature = _clean(rp_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_144'] = {'inputs': ['rp_replacement_144'], 'func': rp_replacement_d2_144}


def rp_replacement_d2_145(rp_replacement_145):
    feature = _clean(rp_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_145'] = {'inputs': ['rp_replacement_145'], 'func': rp_replacement_d2_145}


def rp_replacement_d2_146(rp_replacement_146):
    feature = _clean(rp_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_146'] = {'inputs': ['rp_replacement_146'], 'func': rp_replacement_d2_146}


def rp_replacement_d2_147(rp_replacement_147):
    feature = _clean(rp_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_147'] = {'inputs': ['rp_replacement_147'], 'func': rp_replacement_d2_147}


def rp_replacement_d2_148(rp_replacement_148):
    feature = _clean(rp_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_148'] = {'inputs': ['rp_replacement_148'], 'func': rp_replacement_d2_148}


def rp_replacement_d2_149(rp_replacement_149):
    feature = _clean(rp_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_149'] = {'inputs': ['rp_replacement_149'], 'func': rp_replacement_d2_149}


def rp_replacement_d2_150(rp_replacement_150):
    feature = _clean(rp_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_150'] = {'inputs': ['rp_replacement_150'], 'func': rp_replacement_d2_150}


def rp_replacement_d2_151(rp_replacement_151):
    feature = _clean(rp_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_151'] = {'inputs': ['rp_replacement_151'], 'func': rp_replacement_d2_151}


def rp_replacement_d2_152(rp_replacement_152):
    feature = _clean(rp_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_152'] = {'inputs': ['rp_replacement_152'], 'func': rp_replacement_d2_152}


def rp_replacement_d2_153(rp_replacement_153):
    feature = _clean(rp_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_153'] = {'inputs': ['rp_replacement_153'], 'func': rp_replacement_d2_153}


def rp_replacement_d2_154(rp_replacement_154):
    feature = _clean(rp_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_154'] = {'inputs': ['rp_replacement_154'], 'func': rp_replacement_d2_154}


def rp_replacement_d2_155(rp_replacement_155):
    feature = _clean(rp_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_155'] = {'inputs': ['rp_replacement_155'], 'func': rp_replacement_d2_155}


def rp_replacement_d2_156(rp_replacement_156):
    feature = _clean(rp_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_156'] = {'inputs': ['rp_replacement_156'], 'func': rp_replacement_d2_156}


def rp_replacement_d2_157(rp_replacement_157):
    feature = _clean(rp_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_157'] = {'inputs': ['rp_replacement_157'], 'func': rp_replacement_d2_157}


def rp_replacement_d2_158(rp_replacement_158):
    feature = _clean(rp_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_158'] = {'inputs': ['rp_replacement_158'], 'func': rp_replacement_d2_158}


def rp_replacement_d2_159(rp_replacement_159):
    feature = _clean(rp_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_159'] = {'inputs': ['rp_replacement_159'], 'func': rp_replacement_d2_159}


def rp_replacement_d2_160(rp_replacement_160):
    feature = _clean(rp_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
RP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rp_replacement_d2_160'] = {'inputs': ['rp_replacement_160'], 'func': rp_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rev_base_universe_d2_001_rev_002_gap_magnitude_10_002(rev_002_gap_magnitude_10_002):
    return _base_universe_d2(rev_002_gap_magnitude_10_002, 1)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_001_rev_002_gap_magnitude_10_002'] = {'inputs': ['rev_002_gap_magnitude_10_002'], 'func': rev_base_universe_d2_001_rev_002_gap_magnitude_10_002}


def rev_base_universe_d2_002_rev_003_open_close_pressure_21_003(rev_003_open_close_pressure_21_003):
    return _base_universe_d2(rev_003_open_close_pressure_21_003, 2)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_002_rev_003_open_close_pressure_21_003'] = {'inputs': ['rev_003_open_close_pressure_21_003'], 'func': rev_base_universe_d2_002_rev_003_open_close_pressure_21_003}


def rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004(rev_004_lower_wick_ratio_42_004):
    return _base_universe_d2(rev_004_lower_wick_ratio_42_004, 3)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004'] = {'inputs': ['rev_004_lower_wick_ratio_42_004'], 'func': rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004}


def rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005(rev_005_upper_wick_ratio_63_005):
    return _base_universe_d2(rev_005_upper_wick_ratio_63_005, 4)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005'] = {'inputs': ['rev_005_upper_wick_ratio_63_005'], 'func': rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005}


def rev_base_universe_d2_005_rev_006_body_to_range_84_006(rev_006_body_to_range_84_006):
    return _base_universe_d2(rev_006_body_to_range_84_006, 5)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_005_rev_006_body_to_range_84_006'] = {'inputs': ['rev_006_body_to_range_84_006'], 'func': rev_base_universe_d2_005_rev_006_body_to_range_84_006}


def rev_base_universe_d2_006_rev_008_gap_magnitude_189_008(rev_008_gap_magnitude_189_008):
    return _base_universe_d2(rev_008_gap_magnitude_189_008, 6)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_006_rev_008_gap_magnitude_189_008'] = {'inputs': ['rev_008_gap_magnitude_189_008'], 'func': rev_base_universe_d2_006_rev_008_gap_magnitude_189_008}


def rev_base_universe_d2_007_rev_009_open_close_pressure_252_009(rev_009_open_close_pressure_252_009):
    return _base_universe_d2(rev_009_open_close_pressure_252_009, 7)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_007_rev_009_open_close_pressure_252_009'] = {'inputs': ['rev_009_open_close_pressure_252_009'], 'func': rev_base_universe_d2_007_rev_009_open_close_pressure_252_009}


def rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010(rev_010_lower_wick_ratio_378_010):
    return _base_universe_d2(rev_010_lower_wick_ratio_378_010, 8)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010'] = {'inputs': ['rev_010_lower_wick_ratio_378_010'], 'func': rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010}


def rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011(rev_011_upper_wick_ratio_504_011):
    return _base_universe_d2(rev_011_upper_wick_ratio_504_011, 9)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011'] = {'inputs': ['rev_011_upper_wick_ratio_504_011'], 'func': rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011}


def rev_base_universe_d2_010_rev_012_body_to_range_756_012(rev_012_body_to_range_756_012):
    return _base_universe_d2(rev_012_body_to_range_756_012, 10)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_010_rev_012_body_to_range_756_012'] = {'inputs': ['rev_012_body_to_range_756_012'], 'func': rev_base_universe_d2_010_rev_012_body_to_range_756_012}


def rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014(rev_014_gap_magnitude_1260_014):
    return _base_universe_d2(rev_014_gap_magnitude_1260_014, 11)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014'] = {'inputs': ['rev_014_gap_magnitude_1260_014'], 'func': rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014}


def rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015(rev_015_open_close_pressure_1512_015):
    return _base_universe_d2(rev_015_open_close_pressure_1512_015, 12)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015'] = {'inputs': ['rev_015_open_close_pressure_1512_015'], 'func': rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015}


def rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016(rev_016_lower_wick_ratio_5_016):
    return _base_universe_d2(rev_016_lower_wick_ratio_5_016, 13)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016'] = {'inputs': ['rev_016_lower_wick_ratio_5_016'], 'func': rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016}


def rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017(rev_017_upper_wick_ratio_10_017):
    return _base_universe_d2(rev_017_upper_wick_ratio_10_017, 14)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017'] = {'inputs': ['rev_017_upper_wick_ratio_10_017'], 'func': rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017}


def rev_base_universe_d2_015_rev_018_body_to_range_21_018(rev_018_body_to_range_21_018):
    return _base_universe_d2(rev_018_body_to_range_21_018, 15)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_015_rev_018_body_to_range_21_018'] = {'inputs': ['rev_018_body_to_range_21_018'], 'func': rev_base_universe_d2_015_rev_018_body_to_range_21_018}


def rev_base_universe_d2_016_rev_020_gap_magnitude_63_020(rev_020_gap_magnitude_63_020):
    return _base_universe_d2(rev_020_gap_magnitude_63_020, 16)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_016_rev_020_gap_magnitude_63_020'] = {'inputs': ['rev_020_gap_magnitude_63_020'], 'func': rev_base_universe_d2_016_rev_020_gap_magnitude_63_020}


def rev_base_universe_d2_017_rev_021_open_close_pressure_84_021(rev_021_open_close_pressure_84_021):
    return _base_universe_d2(rev_021_open_close_pressure_84_021, 17)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_017_rev_021_open_close_pressure_84_021'] = {'inputs': ['rev_021_open_close_pressure_84_021'], 'func': rev_base_universe_d2_017_rev_021_open_close_pressure_84_021}


def rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022(rev_022_lower_wick_ratio_126_022):
    return _base_universe_d2(rev_022_lower_wick_ratio_126_022, 18)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022'] = {'inputs': ['rev_022_lower_wick_ratio_126_022'], 'func': rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022}


def rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023(rev_023_upper_wick_ratio_189_023):
    return _base_universe_d2(rev_023_upper_wick_ratio_189_023, 19)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023'] = {'inputs': ['rev_023_upper_wick_ratio_189_023'], 'func': rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023}


def rev_base_universe_d2_020_rev_024_body_to_range_252_024(rev_024_body_to_range_252_024):
    return _base_universe_d2(rev_024_body_to_range_252_024, 20)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_020_rev_024_body_to_range_252_024'] = {'inputs': ['rev_024_body_to_range_252_024'], 'func': rev_base_universe_d2_020_rev_024_body_to_range_252_024}


def rev_base_universe_d2_021_rev_026_gap_magnitude_504_026(rev_026_gap_magnitude_504_026):
    return _base_universe_d2(rev_026_gap_magnitude_504_026, 21)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_021_rev_026_gap_magnitude_504_026'] = {'inputs': ['rev_026_gap_magnitude_504_026'], 'func': rev_base_universe_d2_021_rev_026_gap_magnitude_504_026}


def rev_base_universe_d2_022_rev_027_open_close_pressure_756_027(rev_027_open_close_pressure_756_027):
    return _base_universe_d2(rev_027_open_close_pressure_756_027, 22)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_022_rev_027_open_close_pressure_756_027'] = {'inputs': ['rev_027_open_close_pressure_756_027'], 'func': rev_base_universe_d2_022_rev_027_open_close_pressure_756_027}


def rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028(rev_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(rev_028_lower_wick_ratio_1008_028, 23)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028'] = {'inputs': ['rev_028_lower_wick_ratio_1008_028'], 'func': rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028}


def rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029(rev_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(rev_029_upper_wick_ratio_1260_029, 24)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029'] = {'inputs': ['rev_029_upper_wick_ratio_1260_029'], 'func': rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029}


def rev_base_universe_d2_025_rev_030_body_to_range_1512_030(rev_030_body_to_range_1512_030):
    return _base_universe_d2(rev_030_body_to_range_1512_030, 25)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_025_rev_030_body_to_range_1512_030'] = {'inputs': ['rev_030_body_to_range_1512_030'], 'func': rev_base_universe_d2_025_rev_030_body_to_range_1512_030}


def rev_base_universe_d2_026_rev_basefill_031(rev_basefill_031):
    return _base_universe_d2(rev_basefill_031, 26)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_026_rev_basefill_031'] = {'inputs': ['rev_basefill_031'], 'func': rev_base_universe_d2_026_rev_basefill_031}


def rev_base_universe_d2_027_rev_basefill_032(rev_basefill_032):
    return _base_universe_d2(rev_basefill_032, 27)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_027_rev_basefill_032'] = {'inputs': ['rev_basefill_032'], 'func': rev_base_universe_d2_027_rev_basefill_032}


def rev_base_universe_d2_028_rev_basefill_033(rev_basefill_033):
    return _base_universe_d2(rev_basefill_033, 28)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_028_rev_basefill_033'] = {'inputs': ['rev_basefill_033'], 'func': rev_base_universe_d2_028_rev_basefill_033}


def rev_base_universe_d2_029_rev_basefill_034(rev_basefill_034):
    return _base_universe_d2(rev_basefill_034, 29)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_029_rev_basefill_034'] = {'inputs': ['rev_basefill_034'], 'func': rev_base_universe_d2_029_rev_basefill_034}


def rev_base_universe_d2_030_rev_basefill_035(rev_basefill_035):
    return _base_universe_d2(rev_basefill_035, 30)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_030_rev_basefill_035'] = {'inputs': ['rev_basefill_035'], 'func': rev_base_universe_d2_030_rev_basefill_035}


def rev_base_universe_d2_031_rev_basefill_036(rev_basefill_036):
    return _base_universe_d2(rev_basefill_036, 31)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_031_rev_basefill_036'] = {'inputs': ['rev_basefill_036'], 'func': rev_base_universe_d2_031_rev_basefill_036}


def rev_base_universe_d2_032_rev_basefill_037(rev_basefill_037):
    return _base_universe_d2(rev_basefill_037, 32)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_032_rev_basefill_037'] = {'inputs': ['rev_basefill_037'], 'func': rev_base_universe_d2_032_rev_basefill_037}


def rev_base_universe_d2_033_rev_basefill_038(rev_basefill_038):
    return _base_universe_d2(rev_basefill_038, 33)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_033_rev_basefill_038'] = {'inputs': ['rev_basefill_038'], 'func': rev_base_universe_d2_033_rev_basefill_038}


def rev_base_universe_d2_034_rev_basefill_039(rev_basefill_039):
    return _base_universe_d2(rev_basefill_039, 34)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_034_rev_basefill_039'] = {'inputs': ['rev_basefill_039'], 'func': rev_base_universe_d2_034_rev_basefill_039}


def rev_base_universe_d2_035_rev_basefill_040(rev_basefill_040):
    return _base_universe_d2(rev_basefill_040, 35)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_035_rev_basefill_040'] = {'inputs': ['rev_basefill_040'], 'func': rev_base_universe_d2_035_rev_basefill_040}


def rev_base_universe_d2_036_rev_basefill_041(rev_basefill_041):
    return _base_universe_d2(rev_basefill_041, 36)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_036_rev_basefill_041'] = {'inputs': ['rev_basefill_041'], 'func': rev_base_universe_d2_036_rev_basefill_041}


def rev_base_universe_d2_037_rev_basefill_042(rev_basefill_042):
    return _base_universe_d2(rev_basefill_042, 37)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_037_rev_basefill_042'] = {'inputs': ['rev_basefill_042'], 'func': rev_base_universe_d2_037_rev_basefill_042}


def rev_base_universe_d2_038_rev_basefill_043(rev_basefill_043):
    return _base_universe_d2(rev_basefill_043, 38)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_038_rev_basefill_043'] = {'inputs': ['rev_basefill_043'], 'func': rev_base_universe_d2_038_rev_basefill_043}


def rev_base_universe_d2_039_rev_basefill_044(rev_basefill_044):
    return _base_universe_d2(rev_basefill_044, 39)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_039_rev_basefill_044'] = {'inputs': ['rev_basefill_044'], 'func': rev_base_universe_d2_039_rev_basefill_044}


def rev_base_universe_d2_040_rev_basefill_045(rev_basefill_045):
    return _base_universe_d2(rev_basefill_045, 40)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_040_rev_basefill_045'] = {'inputs': ['rev_basefill_045'], 'func': rev_base_universe_d2_040_rev_basefill_045}


def rev_base_universe_d2_041_rev_basefill_046(rev_basefill_046):
    return _base_universe_d2(rev_basefill_046, 41)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_041_rev_basefill_046'] = {'inputs': ['rev_basefill_046'], 'func': rev_base_universe_d2_041_rev_basefill_046}


def rev_base_universe_d2_042_rev_basefill_047(rev_basefill_047):
    return _base_universe_d2(rev_basefill_047, 42)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_042_rev_basefill_047'] = {'inputs': ['rev_basefill_047'], 'func': rev_base_universe_d2_042_rev_basefill_047}


def rev_base_universe_d2_043_rev_basefill_048(rev_basefill_048):
    return _base_universe_d2(rev_basefill_048, 43)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_043_rev_basefill_048'] = {'inputs': ['rev_basefill_048'], 'func': rev_base_universe_d2_043_rev_basefill_048}


def rev_base_universe_d2_044_rev_basefill_049(rev_basefill_049):
    return _base_universe_d2(rev_basefill_049, 44)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_044_rev_basefill_049'] = {'inputs': ['rev_basefill_049'], 'func': rev_base_universe_d2_044_rev_basefill_049}


def rev_base_universe_d2_045_rev_basefill_050(rev_basefill_050):
    return _base_universe_d2(rev_basefill_050, 45)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_045_rev_basefill_050'] = {'inputs': ['rev_basefill_050'], 'func': rev_base_universe_d2_045_rev_basefill_050}


def rev_base_universe_d2_046_rev_basefill_051(rev_basefill_051):
    return _base_universe_d2(rev_basefill_051, 46)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_046_rev_basefill_051'] = {'inputs': ['rev_basefill_051'], 'func': rev_base_universe_d2_046_rev_basefill_051}


def rev_base_universe_d2_047_rev_basefill_052(rev_basefill_052):
    return _base_universe_d2(rev_basefill_052, 47)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_047_rev_basefill_052'] = {'inputs': ['rev_basefill_052'], 'func': rev_base_universe_d2_047_rev_basefill_052}


def rev_base_universe_d2_048_rev_basefill_053(rev_basefill_053):
    return _base_universe_d2(rev_basefill_053, 48)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_048_rev_basefill_053'] = {'inputs': ['rev_basefill_053'], 'func': rev_base_universe_d2_048_rev_basefill_053}


def rev_base_universe_d2_049_rev_basefill_054(rev_basefill_054):
    return _base_universe_d2(rev_basefill_054, 49)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_049_rev_basefill_054'] = {'inputs': ['rev_basefill_054'], 'func': rev_base_universe_d2_049_rev_basefill_054}


def rev_base_universe_d2_050_rev_basefill_055(rev_basefill_055):
    return _base_universe_d2(rev_basefill_055, 50)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_050_rev_basefill_055'] = {'inputs': ['rev_basefill_055'], 'func': rev_base_universe_d2_050_rev_basefill_055}


def rev_base_universe_d2_051_rev_basefill_056(rev_basefill_056):
    return _base_universe_d2(rev_basefill_056, 51)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_051_rev_basefill_056'] = {'inputs': ['rev_basefill_056'], 'func': rev_base_universe_d2_051_rev_basefill_056}


def rev_base_universe_d2_052_rev_basefill_057(rev_basefill_057):
    return _base_universe_d2(rev_basefill_057, 52)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_052_rev_basefill_057'] = {'inputs': ['rev_basefill_057'], 'func': rev_base_universe_d2_052_rev_basefill_057}


def rev_base_universe_d2_053_rev_basefill_058(rev_basefill_058):
    return _base_universe_d2(rev_basefill_058, 53)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_053_rev_basefill_058'] = {'inputs': ['rev_basefill_058'], 'func': rev_base_universe_d2_053_rev_basefill_058}


def rev_base_universe_d2_054_rev_basefill_059(rev_basefill_059):
    return _base_universe_d2(rev_basefill_059, 54)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_054_rev_basefill_059'] = {'inputs': ['rev_basefill_059'], 'func': rev_base_universe_d2_054_rev_basefill_059}


def rev_base_universe_d2_055_rev_basefill_060(rev_basefill_060):
    return _base_universe_d2(rev_basefill_060, 55)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_055_rev_basefill_060'] = {'inputs': ['rev_basefill_060'], 'func': rev_base_universe_d2_055_rev_basefill_060}


def rev_base_universe_d2_056_rev_basefill_061(rev_basefill_061):
    return _base_universe_d2(rev_basefill_061, 56)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_056_rev_basefill_061'] = {'inputs': ['rev_basefill_061'], 'func': rev_base_universe_d2_056_rev_basefill_061}


def rev_base_universe_d2_057_rev_basefill_062(rev_basefill_062):
    return _base_universe_d2(rev_basefill_062, 57)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_057_rev_basefill_062'] = {'inputs': ['rev_basefill_062'], 'func': rev_base_universe_d2_057_rev_basefill_062}


def rev_base_universe_d2_058_rev_basefill_063(rev_basefill_063):
    return _base_universe_d2(rev_basefill_063, 58)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_058_rev_basefill_063'] = {'inputs': ['rev_basefill_063'], 'func': rev_base_universe_d2_058_rev_basefill_063}


def rev_base_universe_d2_059_rev_basefill_064(rev_basefill_064):
    return _base_universe_d2(rev_basefill_064, 59)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_059_rev_basefill_064'] = {'inputs': ['rev_basefill_064'], 'func': rev_base_universe_d2_059_rev_basefill_064}


def rev_base_universe_d2_060_rev_basefill_065(rev_basefill_065):
    return _base_universe_d2(rev_basefill_065, 60)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_060_rev_basefill_065'] = {'inputs': ['rev_basefill_065'], 'func': rev_base_universe_d2_060_rev_basefill_065}


def rev_base_universe_d2_061_rev_basefill_066(rev_basefill_066):
    return _base_universe_d2(rev_basefill_066, 61)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_061_rev_basefill_066'] = {'inputs': ['rev_basefill_066'], 'func': rev_base_universe_d2_061_rev_basefill_066}


def rev_base_universe_d2_062_rev_basefill_067(rev_basefill_067):
    return _base_universe_d2(rev_basefill_067, 62)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_062_rev_basefill_067'] = {'inputs': ['rev_basefill_067'], 'func': rev_base_universe_d2_062_rev_basefill_067}


def rev_base_universe_d2_063_rev_basefill_068(rev_basefill_068):
    return _base_universe_d2(rev_basefill_068, 63)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_063_rev_basefill_068'] = {'inputs': ['rev_basefill_068'], 'func': rev_base_universe_d2_063_rev_basefill_068}


def rev_base_universe_d2_064_rev_basefill_069(rev_basefill_069):
    return _base_universe_d2(rev_basefill_069, 64)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_064_rev_basefill_069'] = {'inputs': ['rev_basefill_069'], 'func': rev_base_universe_d2_064_rev_basefill_069}


def rev_base_universe_d2_065_rev_basefill_070(rev_basefill_070):
    return _base_universe_d2(rev_basefill_070, 65)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_065_rev_basefill_070'] = {'inputs': ['rev_basefill_070'], 'func': rev_base_universe_d2_065_rev_basefill_070}


def rev_base_universe_d2_066_rev_basefill_071(rev_basefill_071):
    return _base_universe_d2(rev_basefill_071, 66)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_066_rev_basefill_071'] = {'inputs': ['rev_basefill_071'], 'func': rev_base_universe_d2_066_rev_basefill_071}


def rev_base_universe_d2_067_rev_basefill_072(rev_basefill_072):
    return _base_universe_d2(rev_basefill_072, 67)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_067_rev_basefill_072'] = {'inputs': ['rev_basefill_072'], 'func': rev_base_universe_d2_067_rev_basefill_072}


def rev_base_universe_d2_068_rev_basefill_073(rev_basefill_073):
    return _base_universe_d2(rev_basefill_073, 68)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_068_rev_basefill_073'] = {'inputs': ['rev_basefill_073'], 'func': rev_base_universe_d2_068_rev_basefill_073}


def rev_base_universe_d2_069_rev_basefill_074(rev_basefill_074):
    return _base_universe_d2(rev_basefill_074, 69)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_069_rev_basefill_074'] = {'inputs': ['rev_basefill_074'], 'func': rev_base_universe_d2_069_rev_basefill_074}


def rev_base_universe_d2_070_rev_basefill_075(rev_basefill_075):
    return _base_universe_d2(rev_basefill_075, 70)
REV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rev_base_universe_d2_070_rev_basefill_075'] = {'inputs': ['rev_basefill_075'], 'func': rev_base_universe_d2_070_rev_basefill_075}
