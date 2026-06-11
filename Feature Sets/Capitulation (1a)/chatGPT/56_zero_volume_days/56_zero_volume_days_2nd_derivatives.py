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



def zvd_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def zvd_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def zvd_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















ZERO_VOLUME_DAYS_REGISTRY_2ND_DERIVATIVES = {
    'zvd_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': zvd_001_amihud_illiquidity_roc_1},
    'zvd_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': zvd_007_amihud_illiquidity_roc_5},
    'zvd_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': zvd_013_amihud_illiquidity_roc_42},
    'zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': zvd_154_zvd_019_amihud_illiquidity_42_019_roc_126},
    'zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': zvd_155_zvd_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def zvd_replacement_d2_001(zvd_replacement_001):
    feature = _clean(zvd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_001'] = {'inputs': ['zvd_replacement_001'], 'func': zvd_replacement_d2_001}


def zvd_replacement_d2_002(zvd_replacement_002):
    feature = _clean(zvd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_002'] = {'inputs': ['zvd_replacement_002'], 'func': zvd_replacement_d2_002}


def zvd_replacement_d2_003(zvd_replacement_003):
    feature = _clean(zvd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_003'] = {'inputs': ['zvd_replacement_003'], 'func': zvd_replacement_d2_003}


def zvd_replacement_d2_004(zvd_replacement_004):
    feature = _clean(zvd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_004'] = {'inputs': ['zvd_replacement_004'], 'func': zvd_replacement_d2_004}


def zvd_replacement_d2_005(zvd_replacement_005):
    feature = _clean(zvd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_005'] = {'inputs': ['zvd_replacement_005'], 'func': zvd_replacement_d2_005}


def zvd_replacement_d2_006(zvd_replacement_006):
    feature = _clean(zvd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_006'] = {'inputs': ['zvd_replacement_006'], 'func': zvd_replacement_d2_006}


def zvd_replacement_d2_007(zvd_replacement_007):
    feature = _clean(zvd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_007'] = {'inputs': ['zvd_replacement_007'], 'func': zvd_replacement_d2_007}


def zvd_replacement_d2_008(zvd_replacement_008):
    feature = _clean(zvd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_008'] = {'inputs': ['zvd_replacement_008'], 'func': zvd_replacement_d2_008}


def zvd_replacement_d2_009(zvd_replacement_009):
    feature = _clean(zvd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_009'] = {'inputs': ['zvd_replacement_009'], 'func': zvd_replacement_d2_009}


def zvd_replacement_d2_010(zvd_replacement_010):
    feature = _clean(zvd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_010'] = {'inputs': ['zvd_replacement_010'], 'func': zvd_replacement_d2_010}


def zvd_replacement_d2_011(zvd_replacement_011):
    feature = _clean(zvd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_011'] = {'inputs': ['zvd_replacement_011'], 'func': zvd_replacement_d2_011}


def zvd_replacement_d2_012(zvd_replacement_012):
    feature = _clean(zvd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_012'] = {'inputs': ['zvd_replacement_012'], 'func': zvd_replacement_d2_012}


def zvd_replacement_d2_013(zvd_replacement_013):
    feature = _clean(zvd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_013'] = {'inputs': ['zvd_replacement_013'], 'func': zvd_replacement_d2_013}


def zvd_replacement_d2_014(zvd_replacement_014):
    feature = _clean(zvd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_014'] = {'inputs': ['zvd_replacement_014'], 'func': zvd_replacement_d2_014}


def zvd_replacement_d2_015(zvd_replacement_015):
    feature = _clean(zvd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_015'] = {'inputs': ['zvd_replacement_015'], 'func': zvd_replacement_d2_015}


def zvd_replacement_d2_016(zvd_replacement_016):
    feature = _clean(zvd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_016'] = {'inputs': ['zvd_replacement_016'], 'func': zvd_replacement_d2_016}


def zvd_replacement_d2_017(zvd_replacement_017):
    feature = _clean(zvd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_017'] = {'inputs': ['zvd_replacement_017'], 'func': zvd_replacement_d2_017}


def zvd_replacement_d2_018(zvd_replacement_018):
    feature = _clean(zvd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_018'] = {'inputs': ['zvd_replacement_018'], 'func': zvd_replacement_d2_018}


def zvd_replacement_d2_019(zvd_replacement_019):
    feature = _clean(zvd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_019'] = {'inputs': ['zvd_replacement_019'], 'func': zvd_replacement_d2_019}


def zvd_replacement_d2_020(zvd_replacement_020):
    feature = _clean(zvd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_020'] = {'inputs': ['zvd_replacement_020'], 'func': zvd_replacement_d2_020}


def zvd_replacement_d2_021(zvd_replacement_021):
    feature = _clean(zvd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_021'] = {'inputs': ['zvd_replacement_021'], 'func': zvd_replacement_d2_021}


def zvd_replacement_d2_022(zvd_replacement_022):
    feature = _clean(zvd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_022'] = {'inputs': ['zvd_replacement_022'], 'func': zvd_replacement_d2_022}


def zvd_replacement_d2_023(zvd_replacement_023):
    feature = _clean(zvd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_023'] = {'inputs': ['zvd_replacement_023'], 'func': zvd_replacement_d2_023}


def zvd_replacement_d2_024(zvd_replacement_024):
    feature = _clean(zvd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_024'] = {'inputs': ['zvd_replacement_024'], 'func': zvd_replacement_d2_024}


def zvd_replacement_d2_025(zvd_replacement_025):
    feature = _clean(zvd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_025'] = {'inputs': ['zvd_replacement_025'], 'func': zvd_replacement_d2_025}


def zvd_replacement_d2_026(zvd_replacement_026):
    feature = _clean(zvd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_026'] = {'inputs': ['zvd_replacement_026'], 'func': zvd_replacement_d2_026}


def zvd_replacement_d2_027(zvd_replacement_027):
    feature = _clean(zvd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_027'] = {'inputs': ['zvd_replacement_027'], 'func': zvd_replacement_d2_027}


def zvd_replacement_d2_028(zvd_replacement_028):
    feature = _clean(zvd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_028'] = {'inputs': ['zvd_replacement_028'], 'func': zvd_replacement_d2_028}


def zvd_replacement_d2_029(zvd_replacement_029):
    feature = _clean(zvd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_029'] = {'inputs': ['zvd_replacement_029'], 'func': zvd_replacement_d2_029}


def zvd_replacement_d2_030(zvd_replacement_030):
    feature = _clean(zvd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_030'] = {'inputs': ['zvd_replacement_030'], 'func': zvd_replacement_d2_030}


def zvd_replacement_d2_031(zvd_replacement_031):
    feature = _clean(zvd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_031'] = {'inputs': ['zvd_replacement_031'], 'func': zvd_replacement_d2_031}


def zvd_replacement_d2_032(zvd_replacement_032):
    feature = _clean(zvd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_032'] = {'inputs': ['zvd_replacement_032'], 'func': zvd_replacement_d2_032}


def zvd_replacement_d2_033(zvd_replacement_033):
    feature = _clean(zvd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_033'] = {'inputs': ['zvd_replacement_033'], 'func': zvd_replacement_d2_033}


def zvd_replacement_d2_034(zvd_replacement_034):
    feature = _clean(zvd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_034'] = {'inputs': ['zvd_replacement_034'], 'func': zvd_replacement_d2_034}


def zvd_replacement_d2_035(zvd_replacement_035):
    feature = _clean(zvd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_035'] = {'inputs': ['zvd_replacement_035'], 'func': zvd_replacement_d2_035}


def zvd_replacement_d2_036(zvd_replacement_036):
    feature = _clean(zvd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_036'] = {'inputs': ['zvd_replacement_036'], 'func': zvd_replacement_d2_036}


def zvd_replacement_d2_037(zvd_replacement_037):
    feature = _clean(zvd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_037'] = {'inputs': ['zvd_replacement_037'], 'func': zvd_replacement_d2_037}


def zvd_replacement_d2_038(zvd_replacement_038):
    feature = _clean(zvd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_038'] = {'inputs': ['zvd_replacement_038'], 'func': zvd_replacement_d2_038}


def zvd_replacement_d2_039(zvd_replacement_039):
    feature = _clean(zvd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_039'] = {'inputs': ['zvd_replacement_039'], 'func': zvd_replacement_d2_039}


def zvd_replacement_d2_040(zvd_replacement_040):
    feature = _clean(zvd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_040'] = {'inputs': ['zvd_replacement_040'], 'func': zvd_replacement_d2_040}


def zvd_replacement_d2_041(zvd_replacement_041):
    feature = _clean(zvd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_041'] = {'inputs': ['zvd_replacement_041'], 'func': zvd_replacement_d2_041}


def zvd_replacement_d2_042(zvd_replacement_042):
    feature = _clean(zvd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_042'] = {'inputs': ['zvd_replacement_042'], 'func': zvd_replacement_d2_042}


def zvd_replacement_d2_043(zvd_replacement_043):
    feature = _clean(zvd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_043'] = {'inputs': ['zvd_replacement_043'], 'func': zvd_replacement_d2_043}


def zvd_replacement_d2_044(zvd_replacement_044):
    feature = _clean(zvd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_044'] = {'inputs': ['zvd_replacement_044'], 'func': zvd_replacement_d2_044}


def zvd_replacement_d2_045(zvd_replacement_045):
    feature = _clean(zvd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_045'] = {'inputs': ['zvd_replacement_045'], 'func': zvd_replacement_d2_045}


def zvd_replacement_d2_046(zvd_replacement_046):
    feature = _clean(zvd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_046'] = {'inputs': ['zvd_replacement_046'], 'func': zvd_replacement_d2_046}


def zvd_replacement_d2_047(zvd_replacement_047):
    feature = _clean(zvd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_047'] = {'inputs': ['zvd_replacement_047'], 'func': zvd_replacement_d2_047}


def zvd_replacement_d2_048(zvd_replacement_048):
    feature = _clean(zvd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_048'] = {'inputs': ['zvd_replacement_048'], 'func': zvd_replacement_d2_048}


def zvd_replacement_d2_049(zvd_replacement_049):
    feature = _clean(zvd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_049'] = {'inputs': ['zvd_replacement_049'], 'func': zvd_replacement_d2_049}


def zvd_replacement_d2_050(zvd_replacement_050):
    feature = _clean(zvd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_050'] = {'inputs': ['zvd_replacement_050'], 'func': zvd_replacement_d2_050}


def zvd_replacement_d2_051(zvd_replacement_051):
    feature = _clean(zvd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_051'] = {'inputs': ['zvd_replacement_051'], 'func': zvd_replacement_d2_051}


def zvd_replacement_d2_052(zvd_replacement_052):
    feature = _clean(zvd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_052'] = {'inputs': ['zvd_replacement_052'], 'func': zvd_replacement_d2_052}


def zvd_replacement_d2_053(zvd_replacement_053):
    feature = _clean(zvd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_053'] = {'inputs': ['zvd_replacement_053'], 'func': zvd_replacement_d2_053}


def zvd_replacement_d2_054(zvd_replacement_054):
    feature = _clean(zvd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_054'] = {'inputs': ['zvd_replacement_054'], 'func': zvd_replacement_d2_054}


def zvd_replacement_d2_055(zvd_replacement_055):
    feature = _clean(zvd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_055'] = {'inputs': ['zvd_replacement_055'], 'func': zvd_replacement_d2_055}


def zvd_replacement_d2_056(zvd_replacement_056):
    feature = _clean(zvd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_056'] = {'inputs': ['zvd_replacement_056'], 'func': zvd_replacement_d2_056}


def zvd_replacement_d2_057(zvd_replacement_057):
    feature = _clean(zvd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_057'] = {'inputs': ['zvd_replacement_057'], 'func': zvd_replacement_d2_057}


def zvd_replacement_d2_058(zvd_replacement_058):
    feature = _clean(zvd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_058'] = {'inputs': ['zvd_replacement_058'], 'func': zvd_replacement_d2_058}


def zvd_replacement_d2_059(zvd_replacement_059):
    feature = _clean(zvd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_059'] = {'inputs': ['zvd_replacement_059'], 'func': zvd_replacement_d2_059}


def zvd_replacement_d2_060(zvd_replacement_060):
    feature = _clean(zvd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_060'] = {'inputs': ['zvd_replacement_060'], 'func': zvd_replacement_d2_060}


def zvd_replacement_d2_061(zvd_replacement_061):
    feature = _clean(zvd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_061'] = {'inputs': ['zvd_replacement_061'], 'func': zvd_replacement_d2_061}


def zvd_replacement_d2_062(zvd_replacement_062):
    feature = _clean(zvd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_062'] = {'inputs': ['zvd_replacement_062'], 'func': zvd_replacement_d2_062}


def zvd_replacement_d2_063(zvd_replacement_063):
    feature = _clean(zvd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_063'] = {'inputs': ['zvd_replacement_063'], 'func': zvd_replacement_d2_063}


def zvd_replacement_d2_064(zvd_replacement_064):
    feature = _clean(zvd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_064'] = {'inputs': ['zvd_replacement_064'], 'func': zvd_replacement_d2_064}


def zvd_replacement_d2_065(zvd_replacement_065):
    feature = _clean(zvd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_065'] = {'inputs': ['zvd_replacement_065'], 'func': zvd_replacement_d2_065}


def zvd_replacement_d2_066(zvd_replacement_066):
    feature = _clean(zvd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_066'] = {'inputs': ['zvd_replacement_066'], 'func': zvd_replacement_d2_066}


def zvd_replacement_d2_067(zvd_replacement_067):
    feature = _clean(zvd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_067'] = {'inputs': ['zvd_replacement_067'], 'func': zvd_replacement_d2_067}


def zvd_replacement_d2_068(zvd_replacement_068):
    feature = _clean(zvd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_068'] = {'inputs': ['zvd_replacement_068'], 'func': zvd_replacement_d2_068}


def zvd_replacement_d2_069(zvd_replacement_069):
    feature = _clean(zvd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_069'] = {'inputs': ['zvd_replacement_069'], 'func': zvd_replacement_d2_069}


def zvd_replacement_d2_070(zvd_replacement_070):
    feature = _clean(zvd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_070'] = {'inputs': ['zvd_replacement_070'], 'func': zvd_replacement_d2_070}


def zvd_replacement_d2_071(zvd_replacement_071):
    feature = _clean(zvd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_071'] = {'inputs': ['zvd_replacement_071'], 'func': zvd_replacement_d2_071}


def zvd_replacement_d2_072(zvd_replacement_072):
    feature = _clean(zvd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_072'] = {'inputs': ['zvd_replacement_072'], 'func': zvd_replacement_d2_072}


def zvd_replacement_d2_073(zvd_replacement_073):
    feature = _clean(zvd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_073'] = {'inputs': ['zvd_replacement_073'], 'func': zvd_replacement_d2_073}


def zvd_replacement_d2_074(zvd_replacement_074):
    feature = _clean(zvd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_074'] = {'inputs': ['zvd_replacement_074'], 'func': zvd_replacement_d2_074}


def zvd_replacement_d2_075(zvd_replacement_075):
    feature = _clean(zvd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_075'] = {'inputs': ['zvd_replacement_075'], 'func': zvd_replacement_d2_075}


def zvd_replacement_d2_076(zvd_replacement_076):
    feature = _clean(zvd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_076'] = {'inputs': ['zvd_replacement_076'], 'func': zvd_replacement_d2_076}


def zvd_replacement_d2_077(zvd_replacement_077):
    feature = _clean(zvd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_077'] = {'inputs': ['zvd_replacement_077'], 'func': zvd_replacement_d2_077}


def zvd_replacement_d2_078(zvd_replacement_078):
    feature = _clean(zvd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_078'] = {'inputs': ['zvd_replacement_078'], 'func': zvd_replacement_d2_078}


def zvd_replacement_d2_079(zvd_replacement_079):
    feature = _clean(zvd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_079'] = {'inputs': ['zvd_replacement_079'], 'func': zvd_replacement_d2_079}


def zvd_replacement_d2_080(zvd_replacement_080):
    feature = _clean(zvd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_080'] = {'inputs': ['zvd_replacement_080'], 'func': zvd_replacement_d2_080}


def zvd_replacement_d2_081(zvd_replacement_081):
    feature = _clean(zvd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_081'] = {'inputs': ['zvd_replacement_081'], 'func': zvd_replacement_d2_081}


def zvd_replacement_d2_082(zvd_replacement_082):
    feature = _clean(zvd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_082'] = {'inputs': ['zvd_replacement_082'], 'func': zvd_replacement_d2_082}


def zvd_replacement_d2_083(zvd_replacement_083):
    feature = _clean(zvd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_083'] = {'inputs': ['zvd_replacement_083'], 'func': zvd_replacement_d2_083}


def zvd_replacement_d2_084(zvd_replacement_084):
    feature = _clean(zvd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_084'] = {'inputs': ['zvd_replacement_084'], 'func': zvd_replacement_d2_084}


def zvd_replacement_d2_085(zvd_replacement_085):
    feature = _clean(zvd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_085'] = {'inputs': ['zvd_replacement_085'], 'func': zvd_replacement_d2_085}


def zvd_replacement_d2_086(zvd_replacement_086):
    feature = _clean(zvd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_086'] = {'inputs': ['zvd_replacement_086'], 'func': zvd_replacement_d2_086}


def zvd_replacement_d2_087(zvd_replacement_087):
    feature = _clean(zvd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_087'] = {'inputs': ['zvd_replacement_087'], 'func': zvd_replacement_d2_087}


def zvd_replacement_d2_088(zvd_replacement_088):
    feature = _clean(zvd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_088'] = {'inputs': ['zvd_replacement_088'], 'func': zvd_replacement_d2_088}


def zvd_replacement_d2_089(zvd_replacement_089):
    feature = _clean(zvd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_089'] = {'inputs': ['zvd_replacement_089'], 'func': zvd_replacement_d2_089}


def zvd_replacement_d2_090(zvd_replacement_090):
    feature = _clean(zvd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_090'] = {'inputs': ['zvd_replacement_090'], 'func': zvd_replacement_d2_090}


def zvd_replacement_d2_091(zvd_replacement_091):
    feature = _clean(zvd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_091'] = {'inputs': ['zvd_replacement_091'], 'func': zvd_replacement_d2_091}


def zvd_replacement_d2_092(zvd_replacement_092):
    feature = _clean(zvd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_092'] = {'inputs': ['zvd_replacement_092'], 'func': zvd_replacement_d2_092}


def zvd_replacement_d2_093(zvd_replacement_093):
    feature = _clean(zvd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_093'] = {'inputs': ['zvd_replacement_093'], 'func': zvd_replacement_d2_093}


def zvd_replacement_d2_094(zvd_replacement_094):
    feature = _clean(zvd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_094'] = {'inputs': ['zvd_replacement_094'], 'func': zvd_replacement_d2_094}


def zvd_replacement_d2_095(zvd_replacement_095):
    feature = _clean(zvd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_095'] = {'inputs': ['zvd_replacement_095'], 'func': zvd_replacement_d2_095}


def zvd_replacement_d2_096(zvd_replacement_096):
    feature = _clean(zvd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_096'] = {'inputs': ['zvd_replacement_096'], 'func': zvd_replacement_d2_096}


def zvd_replacement_d2_097(zvd_replacement_097):
    feature = _clean(zvd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_097'] = {'inputs': ['zvd_replacement_097'], 'func': zvd_replacement_d2_097}


def zvd_replacement_d2_098(zvd_replacement_098):
    feature = _clean(zvd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_098'] = {'inputs': ['zvd_replacement_098'], 'func': zvd_replacement_d2_098}


def zvd_replacement_d2_099(zvd_replacement_099):
    feature = _clean(zvd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_099'] = {'inputs': ['zvd_replacement_099'], 'func': zvd_replacement_d2_099}


def zvd_replacement_d2_100(zvd_replacement_100):
    feature = _clean(zvd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_100'] = {'inputs': ['zvd_replacement_100'], 'func': zvd_replacement_d2_100}


def zvd_replacement_d2_101(zvd_replacement_101):
    feature = _clean(zvd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_101'] = {'inputs': ['zvd_replacement_101'], 'func': zvd_replacement_d2_101}


def zvd_replacement_d2_102(zvd_replacement_102):
    feature = _clean(zvd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_102'] = {'inputs': ['zvd_replacement_102'], 'func': zvd_replacement_d2_102}


def zvd_replacement_d2_103(zvd_replacement_103):
    feature = _clean(zvd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_103'] = {'inputs': ['zvd_replacement_103'], 'func': zvd_replacement_d2_103}


def zvd_replacement_d2_104(zvd_replacement_104):
    feature = _clean(zvd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_104'] = {'inputs': ['zvd_replacement_104'], 'func': zvd_replacement_d2_104}


def zvd_replacement_d2_105(zvd_replacement_105):
    feature = _clean(zvd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_105'] = {'inputs': ['zvd_replacement_105'], 'func': zvd_replacement_d2_105}


def zvd_replacement_d2_106(zvd_replacement_106):
    feature = _clean(zvd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_106'] = {'inputs': ['zvd_replacement_106'], 'func': zvd_replacement_d2_106}


def zvd_replacement_d2_107(zvd_replacement_107):
    feature = _clean(zvd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_107'] = {'inputs': ['zvd_replacement_107'], 'func': zvd_replacement_d2_107}


def zvd_replacement_d2_108(zvd_replacement_108):
    feature = _clean(zvd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_108'] = {'inputs': ['zvd_replacement_108'], 'func': zvd_replacement_d2_108}


def zvd_replacement_d2_109(zvd_replacement_109):
    feature = _clean(zvd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_109'] = {'inputs': ['zvd_replacement_109'], 'func': zvd_replacement_d2_109}


def zvd_replacement_d2_110(zvd_replacement_110):
    feature = _clean(zvd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_110'] = {'inputs': ['zvd_replacement_110'], 'func': zvd_replacement_d2_110}


def zvd_replacement_d2_111(zvd_replacement_111):
    feature = _clean(zvd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_111'] = {'inputs': ['zvd_replacement_111'], 'func': zvd_replacement_d2_111}


def zvd_replacement_d2_112(zvd_replacement_112):
    feature = _clean(zvd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_112'] = {'inputs': ['zvd_replacement_112'], 'func': zvd_replacement_d2_112}


def zvd_replacement_d2_113(zvd_replacement_113):
    feature = _clean(zvd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_113'] = {'inputs': ['zvd_replacement_113'], 'func': zvd_replacement_d2_113}


def zvd_replacement_d2_114(zvd_replacement_114):
    feature = _clean(zvd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_114'] = {'inputs': ['zvd_replacement_114'], 'func': zvd_replacement_d2_114}


def zvd_replacement_d2_115(zvd_replacement_115):
    feature = _clean(zvd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_115'] = {'inputs': ['zvd_replacement_115'], 'func': zvd_replacement_d2_115}


def zvd_replacement_d2_116(zvd_replacement_116):
    feature = _clean(zvd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_116'] = {'inputs': ['zvd_replacement_116'], 'func': zvd_replacement_d2_116}


def zvd_replacement_d2_117(zvd_replacement_117):
    feature = _clean(zvd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_117'] = {'inputs': ['zvd_replacement_117'], 'func': zvd_replacement_d2_117}


def zvd_replacement_d2_118(zvd_replacement_118):
    feature = _clean(zvd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_118'] = {'inputs': ['zvd_replacement_118'], 'func': zvd_replacement_d2_118}


def zvd_replacement_d2_119(zvd_replacement_119):
    feature = _clean(zvd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_119'] = {'inputs': ['zvd_replacement_119'], 'func': zvd_replacement_d2_119}


def zvd_replacement_d2_120(zvd_replacement_120):
    feature = _clean(zvd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_120'] = {'inputs': ['zvd_replacement_120'], 'func': zvd_replacement_d2_120}


def zvd_replacement_d2_121(zvd_replacement_121):
    feature = _clean(zvd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_121'] = {'inputs': ['zvd_replacement_121'], 'func': zvd_replacement_d2_121}


def zvd_replacement_d2_122(zvd_replacement_122):
    feature = _clean(zvd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_122'] = {'inputs': ['zvd_replacement_122'], 'func': zvd_replacement_d2_122}


def zvd_replacement_d2_123(zvd_replacement_123):
    feature = _clean(zvd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_123'] = {'inputs': ['zvd_replacement_123'], 'func': zvd_replacement_d2_123}


def zvd_replacement_d2_124(zvd_replacement_124):
    feature = _clean(zvd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_124'] = {'inputs': ['zvd_replacement_124'], 'func': zvd_replacement_d2_124}


def zvd_replacement_d2_125(zvd_replacement_125):
    feature = _clean(zvd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_125'] = {'inputs': ['zvd_replacement_125'], 'func': zvd_replacement_d2_125}


def zvd_replacement_d2_126(zvd_replacement_126):
    feature = _clean(zvd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_126'] = {'inputs': ['zvd_replacement_126'], 'func': zvd_replacement_d2_126}


def zvd_replacement_d2_127(zvd_replacement_127):
    feature = _clean(zvd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_127'] = {'inputs': ['zvd_replacement_127'], 'func': zvd_replacement_d2_127}


def zvd_replacement_d2_128(zvd_replacement_128):
    feature = _clean(zvd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_128'] = {'inputs': ['zvd_replacement_128'], 'func': zvd_replacement_d2_128}


def zvd_replacement_d2_129(zvd_replacement_129):
    feature = _clean(zvd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_129'] = {'inputs': ['zvd_replacement_129'], 'func': zvd_replacement_d2_129}


def zvd_replacement_d2_130(zvd_replacement_130):
    feature = _clean(zvd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_130'] = {'inputs': ['zvd_replacement_130'], 'func': zvd_replacement_d2_130}


def zvd_replacement_d2_131(zvd_replacement_131):
    feature = _clean(zvd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_131'] = {'inputs': ['zvd_replacement_131'], 'func': zvd_replacement_d2_131}


def zvd_replacement_d2_132(zvd_replacement_132):
    feature = _clean(zvd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_132'] = {'inputs': ['zvd_replacement_132'], 'func': zvd_replacement_d2_132}


def zvd_replacement_d2_133(zvd_replacement_133):
    feature = _clean(zvd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_133'] = {'inputs': ['zvd_replacement_133'], 'func': zvd_replacement_d2_133}


def zvd_replacement_d2_134(zvd_replacement_134):
    feature = _clean(zvd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_134'] = {'inputs': ['zvd_replacement_134'], 'func': zvd_replacement_d2_134}


def zvd_replacement_d2_135(zvd_replacement_135):
    feature = _clean(zvd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_135'] = {'inputs': ['zvd_replacement_135'], 'func': zvd_replacement_d2_135}


def zvd_replacement_d2_136(zvd_replacement_136):
    feature = _clean(zvd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_136'] = {'inputs': ['zvd_replacement_136'], 'func': zvd_replacement_d2_136}


def zvd_replacement_d2_137(zvd_replacement_137):
    feature = _clean(zvd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_137'] = {'inputs': ['zvd_replacement_137'], 'func': zvd_replacement_d2_137}


def zvd_replacement_d2_138(zvd_replacement_138):
    feature = _clean(zvd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_138'] = {'inputs': ['zvd_replacement_138'], 'func': zvd_replacement_d2_138}


def zvd_replacement_d2_139(zvd_replacement_139):
    feature = _clean(zvd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_139'] = {'inputs': ['zvd_replacement_139'], 'func': zvd_replacement_d2_139}


def zvd_replacement_d2_140(zvd_replacement_140):
    feature = _clean(zvd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_140'] = {'inputs': ['zvd_replacement_140'], 'func': zvd_replacement_d2_140}


def zvd_replacement_d2_141(zvd_replacement_141):
    feature = _clean(zvd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_141'] = {'inputs': ['zvd_replacement_141'], 'func': zvd_replacement_d2_141}


def zvd_replacement_d2_142(zvd_replacement_142):
    feature = _clean(zvd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_142'] = {'inputs': ['zvd_replacement_142'], 'func': zvd_replacement_d2_142}


def zvd_replacement_d2_143(zvd_replacement_143):
    feature = _clean(zvd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_143'] = {'inputs': ['zvd_replacement_143'], 'func': zvd_replacement_d2_143}


def zvd_replacement_d2_144(zvd_replacement_144):
    feature = _clean(zvd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_144'] = {'inputs': ['zvd_replacement_144'], 'func': zvd_replacement_d2_144}


def zvd_replacement_d2_145(zvd_replacement_145):
    feature = _clean(zvd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_145'] = {'inputs': ['zvd_replacement_145'], 'func': zvd_replacement_d2_145}


def zvd_replacement_d2_146(zvd_replacement_146):
    feature = _clean(zvd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_146'] = {'inputs': ['zvd_replacement_146'], 'func': zvd_replacement_d2_146}


def zvd_replacement_d2_147(zvd_replacement_147):
    feature = _clean(zvd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_147'] = {'inputs': ['zvd_replacement_147'], 'func': zvd_replacement_d2_147}


def zvd_replacement_d2_148(zvd_replacement_148):
    feature = _clean(zvd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_148'] = {'inputs': ['zvd_replacement_148'], 'func': zvd_replacement_d2_148}


def zvd_replacement_d2_149(zvd_replacement_149):
    feature = _clean(zvd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_149'] = {'inputs': ['zvd_replacement_149'], 'func': zvd_replacement_d2_149}


def zvd_replacement_d2_150(zvd_replacement_150):
    feature = _clean(zvd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_150'] = {'inputs': ['zvd_replacement_150'], 'func': zvd_replacement_d2_150}


def zvd_replacement_d2_151(zvd_replacement_151):
    feature = _clean(zvd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_151'] = {'inputs': ['zvd_replacement_151'], 'func': zvd_replacement_d2_151}


def zvd_replacement_d2_152(zvd_replacement_152):
    feature = _clean(zvd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_152'] = {'inputs': ['zvd_replacement_152'], 'func': zvd_replacement_d2_152}


def zvd_replacement_d2_153(zvd_replacement_153):
    feature = _clean(zvd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_153'] = {'inputs': ['zvd_replacement_153'], 'func': zvd_replacement_d2_153}


def zvd_replacement_d2_154(zvd_replacement_154):
    feature = _clean(zvd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_154'] = {'inputs': ['zvd_replacement_154'], 'func': zvd_replacement_d2_154}


def zvd_replacement_d2_155(zvd_replacement_155):
    feature = _clean(zvd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_155'] = {'inputs': ['zvd_replacement_155'], 'func': zvd_replacement_d2_155}


def zvd_replacement_d2_156(zvd_replacement_156):
    feature = _clean(zvd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_156'] = {'inputs': ['zvd_replacement_156'], 'func': zvd_replacement_d2_156}


def zvd_replacement_d2_157(zvd_replacement_157):
    feature = _clean(zvd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_157'] = {'inputs': ['zvd_replacement_157'], 'func': zvd_replacement_d2_157}


def zvd_replacement_d2_158(zvd_replacement_158):
    feature = _clean(zvd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_158'] = {'inputs': ['zvd_replacement_158'], 'func': zvd_replacement_d2_158}


def zvd_replacement_d2_159(zvd_replacement_159):
    feature = _clean(zvd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_159'] = {'inputs': ['zvd_replacement_159'], 'func': zvd_replacement_d2_159}


def zvd_replacement_d2_160(zvd_replacement_160):
    feature = _clean(zvd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_160'] = {'inputs': ['zvd_replacement_160'], 'func': zvd_replacement_d2_160}


def zvd_replacement_d2_161(zvd_replacement_161):
    feature = _clean(zvd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_161'] = {'inputs': ['zvd_replacement_161'], 'func': zvd_replacement_d2_161}


def zvd_replacement_d2_162(zvd_replacement_162):
    feature = _clean(zvd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_162'] = {'inputs': ['zvd_replacement_162'], 'func': zvd_replacement_d2_162}


def zvd_replacement_d2_163(zvd_replacement_163):
    feature = _clean(zvd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_163'] = {'inputs': ['zvd_replacement_163'], 'func': zvd_replacement_d2_163}


def zvd_replacement_d2_164(zvd_replacement_164):
    feature = _clean(zvd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_164'] = {'inputs': ['zvd_replacement_164'], 'func': zvd_replacement_d2_164}


def zvd_replacement_d2_165(zvd_replacement_165):
    feature = _clean(zvd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_165'] = {'inputs': ['zvd_replacement_165'], 'func': zvd_replacement_d2_165}


def zvd_replacement_d2_166(zvd_replacement_166):
    feature = _clean(zvd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_166'] = {'inputs': ['zvd_replacement_166'], 'func': zvd_replacement_d2_166}


def zvd_replacement_d2_167(zvd_replacement_167):
    feature = _clean(zvd_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_167'] = {'inputs': ['zvd_replacement_167'], 'func': zvd_replacement_d2_167}


def zvd_replacement_d2_168(zvd_replacement_168):
    feature = _clean(zvd_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_168'] = {'inputs': ['zvd_replacement_168'], 'func': zvd_replacement_d2_168}


def zvd_replacement_d2_169(zvd_replacement_169):
    feature = _clean(zvd_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_169'] = {'inputs': ['zvd_replacement_169'], 'func': zvd_replacement_d2_169}


def zvd_replacement_d2_170(zvd_replacement_170):
    feature = _clean(zvd_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
ZVD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['zvd_replacement_d2_170'] = {'inputs': ['zvd_replacement_170'], 'func': zvd_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002(zvd_002_zero_volume_frequency_10_002):
    return _base_universe_d2(zvd_002_zero_volume_frequency_10_002, 1)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002'] = {'inputs': ['zvd_002_zero_volume_frequency_10_002'], 'func': zvd_base_universe_d2_001_zvd_002_zero_volume_frequency_10_002}


def zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003(zvd_003_spread_proxy_21_003):
    return _base_universe_d2(zvd_003_spread_proxy_21_003, 2)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003'] = {'inputs': ['zvd_003_spread_proxy_21_003'], 'func': zvd_base_universe_d2_002_zvd_003_spread_proxy_21_003}


def zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004(zvd_004_trading_intensity_42_004):
    return _base_universe_d2(zvd_004_trading_intensity_42_004, 3)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004'] = {'inputs': ['zvd_004_trading_intensity_42_004'], 'func': zvd_base_universe_d2_003_zvd_004_trading_intensity_42_004}


def zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006(zvd_006_price_level_distress_84_006):
    return _base_universe_d2(zvd_006_price_level_distress_84_006, 4)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006'] = {'inputs': ['zvd_006_price_level_distress_84_006'], 'func': zvd_base_universe_d2_004_zvd_006_price_level_distress_84_006}


def zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008(zvd_008_zero_volume_frequency_189_008):
    return _base_universe_d2(zvd_008_zero_volume_frequency_189_008, 5)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008'] = {'inputs': ['zvd_008_zero_volume_frequency_189_008'], 'func': zvd_base_universe_d2_005_zvd_008_zero_volume_frequency_189_008}


def zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009(zvd_009_spread_proxy_252_009):
    return _base_universe_d2(zvd_009_spread_proxy_252_009, 6)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009'] = {'inputs': ['zvd_009_spread_proxy_252_009'], 'func': zvd_base_universe_d2_006_zvd_009_spread_proxy_252_009}


def zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010(zvd_010_trading_intensity_378_010):
    return _base_universe_d2(zvd_010_trading_intensity_378_010, 7)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010'] = {'inputs': ['zvd_010_trading_intensity_378_010'], 'func': zvd_base_universe_d2_007_zvd_010_trading_intensity_378_010}


def zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012(zvd_012_price_level_distress_756_012):
    return _base_universe_d2(zvd_012_price_level_distress_756_012, 8)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012'] = {'inputs': ['zvd_012_price_level_distress_756_012'], 'func': zvd_base_universe_d2_008_zvd_012_price_level_distress_756_012}


def zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014(zvd_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(zvd_014_zero_volume_frequency_1260_014, 9)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014'] = {'inputs': ['zvd_014_zero_volume_frequency_1260_014'], 'func': zvd_base_universe_d2_009_zvd_014_zero_volume_frequency_1260_014}


def zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015(zvd_015_spread_proxy_1512_015):
    return _base_universe_d2(zvd_015_spread_proxy_1512_015, 10)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015'] = {'inputs': ['zvd_015_spread_proxy_1512_015'], 'func': zvd_base_universe_d2_010_zvd_015_spread_proxy_1512_015}


def zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016(zvd_016_trading_intensity_5_016):
    return _base_universe_d2(zvd_016_trading_intensity_5_016, 11)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016'] = {'inputs': ['zvd_016_trading_intensity_5_016'], 'func': zvd_base_universe_d2_011_zvd_016_trading_intensity_5_016}


def zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018(zvd_018_price_level_distress_21_018):
    return _base_universe_d2(zvd_018_price_level_distress_21_018, 12)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018'] = {'inputs': ['zvd_018_price_level_distress_21_018'], 'func': zvd_base_universe_d2_012_zvd_018_price_level_distress_21_018}


def zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020(zvd_020_zero_volume_frequency_63_020):
    return _base_universe_d2(zvd_020_zero_volume_frequency_63_020, 13)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020'] = {'inputs': ['zvd_020_zero_volume_frequency_63_020'], 'func': zvd_base_universe_d2_013_zvd_020_zero_volume_frequency_63_020}


def zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021(zvd_021_spread_proxy_84_021):
    return _base_universe_d2(zvd_021_spread_proxy_84_021, 14)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021'] = {'inputs': ['zvd_021_spread_proxy_84_021'], 'func': zvd_base_universe_d2_014_zvd_021_spread_proxy_84_021}


def zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022(zvd_022_trading_intensity_126_022):
    return _base_universe_d2(zvd_022_trading_intensity_126_022, 15)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022'] = {'inputs': ['zvd_022_trading_intensity_126_022'], 'func': zvd_base_universe_d2_015_zvd_022_trading_intensity_126_022}


def zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024(zvd_024_price_level_distress_252_024):
    return _base_universe_d2(zvd_024_price_level_distress_252_024, 16)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024'] = {'inputs': ['zvd_024_price_level_distress_252_024'], 'func': zvd_base_universe_d2_016_zvd_024_price_level_distress_252_024}


def zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026(zvd_026_zero_volume_frequency_504_026):
    return _base_universe_d2(zvd_026_zero_volume_frequency_504_026, 17)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026'] = {'inputs': ['zvd_026_zero_volume_frequency_504_026'], 'func': zvd_base_universe_d2_017_zvd_026_zero_volume_frequency_504_026}


def zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027(zvd_027_spread_proxy_756_027):
    return _base_universe_d2(zvd_027_spread_proxy_756_027, 18)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027'] = {'inputs': ['zvd_027_spread_proxy_756_027'], 'func': zvd_base_universe_d2_018_zvd_027_spread_proxy_756_027}


def zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028(zvd_028_trading_intensity_1008_028):
    return _base_universe_d2(zvd_028_trading_intensity_1008_028, 19)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028'] = {'inputs': ['zvd_028_trading_intensity_1008_028'], 'func': zvd_base_universe_d2_019_zvd_028_trading_intensity_1008_028}


def zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030(zvd_030_price_level_distress_1512_030):
    return _base_universe_d2(zvd_030_price_level_distress_1512_030, 20)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030'] = {'inputs': ['zvd_030_price_level_distress_1512_030'], 'func': zvd_base_universe_d2_020_zvd_030_price_level_distress_1512_030}


def zvd_base_universe_d2_021_zvd_basefill_001(zvd_basefill_001):
    return _base_universe_d2(zvd_basefill_001, 21)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_021_zvd_basefill_001'] = {'inputs': ['zvd_basefill_001'], 'func': zvd_base_universe_d2_021_zvd_basefill_001}


def zvd_base_universe_d2_022_zvd_basefill_005(zvd_basefill_005):
    return _base_universe_d2(zvd_basefill_005, 22)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_022_zvd_basefill_005'] = {'inputs': ['zvd_basefill_005'], 'func': zvd_base_universe_d2_022_zvd_basefill_005}


def zvd_base_universe_d2_023_zvd_basefill_007(zvd_basefill_007):
    return _base_universe_d2(zvd_basefill_007, 23)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_023_zvd_basefill_007'] = {'inputs': ['zvd_basefill_007'], 'func': zvd_base_universe_d2_023_zvd_basefill_007}


def zvd_base_universe_d2_024_zvd_basefill_011(zvd_basefill_011):
    return _base_universe_d2(zvd_basefill_011, 24)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_024_zvd_basefill_011'] = {'inputs': ['zvd_basefill_011'], 'func': zvd_base_universe_d2_024_zvd_basefill_011}


def zvd_base_universe_d2_025_zvd_basefill_013(zvd_basefill_013):
    return _base_universe_d2(zvd_basefill_013, 25)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_025_zvd_basefill_013'] = {'inputs': ['zvd_basefill_013'], 'func': zvd_base_universe_d2_025_zvd_basefill_013}


def zvd_base_universe_d2_026_zvd_basefill_017(zvd_basefill_017):
    return _base_universe_d2(zvd_basefill_017, 26)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_026_zvd_basefill_017'] = {'inputs': ['zvd_basefill_017'], 'func': zvd_base_universe_d2_026_zvd_basefill_017}


def zvd_base_universe_d2_027_zvd_basefill_019(zvd_basefill_019):
    return _base_universe_d2(zvd_basefill_019, 27)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_027_zvd_basefill_019'] = {'inputs': ['zvd_basefill_019'], 'func': zvd_base_universe_d2_027_zvd_basefill_019}


def zvd_base_universe_d2_028_zvd_basefill_023(zvd_basefill_023):
    return _base_universe_d2(zvd_basefill_023, 28)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_028_zvd_basefill_023'] = {'inputs': ['zvd_basefill_023'], 'func': zvd_base_universe_d2_028_zvd_basefill_023}


def zvd_base_universe_d2_029_zvd_basefill_025(zvd_basefill_025):
    return _base_universe_d2(zvd_basefill_025, 29)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_029_zvd_basefill_025'] = {'inputs': ['zvd_basefill_025'], 'func': zvd_base_universe_d2_029_zvd_basefill_025}


def zvd_base_universe_d2_030_zvd_basefill_029(zvd_basefill_029):
    return _base_universe_d2(zvd_basefill_029, 30)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_030_zvd_basefill_029'] = {'inputs': ['zvd_basefill_029'], 'func': zvd_base_universe_d2_030_zvd_basefill_029}


def zvd_base_universe_d2_031_zvd_basefill_031(zvd_basefill_031):
    return _base_universe_d2(zvd_basefill_031, 31)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_031_zvd_basefill_031'] = {'inputs': ['zvd_basefill_031'], 'func': zvd_base_universe_d2_031_zvd_basefill_031}


def zvd_base_universe_d2_032_zvd_basefill_032(zvd_basefill_032):
    return _base_universe_d2(zvd_basefill_032, 32)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_032_zvd_basefill_032'] = {'inputs': ['zvd_basefill_032'], 'func': zvd_base_universe_d2_032_zvd_basefill_032}


def zvd_base_universe_d2_033_zvd_basefill_033(zvd_basefill_033):
    return _base_universe_d2(zvd_basefill_033, 33)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_033_zvd_basefill_033'] = {'inputs': ['zvd_basefill_033'], 'func': zvd_base_universe_d2_033_zvd_basefill_033}


def zvd_base_universe_d2_034_zvd_basefill_034(zvd_basefill_034):
    return _base_universe_d2(zvd_basefill_034, 34)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_034_zvd_basefill_034'] = {'inputs': ['zvd_basefill_034'], 'func': zvd_base_universe_d2_034_zvd_basefill_034}


def zvd_base_universe_d2_035_zvd_basefill_035(zvd_basefill_035):
    return _base_universe_d2(zvd_basefill_035, 35)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_035_zvd_basefill_035'] = {'inputs': ['zvd_basefill_035'], 'func': zvd_base_universe_d2_035_zvd_basefill_035}


def zvd_base_universe_d2_036_zvd_basefill_036(zvd_basefill_036):
    return _base_universe_d2(zvd_basefill_036, 36)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_036_zvd_basefill_036'] = {'inputs': ['zvd_basefill_036'], 'func': zvd_base_universe_d2_036_zvd_basefill_036}


def zvd_base_universe_d2_037_zvd_basefill_037(zvd_basefill_037):
    return _base_universe_d2(zvd_basefill_037, 37)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_037_zvd_basefill_037'] = {'inputs': ['zvd_basefill_037'], 'func': zvd_base_universe_d2_037_zvd_basefill_037}


def zvd_base_universe_d2_038_zvd_basefill_038(zvd_basefill_038):
    return _base_universe_d2(zvd_basefill_038, 38)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_038_zvd_basefill_038'] = {'inputs': ['zvd_basefill_038'], 'func': zvd_base_universe_d2_038_zvd_basefill_038}


def zvd_base_universe_d2_039_zvd_basefill_039(zvd_basefill_039):
    return _base_universe_d2(zvd_basefill_039, 39)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_039_zvd_basefill_039'] = {'inputs': ['zvd_basefill_039'], 'func': zvd_base_universe_d2_039_zvd_basefill_039}


def zvd_base_universe_d2_040_zvd_basefill_040(zvd_basefill_040):
    return _base_universe_d2(zvd_basefill_040, 40)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_040_zvd_basefill_040'] = {'inputs': ['zvd_basefill_040'], 'func': zvd_base_universe_d2_040_zvd_basefill_040}


def zvd_base_universe_d2_041_zvd_basefill_041(zvd_basefill_041):
    return _base_universe_d2(zvd_basefill_041, 41)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_041_zvd_basefill_041'] = {'inputs': ['zvd_basefill_041'], 'func': zvd_base_universe_d2_041_zvd_basefill_041}


def zvd_base_universe_d2_042_zvd_basefill_042(zvd_basefill_042):
    return _base_universe_d2(zvd_basefill_042, 42)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_042_zvd_basefill_042'] = {'inputs': ['zvd_basefill_042'], 'func': zvd_base_universe_d2_042_zvd_basefill_042}


def zvd_base_universe_d2_043_zvd_basefill_043(zvd_basefill_043):
    return _base_universe_d2(zvd_basefill_043, 43)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_043_zvd_basefill_043'] = {'inputs': ['zvd_basefill_043'], 'func': zvd_base_universe_d2_043_zvd_basefill_043}


def zvd_base_universe_d2_044_zvd_basefill_044(zvd_basefill_044):
    return _base_universe_d2(zvd_basefill_044, 44)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_044_zvd_basefill_044'] = {'inputs': ['zvd_basefill_044'], 'func': zvd_base_universe_d2_044_zvd_basefill_044}


def zvd_base_universe_d2_045_zvd_basefill_045(zvd_basefill_045):
    return _base_universe_d2(zvd_basefill_045, 45)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_045_zvd_basefill_045'] = {'inputs': ['zvd_basefill_045'], 'func': zvd_base_universe_d2_045_zvd_basefill_045}


def zvd_base_universe_d2_046_zvd_basefill_046(zvd_basefill_046):
    return _base_universe_d2(zvd_basefill_046, 46)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_046_zvd_basefill_046'] = {'inputs': ['zvd_basefill_046'], 'func': zvd_base_universe_d2_046_zvd_basefill_046}


def zvd_base_universe_d2_047_zvd_basefill_047(zvd_basefill_047):
    return _base_universe_d2(zvd_basefill_047, 47)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_047_zvd_basefill_047'] = {'inputs': ['zvd_basefill_047'], 'func': zvd_base_universe_d2_047_zvd_basefill_047}


def zvd_base_universe_d2_048_zvd_basefill_048(zvd_basefill_048):
    return _base_universe_d2(zvd_basefill_048, 48)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_048_zvd_basefill_048'] = {'inputs': ['zvd_basefill_048'], 'func': zvd_base_universe_d2_048_zvd_basefill_048}


def zvd_base_universe_d2_049_zvd_basefill_049(zvd_basefill_049):
    return _base_universe_d2(zvd_basefill_049, 49)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_049_zvd_basefill_049'] = {'inputs': ['zvd_basefill_049'], 'func': zvd_base_universe_d2_049_zvd_basefill_049}


def zvd_base_universe_d2_050_zvd_basefill_050(zvd_basefill_050):
    return _base_universe_d2(zvd_basefill_050, 50)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_050_zvd_basefill_050'] = {'inputs': ['zvd_basefill_050'], 'func': zvd_base_universe_d2_050_zvd_basefill_050}


def zvd_base_universe_d2_051_zvd_basefill_051(zvd_basefill_051):
    return _base_universe_d2(zvd_basefill_051, 51)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_051_zvd_basefill_051'] = {'inputs': ['zvd_basefill_051'], 'func': zvd_base_universe_d2_051_zvd_basefill_051}


def zvd_base_universe_d2_052_zvd_basefill_052(zvd_basefill_052):
    return _base_universe_d2(zvd_basefill_052, 52)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_052_zvd_basefill_052'] = {'inputs': ['zvd_basefill_052'], 'func': zvd_base_universe_d2_052_zvd_basefill_052}


def zvd_base_universe_d2_053_zvd_basefill_053(zvd_basefill_053):
    return _base_universe_d2(zvd_basefill_053, 53)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_053_zvd_basefill_053'] = {'inputs': ['zvd_basefill_053'], 'func': zvd_base_universe_d2_053_zvd_basefill_053}


def zvd_base_universe_d2_054_zvd_basefill_054(zvd_basefill_054):
    return _base_universe_d2(zvd_basefill_054, 54)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_054_zvd_basefill_054'] = {'inputs': ['zvd_basefill_054'], 'func': zvd_base_universe_d2_054_zvd_basefill_054}


def zvd_base_universe_d2_055_zvd_basefill_055(zvd_basefill_055):
    return _base_universe_d2(zvd_basefill_055, 55)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_055_zvd_basefill_055'] = {'inputs': ['zvd_basefill_055'], 'func': zvd_base_universe_d2_055_zvd_basefill_055}


def zvd_base_universe_d2_056_zvd_basefill_056(zvd_basefill_056):
    return _base_universe_d2(zvd_basefill_056, 56)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_056_zvd_basefill_056'] = {'inputs': ['zvd_basefill_056'], 'func': zvd_base_universe_d2_056_zvd_basefill_056}


def zvd_base_universe_d2_057_zvd_basefill_057(zvd_basefill_057):
    return _base_universe_d2(zvd_basefill_057, 57)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_057_zvd_basefill_057'] = {'inputs': ['zvd_basefill_057'], 'func': zvd_base_universe_d2_057_zvd_basefill_057}


def zvd_base_universe_d2_058_zvd_basefill_058(zvd_basefill_058):
    return _base_universe_d2(zvd_basefill_058, 58)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_058_zvd_basefill_058'] = {'inputs': ['zvd_basefill_058'], 'func': zvd_base_universe_d2_058_zvd_basefill_058}


def zvd_base_universe_d2_059_zvd_basefill_059(zvd_basefill_059):
    return _base_universe_d2(zvd_basefill_059, 59)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_059_zvd_basefill_059'] = {'inputs': ['zvd_basefill_059'], 'func': zvd_base_universe_d2_059_zvd_basefill_059}


def zvd_base_universe_d2_060_zvd_basefill_060(zvd_basefill_060):
    return _base_universe_d2(zvd_basefill_060, 60)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_060_zvd_basefill_060'] = {'inputs': ['zvd_basefill_060'], 'func': zvd_base_universe_d2_060_zvd_basefill_060}


def zvd_base_universe_d2_061_zvd_basefill_061(zvd_basefill_061):
    return _base_universe_d2(zvd_basefill_061, 61)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_061_zvd_basefill_061'] = {'inputs': ['zvd_basefill_061'], 'func': zvd_base_universe_d2_061_zvd_basefill_061}


def zvd_base_universe_d2_062_zvd_basefill_062(zvd_basefill_062):
    return _base_universe_d2(zvd_basefill_062, 62)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_062_zvd_basefill_062'] = {'inputs': ['zvd_basefill_062'], 'func': zvd_base_universe_d2_062_zvd_basefill_062}


def zvd_base_universe_d2_063_zvd_basefill_063(zvd_basefill_063):
    return _base_universe_d2(zvd_basefill_063, 63)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_063_zvd_basefill_063'] = {'inputs': ['zvd_basefill_063'], 'func': zvd_base_universe_d2_063_zvd_basefill_063}


def zvd_base_universe_d2_064_zvd_basefill_064(zvd_basefill_064):
    return _base_universe_d2(zvd_basefill_064, 64)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_064_zvd_basefill_064'] = {'inputs': ['zvd_basefill_064'], 'func': zvd_base_universe_d2_064_zvd_basefill_064}


def zvd_base_universe_d2_065_zvd_basefill_065(zvd_basefill_065):
    return _base_universe_d2(zvd_basefill_065, 65)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_065_zvd_basefill_065'] = {'inputs': ['zvd_basefill_065'], 'func': zvd_base_universe_d2_065_zvd_basefill_065}


def zvd_base_universe_d2_066_zvd_basefill_066(zvd_basefill_066):
    return _base_universe_d2(zvd_basefill_066, 66)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_066_zvd_basefill_066'] = {'inputs': ['zvd_basefill_066'], 'func': zvd_base_universe_d2_066_zvd_basefill_066}


def zvd_base_universe_d2_067_zvd_basefill_067(zvd_basefill_067):
    return _base_universe_d2(zvd_basefill_067, 67)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_067_zvd_basefill_067'] = {'inputs': ['zvd_basefill_067'], 'func': zvd_base_universe_d2_067_zvd_basefill_067}


def zvd_base_universe_d2_068_zvd_basefill_068(zvd_basefill_068):
    return _base_universe_d2(zvd_basefill_068, 68)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_068_zvd_basefill_068'] = {'inputs': ['zvd_basefill_068'], 'func': zvd_base_universe_d2_068_zvd_basefill_068}


def zvd_base_universe_d2_069_zvd_basefill_069(zvd_basefill_069):
    return _base_universe_d2(zvd_basefill_069, 69)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_069_zvd_basefill_069'] = {'inputs': ['zvd_basefill_069'], 'func': zvd_base_universe_d2_069_zvd_basefill_069}


def zvd_base_universe_d2_070_zvd_basefill_070(zvd_basefill_070):
    return _base_universe_d2(zvd_basefill_070, 70)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_070_zvd_basefill_070'] = {'inputs': ['zvd_basefill_070'], 'func': zvd_base_universe_d2_070_zvd_basefill_070}


def zvd_base_universe_d2_071_zvd_basefill_071(zvd_basefill_071):
    return _base_universe_d2(zvd_basefill_071, 71)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_071_zvd_basefill_071'] = {'inputs': ['zvd_basefill_071'], 'func': zvd_base_universe_d2_071_zvd_basefill_071}


def zvd_base_universe_d2_072_zvd_basefill_072(zvd_basefill_072):
    return _base_universe_d2(zvd_basefill_072, 72)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_072_zvd_basefill_072'] = {'inputs': ['zvd_basefill_072'], 'func': zvd_base_universe_d2_072_zvd_basefill_072}


def zvd_base_universe_d2_073_zvd_basefill_073(zvd_basefill_073):
    return _base_universe_d2(zvd_basefill_073, 73)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_073_zvd_basefill_073'] = {'inputs': ['zvd_basefill_073'], 'func': zvd_base_universe_d2_073_zvd_basefill_073}


def zvd_base_universe_d2_074_zvd_basefill_074(zvd_basefill_074):
    return _base_universe_d2(zvd_basefill_074, 74)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_074_zvd_basefill_074'] = {'inputs': ['zvd_basefill_074'], 'func': zvd_base_universe_d2_074_zvd_basefill_074}


def zvd_base_universe_d2_075_zvd_basefill_075(zvd_basefill_075):
    return _base_universe_d2(zvd_basefill_075, 75)
ZVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['zvd_base_universe_d2_075_zvd_basefill_075'] = {'inputs': ['zvd_basefill_075'], 'func': zvd_base_universe_d2_075_zvd_basefill_075}
