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



def vrg_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def vrg_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def vrg_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def vrg_154_vrg_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def vrg_155_vrg_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLATILITY_REGIME_REGISTRY_2ND_DERIVATIVES = {
    'vrg_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': vrg_001_realized_vol_z_roc_1},
    'vrg_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': vrg_007_realized_vol_z_roc_5},
    'vrg_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': vrg_013_realized_vol_z_roc_42},
    'vrg_154_vrg_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': vrg_154_vrg_019_realized_vol_z_42_019_roc_126},
    'vrg_155_vrg_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': vrg_155_vrg_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vr_replacement_d2_001(vr_replacement_001):
    feature = _clean(vr_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_001'] = {'inputs': ['vr_replacement_001'], 'func': vr_replacement_d2_001}


def vr_replacement_d2_002(vr_replacement_002):
    feature = _clean(vr_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_002'] = {'inputs': ['vr_replacement_002'], 'func': vr_replacement_d2_002}


def vr_replacement_d2_003(vr_replacement_003):
    feature = _clean(vr_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_003'] = {'inputs': ['vr_replacement_003'], 'func': vr_replacement_d2_003}


def vr_replacement_d2_004(vr_replacement_004):
    feature = _clean(vr_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_004'] = {'inputs': ['vr_replacement_004'], 'func': vr_replacement_d2_004}


def vr_replacement_d2_005(vr_replacement_005):
    feature = _clean(vr_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_005'] = {'inputs': ['vr_replacement_005'], 'func': vr_replacement_d2_005}


def vr_replacement_d2_006(vr_replacement_006):
    feature = _clean(vr_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_006'] = {'inputs': ['vr_replacement_006'], 'func': vr_replacement_d2_006}


def vr_replacement_d2_007(vr_replacement_007):
    feature = _clean(vr_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_007'] = {'inputs': ['vr_replacement_007'], 'func': vr_replacement_d2_007}


def vr_replacement_d2_008(vr_replacement_008):
    feature = _clean(vr_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_008'] = {'inputs': ['vr_replacement_008'], 'func': vr_replacement_d2_008}


def vr_replacement_d2_009(vr_replacement_009):
    feature = _clean(vr_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_009'] = {'inputs': ['vr_replacement_009'], 'func': vr_replacement_d2_009}


def vr_replacement_d2_010(vr_replacement_010):
    feature = _clean(vr_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_010'] = {'inputs': ['vr_replacement_010'], 'func': vr_replacement_d2_010}


def vr_replacement_d2_011(vr_replacement_011):
    feature = _clean(vr_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_011'] = {'inputs': ['vr_replacement_011'], 'func': vr_replacement_d2_011}


def vr_replacement_d2_012(vr_replacement_012):
    feature = _clean(vr_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_012'] = {'inputs': ['vr_replacement_012'], 'func': vr_replacement_d2_012}


def vr_replacement_d2_013(vr_replacement_013):
    feature = _clean(vr_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_013'] = {'inputs': ['vr_replacement_013'], 'func': vr_replacement_d2_013}


def vr_replacement_d2_014(vr_replacement_014):
    feature = _clean(vr_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_014'] = {'inputs': ['vr_replacement_014'], 'func': vr_replacement_d2_014}


def vr_replacement_d2_015(vr_replacement_015):
    feature = _clean(vr_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_015'] = {'inputs': ['vr_replacement_015'], 'func': vr_replacement_d2_015}


def vr_replacement_d2_016(vr_replacement_016):
    feature = _clean(vr_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_016'] = {'inputs': ['vr_replacement_016'], 'func': vr_replacement_d2_016}


def vr_replacement_d2_017(vr_replacement_017):
    feature = _clean(vr_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_017'] = {'inputs': ['vr_replacement_017'], 'func': vr_replacement_d2_017}


def vr_replacement_d2_018(vr_replacement_018):
    feature = _clean(vr_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_018'] = {'inputs': ['vr_replacement_018'], 'func': vr_replacement_d2_018}


def vr_replacement_d2_019(vr_replacement_019):
    feature = _clean(vr_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_019'] = {'inputs': ['vr_replacement_019'], 'func': vr_replacement_d2_019}


def vr_replacement_d2_020(vr_replacement_020):
    feature = _clean(vr_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_020'] = {'inputs': ['vr_replacement_020'], 'func': vr_replacement_d2_020}


def vr_replacement_d2_021(vr_replacement_021):
    feature = _clean(vr_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_021'] = {'inputs': ['vr_replacement_021'], 'func': vr_replacement_d2_021}


def vr_replacement_d2_022(vr_replacement_022):
    feature = _clean(vr_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_022'] = {'inputs': ['vr_replacement_022'], 'func': vr_replacement_d2_022}


def vr_replacement_d2_023(vr_replacement_023):
    feature = _clean(vr_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_023'] = {'inputs': ['vr_replacement_023'], 'func': vr_replacement_d2_023}


def vr_replacement_d2_024(vr_replacement_024):
    feature = _clean(vr_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_024'] = {'inputs': ['vr_replacement_024'], 'func': vr_replacement_d2_024}


def vr_replacement_d2_025(vr_replacement_025):
    feature = _clean(vr_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_025'] = {'inputs': ['vr_replacement_025'], 'func': vr_replacement_d2_025}


def vr_replacement_d2_026(vr_replacement_026):
    feature = _clean(vr_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_026'] = {'inputs': ['vr_replacement_026'], 'func': vr_replacement_d2_026}


def vr_replacement_d2_027(vr_replacement_027):
    feature = _clean(vr_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_027'] = {'inputs': ['vr_replacement_027'], 'func': vr_replacement_d2_027}


def vr_replacement_d2_028(vr_replacement_028):
    feature = _clean(vr_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_028'] = {'inputs': ['vr_replacement_028'], 'func': vr_replacement_d2_028}


def vr_replacement_d2_029(vr_replacement_029):
    feature = _clean(vr_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_029'] = {'inputs': ['vr_replacement_029'], 'func': vr_replacement_d2_029}


def vr_replacement_d2_030(vr_replacement_030):
    feature = _clean(vr_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_030'] = {'inputs': ['vr_replacement_030'], 'func': vr_replacement_d2_030}


def vr_replacement_d2_031(vr_replacement_031):
    feature = _clean(vr_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_031'] = {'inputs': ['vr_replacement_031'], 'func': vr_replacement_d2_031}


def vr_replacement_d2_032(vr_replacement_032):
    feature = _clean(vr_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_032'] = {'inputs': ['vr_replacement_032'], 'func': vr_replacement_d2_032}


def vr_replacement_d2_033(vr_replacement_033):
    feature = _clean(vr_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_033'] = {'inputs': ['vr_replacement_033'], 'func': vr_replacement_d2_033}


def vr_replacement_d2_034(vr_replacement_034):
    feature = _clean(vr_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_034'] = {'inputs': ['vr_replacement_034'], 'func': vr_replacement_d2_034}


def vr_replacement_d2_035(vr_replacement_035):
    feature = _clean(vr_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_035'] = {'inputs': ['vr_replacement_035'], 'func': vr_replacement_d2_035}


def vr_replacement_d2_036(vr_replacement_036):
    feature = _clean(vr_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_036'] = {'inputs': ['vr_replacement_036'], 'func': vr_replacement_d2_036}


def vr_replacement_d2_037(vr_replacement_037):
    feature = _clean(vr_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_037'] = {'inputs': ['vr_replacement_037'], 'func': vr_replacement_d2_037}


def vr_replacement_d2_038(vr_replacement_038):
    feature = _clean(vr_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_038'] = {'inputs': ['vr_replacement_038'], 'func': vr_replacement_d2_038}


def vr_replacement_d2_039(vr_replacement_039):
    feature = _clean(vr_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_039'] = {'inputs': ['vr_replacement_039'], 'func': vr_replacement_d2_039}


def vr_replacement_d2_040(vr_replacement_040):
    feature = _clean(vr_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_040'] = {'inputs': ['vr_replacement_040'], 'func': vr_replacement_d2_040}


def vr_replacement_d2_041(vr_replacement_041):
    feature = _clean(vr_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_041'] = {'inputs': ['vr_replacement_041'], 'func': vr_replacement_d2_041}


def vr_replacement_d2_042(vr_replacement_042):
    feature = _clean(vr_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_042'] = {'inputs': ['vr_replacement_042'], 'func': vr_replacement_d2_042}


def vr_replacement_d2_043(vr_replacement_043):
    feature = _clean(vr_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_043'] = {'inputs': ['vr_replacement_043'], 'func': vr_replacement_d2_043}


def vr_replacement_d2_044(vr_replacement_044):
    feature = _clean(vr_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_044'] = {'inputs': ['vr_replacement_044'], 'func': vr_replacement_d2_044}


def vr_replacement_d2_045(vr_replacement_045):
    feature = _clean(vr_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_045'] = {'inputs': ['vr_replacement_045'], 'func': vr_replacement_d2_045}


def vr_replacement_d2_046(vr_replacement_046):
    feature = _clean(vr_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_046'] = {'inputs': ['vr_replacement_046'], 'func': vr_replacement_d2_046}


def vr_replacement_d2_047(vr_replacement_047):
    feature = _clean(vr_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_047'] = {'inputs': ['vr_replacement_047'], 'func': vr_replacement_d2_047}


def vr_replacement_d2_048(vr_replacement_048):
    feature = _clean(vr_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_048'] = {'inputs': ['vr_replacement_048'], 'func': vr_replacement_d2_048}


def vr_replacement_d2_049(vr_replacement_049):
    feature = _clean(vr_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_049'] = {'inputs': ['vr_replacement_049'], 'func': vr_replacement_d2_049}


def vr_replacement_d2_050(vr_replacement_050):
    feature = _clean(vr_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_050'] = {'inputs': ['vr_replacement_050'], 'func': vr_replacement_d2_050}


def vr_replacement_d2_051(vr_replacement_051):
    feature = _clean(vr_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_051'] = {'inputs': ['vr_replacement_051'], 'func': vr_replacement_d2_051}


def vr_replacement_d2_052(vr_replacement_052):
    feature = _clean(vr_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_052'] = {'inputs': ['vr_replacement_052'], 'func': vr_replacement_d2_052}


def vr_replacement_d2_053(vr_replacement_053):
    feature = _clean(vr_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_053'] = {'inputs': ['vr_replacement_053'], 'func': vr_replacement_d2_053}


def vr_replacement_d2_054(vr_replacement_054):
    feature = _clean(vr_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_054'] = {'inputs': ['vr_replacement_054'], 'func': vr_replacement_d2_054}


def vr_replacement_d2_055(vr_replacement_055):
    feature = _clean(vr_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_055'] = {'inputs': ['vr_replacement_055'], 'func': vr_replacement_d2_055}


def vr_replacement_d2_056(vr_replacement_056):
    feature = _clean(vr_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_056'] = {'inputs': ['vr_replacement_056'], 'func': vr_replacement_d2_056}


def vr_replacement_d2_057(vr_replacement_057):
    feature = _clean(vr_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_057'] = {'inputs': ['vr_replacement_057'], 'func': vr_replacement_d2_057}


def vr_replacement_d2_058(vr_replacement_058):
    feature = _clean(vr_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_058'] = {'inputs': ['vr_replacement_058'], 'func': vr_replacement_d2_058}


def vr_replacement_d2_059(vr_replacement_059):
    feature = _clean(vr_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_059'] = {'inputs': ['vr_replacement_059'], 'func': vr_replacement_d2_059}


def vr_replacement_d2_060(vr_replacement_060):
    feature = _clean(vr_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_060'] = {'inputs': ['vr_replacement_060'], 'func': vr_replacement_d2_060}


def vr_replacement_d2_061(vr_replacement_061):
    feature = _clean(vr_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_061'] = {'inputs': ['vr_replacement_061'], 'func': vr_replacement_d2_061}


def vr_replacement_d2_062(vr_replacement_062):
    feature = _clean(vr_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_062'] = {'inputs': ['vr_replacement_062'], 'func': vr_replacement_d2_062}


def vr_replacement_d2_063(vr_replacement_063):
    feature = _clean(vr_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_063'] = {'inputs': ['vr_replacement_063'], 'func': vr_replacement_d2_063}


def vr_replacement_d2_064(vr_replacement_064):
    feature = _clean(vr_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_064'] = {'inputs': ['vr_replacement_064'], 'func': vr_replacement_d2_064}


def vr_replacement_d2_065(vr_replacement_065):
    feature = _clean(vr_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_065'] = {'inputs': ['vr_replacement_065'], 'func': vr_replacement_d2_065}


def vr_replacement_d2_066(vr_replacement_066):
    feature = _clean(vr_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_066'] = {'inputs': ['vr_replacement_066'], 'func': vr_replacement_d2_066}


def vr_replacement_d2_067(vr_replacement_067):
    feature = _clean(vr_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_067'] = {'inputs': ['vr_replacement_067'], 'func': vr_replacement_d2_067}


def vr_replacement_d2_068(vr_replacement_068):
    feature = _clean(vr_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_068'] = {'inputs': ['vr_replacement_068'], 'func': vr_replacement_d2_068}


def vr_replacement_d2_069(vr_replacement_069):
    feature = _clean(vr_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_069'] = {'inputs': ['vr_replacement_069'], 'func': vr_replacement_d2_069}


def vr_replacement_d2_070(vr_replacement_070):
    feature = _clean(vr_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_070'] = {'inputs': ['vr_replacement_070'], 'func': vr_replacement_d2_070}


def vr_replacement_d2_071(vr_replacement_071):
    feature = _clean(vr_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_071'] = {'inputs': ['vr_replacement_071'], 'func': vr_replacement_d2_071}


def vr_replacement_d2_072(vr_replacement_072):
    feature = _clean(vr_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_072'] = {'inputs': ['vr_replacement_072'], 'func': vr_replacement_d2_072}


def vr_replacement_d2_073(vr_replacement_073):
    feature = _clean(vr_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_073'] = {'inputs': ['vr_replacement_073'], 'func': vr_replacement_d2_073}


def vr_replacement_d2_074(vr_replacement_074):
    feature = _clean(vr_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_074'] = {'inputs': ['vr_replacement_074'], 'func': vr_replacement_d2_074}


def vr_replacement_d2_075(vr_replacement_075):
    feature = _clean(vr_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_075'] = {'inputs': ['vr_replacement_075'], 'func': vr_replacement_d2_075}


def vr_replacement_d2_076(vr_replacement_076):
    feature = _clean(vr_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_076'] = {'inputs': ['vr_replacement_076'], 'func': vr_replacement_d2_076}


def vr_replacement_d2_077(vr_replacement_077):
    feature = _clean(vr_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_077'] = {'inputs': ['vr_replacement_077'], 'func': vr_replacement_d2_077}


def vr_replacement_d2_078(vr_replacement_078):
    feature = _clean(vr_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_078'] = {'inputs': ['vr_replacement_078'], 'func': vr_replacement_d2_078}


def vr_replacement_d2_079(vr_replacement_079):
    feature = _clean(vr_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_079'] = {'inputs': ['vr_replacement_079'], 'func': vr_replacement_d2_079}


def vr_replacement_d2_080(vr_replacement_080):
    feature = _clean(vr_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_080'] = {'inputs': ['vr_replacement_080'], 'func': vr_replacement_d2_080}


def vr_replacement_d2_081(vr_replacement_081):
    feature = _clean(vr_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_081'] = {'inputs': ['vr_replacement_081'], 'func': vr_replacement_d2_081}


def vr_replacement_d2_082(vr_replacement_082):
    feature = _clean(vr_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_082'] = {'inputs': ['vr_replacement_082'], 'func': vr_replacement_d2_082}


def vr_replacement_d2_083(vr_replacement_083):
    feature = _clean(vr_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_083'] = {'inputs': ['vr_replacement_083'], 'func': vr_replacement_d2_083}


def vr_replacement_d2_084(vr_replacement_084):
    feature = _clean(vr_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_084'] = {'inputs': ['vr_replacement_084'], 'func': vr_replacement_d2_084}


def vr_replacement_d2_085(vr_replacement_085):
    feature = _clean(vr_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_085'] = {'inputs': ['vr_replacement_085'], 'func': vr_replacement_d2_085}


def vr_replacement_d2_086(vr_replacement_086):
    feature = _clean(vr_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_086'] = {'inputs': ['vr_replacement_086'], 'func': vr_replacement_d2_086}


def vr_replacement_d2_087(vr_replacement_087):
    feature = _clean(vr_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_087'] = {'inputs': ['vr_replacement_087'], 'func': vr_replacement_d2_087}


def vr_replacement_d2_088(vr_replacement_088):
    feature = _clean(vr_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_088'] = {'inputs': ['vr_replacement_088'], 'func': vr_replacement_d2_088}


def vr_replacement_d2_089(vr_replacement_089):
    feature = _clean(vr_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_089'] = {'inputs': ['vr_replacement_089'], 'func': vr_replacement_d2_089}


def vr_replacement_d2_090(vr_replacement_090):
    feature = _clean(vr_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_090'] = {'inputs': ['vr_replacement_090'], 'func': vr_replacement_d2_090}


def vr_replacement_d2_091(vr_replacement_091):
    feature = _clean(vr_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_091'] = {'inputs': ['vr_replacement_091'], 'func': vr_replacement_d2_091}


def vr_replacement_d2_092(vr_replacement_092):
    feature = _clean(vr_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_092'] = {'inputs': ['vr_replacement_092'], 'func': vr_replacement_d2_092}


def vr_replacement_d2_093(vr_replacement_093):
    feature = _clean(vr_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_093'] = {'inputs': ['vr_replacement_093'], 'func': vr_replacement_d2_093}


def vr_replacement_d2_094(vr_replacement_094):
    feature = _clean(vr_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_094'] = {'inputs': ['vr_replacement_094'], 'func': vr_replacement_d2_094}


def vr_replacement_d2_095(vr_replacement_095):
    feature = _clean(vr_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_095'] = {'inputs': ['vr_replacement_095'], 'func': vr_replacement_d2_095}


def vr_replacement_d2_096(vr_replacement_096):
    feature = _clean(vr_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_096'] = {'inputs': ['vr_replacement_096'], 'func': vr_replacement_d2_096}


def vr_replacement_d2_097(vr_replacement_097):
    feature = _clean(vr_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_097'] = {'inputs': ['vr_replacement_097'], 'func': vr_replacement_d2_097}


def vr_replacement_d2_098(vr_replacement_098):
    feature = _clean(vr_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_098'] = {'inputs': ['vr_replacement_098'], 'func': vr_replacement_d2_098}


def vr_replacement_d2_099(vr_replacement_099):
    feature = _clean(vr_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_099'] = {'inputs': ['vr_replacement_099'], 'func': vr_replacement_d2_099}


def vr_replacement_d2_100(vr_replacement_100):
    feature = _clean(vr_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_100'] = {'inputs': ['vr_replacement_100'], 'func': vr_replacement_d2_100}


def vr_replacement_d2_101(vr_replacement_101):
    feature = _clean(vr_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_101'] = {'inputs': ['vr_replacement_101'], 'func': vr_replacement_d2_101}


def vr_replacement_d2_102(vr_replacement_102):
    feature = _clean(vr_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_102'] = {'inputs': ['vr_replacement_102'], 'func': vr_replacement_d2_102}


def vr_replacement_d2_103(vr_replacement_103):
    feature = _clean(vr_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_103'] = {'inputs': ['vr_replacement_103'], 'func': vr_replacement_d2_103}


def vr_replacement_d2_104(vr_replacement_104):
    feature = _clean(vr_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_104'] = {'inputs': ['vr_replacement_104'], 'func': vr_replacement_d2_104}


def vr_replacement_d2_105(vr_replacement_105):
    feature = _clean(vr_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_105'] = {'inputs': ['vr_replacement_105'], 'func': vr_replacement_d2_105}


def vr_replacement_d2_106(vr_replacement_106):
    feature = _clean(vr_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_106'] = {'inputs': ['vr_replacement_106'], 'func': vr_replacement_d2_106}


def vr_replacement_d2_107(vr_replacement_107):
    feature = _clean(vr_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_107'] = {'inputs': ['vr_replacement_107'], 'func': vr_replacement_d2_107}


def vr_replacement_d2_108(vr_replacement_108):
    feature = _clean(vr_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_108'] = {'inputs': ['vr_replacement_108'], 'func': vr_replacement_d2_108}


def vr_replacement_d2_109(vr_replacement_109):
    feature = _clean(vr_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_109'] = {'inputs': ['vr_replacement_109'], 'func': vr_replacement_d2_109}


def vr_replacement_d2_110(vr_replacement_110):
    feature = _clean(vr_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_110'] = {'inputs': ['vr_replacement_110'], 'func': vr_replacement_d2_110}


def vr_replacement_d2_111(vr_replacement_111):
    feature = _clean(vr_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_111'] = {'inputs': ['vr_replacement_111'], 'func': vr_replacement_d2_111}


def vr_replacement_d2_112(vr_replacement_112):
    feature = _clean(vr_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_112'] = {'inputs': ['vr_replacement_112'], 'func': vr_replacement_d2_112}


def vr_replacement_d2_113(vr_replacement_113):
    feature = _clean(vr_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_113'] = {'inputs': ['vr_replacement_113'], 'func': vr_replacement_d2_113}


def vr_replacement_d2_114(vr_replacement_114):
    feature = _clean(vr_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_114'] = {'inputs': ['vr_replacement_114'], 'func': vr_replacement_d2_114}


def vr_replacement_d2_115(vr_replacement_115):
    feature = _clean(vr_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_115'] = {'inputs': ['vr_replacement_115'], 'func': vr_replacement_d2_115}


def vr_replacement_d2_116(vr_replacement_116):
    feature = _clean(vr_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_116'] = {'inputs': ['vr_replacement_116'], 'func': vr_replacement_d2_116}


def vr_replacement_d2_117(vr_replacement_117):
    feature = _clean(vr_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_117'] = {'inputs': ['vr_replacement_117'], 'func': vr_replacement_d2_117}


def vr_replacement_d2_118(vr_replacement_118):
    feature = _clean(vr_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_118'] = {'inputs': ['vr_replacement_118'], 'func': vr_replacement_d2_118}


def vr_replacement_d2_119(vr_replacement_119):
    feature = _clean(vr_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_119'] = {'inputs': ['vr_replacement_119'], 'func': vr_replacement_d2_119}


def vr_replacement_d2_120(vr_replacement_120):
    feature = _clean(vr_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_120'] = {'inputs': ['vr_replacement_120'], 'func': vr_replacement_d2_120}


def vr_replacement_d2_121(vr_replacement_121):
    feature = _clean(vr_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_121'] = {'inputs': ['vr_replacement_121'], 'func': vr_replacement_d2_121}


def vr_replacement_d2_122(vr_replacement_122):
    feature = _clean(vr_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_122'] = {'inputs': ['vr_replacement_122'], 'func': vr_replacement_d2_122}


def vr_replacement_d2_123(vr_replacement_123):
    feature = _clean(vr_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_123'] = {'inputs': ['vr_replacement_123'], 'func': vr_replacement_d2_123}


def vr_replacement_d2_124(vr_replacement_124):
    feature = _clean(vr_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_124'] = {'inputs': ['vr_replacement_124'], 'func': vr_replacement_d2_124}


def vr_replacement_d2_125(vr_replacement_125):
    feature = _clean(vr_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_125'] = {'inputs': ['vr_replacement_125'], 'func': vr_replacement_d2_125}


def vr_replacement_d2_126(vr_replacement_126):
    feature = _clean(vr_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_126'] = {'inputs': ['vr_replacement_126'], 'func': vr_replacement_d2_126}


def vr_replacement_d2_127(vr_replacement_127):
    feature = _clean(vr_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_127'] = {'inputs': ['vr_replacement_127'], 'func': vr_replacement_d2_127}


def vr_replacement_d2_128(vr_replacement_128):
    feature = _clean(vr_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_128'] = {'inputs': ['vr_replacement_128'], 'func': vr_replacement_d2_128}


def vr_replacement_d2_129(vr_replacement_129):
    feature = _clean(vr_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_129'] = {'inputs': ['vr_replacement_129'], 'func': vr_replacement_d2_129}


def vr_replacement_d2_130(vr_replacement_130):
    feature = _clean(vr_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_130'] = {'inputs': ['vr_replacement_130'], 'func': vr_replacement_d2_130}


def vr_replacement_d2_131(vr_replacement_131):
    feature = _clean(vr_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_131'] = {'inputs': ['vr_replacement_131'], 'func': vr_replacement_d2_131}


def vr_replacement_d2_132(vr_replacement_132):
    feature = _clean(vr_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_132'] = {'inputs': ['vr_replacement_132'], 'func': vr_replacement_d2_132}


def vr_replacement_d2_133(vr_replacement_133):
    feature = _clean(vr_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_133'] = {'inputs': ['vr_replacement_133'], 'func': vr_replacement_d2_133}


def vr_replacement_d2_134(vr_replacement_134):
    feature = _clean(vr_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_134'] = {'inputs': ['vr_replacement_134'], 'func': vr_replacement_d2_134}


def vr_replacement_d2_135(vr_replacement_135):
    feature = _clean(vr_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_135'] = {'inputs': ['vr_replacement_135'], 'func': vr_replacement_d2_135}


def vr_replacement_d2_136(vr_replacement_136):
    feature = _clean(vr_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_136'] = {'inputs': ['vr_replacement_136'], 'func': vr_replacement_d2_136}


def vr_replacement_d2_137(vr_replacement_137):
    feature = _clean(vr_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_137'] = {'inputs': ['vr_replacement_137'], 'func': vr_replacement_d2_137}


def vr_replacement_d2_138(vr_replacement_138):
    feature = _clean(vr_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_138'] = {'inputs': ['vr_replacement_138'], 'func': vr_replacement_d2_138}


def vr_replacement_d2_139(vr_replacement_139):
    feature = _clean(vr_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_139'] = {'inputs': ['vr_replacement_139'], 'func': vr_replacement_d2_139}


def vr_replacement_d2_140(vr_replacement_140):
    feature = _clean(vr_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_140'] = {'inputs': ['vr_replacement_140'], 'func': vr_replacement_d2_140}


def vr_replacement_d2_141(vr_replacement_141):
    feature = _clean(vr_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_141'] = {'inputs': ['vr_replacement_141'], 'func': vr_replacement_d2_141}


def vr_replacement_d2_142(vr_replacement_142):
    feature = _clean(vr_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_142'] = {'inputs': ['vr_replacement_142'], 'func': vr_replacement_d2_142}


def vr_replacement_d2_143(vr_replacement_143):
    feature = _clean(vr_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_143'] = {'inputs': ['vr_replacement_143'], 'func': vr_replacement_d2_143}


def vr_replacement_d2_144(vr_replacement_144):
    feature = _clean(vr_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_144'] = {'inputs': ['vr_replacement_144'], 'func': vr_replacement_d2_144}


def vr_replacement_d2_145(vr_replacement_145):
    feature = _clean(vr_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_145'] = {'inputs': ['vr_replacement_145'], 'func': vr_replacement_d2_145}


def vr_replacement_d2_146(vr_replacement_146):
    feature = _clean(vr_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_146'] = {'inputs': ['vr_replacement_146'], 'func': vr_replacement_d2_146}


def vr_replacement_d2_147(vr_replacement_147):
    feature = _clean(vr_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_147'] = {'inputs': ['vr_replacement_147'], 'func': vr_replacement_d2_147}


def vr_replacement_d2_148(vr_replacement_148):
    feature = _clean(vr_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_148'] = {'inputs': ['vr_replacement_148'], 'func': vr_replacement_d2_148}


def vr_replacement_d2_149(vr_replacement_149):
    feature = _clean(vr_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_149'] = {'inputs': ['vr_replacement_149'], 'func': vr_replacement_d2_149}


def vr_replacement_d2_150(vr_replacement_150):
    feature = _clean(vr_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_150'] = {'inputs': ['vr_replacement_150'], 'func': vr_replacement_d2_150}


def vr_replacement_d2_151(vr_replacement_151):
    feature = _clean(vr_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_151'] = {'inputs': ['vr_replacement_151'], 'func': vr_replacement_d2_151}


def vr_replacement_d2_152(vr_replacement_152):
    feature = _clean(vr_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_152'] = {'inputs': ['vr_replacement_152'], 'func': vr_replacement_d2_152}


def vr_replacement_d2_153(vr_replacement_153):
    feature = _clean(vr_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_153'] = {'inputs': ['vr_replacement_153'], 'func': vr_replacement_d2_153}


def vr_replacement_d2_154(vr_replacement_154):
    feature = _clean(vr_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_154'] = {'inputs': ['vr_replacement_154'], 'func': vr_replacement_d2_154}


def vr_replacement_d2_155(vr_replacement_155):
    feature = _clean(vr_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_155'] = {'inputs': ['vr_replacement_155'], 'func': vr_replacement_d2_155}


def vr_replacement_d2_156(vr_replacement_156):
    feature = _clean(vr_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_156'] = {'inputs': ['vr_replacement_156'], 'func': vr_replacement_d2_156}


def vr_replacement_d2_157(vr_replacement_157):
    feature = _clean(vr_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_157'] = {'inputs': ['vr_replacement_157'], 'func': vr_replacement_d2_157}


def vr_replacement_d2_158(vr_replacement_158):
    feature = _clean(vr_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_158'] = {'inputs': ['vr_replacement_158'], 'func': vr_replacement_d2_158}


def vr_replacement_d2_159(vr_replacement_159):
    feature = _clean(vr_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_159'] = {'inputs': ['vr_replacement_159'], 'func': vr_replacement_d2_159}


def vr_replacement_d2_160(vr_replacement_160):
    feature = _clean(vr_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_160'] = {'inputs': ['vr_replacement_160'], 'func': vr_replacement_d2_160}


def vr_replacement_d2_161(vr_replacement_161):
    feature = _clean(vr_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_161'] = {'inputs': ['vr_replacement_161'], 'func': vr_replacement_d2_161}


def vr_replacement_d2_162(vr_replacement_162):
    feature = _clean(vr_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_162'] = {'inputs': ['vr_replacement_162'], 'func': vr_replacement_d2_162}


def vr_replacement_d2_163(vr_replacement_163):
    feature = _clean(vr_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_163'] = {'inputs': ['vr_replacement_163'], 'func': vr_replacement_d2_163}


def vr_replacement_d2_164(vr_replacement_164):
    feature = _clean(vr_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_164'] = {'inputs': ['vr_replacement_164'], 'func': vr_replacement_d2_164}


def vr_replacement_d2_165(vr_replacement_165):
    feature = _clean(vr_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_165'] = {'inputs': ['vr_replacement_165'], 'func': vr_replacement_d2_165}


def vr_replacement_d2_166(vr_replacement_166):
    feature = _clean(vr_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_166'] = {'inputs': ['vr_replacement_166'], 'func': vr_replacement_d2_166}


def vr_replacement_d2_167(vr_replacement_167):
    feature = _clean(vr_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_167'] = {'inputs': ['vr_replacement_167'], 'func': vr_replacement_d2_167}


def vr_replacement_d2_168(vr_replacement_168):
    feature = _clean(vr_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_168'] = {'inputs': ['vr_replacement_168'], 'func': vr_replacement_d2_168}


def vr_replacement_d2_169(vr_replacement_169):
    feature = _clean(vr_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_169'] = {'inputs': ['vr_replacement_169'], 'func': vr_replacement_d2_169}


def vr_replacement_d2_170(vr_replacement_170):
    feature = _clean(vr_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_170'] = {'inputs': ['vr_replacement_170'], 'func': vr_replacement_d2_170}


def vr_replacement_d2_171(vr_replacement_171):
    feature = _clean(vr_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_171'] = {'inputs': ['vr_replacement_171'], 'func': vr_replacement_d2_171}


def vr_replacement_d2_172(vr_replacement_172):
    feature = _clean(vr_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_172'] = {'inputs': ['vr_replacement_172'], 'func': vr_replacement_d2_172}


def vr_replacement_d2_173(vr_replacement_173):
    feature = _clean(vr_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_173'] = {'inputs': ['vr_replacement_173'], 'func': vr_replacement_d2_173}


def vr_replacement_d2_174(vr_replacement_174):
    feature = _clean(vr_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_174'] = {'inputs': ['vr_replacement_174'], 'func': vr_replacement_d2_174}


def vr_replacement_d2_175(vr_replacement_175):
    feature = _clean(vr_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
VR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vr_replacement_d2_175'] = {'inputs': ['vr_replacement_175'], 'func': vr_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vrg_base_universe_d2_001_vrg_002_range_expansion_10_002(vrg_002_range_expansion_10_002):
    return _base_universe_d2(vrg_002_range_expansion_10_002, 1)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_001_vrg_002_range_expansion_10_002'] = {'inputs': ['vrg_002_range_expansion_10_002'], 'func': vrg_base_universe_d2_001_vrg_002_range_expansion_10_002}


def vrg_base_universe_d2_002_vrg_004_close_location_42_004(vrg_004_close_location_42_004):
    return _base_universe_d2(vrg_004_close_location_42_004, 2)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_002_vrg_004_close_location_42_004'] = {'inputs': ['vrg_004_close_location_42_004'], 'func': vrg_base_universe_d2_002_vrg_004_close_location_42_004}


def vrg_base_universe_d2_003_vrg_005_atr_move_63_005(vrg_005_atr_move_63_005):
    return _base_universe_d2(vrg_005_atr_move_63_005, 3)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_003_vrg_005_atr_move_63_005'] = {'inputs': ['vrg_005_atr_move_63_005'], 'func': vrg_base_universe_d2_003_vrg_005_atr_move_63_005}


def vrg_base_universe_d2_004_vrg_008_range_expansion_189_008(vrg_008_range_expansion_189_008):
    return _base_universe_d2(vrg_008_range_expansion_189_008, 4)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_004_vrg_008_range_expansion_189_008'] = {'inputs': ['vrg_008_range_expansion_189_008'], 'func': vrg_base_universe_d2_004_vrg_008_range_expansion_189_008}


def vrg_base_universe_d2_005_vrg_010_close_location_378_010(vrg_010_close_location_378_010):
    return _base_universe_d2(vrg_010_close_location_378_010, 5)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_005_vrg_010_close_location_378_010'] = {'inputs': ['vrg_010_close_location_378_010'], 'func': vrg_base_universe_d2_005_vrg_010_close_location_378_010}


def vrg_base_universe_d2_006_vrg_011_atr_move_504_011(vrg_011_atr_move_504_011):
    return _base_universe_d2(vrg_011_atr_move_504_011, 6)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_006_vrg_011_atr_move_504_011'] = {'inputs': ['vrg_011_atr_move_504_011'], 'func': vrg_base_universe_d2_006_vrg_011_atr_move_504_011}


def vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014(vrg_014_range_expansion_1260_014):
    return _base_universe_d2(vrg_014_range_expansion_1260_014, 7)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014'] = {'inputs': ['vrg_014_range_expansion_1260_014'], 'func': vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014}


def vrg_base_universe_d2_008_vrg_016_close_location_5_016(vrg_016_close_location_5_016):
    return _base_universe_d2(vrg_016_close_location_5_016, 8)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_008_vrg_016_close_location_5_016'] = {'inputs': ['vrg_016_close_location_5_016'], 'func': vrg_base_universe_d2_008_vrg_016_close_location_5_016}


def vrg_base_universe_d2_009_vrg_017_atr_move_10_017(vrg_017_atr_move_10_017):
    return _base_universe_d2(vrg_017_atr_move_10_017, 9)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_009_vrg_017_atr_move_10_017'] = {'inputs': ['vrg_017_atr_move_10_017'], 'func': vrg_base_universe_d2_009_vrg_017_atr_move_10_017}


def vrg_base_universe_d2_010_vrg_020_range_expansion_63_020(vrg_020_range_expansion_63_020):
    return _base_universe_d2(vrg_020_range_expansion_63_020, 10)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_010_vrg_020_range_expansion_63_020'] = {'inputs': ['vrg_020_range_expansion_63_020'], 'func': vrg_base_universe_d2_010_vrg_020_range_expansion_63_020}


def vrg_base_universe_d2_011_vrg_022_close_location_126_022(vrg_022_close_location_126_022):
    return _base_universe_d2(vrg_022_close_location_126_022, 11)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_011_vrg_022_close_location_126_022'] = {'inputs': ['vrg_022_close_location_126_022'], 'func': vrg_base_universe_d2_011_vrg_022_close_location_126_022}


def vrg_base_universe_d2_012_vrg_023_atr_move_189_023(vrg_023_atr_move_189_023):
    return _base_universe_d2(vrg_023_atr_move_189_023, 12)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_012_vrg_023_atr_move_189_023'] = {'inputs': ['vrg_023_atr_move_189_023'], 'func': vrg_base_universe_d2_012_vrg_023_atr_move_189_023}


def vrg_base_universe_d2_013_vrg_026_range_expansion_504_026(vrg_026_range_expansion_504_026):
    return _base_universe_d2(vrg_026_range_expansion_504_026, 13)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_013_vrg_026_range_expansion_504_026'] = {'inputs': ['vrg_026_range_expansion_504_026'], 'func': vrg_base_universe_d2_013_vrg_026_range_expansion_504_026}


def vrg_base_universe_d2_014_vrg_028_close_location_1008_028(vrg_028_close_location_1008_028):
    return _base_universe_d2(vrg_028_close_location_1008_028, 14)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_014_vrg_028_close_location_1008_028'] = {'inputs': ['vrg_028_close_location_1008_028'], 'func': vrg_base_universe_d2_014_vrg_028_close_location_1008_028}


def vrg_base_universe_d2_015_vrg_029_atr_move_1260_029(vrg_029_atr_move_1260_029):
    return _base_universe_d2(vrg_029_atr_move_1260_029, 15)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_015_vrg_029_atr_move_1260_029'] = {'inputs': ['vrg_029_atr_move_1260_029'], 'func': vrg_base_universe_d2_015_vrg_029_atr_move_1260_029}


def vrg_base_universe_d2_016_vrg_basefill_001(vrg_basefill_001):
    return _base_universe_d2(vrg_basefill_001, 16)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_016_vrg_basefill_001'] = {'inputs': ['vrg_basefill_001'], 'func': vrg_base_universe_d2_016_vrg_basefill_001}


def vrg_base_universe_d2_017_vrg_basefill_003(vrg_basefill_003):
    return _base_universe_d2(vrg_basefill_003, 17)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_017_vrg_basefill_003'] = {'inputs': ['vrg_basefill_003'], 'func': vrg_base_universe_d2_017_vrg_basefill_003}


def vrg_base_universe_d2_018_vrg_basefill_006(vrg_basefill_006):
    return _base_universe_d2(vrg_basefill_006, 18)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_018_vrg_basefill_006'] = {'inputs': ['vrg_basefill_006'], 'func': vrg_base_universe_d2_018_vrg_basefill_006}


def vrg_base_universe_d2_019_vrg_basefill_007(vrg_basefill_007):
    return _base_universe_d2(vrg_basefill_007, 19)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_019_vrg_basefill_007'] = {'inputs': ['vrg_basefill_007'], 'func': vrg_base_universe_d2_019_vrg_basefill_007}


def vrg_base_universe_d2_020_vrg_basefill_009(vrg_basefill_009):
    return _base_universe_d2(vrg_basefill_009, 20)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_020_vrg_basefill_009'] = {'inputs': ['vrg_basefill_009'], 'func': vrg_base_universe_d2_020_vrg_basefill_009}


def vrg_base_universe_d2_021_vrg_basefill_012(vrg_basefill_012):
    return _base_universe_d2(vrg_basefill_012, 21)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_021_vrg_basefill_012'] = {'inputs': ['vrg_basefill_012'], 'func': vrg_base_universe_d2_021_vrg_basefill_012}


def vrg_base_universe_d2_022_vrg_basefill_013(vrg_basefill_013):
    return _base_universe_d2(vrg_basefill_013, 22)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_022_vrg_basefill_013'] = {'inputs': ['vrg_basefill_013'], 'func': vrg_base_universe_d2_022_vrg_basefill_013}


def vrg_base_universe_d2_023_vrg_basefill_015(vrg_basefill_015):
    return _base_universe_d2(vrg_basefill_015, 23)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_023_vrg_basefill_015'] = {'inputs': ['vrg_basefill_015'], 'func': vrg_base_universe_d2_023_vrg_basefill_015}


def vrg_base_universe_d2_024_vrg_basefill_018(vrg_basefill_018):
    return _base_universe_d2(vrg_basefill_018, 24)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_024_vrg_basefill_018'] = {'inputs': ['vrg_basefill_018'], 'func': vrg_base_universe_d2_024_vrg_basefill_018}


def vrg_base_universe_d2_025_vrg_basefill_019(vrg_basefill_019):
    return _base_universe_d2(vrg_basefill_019, 25)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_025_vrg_basefill_019'] = {'inputs': ['vrg_basefill_019'], 'func': vrg_base_universe_d2_025_vrg_basefill_019}


def vrg_base_universe_d2_026_vrg_basefill_021(vrg_basefill_021):
    return _base_universe_d2(vrg_basefill_021, 26)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_026_vrg_basefill_021'] = {'inputs': ['vrg_basefill_021'], 'func': vrg_base_universe_d2_026_vrg_basefill_021}


def vrg_base_universe_d2_027_vrg_basefill_024(vrg_basefill_024):
    return _base_universe_d2(vrg_basefill_024, 27)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_027_vrg_basefill_024'] = {'inputs': ['vrg_basefill_024'], 'func': vrg_base_universe_d2_027_vrg_basefill_024}


def vrg_base_universe_d2_028_vrg_basefill_025(vrg_basefill_025):
    return _base_universe_d2(vrg_basefill_025, 28)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_028_vrg_basefill_025'] = {'inputs': ['vrg_basefill_025'], 'func': vrg_base_universe_d2_028_vrg_basefill_025}


def vrg_base_universe_d2_029_vrg_basefill_027(vrg_basefill_027):
    return _base_universe_d2(vrg_basefill_027, 29)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_029_vrg_basefill_027'] = {'inputs': ['vrg_basefill_027'], 'func': vrg_base_universe_d2_029_vrg_basefill_027}


def vrg_base_universe_d2_030_vrg_basefill_030(vrg_basefill_030):
    return _base_universe_d2(vrg_basefill_030, 30)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_030_vrg_basefill_030'] = {'inputs': ['vrg_basefill_030'], 'func': vrg_base_universe_d2_030_vrg_basefill_030}


def vrg_base_universe_d2_031_vrg_basefill_031(vrg_basefill_031):
    return _base_universe_d2(vrg_basefill_031, 31)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_031_vrg_basefill_031'] = {'inputs': ['vrg_basefill_031'], 'func': vrg_base_universe_d2_031_vrg_basefill_031}


def vrg_base_universe_d2_032_vrg_basefill_032(vrg_basefill_032):
    return _base_universe_d2(vrg_basefill_032, 32)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_032_vrg_basefill_032'] = {'inputs': ['vrg_basefill_032'], 'func': vrg_base_universe_d2_032_vrg_basefill_032}


def vrg_base_universe_d2_033_vrg_basefill_033(vrg_basefill_033):
    return _base_universe_d2(vrg_basefill_033, 33)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_033_vrg_basefill_033'] = {'inputs': ['vrg_basefill_033'], 'func': vrg_base_universe_d2_033_vrg_basefill_033}


def vrg_base_universe_d2_034_vrg_basefill_034(vrg_basefill_034):
    return _base_universe_d2(vrg_basefill_034, 34)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_034_vrg_basefill_034'] = {'inputs': ['vrg_basefill_034'], 'func': vrg_base_universe_d2_034_vrg_basefill_034}


def vrg_base_universe_d2_035_vrg_basefill_035(vrg_basefill_035):
    return _base_universe_d2(vrg_basefill_035, 35)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_035_vrg_basefill_035'] = {'inputs': ['vrg_basefill_035'], 'func': vrg_base_universe_d2_035_vrg_basefill_035}


def vrg_base_universe_d2_036_vrg_basefill_036(vrg_basefill_036):
    return _base_universe_d2(vrg_basefill_036, 36)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_036_vrg_basefill_036'] = {'inputs': ['vrg_basefill_036'], 'func': vrg_base_universe_d2_036_vrg_basefill_036}


def vrg_base_universe_d2_037_vrg_basefill_037(vrg_basefill_037):
    return _base_universe_d2(vrg_basefill_037, 37)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_037_vrg_basefill_037'] = {'inputs': ['vrg_basefill_037'], 'func': vrg_base_universe_d2_037_vrg_basefill_037}


def vrg_base_universe_d2_038_vrg_basefill_038(vrg_basefill_038):
    return _base_universe_d2(vrg_basefill_038, 38)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_038_vrg_basefill_038'] = {'inputs': ['vrg_basefill_038'], 'func': vrg_base_universe_d2_038_vrg_basefill_038}


def vrg_base_universe_d2_039_vrg_basefill_039(vrg_basefill_039):
    return _base_universe_d2(vrg_basefill_039, 39)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_039_vrg_basefill_039'] = {'inputs': ['vrg_basefill_039'], 'func': vrg_base_universe_d2_039_vrg_basefill_039}


def vrg_base_universe_d2_040_vrg_basefill_040(vrg_basefill_040):
    return _base_universe_d2(vrg_basefill_040, 40)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_040_vrg_basefill_040'] = {'inputs': ['vrg_basefill_040'], 'func': vrg_base_universe_d2_040_vrg_basefill_040}


def vrg_base_universe_d2_041_vrg_basefill_041(vrg_basefill_041):
    return _base_universe_d2(vrg_basefill_041, 41)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_041_vrg_basefill_041'] = {'inputs': ['vrg_basefill_041'], 'func': vrg_base_universe_d2_041_vrg_basefill_041}


def vrg_base_universe_d2_042_vrg_basefill_042(vrg_basefill_042):
    return _base_universe_d2(vrg_basefill_042, 42)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_042_vrg_basefill_042'] = {'inputs': ['vrg_basefill_042'], 'func': vrg_base_universe_d2_042_vrg_basefill_042}


def vrg_base_universe_d2_043_vrg_basefill_043(vrg_basefill_043):
    return _base_universe_d2(vrg_basefill_043, 43)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_043_vrg_basefill_043'] = {'inputs': ['vrg_basefill_043'], 'func': vrg_base_universe_d2_043_vrg_basefill_043}


def vrg_base_universe_d2_044_vrg_basefill_044(vrg_basefill_044):
    return _base_universe_d2(vrg_basefill_044, 44)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_044_vrg_basefill_044'] = {'inputs': ['vrg_basefill_044'], 'func': vrg_base_universe_d2_044_vrg_basefill_044}


def vrg_base_universe_d2_045_vrg_basefill_045(vrg_basefill_045):
    return _base_universe_d2(vrg_basefill_045, 45)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_045_vrg_basefill_045'] = {'inputs': ['vrg_basefill_045'], 'func': vrg_base_universe_d2_045_vrg_basefill_045}


def vrg_base_universe_d2_046_vrg_basefill_046(vrg_basefill_046):
    return _base_universe_d2(vrg_basefill_046, 46)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_046_vrg_basefill_046'] = {'inputs': ['vrg_basefill_046'], 'func': vrg_base_universe_d2_046_vrg_basefill_046}


def vrg_base_universe_d2_047_vrg_basefill_047(vrg_basefill_047):
    return _base_universe_d2(vrg_basefill_047, 47)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_047_vrg_basefill_047'] = {'inputs': ['vrg_basefill_047'], 'func': vrg_base_universe_d2_047_vrg_basefill_047}


def vrg_base_universe_d2_048_vrg_basefill_048(vrg_basefill_048):
    return _base_universe_d2(vrg_basefill_048, 48)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_048_vrg_basefill_048'] = {'inputs': ['vrg_basefill_048'], 'func': vrg_base_universe_d2_048_vrg_basefill_048}


def vrg_base_universe_d2_049_vrg_basefill_049(vrg_basefill_049):
    return _base_universe_d2(vrg_basefill_049, 49)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_049_vrg_basefill_049'] = {'inputs': ['vrg_basefill_049'], 'func': vrg_base_universe_d2_049_vrg_basefill_049}


def vrg_base_universe_d2_050_vrg_basefill_050(vrg_basefill_050):
    return _base_universe_d2(vrg_basefill_050, 50)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_050_vrg_basefill_050'] = {'inputs': ['vrg_basefill_050'], 'func': vrg_base_universe_d2_050_vrg_basefill_050}


def vrg_base_universe_d2_051_vrg_basefill_051(vrg_basefill_051):
    return _base_universe_d2(vrg_basefill_051, 51)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_051_vrg_basefill_051'] = {'inputs': ['vrg_basefill_051'], 'func': vrg_base_universe_d2_051_vrg_basefill_051}


def vrg_base_universe_d2_052_vrg_basefill_052(vrg_basefill_052):
    return _base_universe_d2(vrg_basefill_052, 52)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_052_vrg_basefill_052'] = {'inputs': ['vrg_basefill_052'], 'func': vrg_base_universe_d2_052_vrg_basefill_052}


def vrg_base_universe_d2_053_vrg_basefill_053(vrg_basefill_053):
    return _base_universe_d2(vrg_basefill_053, 53)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_053_vrg_basefill_053'] = {'inputs': ['vrg_basefill_053'], 'func': vrg_base_universe_d2_053_vrg_basefill_053}


def vrg_base_universe_d2_054_vrg_basefill_054(vrg_basefill_054):
    return _base_universe_d2(vrg_basefill_054, 54)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_054_vrg_basefill_054'] = {'inputs': ['vrg_basefill_054'], 'func': vrg_base_universe_d2_054_vrg_basefill_054}


def vrg_base_universe_d2_055_vrg_basefill_055(vrg_basefill_055):
    return _base_universe_d2(vrg_basefill_055, 55)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_055_vrg_basefill_055'] = {'inputs': ['vrg_basefill_055'], 'func': vrg_base_universe_d2_055_vrg_basefill_055}


def vrg_base_universe_d2_056_vrg_basefill_056(vrg_basefill_056):
    return _base_universe_d2(vrg_basefill_056, 56)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_056_vrg_basefill_056'] = {'inputs': ['vrg_basefill_056'], 'func': vrg_base_universe_d2_056_vrg_basefill_056}


def vrg_base_universe_d2_057_vrg_basefill_057(vrg_basefill_057):
    return _base_universe_d2(vrg_basefill_057, 57)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_057_vrg_basefill_057'] = {'inputs': ['vrg_basefill_057'], 'func': vrg_base_universe_d2_057_vrg_basefill_057}


def vrg_base_universe_d2_058_vrg_basefill_058(vrg_basefill_058):
    return _base_universe_d2(vrg_basefill_058, 58)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_058_vrg_basefill_058'] = {'inputs': ['vrg_basefill_058'], 'func': vrg_base_universe_d2_058_vrg_basefill_058}


def vrg_base_universe_d2_059_vrg_basefill_059(vrg_basefill_059):
    return _base_universe_d2(vrg_basefill_059, 59)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_059_vrg_basefill_059'] = {'inputs': ['vrg_basefill_059'], 'func': vrg_base_universe_d2_059_vrg_basefill_059}


def vrg_base_universe_d2_060_vrg_basefill_060(vrg_basefill_060):
    return _base_universe_d2(vrg_basefill_060, 60)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_060_vrg_basefill_060'] = {'inputs': ['vrg_basefill_060'], 'func': vrg_base_universe_d2_060_vrg_basefill_060}


def vrg_base_universe_d2_061_vrg_basefill_061(vrg_basefill_061):
    return _base_universe_d2(vrg_basefill_061, 61)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_061_vrg_basefill_061'] = {'inputs': ['vrg_basefill_061'], 'func': vrg_base_universe_d2_061_vrg_basefill_061}


def vrg_base_universe_d2_062_vrg_basefill_062(vrg_basefill_062):
    return _base_universe_d2(vrg_basefill_062, 62)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_062_vrg_basefill_062'] = {'inputs': ['vrg_basefill_062'], 'func': vrg_base_universe_d2_062_vrg_basefill_062}


def vrg_base_universe_d2_063_vrg_basefill_063(vrg_basefill_063):
    return _base_universe_d2(vrg_basefill_063, 63)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_063_vrg_basefill_063'] = {'inputs': ['vrg_basefill_063'], 'func': vrg_base_universe_d2_063_vrg_basefill_063}


def vrg_base_universe_d2_064_vrg_basefill_064(vrg_basefill_064):
    return _base_universe_d2(vrg_basefill_064, 64)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_064_vrg_basefill_064'] = {'inputs': ['vrg_basefill_064'], 'func': vrg_base_universe_d2_064_vrg_basefill_064}


def vrg_base_universe_d2_065_vrg_basefill_065(vrg_basefill_065):
    return _base_universe_d2(vrg_basefill_065, 65)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_065_vrg_basefill_065'] = {'inputs': ['vrg_basefill_065'], 'func': vrg_base_universe_d2_065_vrg_basefill_065}


def vrg_base_universe_d2_066_vrg_basefill_066(vrg_basefill_066):
    return _base_universe_d2(vrg_basefill_066, 66)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_066_vrg_basefill_066'] = {'inputs': ['vrg_basefill_066'], 'func': vrg_base_universe_d2_066_vrg_basefill_066}


def vrg_base_universe_d2_067_vrg_basefill_067(vrg_basefill_067):
    return _base_universe_d2(vrg_basefill_067, 67)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_067_vrg_basefill_067'] = {'inputs': ['vrg_basefill_067'], 'func': vrg_base_universe_d2_067_vrg_basefill_067}


def vrg_base_universe_d2_068_vrg_basefill_068(vrg_basefill_068):
    return _base_universe_d2(vrg_basefill_068, 68)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_068_vrg_basefill_068'] = {'inputs': ['vrg_basefill_068'], 'func': vrg_base_universe_d2_068_vrg_basefill_068}


def vrg_base_universe_d2_069_vrg_basefill_069(vrg_basefill_069):
    return _base_universe_d2(vrg_basefill_069, 69)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_069_vrg_basefill_069'] = {'inputs': ['vrg_basefill_069'], 'func': vrg_base_universe_d2_069_vrg_basefill_069}


def vrg_base_universe_d2_070_vrg_basefill_070(vrg_basefill_070):
    return _base_universe_d2(vrg_basefill_070, 70)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_070_vrg_basefill_070'] = {'inputs': ['vrg_basefill_070'], 'func': vrg_base_universe_d2_070_vrg_basefill_070}


def vrg_base_universe_d2_071_vrg_basefill_071(vrg_basefill_071):
    return _base_universe_d2(vrg_basefill_071, 71)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_071_vrg_basefill_071'] = {'inputs': ['vrg_basefill_071'], 'func': vrg_base_universe_d2_071_vrg_basefill_071}


def vrg_base_universe_d2_072_vrg_basefill_072(vrg_basefill_072):
    return _base_universe_d2(vrg_basefill_072, 72)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_072_vrg_basefill_072'] = {'inputs': ['vrg_basefill_072'], 'func': vrg_base_universe_d2_072_vrg_basefill_072}


def vrg_base_universe_d2_073_vrg_basefill_073(vrg_basefill_073):
    return _base_universe_d2(vrg_basefill_073, 73)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_073_vrg_basefill_073'] = {'inputs': ['vrg_basefill_073'], 'func': vrg_base_universe_d2_073_vrg_basefill_073}


def vrg_base_universe_d2_074_vrg_basefill_074(vrg_basefill_074):
    return _base_universe_d2(vrg_basefill_074, 74)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_074_vrg_basefill_074'] = {'inputs': ['vrg_basefill_074'], 'func': vrg_base_universe_d2_074_vrg_basefill_074}


def vrg_base_universe_d2_075_vrg_basefill_075(vrg_basefill_075):
    return _base_universe_d2(vrg_basefill_075, 75)
VRG_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vrg_base_universe_d2_075_vrg_basefill_075'] = {'inputs': ['vrg_basefill_075'], 'func': vrg_base_universe_d2_075_vrg_basefill_075}
