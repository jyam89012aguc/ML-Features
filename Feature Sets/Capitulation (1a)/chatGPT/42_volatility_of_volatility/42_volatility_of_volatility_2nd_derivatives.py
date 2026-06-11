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



def vov_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def vov_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def vov_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def vov_154_vov_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def vov_155_vov_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLATILITY_OF_VOLATILITY_REGISTRY_2ND_DERIVATIVES = {
    'vov_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': vov_001_realized_vol_z_roc_1},
    'vov_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': vov_007_realized_vol_z_roc_5},
    'vov_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': vov_013_realized_vol_z_roc_42},
    'vov_154_vov_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': vov_154_vov_019_realized_vol_z_42_019_roc_126},
    'vov_155_vov_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': vov_155_vov_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vov_replacement_d2_001(vov_replacement_001):
    feature = _clean(vov_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_001'] = {'inputs': ['vov_replacement_001'], 'func': vov_replacement_d2_001}


def vov_replacement_d2_002(vov_replacement_002):
    feature = _clean(vov_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_002'] = {'inputs': ['vov_replacement_002'], 'func': vov_replacement_d2_002}


def vov_replacement_d2_003(vov_replacement_003):
    feature = _clean(vov_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_003'] = {'inputs': ['vov_replacement_003'], 'func': vov_replacement_d2_003}


def vov_replacement_d2_004(vov_replacement_004):
    feature = _clean(vov_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_004'] = {'inputs': ['vov_replacement_004'], 'func': vov_replacement_d2_004}


def vov_replacement_d2_005(vov_replacement_005):
    feature = _clean(vov_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_005'] = {'inputs': ['vov_replacement_005'], 'func': vov_replacement_d2_005}


def vov_replacement_d2_006(vov_replacement_006):
    feature = _clean(vov_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_006'] = {'inputs': ['vov_replacement_006'], 'func': vov_replacement_d2_006}


def vov_replacement_d2_007(vov_replacement_007):
    feature = _clean(vov_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_007'] = {'inputs': ['vov_replacement_007'], 'func': vov_replacement_d2_007}


def vov_replacement_d2_008(vov_replacement_008):
    feature = _clean(vov_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_008'] = {'inputs': ['vov_replacement_008'], 'func': vov_replacement_d2_008}


def vov_replacement_d2_009(vov_replacement_009):
    feature = _clean(vov_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_009'] = {'inputs': ['vov_replacement_009'], 'func': vov_replacement_d2_009}


def vov_replacement_d2_010(vov_replacement_010):
    feature = _clean(vov_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_010'] = {'inputs': ['vov_replacement_010'], 'func': vov_replacement_d2_010}


def vov_replacement_d2_011(vov_replacement_011):
    feature = _clean(vov_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_011'] = {'inputs': ['vov_replacement_011'], 'func': vov_replacement_d2_011}


def vov_replacement_d2_012(vov_replacement_012):
    feature = _clean(vov_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_012'] = {'inputs': ['vov_replacement_012'], 'func': vov_replacement_d2_012}


def vov_replacement_d2_013(vov_replacement_013):
    feature = _clean(vov_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_013'] = {'inputs': ['vov_replacement_013'], 'func': vov_replacement_d2_013}


def vov_replacement_d2_014(vov_replacement_014):
    feature = _clean(vov_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_014'] = {'inputs': ['vov_replacement_014'], 'func': vov_replacement_d2_014}


def vov_replacement_d2_015(vov_replacement_015):
    feature = _clean(vov_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_015'] = {'inputs': ['vov_replacement_015'], 'func': vov_replacement_d2_015}


def vov_replacement_d2_016(vov_replacement_016):
    feature = _clean(vov_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_016'] = {'inputs': ['vov_replacement_016'], 'func': vov_replacement_d2_016}


def vov_replacement_d2_017(vov_replacement_017):
    feature = _clean(vov_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_017'] = {'inputs': ['vov_replacement_017'], 'func': vov_replacement_d2_017}


def vov_replacement_d2_018(vov_replacement_018):
    feature = _clean(vov_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_018'] = {'inputs': ['vov_replacement_018'], 'func': vov_replacement_d2_018}


def vov_replacement_d2_019(vov_replacement_019):
    feature = _clean(vov_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_019'] = {'inputs': ['vov_replacement_019'], 'func': vov_replacement_d2_019}


def vov_replacement_d2_020(vov_replacement_020):
    feature = _clean(vov_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_020'] = {'inputs': ['vov_replacement_020'], 'func': vov_replacement_d2_020}


def vov_replacement_d2_021(vov_replacement_021):
    feature = _clean(vov_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_021'] = {'inputs': ['vov_replacement_021'], 'func': vov_replacement_d2_021}


def vov_replacement_d2_022(vov_replacement_022):
    feature = _clean(vov_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_022'] = {'inputs': ['vov_replacement_022'], 'func': vov_replacement_d2_022}


def vov_replacement_d2_023(vov_replacement_023):
    feature = _clean(vov_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_023'] = {'inputs': ['vov_replacement_023'], 'func': vov_replacement_d2_023}


def vov_replacement_d2_024(vov_replacement_024):
    feature = _clean(vov_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_024'] = {'inputs': ['vov_replacement_024'], 'func': vov_replacement_d2_024}


def vov_replacement_d2_025(vov_replacement_025):
    feature = _clean(vov_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_025'] = {'inputs': ['vov_replacement_025'], 'func': vov_replacement_d2_025}


def vov_replacement_d2_026(vov_replacement_026):
    feature = _clean(vov_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_026'] = {'inputs': ['vov_replacement_026'], 'func': vov_replacement_d2_026}


def vov_replacement_d2_027(vov_replacement_027):
    feature = _clean(vov_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_027'] = {'inputs': ['vov_replacement_027'], 'func': vov_replacement_d2_027}


def vov_replacement_d2_028(vov_replacement_028):
    feature = _clean(vov_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_028'] = {'inputs': ['vov_replacement_028'], 'func': vov_replacement_d2_028}


def vov_replacement_d2_029(vov_replacement_029):
    feature = _clean(vov_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_029'] = {'inputs': ['vov_replacement_029'], 'func': vov_replacement_d2_029}


def vov_replacement_d2_030(vov_replacement_030):
    feature = _clean(vov_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_030'] = {'inputs': ['vov_replacement_030'], 'func': vov_replacement_d2_030}


def vov_replacement_d2_031(vov_replacement_031):
    feature = _clean(vov_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_031'] = {'inputs': ['vov_replacement_031'], 'func': vov_replacement_d2_031}


def vov_replacement_d2_032(vov_replacement_032):
    feature = _clean(vov_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_032'] = {'inputs': ['vov_replacement_032'], 'func': vov_replacement_d2_032}


def vov_replacement_d2_033(vov_replacement_033):
    feature = _clean(vov_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_033'] = {'inputs': ['vov_replacement_033'], 'func': vov_replacement_d2_033}


def vov_replacement_d2_034(vov_replacement_034):
    feature = _clean(vov_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_034'] = {'inputs': ['vov_replacement_034'], 'func': vov_replacement_d2_034}


def vov_replacement_d2_035(vov_replacement_035):
    feature = _clean(vov_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_035'] = {'inputs': ['vov_replacement_035'], 'func': vov_replacement_d2_035}


def vov_replacement_d2_036(vov_replacement_036):
    feature = _clean(vov_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_036'] = {'inputs': ['vov_replacement_036'], 'func': vov_replacement_d2_036}


def vov_replacement_d2_037(vov_replacement_037):
    feature = _clean(vov_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_037'] = {'inputs': ['vov_replacement_037'], 'func': vov_replacement_d2_037}


def vov_replacement_d2_038(vov_replacement_038):
    feature = _clean(vov_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_038'] = {'inputs': ['vov_replacement_038'], 'func': vov_replacement_d2_038}


def vov_replacement_d2_039(vov_replacement_039):
    feature = _clean(vov_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_039'] = {'inputs': ['vov_replacement_039'], 'func': vov_replacement_d2_039}


def vov_replacement_d2_040(vov_replacement_040):
    feature = _clean(vov_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_040'] = {'inputs': ['vov_replacement_040'], 'func': vov_replacement_d2_040}


def vov_replacement_d2_041(vov_replacement_041):
    feature = _clean(vov_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_041'] = {'inputs': ['vov_replacement_041'], 'func': vov_replacement_d2_041}


def vov_replacement_d2_042(vov_replacement_042):
    feature = _clean(vov_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_042'] = {'inputs': ['vov_replacement_042'], 'func': vov_replacement_d2_042}


def vov_replacement_d2_043(vov_replacement_043):
    feature = _clean(vov_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_043'] = {'inputs': ['vov_replacement_043'], 'func': vov_replacement_d2_043}


def vov_replacement_d2_044(vov_replacement_044):
    feature = _clean(vov_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_044'] = {'inputs': ['vov_replacement_044'], 'func': vov_replacement_d2_044}


def vov_replacement_d2_045(vov_replacement_045):
    feature = _clean(vov_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_045'] = {'inputs': ['vov_replacement_045'], 'func': vov_replacement_d2_045}


def vov_replacement_d2_046(vov_replacement_046):
    feature = _clean(vov_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_046'] = {'inputs': ['vov_replacement_046'], 'func': vov_replacement_d2_046}


def vov_replacement_d2_047(vov_replacement_047):
    feature = _clean(vov_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_047'] = {'inputs': ['vov_replacement_047'], 'func': vov_replacement_d2_047}


def vov_replacement_d2_048(vov_replacement_048):
    feature = _clean(vov_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_048'] = {'inputs': ['vov_replacement_048'], 'func': vov_replacement_d2_048}


def vov_replacement_d2_049(vov_replacement_049):
    feature = _clean(vov_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_049'] = {'inputs': ['vov_replacement_049'], 'func': vov_replacement_d2_049}


def vov_replacement_d2_050(vov_replacement_050):
    feature = _clean(vov_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_050'] = {'inputs': ['vov_replacement_050'], 'func': vov_replacement_d2_050}


def vov_replacement_d2_051(vov_replacement_051):
    feature = _clean(vov_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_051'] = {'inputs': ['vov_replacement_051'], 'func': vov_replacement_d2_051}


def vov_replacement_d2_052(vov_replacement_052):
    feature = _clean(vov_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_052'] = {'inputs': ['vov_replacement_052'], 'func': vov_replacement_d2_052}


def vov_replacement_d2_053(vov_replacement_053):
    feature = _clean(vov_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_053'] = {'inputs': ['vov_replacement_053'], 'func': vov_replacement_d2_053}


def vov_replacement_d2_054(vov_replacement_054):
    feature = _clean(vov_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_054'] = {'inputs': ['vov_replacement_054'], 'func': vov_replacement_d2_054}


def vov_replacement_d2_055(vov_replacement_055):
    feature = _clean(vov_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_055'] = {'inputs': ['vov_replacement_055'], 'func': vov_replacement_d2_055}


def vov_replacement_d2_056(vov_replacement_056):
    feature = _clean(vov_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_056'] = {'inputs': ['vov_replacement_056'], 'func': vov_replacement_d2_056}


def vov_replacement_d2_057(vov_replacement_057):
    feature = _clean(vov_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_057'] = {'inputs': ['vov_replacement_057'], 'func': vov_replacement_d2_057}


def vov_replacement_d2_058(vov_replacement_058):
    feature = _clean(vov_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_058'] = {'inputs': ['vov_replacement_058'], 'func': vov_replacement_d2_058}


def vov_replacement_d2_059(vov_replacement_059):
    feature = _clean(vov_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_059'] = {'inputs': ['vov_replacement_059'], 'func': vov_replacement_d2_059}


def vov_replacement_d2_060(vov_replacement_060):
    feature = _clean(vov_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_060'] = {'inputs': ['vov_replacement_060'], 'func': vov_replacement_d2_060}


def vov_replacement_d2_061(vov_replacement_061):
    feature = _clean(vov_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_061'] = {'inputs': ['vov_replacement_061'], 'func': vov_replacement_d2_061}


def vov_replacement_d2_062(vov_replacement_062):
    feature = _clean(vov_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_062'] = {'inputs': ['vov_replacement_062'], 'func': vov_replacement_d2_062}


def vov_replacement_d2_063(vov_replacement_063):
    feature = _clean(vov_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_063'] = {'inputs': ['vov_replacement_063'], 'func': vov_replacement_d2_063}


def vov_replacement_d2_064(vov_replacement_064):
    feature = _clean(vov_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_064'] = {'inputs': ['vov_replacement_064'], 'func': vov_replacement_d2_064}


def vov_replacement_d2_065(vov_replacement_065):
    feature = _clean(vov_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_065'] = {'inputs': ['vov_replacement_065'], 'func': vov_replacement_d2_065}


def vov_replacement_d2_066(vov_replacement_066):
    feature = _clean(vov_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_066'] = {'inputs': ['vov_replacement_066'], 'func': vov_replacement_d2_066}


def vov_replacement_d2_067(vov_replacement_067):
    feature = _clean(vov_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_067'] = {'inputs': ['vov_replacement_067'], 'func': vov_replacement_d2_067}


def vov_replacement_d2_068(vov_replacement_068):
    feature = _clean(vov_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_068'] = {'inputs': ['vov_replacement_068'], 'func': vov_replacement_d2_068}


def vov_replacement_d2_069(vov_replacement_069):
    feature = _clean(vov_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_069'] = {'inputs': ['vov_replacement_069'], 'func': vov_replacement_d2_069}


def vov_replacement_d2_070(vov_replacement_070):
    feature = _clean(vov_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_070'] = {'inputs': ['vov_replacement_070'], 'func': vov_replacement_d2_070}


def vov_replacement_d2_071(vov_replacement_071):
    feature = _clean(vov_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_071'] = {'inputs': ['vov_replacement_071'], 'func': vov_replacement_d2_071}


def vov_replacement_d2_072(vov_replacement_072):
    feature = _clean(vov_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_072'] = {'inputs': ['vov_replacement_072'], 'func': vov_replacement_d2_072}


def vov_replacement_d2_073(vov_replacement_073):
    feature = _clean(vov_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_073'] = {'inputs': ['vov_replacement_073'], 'func': vov_replacement_d2_073}


def vov_replacement_d2_074(vov_replacement_074):
    feature = _clean(vov_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_074'] = {'inputs': ['vov_replacement_074'], 'func': vov_replacement_d2_074}


def vov_replacement_d2_075(vov_replacement_075):
    feature = _clean(vov_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_075'] = {'inputs': ['vov_replacement_075'], 'func': vov_replacement_d2_075}


def vov_replacement_d2_076(vov_replacement_076):
    feature = _clean(vov_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_076'] = {'inputs': ['vov_replacement_076'], 'func': vov_replacement_d2_076}


def vov_replacement_d2_077(vov_replacement_077):
    feature = _clean(vov_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_077'] = {'inputs': ['vov_replacement_077'], 'func': vov_replacement_d2_077}


def vov_replacement_d2_078(vov_replacement_078):
    feature = _clean(vov_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_078'] = {'inputs': ['vov_replacement_078'], 'func': vov_replacement_d2_078}


def vov_replacement_d2_079(vov_replacement_079):
    feature = _clean(vov_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_079'] = {'inputs': ['vov_replacement_079'], 'func': vov_replacement_d2_079}


def vov_replacement_d2_080(vov_replacement_080):
    feature = _clean(vov_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_080'] = {'inputs': ['vov_replacement_080'], 'func': vov_replacement_d2_080}


def vov_replacement_d2_081(vov_replacement_081):
    feature = _clean(vov_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_081'] = {'inputs': ['vov_replacement_081'], 'func': vov_replacement_d2_081}


def vov_replacement_d2_082(vov_replacement_082):
    feature = _clean(vov_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_082'] = {'inputs': ['vov_replacement_082'], 'func': vov_replacement_d2_082}


def vov_replacement_d2_083(vov_replacement_083):
    feature = _clean(vov_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_083'] = {'inputs': ['vov_replacement_083'], 'func': vov_replacement_d2_083}


def vov_replacement_d2_084(vov_replacement_084):
    feature = _clean(vov_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_084'] = {'inputs': ['vov_replacement_084'], 'func': vov_replacement_d2_084}


def vov_replacement_d2_085(vov_replacement_085):
    feature = _clean(vov_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_085'] = {'inputs': ['vov_replacement_085'], 'func': vov_replacement_d2_085}


def vov_replacement_d2_086(vov_replacement_086):
    feature = _clean(vov_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_086'] = {'inputs': ['vov_replacement_086'], 'func': vov_replacement_d2_086}


def vov_replacement_d2_087(vov_replacement_087):
    feature = _clean(vov_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_087'] = {'inputs': ['vov_replacement_087'], 'func': vov_replacement_d2_087}


def vov_replacement_d2_088(vov_replacement_088):
    feature = _clean(vov_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_088'] = {'inputs': ['vov_replacement_088'], 'func': vov_replacement_d2_088}


def vov_replacement_d2_089(vov_replacement_089):
    feature = _clean(vov_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_089'] = {'inputs': ['vov_replacement_089'], 'func': vov_replacement_d2_089}


def vov_replacement_d2_090(vov_replacement_090):
    feature = _clean(vov_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_090'] = {'inputs': ['vov_replacement_090'], 'func': vov_replacement_d2_090}


def vov_replacement_d2_091(vov_replacement_091):
    feature = _clean(vov_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_091'] = {'inputs': ['vov_replacement_091'], 'func': vov_replacement_d2_091}


def vov_replacement_d2_092(vov_replacement_092):
    feature = _clean(vov_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_092'] = {'inputs': ['vov_replacement_092'], 'func': vov_replacement_d2_092}


def vov_replacement_d2_093(vov_replacement_093):
    feature = _clean(vov_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_093'] = {'inputs': ['vov_replacement_093'], 'func': vov_replacement_d2_093}


def vov_replacement_d2_094(vov_replacement_094):
    feature = _clean(vov_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_094'] = {'inputs': ['vov_replacement_094'], 'func': vov_replacement_d2_094}


def vov_replacement_d2_095(vov_replacement_095):
    feature = _clean(vov_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_095'] = {'inputs': ['vov_replacement_095'], 'func': vov_replacement_d2_095}


def vov_replacement_d2_096(vov_replacement_096):
    feature = _clean(vov_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_096'] = {'inputs': ['vov_replacement_096'], 'func': vov_replacement_d2_096}


def vov_replacement_d2_097(vov_replacement_097):
    feature = _clean(vov_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_097'] = {'inputs': ['vov_replacement_097'], 'func': vov_replacement_d2_097}


def vov_replacement_d2_098(vov_replacement_098):
    feature = _clean(vov_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_098'] = {'inputs': ['vov_replacement_098'], 'func': vov_replacement_d2_098}


def vov_replacement_d2_099(vov_replacement_099):
    feature = _clean(vov_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_099'] = {'inputs': ['vov_replacement_099'], 'func': vov_replacement_d2_099}


def vov_replacement_d2_100(vov_replacement_100):
    feature = _clean(vov_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_100'] = {'inputs': ['vov_replacement_100'], 'func': vov_replacement_d2_100}


def vov_replacement_d2_101(vov_replacement_101):
    feature = _clean(vov_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_101'] = {'inputs': ['vov_replacement_101'], 'func': vov_replacement_d2_101}


def vov_replacement_d2_102(vov_replacement_102):
    feature = _clean(vov_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_102'] = {'inputs': ['vov_replacement_102'], 'func': vov_replacement_d2_102}


def vov_replacement_d2_103(vov_replacement_103):
    feature = _clean(vov_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_103'] = {'inputs': ['vov_replacement_103'], 'func': vov_replacement_d2_103}


def vov_replacement_d2_104(vov_replacement_104):
    feature = _clean(vov_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_104'] = {'inputs': ['vov_replacement_104'], 'func': vov_replacement_d2_104}


def vov_replacement_d2_105(vov_replacement_105):
    feature = _clean(vov_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_105'] = {'inputs': ['vov_replacement_105'], 'func': vov_replacement_d2_105}


def vov_replacement_d2_106(vov_replacement_106):
    feature = _clean(vov_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_106'] = {'inputs': ['vov_replacement_106'], 'func': vov_replacement_d2_106}


def vov_replacement_d2_107(vov_replacement_107):
    feature = _clean(vov_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_107'] = {'inputs': ['vov_replacement_107'], 'func': vov_replacement_d2_107}


def vov_replacement_d2_108(vov_replacement_108):
    feature = _clean(vov_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_108'] = {'inputs': ['vov_replacement_108'], 'func': vov_replacement_d2_108}


def vov_replacement_d2_109(vov_replacement_109):
    feature = _clean(vov_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_109'] = {'inputs': ['vov_replacement_109'], 'func': vov_replacement_d2_109}


def vov_replacement_d2_110(vov_replacement_110):
    feature = _clean(vov_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_110'] = {'inputs': ['vov_replacement_110'], 'func': vov_replacement_d2_110}


def vov_replacement_d2_111(vov_replacement_111):
    feature = _clean(vov_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_111'] = {'inputs': ['vov_replacement_111'], 'func': vov_replacement_d2_111}


def vov_replacement_d2_112(vov_replacement_112):
    feature = _clean(vov_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_112'] = {'inputs': ['vov_replacement_112'], 'func': vov_replacement_d2_112}


def vov_replacement_d2_113(vov_replacement_113):
    feature = _clean(vov_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_113'] = {'inputs': ['vov_replacement_113'], 'func': vov_replacement_d2_113}


def vov_replacement_d2_114(vov_replacement_114):
    feature = _clean(vov_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_114'] = {'inputs': ['vov_replacement_114'], 'func': vov_replacement_d2_114}


def vov_replacement_d2_115(vov_replacement_115):
    feature = _clean(vov_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_115'] = {'inputs': ['vov_replacement_115'], 'func': vov_replacement_d2_115}


def vov_replacement_d2_116(vov_replacement_116):
    feature = _clean(vov_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_116'] = {'inputs': ['vov_replacement_116'], 'func': vov_replacement_d2_116}


def vov_replacement_d2_117(vov_replacement_117):
    feature = _clean(vov_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_117'] = {'inputs': ['vov_replacement_117'], 'func': vov_replacement_d2_117}


def vov_replacement_d2_118(vov_replacement_118):
    feature = _clean(vov_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_118'] = {'inputs': ['vov_replacement_118'], 'func': vov_replacement_d2_118}


def vov_replacement_d2_119(vov_replacement_119):
    feature = _clean(vov_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_119'] = {'inputs': ['vov_replacement_119'], 'func': vov_replacement_d2_119}


def vov_replacement_d2_120(vov_replacement_120):
    feature = _clean(vov_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_120'] = {'inputs': ['vov_replacement_120'], 'func': vov_replacement_d2_120}


def vov_replacement_d2_121(vov_replacement_121):
    feature = _clean(vov_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_121'] = {'inputs': ['vov_replacement_121'], 'func': vov_replacement_d2_121}


def vov_replacement_d2_122(vov_replacement_122):
    feature = _clean(vov_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_122'] = {'inputs': ['vov_replacement_122'], 'func': vov_replacement_d2_122}


def vov_replacement_d2_123(vov_replacement_123):
    feature = _clean(vov_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_123'] = {'inputs': ['vov_replacement_123'], 'func': vov_replacement_d2_123}


def vov_replacement_d2_124(vov_replacement_124):
    feature = _clean(vov_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_124'] = {'inputs': ['vov_replacement_124'], 'func': vov_replacement_d2_124}


def vov_replacement_d2_125(vov_replacement_125):
    feature = _clean(vov_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_125'] = {'inputs': ['vov_replacement_125'], 'func': vov_replacement_d2_125}


def vov_replacement_d2_126(vov_replacement_126):
    feature = _clean(vov_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_126'] = {'inputs': ['vov_replacement_126'], 'func': vov_replacement_d2_126}


def vov_replacement_d2_127(vov_replacement_127):
    feature = _clean(vov_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_127'] = {'inputs': ['vov_replacement_127'], 'func': vov_replacement_d2_127}


def vov_replacement_d2_128(vov_replacement_128):
    feature = _clean(vov_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_128'] = {'inputs': ['vov_replacement_128'], 'func': vov_replacement_d2_128}


def vov_replacement_d2_129(vov_replacement_129):
    feature = _clean(vov_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_129'] = {'inputs': ['vov_replacement_129'], 'func': vov_replacement_d2_129}


def vov_replacement_d2_130(vov_replacement_130):
    feature = _clean(vov_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_130'] = {'inputs': ['vov_replacement_130'], 'func': vov_replacement_d2_130}


def vov_replacement_d2_131(vov_replacement_131):
    feature = _clean(vov_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_131'] = {'inputs': ['vov_replacement_131'], 'func': vov_replacement_d2_131}


def vov_replacement_d2_132(vov_replacement_132):
    feature = _clean(vov_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_132'] = {'inputs': ['vov_replacement_132'], 'func': vov_replacement_d2_132}


def vov_replacement_d2_133(vov_replacement_133):
    feature = _clean(vov_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_133'] = {'inputs': ['vov_replacement_133'], 'func': vov_replacement_d2_133}


def vov_replacement_d2_134(vov_replacement_134):
    feature = _clean(vov_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_134'] = {'inputs': ['vov_replacement_134'], 'func': vov_replacement_d2_134}


def vov_replacement_d2_135(vov_replacement_135):
    feature = _clean(vov_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_135'] = {'inputs': ['vov_replacement_135'], 'func': vov_replacement_d2_135}


def vov_replacement_d2_136(vov_replacement_136):
    feature = _clean(vov_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_136'] = {'inputs': ['vov_replacement_136'], 'func': vov_replacement_d2_136}


def vov_replacement_d2_137(vov_replacement_137):
    feature = _clean(vov_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_137'] = {'inputs': ['vov_replacement_137'], 'func': vov_replacement_d2_137}


def vov_replacement_d2_138(vov_replacement_138):
    feature = _clean(vov_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_138'] = {'inputs': ['vov_replacement_138'], 'func': vov_replacement_d2_138}


def vov_replacement_d2_139(vov_replacement_139):
    feature = _clean(vov_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_139'] = {'inputs': ['vov_replacement_139'], 'func': vov_replacement_d2_139}


def vov_replacement_d2_140(vov_replacement_140):
    feature = _clean(vov_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_140'] = {'inputs': ['vov_replacement_140'], 'func': vov_replacement_d2_140}


def vov_replacement_d2_141(vov_replacement_141):
    feature = _clean(vov_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_141'] = {'inputs': ['vov_replacement_141'], 'func': vov_replacement_d2_141}


def vov_replacement_d2_142(vov_replacement_142):
    feature = _clean(vov_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_142'] = {'inputs': ['vov_replacement_142'], 'func': vov_replacement_d2_142}


def vov_replacement_d2_143(vov_replacement_143):
    feature = _clean(vov_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_143'] = {'inputs': ['vov_replacement_143'], 'func': vov_replacement_d2_143}


def vov_replacement_d2_144(vov_replacement_144):
    feature = _clean(vov_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_144'] = {'inputs': ['vov_replacement_144'], 'func': vov_replacement_d2_144}


def vov_replacement_d2_145(vov_replacement_145):
    feature = _clean(vov_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_145'] = {'inputs': ['vov_replacement_145'], 'func': vov_replacement_d2_145}


def vov_replacement_d2_146(vov_replacement_146):
    feature = _clean(vov_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_146'] = {'inputs': ['vov_replacement_146'], 'func': vov_replacement_d2_146}


def vov_replacement_d2_147(vov_replacement_147):
    feature = _clean(vov_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_147'] = {'inputs': ['vov_replacement_147'], 'func': vov_replacement_d2_147}


def vov_replacement_d2_148(vov_replacement_148):
    feature = _clean(vov_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_148'] = {'inputs': ['vov_replacement_148'], 'func': vov_replacement_d2_148}


def vov_replacement_d2_149(vov_replacement_149):
    feature = _clean(vov_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_149'] = {'inputs': ['vov_replacement_149'], 'func': vov_replacement_d2_149}


def vov_replacement_d2_150(vov_replacement_150):
    feature = _clean(vov_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_150'] = {'inputs': ['vov_replacement_150'], 'func': vov_replacement_d2_150}


def vov_replacement_d2_151(vov_replacement_151):
    feature = _clean(vov_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_151'] = {'inputs': ['vov_replacement_151'], 'func': vov_replacement_d2_151}


def vov_replacement_d2_152(vov_replacement_152):
    feature = _clean(vov_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_152'] = {'inputs': ['vov_replacement_152'], 'func': vov_replacement_d2_152}


def vov_replacement_d2_153(vov_replacement_153):
    feature = _clean(vov_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_153'] = {'inputs': ['vov_replacement_153'], 'func': vov_replacement_d2_153}


def vov_replacement_d2_154(vov_replacement_154):
    feature = _clean(vov_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_154'] = {'inputs': ['vov_replacement_154'], 'func': vov_replacement_d2_154}


def vov_replacement_d2_155(vov_replacement_155):
    feature = _clean(vov_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_155'] = {'inputs': ['vov_replacement_155'], 'func': vov_replacement_d2_155}


def vov_replacement_d2_156(vov_replacement_156):
    feature = _clean(vov_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_156'] = {'inputs': ['vov_replacement_156'], 'func': vov_replacement_d2_156}


def vov_replacement_d2_157(vov_replacement_157):
    feature = _clean(vov_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_157'] = {'inputs': ['vov_replacement_157'], 'func': vov_replacement_d2_157}


def vov_replacement_d2_158(vov_replacement_158):
    feature = _clean(vov_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_158'] = {'inputs': ['vov_replacement_158'], 'func': vov_replacement_d2_158}


def vov_replacement_d2_159(vov_replacement_159):
    feature = _clean(vov_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_159'] = {'inputs': ['vov_replacement_159'], 'func': vov_replacement_d2_159}


def vov_replacement_d2_160(vov_replacement_160):
    feature = _clean(vov_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_160'] = {'inputs': ['vov_replacement_160'], 'func': vov_replacement_d2_160}


def vov_replacement_d2_161(vov_replacement_161):
    feature = _clean(vov_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_161'] = {'inputs': ['vov_replacement_161'], 'func': vov_replacement_d2_161}


def vov_replacement_d2_162(vov_replacement_162):
    feature = _clean(vov_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_162'] = {'inputs': ['vov_replacement_162'], 'func': vov_replacement_d2_162}


def vov_replacement_d2_163(vov_replacement_163):
    feature = _clean(vov_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_163'] = {'inputs': ['vov_replacement_163'], 'func': vov_replacement_d2_163}


def vov_replacement_d2_164(vov_replacement_164):
    feature = _clean(vov_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_164'] = {'inputs': ['vov_replacement_164'], 'func': vov_replacement_d2_164}


def vov_replacement_d2_165(vov_replacement_165):
    feature = _clean(vov_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_165'] = {'inputs': ['vov_replacement_165'], 'func': vov_replacement_d2_165}


def vov_replacement_d2_166(vov_replacement_166):
    feature = _clean(vov_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_166'] = {'inputs': ['vov_replacement_166'], 'func': vov_replacement_d2_166}


def vov_replacement_d2_167(vov_replacement_167):
    feature = _clean(vov_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_167'] = {'inputs': ['vov_replacement_167'], 'func': vov_replacement_d2_167}


def vov_replacement_d2_168(vov_replacement_168):
    feature = _clean(vov_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_168'] = {'inputs': ['vov_replacement_168'], 'func': vov_replacement_d2_168}


def vov_replacement_d2_169(vov_replacement_169):
    feature = _clean(vov_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_169'] = {'inputs': ['vov_replacement_169'], 'func': vov_replacement_d2_169}


def vov_replacement_d2_170(vov_replacement_170):
    feature = _clean(vov_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_170'] = {'inputs': ['vov_replacement_170'], 'func': vov_replacement_d2_170}


def vov_replacement_d2_171(vov_replacement_171):
    feature = _clean(vov_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_171'] = {'inputs': ['vov_replacement_171'], 'func': vov_replacement_d2_171}


def vov_replacement_d2_172(vov_replacement_172):
    feature = _clean(vov_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_172'] = {'inputs': ['vov_replacement_172'], 'func': vov_replacement_d2_172}


def vov_replacement_d2_173(vov_replacement_173):
    feature = _clean(vov_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_173'] = {'inputs': ['vov_replacement_173'], 'func': vov_replacement_d2_173}


def vov_replacement_d2_174(vov_replacement_174):
    feature = _clean(vov_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_174'] = {'inputs': ['vov_replacement_174'], 'func': vov_replacement_d2_174}


def vov_replacement_d2_175(vov_replacement_175):
    feature = _clean(vov_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
VOV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vov_replacement_d2_175'] = {'inputs': ['vov_replacement_175'], 'func': vov_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vov_base_universe_d2_001_vov_002_range_expansion_10_002(vov_002_range_expansion_10_002):
    return _base_universe_d2(vov_002_range_expansion_10_002, 1)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_001_vov_002_range_expansion_10_002'] = {'inputs': ['vov_002_range_expansion_10_002'], 'func': vov_base_universe_d2_001_vov_002_range_expansion_10_002}


def vov_base_universe_d2_002_vov_004_close_location_42_004(vov_004_close_location_42_004):
    return _base_universe_d2(vov_004_close_location_42_004, 2)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_002_vov_004_close_location_42_004'] = {'inputs': ['vov_004_close_location_42_004'], 'func': vov_base_universe_d2_002_vov_004_close_location_42_004}


def vov_base_universe_d2_003_vov_005_atr_move_63_005(vov_005_atr_move_63_005):
    return _base_universe_d2(vov_005_atr_move_63_005, 3)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_003_vov_005_atr_move_63_005'] = {'inputs': ['vov_005_atr_move_63_005'], 'func': vov_base_universe_d2_003_vov_005_atr_move_63_005}


def vov_base_universe_d2_004_vov_008_range_expansion_189_008(vov_008_range_expansion_189_008):
    return _base_universe_d2(vov_008_range_expansion_189_008, 4)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_004_vov_008_range_expansion_189_008'] = {'inputs': ['vov_008_range_expansion_189_008'], 'func': vov_base_universe_d2_004_vov_008_range_expansion_189_008}


def vov_base_universe_d2_005_vov_010_close_location_378_010(vov_010_close_location_378_010):
    return _base_universe_d2(vov_010_close_location_378_010, 5)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_005_vov_010_close_location_378_010'] = {'inputs': ['vov_010_close_location_378_010'], 'func': vov_base_universe_d2_005_vov_010_close_location_378_010}


def vov_base_universe_d2_006_vov_011_atr_move_504_011(vov_011_atr_move_504_011):
    return _base_universe_d2(vov_011_atr_move_504_011, 6)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_006_vov_011_atr_move_504_011'] = {'inputs': ['vov_011_atr_move_504_011'], 'func': vov_base_universe_d2_006_vov_011_atr_move_504_011}


def vov_base_universe_d2_007_vov_014_range_expansion_1260_014(vov_014_range_expansion_1260_014):
    return _base_universe_d2(vov_014_range_expansion_1260_014, 7)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_007_vov_014_range_expansion_1260_014'] = {'inputs': ['vov_014_range_expansion_1260_014'], 'func': vov_base_universe_d2_007_vov_014_range_expansion_1260_014}


def vov_base_universe_d2_008_vov_016_close_location_5_016(vov_016_close_location_5_016):
    return _base_universe_d2(vov_016_close_location_5_016, 8)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_008_vov_016_close_location_5_016'] = {'inputs': ['vov_016_close_location_5_016'], 'func': vov_base_universe_d2_008_vov_016_close_location_5_016}


def vov_base_universe_d2_009_vov_017_atr_move_10_017(vov_017_atr_move_10_017):
    return _base_universe_d2(vov_017_atr_move_10_017, 9)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_009_vov_017_atr_move_10_017'] = {'inputs': ['vov_017_atr_move_10_017'], 'func': vov_base_universe_d2_009_vov_017_atr_move_10_017}


def vov_base_universe_d2_010_vov_020_range_expansion_63_020(vov_020_range_expansion_63_020):
    return _base_universe_d2(vov_020_range_expansion_63_020, 10)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_010_vov_020_range_expansion_63_020'] = {'inputs': ['vov_020_range_expansion_63_020'], 'func': vov_base_universe_d2_010_vov_020_range_expansion_63_020}


def vov_base_universe_d2_011_vov_022_close_location_126_022(vov_022_close_location_126_022):
    return _base_universe_d2(vov_022_close_location_126_022, 11)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_011_vov_022_close_location_126_022'] = {'inputs': ['vov_022_close_location_126_022'], 'func': vov_base_universe_d2_011_vov_022_close_location_126_022}


def vov_base_universe_d2_012_vov_023_atr_move_189_023(vov_023_atr_move_189_023):
    return _base_universe_d2(vov_023_atr_move_189_023, 12)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_012_vov_023_atr_move_189_023'] = {'inputs': ['vov_023_atr_move_189_023'], 'func': vov_base_universe_d2_012_vov_023_atr_move_189_023}


def vov_base_universe_d2_013_vov_026_range_expansion_504_026(vov_026_range_expansion_504_026):
    return _base_universe_d2(vov_026_range_expansion_504_026, 13)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_013_vov_026_range_expansion_504_026'] = {'inputs': ['vov_026_range_expansion_504_026'], 'func': vov_base_universe_d2_013_vov_026_range_expansion_504_026}


def vov_base_universe_d2_014_vov_028_close_location_1008_028(vov_028_close_location_1008_028):
    return _base_universe_d2(vov_028_close_location_1008_028, 14)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_014_vov_028_close_location_1008_028'] = {'inputs': ['vov_028_close_location_1008_028'], 'func': vov_base_universe_d2_014_vov_028_close_location_1008_028}


def vov_base_universe_d2_015_vov_029_atr_move_1260_029(vov_029_atr_move_1260_029):
    return _base_universe_d2(vov_029_atr_move_1260_029, 15)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_015_vov_029_atr_move_1260_029'] = {'inputs': ['vov_029_atr_move_1260_029'], 'func': vov_base_universe_d2_015_vov_029_atr_move_1260_029}


def vov_base_universe_d2_016_vov_basefill_001(vov_basefill_001):
    return _base_universe_d2(vov_basefill_001, 16)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_016_vov_basefill_001'] = {'inputs': ['vov_basefill_001'], 'func': vov_base_universe_d2_016_vov_basefill_001}


def vov_base_universe_d2_017_vov_basefill_003(vov_basefill_003):
    return _base_universe_d2(vov_basefill_003, 17)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_017_vov_basefill_003'] = {'inputs': ['vov_basefill_003'], 'func': vov_base_universe_d2_017_vov_basefill_003}


def vov_base_universe_d2_018_vov_basefill_006(vov_basefill_006):
    return _base_universe_d2(vov_basefill_006, 18)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_018_vov_basefill_006'] = {'inputs': ['vov_basefill_006'], 'func': vov_base_universe_d2_018_vov_basefill_006}


def vov_base_universe_d2_019_vov_basefill_007(vov_basefill_007):
    return _base_universe_d2(vov_basefill_007, 19)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_019_vov_basefill_007'] = {'inputs': ['vov_basefill_007'], 'func': vov_base_universe_d2_019_vov_basefill_007}


def vov_base_universe_d2_020_vov_basefill_009(vov_basefill_009):
    return _base_universe_d2(vov_basefill_009, 20)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_020_vov_basefill_009'] = {'inputs': ['vov_basefill_009'], 'func': vov_base_universe_d2_020_vov_basefill_009}


def vov_base_universe_d2_021_vov_basefill_012(vov_basefill_012):
    return _base_universe_d2(vov_basefill_012, 21)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_021_vov_basefill_012'] = {'inputs': ['vov_basefill_012'], 'func': vov_base_universe_d2_021_vov_basefill_012}


def vov_base_universe_d2_022_vov_basefill_013(vov_basefill_013):
    return _base_universe_d2(vov_basefill_013, 22)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_022_vov_basefill_013'] = {'inputs': ['vov_basefill_013'], 'func': vov_base_universe_d2_022_vov_basefill_013}


def vov_base_universe_d2_023_vov_basefill_015(vov_basefill_015):
    return _base_universe_d2(vov_basefill_015, 23)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_023_vov_basefill_015'] = {'inputs': ['vov_basefill_015'], 'func': vov_base_universe_d2_023_vov_basefill_015}


def vov_base_universe_d2_024_vov_basefill_018(vov_basefill_018):
    return _base_universe_d2(vov_basefill_018, 24)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_024_vov_basefill_018'] = {'inputs': ['vov_basefill_018'], 'func': vov_base_universe_d2_024_vov_basefill_018}


def vov_base_universe_d2_025_vov_basefill_019(vov_basefill_019):
    return _base_universe_d2(vov_basefill_019, 25)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_025_vov_basefill_019'] = {'inputs': ['vov_basefill_019'], 'func': vov_base_universe_d2_025_vov_basefill_019}


def vov_base_universe_d2_026_vov_basefill_021(vov_basefill_021):
    return _base_universe_d2(vov_basefill_021, 26)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_026_vov_basefill_021'] = {'inputs': ['vov_basefill_021'], 'func': vov_base_universe_d2_026_vov_basefill_021}


def vov_base_universe_d2_027_vov_basefill_024(vov_basefill_024):
    return _base_universe_d2(vov_basefill_024, 27)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_027_vov_basefill_024'] = {'inputs': ['vov_basefill_024'], 'func': vov_base_universe_d2_027_vov_basefill_024}


def vov_base_universe_d2_028_vov_basefill_025(vov_basefill_025):
    return _base_universe_d2(vov_basefill_025, 28)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_028_vov_basefill_025'] = {'inputs': ['vov_basefill_025'], 'func': vov_base_universe_d2_028_vov_basefill_025}


def vov_base_universe_d2_029_vov_basefill_027(vov_basefill_027):
    return _base_universe_d2(vov_basefill_027, 29)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_029_vov_basefill_027'] = {'inputs': ['vov_basefill_027'], 'func': vov_base_universe_d2_029_vov_basefill_027}


def vov_base_universe_d2_030_vov_basefill_030(vov_basefill_030):
    return _base_universe_d2(vov_basefill_030, 30)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_030_vov_basefill_030'] = {'inputs': ['vov_basefill_030'], 'func': vov_base_universe_d2_030_vov_basefill_030}


def vov_base_universe_d2_031_vov_basefill_031(vov_basefill_031):
    return _base_universe_d2(vov_basefill_031, 31)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_031_vov_basefill_031'] = {'inputs': ['vov_basefill_031'], 'func': vov_base_universe_d2_031_vov_basefill_031}


def vov_base_universe_d2_032_vov_basefill_032(vov_basefill_032):
    return _base_universe_d2(vov_basefill_032, 32)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_032_vov_basefill_032'] = {'inputs': ['vov_basefill_032'], 'func': vov_base_universe_d2_032_vov_basefill_032}


def vov_base_universe_d2_033_vov_basefill_033(vov_basefill_033):
    return _base_universe_d2(vov_basefill_033, 33)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_033_vov_basefill_033'] = {'inputs': ['vov_basefill_033'], 'func': vov_base_universe_d2_033_vov_basefill_033}


def vov_base_universe_d2_034_vov_basefill_034(vov_basefill_034):
    return _base_universe_d2(vov_basefill_034, 34)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_034_vov_basefill_034'] = {'inputs': ['vov_basefill_034'], 'func': vov_base_universe_d2_034_vov_basefill_034}


def vov_base_universe_d2_035_vov_basefill_035(vov_basefill_035):
    return _base_universe_d2(vov_basefill_035, 35)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_035_vov_basefill_035'] = {'inputs': ['vov_basefill_035'], 'func': vov_base_universe_d2_035_vov_basefill_035}


def vov_base_universe_d2_036_vov_basefill_036(vov_basefill_036):
    return _base_universe_d2(vov_basefill_036, 36)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_036_vov_basefill_036'] = {'inputs': ['vov_basefill_036'], 'func': vov_base_universe_d2_036_vov_basefill_036}


def vov_base_universe_d2_037_vov_basefill_037(vov_basefill_037):
    return _base_universe_d2(vov_basefill_037, 37)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_037_vov_basefill_037'] = {'inputs': ['vov_basefill_037'], 'func': vov_base_universe_d2_037_vov_basefill_037}


def vov_base_universe_d2_038_vov_basefill_038(vov_basefill_038):
    return _base_universe_d2(vov_basefill_038, 38)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_038_vov_basefill_038'] = {'inputs': ['vov_basefill_038'], 'func': vov_base_universe_d2_038_vov_basefill_038}


def vov_base_universe_d2_039_vov_basefill_039(vov_basefill_039):
    return _base_universe_d2(vov_basefill_039, 39)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_039_vov_basefill_039'] = {'inputs': ['vov_basefill_039'], 'func': vov_base_universe_d2_039_vov_basefill_039}


def vov_base_universe_d2_040_vov_basefill_040(vov_basefill_040):
    return _base_universe_d2(vov_basefill_040, 40)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_040_vov_basefill_040'] = {'inputs': ['vov_basefill_040'], 'func': vov_base_universe_d2_040_vov_basefill_040}


def vov_base_universe_d2_041_vov_basefill_041(vov_basefill_041):
    return _base_universe_d2(vov_basefill_041, 41)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_041_vov_basefill_041'] = {'inputs': ['vov_basefill_041'], 'func': vov_base_universe_d2_041_vov_basefill_041}


def vov_base_universe_d2_042_vov_basefill_042(vov_basefill_042):
    return _base_universe_d2(vov_basefill_042, 42)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_042_vov_basefill_042'] = {'inputs': ['vov_basefill_042'], 'func': vov_base_universe_d2_042_vov_basefill_042}


def vov_base_universe_d2_043_vov_basefill_043(vov_basefill_043):
    return _base_universe_d2(vov_basefill_043, 43)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_043_vov_basefill_043'] = {'inputs': ['vov_basefill_043'], 'func': vov_base_universe_d2_043_vov_basefill_043}


def vov_base_universe_d2_044_vov_basefill_044(vov_basefill_044):
    return _base_universe_d2(vov_basefill_044, 44)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_044_vov_basefill_044'] = {'inputs': ['vov_basefill_044'], 'func': vov_base_universe_d2_044_vov_basefill_044}


def vov_base_universe_d2_045_vov_basefill_045(vov_basefill_045):
    return _base_universe_d2(vov_basefill_045, 45)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_045_vov_basefill_045'] = {'inputs': ['vov_basefill_045'], 'func': vov_base_universe_d2_045_vov_basefill_045}


def vov_base_universe_d2_046_vov_basefill_046(vov_basefill_046):
    return _base_universe_d2(vov_basefill_046, 46)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_046_vov_basefill_046'] = {'inputs': ['vov_basefill_046'], 'func': vov_base_universe_d2_046_vov_basefill_046}


def vov_base_universe_d2_047_vov_basefill_047(vov_basefill_047):
    return _base_universe_d2(vov_basefill_047, 47)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_047_vov_basefill_047'] = {'inputs': ['vov_basefill_047'], 'func': vov_base_universe_d2_047_vov_basefill_047}


def vov_base_universe_d2_048_vov_basefill_048(vov_basefill_048):
    return _base_universe_d2(vov_basefill_048, 48)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_048_vov_basefill_048'] = {'inputs': ['vov_basefill_048'], 'func': vov_base_universe_d2_048_vov_basefill_048}


def vov_base_universe_d2_049_vov_basefill_049(vov_basefill_049):
    return _base_universe_d2(vov_basefill_049, 49)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_049_vov_basefill_049'] = {'inputs': ['vov_basefill_049'], 'func': vov_base_universe_d2_049_vov_basefill_049}


def vov_base_universe_d2_050_vov_basefill_050(vov_basefill_050):
    return _base_universe_d2(vov_basefill_050, 50)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_050_vov_basefill_050'] = {'inputs': ['vov_basefill_050'], 'func': vov_base_universe_d2_050_vov_basefill_050}


def vov_base_universe_d2_051_vov_basefill_051(vov_basefill_051):
    return _base_universe_d2(vov_basefill_051, 51)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_051_vov_basefill_051'] = {'inputs': ['vov_basefill_051'], 'func': vov_base_universe_d2_051_vov_basefill_051}


def vov_base_universe_d2_052_vov_basefill_052(vov_basefill_052):
    return _base_universe_d2(vov_basefill_052, 52)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_052_vov_basefill_052'] = {'inputs': ['vov_basefill_052'], 'func': vov_base_universe_d2_052_vov_basefill_052}


def vov_base_universe_d2_053_vov_basefill_053(vov_basefill_053):
    return _base_universe_d2(vov_basefill_053, 53)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_053_vov_basefill_053'] = {'inputs': ['vov_basefill_053'], 'func': vov_base_universe_d2_053_vov_basefill_053}


def vov_base_universe_d2_054_vov_basefill_054(vov_basefill_054):
    return _base_universe_d2(vov_basefill_054, 54)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_054_vov_basefill_054'] = {'inputs': ['vov_basefill_054'], 'func': vov_base_universe_d2_054_vov_basefill_054}


def vov_base_universe_d2_055_vov_basefill_055(vov_basefill_055):
    return _base_universe_d2(vov_basefill_055, 55)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_055_vov_basefill_055'] = {'inputs': ['vov_basefill_055'], 'func': vov_base_universe_d2_055_vov_basefill_055}


def vov_base_universe_d2_056_vov_basefill_056(vov_basefill_056):
    return _base_universe_d2(vov_basefill_056, 56)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_056_vov_basefill_056'] = {'inputs': ['vov_basefill_056'], 'func': vov_base_universe_d2_056_vov_basefill_056}


def vov_base_universe_d2_057_vov_basefill_057(vov_basefill_057):
    return _base_universe_d2(vov_basefill_057, 57)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_057_vov_basefill_057'] = {'inputs': ['vov_basefill_057'], 'func': vov_base_universe_d2_057_vov_basefill_057}


def vov_base_universe_d2_058_vov_basefill_058(vov_basefill_058):
    return _base_universe_d2(vov_basefill_058, 58)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_058_vov_basefill_058'] = {'inputs': ['vov_basefill_058'], 'func': vov_base_universe_d2_058_vov_basefill_058}


def vov_base_universe_d2_059_vov_basefill_059(vov_basefill_059):
    return _base_universe_d2(vov_basefill_059, 59)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_059_vov_basefill_059'] = {'inputs': ['vov_basefill_059'], 'func': vov_base_universe_d2_059_vov_basefill_059}


def vov_base_universe_d2_060_vov_basefill_060(vov_basefill_060):
    return _base_universe_d2(vov_basefill_060, 60)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_060_vov_basefill_060'] = {'inputs': ['vov_basefill_060'], 'func': vov_base_universe_d2_060_vov_basefill_060}


def vov_base_universe_d2_061_vov_basefill_061(vov_basefill_061):
    return _base_universe_d2(vov_basefill_061, 61)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_061_vov_basefill_061'] = {'inputs': ['vov_basefill_061'], 'func': vov_base_universe_d2_061_vov_basefill_061}


def vov_base_universe_d2_062_vov_basefill_062(vov_basefill_062):
    return _base_universe_d2(vov_basefill_062, 62)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_062_vov_basefill_062'] = {'inputs': ['vov_basefill_062'], 'func': vov_base_universe_d2_062_vov_basefill_062}


def vov_base_universe_d2_063_vov_basefill_063(vov_basefill_063):
    return _base_universe_d2(vov_basefill_063, 63)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_063_vov_basefill_063'] = {'inputs': ['vov_basefill_063'], 'func': vov_base_universe_d2_063_vov_basefill_063}


def vov_base_universe_d2_064_vov_basefill_064(vov_basefill_064):
    return _base_universe_d2(vov_basefill_064, 64)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_064_vov_basefill_064'] = {'inputs': ['vov_basefill_064'], 'func': vov_base_universe_d2_064_vov_basefill_064}


def vov_base_universe_d2_065_vov_basefill_065(vov_basefill_065):
    return _base_universe_d2(vov_basefill_065, 65)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_065_vov_basefill_065'] = {'inputs': ['vov_basefill_065'], 'func': vov_base_universe_d2_065_vov_basefill_065}


def vov_base_universe_d2_066_vov_basefill_066(vov_basefill_066):
    return _base_universe_d2(vov_basefill_066, 66)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_066_vov_basefill_066'] = {'inputs': ['vov_basefill_066'], 'func': vov_base_universe_d2_066_vov_basefill_066}


def vov_base_universe_d2_067_vov_basefill_067(vov_basefill_067):
    return _base_universe_d2(vov_basefill_067, 67)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_067_vov_basefill_067'] = {'inputs': ['vov_basefill_067'], 'func': vov_base_universe_d2_067_vov_basefill_067}


def vov_base_universe_d2_068_vov_basefill_068(vov_basefill_068):
    return _base_universe_d2(vov_basefill_068, 68)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_068_vov_basefill_068'] = {'inputs': ['vov_basefill_068'], 'func': vov_base_universe_d2_068_vov_basefill_068}


def vov_base_universe_d2_069_vov_basefill_069(vov_basefill_069):
    return _base_universe_d2(vov_basefill_069, 69)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_069_vov_basefill_069'] = {'inputs': ['vov_basefill_069'], 'func': vov_base_universe_d2_069_vov_basefill_069}


def vov_base_universe_d2_070_vov_basefill_070(vov_basefill_070):
    return _base_universe_d2(vov_basefill_070, 70)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_070_vov_basefill_070'] = {'inputs': ['vov_basefill_070'], 'func': vov_base_universe_d2_070_vov_basefill_070}


def vov_base_universe_d2_071_vov_basefill_071(vov_basefill_071):
    return _base_universe_d2(vov_basefill_071, 71)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_071_vov_basefill_071'] = {'inputs': ['vov_basefill_071'], 'func': vov_base_universe_d2_071_vov_basefill_071}


def vov_base_universe_d2_072_vov_basefill_072(vov_basefill_072):
    return _base_universe_d2(vov_basefill_072, 72)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_072_vov_basefill_072'] = {'inputs': ['vov_basefill_072'], 'func': vov_base_universe_d2_072_vov_basefill_072}


def vov_base_universe_d2_073_vov_basefill_073(vov_basefill_073):
    return _base_universe_d2(vov_basefill_073, 73)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_073_vov_basefill_073'] = {'inputs': ['vov_basefill_073'], 'func': vov_base_universe_d2_073_vov_basefill_073}


def vov_base_universe_d2_074_vov_basefill_074(vov_basefill_074):
    return _base_universe_d2(vov_basefill_074, 74)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_074_vov_basefill_074'] = {'inputs': ['vov_basefill_074'], 'func': vov_base_universe_d2_074_vov_basefill_074}


def vov_base_universe_d2_075_vov_basefill_075(vov_basefill_075):
    return _base_universe_d2(vov_basefill_075, 75)
VOV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vov_base_universe_d2_075_vov_basefill_075'] = {'inputs': ['vov_basefill_075'], 'func': vov_base_universe_d2_075_vov_basefill_075}
