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



def fbd_151_fbd_001_gap_down_frequency_5_001_roc_1(fbd_001_gap_down_frequency_5_001):
    feature = _s(fbd_001_gap_down_frequency_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def fbd_152_fbd_007_gap_down_frequency_126_007_roc_5(fbd_007_gap_down_frequency_126_007):
    feature = _s(fbd_007_gap_down_frequency_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42(fbd_013_gap_down_frequency_1008_013):
    feature = _s(fbd_013_gap_down_frequency_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def fbd_154_fbd_019_gap_down_frequency_42_019_roc_126(fbd_019_gap_down_frequency_42_019):
    feature = _s(fbd_019_gap_down_frequency_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def fbd_155_fbd_025_gap_down_frequency_378_025_roc_378(fbd_025_gap_down_frequency_378_025):
    feature = _s(fbd_025_gap_down_frequency_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















FAILED_BREAKDOWN_REGISTRY_2ND_DERIVATIVES = {
    'fbd_151_fbd_001_gap_down_frequency_5_001_roc_1': {'inputs': ['fbd_001_gap_down_frequency_5_001'], 'func': fbd_151_fbd_001_gap_down_frequency_5_001_roc_1},
    'fbd_152_fbd_007_gap_down_frequency_126_007_roc_5': {'inputs': ['fbd_007_gap_down_frequency_126_007'], 'func': fbd_152_fbd_007_gap_down_frequency_126_007_roc_5},
    'fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42': {'inputs': ['fbd_013_gap_down_frequency_1008_013'], 'func': fbd_153_fbd_013_gap_down_frequency_1008_013_roc_42},
    'fbd_154_fbd_019_gap_down_frequency_42_019_roc_126': {'inputs': ['fbd_019_gap_down_frequency_42_019'], 'func': fbd_154_fbd_019_gap_down_frequency_42_019_roc_126},
    'fbd_155_fbd_025_gap_down_frequency_378_025_roc_378': {'inputs': ['fbd_025_gap_down_frequency_378_025'], 'func': fbd_155_fbd_025_gap_down_frequency_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def fb_replacement_d2_001(fb_replacement_001):
    feature = _clean(fb_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_001'] = {'inputs': ['fb_replacement_001'], 'func': fb_replacement_d2_001}


def fb_replacement_d2_002(fb_replacement_002):
    feature = _clean(fb_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_002'] = {'inputs': ['fb_replacement_002'], 'func': fb_replacement_d2_002}


def fb_replacement_d2_003(fb_replacement_003):
    feature = _clean(fb_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_003'] = {'inputs': ['fb_replacement_003'], 'func': fb_replacement_d2_003}


def fb_replacement_d2_004(fb_replacement_004):
    feature = _clean(fb_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_004'] = {'inputs': ['fb_replacement_004'], 'func': fb_replacement_d2_004}


def fb_replacement_d2_005(fb_replacement_005):
    feature = _clean(fb_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_005'] = {'inputs': ['fb_replacement_005'], 'func': fb_replacement_d2_005}


def fb_replacement_d2_006(fb_replacement_006):
    feature = _clean(fb_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_006'] = {'inputs': ['fb_replacement_006'], 'func': fb_replacement_d2_006}


def fb_replacement_d2_007(fb_replacement_007):
    feature = _clean(fb_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_007'] = {'inputs': ['fb_replacement_007'], 'func': fb_replacement_d2_007}


def fb_replacement_d2_008(fb_replacement_008):
    feature = _clean(fb_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_008'] = {'inputs': ['fb_replacement_008'], 'func': fb_replacement_d2_008}


def fb_replacement_d2_009(fb_replacement_009):
    feature = _clean(fb_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_009'] = {'inputs': ['fb_replacement_009'], 'func': fb_replacement_d2_009}


def fb_replacement_d2_010(fb_replacement_010):
    feature = _clean(fb_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_010'] = {'inputs': ['fb_replacement_010'], 'func': fb_replacement_d2_010}


def fb_replacement_d2_011(fb_replacement_011):
    feature = _clean(fb_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_011'] = {'inputs': ['fb_replacement_011'], 'func': fb_replacement_d2_011}


def fb_replacement_d2_012(fb_replacement_012):
    feature = _clean(fb_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_012'] = {'inputs': ['fb_replacement_012'], 'func': fb_replacement_d2_012}


def fb_replacement_d2_013(fb_replacement_013):
    feature = _clean(fb_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_013'] = {'inputs': ['fb_replacement_013'], 'func': fb_replacement_d2_013}


def fb_replacement_d2_014(fb_replacement_014):
    feature = _clean(fb_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_014'] = {'inputs': ['fb_replacement_014'], 'func': fb_replacement_d2_014}


def fb_replacement_d2_015(fb_replacement_015):
    feature = _clean(fb_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_015'] = {'inputs': ['fb_replacement_015'], 'func': fb_replacement_d2_015}


def fb_replacement_d2_016(fb_replacement_016):
    feature = _clean(fb_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_016'] = {'inputs': ['fb_replacement_016'], 'func': fb_replacement_d2_016}


def fb_replacement_d2_017(fb_replacement_017):
    feature = _clean(fb_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_017'] = {'inputs': ['fb_replacement_017'], 'func': fb_replacement_d2_017}


def fb_replacement_d2_018(fb_replacement_018):
    feature = _clean(fb_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_018'] = {'inputs': ['fb_replacement_018'], 'func': fb_replacement_d2_018}


def fb_replacement_d2_019(fb_replacement_019):
    feature = _clean(fb_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_019'] = {'inputs': ['fb_replacement_019'], 'func': fb_replacement_d2_019}


def fb_replacement_d2_020(fb_replacement_020):
    feature = _clean(fb_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_020'] = {'inputs': ['fb_replacement_020'], 'func': fb_replacement_d2_020}


def fb_replacement_d2_021(fb_replacement_021):
    feature = _clean(fb_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_021'] = {'inputs': ['fb_replacement_021'], 'func': fb_replacement_d2_021}


def fb_replacement_d2_022(fb_replacement_022):
    feature = _clean(fb_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_022'] = {'inputs': ['fb_replacement_022'], 'func': fb_replacement_d2_022}


def fb_replacement_d2_023(fb_replacement_023):
    feature = _clean(fb_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_023'] = {'inputs': ['fb_replacement_023'], 'func': fb_replacement_d2_023}


def fb_replacement_d2_024(fb_replacement_024):
    feature = _clean(fb_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_024'] = {'inputs': ['fb_replacement_024'], 'func': fb_replacement_d2_024}


def fb_replacement_d2_025(fb_replacement_025):
    feature = _clean(fb_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_025'] = {'inputs': ['fb_replacement_025'], 'func': fb_replacement_d2_025}


def fb_replacement_d2_026(fb_replacement_026):
    feature = _clean(fb_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_026'] = {'inputs': ['fb_replacement_026'], 'func': fb_replacement_d2_026}


def fb_replacement_d2_027(fb_replacement_027):
    feature = _clean(fb_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_027'] = {'inputs': ['fb_replacement_027'], 'func': fb_replacement_d2_027}


def fb_replacement_d2_028(fb_replacement_028):
    feature = _clean(fb_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_028'] = {'inputs': ['fb_replacement_028'], 'func': fb_replacement_d2_028}


def fb_replacement_d2_029(fb_replacement_029):
    feature = _clean(fb_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_029'] = {'inputs': ['fb_replacement_029'], 'func': fb_replacement_d2_029}


def fb_replacement_d2_030(fb_replacement_030):
    feature = _clean(fb_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_030'] = {'inputs': ['fb_replacement_030'], 'func': fb_replacement_d2_030}


def fb_replacement_d2_031(fb_replacement_031):
    feature = _clean(fb_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_031'] = {'inputs': ['fb_replacement_031'], 'func': fb_replacement_d2_031}


def fb_replacement_d2_032(fb_replacement_032):
    feature = _clean(fb_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_032'] = {'inputs': ['fb_replacement_032'], 'func': fb_replacement_d2_032}


def fb_replacement_d2_033(fb_replacement_033):
    feature = _clean(fb_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_033'] = {'inputs': ['fb_replacement_033'], 'func': fb_replacement_d2_033}


def fb_replacement_d2_034(fb_replacement_034):
    feature = _clean(fb_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_034'] = {'inputs': ['fb_replacement_034'], 'func': fb_replacement_d2_034}


def fb_replacement_d2_035(fb_replacement_035):
    feature = _clean(fb_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_035'] = {'inputs': ['fb_replacement_035'], 'func': fb_replacement_d2_035}


def fb_replacement_d2_036(fb_replacement_036):
    feature = _clean(fb_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_036'] = {'inputs': ['fb_replacement_036'], 'func': fb_replacement_d2_036}


def fb_replacement_d2_037(fb_replacement_037):
    feature = _clean(fb_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_037'] = {'inputs': ['fb_replacement_037'], 'func': fb_replacement_d2_037}


def fb_replacement_d2_038(fb_replacement_038):
    feature = _clean(fb_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_038'] = {'inputs': ['fb_replacement_038'], 'func': fb_replacement_d2_038}


def fb_replacement_d2_039(fb_replacement_039):
    feature = _clean(fb_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_039'] = {'inputs': ['fb_replacement_039'], 'func': fb_replacement_d2_039}


def fb_replacement_d2_040(fb_replacement_040):
    feature = _clean(fb_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_040'] = {'inputs': ['fb_replacement_040'], 'func': fb_replacement_d2_040}


def fb_replacement_d2_041(fb_replacement_041):
    feature = _clean(fb_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_041'] = {'inputs': ['fb_replacement_041'], 'func': fb_replacement_d2_041}


def fb_replacement_d2_042(fb_replacement_042):
    feature = _clean(fb_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_042'] = {'inputs': ['fb_replacement_042'], 'func': fb_replacement_d2_042}


def fb_replacement_d2_043(fb_replacement_043):
    feature = _clean(fb_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_043'] = {'inputs': ['fb_replacement_043'], 'func': fb_replacement_d2_043}


def fb_replacement_d2_044(fb_replacement_044):
    feature = _clean(fb_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_044'] = {'inputs': ['fb_replacement_044'], 'func': fb_replacement_d2_044}


def fb_replacement_d2_045(fb_replacement_045):
    feature = _clean(fb_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_045'] = {'inputs': ['fb_replacement_045'], 'func': fb_replacement_d2_045}


def fb_replacement_d2_046(fb_replacement_046):
    feature = _clean(fb_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_046'] = {'inputs': ['fb_replacement_046'], 'func': fb_replacement_d2_046}


def fb_replacement_d2_047(fb_replacement_047):
    feature = _clean(fb_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_047'] = {'inputs': ['fb_replacement_047'], 'func': fb_replacement_d2_047}


def fb_replacement_d2_048(fb_replacement_048):
    feature = _clean(fb_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_048'] = {'inputs': ['fb_replacement_048'], 'func': fb_replacement_d2_048}


def fb_replacement_d2_049(fb_replacement_049):
    feature = _clean(fb_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_049'] = {'inputs': ['fb_replacement_049'], 'func': fb_replacement_d2_049}


def fb_replacement_d2_050(fb_replacement_050):
    feature = _clean(fb_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_050'] = {'inputs': ['fb_replacement_050'], 'func': fb_replacement_d2_050}


def fb_replacement_d2_051(fb_replacement_051):
    feature = _clean(fb_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_051'] = {'inputs': ['fb_replacement_051'], 'func': fb_replacement_d2_051}


def fb_replacement_d2_052(fb_replacement_052):
    feature = _clean(fb_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_052'] = {'inputs': ['fb_replacement_052'], 'func': fb_replacement_d2_052}


def fb_replacement_d2_053(fb_replacement_053):
    feature = _clean(fb_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_053'] = {'inputs': ['fb_replacement_053'], 'func': fb_replacement_d2_053}


def fb_replacement_d2_054(fb_replacement_054):
    feature = _clean(fb_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_054'] = {'inputs': ['fb_replacement_054'], 'func': fb_replacement_d2_054}


def fb_replacement_d2_055(fb_replacement_055):
    feature = _clean(fb_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_055'] = {'inputs': ['fb_replacement_055'], 'func': fb_replacement_d2_055}


def fb_replacement_d2_056(fb_replacement_056):
    feature = _clean(fb_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_056'] = {'inputs': ['fb_replacement_056'], 'func': fb_replacement_d2_056}


def fb_replacement_d2_057(fb_replacement_057):
    feature = _clean(fb_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_057'] = {'inputs': ['fb_replacement_057'], 'func': fb_replacement_d2_057}


def fb_replacement_d2_058(fb_replacement_058):
    feature = _clean(fb_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_058'] = {'inputs': ['fb_replacement_058'], 'func': fb_replacement_d2_058}


def fb_replacement_d2_059(fb_replacement_059):
    feature = _clean(fb_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_059'] = {'inputs': ['fb_replacement_059'], 'func': fb_replacement_d2_059}


def fb_replacement_d2_060(fb_replacement_060):
    feature = _clean(fb_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_060'] = {'inputs': ['fb_replacement_060'], 'func': fb_replacement_d2_060}


def fb_replacement_d2_061(fb_replacement_061):
    feature = _clean(fb_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_061'] = {'inputs': ['fb_replacement_061'], 'func': fb_replacement_d2_061}


def fb_replacement_d2_062(fb_replacement_062):
    feature = _clean(fb_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_062'] = {'inputs': ['fb_replacement_062'], 'func': fb_replacement_d2_062}


def fb_replacement_d2_063(fb_replacement_063):
    feature = _clean(fb_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_063'] = {'inputs': ['fb_replacement_063'], 'func': fb_replacement_d2_063}


def fb_replacement_d2_064(fb_replacement_064):
    feature = _clean(fb_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_064'] = {'inputs': ['fb_replacement_064'], 'func': fb_replacement_d2_064}


def fb_replacement_d2_065(fb_replacement_065):
    feature = _clean(fb_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_065'] = {'inputs': ['fb_replacement_065'], 'func': fb_replacement_d2_065}


def fb_replacement_d2_066(fb_replacement_066):
    feature = _clean(fb_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_066'] = {'inputs': ['fb_replacement_066'], 'func': fb_replacement_d2_066}


def fb_replacement_d2_067(fb_replacement_067):
    feature = _clean(fb_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_067'] = {'inputs': ['fb_replacement_067'], 'func': fb_replacement_d2_067}


def fb_replacement_d2_068(fb_replacement_068):
    feature = _clean(fb_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_068'] = {'inputs': ['fb_replacement_068'], 'func': fb_replacement_d2_068}


def fb_replacement_d2_069(fb_replacement_069):
    feature = _clean(fb_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_069'] = {'inputs': ['fb_replacement_069'], 'func': fb_replacement_d2_069}


def fb_replacement_d2_070(fb_replacement_070):
    feature = _clean(fb_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_070'] = {'inputs': ['fb_replacement_070'], 'func': fb_replacement_d2_070}


def fb_replacement_d2_071(fb_replacement_071):
    feature = _clean(fb_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_071'] = {'inputs': ['fb_replacement_071'], 'func': fb_replacement_d2_071}


def fb_replacement_d2_072(fb_replacement_072):
    feature = _clean(fb_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_072'] = {'inputs': ['fb_replacement_072'], 'func': fb_replacement_d2_072}


def fb_replacement_d2_073(fb_replacement_073):
    feature = _clean(fb_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_073'] = {'inputs': ['fb_replacement_073'], 'func': fb_replacement_d2_073}


def fb_replacement_d2_074(fb_replacement_074):
    feature = _clean(fb_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_074'] = {'inputs': ['fb_replacement_074'], 'func': fb_replacement_d2_074}


def fb_replacement_d2_075(fb_replacement_075):
    feature = _clean(fb_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_075'] = {'inputs': ['fb_replacement_075'], 'func': fb_replacement_d2_075}


def fb_replacement_d2_076(fb_replacement_076):
    feature = _clean(fb_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_076'] = {'inputs': ['fb_replacement_076'], 'func': fb_replacement_d2_076}


def fb_replacement_d2_077(fb_replacement_077):
    feature = _clean(fb_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_077'] = {'inputs': ['fb_replacement_077'], 'func': fb_replacement_d2_077}


def fb_replacement_d2_078(fb_replacement_078):
    feature = _clean(fb_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_078'] = {'inputs': ['fb_replacement_078'], 'func': fb_replacement_d2_078}


def fb_replacement_d2_079(fb_replacement_079):
    feature = _clean(fb_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_079'] = {'inputs': ['fb_replacement_079'], 'func': fb_replacement_d2_079}


def fb_replacement_d2_080(fb_replacement_080):
    feature = _clean(fb_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_080'] = {'inputs': ['fb_replacement_080'], 'func': fb_replacement_d2_080}


def fb_replacement_d2_081(fb_replacement_081):
    feature = _clean(fb_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_081'] = {'inputs': ['fb_replacement_081'], 'func': fb_replacement_d2_081}


def fb_replacement_d2_082(fb_replacement_082):
    feature = _clean(fb_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_082'] = {'inputs': ['fb_replacement_082'], 'func': fb_replacement_d2_082}


def fb_replacement_d2_083(fb_replacement_083):
    feature = _clean(fb_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_083'] = {'inputs': ['fb_replacement_083'], 'func': fb_replacement_d2_083}


def fb_replacement_d2_084(fb_replacement_084):
    feature = _clean(fb_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_084'] = {'inputs': ['fb_replacement_084'], 'func': fb_replacement_d2_084}


def fb_replacement_d2_085(fb_replacement_085):
    feature = _clean(fb_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_085'] = {'inputs': ['fb_replacement_085'], 'func': fb_replacement_d2_085}


def fb_replacement_d2_086(fb_replacement_086):
    feature = _clean(fb_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_086'] = {'inputs': ['fb_replacement_086'], 'func': fb_replacement_d2_086}


def fb_replacement_d2_087(fb_replacement_087):
    feature = _clean(fb_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_087'] = {'inputs': ['fb_replacement_087'], 'func': fb_replacement_d2_087}


def fb_replacement_d2_088(fb_replacement_088):
    feature = _clean(fb_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_088'] = {'inputs': ['fb_replacement_088'], 'func': fb_replacement_d2_088}


def fb_replacement_d2_089(fb_replacement_089):
    feature = _clean(fb_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_089'] = {'inputs': ['fb_replacement_089'], 'func': fb_replacement_d2_089}


def fb_replacement_d2_090(fb_replacement_090):
    feature = _clean(fb_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_090'] = {'inputs': ['fb_replacement_090'], 'func': fb_replacement_d2_090}


def fb_replacement_d2_091(fb_replacement_091):
    feature = _clean(fb_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_091'] = {'inputs': ['fb_replacement_091'], 'func': fb_replacement_d2_091}


def fb_replacement_d2_092(fb_replacement_092):
    feature = _clean(fb_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_092'] = {'inputs': ['fb_replacement_092'], 'func': fb_replacement_d2_092}


def fb_replacement_d2_093(fb_replacement_093):
    feature = _clean(fb_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_093'] = {'inputs': ['fb_replacement_093'], 'func': fb_replacement_d2_093}


def fb_replacement_d2_094(fb_replacement_094):
    feature = _clean(fb_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_094'] = {'inputs': ['fb_replacement_094'], 'func': fb_replacement_d2_094}


def fb_replacement_d2_095(fb_replacement_095):
    feature = _clean(fb_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_095'] = {'inputs': ['fb_replacement_095'], 'func': fb_replacement_d2_095}


def fb_replacement_d2_096(fb_replacement_096):
    feature = _clean(fb_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_096'] = {'inputs': ['fb_replacement_096'], 'func': fb_replacement_d2_096}


def fb_replacement_d2_097(fb_replacement_097):
    feature = _clean(fb_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_097'] = {'inputs': ['fb_replacement_097'], 'func': fb_replacement_d2_097}


def fb_replacement_d2_098(fb_replacement_098):
    feature = _clean(fb_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_098'] = {'inputs': ['fb_replacement_098'], 'func': fb_replacement_d2_098}


def fb_replacement_d2_099(fb_replacement_099):
    feature = _clean(fb_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_099'] = {'inputs': ['fb_replacement_099'], 'func': fb_replacement_d2_099}


def fb_replacement_d2_100(fb_replacement_100):
    feature = _clean(fb_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_100'] = {'inputs': ['fb_replacement_100'], 'func': fb_replacement_d2_100}


def fb_replacement_d2_101(fb_replacement_101):
    feature = _clean(fb_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_101'] = {'inputs': ['fb_replacement_101'], 'func': fb_replacement_d2_101}


def fb_replacement_d2_102(fb_replacement_102):
    feature = _clean(fb_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_102'] = {'inputs': ['fb_replacement_102'], 'func': fb_replacement_d2_102}


def fb_replacement_d2_103(fb_replacement_103):
    feature = _clean(fb_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_103'] = {'inputs': ['fb_replacement_103'], 'func': fb_replacement_d2_103}


def fb_replacement_d2_104(fb_replacement_104):
    feature = _clean(fb_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_104'] = {'inputs': ['fb_replacement_104'], 'func': fb_replacement_d2_104}


def fb_replacement_d2_105(fb_replacement_105):
    feature = _clean(fb_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_105'] = {'inputs': ['fb_replacement_105'], 'func': fb_replacement_d2_105}


def fb_replacement_d2_106(fb_replacement_106):
    feature = _clean(fb_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_106'] = {'inputs': ['fb_replacement_106'], 'func': fb_replacement_d2_106}


def fb_replacement_d2_107(fb_replacement_107):
    feature = _clean(fb_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_107'] = {'inputs': ['fb_replacement_107'], 'func': fb_replacement_d2_107}


def fb_replacement_d2_108(fb_replacement_108):
    feature = _clean(fb_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_108'] = {'inputs': ['fb_replacement_108'], 'func': fb_replacement_d2_108}


def fb_replacement_d2_109(fb_replacement_109):
    feature = _clean(fb_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_109'] = {'inputs': ['fb_replacement_109'], 'func': fb_replacement_d2_109}


def fb_replacement_d2_110(fb_replacement_110):
    feature = _clean(fb_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_110'] = {'inputs': ['fb_replacement_110'], 'func': fb_replacement_d2_110}


def fb_replacement_d2_111(fb_replacement_111):
    feature = _clean(fb_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_111'] = {'inputs': ['fb_replacement_111'], 'func': fb_replacement_d2_111}


def fb_replacement_d2_112(fb_replacement_112):
    feature = _clean(fb_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_112'] = {'inputs': ['fb_replacement_112'], 'func': fb_replacement_d2_112}


def fb_replacement_d2_113(fb_replacement_113):
    feature = _clean(fb_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_113'] = {'inputs': ['fb_replacement_113'], 'func': fb_replacement_d2_113}


def fb_replacement_d2_114(fb_replacement_114):
    feature = _clean(fb_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_114'] = {'inputs': ['fb_replacement_114'], 'func': fb_replacement_d2_114}


def fb_replacement_d2_115(fb_replacement_115):
    feature = _clean(fb_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_115'] = {'inputs': ['fb_replacement_115'], 'func': fb_replacement_d2_115}


def fb_replacement_d2_116(fb_replacement_116):
    feature = _clean(fb_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_116'] = {'inputs': ['fb_replacement_116'], 'func': fb_replacement_d2_116}


def fb_replacement_d2_117(fb_replacement_117):
    feature = _clean(fb_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_117'] = {'inputs': ['fb_replacement_117'], 'func': fb_replacement_d2_117}


def fb_replacement_d2_118(fb_replacement_118):
    feature = _clean(fb_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_118'] = {'inputs': ['fb_replacement_118'], 'func': fb_replacement_d2_118}


def fb_replacement_d2_119(fb_replacement_119):
    feature = _clean(fb_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_119'] = {'inputs': ['fb_replacement_119'], 'func': fb_replacement_d2_119}


def fb_replacement_d2_120(fb_replacement_120):
    feature = _clean(fb_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_120'] = {'inputs': ['fb_replacement_120'], 'func': fb_replacement_d2_120}


def fb_replacement_d2_121(fb_replacement_121):
    feature = _clean(fb_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_121'] = {'inputs': ['fb_replacement_121'], 'func': fb_replacement_d2_121}


def fb_replacement_d2_122(fb_replacement_122):
    feature = _clean(fb_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_122'] = {'inputs': ['fb_replacement_122'], 'func': fb_replacement_d2_122}


def fb_replacement_d2_123(fb_replacement_123):
    feature = _clean(fb_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_123'] = {'inputs': ['fb_replacement_123'], 'func': fb_replacement_d2_123}


def fb_replacement_d2_124(fb_replacement_124):
    feature = _clean(fb_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_124'] = {'inputs': ['fb_replacement_124'], 'func': fb_replacement_d2_124}


def fb_replacement_d2_125(fb_replacement_125):
    feature = _clean(fb_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_125'] = {'inputs': ['fb_replacement_125'], 'func': fb_replacement_d2_125}


def fb_replacement_d2_126(fb_replacement_126):
    feature = _clean(fb_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_126'] = {'inputs': ['fb_replacement_126'], 'func': fb_replacement_d2_126}


def fb_replacement_d2_127(fb_replacement_127):
    feature = _clean(fb_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_127'] = {'inputs': ['fb_replacement_127'], 'func': fb_replacement_d2_127}


def fb_replacement_d2_128(fb_replacement_128):
    feature = _clean(fb_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_128'] = {'inputs': ['fb_replacement_128'], 'func': fb_replacement_d2_128}


def fb_replacement_d2_129(fb_replacement_129):
    feature = _clean(fb_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_129'] = {'inputs': ['fb_replacement_129'], 'func': fb_replacement_d2_129}


def fb_replacement_d2_130(fb_replacement_130):
    feature = _clean(fb_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_130'] = {'inputs': ['fb_replacement_130'], 'func': fb_replacement_d2_130}


def fb_replacement_d2_131(fb_replacement_131):
    feature = _clean(fb_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_131'] = {'inputs': ['fb_replacement_131'], 'func': fb_replacement_d2_131}


def fb_replacement_d2_132(fb_replacement_132):
    feature = _clean(fb_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_132'] = {'inputs': ['fb_replacement_132'], 'func': fb_replacement_d2_132}


def fb_replacement_d2_133(fb_replacement_133):
    feature = _clean(fb_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_133'] = {'inputs': ['fb_replacement_133'], 'func': fb_replacement_d2_133}


def fb_replacement_d2_134(fb_replacement_134):
    feature = _clean(fb_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_134'] = {'inputs': ['fb_replacement_134'], 'func': fb_replacement_d2_134}


def fb_replacement_d2_135(fb_replacement_135):
    feature = _clean(fb_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_135'] = {'inputs': ['fb_replacement_135'], 'func': fb_replacement_d2_135}


def fb_replacement_d2_136(fb_replacement_136):
    feature = _clean(fb_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_136'] = {'inputs': ['fb_replacement_136'], 'func': fb_replacement_d2_136}


def fb_replacement_d2_137(fb_replacement_137):
    feature = _clean(fb_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_137'] = {'inputs': ['fb_replacement_137'], 'func': fb_replacement_d2_137}


def fb_replacement_d2_138(fb_replacement_138):
    feature = _clean(fb_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_138'] = {'inputs': ['fb_replacement_138'], 'func': fb_replacement_d2_138}


def fb_replacement_d2_139(fb_replacement_139):
    feature = _clean(fb_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_139'] = {'inputs': ['fb_replacement_139'], 'func': fb_replacement_d2_139}


def fb_replacement_d2_140(fb_replacement_140):
    feature = _clean(fb_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_140'] = {'inputs': ['fb_replacement_140'], 'func': fb_replacement_d2_140}


def fb_replacement_d2_141(fb_replacement_141):
    feature = _clean(fb_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_141'] = {'inputs': ['fb_replacement_141'], 'func': fb_replacement_d2_141}


def fb_replacement_d2_142(fb_replacement_142):
    feature = _clean(fb_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_142'] = {'inputs': ['fb_replacement_142'], 'func': fb_replacement_d2_142}


def fb_replacement_d2_143(fb_replacement_143):
    feature = _clean(fb_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_143'] = {'inputs': ['fb_replacement_143'], 'func': fb_replacement_d2_143}


def fb_replacement_d2_144(fb_replacement_144):
    feature = _clean(fb_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_144'] = {'inputs': ['fb_replacement_144'], 'func': fb_replacement_d2_144}


def fb_replacement_d2_145(fb_replacement_145):
    feature = _clean(fb_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_145'] = {'inputs': ['fb_replacement_145'], 'func': fb_replacement_d2_145}


def fb_replacement_d2_146(fb_replacement_146):
    feature = _clean(fb_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_146'] = {'inputs': ['fb_replacement_146'], 'func': fb_replacement_d2_146}


def fb_replacement_d2_147(fb_replacement_147):
    feature = _clean(fb_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_147'] = {'inputs': ['fb_replacement_147'], 'func': fb_replacement_d2_147}


def fb_replacement_d2_148(fb_replacement_148):
    feature = _clean(fb_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_148'] = {'inputs': ['fb_replacement_148'], 'func': fb_replacement_d2_148}


def fb_replacement_d2_149(fb_replacement_149):
    feature = _clean(fb_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_149'] = {'inputs': ['fb_replacement_149'], 'func': fb_replacement_d2_149}


def fb_replacement_d2_150(fb_replacement_150):
    feature = _clean(fb_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_150'] = {'inputs': ['fb_replacement_150'], 'func': fb_replacement_d2_150}


def fb_replacement_d2_151(fb_replacement_151):
    feature = _clean(fb_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_151'] = {'inputs': ['fb_replacement_151'], 'func': fb_replacement_d2_151}


def fb_replacement_d2_152(fb_replacement_152):
    feature = _clean(fb_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_152'] = {'inputs': ['fb_replacement_152'], 'func': fb_replacement_d2_152}


def fb_replacement_d2_153(fb_replacement_153):
    feature = _clean(fb_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_153'] = {'inputs': ['fb_replacement_153'], 'func': fb_replacement_d2_153}


def fb_replacement_d2_154(fb_replacement_154):
    feature = _clean(fb_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_154'] = {'inputs': ['fb_replacement_154'], 'func': fb_replacement_d2_154}


def fb_replacement_d2_155(fb_replacement_155):
    feature = _clean(fb_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_155'] = {'inputs': ['fb_replacement_155'], 'func': fb_replacement_d2_155}


def fb_replacement_d2_156(fb_replacement_156):
    feature = _clean(fb_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_156'] = {'inputs': ['fb_replacement_156'], 'func': fb_replacement_d2_156}


def fb_replacement_d2_157(fb_replacement_157):
    feature = _clean(fb_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_157'] = {'inputs': ['fb_replacement_157'], 'func': fb_replacement_d2_157}


def fb_replacement_d2_158(fb_replacement_158):
    feature = _clean(fb_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_158'] = {'inputs': ['fb_replacement_158'], 'func': fb_replacement_d2_158}


def fb_replacement_d2_159(fb_replacement_159):
    feature = _clean(fb_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_159'] = {'inputs': ['fb_replacement_159'], 'func': fb_replacement_d2_159}


def fb_replacement_d2_160(fb_replacement_160):
    feature = _clean(fb_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
FB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fb_replacement_d2_160'] = {'inputs': ['fb_replacement_160'], 'func': fb_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002(fbd_002_gap_magnitude_10_002):
    return _base_universe_d2(fbd_002_gap_magnitude_10_002, 1)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002'] = {'inputs': ['fbd_002_gap_magnitude_10_002'], 'func': fbd_base_universe_d2_001_fbd_002_gap_magnitude_10_002}


def fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003(fbd_003_open_close_pressure_21_003):
    return _base_universe_d2(fbd_003_open_close_pressure_21_003, 2)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003'] = {'inputs': ['fbd_003_open_close_pressure_21_003'], 'func': fbd_base_universe_d2_002_fbd_003_open_close_pressure_21_003}


def fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004(fbd_004_lower_wick_ratio_42_004):
    return _base_universe_d2(fbd_004_lower_wick_ratio_42_004, 3)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004'] = {'inputs': ['fbd_004_lower_wick_ratio_42_004'], 'func': fbd_base_universe_d2_003_fbd_004_lower_wick_ratio_42_004}


def fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005(fbd_005_upper_wick_ratio_63_005):
    return _base_universe_d2(fbd_005_upper_wick_ratio_63_005, 4)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005'] = {'inputs': ['fbd_005_upper_wick_ratio_63_005'], 'func': fbd_base_universe_d2_004_fbd_005_upper_wick_ratio_63_005}


def fbd_base_universe_d2_005_fbd_006_body_to_range_84_006(fbd_006_body_to_range_84_006):
    return _base_universe_d2(fbd_006_body_to_range_84_006, 5)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_005_fbd_006_body_to_range_84_006'] = {'inputs': ['fbd_006_body_to_range_84_006'], 'func': fbd_base_universe_d2_005_fbd_006_body_to_range_84_006}


def fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008(fbd_008_gap_magnitude_189_008):
    return _base_universe_d2(fbd_008_gap_magnitude_189_008, 6)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008'] = {'inputs': ['fbd_008_gap_magnitude_189_008'], 'func': fbd_base_universe_d2_006_fbd_008_gap_magnitude_189_008}


def fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009(fbd_009_open_close_pressure_252_009):
    return _base_universe_d2(fbd_009_open_close_pressure_252_009, 7)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009'] = {'inputs': ['fbd_009_open_close_pressure_252_009'], 'func': fbd_base_universe_d2_007_fbd_009_open_close_pressure_252_009}


def fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010(fbd_010_lower_wick_ratio_378_010):
    return _base_universe_d2(fbd_010_lower_wick_ratio_378_010, 8)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010'] = {'inputs': ['fbd_010_lower_wick_ratio_378_010'], 'func': fbd_base_universe_d2_008_fbd_010_lower_wick_ratio_378_010}


def fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011(fbd_011_upper_wick_ratio_504_011):
    return _base_universe_d2(fbd_011_upper_wick_ratio_504_011, 9)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011'] = {'inputs': ['fbd_011_upper_wick_ratio_504_011'], 'func': fbd_base_universe_d2_009_fbd_011_upper_wick_ratio_504_011}


def fbd_base_universe_d2_010_fbd_012_body_to_range_756_012(fbd_012_body_to_range_756_012):
    return _base_universe_d2(fbd_012_body_to_range_756_012, 10)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_010_fbd_012_body_to_range_756_012'] = {'inputs': ['fbd_012_body_to_range_756_012'], 'func': fbd_base_universe_d2_010_fbd_012_body_to_range_756_012}


def fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014(fbd_014_gap_magnitude_1260_014):
    return _base_universe_d2(fbd_014_gap_magnitude_1260_014, 11)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014'] = {'inputs': ['fbd_014_gap_magnitude_1260_014'], 'func': fbd_base_universe_d2_011_fbd_014_gap_magnitude_1260_014}


def fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015(fbd_015_open_close_pressure_1512_015):
    return _base_universe_d2(fbd_015_open_close_pressure_1512_015, 12)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015'] = {'inputs': ['fbd_015_open_close_pressure_1512_015'], 'func': fbd_base_universe_d2_012_fbd_015_open_close_pressure_1512_015}


def fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016(fbd_016_lower_wick_ratio_5_016):
    return _base_universe_d2(fbd_016_lower_wick_ratio_5_016, 13)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016'] = {'inputs': ['fbd_016_lower_wick_ratio_5_016'], 'func': fbd_base_universe_d2_013_fbd_016_lower_wick_ratio_5_016}


def fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017(fbd_017_upper_wick_ratio_10_017):
    return _base_universe_d2(fbd_017_upper_wick_ratio_10_017, 14)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017'] = {'inputs': ['fbd_017_upper_wick_ratio_10_017'], 'func': fbd_base_universe_d2_014_fbd_017_upper_wick_ratio_10_017}


def fbd_base_universe_d2_015_fbd_018_body_to_range_21_018(fbd_018_body_to_range_21_018):
    return _base_universe_d2(fbd_018_body_to_range_21_018, 15)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_015_fbd_018_body_to_range_21_018'] = {'inputs': ['fbd_018_body_to_range_21_018'], 'func': fbd_base_universe_d2_015_fbd_018_body_to_range_21_018}


def fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020(fbd_020_gap_magnitude_63_020):
    return _base_universe_d2(fbd_020_gap_magnitude_63_020, 16)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020'] = {'inputs': ['fbd_020_gap_magnitude_63_020'], 'func': fbd_base_universe_d2_016_fbd_020_gap_magnitude_63_020}


def fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021(fbd_021_open_close_pressure_84_021):
    return _base_universe_d2(fbd_021_open_close_pressure_84_021, 17)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021'] = {'inputs': ['fbd_021_open_close_pressure_84_021'], 'func': fbd_base_universe_d2_017_fbd_021_open_close_pressure_84_021}


def fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022(fbd_022_lower_wick_ratio_126_022):
    return _base_universe_d2(fbd_022_lower_wick_ratio_126_022, 18)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022'] = {'inputs': ['fbd_022_lower_wick_ratio_126_022'], 'func': fbd_base_universe_d2_018_fbd_022_lower_wick_ratio_126_022}


def fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023(fbd_023_upper_wick_ratio_189_023):
    return _base_universe_d2(fbd_023_upper_wick_ratio_189_023, 19)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023'] = {'inputs': ['fbd_023_upper_wick_ratio_189_023'], 'func': fbd_base_universe_d2_019_fbd_023_upper_wick_ratio_189_023}


def fbd_base_universe_d2_020_fbd_024_body_to_range_252_024(fbd_024_body_to_range_252_024):
    return _base_universe_d2(fbd_024_body_to_range_252_024, 20)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_020_fbd_024_body_to_range_252_024'] = {'inputs': ['fbd_024_body_to_range_252_024'], 'func': fbd_base_universe_d2_020_fbd_024_body_to_range_252_024}


def fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026(fbd_026_gap_magnitude_504_026):
    return _base_universe_d2(fbd_026_gap_magnitude_504_026, 21)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026'] = {'inputs': ['fbd_026_gap_magnitude_504_026'], 'func': fbd_base_universe_d2_021_fbd_026_gap_magnitude_504_026}


def fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027(fbd_027_open_close_pressure_756_027):
    return _base_universe_d2(fbd_027_open_close_pressure_756_027, 22)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027'] = {'inputs': ['fbd_027_open_close_pressure_756_027'], 'func': fbd_base_universe_d2_022_fbd_027_open_close_pressure_756_027}


def fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028(fbd_028_lower_wick_ratio_1008_028):
    return _base_universe_d2(fbd_028_lower_wick_ratio_1008_028, 23)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028'] = {'inputs': ['fbd_028_lower_wick_ratio_1008_028'], 'func': fbd_base_universe_d2_023_fbd_028_lower_wick_ratio_1008_028}


def fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029(fbd_029_upper_wick_ratio_1260_029):
    return _base_universe_d2(fbd_029_upper_wick_ratio_1260_029, 24)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029'] = {'inputs': ['fbd_029_upper_wick_ratio_1260_029'], 'func': fbd_base_universe_d2_024_fbd_029_upper_wick_ratio_1260_029}


def fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030(fbd_030_body_to_range_1512_030):
    return _base_universe_d2(fbd_030_body_to_range_1512_030, 25)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030'] = {'inputs': ['fbd_030_body_to_range_1512_030'], 'func': fbd_base_universe_d2_025_fbd_030_body_to_range_1512_030}


def fbd_base_universe_d2_026_fbd_basefill_031(fbd_basefill_031):
    return _base_universe_d2(fbd_basefill_031, 26)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_026_fbd_basefill_031'] = {'inputs': ['fbd_basefill_031'], 'func': fbd_base_universe_d2_026_fbd_basefill_031}


def fbd_base_universe_d2_027_fbd_basefill_032(fbd_basefill_032):
    return _base_universe_d2(fbd_basefill_032, 27)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_027_fbd_basefill_032'] = {'inputs': ['fbd_basefill_032'], 'func': fbd_base_universe_d2_027_fbd_basefill_032}


def fbd_base_universe_d2_028_fbd_basefill_033(fbd_basefill_033):
    return _base_universe_d2(fbd_basefill_033, 28)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_028_fbd_basefill_033'] = {'inputs': ['fbd_basefill_033'], 'func': fbd_base_universe_d2_028_fbd_basefill_033}


def fbd_base_universe_d2_029_fbd_basefill_034(fbd_basefill_034):
    return _base_universe_d2(fbd_basefill_034, 29)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_029_fbd_basefill_034'] = {'inputs': ['fbd_basefill_034'], 'func': fbd_base_universe_d2_029_fbd_basefill_034}


def fbd_base_universe_d2_030_fbd_basefill_035(fbd_basefill_035):
    return _base_universe_d2(fbd_basefill_035, 30)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_030_fbd_basefill_035'] = {'inputs': ['fbd_basefill_035'], 'func': fbd_base_universe_d2_030_fbd_basefill_035}


def fbd_base_universe_d2_031_fbd_basefill_036(fbd_basefill_036):
    return _base_universe_d2(fbd_basefill_036, 31)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_031_fbd_basefill_036'] = {'inputs': ['fbd_basefill_036'], 'func': fbd_base_universe_d2_031_fbd_basefill_036}


def fbd_base_universe_d2_032_fbd_basefill_037(fbd_basefill_037):
    return _base_universe_d2(fbd_basefill_037, 32)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_032_fbd_basefill_037'] = {'inputs': ['fbd_basefill_037'], 'func': fbd_base_universe_d2_032_fbd_basefill_037}


def fbd_base_universe_d2_033_fbd_basefill_038(fbd_basefill_038):
    return _base_universe_d2(fbd_basefill_038, 33)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_033_fbd_basefill_038'] = {'inputs': ['fbd_basefill_038'], 'func': fbd_base_universe_d2_033_fbd_basefill_038}


def fbd_base_universe_d2_034_fbd_basefill_039(fbd_basefill_039):
    return _base_universe_d2(fbd_basefill_039, 34)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_034_fbd_basefill_039'] = {'inputs': ['fbd_basefill_039'], 'func': fbd_base_universe_d2_034_fbd_basefill_039}


def fbd_base_universe_d2_035_fbd_basefill_040(fbd_basefill_040):
    return _base_universe_d2(fbd_basefill_040, 35)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_035_fbd_basefill_040'] = {'inputs': ['fbd_basefill_040'], 'func': fbd_base_universe_d2_035_fbd_basefill_040}


def fbd_base_universe_d2_036_fbd_basefill_041(fbd_basefill_041):
    return _base_universe_d2(fbd_basefill_041, 36)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_036_fbd_basefill_041'] = {'inputs': ['fbd_basefill_041'], 'func': fbd_base_universe_d2_036_fbd_basefill_041}


def fbd_base_universe_d2_037_fbd_basefill_042(fbd_basefill_042):
    return _base_universe_d2(fbd_basefill_042, 37)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_037_fbd_basefill_042'] = {'inputs': ['fbd_basefill_042'], 'func': fbd_base_universe_d2_037_fbd_basefill_042}


def fbd_base_universe_d2_038_fbd_basefill_043(fbd_basefill_043):
    return _base_universe_d2(fbd_basefill_043, 38)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_038_fbd_basefill_043'] = {'inputs': ['fbd_basefill_043'], 'func': fbd_base_universe_d2_038_fbd_basefill_043}


def fbd_base_universe_d2_039_fbd_basefill_044(fbd_basefill_044):
    return _base_universe_d2(fbd_basefill_044, 39)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_039_fbd_basefill_044'] = {'inputs': ['fbd_basefill_044'], 'func': fbd_base_universe_d2_039_fbd_basefill_044}


def fbd_base_universe_d2_040_fbd_basefill_045(fbd_basefill_045):
    return _base_universe_d2(fbd_basefill_045, 40)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_040_fbd_basefill_045'] = {'inputs': ['fbd_basefill_045'], 'func': fbd_base_universe_d2_040_fbd_basefill_045}


def fbd_base_universe_d2_041_fbd_basefill_046(fbd_basefill_046):
    return _base_universe_d2(fbd_basefill_046, 41)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_041_fbd_basefill_046'] = {'inputs': ['fbd_basefill_046'], 'func': fbd_base_universe_d2_041_fbd_basefill_046}


def fbd_base_universe_d2_042_fbd_basefill_047(fbd_basefill_047):
    return _base_universe_d2(fbd_basefill_047, 42)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_042_fbd_basefill_047'] = {'inputs': ['fbd_basefill_047'], 'func': fbd_base_universe_d2_042_fbd_basefill_047}


def fbd_base_universe_d2_043_fbd_basefill_048(fbd_basefill_048):
    return _base_universe_d2(fbd_basefill_048, 43)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_043_fbd_basefill_048'] = {'inputs': ['fbd_basefill_048'], 'func': fbd_base_universe_d2_043_fbd_basefill_048}


def fbd_base_universe_d2_044_fbd_basefill_049(fbd_basefill_049):
    return _base_universe_d2(fbd_basefill_049, 44)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_044_fbd_basefill_049'] = {'inputs': ['fbd_basefill_049'], 'func': fbd_base_universe_d2_044_fbd_basefill_049}


def fbd_base_universe_d2_045_fbd_basefill_050(fbd_basefill_050):
    return _base_universe_d2(fbd_basefill_050, 45)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_045_fbd_basefill_050'] = {'inputs': ['fbd_basefill_050'], 'func': fbd_base_universe_d2_045_fbd_basefill_050}


def fbd_base_universe_d2_046_fbd_basefill_051(fbd_basefill_051):
    return _base_universe_d2(fbd_basefill_051, 46)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_046_fbd_basefill_051'] = {'inputs': ['fbd_basefill_051'], 'func': fbd_base_universe_d2_046_fbd_basefill_051}


def fbd_base_universe_d2_047_fbd_basefill_052(fbd_basefill_052):
    return _base_universe_d2(fbd_basefill_052, 47)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_047_fbd_basefill_052'] = {'inputs': ['fbd_basefill_052'], 'func': fbd_base_universe_d2_047_fbd_basefill_052}


def fbd_base_universe_d2_048_fbd_basefill_053(fbd_basefill_053):
    return _base_universe_d2(fbd_basefill_053, 48)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_048_fbd_basefill_053'] = {'inputs': ['fbd_basefill_053'], 'func': fbd_base_universe_d2_048_fbd_basefill_053}


def fbd_base_universe_d2_049_fbd_basefill_054(fbd_basefill_054):
    return _base_universe_d2(fbd_basefill_054, 49)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_049_fbd_basefill_054'] = {'inputs': ['fbd_basefill_054'], 'func': fbd_base_universe_d2_049_fbd_basefill_054}


def fbd_base_universe_d2_050_fbd_basefill_055(fbd_basefill_055):
    return _base_universe_d2(fbd_basefill_055, 50)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_050_fbd_basefill_055'] = {'inputs': ['fbd_basefill_055'], 'func': fbd_base_universe_d2_050_fbd_basefill_055}


def fbd_base_universe_d2_051_fbd_basefill_056(fbd_basefill_056):
    return _base_universe_d2(fbd_basefill_056, 51)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_051_fbd_basefill_056'] = {'inputs': ['fbd_basefill_056'], 'func': fbd_base_universe_d2_051_fbd_basefill_056}


def fbd_base_universe_d2_052_fbd_basefill_057(fbd_basefill_057):
    return _base_universe_d2(fbd_basefill_057, 52)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_052_fbd_basefill_057'] = {'inputs': ['fbd_basefill_057'], 'func': fbd_base_universe_d2_052_fbd_basefill_057}


def fbd_base_universe_d2_053_fbd_basefill_058(fbd_basefill_058):
    return _base_universe_d2(fbd_basefill_058, 53)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_053_fbd_basefill_058'] = {'inputs': ['fbd_basefill_058'], 'func': fbd_base_universe_d2_053_fbd_basefill_058}


def fbd_base_universe_d2_054_fbd_basefill_059(fbd_basefill_059):
    return _base_universe_d2(fbd_basefill_059, 54)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_054_fbd_basefill_059'] = {'inputs': ['fbd_basefill_059'], 'func': fbd_base_universe_d2_054_fbd_basefill_059}


def fbd_base_universe_d2_055_fbd_basefill_060(fbd_basefill_060):
    return _base_universe_d2(fbd_basefill_060, 55)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_055_fbd_basefill_060'] = {'inputs': ['fbd_basefill_060'], 'func': fbd_base_universe_d2_055_fbd_basefill_060}


def fbd_base_universe_d2_056_fbd_basefill_061(fbd_basefill_061):
    return _base_universe_d2(fbd_basefill_061, 56)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_056_fbd_basefill_061'] = {'inputs': ['fbd_basefill_061'], 'func': fbd_base_universe_d2_056_fbd_basefill_061}


def fbd_base_universe_d2_057_fbd_basefill_062(fbd_basefill_062):
    return _base_universe_d2(fbd_basefill_062, 57)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_057_fbd_basefill_062'] = {'inputs': ['fbd_basefill_062'], 'func': fbd_base_universe_d2_057_fbd_basefill_062}


def fbd_base_universe_d2_058_fbd_basefill_063(fbd_basefill_063):
    return _base_universe_d2(fbd_basefill_063, 58)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_058_fbd_basefill_063'] = {'inputs': ['fbd_basefill_063'], 'func': fbd_base_universe_d2_058_fbd_basefill_063}


def fbd_base_universe_d2_059_fbd_basefill_064(fbd_basefill_064):
    return _base_universe_d2(fbd_basefill_064, 59)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_059_fbd_basefill_064'] = {'inputs': ['fbd_basefill_064'], 'func': fbd_base_universe_d2_059_fbd_basefill_064}


def fbd_base_universe_d2_060_fbd_basefill_065(fbd_basefill_065):
    return _base_universe_d2(fbd_basefill_065, 60)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_060_fbd_basefill_065'] = {'inputs': ['fbd_basefill_065'], 'func': fbd_base_universe_d2_060_fbd_basefill_065}


def fbd_base_universe_d2_061_fbd_basefill_066(fbd_basefill_066):
    return _base_universe_d2(fbd_basefill_066, 61)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_061_fbd_basefill_066'] = {'inputs': ['fbd_basefill_066'], 'func': fbd_base_universe_d2_061_fbd_basefill_066}


def fbd_base_universe_d2_062_fbd_basefill_067(fbd_basefill_067):
    return _base_universe_d2(fbd_basefill_067, 62)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_062_fbd_basefill_067'] = {'inputs': ['fbd_basefill_067'], 'func': fbd_base_universe_d2_062_fbd_basefill_067}


def fbd_base_universe_d2_063_fbd_basefill_068(fbd_basefill_068):
    return _base_universe_d2(fbd_basefill_068, 63)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_063_fbd_basefill_068'] = {'inputs': ['fbd_basefill_068'], 'func': fbd_base_universe_d2_063_fbd_basefill_068}


def fbd_base_universe_d2_064_fbd_basefill_069(fbd_basefill_069):
    return _base_universe_d2(fbd_basefill_069, 64)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_064_fbd_basefill_069'] = {'inputs': ['fbd_basefill_069'], 'func': fbd_base_universe_d2_064_fbd_basefill_069}


def fbd_base_universe_d2_065_fbd_basefill_070(fbd_basefill_070):
    return _base_universe_d2(fbd_basefill_070, 65)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_065_fbd_basefill_070'] = {'inputs': ['fbd_basefill_070'], 'func': fbd_base_universe_d2_065_fbd_basefill_070}


def fbd_base_universe_d2_066_fbd_basefill_071(fbd_basefill_071):
    return _base_universe_d2(fbd_basefill_071, 66)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_066_fbd_basefill_071'] = {'inputs': ['fbd_basefill_071'], 'func': fbd_base_universe_d2_066_fbd_basefill_071}


def fbd_base_universe_d2_067_fbd_basefill_072(fbd_basefill_072):
    return _base_universe_d2(fbd_basefill_072, 67)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_067_fbd_basefill_072'] = {'inputs': ['fbd_basefill_072'], 'func': fbd_base_universe_d2_067_fbd_basefill_072}


def fbd_base_universe_d2_068_fbd_basefill_073(fbd_basefill_073):
    return _base_universe_d2(fbd_basefill_073, 68)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_068_fbd_basefill_073'] = {'inputs': ['fbd_basefill_073'], 'func': fbd_base_universe_d2_068_fbd_basefill_073}


def fbd_base_universe_d2_069_fbd_basefill_074(fbd_basefill_074):
    return _base_universe_d2(fbd_basefill_074, 69)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_069_fbd_basefill_074'] = {'inputs': ['fbd_basefill_074'], 'func': fbd_base_universe_d2_069_fbd_basefill_074}


def fbd_base_universe_d2_070_fbd_basefill_075(fbd_basefill_075):
    return _base_universe_d2(fbd_basefill_075, 70)
FBD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fbd_base_universe_d2_070_fbd_basefill_075'] = {'inputs': ['fbd_basefill_075'], 'func': fbd_base_universe_d2_070_fbd_basefill_075}
