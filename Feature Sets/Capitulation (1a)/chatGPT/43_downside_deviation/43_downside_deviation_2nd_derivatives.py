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



def dsd_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def dsd_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def dsd_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def dsd_154_dsd_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def dsd_155_dsd_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















DOWNSIDE_DEVIATION_REGISTRY_2ND_DERIVATIVES = {
    'dsd_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': dsd_001_realized_vol_z_roc_1},
    'dsd_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': dsd_007_realized_vol_z_roc_5},
    'dsd_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': dsd_013_realized_vol_z_roc_42},
    'dsd_154_dsd_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': dsd_154_dsd_019_realized_vol_z_42_019_roc_126},
    'dsd_155_dsd_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': dsd_155_dsd_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def dd_replacement_d2_001(dd_replacement_001):
    feature = _clean(dd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_001'] = {'inputs': ['dd_replacement_001'], 'func': dd_replacement_d2_001}


def dd_replacement_d2_002(dd_replacement_002):
    feature = _clean(dd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_002'] = {'inputs': ['dd_replacement_002'], 'func': dd_replacement_d2_002}


def dd_replacement_d2_003(dd_replacement_003):
    feature = _clean(dd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_003'] = {'inputs': ['dd_replacement_003'], 'func': dd_replacement_d2_003}


def dd_replacement_d2_004(dd_replacement_004):
    feature = _clean(dd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_004'] = {'inputs': ['dd_replacement_004'], 'func': dd_replacement_d2_004}


def dd_replacement_d2_005(dd_replacement_005):
    feature = _clean(dd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_005'] = {'inputs': ['dd_replacement_005'], 'func': dd_replacement_d2_005}


def dd_replacement_d2_006(dd_replacement_006):
    feature = _clean(dd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_006'] = {'inputs': ['dd_replacement_006'], 'func': dd_replacement_d2_006}


def dd_replacement_d2_007(dd_replacement_007):
    feature = _clean(dd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_007'] = {'inputs': ['dd_replacement_007'], 'func': dd_replacement_d2_007}


def dd_replacement_d2_008(dd_replacement_008):
    feature = _clean(dd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_008'] = {'inputs': ['dd_replacement_008'], 'func': dd_replacement_d2_008}


def dd_replacement_d2_009(dd_replacement_009):
    feature = _clean(dd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_009'] = {'inputs': ['dd_replacement_009'], 'func': dd_replacement_d2_009}


def dd_replacement_d2_010(dd_replacement_010):
    feature = _clean(dd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_010'] = {'inputs': ['dd_replacement_010'], 'func': dd_replacement_d2_010}


def dd_replacement_d2_011(dd_replacement_011):
    feature = _clean(dd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_011'] = {'inputs': ['dd_replacement_011'], 'func': dd_replacement_d2_011}


def dd_replacement_d2_012(dd_replacement_012):
    feature = _clean(dd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_012'] = {'inputs': ['dd_replacement_012'], 'func': dd_replacement_d2_012}


def dd_replacement_d2_013(dd_replacement_013):
    feature = _clean(dd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_013'] = {'inputs': ['dd_replacement_013'], 'func': dd_replacement_d2_013}


def dd_replacement_d2_014(dd_replacement_014):
    feature = _clean(dd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_014'] = {'inputs': ['dd_replacement_014'], 'func': dd_replacement_d2_014}


def dd_replacement_d2_015(dd_replacement_015):
    feature = _clean(dd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_015'] = {'inputs': ['dd_replacement_015'], 'func': dd_replacement_d2_015}


def dd_replacement_d2_016(dd_replacement_016):
    feature = _clean(dd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_016'] = {'inputs': ['dd_replacement_016'], 'func': dd_replacement_d2_016}


def dd_replacement_d2_017(dd_replacement_017):
    feature = _clean(dd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_017'] = {'inputs': ['dd_replacement_017'], 'func': dd_replacement_d2_017}


def dd_replacement_d2_018(dd_replacement_018):
    feature = _clean(dd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_018'] = {'inputs': ['dd_replacement_018'], 'func': dd_replacement_d2_018}


def dd_replacement_d2_019(dd_replacement_019):
    feature = _clean(dd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_019'] = {'inputs': ['dd_replacement_019'], 'func': dd_replacement_d2_019}


def dd_replacement_d2_020(dd_replacement_020):
    feature = _clean(dd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_020'] = {'inputs': ['dd_replacement_020'], 'func': dd_replacement_d2_020}


def dd_replacement_d2_021(dd_replacement_021):
    feature = _clean(dd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_021'] = {'inputs': ['dd_replacement_021'], 'func': dd_replacement_d2_021}


def dd_replacement_d2_022(dd_replacement_022):
    feature = _clean(dd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_022'] = {'inputs': ['dd_replacement_022'], 'func': dd_replacement_d2_022}


def dd_replacement_d2_023(dd_replacement_023):
    feature = _clean(dd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_023'] = {'inputs': ['dd_replacement_023'], 'func': dd_replacement_d2_023}


def dd_replacement_d2_024(dd_replacement_024):
    feature = _clean(dd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_024'] = {'inputs': ['dd_replacement_024'], 'func': dd_replacement_d2_024}


def dd_replacement_d2_025(dd_replacement_025):
    feature = _clean(dd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_025'] = {'inputs': ['dd_replacement_025'], 'func': dd_replacement_d2_025}


def dd_replacement_d2_026(dd_replacement_026):
    feature = _clean(dd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_026'] = {'inputs': ['dd_replacement_026'], 'func': dd_replacement_d2_026}


def dd_replacement_d2_027(dd_replacement_027):
    feature = _clean(dd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_027'] = {'inputs': ['dd_replacement_027'], 'func': dd_replacement_d2_027}


def dd_replacement_d2_028(dd_replacement_028):
    feature = _clean(dd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_028'] = {'inputs': ['dd_replacement_028'], 'func': dd_replacement_d2_028}


def dd_replacement_d2_029(dd_replacement_029):
    feature = _clean(dd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_029'] = {'inputs': ['dd_replacement_029'], 'func': dd_replacement_d2_029}


def dd_replacement_d2_030(dd_replacement_030):
    feature = _clean(dd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_030'] = {'inputs': ['dd_replacement_030'], 'func': dd_replacement_d2_030}


def dd_replacement_d2_031(dd_replacement_031):
    feature = _clean(dd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_031'] = {'inputs': ['dd_replacement_031'], 'func': dd_replacement_d2_031}


def dd_replacement_d2_032(dd_replacement_032):
    feature = _clean(dd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_032'] = {'inputs': ['dd_replacement_032'], 'func': dd_replacement_d2_032}


def dd_replacement_d2_033(dd_replacement_033):
    feature = _clean(dd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_033'] = {'inputs': ['dd_replacement_033'], 'func': dd_replacement_d2_033}


def dd_replacement_d2_034(dd_replacement_034):
    feature = _clean(dd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_034'] = {'inputs': ['dd_replacement_034'], 'func': dd_replacement_d2_034}


def dd_replacement_d2_035(dd_replacement_035):
    feature = _clean(dd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_035'] = {'inputs': ['dd_replacement_035'], 'func': dd_replacement_d2_035}


def dd_replacement_d2_036(dd_replacement_036):
    feature = _clean(dd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_036'] = {'inputs': ['dd_replacement_036'], 'func': dd_replacement_d2_036}


def dd_replacement_d2_037(dd_replacement_037):
    feature = _clean(dd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_037'] = {'inputs': ['dd_replacement_037'], 'func': dd_replacement_d2_037}


def dd_replacement_d2_038(dd_replacement_038):
    feature = _clean(dd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_038'] = {'inputs': ['dd_replacement_038'], 'func': dd_replacement_d2_038}


def dd_replacement_d2_039(dd_replacement_039):
    feature = _clean(dd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_039'] = {'inputs': ['dd_replacement_039'], 'func': dd_replacement_d2_039}


def dd_replacement_d2_040(dd_replacement_040):
    feature = _clean(dd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_040'] = {'inputs': ['dd_replacement_040'], 'func': dd_replacement_d2_040}


def dd_replacement_d2_041(dd_replacement_041):
    feature = _clean(dd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_041'] = {'inputs': ['dd_replacement_041'], 'func': dd_replacement_d2_041}


def dd_replacement_d2_042(dd_replacement_042):
    feature = _clean(dd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_042'] = {'inputs': ['dd_replacement_042'], 'func': dd_replacement_d2_042}


def dd_replacement_d2_043(dd_replacement_043):
    feature = _clean(dd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_043'] = {'inputs': ['dd_replacement_043'], 'func': dd_replacement_d2_043}


def dd_replacement_d2_044(dd_replacement_044):
    feature = _clean(dd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_044'] = {'inputs': ['dd_replacement_044'], 'func': dd_replacement_d2_044}


def dd_replacement_d2_045(dd_replacement_045):
    feature = _clean(dd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_045'] = {'inputs': ['dd_replacement_045'], 'func': dd_replacement_d2_045}


def dd_replacement_d2_046(dd_replacement_046):
    feature = _clean(dd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_046'] = {'inputs': ['dd_replacement_046'], 'func': dd_replacement_d2_046}


def dd_replacement_d2_047(dd_replacement_047):
    feature = _clean(dd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_047'] = {'inputs': ['dd_replacement_047'], 'func': dd_replacement_d2_047}


def dd_replacement_d2_048(dd_replacement_048):
    feature = _clean(dd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_048'] = {'inputs': ['dd_replacement_048'], 'func': dd_replacement_d2_048}


def dd_replacement_d2_049(dd_replacement_049):
    feature = _clean(dd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_049'] = {'inputs': ['dd_replacement_049'], 'func': dd_replacement_d2_049}


def dd_replacement_d2_050(dd_replacement_050):
    feature = _clean(dd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_050'] = {'inputs': ['dd_replacement_050'], 'func': dd_replacement_d2_050}


def dd_replacement_d2_051(dd_replacement_051):
    feature = _clean(dd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_051'] = {'inputs': ['dd_replacement_051'], 'func': dd_replacement_d2_051}


def dd_replacement_d2_052(dd_replacement_052):
    feature = _clean(dd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_052'] = {'inputs': ['dd_replacement_052'], 'func': dd_replacement_d2_052}


def dd_replacement_d2_053(dd_replacement_053):
    feature = _clean(dd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_053'] = {'inputs': ['dd_replacement_053'], 'func': dd_replacement_d2_053}


def dd_replacement_d2_054(dd_replacement_054):
    feature = _clean(dd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_054'] = {'inputs': ['dd_replacement_054'], 'func': dd_replacement_d2_054}


def dd_replacement_d2_055(dd_replacement_055):
    feature = _clean(dd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_055'] = {'inputs': ['dd_replacement_055'], 'func': dd_replacement_d2_055}


def dd_replacement_d2_056(dd_replacement_056):
    feature = _clean(dd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_056'] = {'inputs': ['dd_replacement_056'], 'func': dd_replacement_d2_056}


def dd_replacement_d2_057(dd_replacement_057):
    feature = _clean(dd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_057'] = {'inputs': ['dd_replacement_057'], 'func': dd_replacement_d2_057}


def dd_replacement_d2_058(dd_replacement_058):
    feature = _clean(dd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_058'] = {'inputs': ['dd_replacement_058'], 'func': dd_replacement_d2_058}


def dd_replacement_d2_059(dd_replacement_059):
    feature = _clean(dd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_059'] = {'inputs': ['dd_replacement_059'], 'func': dd_replacement_d2_059}


def dd_replacement_d2_060(dd_replacement_060):
    feature = _clean(dd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_060'] = {'inputs': ['dd_replacement_060'], 'func': dd_replacement_d2_060}


def dd_replacement_d2_061(dd_replacement_061):
    feature = _clean(dd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_061'] = {'inputs': ['dd_replacement_061'], 'func': dd_replacement_d2_061}


def dd_replacement_d2_062(dd_replacement_062):
    feature = _clean(dd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_062'] = {'inputs': ['dd_replacement_062'], 'func': dd_replacement_d2_062}


def dd_replacement_d2_063(dd_replacement_063):
    feature = _clean(dd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_063'] = {'inputs': ['dd_replacement_063'], 'func': dd_replacement_d2_063}


def dd_replacement_d2_064(dd_replacement_064):
    feature = _clean(dd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_064'] = {'inputs': ['dd_replacement_064'], 'func': dd_replacement_d2_064}


def dd_replacement_d2_065(dd_replacement_065):
    feature = _clean(dd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_065'] = {'inputs': ['dd_replacement_065'], 'func': dd_replacement_d2_065}


def dd_replacement_d2_066(dd_replacement_066):
    feature = _clean(dd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_066'] = {'inputs': ['dd_replacement_066'], 'func': dd_replacement_d2_066}


def dd_replacement_d2_067(dd_replacement_067):
    feature = _clean(dd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_067'] = {'inputs': ['dd_replacement_067'], 'func': dd_replacement_d2_067}


def dd_replacement_d2_068(dd_replacement_068):
    feature = _clean(dd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_068'] = {'inputs': ['dd_replacement_068'], 'func': dd_replacement_d2_068}


def dd_replacement_d2_069(dd_replacement_069):
    feature = _clean(dd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_069'] = {'inputs': ['dd_replacement_069'], 'func': dd_replacement_d2_069}


def dd_replacement_d2_070(dd_replacement_070):
    feature = _clean(dd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_070'] = {'inputs': ['dd_replacement_070'], 'func': dd_replacement_d2_070}


def dd_replacement_d2_071(dd_replacement_071):
    feature = _clean(dd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_071'] = {'inputs': ['dd_replacement_071'], 'func': dd_replacement_d2_071}


def dd_replacement_d2_072(dd_replacement_072):
    feature = _clean(dd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_072'] = {'inputs': ['dd_replacement_072'], 'func': dd_replacement_d2_072}


def dd_replacement_d2_073(dd_replacement_073):
    feature = _clean(dd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_073'] = {'inputs': ['dd_replacement_073'], 'func': dd_replacement_d2_073}


def dd_replacement_d2_074(dd_replacement_074):
    feature = _clean(dd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_074'] = {'inputs': ['dd_replacement_074'], 'func': dd_replacement_d2_074}


def dd_replacement_d2_075(dd_replacement_075):
    feature = _clean(dd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_075'] = {'inputs': ['dd_replacement_075'], 'func': dd_replacement_d2_075}


def dd_replacement_d2_076(dd_replacement_076):
    feature = _clean(dd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_076'] = {'inputs': ['dd_replacement_076'], 'func': dd_replacement_d2_076}


def dd_replacement_d2_077(dd_replacement_077):
    feature = _clean(dd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_077'] = {'inputs': ['dd_replacement_077'], 'func': dd_replacement_d2_077}


def dd_replacement_d2_078(dd_replacement_078):
    feature = _clean(dd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_078'] = {'inputs': ['dd_replacement_078'], 'func': dd_replacement_d2_078}


def dd_replacement_d2_079(dd_replacement_079):
    feature = _clean(dd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_079'] = {'inputs': ['dd_replacement_079'], 'func': dd_replacement_d2_079}


def dd_replacement_d2_080(dd_replacement_080):
    feature = _clean(dd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_080'] = {'inputs': ['dd_replacement_080'], 'func': dd_replacement_d2_080}


def dd_replacement_d2_081(dd_replacement_081):
    feature = _clean(dd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_081'] = {'inputs': ['dd_replacement_081'], 'func': dd_replacement_d2_081}


def dd_replacement_d2_082(dd_replacement_082):
    feature = _clean(dd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_082'] = {'inputs': ['dd_replacement_082'], 'func': dd_replacement_d2_082}


def dd_replacement_d2_083(dd_replacement_083):
    feature = _clean(dd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_083'] = {'inputs': ['dd_replacement_083'], 'func': dd_replacement_d2_083}


def dd_replacement_d2_084(dd_replacement_084):
    feature = _clean(dd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_084'] = {'inputs': ['dd_replacement_084'], 'func': dd_replacement_d2_084}


def dd_replacement_d2_085(dd_replacement_085):
    feature = _clean(dd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_085'] = {'inputs': ['dd_replacement_085'], 'func': dd_replacement_d2_085}


def dd_replacement_d2_086(dd_replacement_086):
    feature = _clean(dd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_086'] = {'inputs': ['dd_replacement_086'], 'func': dd_replacement_d2_086}


def dd_replacement_d2_087(dd_replacement_087):
    feature = _clean(dd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_087'] = {'inputs': ['dd_replacement_087'], 'func': dd_replacement_d2_087}


def dd_replacement_d2_088(dd_replacement_088):
    feature = _clean(dd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_088'] = {'inputs': ['dd_replacement_088'], 'func': dd_replacement_d2_088}


def dd_replacement_d2_089(dd_replacement_089):
    feature = _clean(dd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_089'] = {'inputs': ['dd_replacement_089'], 'func': dd_replacement_d2_089}


def dd_replacement_d2_090(dd_replacement_090):
    feature = _clean(dd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_090'] = {'inputs': ['dd_replacement_090'], 'func': dd_replacement_d2_090}


def dd_replacement_d2_091(dd_replacement_091):
    feature = _clean(dd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_091'] = {'inputs': ['dd_replacement_091'], 'func': dd_replacement_d2_091}


def dd_replacement_d2_092(dd_replacement_092):
    feature = _clean(dd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_092'] = {'inputs': ['dd_replacement_092'], 'func': dd_replacement_d2_092}


def dd_replacement_d2_093(dd_replacement_093):
    feature = _clean(dd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_093'] = {'inputs': ['dd_replacement_093'], 'func': dd_replacement_d2_093}


def dd_replacement_d2_094(dd_replacement_094):
    feature = _clean(dd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_094'] = {'inputs': ['dd_replacement_094'], 'func': dd_replacement_d2_094}


def dd_replacement_d2_095(dd_replacement_095):
    feature = _clean(dd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_095'] = {'inputs': ['dd_replacement_095'], 'func': dd_replacement_d2_095}


def dd_replacement_d2_096(dd_replacement_096):
    feature = _clean(dd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_096'] = {'inputs': ['dd_replacement_096'], 'func': dd_replacement_d2_096}


def dd_replacement_d2_097(dd_replacement_097):
    feature = _clean(dd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_097'] = {'inputs': ['dd_replacement_097'], 'func': dd_replacement_d2_097}


def dd_replacement_d2_098(dd_replacement_098):
    feature = _clean(dd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_098'] = {'inputs': ['dd_replacement_098'], 'func': dd_replacement_d2_098}


def dd_replacement_d2_099(dd_replacement_099):
    feature = _clean(dd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_099'] = {'inputs': ['dd_replacement_099'], 'func': dd_replacement_d2_099}


def dd_replacement_d2_100(dd_replacement_100):
    feature = _clean(dd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_100'] = {'inputs': ['dd_replacement_100'], 'func': dd_replacement_d2_100}


def dd_replacement_d2_101(dd_replacement_101):
    feature = _clean(dd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_101'] = {'inputs': ['dd_replacement_101'], 'func': dd_replacement_d2_101}


def dd_replacement_d2_102(dd_replacement_102):
    feature = _clean(dd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_102'] = {'inputs': ['dd_replacement_102'], 'func': dd_replacement_d2_102}


def dd_replacement_d2_103(dd_replacement_103):
    feature = _clean(dd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_103'] = {'inputs': ['dd_replacement_103'], 'func': dd_replacement_d2_103}


def dd_replacement_d2_104(dd_replacement_104):
    feature = _clean(dd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_104'] = {'inputs': ['dd_replacement_104'], 'func': dd_replacement_d2_104}


def dd_replacement_d2_105(dd_replacement_105):
    feature = _clean(dd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_105'] = {'inputs': ['dd_replacement_105'], 'func': dd_replacement_d2_105}


def dd_replacement_d2_106(dd_replacement_106):
    feature = _clean(dd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_106'] = {'inputs': ['dd_replacement_106'], 'func': dd_replacement_d2_106}


def dd_replacement_d2_107(dd_replacement_107):
    feature = _clean(dd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_107'] = {'inputs': ['dd_replacement_107'], 'func': dd_replacement_d2_107}


def dd_replacement_d2_108(dd_replacement_108):
    feature = _clean(dd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_108'] = {'inputs': ['dd_replacement_108'], 'func': dd_replacement_d2_108}


def dd_replacement_d2_109(dd_replacement_109):
    feature = _clean(dd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_109'] = {'inputs': ['dd_replacement_109'], 'func': dd_replacement_d2_109}


def dd_replacement_d2_110(dd_replacement_110):
    feature = _clean(dd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_110'] = {'inputs': ['dd_replacement_110'], 'func': dd_replacement_d2_110}


def dd_replacement_d2_111(dd_replacement_111):
    feature = _clean(dd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_111'] = {'inputs': ['dd_replacement_111'], 'func': dd_replacement_d2_111}


def dd_replacement_d2_112(dd_replacement_112):
    feature = _clean(dd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_112'] = {'inputs': ['dd_replacement_112'], 'func': dd_replacement_d2_112}


def dd_replacement_d2_113(dd_replacement_113):
    feature = _clean(dd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_113'] = {'inputs': ['dd_replacement_113'], 'func': dd_replacement_d2_113}


def dd_replacement_d2_114(dd_replacement_114):
    feature = _clean(dd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_114'] = {'inputs': ['dd_replacement_114'], 'func': dd_replacement_d2_114}


def dd_replacement_d2_115(dd_replacement_115):
    feature = _clean(dd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_115'] = {'inputs': ['dd_replacement_115'], 'func': dd_replacement_d2_115}


def dd_replacement_d2_116(dd_replacement_116):
    feature = _clean(dd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_116'] = {'inputs': ['dd_replacement_116'], 'func': dd_replacement_d2_116}


def dd_replacement_d2_117(dd_replacement_117):
    feature = _clean(dd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_117'] = {'inputs': ['dd_replacement_117'], 'func': dd_replacement_d2_117}


def dd_replacement_d2_118(dd_replacement_118):
    feature = _clean(dd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_118'] = {'inputs': ['dd_replacement_118'], 'func': dd_replacement_d2_118}


def dd_replacement_d2_119(dd_replacement_119):
    feature = _clean(dd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_119'] = {'inputs': ['dd_replacement_119'], 'func': dd_replacement_d2_119}


def dd_replacement_d2_120(dd_replacement_120):
    feature = _clean(dd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_120'] = {'inputs': ['dd_replacement_120'], 'func': dd_replacement_d2_120}


def dd_replacement_d2_121(dd_replacement_121):
    feature = _clean(dd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_121'] = {'inputs': ['dd_replacement_121'], 'func': dd_replacement_d2_121}


def dd_replacement_d2_122(dd_replacement_122):
    feature = _clean(dd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_122'] = {'inputs': ['dd_replacement_122'], 'func': dd_replacement_d2_122}


def dd_replacement_d2_123(dd_replacement_123):
    feature = _clean(dd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_123'] = {'inputs': ['dd_replacement_123'], 'func': dd_replacement_d2_123}


def dd_replacement_d2_124(dd_replacement_124):
    feature = _clean(dd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_124'] = {'inputs': ['dd_replacement_124'], 'func': dd_replacement_d2_124}


def dd_replacement_d2_125(dd_replacement_125):
    feature = _clean(dd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_125'] = {'inputs': ['dd_replacement_125'], 'func': dd_replacement_d2_125}


def dd_replacement_d2_126(dd_replacement_126):
    feature = _clean(dd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_126'] = {'inputs': ['dd_replacement_126'], 'func': dd_replacement_d2_126}


def dd_replacement_d2_127(dd_replacement_127):
    feature = _clean(dd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_127'] = {'inputs': ['dd_replacement_127'], 'func': dd_replacement_d2_127}


def dd_replacement_d2_128(dd_replacement_128):
    feature = _clean(dd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_128'] = {'inputs': ['dd_replacement_128'], 'func': dd_replacement_d2_128}


def dd_replacement_d2_129(dd_replacement_129):
    feature = _clean(dd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_129'] = {'inputs': ['dd_replacement_129'], 'func': dd_replacement_d2_129}


def dd_replacement_d2_130(dd_replacement_130):
    feature = _clean(dd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_130'] = {'inputs': ['dd_replacement_130'], 'func': dd_replacement_d2_130}


def dd_replacement_d2_131(dd_replacement_131):
    feature = _clean(dd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_131'] = {'inputs': ['dd_replacement_131'], 'func': dd_replacement_d2_131}


def dd_replacement_d2_132(dd_replacement_132):
    feature = _clean(dd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_132'] = {'inputs': ['dd_replacement_132'], 'func': dd_replacement_d2_132}


def dd_replacement_d2_133(dd_replacement_133):
    feature = _clean(dd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_133'] = {'inputs': ['dd_replacement_133'], 'func': dd_replacement_d2_133}


def dd_replacement_d2_134(dd_replacement_134):
    feature = _clean(dd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_134'] = {'inputs': ['dd_replacement_134'], 'func': dd_replacement_d2_134}


def dd_replacement_d2_135(dd_replacement_135):
    feature = _clean(dd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_135'] = {'inputs': ['dd_replacement_135'], 'func': dd_replacement_d2_135}


def dd_replacement_d2_136(dd_replacement_136):
    feature = _clean(dd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_136'] = {'inputs': ['dd_replacement_136'], 'func': dd_replacement_d2_136}


def dd_replacement_d2_137(dd_replacement_137):
    feature = _clean(dd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_137'] = {'inputs': ['dd_replacement_137'], 'func': dd_replacement_d2_137}


def dd_replacement_d2_138(dd_replacement_138):
    feature = _clean(dd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_138'] = {'inputs': ['dd_replacement_138'], 'func': dd_replacement_d2_138}


def dd_replacement_d2_139(dd_replacement_139):
    feature = _clean(dd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_139'] = {'inputs': ['dd_replacement_139'], 'func': dd_replacement_d2_139}


def dd_replacement_d2_140(dd_replacement_140):
    feature = _clean(dd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_140'] = {'inputs': ['dd_replacement_140'], 'func': dd_replacement_d2_140}


def dd_replacement_d2_141(dd_replacement_141):
    feature = _clean(dd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_141'] = {'inputs': ['dd_replacement_141'], 'func': dd_replacement_d2_141}


def dd_replacement_d2_142(dd_replacement_142):
    feature = _clean(dd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_142'] = {'inputs': ['dd_replacement_142'], 'func': dd_replacement_d2_142}


def dd_replacement_d2_143(dd_replacement_143):
    feature = _clean(dd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_143'] = {'inputs': ['dd_replacement_143'], 'func': dd_replacement_d2_143}


def dd_replacement_d2_144(dd_replacement_144):
    feature = _clean(dd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_144'] = {'inputs': ['dd_replacement_144'], 'func': dd_replacement_d2_144}


def dd_replacement_d2_145(dd_replacement_145):
    feature = _clean(dd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_145'] = {'inputs': ['dd_replacement_145'], 'func': dd_replacement_d2_145}


def dd_replacement_d2_146(dd_replacement_146):
    feature = _clean(dd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_146'] = {'inputs': ['dd_replacement_146'], 'func': dd_replacement_d2_146}


def dd_replacement_d2_147(dd_replacement_147):
    feature = _clean(dd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_147'] = {'inputs': ['dd_replacement_147'], 'func': dd_replacement_d2_147}


def dd_replacement_d2_148(dd_replacement_148):
    feature = _clean(dd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_148'] = {'inputs': ['dd_replacement_148'], 'func': dd_replacement_d2_148}


def dd_replacement_d2_149(dd_replacement_149):
    feature = _clean(dd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_149'] = {'inputs': ['dd_replacement_149'], 'func': dd_replacement_d2_149}


def dd_replacement_d2_150(dd_replacement_150):
    feature = _clean(dd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_150'] = {'inputs': ['dd_replacement_150'], 'func': dd_replacement_d2_150}


def dd_replacement_d2_151(dd_replacement_151):
    feature = _clean(dd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_151'] = {'inputs': ['dd_replacement_151'], 'func': dd_replacement_d2_151}


def dd_replacement_d2_152(dd_replacement_152):
    feature = _clean(dd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_152'] = {'inputs': ['dd_replacement_152'], 'func': dd_replacement_d2_152}


def dd_replacement_d2_153(dd_replacement_153):
    feature = _clean(dd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_153'] = {'inputs': ['dd_replacement_153'], 'func': dd_replacement_d2_153}


def dd_replacement_d2_154(dd_replacement_154):
    feature = _clean(dd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_154'] = {'inputs': ['dd_replacement_154'], 'func': dd_replacement_d2_154}


def dd_replacement_d2_155(dd_replacement_155):
    feature = _clean(dd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_155'] = {'inputs': ['dd_replacement_155'], 'func': dd_replacement_d2_155}


def dd_replacement_d2_156(dd_replacement_156):
    feature = _clean(dd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_156'] = {'inputs': ['dd_replacement_156'], 'func': dd_replacement_d2_156}


def dd_replacement_d2_157(dd_replacement_157):
    feature = _clean(dd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_157'] = {'inputs': ['dd_replacement_157'], 'func': dd_replacement_d2_157}


def dd_replacement_d2_158(dd_replacement_158):
    feature = _clean(dd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_158'] = {'inputs': ['dd_replacement_158'], 'func': dd_replacement_d2_158}


def dd_replacement_d2_159(dd_replacement_159):
    feature = _clean(dd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_159'] = {'inputs': ['dd_replacement_159'], 'func': dd_replacement_d2_159}


def dd_replacement_d2_160(dd_replacement_160):
    feature = _clean(dd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_160'] = {'inputs': ['dd_replacement_160'], 'func': dd_replacement_d2_160}


def dd_replacement_d2_161(dd_replacement_161):
    feature = _clean(dd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_161'] = {'inputs': ['dd_replacement_161'], 'func': dd_replacement_d2_161}


def dd_replacement_d2_162(dd_replacement_162):
    feature = _clean(dd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_162'] = {'inputs': ['dd_replacement_162'], 'func': dd_replacement_d2_162}


def dd_replacement_d2_163(dd_replacement_163):
    feature = _clean(dd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_163'] = {'inputs': ['dd_replacement_163'], 'func': dd_replacement_d2_163}


def dd_replacement_d2_164(dd_replacement_164):
    feature = _clean(dd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_164'] = {'inputs': ['dd_replacement_164'], 'func': dd_replacement_d2_164}


def dd_replacement_d2_165(dd_replacement_165):
    feature = _clean(dd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_165'] = {'inputs': ['dd_replacement_165'], 'func': dd_replacement_d2_165}


def dd_replacement_d2_166(dd_replacement_166):
    feature = _clean(dd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_166'] = {'inputs': ['dd_replacement_166'], 'func': dd_replacement_d2_166}


def dd_replacement_d2_167(dd_replacement_167):
    feature = _clean(dd_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_167'] = {'inputs': ['dd_replacement_167'], 'func': dd_replacement_d2_167}


def dd_replacement_d2_168(dd_replacement_168):
    feature = _clean(dd_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_168'] = {'inputs': ['dd_replacement_168'], 'func': dd_replacement_d2_168}


def dd_replacement_d2_169(dd_replacement_169):
    feature = _clean(dd_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_169'] = {'inputs': ['dd_replacement_169'], 'func': dd_replacement_d2_169}


def dd_replacement_d2_170(dd_replacement_170):
    feature = _clean(dd_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_170'] = {'inputs': ['dd_replacement_170'], 'func': dd_replacement_d2_170}


def dd_replacement_d2_171(dd_replacement_171):
    feature = _clean(dd_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_171'] = {'inputs': ['dd_replacement_171'], 'func': dd_replacement_d2_171}


def dd_replacement_d2_172(dd_replacement_172):
    feature = _clean(dd_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_172'] = {'inputs': ['dd_replacement_172'], 'func': dd_replacement_d2_172}


def dd_replacement_d2_173(dd_replacement_173):
    feature = _clean(dd_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_173'] = {'inputs': ['dd_replacement_173'], 'func': dd_replacement_d2_173}


def dd_replacement_d2_174(dd_replacement_174):
    feature = _clean(dd_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_174'] = {'inputs': ['dd_replacement_174'], 'func': dd_replacement_d2_174}


def dd_replacement_d2_175(dd_replacement_175):
    feature = _clean(dd_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
DD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dd_replacement_d2_175'] = {'inputs': ['dd_replacement_175'], 'func': dd_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dsd_base_universe_d2_001_dsd_002_range_expansion_10_002(dsd_002_range_expansion_10_002):
    return _base_universe_d2(dsd_002_range_expansion_10_002, 1)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_001_dsd_002_range_expansion_10_002'] = {'inputs': ['dsd_002_range_expansion_10_002'], 'func': dsd_base_universe_d2_001_dsd_002_range_expansion_10_002}


def dsd_base_universe_d2_002_dsd_004_close_location_42_004(dsd_004_close_location_42_004):
    return _base_universe_d2(dsd_004_close_location_42_004, 2)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_002_dsd_004_close_location_42_004'] = {'inputs': ['dsd_004_close_location_42_004'], 'func': dsd_base_universe_d2_002_dsd_004_close_location_42_004}


def dsd_base_universe_d2_003_dsd_005_atr_move_63_005(dsd_005_atr_move_63_005):
    return _base_universe_d2(dsd_005_atr_move_63_005, 3)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_003_dsd_005_atr_move_63_005'] = {'inputs': ['dsd_005_atr_move_63_005'], 'func': dsd_base_universe_d2_003_dsd_005_atr_move_63_005}


def dsd_base_universe_d2_004_dsd_008_range_expansion_189_008(dsd_008_range_expansion_189_008):
    return _base_universe_d2(dsd_008_range_expansion_189_008, 4)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_004_dsd_008_range_expansion_189_008'] = {'inputs': ['dsd_008_range_expansion_189_008'], 'func': dsd_base_universe_d2_004_dsd_008_range_expansion_189_008}


def dsd_base_universe_d2_005_dsd_010_close_location_378_010(dsd_010_close_location_378_010):
    return _base_universe_d2(dsd_010_close_location_378_010, 5)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_005_dsd_010_close_location_378_010'] = {'inputs': ['dsd_010_close_location_378_010'], 'func': dsd_base_universe_d2_005_dsd_010_close_location_378_010}


def dsd_base_universe_d2_006_dsd_011_atr_move_504_011(dsd_011_atr_move_504_011):
    return _base_universe_d2(dsd_011_atr_move_504_011, 6)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_006_dsd_011_atr_move_504_011'] = {'inputs': ['dsd_011_atr_move_504_011'], 'func': dsd_base_universe_d2_006_dsd_011_atr_move_504_011}


def dsd_base_universe_d2_007_dsd_014_range_expansion_1260_014(dsd_014_range_expansion_1260_014):
    return _base_universe_d2(dsd_014_range_expansion_1260_014, 7)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_007_dsd_014_range_expansion_1260_014'] = {'inputs': ['dsd_014_range_expansion_1260_014'], 'func': dsd_base_universe_d2_007_dsd_014_range_expansion_1260_014}


def dsd_base_universe_d2_008_dsd_016_close_location_5_016(dsd_016_close_location_5_016):
    return _base_universe_d2(dsd_016_close_location_5_016, 8)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_008_dsd_016_close_location_5_016'] = {'inputs': ['dsd_016_close_location_5_016'], 'func': dsd_base_universe_d2_008_dsd_016_close_location_5_016}


def dsd_base_universe_d2_009_dsd_017_atr_move_10_017(dsd_017_atr_move_10_017):
    return _base_universe_d2(dsd_017_atr_move_10_017, 9)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_009_dsd_017_atr_move_10_017'] = {'inputs': ['dsd_017_atr_move_10_017'], 'func': dsd_base_universe_d2_009_dsd_017_atr_move_10_017}


def dsd_base_universe_d2_010_dsd_020_range_expansion_63_020(dsd_020_range_expansion_63_020):
    return _base_universe_d2(dsd_020_range_expansion_63_020, 10)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_010_dsd_020_range_expansion_63_020'] = {'inputs': ['dsd_020_range_expansion_63_020'], 'func': dsd_base_universe_d2_010_dsd_020_range_expansion_63_020}


def dsd_base_universe_d2_011_dsd_022_close_location_126_022(dsd_022_close_location_126_022):
    return _base_universe_d2(dsd_022_close_location_126_022, 11)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_011_dsd_022_close_location_126_022'] = {'inputs': ['dsd_022_close_location_126_022'], 'func': dsd_base_universe_d2_011_dsd_022_close_location_126_022}


def dsd_base_universe_d2_012_dsd_023_atr_move_189_023(dsd_023_atr_move_189_023):
    return _base_universe_d2(dsd_023_atr_move_189_023, 12)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_012_dsd_023_atr_move_189_023'] = {'inputs': ['dsd_023_atr_move_189_023'], 'func': dsd_base_universe_d2_012_dsd_023_atr_move_189_023}


def dsd_base_universe_d2_013_dsd_026_range_expansion_504_026(dsd_026_range_expansion_504_026):
    return _base_universe_d2(dsd_026_range_expansion_504_026, 13)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_013_dsd_026_range_expansion_504_026'] = {'inputs': ['dsd_026_range_expansion_504_026'], 'func': dsd_base_universe_d2_013_dsd_026_range_expansion_504_026}


def dsd_base_universe_d2_014_dsd_028_close_location_1008_028(dsd_028_close_location_1008_028):
    return _base_universe_d2(dsd_028_close_location_1008_028, 14)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_014_dsd_028_close_location_1008_028'] = {'inputs': ['dsd_028_close_location_1008_028'], 'func': dsd_base_universe_d2_014_dsd_028_close_location_1008_028}


def dsd_base_universe_d2_015_dsd_029_atr_move_1260_029(dsd_029_atr_move_1260_029):
    return _base_universe_d2(dsd_029_atr_move_1260_029, 15)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_015_dsd_029_atr_move_1260_029'] = {'inputs': ['dsd_029_atr_move_1260_029'], 'func': dsd_base_universe_d2_015_dsd_029_atr_move_1260_029}


def dsd_base_universe_d2_016_dsd_basefill_001(dsd_basefill_001):
    return _base_universe_d2(dsd_basefill_001, 16)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_016_dsd_basefill_001'] = {'inputs': ['dsd_basefill_001'], 'func': dsd_base_universe_d2_016_dsd_basefill_001}


def dsd_base_universe_d2_017_dsd_basefill_003(dsd_basefill_003):
    return _base_universe_d2(dsd_basefill_003, 17)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_017_dsd_basefill_003'] = {'inputs': ['dsd_basefill_003'], 'func': dsd_base_universe_d2_017_dsd_basefill_003}


def dsd_base_universe_d2_018_dsd_basefill_006(dsd_basefill_006):
    return _base_universe_d2(dsd_basefill_006, 18)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_018_dsd_basefill_006'] = {'inputs': ['dsd_basefill_006'], 'func': dsd_base_universe_d2_018_dsd_basefill_006}


def dsd_base_universe_d2_019_dsd_basefill_007(dsd_basefill_007):
    return _base_universe_d2(dsd_basefill_007, 19)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_019_dsd_basefill_007'] = {'inputs': ['dsd_basefill_007'], 'func': dsd_base_universe_d2_019_dsd_basefill_007}


def dsd_base_universe_d2_020_dsd_basefill_009(dsd_basefill_009):
    return _base_universe_d2(dsd_basefill_009, 20)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_020_dsd_basefill_009'] = {'inputs': ['dsd_basefill_009'], 'func': dsd_base_universe_d2_020_dsd_basefill_009}


def dsd_base_universe_d2_021_dsd_basefill_012(dsd_basefill_012):
    return _base_universe_d2(dsd_basefill_012, 21)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_021_dsd_basefill_012'] = {'inputs': ['dsd_basefill_012'], 'func': dsd_base_universe_d2_021_dsd_basefill_012}


def dsd_base_universe_d2_022_dsd_basefill_013(dsd_basefill_013):
    return _base_universe_d2(dsd_basefill_013, 22)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_022_dsd_basefill_013'] = {'inputs': ['dsd_basefill_013'], 'func': dsd_base_universe_d2_022_dsd_basefill_013}


def dsd_base_universe_d2_023_dsd_basefill_015(dsd_basefill_015):
    return _base_universe_d2(dsd_basefill_015, 23)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_023_dsd_basefill_015'] = {'inputs': ['dsd_basefill_015'], 'func': dsd_base_universe_d2_023_dsd_basefill_015}


def dsd_base_universe_d2_024_dsd_basefill_018(dsd_basefill_018):
    return _base_universe_d2(dsd_basefill_018, 24)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_024_dsd_basefill_018'] = {'inputs': ['dsd_basefill_018'], 'func': dsd_base_universe_d2_024_dsd_basefill_018}


def dsd_base_universe_d2_025_dsd_basefill_019(dsd_basefill_019):
    return _base_universe_d2(dsd_basefill_019, 25)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_025_dsd_basefill_019'] = {'inputs': ['dsd_basefill_019'], 'func': dsd_base_universe_d2_025_dsd_basefill_019}


def dsd_base_universe_d2_026_dsd_basefill_021(dsd_basefill_021):
    return _base_universe_d2(dsd_basefill_021, 26)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_026_dsd_basefill_021'] = {'inputs': ['dsd_basefill_021'], 'func': dsd_base_universe_d2_026_dsd_basefill_021}


def dsd_base_universe_d2_027_dsd_basefill_024(dsd_basefill_024):
    return _base_universe_d2(dsd_basefill_024, 27)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_027_dsd_basefill_024'] = {'inputs': ['dsd_basefill_024'], 'func': dsd_base_universe_d2_027_dsd_basefill_024}


def dsd_base_universe_d2_028_dsd_basefill_025(dsd_basefill_025):
    return _base_universe_d2(dsd_basefill_025, 28)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_028_dsd_basefill_025'] = {'inputs': ['dsd_basefill_025'], 'func': dsd_base_universe_d2_028_dsd_basefill_025}


def dsd_base_universe_d2_029_dsd_basefill_027(dsd_basefill_027):
    return _base_universe_d2(dsd_basefill_027, 29)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_029_dsd_basefill_027'] = {'inputs': ['dsd_basefill_027'], 'func': dsd_base_universe_d2_029_dsd_basefill_027}


def dsd_base_universe_d2_030_dsd_basefill_030(dsd_basefill_030):
    return _base_universe_d2(dsd_basefill_030, 30)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_030_dsd_basefill_030'] = {'inputs': ['dsd_basefill_030'], 'func': dsd_base_universe_d2_030_dsd_basefill_030}


def dsd_base_universe_d2_031_dsd_basefill_031(dsd_basefill_031):
    return _base_universe_d2(dsd_basefill_031, 31)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_031_dsd_basefill_031'] = {'inputs': ['dsd_basefill_031'], 'func': dsd_base_universe_d2_031_dsd_basefill_031}


def dsd_base_universe_d2_032_dsd_basefill_032(dsd_basefill_032):
    return _base_universe_d2(dsd_basefill_032, 32)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_032_dsd_basefill_032'] = {'inputs': ['dsd_basefill_032'], 'func': dsd_base_universe_d2_032_dsd_basefill_032}


def dsd_base_universe_d2_033_dsd_basefill_033(dsd_basefill_033):
    return _base_universe_d2(dsd_basefill_033, 33)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_033_dsd_basefill_033'] = {'inputs': ['dsd_basefill_033'], 'func': dsd_base_universe_d2_033_dsd_basefill_033}


def dsd_base_universe_d2_034_dsd_basefill_034(dsd_basefill_034):
    return _base_universe_d2(dsd_basefill_034, 34)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_034_dsd_basefill_034'] = {'inputs': ['dsd_basefill_034'], 'func': dsd_base_universe_d2_034_dsd_basefill_034}


def dsd_base_universe_d2_035_dsd_basefill_035(dsd_basefill_035):
    return _base_universe_d2(dsd_basefill_035, 35)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_035_dsd_basefill_035'] = {'inputs': ['dsd_basefill_035'], 'func': dsd_base_universe_d2_035_dsd_basefill_035}


def dsd_base_universe_d2_036_dsd_basefill_036(dsd_basefill_036):
    return _base_universe_d2(dsd_basefill_036, 36)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_036_dsd_basefill_036'] = {'inputs': ['dsd_basefill_036'], 'func': dsd_base_universe_d2_036_dsd_basefill_036}


def dsd_base_universe_d2_037_dsd_basefill_037(dsd_basefill_037):
    return _base_universe_d2(dsd_basefill_037, 37)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_037_dsd_basefill_037'] = {'inputs': ['dsd_basefill_037'], 'func': dsd_base_universe_d2_037_dsd_basefill_037}


def dsd_base_universe_d2_038_dsd_basefill_038(dsd_basefill_038):
    return _base_universe_d2(dsd_basefill_038, 38)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_038_dsd_basefill_038'] = {'inputs': ['dsd_basefill_038'], 'func': dsd_base_universe_d2_038_dsd_basefill_038}


def dsd_base_universe_d2_039_dsd_basefill_039(dsd_basefill_039):
    return _base_universe_d2(dsd_basefill_039, 39)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_039_dsd_basefill_039'] = {'inputs': ['dsd_basefill_039'], 'func': dsd_base_universe_d2_039_dsd_basefill_039}


def dsd_base_universe_d2_040_dsd_basefill_040(dsd_basefill_040):
    return _base_universe_d2(dsd_basefill_040, 40)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_040_dsd_basefill_040'] = {'inputs': ['dsd_basefill_040'], 'func': dsd_base_universe_d2_040_dsd_basefill_040}


def dsd_base_universe_d2_041_dsd_basefill_041(dsd_basefill_041):
    return _base_universe_d2(dsd_basefill_041, 41)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_041_dsd_basefill_041'] = {'inputs': ['dsd_basefill_041'], 'func': dsd_base_universe_d2_041_dsd_basefill_041}


def dsd_base_universe_d2_042_dsd_basefill_042(dsd_basefill_042):
    return _base_universe_d2(dsd_basefill_042, 42)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_042_dsd_basefill_042'] = {'inputs': ['dsd_basefill_042'], 'func': dsd_base_universe_d2_042_dsd_basefill_042}


def dsd_base_universe_d2_043_dsd_basefill_043(dsd_basefill_043):
    return _base_universe_d2(dsd_basefill_043, 43)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_043_dsd_basefill_043'] = {'inputs': ['dsd_basefill_043'], 'func': dsd_base_universe_d2_043_dsd_basefill_043}


def dsd_base_universe_d2_044_dsd_basefill_044(dsd_basefill_044):
    return _base_universe_d2(dsd_basefill_044, 44)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_044_dsd_basefill_044'] = {'inputs': ['dsd_basefill_044'], 'func': dsd_base_universe_d2_044_dsd_basefill_044}


def dsd_base_universe_d2_045_dsd_basefill_045(dsd_basefill_045):
    return _base_universe_d2(dsd_basefill_045, 45)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_045_dsd_basefill_045'] = {'inputs': ['dsd_basefill_045'], 'func': dsd_base_universe_d2_045_dsd_basefill_045}


def dsd_base_universe_d2_046_dsd_basefill_046(dsd_basefill_046):
    return _base_universe_d2(dsd_basefill_046, 46)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_046_dsd_basefill_046'] = {'inputs': ['dsd_basefill_046'], 'func': dsd_base_universe_d2_046_dsd_basefill_046}


def dsd_base_universe_d2_047_dsd_basefill_047(dsd_basefill_047):
    return _base_universe_d2(dsd_basefill_047, 47)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_047_dsd_basefill_047'] = {'inputs': ['dsd_basefill_047'], 'func': dsd_base_universe_d2_047_dsd_basefill_047}


def dsd_base_universe_d2_048_dsd_basefill_048(dsd_basefill_048):
    return _base_universe_d2(dsd_basefill_048, 48)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_048_dsd_basefill_048'] = {'inputs': ['dsd_basefill_048'], 'func': dsd_base_universe_d2_048_dsd_basefill_048}


def dsd_base_universe_d2_049_dsd_basefill_049(dsd_basefill_049):
    return _base_universe_d2(dsd_basefill_049, 49)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_049_dsd_basefill_049'] = {'inputs': ['dsd_basefill_049'], 'func': dsd_base_universe_d2_049_dsd_basefill_049}


def dsd_base_universe_d2_050_dsd_basefill_050(dsd_basefill_050):
    return _base_universe_d2(dsd_basefill_050, 50)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_050_dsd_basefill_050'] = {'inputs': ['dsd_basefill_050'], 'func': dsd_base_universe_d2_050_dsd_basefill_050}


def dsd_base_universe_d2_051_dsd_basefill_051(dsd_basefill_051):
    return _base_universe_d2(dsd_basefill_051, 51)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_051_dsd_basefill_051'] = {'inputs': ['dsd_basefill_051'], 'func': dsd_base_universe_d2_051_dsd_basefill_051}


def dsd_base_universe_d2_052_dsd_basefill_052(dsd_basefill_052):
    return _base_universe_d2(dsd_basefill_052, 52)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_052_dsd_basefill_052'] = {'inputs': ['dsd_basefill_052'], 'func': dsd_base_universe_d2_052_dsd_basefill_052}


def dsd_base_universe_d2_053_dsd_basefill_053(dsd_basefill_053):
    return _base_universe_d2(dsd_basefill_053, 53)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_053_dsd_basefill_053'] = {'inputs': ['dsd_basefill_053'], 'func': dsd_base_universe_d2_053_dsd_basefill_053}


def dsd_base_universe_d2_054_dsd_basefill_054(dsd_basefill_054):
    return _base_universe_d2(dsd_basefill_054, 54)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_054_dsd_basefill_054'] = {'inputs': ['dsd_basefill_054'], 'func': dsd_base_universe_d2_054_dsd_basefill_054}


def dsd_base_universe_d2_055_dsd_basefill_055(dsd_basefill_055):
    return _base_universe_d2(dsd_basefill_055, 55)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_055_dsd_basefill_055'] = {'inputs': ['dsd_basefill_055'], 'func': dsd_base_universe_d2_055_dsd_basefill_055}


def dsd_base_universe_d2_056_dsd_basefill_056(dsd_basefill_056):
    return _base_universe_d2(dsd_basefill_056, 56)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_056_dsd_basefill_056'] = {'inputs': ['dsd_basefill_056'], 'func': dsd_base_universe_d2_056_dsd_basefill_056}


def dsd_base_universe_d2_057_dsd_basefill_057(dsd_basefill_057):
    return _base_universe_d2(dsd_basefill_057, 57)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_057_dsd_basefill_057'] = {'inputs': ['dsd_basefill_057'], 'func': dsd_base_universe_d2_057_dsd_basefill_057}


def dsd_base_universe_d2_058_dsd_basefill_058(dsd_basefill_058):
    return _base_universe_d2(dsd_basefill_058, 58)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_058_dsd_basefill_058'] = {'inputs': ['dsd_basefill_058'], 'func': dsd_base_universe_d2_058_dsd_basefill_058}


def dsd_base_universe_d2_059_dsd_basefill_059(dsd_basefill_059):
    return _base_universe_d2(dsd_basefill_059, 59)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_059_dsd_basefill_059'] = {'inputs': ['dsd_basefill_059'], 'func': dsd_base_universe_d2_059_dsd_basefill_059}


def dsd_base_universe_d2_060_dsd_basefill_060(dsd_basefill_060):
    return _base_universe_d2(dsd_basefill_060, 60)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_060_dsd_basefill_060'] = {'inputs': ['dsd_basefill_060'], 'func': dsd_base_universe_d2_060_dsd_basefill_060}


def dsd_base_universe_d2_061_dsd_basefill_061(dsd_basefill_061):
    return _base_universe_d2(dsd_basefill_061, 61)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_061_dsd_basefill_061'] = {'inputs': ['dsd_basefill_061'], 'func': dsd_base_universe_d2_061_dsd_basefill_061}


def dsd_base_universe_d2_062_dsd_basefill_062(dsd_basefill_062):
    return _base_universe_d2(dsd_basefill_062, 62)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_062_dsd_basefill_062'] = {'inputs': ['dsd_basefill_062'], 'func': dsd_base_universe_d2_062_dsd_basefill_062}


def dsd_base_universe_d2_063_dsd_basefill_063(dsd_basefill_063):
    return _base_universe_d2(dsd_basefill_063, 63)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_063_dsd_basefill_063'] = {'inputs': ['dsd_basefill_063'], 'func': dsd_base_universe_d2_063_dsd_basefill_063}


def dsd_base_universe_d2_064_dsd_basefill_064(dsd_basefill_064):
    return _base_universe_d2(dsd_basefill_064, 64)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_064_dsd_basefill_064'] = {'inputs': ['dsd_basefill_064'], 'func': dsd_base_universe_d2_064_dsd_basefill_064}


def dsd_base_universe_d2_065_dsd_basefill_065(dsd_basefill_065):
    return _base_universe_d2(dsd_basefill_065, 65)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_065_dsd_basefill_065'] = {'inputs': ['dsd_basefill_065'], 'func': dsd_base_universe_d2_065_dsd_basefill_065}


def dsd_base_universe_d2_066_dsd_basefill_066(dsd_basefill_066):
    return _base_universe_d2(dsd_basefill_066, 66)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_066_dsd_basefill_066'] = {'inputs': ['dsd_basefill_066'], 'func': dsd_base_universe_d2_066_dsd_basefill_066}


def dsd_base_universe_d2_067_dsd_basefill_067(dsd_basefill_067):
    return _base_universe_d2(dsd_basefill_067, 67)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_067_dsd_basefill_067'] = {'inputs': ['dsd_basefill_067'], 'func': dsd_base_universe_d2_067_dsd_basefill_067}


def dsd_base_universe_d2_068_dsd_basefill_068(dsd_basefill_068):
    return _base_universe_d2(dsd_basefill_068, 68)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_068_dsd_basefill_068'] = {'inputs': ['dsd_basefill_068'], 'func': dsd_base_universe_d2_068_dsd_basefill_068}


def dsd_base_universe_d2_069_dsd_basefill_069(dsd_basefill_069):
    return _base_universe_d2(dsd_basefill_069, 69)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_069_dsd_basefill_069'] = {'inputs': ['dsd_basefill_069'], 'func': dsd_base_universe_d2_069_dsd_basefill_069}


def dsd_base_universe_d2_070_dsd_basefill_070(dsd_basefill_070):
    return _base_universe_d2(dsd_basefill_070, 70)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_070_dsd_basefill_070'] = {'inputs': ['dsd_basefill_070'], 'func': dsd_base_universe_d2_070_dsd_basefill_070}


def dsd_base_universe_d2_071_dsd_basefill_071(dsd_basefill_071):
    return _base_universe_d2(dsd_basefill_071, 71)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_071_dsd_basefill_071'] = {'inputs': ['dsd_basefill_071'], 'func': dsd_base_universe_d2_071_dsd_basefill_071}


def dsd_base_universe_d2_072_dsd_basefill_072(dsd_basefill_072):
    return _base_universe_d2(dsd_basefill_072, 72)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_072_dsd_basefill_072'] = {'inputs': ['dsd_basefill_072'], 'func': dsd_base_universe_d2_072_dsd_basefill_072}


def dsd_base_universe_d2_073_dsd_basefill_073(dsd_basefill_073):
    return _base_universe_d2(dsd_basefill_073, 73)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_073_dsd_basefill_073'] = {'inputs': ['dsd_basefill_073'], 'func': dsd_base_universe_d2_073_dsd_basefill_073}


def dsd_base_universe_d2_074_dsd_basefill_074(dsd_basefill_074):
    return _base_universe_d2(dsd_basefill_074, 74)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_074_dsd_basefill_074'] = {'inputs': ['dsd_basefill_074'], 'func': dsd_base_universe_d2_074_dsd_basefill_074}


def dsd_base_universe_d2_075_dsd_basefill_075(dsd_basefill_075):
    return _base_universe_d2(dsd_basefill_075, 75)
DSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dsd_base_universe_d2_075_dsd_basefill_075'] = {'inputs': ['dsd_basefill_075'], 'func': dsd_base_universe_d2_075_dsd_basefill_075}
