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



def rex_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def rex_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def rex_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def rex_154_rex_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def rex_155_rex_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















RANGE_EXPANSION_REGISTRY_2ND_DERIVATIVES = {
    'rex_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': rex_001_realized_vol_z_roc_1},
    'rex_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': rex_007_realized_vol_z_roc_5},
    'rex_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': rex_013_realized_vol_z_roc_42},
    'rex_154_rex_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': rex_154_rex_019_realized_vol_z_42_019_roc_126},
    'rex_155_rex_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': rex_155_rex_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def re_replacement_d2_001(re_replacement_001):
    feature = _clean(re_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_001'] = {'inputs': ['re_replacement_001'], 'func': re_replacement_d2_001}


def re_replacement_d2_002(re_replacement_002):
    feature = _clean(re_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_002'] = {'inputs': ['re_replacement_002'], 'func': re_replacement_d2_002}


def re_replacement_d2_003(re_replacement_003):
    feature = _clean(re_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_003'] = {'inputs': ['re_replacement_003'], 'func': re_replacement_d2_003}


def re_replacement_d2_004(re_replacement_004):
    feature = _clean(re_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_004'] = {'inputs': ['re_replacement_004'], 'func': re_replacement_d2_004}


def re_replacement_d2_005(re_replacement_005):
    feature = _clean(re_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_005'] = {'inputs': ['re_replacement_005'], 'func': re_replacement_d2_005}


def re_replacement_d2_006(re_replacement_006):
    feature = _clean(re_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_006'] = {'inputs': ['re_replacement_006'], 'func': re_replacement_d2_006}


def re_replacement_d2_007(re_replacement_007):
    feature = _clean(re_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_007'] = {'inputs': ['re_replacement_007'], 'func': re_replacement_d2_007}


def re_replacement_d2_008(re_replacement_008):
    feature = _clean(re_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_008'] = {'inputs': ['re_replacement_008'], 'func': re_replacement_d2_008}


def re_replacement_d2_009(re_replacement_009):
    feature = _clean(re_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_009'] = {'inputs': ['re_replacement_009'], 'func': re_replacement_d2_009}


def re_replacement_d2_010(re_replacement_010):
    feature = _clean(re_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_010'] = {'inputs': ['re_replacement_010'], 'func': re_replacement_d2_010}


def re_replacement_d2_011(re_replacement_011):
    feature = _clean(re_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_011'] = {'inputs': ['re_replacement_011'], 'func': re_replacement_d2_011}


def re_replacement_d2_012(re_replacement_012):
    feature = _clean(re_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_012'] = {'inputs': ['re_replacement_012'], 'func': re_replacement_d2_012}


def re_replacement_d2_013(re_replacement_013):
    feature = _clean(re_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_013'] = {'inputs': ['re_replacement_013'], 'func': re_replacement_d2_013}


def re_replacement_d2_014(re_replacement_014):
    feature = _clean(re_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_014'] = {'inputs': ['re_replacement_014'], 'func': re_replacement_d2_014}


def re_replacement_d2_015(re_replacement_015):
    feature = _clean(re_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_015'] = {'inputs': ['re_replacement_015'], 'func': re_replacement_d2_015}


def re_replacement_d2_016(re_replacement_016):
    feature = _clean(re_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_016'] = {'inputs': ['re_replacement_016'], 'func': re_replacement_d2_016}


def re_replacement_d2_017(re_replacement_017):
    feature = _clean(re_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_017'] = {'inputs': ['re_replacement_017'], 'func': re_replacement_d2_017}


def re_replacement_d2_018(re_replacement_018):
    feature = _clean(re_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_018'] = {'inputs': ['re_replacement_018'], 'func': re_replacement_d2_018}


def re_replacement_d2_019(re_replacement_019):
    feature = _clean(re_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_019'] = {'inputs': ['re_replacement_019'], 'func': re_replacement_d2_019}


def re_replacement_d2_020(re_replacement_020):
    feature = _clean(re_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_020'] = {'inputs': ['re_replacement_020'], 'func': re_replacement_d2_020}


def re_replacement_d2_021(re_replacement_021):
    feature = _clean(re_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_021'] = {'inputs': ['re_replacement_021'], 'func': re_replacement_d2_021}


def re_replacement_d2_022(re_replacement_022):
    feature = _clean(re_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_022'] = {'inputs': ['re_replacement_022'], 'func': re_replacement_d2_022}


def re_replacement_d2_023(re_replacement_023):
    feature = _clean(re_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_023'] = {'inputs': ['re_replacement_023'], 'func': re_replacement_d2_023}


def re_replacement_d2_024(re_replacement_024):
    feature = _clean(re_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_024'] = {'inputs': ['re_replacement_024'], 'func': re_replacement_d2_024}


def re_replacement_d2_025(re_replacement_025):
    feature = _clean(re_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_025'] = {'inputs': ['re_replacement_025'], 'func': re_replacement_d2_025}


def re_replacement_d2_026(re_replacement_026):
    feature = _clean(re_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_026'] = {'inputs': ['re_replacement_026'], 'func': re_replacement_d2_026}


def re_replacement_d2_027(re_replacement_027):
    feature = _clean(re_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_027'] = {'inputs': ['re_replacement_027'], 'func': re_replacement_d2_027}


def re_replacement_d2_028(re_replacement_028):
    feature = _clean(re_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_028'] = {'inputs': ['re_replacement_028'], 'func': re_replacement_d2_028}


def re_replacement_d2_029(re_replacement_029):
    feature = _clean(re_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_029'] = {'inputs': ['re_replacement_029'], 'func': re_replacement_d2_029}


def re_replacement_d2_030(re_replacement_030):
    feature = _clean(re_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_030'] = {'inputs': ['re_replacement_030'], 'func': re_replacement_d2_030}


def re_replacement_d2_031(re_replacement_031):
    feature = _clean(re_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_031'] = {'inputs': ['re_replacement_031'], 'func': re_replacement_d2_031}


def re_replacement_d2_032(re_replacement_032):
    feature = _clean(re_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_032'] = {'inputs': ['re_replacement_032'], 'func': re_replacement_d2_032}


def re_replacement_d2_033(re_replacement_033):
    feature = _clean(re_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_033'] = {'inputs': ['re_replacement_033'], 'func': re_replacement_d2_033}


def re_replacement_d2_034(re_replacement_034):
    feature = _clean(re_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_034'] = {'inputs': ['re_replacement_034'], 'func': re_replacement_d2_034}


def re_replacement_d2_035(re_replacement_035):
    feature = _clean(re_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_035'] = {'inputs': ['re_replacement_035'], 'func': re_replacement_d2_035}


def re_replacement_d2_036(re_replacement_036):
    feature = _clean(re_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_036'] = {'inputs': ['re_replacement_036'], 'func': re_replacement_d2_036}


def re_replacement_d2_037(re_replacement_037):
    feature = _clean(re_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_037'] = {'inputs': ['re_replacement_037'], 'func': re_replacement_d2_037}


def re_replacement_d2_038(re_replacement_038):
    feature = _clean(re_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_038'] = {'inputs': ['re_replacement_038'], 'func': re_replacement_d2_038}


def re_replacement_d2_039(re_replacement_039):
    feature = _clean(re_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_039'] = {'inputs': ['re_replacement_039'], 'func': re_replacement_d2_039}


def re_replacement_d2_040(re_replacement_040):
    feature = _clean(re_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_040'] = {'inputs': ['re_replacement_040'], 'func': re_replacement_d2_040}


def re_replacement_d2_041(re_replacement_041):
    feature = _clean(re_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_041'] = {'inputs': ['re_replacement_041'], 'func': re_replacement_d2_041}


def re_replacement_d2_042(re_replacement_042):
    feature = _clean(re_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_042'] = {'inputs': ['re_replacement_042'], 'func': re_replacement_d2_042}


def re_replacement_d2_043(re_replacement_043):
    feature = _clean(re_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_043'] = {'inputs': ['re_replacement_043'], 'func': re_replacement_d2_043}


def re_replacement_d2_044(re_replacement_044):
    feature = _clean(re_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_044'] = {'inputs': ['re_replacement_044'], 'func': re_replacement_d2_044}


def re_replacement_d2_045(re_replacement_045):
    feature = _clean(re_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_045'] = {'inputs': ['re_replacement_045'], 'func': re_replacement_d2_045}


def re_replacement_d2_046(re_replacement_046):
    feature = _clean(re_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_046'] = {'inputs': ['re_replacement_046'], 'func': re_replacement_d2_046}


def re_replacement_d2_047(re_replacement_047):
    feature = _clean(re_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_047'] = {'inputs': ['re_replacement_047'], 'func': re_replacement_d2_047}


def re_replacement_d2_048(re_replacement_048):
    feature = _clean(re_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_048'] = {'inputs': ['re_replacement_048'], 'func': re_replacement_d2_048}


def re_replacement_d2_049(re_replacement_049):
    feature = _clean(re_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_049'] = {'inputs': ['re_replacement_049'], 'func': re_replacement_d2_049}


def re_replacement_d2_050(re_replacement_050):
    feature = _clean(re_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_050'] = {'inputs': ['re_replacement_050'], 'func': re_replacement_d2_050}


def re_replacement_d2_051(re_replacement_051):
    feature = _clean(re_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_051'] = {'inputs': ['re_replacement_051'], 'func': re_replacement_d2_051}


def re_replacement_d2_052(re_replacement_052):
    feature = _clean(re_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_052'] = {'inputs': ['re_replacement_052'], 'func': re_replacement_d2_052}


def re_replacement_d2_053(re_replacement_053):
    feature = _clean(re_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_053'] = {'inputs': ['re_replacement_053'], 'func': re_replacement_d2_053}


def re_replacement_d2_054(re_replacement_054):
    feature = _clean(re_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_054'] = {'inputs': ['re_replacement_054'], 'func': re_replacement_d2_054}


def re_replacement_d2_055(re_replacement_055):
    feature = _clean(re_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_055'] = {'inputs': ['re_replacement_055'], 'func': re_replacement_d2_055}


def re_replacement_d2_056(re_replacement_056):
    feature = _clean(re_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_056'] = {'inputs': ['re_replacement_056'], 'func': re_replacement_d2_056}


def re_replacement_d2_057(re_replacement_057):
    feature = _clean(re_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_057'] = {'inputs': ['re_replacement_057'], 'func': re_replacement_d2_057}


def re_replacement_d2_058(re_replacement_058):
    feature = _clean(re_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_058'] = {'inputs': ['re_replacement_058'], 'func': re_replacement_d2_058}


def re_replacement_d2_059(re_replacement_059):
    feature = _clean(re_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_059'] = {'inputs': ['re_replacement_059'], 'func': re_replacement_d2_059}


def re_replacement_d2_060(re_replacement_060):
    feature = _clean(re_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_060'] = {'inputs': ['re_replacement_060'], 'func': re_replacement_d2_060}


def re_replacement_d2_061(re_replacement_061):
    feature = _clean(re_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_061'] = {'inputs': ['re_replacement_061'], 'func': re_replacement_d2_061}


def re_replacement_d2_062(re_replacement_062):
    feature = _clean(re_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_062'] = {'inputs': ['re_replacement_062'], 'func': re_replacement_d2_062}


def re_replacement_d2_063(re_replacement_063):
    feature = _clean(re_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_063'] = {'inputs': ['re_replacement_063'], 'func': re_replacement_d2_063}


def re_replacement_d2_064(re_replacement_064):
    feature = _clean(re_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_064'] = {'inputs': ['re_replacement_064'], 'func': re_replacement_d2_064}


def re_replacement_d2_065(re_replacement_065):
    feature = _clean(re_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_065'] = {'inputs': ['re_replacement_065'], 'func': re_replacement_d2_065}


def re_replacement_d2_066(re_replacement_066):
    feature = _clean(re_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_066'] = {'inputs': ['re_replacement_066'], 'func': re_replacement_d2_066}


def re_replacement_d2_067(re_replacement_067):
    feature = _clean(re_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_067'] = {'inputs': ['re_replacement_067'], 'func': re_replacement_d2_067}


def re_replacement_d2_068(re_replacement_068):
    feature = _clean(re_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_068'] = {'inputs': ['re_replacement_068'], 'func': re_replacement_d2_068}


def re_replacement_d2_069(re_replacement_069):
    feature = _clean(re_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_069'] = {'inputs': ['re_replacement_069'], 'func': re_replacement_d2_069}


def re_replacement_d2_070(re_replacement_070):
    feature = _clean(re_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_070'] = {'inputs': ['re_replacement_070'], 'func': re_replacement_d2_070}


def re_replacement_d2_071(re_replacement_071):
    feature = _clean(re_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_071'] = {'inputs': ['re_replacement_071'], 'func': re_replacement_d2_071}


def re_replacement_d2_072(re_replacement_072):
    feature = _clean(re_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_072'] = {'inputs': ['re_replacement_072'], 'func': re_replacement_d2_072}


def re_replacement_d2_073(re_replacement_073):
    feature = _clean(re_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_073'] = {'inputs': ['re_replacement_073'], 'func': re_replacement_d2_073}


def re_replacement_d2_074(re_replacement_074):
    feature = _clean(re_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_074'] = {'inputs': ['re_replacement_074'], 'func': re_replacement_d2_074}


def re_replacement_d2_075(re_replacement_075):
    feature = _clean(re_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_075'] = {'inputs': ['re_replacement_075'], 'func': re_replacement_d2_075}


def re_replacement_d2_076(re_replacement_076):
    feature = _clean(re_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_076'] = {'inputs': ['re_replacement_076'], 'func': re_replacement_d2_076}


def re_replacement_d2_077(re_replacement_077):
    feature = _clean(re_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_077'] = {'inputs': ['re_replacement_077'], 'func': re_replacement_d2_077}


def re_replacement_d2_078(re_replacement_078):
    feature = _clean(re_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_078'] = {'inputs': ['re_replacement_078'], 'func': re_replacement_d2_078}


def re_replacement_d2_079(re_replacement_079):
    feature = _clean(re_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_079'] = {'inputs': ['re_replacement_079'], 'func': re_replacement_d2_079}


def re_replacement_d2_080(re_replacement_080):
    feature = _clean(re_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_080'] = {'inputs': ['re_replacement_080'], 'func': re_replacement_d2_080}


def re_replacement_d2_081(re_replacement_081):
    feature = _clean(re_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_081'] = {'inputs': ['re_replacement_081'], 'func': re_replacement_d2_081}


def re_replacement_d2_082(re_replacement_082):
    feature = _clean(re_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_082'] = {'inputs': ['re_replacement_082'], 'func': re_replacement_d2_082}


def re_replacement_d2_083(re_replacement_083):
    feature = _clean(re_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_083'] = {'inputs': ['re_replacement_083'], 'func': re_replacement_d2_083}


def re_replacement_d2_084(re_replacement_084):
    feature = _clean(re_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_084'] = {'inputs': ['re_replacement_084'], 'func': re_replacement_d2_084}


def re_replacement_d2_085(re_replacement_085):
    feature = _clean(re_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_085'] = {'inputs': ['re_replacement_085'], 'func': re_replacement_d2_085}


def re_replacement_d2_086(re_replacement_086):
    feature = _clean(re_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_086'] = {'inputs': ['re_replacement_086'], 'func': re_replacement_d2_086}


def re_replacement_d2_087(re_replacement_087):
    feature = _clean(re_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_087'] = {'inputs': ['re_replacement_087'], 'func': re_replacement_d2_087}


def re_replacement_d2_088(re_replacement_088):
    feature = _clean(re_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_088'] = {'inputs': ['re_replacement_088'], 'func': re_replacement_d2_088}


def re_replacement_d2_089(re_replacement_089):
    feature = _clean(re_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_089'] = {'inputs': ['re_replacement_089'], 'func': re_replacement_d2_089}


def re_replacement_d2_090(re_replacement_090):
    feature = _clean(re_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_090'] = {'inputs': ['re_replacement_090'], 'func': re_replacement_d2_090}


def re_replacement_d2_091(re_replacement_091):
    feature = _clean(re_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_091'] = {'inputs': ['re_replacement_091'], 'func': re_replacement_d2_091}


def re_replacement_d2_092(re_replacement_092):
    feature = _clean(re_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_092'] = {'inputs': ['re_replacement_092'], 'func': re_replacement_d2_092}


def re_replacement_d2_093(re_replacement_093):
    feature = _clean(re_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_093'] = {'inputs': ['re_replacement_093'], 'func': re_replacement_d2_093}


def re_replacement_d2_094(re_replacement_094):
    feature = _clean(re_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_094'] = {'inputs': ['re_replacement_094'], 'func': re_replacement_d2_094}


def re_replacement_d2_095(re_replacement_095):
    feature = _clean(re_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_095'] = {'inputs': ['re_replacement_095'], 'func': re_replacement_d2_095}


def re_replacement_d2_096(re_replacement_096):
    feature = _clean(re_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_096'] = {'inputs': ['re_replacement_096'], 'func': re_replacement_d2_096}


def re_replacement_d2_097(re_replacement_097):
    feature = _clean(re_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_097'] = {'inputs': ['re_replacement_097'], 'func': re_replacement_d2_097}


def re_replacement_d2_098(re_replacement_098):
    feature = _clean(re_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_098'] = {'inputs': ['re_replacement_098'], 'func': re_replacement_d2_098}


def re_replacement_d2_099(re_replacement_099):
    feature = _clean(re_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_099'] = {'inputs': ['re_replacement_099'], 'func': re_replacement_d2_099}


def re_replacement_d2_100(re_replacement_100):
    feature = _clean(re_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_100'] = {'inputs': ['re_replacement_100'], 'func': re_replacement_d2_100}


def re_replacement_d2_101(re_replacement_101):
    feature = _clean(re_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_101'] = {'inputs': ['re_replacement_101'], 'func': re_replacement_d2_101}


def re_replacement_d2_102(re_replacement_102):
    feature = _clean(re_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_102'] = {'inputs': ['re_replacement_102'], 'func': re_replacement_d2_102}


def re_replacement_d2_103(re_replacement_103):
    feature = _clean(re_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_103'] = {'inputs': ['re_replacement_103'], 'func': re_replacement_d2_103}


def re_replacement_d2_104(re_replacement_104):
    feature = _clean(re_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_104'] = {'inputs': ['re_replacement_104'], 'func': re_replacement_d2_104}


def re_replacement_d2_105(re_replacement_105):
    feature = _clean(re_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_105'] = {'inputs': ['re_replacement_105'], 'func': re_replacement_d2_105}


def re_replacement_d2_106(re_replacement_106):
    feature = _clean(re_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_106'] = {'inputs': ['re_replacement_106'], 'func': re_replacement_d2_106}


def re_replacement_d2_107(re_replacement_107):
    feature = _clean(re_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_107'] = {'inputs': ['re_replacement_107'], 'func': re_replacement_d2_107}


def re_replacement_d2_108(re_replacement_108):
    feature = _clean(re_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_108'] = {'inputs': ['re_replacement_108'], 'func': re_replacement_d2_108}


def re_replacement_d2_109(re_replacement_109):
    feature = _clean(re_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_109'] = {'inputs': ['re_replacement_109'], 'func': re_replacement_d2_109}


def re_replacement_d2_110(re_replacement_110):
    feature = _clean(re_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_110'] = {'inputs': ['re_replacement_110'], 'func': re_replacement_d2_110}


def re_replacement_d2_111(re_replacement_111):
    feature = _clean(re_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_111'] = {'inputs': ['re_replacement_111'], 'func': re_replacement_d2_111}


def re_replacement_d2_112(re_replacement_112):
    feature = _clean(re_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_112'] = {'inputs': ['re_replacement_112'], 'func': re_replacement_d2_112}


def re_replacement_d2_113(re_replacement_113):
    feature = _clean(re_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_113'] = {'inputs': ['re_replacement_113'], 'func': re_replacement_d2_113}


def re_replacement_d2_114(re_replacement_114):
    feature = _clean(re_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_114'] = {'inputs': ['re_replacement_114'], 'func': re_replacement_d2_114}


def re_replacement_d2_115(re_replacement_115):
    feature = _clean(re_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_115'] = {'inputs': ['re_replacement_115'], 'func': re_replacement_d2_115}


def re_replacement_d2_116(re_replacement_116):
    feature = _clean(re_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_116'] = {'inputs': ['re_replacement_116'], 'func': re_replacement_d2_116}


def re_replacement_d2_117(re_replacement_117):
    feature = _clean(re_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_117'] = {'inputs': ['re_replacement_117'], 'func': re_replacement_d2_117}


def re_replacement_d2_118(re_replacement_118):
    feature = _clean(re_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_118'] = {'inputs': ['re_replacement_118'], 'func': re_replacement_d2_118}


def re_replacement_d2_119(re_replacement_119):
    feature = _clean(re_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_119'] = {'inputs': ['re_replacement_119'], 'func': re_replacement_d2_119}


def re_replacement_d2_120(re_replacement_120):
    feature = _clean(re_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_120'] = {'inputs': ['re_replacement_120'], 'func': re_replacement_d2_120}


def re_replacement_d2_121(re_replacement_121):
    feature = _clean(re_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_121'] = {'inputs': ['re_replacement_121'], 'func': re_replacement_d2_121}


def re_replacement_d2_122(re_replacement_122):
    feature = _clean(re_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_122'] = {'inputs': ['re_replacement_122'], 'func': re_replacement_d2_122}


def re_replacement_d2_123(re_replacement_123):
    feature = _clean(re_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_123'] = {'inputs': ['re_replacement_123'], 'func': re_replacement_d2_123}


def re_replacement_d2_124(re_replacement_124):
    feature = _clean(re_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_124'] = {'inputs': ['re_replacement_124'], 'func': re_replacement_d2_124}


def re_replacement_d2_125(re_replacement_125):
    feature = _clean(re_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_125'] = {'inputs': ['re_replacement_125'], 'func': re_replacement_d2_125}


def re_replacement_d2_126(re_replacement_126):
    feature = _clean(re_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_126'] = {'inputs': ['re_replacement_126'], 'func': re_replacement_d2_126}


def re_replacement_d2_127(re_replacement_127):
    feature = _clean(re_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_127'] = {'inputs': ['re_replacement_127'], 'func': re_replacement_d2_127}


def re_replacement_d2_128(re_replacement_128):
    feature = _clean(re_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_128'] = {'inputs': ['re_replacement_128'], 'func': re_replacement_d2_128}


def re_replacement_d2_129(re_replacement_129):
    feature = _clean(re_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_129'] = {'inputs': ['re_replacement_129'], 'func': re_replacement_d2_129}


def re_replacement_d2_130(re_replacement_130):
    feature = _clean(re_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_130'] = {'inputs': ['re_replacement_130'], 'func': re_replacement_d2_130}


def re_replacement_d2_131(re_replacement_131):
    feature = _clean(re_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_131'] = {'inputs': ['re_replacement_131'], 'func': re_replacement_d2_131}


def re_replacement_d2_132(re_replacement_132):
    feature = _clean(re_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_132'] = {'inputs': ['re_replacement_132'], 'func': re_replacement_d2_132}


def re_replacement_d2_133(re_replacement_133):
    feature = _clean(re_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_133'] = {'inputs': ['re_replacement_133'], 'func': re_replacement_d2_133}


def re_replacement_d2_134(re_replacement_134):
    feature = _clean(re_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_134'] = {'inputs': ['re_replacement_134'], 'func': re_replacement_d2_134}


def re_replacement_d2_135(re_replacement_135):
    feature = _clean(re_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_135'] = {'inputs': ['re_replacement_135'], 'func': re_replacement_d2_135}


def re_replacement_d2_136(re_replacement_136):
    feature = _clean(re_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_136'] = {'inputs': ['re_replacement_136'], 'func': re_replacement_d2_136}


def re_replacement_d2_137(re_replacement_137):
    feature = _clean(re_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_137'] = {'inputs': ['re_replacement_137'], 'func': re_replacement_d2_137}


def re_replacement_d2_138(re_replacement_138):
    feature = _clean(re_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_138'] = {'inputs': ['re_replacement_138'], 'func': re_replacement_d2_138}


def re_replacement_d2_139(re_replacement_139):
    feature = _clean(re_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_139'] = {'inputs': ['re_replacement_139'], 'func': re_replacement_d2_139}


def re_replacement_d2_140(re_replacement_140):
    feature = _clean(re_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_140'] = {'inputs': ['re_replacement_140'], 'func': re_replacement_d2_140}


def re_replacement_d2_141(re_replacement_141):
    feature = _clean(re_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_141'] = {'inputs': ['re_replacement_141'], 'func': re_replacement_d2_141}


def re_replacement_d2_142(re_replacement_142):
    feature = _clean(re_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_142'] = {'inputs': ['re_replacement_142'], 'func': re_replacement_d2_142}


def re_replacement_d2_143(re_replacement_143):
    feature = _clean(re_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_143'] = {'inputs': ['re_replacement_143'], 'func': re_replacement_d2_143}


def re_replacement_d2_144(re_replacement_144):
    feature = _clean(re_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_144'] = {'inputs': ['re_replacement_144'], 'func': re_replacement_d2_144}


def re_replacement_d2_145(re_replacement_145):
    feature = _clean(re_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_145'] = {'inputs': ['re_replacement_145'], 'func': re_replacement_d2_145}


def re_replacement_d2_146(re_replacement_146):
    feature = _clean(re_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_146'] = {'inputs': ['re_replacement_146'], 'func': re_replacement_d2_146}


def re_replacement_d2_147(re_replacement_147):
    feature = _clean(re_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_147'] = {'inputs': ['re_replacement_147'], 'func': re_replacement_d2_147}


def re_replacement_d2_148(re_replacement_148):
    feature = _clean(re_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_148'] = {'inputs': ['re_replacement_148'], 'func': re_replacement_d2_148}


def re_replacement_d2_149(re_replacement_149):
    feature = _clean(re_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_149'] = {'inputs': ['re_replacement_149'], 'func': re_replacement_d2_149}


def re_replacement_d2_150(re_replacement_150):
    feature = _clean(re_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_150'] = {'inputs': ['re_replacement_150'], 'func': re_replacement_d2_150}


def re_replacement_d2_151(re_replacement_151):
    feature = _clean(re_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_151'] = {'inputs': ['re_replacement_151'], 'func': re_replacement_d2_151}


def re_replacement_d2_152(re_replacement_152):
    feature = _clean(re_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_152'] = {'inputs': ['re_replacement_152'], 'func': re_replacement_d2_152}


def re_replacement_d2_153(re_replacement_153):
    feature = _clean(re_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_153'] = {'inputs': ['re_replacement_153'], 'func': re_replacement_d2_153}


def re_replacement_d2_154(re_replacement_154):
    feature = _clean(re_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_154'] = {'inputs': ['re_replacement_154'], 'func': re_replacement_d2_154}


def re_replacement_d2_155(re_replacement_155):
    feature = _clean(re_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_155'] = {'inputs': ['re_replacement_155'], 'func': re_replacement_d2_155}


def re_replacement_d2_156(re_replacement_156):
    feature = _clean(re_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_156'] = {'inputs': ['re_replacement_156'], 'func': re_replacement_d2_156}


def re_replacement_d2_157(re_replacement_157):
    feature = _clean(re_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_157'] = {'inputs': ['re_replacement_157'], 'func': re_replacement_d2_157}


def re_replacement_d2_158(re_replacement_158):
    feature = _clean(re_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_158'] = {'inputs': ['re_replacement_158'], 'func': re_replacement_d2_158}


def re_replacement_d2_159(re_replacement_159):
    feature = _clean(re_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_159'] = {'inputs': ['re_replacement_159'], 'func': re_replacement_d2_159}


def re_replacement_d2_160(re_replacement_160):
    feature = _clean(re_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_160'] = {'inputs': ['re_replacement_160'], 'func': re_replacement_d2_160}


def re_replacement_d2_161(re_replacement_161):
    feature = _clean(re_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_161'] = {'inputs': ['re_replacement_161'], 'func': re_replacement_d2_161}


def re_replacement_d2_162(re_replacement_162):
    feature = _clean(re_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_162'] = {'inputs': ['re_replacement_162'], 'func': re_replacement_d2_162}


def re_replacement_d2_163(re_replacement_163):
    feature = _clean(re_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_163'] = {'inputs': ['re_replacement_163'], 'func': re_replacement_d2_163}


def re_replacement_d2_164(re_replacement_164):
    feature = _clean(re_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_164'] = {'inputs': ['re_replacement_164'], 'func': re_replacement_d2_164}


def re_replacement_d2_165(re_replacement_165):
    feature = _clean(re_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_165'] = {'inputs': ['re_replacement_165'], 'func': re_replacement_d2_165}


def re_replacement_d2_166(re_replacement_166):
    feature = _clean(re_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_166'] = {'inputs': ['re_replacement_166'], 'func': re_replacement_d2_166}


def re_replacement_d2_167(re_replacement_167):
    feature = _clean(re_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_167'] = {'inputs': ['re_replacement_167'], 'func': re_replacement_d2_167}


def re_replacement_d2_168(re_replacement_168):
    feature = _clean(re_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_168'] = {'inputs': ['re_replacement_168'], 'func': re_replacement_d2_168}


def re_replacement_d2_169(re_replacement_169):
    feature = _clean(re_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_169'] = {'inputs': ['re_replacement_169'], 'func': re_replacement_d2_169}


def re_replacement_d2_170(re_replacement_170):
    feature = _clean(re_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_170'] = {'inputs': ['re_replacement_170'], 'func': re_replacement_d2_170}


def re_replacement_d2_171(re_replacement_171):
    feature = _clean(re_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_171'] = {'inputs': ['re_replacement_171'], 'func': re_replacement_d2_171}


def re_replacement_d2_172(re_replacement_172):
    feature = _clean(re_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_172'] = {'inputs': ['re_replacement_172'], 'func': re_replacement_d2_172}


def re_replacement_d2_173(re_replacement_173):
    feature = _clean(re_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_173'] = {'inputs': ['re_replacement_173'], 'func': re_replacement_d2_173}


def re_replacement_d2_174(re_replacement_174):
    feature = _clean(re_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_174'] = {'inputs': ['re_replacement_174'], 'func': re_replacement_d2_174}


def re_replacement_d2_175(re_replacement_175):
    feature = _clean(re_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
RE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['re_replacement_d2_175'] = {'inputs': ['re_replacement_175'], 'func': re_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rex_base_universe_d2_001_rex_002_range_expansion_10_002(rex_002_range_expansion_10_002):
    return _base_universe_d2(rex_002_range_expansion_10_002, 1)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_001_rex_002_range_expansion_10_002'] = {'inputs': ['rex_002_range_expansion_10_002'], 'func': rex_base_universe_d2_001_rex_002_range_expansion_10_002}


def rex_base_universe_d2_002_rex_004_close_location_42_004(rex_004_close_location_42_004):
    return _base_universe_d2(rex_004_close_location_42_004, 2)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_002_rex_004_close_location_42_004'] = {'inputs': ['rex_004_close_location_42_004'], 'func': rex_base_universe_d2_002_rex_004_close_location_42_004}


def rex_base_universe_d2_003_rex_005_atr_move_63_005(rex_005_atr_move_63_005):
    return _base_universe_d2(rex_005_atr_move_63_005, 3)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_003_rex_005_atr_move_63_005'] = {'inputs': ['rex_005_atr_move_63_005'], 'func': rex_base_universe_d2_003_rex_005_atr_move_63_005}


def rex_base_universe_d2_004_rex_008_range_expansion_189_008(rex_008_range_expansion_189_008):
    return _base_universe_d2(rex_008_range_expansion_189_008, 4)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_004_rex_008_range_expansion_189_008'] = {'inputs': ['rex_008_range_expansion_189_008'], 'func': rex_base_universe_d2_004_rex_008_range_expansion_189_008}


def rex_base_universe_d2_005_rex_010_close_location_378_010(rex_010_close_location_378_010):
    return _base_universe_d2(rex_010_close_location_378_010, 5)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_005_rex_010_close_location_378_010'] = {'inputs': ['rex_010_close_location_378_010'], 'func': rex_base_universe_d2_005_rex_010_close_location_378_010}


def rex_base_universe_d2_006_rex_011_atr_move_504_011(rex_011_atr_move_504_011):
    return _base_universe_d2(rex_011_atr_move_504_011, 6)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_006_rex_011_atr_move_504_011'] = {'inputs': ['rex_011_atr_move_504_011'], 'func': rex_base_universe_d2_006_rex_011_atr_move_504_011}


def rex_base_universe_d2_007_rex_014_range_expansion_1260_014(rex_014_range_expansion_1260_014):
    return _base_universe_d2(rex_014_range_expansion_1260_014, 7)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_007_rex_014_range_expansion_1260_014'] = {'inputs': ['rex_014_range_expansion_1260_014'], 'func': rex_base_universe_d2_007_rex_014_range_expansion_1260_014}


def rex_base_universe_d2_008_rex_016_close_location_5_016(rex_016_close_location_5_016):
    return _base_universe_d2(rex_016_close_location_5_016, 8)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_008_rex_016_close_location_5_016'] = {'inputs': ['rex_016_close_location_5_016'], 'func': rex_base_universe_d2_008_rex_016_close_location_5_016}


def rex_base_universe_d2_009_rex_017_atr_move_10_017(rex_017_atr_move_10_017):
    return _base_universe_d2(rex_017_atr_move_10_017, 9)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_009_rex_017_atr_move_10_017'] = {'inputs': ['rex_017_atr_move_10_017'], 'func': rex_base_universe_d2_009_rex_017_atr_move_10_017}


def rex_base_universe_d2_010_rex_020_range_expansion_63_020(rex_020_range_expansion_63_020):
    return _base_universe_d2(rex_020_range_expansion_63_020, 10)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_010_rex_020_range_expansion_63_020'] = {'inputs': ['rex_020_range_expansion_63_020'], 'func': rex_base_universe_d2_010_rex_020_range_expansion_63_020}


def rex_base_universe_d2_011_rex_022_close_location_126_022(rex_022_close_location_126_022):
    return _base_universe_d2(rex_022_close_location_126_022, 11)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_011_rex_022_close_location_126_022'] = {'inputs': ['rex_022_close_location_126_022'], 'func': rex_base_universe_d2_011_rex_022_close_location_126_022}


def rex_base_universe_d2_012_rex_023_atr_move_189_023(rex_023_atr_move_189_023):
    return _base_universe_d2(rex_023_atr_move_189_023, 12)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_012_rex_023_atr_move_189_023'] = {'inputs': ['rex_023_atr_move_189_023'], 'func': rex_base_universe_d2_012_rex_023_atr_move_189_023}


def rex_base_universe_d2_013_rex_026_range_expansion_504_026(rex_026_range_expansion_504_026):
    return _base_universe_d2(rex_026_range_expansion_504_026, 13)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_013_rex_026_range_expansion_504_026'] = {'inputs': ['rex_026_range_expansion_504_026'], 'func': rex_base_universe_d2_013_rex_026_range_expansion_504_026}


def rex_base_universe_d2_014_rex_028_close_location_1008_028(rex_028_close_location_1008_028):
    return _base_universe_d2(rex_028_close_location_1008_028, 14)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_014_rex_028_close_location_1008_028'] = {'inputs': ['rex_028_close_location_1008_028'], 'func': rex_base_universe_d2_014_rex_028_close_location_1008_028}


def rex_base_universe_d2_015_rex_029_atr_move_1260_029(rex_029_atr_move_1260_029):
    return _base_universe_d2(rex_029_atr_move_1260_029, 15)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_015_rex_029_atr_move_1260_029'] = {'inputs': ['rex_029_atr_move_1260_029'], 'func': rex_base_universe_d2_015_rex_029_atr_move_1260_029}


def rex_base_universe_d2_016_rex_basefill_001(rex_basefill_001):
    return _base_universe_d2(rex_basefill_001, 16)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_016_rex_basefill_001'] = {'inputs': ['rex_basefill_001'], 'func': rex_base_universe_d2_016_rex_basefill_001}


def rex_base_universe_d2_017_rex_basefill_003(rex_basefill_003):
    return _base_universe_d2(rex_basefill_003, 17)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_017_rex_basefill_003'] = {'inputs': ['rex_basefill_003'], 'func': rex_base_universe_d2_017_rex_basefill_003}


def rex_base_universe_d2_018_rex_basefill_006(rex_basefill_006):
    return _base_universe_d2(rex_basefill_006, 18)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_018_rex_basefill_006'] = {'inputs': ['rex_basefill_006'], 'func': rex_base_universe_d2_018_rex_basefill_006}


def rex_base_universe_d2_019_rex_basefill_007(rex_basefill_007):
    return _base_universe_d2(rex_basefill_007, 19)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_019_rex_basefill_007'] = {'inputs': ['rex_basefill_007'], 'func': rex_base_universe_d2_019_rex_basefill_007}


def rex_base_universe_d2_020_rex_basefill_009(rex_basefill_009):
    return _base_universe_d2(rex_basefill_009, 20)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_020_rex_basefill_009'] = {'inputs': ['rex_basefill_009'], 'func': rex_base_universe_d2_020_rex_basefill_009}


def rex_base_universe_d2_021_rex_basefill_012(rex_basefill_012):
    return _base_universe_d2(rex_basefill_012, 21)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_021_rex_basefill_012'] = {'inputs': ['rex_basefill_012'], 'func': rex_base_universe_d2_021_rex_basefill_012}


def rex_base_universe_d2_022_rex_basefill_013(rex_basefill_013):
    return _base_universe_d2(rex_basefill_013, 22)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_022_rex_basefill_013'] = {'inputs': ['rex_basefill_013'], 'func': rex_base_universe_d2_022_rex_basefill_013}


def rex_base_universe_d2_023_rex_basefill_015(rex_basefill_015):
    return _base_universe_d2(rex_basefill_015, 23)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_023_rex_basefill_015'] = {'inputs': ['rex_basefill_015'], 'func': rex_base_universe_d2_023_rex_basefill_015}


def rex_base_universe_d2_024_rex_basefill_018(rex_basefill_018):
    return _base_universe_d2(rex_basefill_018, 24)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_024_rex_basefill_018'] = {'inputs': ['rex_basefill_018'], 'func': rex_base_universe_d2_024_rex_basefill_018}


def rex_base_universe_d2_025_rex_basefill_019(rex_basefill_019):
    return _base_universe_d2(rex_basefill_019, 25)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_025_rex_basefill_019'] = {'inputs': ['rex_basefill_019'], 'func': rex_base_universe_d2_025_rex_basefill_019}


def rex_base_universe_d2_026_rex_basefill_021(rex_basefill_021):
    return _base_universe_d2(rex_basefill_021, 26)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_026_rex_basefill_021'] = {'inputs': ['rex_basefill_021'], 'func': rex_base_universe_d2_026_rex_basefill_021}


def rex_base_universe_d2_027_rex_basefill_024(rex_basefill_024):
    return _base_universe_d2(rex_basefill_024, 27)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_027_rex_basefill_024'] = {'inputs': ['rex_basefill_024'], 'func': rex_base_universe_d2_027_rex_basefill_024}


def rex_base_universe_d2_028_rex_basefill_025(rex_basefill_025):
    return _base_universe_d2(rex_basefill_025, 28)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_028_rex_basefill_025'] = {'inputs': ['rex_basefill_025'], 'func': rex_base_universe_d2_028_rex_basefill_025}


def rex_base_universe_d2_029_rex_basefill_027(rex_basefill_027):
    return _base_universe_d2(rex_basefill_027, 29)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_029_rex_basefill_027'] = {'inputs': ['rex_basefill_027'], 'func': rex_base_universe_d2_029_rex_basefill_027}


def rex_base_universe_d2_030_rex_basefill_030(rex_basefill_030):
    return _base_universe_d2(rex_basefill_030, 30)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_030_rex_basefill_030'] = {'inputs': ['rex_basefill_030'], 'func': rex_base_universe_d2_030_rex_basefill_030}


def rex_base_universe_d2_031_rex_basefill_031(rex_basefill_031):
    return _base_universe_d2(rex_basefill_031, 31)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_031_rex_basefill_031'] = {'inputs': ['rex_basefill_031'], 'func': rex_base_universe_d2_031_rex_basefill_031}


def rex_base_universe_d2_032_rex_basefill_032(rex_basefill_032):
    return _base_universe_d2(rex_basefill_032, 32)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_032_rex_basefill_032'] = {'inputs': ['rex_basefill_032'], 'func': rex_base_universe_d2_032_rex_basefill_032}


def rex_base_universe_d2_033_rex_basefill_033(rex_basefill_033):
    return _base_universe_d2(rex_basefill_033, 33)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_033_rex_basefill_033'] = {'inputs': ['rex_basefill_033'], 'func': rex_base_universe_d2_033_rex_basefill_033}


def rex_base_universe_d2_034_rex_basefill_034(rex_basefill_034):
    return _base_universe_d2(rex_basefill_034, 34)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_034_rex_basefill_034'] = {'inputs': ['rex_basefill_034'], 'func': rex_base_universe_d2_034_rex_basefill_034}


def rex_base_universe_d2_035_rex_basefill_035(rex_basefill_035):
    return _base_universe_d2(rex_basefill_035, 35)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_035_rex_basefill_035'] = {'inputs': ['rex_basefill_035'], 'func': rex_base_universe_d2_035_rex_basefill_035}


def rex_base_universe_d2_036_rex_basefill_036(rex_basefill_036):
    return _base_universe_d2(rex_basefill_036, 36)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_036_rex_basefill_036'] = {'inputs': ['rex_basefill_036'], 'func': rex_base_universe_d2_036_rex_basefill_036}


def rex_base_universe_d2_037_rex_basefill_037(rex_basefill_037):
    return _base_universe_d2(rex_basefill_037, 37)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_037_rex_basefill_037'] = {'inputs': ['rex_basefill_037'], 'func': rex_base_universe_d2_037_rex_basefill_037}


def rex_base_universe_d2_038_rex_basefill_038(rex_basefill_038):
    return _base_universe_d2(rex_basefill_038, 38)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_038_rex_basefill_038'] = {'inputs': ['rex_basefill_038'], 'func': rex_base_universe_d2_038_rex_basefill_038}


def rex_base_universe_d2_039_rex_basefill_039(rex_basefill_039):
    return _base_universe_d2(rex_basefill_039, 39)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_039_rex_basefill_039'] = {'inputs': ['rex_basefill_039'], 'func': rex_base_universe_d2_039_rex_basefill_039}


def rex_base_universe_d2_040_rex_basefill_040(rex_basefill_040):
    return _base_universe_d2(rex_basefill_040, 40)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_040_rex_basefill_040'] = {'inputs': ['rex_basefill_040'], 'func': rex_base_universe_d2_040_rex_basefill_040}


def rex_base_universe_d2_041_rex_basefill_041(rex_basefill_041):
    return _base_universe_d2(rex_basefill_041, 41)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_041_rex_basefill_041'] = {'inputs': ['rex_basefill_041'], 'func': rex_base_universe_d2_041_rex_basefill_041}


def rex_base_universe_d2_042_rex_basefill_042(rex_basefill_042):
    return _base_universe_d2(rex_basefill_042, 42)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_042_rex_basefill_042'] = {'inputs': ['rex_basefill_042'], 'func': rex_base_universe_d2_042_rex_basefill_042}


def rex_base_universe_d2_043_rex_basefill_043(rex_basefill_043):
    return _base_universe_d2(rex_basefill_043, 43)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_043_rex_basefill_043'] = {'inputs': ['rex_basefill_043'], 'func': rex_base_universe_d2_043_rex_basefill_043}


def rex_base_universe_d2_044_rex_basefill_044(rex_basefill_044):
    return _base_universe_d2(rex_basefill_044, 44)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_044_rex_basefill_044'] = {'inputs': ['rex_basefill_044'], 'func': rex_base_universe_d2_044_rex_basefill_044}


def rex_base_universe_d2_045_rex_basefill_045(rex_basefill_045):
    return _base_universe_d2(rex_basefill_045, 45)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_045_rex_basefill_045'] = {'inputs': ['rex_basefill_045'], 'func': rex_base_universe_d2_045_rex_basefill_045}


def rex_base_universe_d2_046_rex_basefill_046(rex_basefill_046):
    return _base_universe_d2(rex_basefill_046, 46)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_046_rex_basefill_046'] = {'inputs': ['rex_basefill_046'], 'func': rex_base_universe_d2_046_rex_basefill_046}


def rex_base_universe_d2_047_rex_basefill_047(rex_basefill_047):
    return _base_universe_d2(rex_basefill_047, 47)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_047_rex_basefill_047'] = {'inputs': ['rex_basefill_047'], 'func': rex_base_universe_d2_047_rex_basefill_047}


def rex_base_universe_d2_048_rex_basefill_048(rex_basefill_048):
    return _base_universe_d2(rex_basefill_048, 48)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_048_rex_basefill_048'] = {'inputs': ['rex_basefill_048'], 'func': rex_base_universe_d2_048_rex_basefill_048}


def rex_base_universe_d2_049_rex_basefill_049(rex_basefill_049):
    return _base_universe_d2(rex_basefill_049, 49)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_049_rex_basefill_049'] = {'inputs': ['rex_basefill_049'], 'func': rex_base_universe_d2_049_rex_basefill_049}


def rex_base_universe_d2_050_rex_basefill_050(rex_basefill_050):
    return _base_universe_d2(rex_basefill_050, 50)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_050_rex_basefill_050'] = {'inputs': ['rex_basefill_050'], 'func': rex_base_universe_d2_050_rex_basefill_050}


def rex_base_universe_d2_051_rex_basefill_051(rex_basefill_051):
    return _base_universe_d2(rex_basefill_051, 51)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_051_rex_basefill_051'] = {'inputs': ['rex_basefill_051'], 'func': rex_base_universe_d2_051_rex_basefill_051}


def rex_base_universe_d2_052_rex_basefill_052(rex_basefill_052):
    return _base_universe_d2(rex_basefill_052, 52)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_052_rex_basefill_052'] = {'inputs': ['rex_basefill_052'], 'func': rex_base_universe_d2_052_rex_basefill_052}


def rex_base_universe_d2_053_rex_basefill_053(rex_basefill_053):
    return _base_universe_d2(rex_basefill_053, 53)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_053_rex_basefill_053'] = {'inputs': ['rex_basefill_053'], 'func': rex_base_universe_d2_053_rex_basefill_053}


def rex_base_universe_d2_054_rex_basefill_054(rex_basefill_054):
    return _base_universe_d2(rex_basefill_054, 54)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_054_rex_basefill_054'] = {'inputs': ['rex_basefill_054'], 'func': rex_base_universe_d2_054_rex_basefill_054}


def rex_base_universe_d2_055_rex_basefill_055(rex_basefill_055):
    return _base_universe_d2(rex_basefill_055, 55)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_055_rex_basefill_055'] = {'inputs': ['rex_basefill_055'], 'func': rex_base_universe_d2_055_rex_basefill_055}


def rex_base_universe_d2_056_rex_basefill_056(rex_basefill_056):
    return _base_universe_d2(rex_basefill_056, 56)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_056_rex_basefill_056'] = {'inputs': ['rex_basefill_056'], 'func': rex_base_universe_d2_056_rex_basefill_056}


def rex_base_universe_d2_057_rex_basefill_057(rex_basefill_057):
    return _base_universe_d2(rex_basefill_057, 57)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_057_rex_basefill_057'] = {'inputs': ['rex_basefill_057'], 'func': rex_base_universe_d2_057_rex_basefill_057}


def rex_base_universe_d2_058_rex_basefill_058(rex_basefill_058):
    return _base_universe_d2(rex_basefill_058, 58)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_058_rex_basefill_058'] = {'inputs': ['rex_basefill_058'], 'func': rex_base_universe_d2_058_rex_basefill_058}


def rex_base_universe_d2_059_rex_basefill_059(rex_basefill_059):
    return _base_universe_d2(rex_basefill_059, 59)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_059_rex_basefill_059'] = {'inputs': ['rex_basefill_059'], 'func': rex_base_universe_d2_059_rex_basefill_059}


def rex_base_universe_d2_060_rex_basefill_060(rex_basefill_060):
    return _base_universe_d2(rex_basefill_060, 60)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_060_rex_basefill_060'] = {'inputs': ['rex_basefill_060'], 'func': rex_base_universe_d2_060_rex_basefill_060}


def rex_base_universe_d2_061_rex_basefill_061(rex_basefill_061):
    return _base_universe_d2(rex_basefill_061, 61)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_061_rex_basefill_061'] = {'inputs': ['rex_basefill_061'], 'func': rex_base_universe_d2_061_rex_basefill_061}


def rex_base_universe_d2_062_rex_basefill_062(rex_basefill_062):
    return _base_universe_d2(rex_basefill_062, 62)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_062_rex_basefill_062'] = {'inputs': ['rex_basefill_062'], 'func': rex_base_universe_d2_062_rex_basefill_062}


def rex_base_universe_d2_063_rex_basefill_063(rex_basefill_063):
    return _base_universe_d2(rex_basefill_063, 63)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_063_rex_basefill_063'] = {'inputs': ['rex_basefill_063'], 'func': rex_base_universe_d2_063_rex_basefill_063}


def rex_base_universe_d2_064_rex_basefill_064(rex_basefill_064):
    return _base_universe_d2(rex_basefill_064, 64)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_064_rex_basefill_064'] = {'inputs': ['rex_basefill_064'], 'func': rex_base_universe_d2_064_rex_basefill_064}


def rex_base_universe_d2_065_rex_basefill_065(rex_basefill_065):
    return _base_universe_d2(rex_basefill_065, 65)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_065_rex_basefill_065'] = {'inputs': ['rex_basefill_065'], 'func': rex_base_universe_d2_065_rex_basefill_065}


def rex_base_universe_d2_066_rex_basefill_066(rex_basefill_066):
    return _base_universe_d2(rex_basefill_066, 66)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_066_rex_basefill_066'] = {'inputs': ['rex_basefill_066'], 'func': rex_base_universe_d2_066_rex_basefill_066}


def rex_base_universe_d2_067_rex_basefill_067(rex_basefill_067):
    return _base_universe_d2(rex_basefill_067, 67)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_067_rex_basefill_067'] = {'inputs': ['rex_basefill_067'], 'func': rex_base_universe_d2_067_rex_basefill_067}


def rex_base_universe_d2_068_rex_basefill_068(rex_basefill_068):
    return _base_universe_d2(rex_basefill_068, 68)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_068_rex_basefill_068'] = {'inputs': ['rex_basefill_068'], 'func': rex_base_universe_d2_068_rex_basefill_068}


def rex_base_universe_d2_069_rex_basefill_069(rex_basefill_069):
    return _base_universe_d2(rex_basefill_069, 69)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_069_rex_basefill_069'] = {'inputs': ['rex_basefill_069'], 'func': rex_base_universe_d2_069_rex_basefill_069}


def rex_base_universe_d2_070_rex_basefill_070(rex_basefill_070):
    return _base_universe_d2(rex_basefill_070, 70)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_070_rex_basefill_070'] = {'inputs': ['rex_basefill_070'], 'func': rex_base_universe_d2_070_rex_basefill_070}


def rex_base_universe_d2_071_rex_basefill_071(rex_basefill_071):
    return _base_universe_d2(rex_basefill_071, 71)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_071_rex_basefill_071'] = {'inputs': ['rex_basefill_071'], 'func': rex_base_universe_d2_071_rex_basefill_071}


def rex_base_universe_d2_072_rex_basefill_072(rex_basefill_072):
    return _base_universe_d2(rex_basefill_072, 72)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_072_rex_basefill_072'] = {'inputs': ['rex_basefill_072'], 'func': rex_base_universe_d2_072_rex_basefill_072}


def rex_base_universe_d2_073_rex_basefill_073(rex_basefill_073):
    return _base_universe_d2(rex_basefill_073, 73)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_073_rex_basefill_073'] = {'inputs': ['rex_basefill_073'], 'func': rex_base_universe_d2_073_rex_basefill_073}


def rex_base_universe_d2_074_rex_basefill_074(rex_basefill_074):
    return _base_universe_d2(rex_basefill_074, 74)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_074_rex_basefill_074'] = {'inputs': ['rex_basefill_074'], 'func': rex_base_universe_d2_074_rex_basefill_074}


def rex_base_universe_d2_075_rex_basefill_075(rex_basefill_075):
    return _base_universe_d2(rex_basefill_075, 75)
REX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rex_base_universe_d2_075_rex_basefill_075'] = {'inputs': ['rex_basefill_075'], 'func': rex_base_universe_d2_075_rex_basefill_075}
