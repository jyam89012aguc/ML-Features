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



def clv_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def clv_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def clv_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def clv_154_clv_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def clv_155_clv_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















CLOSE_LOCATION_REGISTRY_2ND_DERIVATIVES = {
    'clv_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': clv_001_realized_vol_z_roc_1},
    'clv_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': clv_007_realized_vol_z_roc_5},
    'clv_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': clv_013_realized_vol_z_roc_42},
    'clv_154_clv_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': clv_154_clv_019_realized_vol_z_42_019_roc_126},
    'clv_155_clv_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': clv_155_clv_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def cl_replacement_d2_001(cl_replacement_001):
    feature = _clean(cl_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_001'] = {'inputs': ['cl_replacement_001'], 'func': cl_replacement_d2_001}


def cl_replacement_d2_002(cl_replacement_002):
    feature = _clean(cl_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_002'] = {'inputs': ['cl_replacement_002'], 'func': cl_replacement_d2_002}


def cl_replacement_d2_003(cl_replacement_003):
    feature = _clean(cl_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_003'] = {'inputs': ['cl_replacement_003'], 'func': cl_replacement_d2_003}


def cl_replacement_d2_004(cl_replacement_004):
    feature = _clean(cl_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_004'] = {'inputs': ['cl_replacement_004'], 'func': cl_replacement_d2_004}


def cl_replacement_d2_005(cl_replacement_005):
    feature = _clean(cl_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_005'] = {'inputs': ['cl_replacement_005'], 'func': cl_replacement_d2_005}


def cl_replacement_d2_006(cl_replacement_006):
    feature = _clean(cl_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_006'] = {'inputs': ['cl_replacement_006'], 'func': cl_replacement_d2_006}


def cl_replacement_d2_007(cl_replacement_007):
    feature = _clean(cl_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_007'] = {'inputs': ['cl_replacement_007'], 'func': cl_replacement_d2_007}


def cl_replacement_d2_008(cl_replacement_008):
    feature = _clean(cl_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_008'] = {'inputs': ['cl_replacement_008'], 'func': cl_replacement_d2_008}


def cl_replacement_d2_009(cl_replacement_009):
    feature = _clean(cl_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_009'] = {'inputs': ['cl_replacement_009'], 'func': cl_replacement_d2_009}


def cl_replacement_d2_010(cl_replacement_010):
    feature = _clean(cl_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_010'] = {'inputs': ['cl_replacement_010'], 'func': cl_replacement_d2_010}


def cl_replacement_d2_011(cl_replacement_011):
    feature = _clean(cl_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_011'] = {'inputs': ['cl_replacement_011'], 'func': cl_replacement_d2_011}


def cl_replacement_d2_012(cl_replacement_012):
    feature = _clean(cl_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_012'] = {'inputs': ['cl_replacement_012'], 'func': cl_replacement_d2_012}


def cl_replacement_d2_013(cl_replacement_013):
    feature = _clean(cl_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_013'] = {'inputs': ['cl_replacement_013'], 'func': cl_replacement_d2_013}


def cl_replacement_d2_014(cl_replacement_014):
    feature = _clean(cl_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_014'] = {'inputs': ['cl_replacement_014'], 'func': cl_replacement_d2_014}


def cl_replacement_d2_015(cl_replacement_015):
    feature = _clean(cl_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_015'] = {'inputs': ['cl_replacement_015'], 'func': cl_replacement_d2_015}


def cl_replacement_d2_016(cl_replacement_016):
    feature = _clean(cl_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_016'] = {'inputs': ['cl_replacement_016'], 'func': cl_replacement_d2_016}


def cl_replacement_d2_017(cl_replacement_017):
    feature = _clean(cl_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_017'] = {'inputs': ['cl_replacement_017'], 'func': cl_replacement_d2_017}


def cl_replacement_d2_018(cl_replacement_018):
    feature = _clean(cl_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_018'] = {'inputs': ['cl_replacement_018'], 'func': cl_replacement_d2_018}


def cl_replacement_d2_019(cl_replacement_019):
    feature = _clean(cl_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_019'] = {'inputs': ['cl_replacement_019'], 'func': cl_replacement_d2_019}


def cl_replacement_d2_020(cl_replacement_020):
    feature = _clean(cl_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_020'] = {'inputs': ['cl_replacement_020'], 'func': cl_replacement_d2_020}


def cl_replacement_d2_021(cl_replacement_021):
    feature = _clean(cl_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_021'] = {'inputs': ['cl_replacement_021'], 'func': cl_replacement_d2_021}


def cl_replacement_d2_022(cl_replacement_022):
    feature = _clean(cl_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_022'] = {'inputs': ['cl_replacement_022'], 'func': cl_replacement_d2_022}


def cl_replacement_d2_023(cl_replacement_023):
    feature = _clean(cl_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_023'] = {'inputs': ['cl_replacement_023'], 'func': cl_replacement_d2_023}


def cl_replacement_d2_024(cl_replacement_024):
    feature = _clean(cl_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_024'] = {'inputs': ['cl_replacement_024'], 'func': cl_replacement_d2_024}


def cl_replacement_d2_025(cl_replacement_025):
    feature = _clean(cl_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_025'] = {'inputs': ['cl_replacement_025'], 'func': cl_replacement_d2_025}


def cl_replacement_d2_026(cl_replacement_026):
    feature = _clean(cl_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_026'] = {'inputs': ['cl_replacement_026'], 'func': cl_replacement_d2_026}


def cl_replacement_d2_027(cl_replacement_027):
    feature = _clean(cl_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_027'] = {'inputs': ['cl_replacement_027'], 'func': cl_replacement_d2_027}


def cl_replacement_d2_028(cl_replacement_028):
    feature = _clean(cl_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_028'] = {'inputs': ['cl_replacement_028'], 'func': cl_replacement_d2_028}


def cl_replacement_d2_029(cl_replacement_029):
    feature = _clean(cl_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_029'] = {'inputs': ['cl_replacement_029'], 'func': cl_replacement_d2_029}


def cl_replacement_d2_030(cl_replacement_030):
    feature = _clean(cl_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_030'] = {'inputs': ['cl_replacement_030'], 'func': cl_replacement_d2_030}


def cl_replacement_d2_031(cl_replacement_031):
    feature = _clean(cl_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_031'] = {'inputs': ['cl_replacement_031'], 'func': cl_replacement_d2_031}


def cl_replacement_d2_032(cl_replacement_032):
    feature = _clean(cl_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_032'] = {'inputs': ['cl_replacement_032'], 'func': cl_replacement_d2_032}


def cl_replacement_d2_033(cl_replacement_033):
    feature = _clean(cl_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_033'] = {'inputs': ['cl_replacement_033'], 'func': cl_replacement_d2_033}


def cl_replacement_d2_034(cl_replacement_034):
    feature = _clean(cl_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_034'] = {'inputs': ['cl_replacement_034'], 'func': cl_replacement_d2_034}


def cl_replacement_d2_035(cl_replacement_035):
    feature = _clean(cl_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_035'] = {'inputs': ['cl_replacement_035'], 'func': cl_replacement_d2_035}


def cl_replacement_d2_036(cl_replacement_036):
    feature = _clean(cl_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_036'] = {'inputs': ['cl_replacement_036'], 'func': cl_replacement_d2_036}


def cl_replacement_d2_037(cl_replacement_037):
    feature = _clean(cl_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_037'] = {'inputs': ['cl_replacement_037'], 'func': cl_replacement_d2_037}


def cl_replacement_d2_038(cl_replacement_038):
    feature = _clean(cl_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_038'] = {'inputs': ['cl_replacement_038'], 'func': cl_replacement_d2_038}


def cl_replacement_d2_039(cl_replacement_039):
    feature = _clean(cl_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_039'] = {'inputs': ['cl_replacement_039'], 'func': cl_replacement_d2_039}


def cl_replacement_d2_040(cl_replacement_040):
    feature = _clean(cl_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_040'] = {'inputs': ['cl_replacement_040'], 'func': cl_replacement_d2_040}


def cl_replacement_d2_041(cl_replacement_041):
    feature = _clean(cl_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_041'] = {'inputs': ['cl_replacement_041'], 'func': cl_replacement_d2_041}


def cl_replacement_d2_042(cl_replacement_042):
    feature = _clean(cl_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_042'] = {'inputs': ['cl_replacement_042'], 'func': cl_replacement_d2_042}


def cl_replacement_d2_043(cl_replacement_043):
    feature = _clean(cl_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_043'] = {'inputs': ['cl_replacement_043'], 'func': cl_replacement_d2_043}


def cl_replacement_d2_044(cl_replacement_044):
    feature = _clean(cl_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_044'] = {'inputs': ['cl_replacement_044'], 'func': cl_replacement_d2_044}


def cl_replacement_d2_045(cl_replacement_045):
    feature = _clean(cl_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_045'] = {'inputs': ['cl_replacement_045'], 'func': cl_replacement_d2_045}


def cl_replacement_d2_046(cl_replacement_046):
    feature = _clean(cl_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_046'] = {'inputs': ['cl_replacement_046'], 'func': cl_replacement_d2_046}


def cl_replacement_d2_047(cl_replacement_047):
    feature = _clean(cl_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_047'] = {'inputs': ['cl_replacement_047'], 'func': cl_replacement_d2_047}


def cl_replacement_d2_048(cl_replacement_048):
    feature = _clean(cl_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_048'] = {'inputs': ['cl_replacement_048'], 'func': cl_replacement_d2_048}


def cl_replacement_d2_049(cl_replacement_049):
    feature = _clean(cl_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_049'] = {'inputs': ['cl_replacement_049'], 'func': cl_replacement_d2_049}


def cl_replacement_d2_050(cl_replacement_050):
    feature = _clean(cl_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_050'] = {'inputs': ['cl_replacement_050'], 'func': cl_replacement_d2_050}


def cl_replacement_d2_051(cl_replacement_051):
    feature = _clean(cl_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_051'] = {'inputs': ['cl_replacement_051'], 'func': cl_replacement_d2_051}


def cl_replacement_d2_052(cl_replacement_052):
    feature = _clean(cl_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_052'] = {'inputs': ['cl_replacement_052'], 'func': cl_replacement_d2_052}


def cl_replacement_d2_053(cl_replacement_053):
    feature = _clean(cl_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_053'] = {'inputs': ['cl_replacement_053'], 'func': cl_replacement_d2_053}


def cl_replacement_d2_054(cl_replacement_054):
    feature = _clean(cl_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_054'] = {'inputs': ['cl_replacement_054'], 'func': cl_replacement_d2_054}


def cl_replacement_d2_055(cl_replacement_055):
    feature = _clean(cl_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_055'] = {'inputs': ['cl_replacement_055'], 'func': cl_replacement_d2_055}


def cl_replacement_d2_056(cl_replacement_056):
    feature = _clean(cl_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_056'] = {'inputs': ['cl_replacement_056'], 'func': cl_replacement_d2_056}


def cl_replacement_d2_057(cl_replacement_057):
    feature = _clean(cl_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_057'] = {'inputs': ['cl_replacement_057'], 'func': cl_replacement_d2_057}


def cl_replacement_d2_058(cl_replacement_058):
    feature = _clean(cl_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_058'] = {'inputs': ['cl_replacement_058'], 'func': cl_replacement_d2_058}


def cl_replacement_d2_059(cl_replacement_059):
    feature = _clean(cl_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_059'] = {'inputs': ['cl_replacement_059'], 'func': cl_replacement_d2_059}


def cl_replacement_d2_060(cl_replacement_060):
    feature = _clean(cl_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_060'] = {'inputs': ['cl_replacement_060'], 'func': cl_replacement_d2_060}


def cl_replacement_d2_061(cl_replacement_061):
    feature = _clean(cl_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_061'] = {'inputs': ['cl_replacement_061'], 'func': cl_replacement_d2_061}


def cl_replacement_d2_062(cl_replacement_062):
    feature = _clean(cl_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_062'] = {'inputs': ['cl_replacement_062'], 'func': cl_replacement_d2_062}


def cl_replacement_d2_063(cl_replacement_063):
    feature = _clean(cl_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_063'] = {'inputs': ['cl_replacement_063'], 'func': cl_replacement_d2_063}


def cl_replacement_d2_064(cl_replacement_064):
    feature = _clean(cl_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_064'] = {'inputs': ['cl_replacement_064'], 'func': cl_replacement_d2_064}


def cl_replacement_d2_065(cl_replacement_065):
    feature = _clean(cl_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_065'] = {'inputs': ['cl_replacement_065'], 'func': cl_replacement_d2_065}


def cl_replacement_d2_066(cl_replacement_066):
    feature = _clean(cl_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_066'] = {'inputs': ['cl_replacement_066'], 'func': cl_replacement_d2_066}


def cl_replacement_d2_067(cl_replacement_067):
    feature = _clean(cl_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_067'] = {'inputs': ['cl_replacement_067'], 'func': cl_replacement_d2_067}


def cl_replacement_d2_068(cl_replacement_068):
    feature = _clean(cl_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_068'] = {'inputs': ['cl_replacement_068'], 'func': cl_replacement_d2_068}


def cl_replacement_d2_069(cl_replacement_069):
    feature = _clean(cl_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_069'] = {'inputs': ['cl_replacement_069'], 'func': cl_replacement_d2_069}


def cl_replacement_d2_070(cl_replacement_070):
    feature = _clean(cl_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_070'] = {'inputs': ['cl_replacement_070'], 'func': cl_replacement_d2_070}


def cl_replacement_d2_071(cl_replacement_071):
    feature = _clean(cl_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_071'] = {'inputs': ['cl_replacement_071'], 'func': cl_replacement_d2_071}


def cl_replacement_d2_072(cl_replacement_072):
    feature = _clean(cl_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_072'] = {'inputs': ['cl_replacement_072'], 'func': cl_replacement_d2_072}


def cl_replacement_d2_073(cl_replacement_073):
    feature = _clean(cl_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_073'] = {'inputs': ['cl_replacement_073'], 'func': cl_replacement_d2_073}


def cl_replacement_d2_074(cl_replacement_074):
    feature = _clean(cl_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_074'] = {'inputs': ['cl_replacement_074'], 'func': cl_replacement_d2_074}


def cl_replacement_d2_075(cl_replacement_075):
    feature = _clean(cl_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_075'] = {'inputs': ['cl_replacement_075'], 'func': cl_replacement_d2_075}


def cl_replacement_d2_076(cl_replacement_076):
    feature = _clean(cl_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_076'] = {'inputs': ['cl_replacement_076'], 'func': cl_replacement_d2_076}


def cl_replacement_d2_077(cl_replacement_077):
    feature = _clean(cl_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_077'] = {'inputs': ['cl_replacement_077'], 'func': cl_replacement_d2_077}


def cl_replacement_d2_078(cl_replacement_078):
    feature = _clean(cl_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_078'] = {'inputs': ['cl_replacement_078'], 'func': cl_replacement_d2_078}


def cl_replacement_d2_079(cl_replacement_079):
    feature = _clean(cl_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_079'] = {'inputs': ['cl_replacement_079'], 'func': cl_replacement_d2_079}


def cl_replacement_d2_080(cl_replacement_080):
    feature = _clean(cl_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_080'] = {'inputs': ['cl_replacement_080'], 'func': cl_replacement_d2_080}


def cl_replacement_d2_081(cl_replacement_081):
    feature = _clean(cl_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_081'] = {'inputs': ['cl_replacement_081'], 'func': cl_replacement_d2_081}


def cl_replacement_d2_082(cl_replacement_082):
    feature = _clean(cl_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_082'] = {'inputs': ['cl_replacement_082'], 'func': cl_replacement_d2_082}


def cl_replacement_d2_083(cl_replacement_083):
    feature = _clean(cl_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_083'] = {'inputs': ['cl_replacement_083'], 'func': cl_replacement_d2_083}


def cl_replacement_d2_084(cl_replacement_084):
    feature = _clean(cl_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_084'] = {'inputs': ['cl_replacement_084'], 'func': cl_replacement_d2_084}


def cl_replacement_d2_085(cl_replacement_085):
    feature = _clean(cl_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_085'] = {'inputs': ['cl_replacement_085'], 'func': cl_replacement_d2_085}


def cl_replacement_d2_086(cl_replacement_086):
    feature = _clean(cl_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_086'] = {'inputs': ['cl_replacement_086'], 'func': cl_replacement_d2_086}


def cl_replacement_d2_087(cl_replacement_087):
    feature = _clean(cl_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_087'] = {'inputs': ['cl_replacement_087'], 'func': cl_replacement_d2_087}


def cl_replacement_d2_088(cl_replacement_088):
    feature = _clean(cl_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_088'] = {'inputs': ['cl_replacement_088'], 'func': cl_replacement_d2_088}


def cl_replacement_d2_089(cl_replacement_089):
    feature = _clean(cl_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_089'] = {'inputs': ['cl_replacement_089'], 'func': cl_replacement_d2_089}


def cl_replacement_d2_090(cl_replacement_090):
    feature = _clean(cl_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_090'] = {'inputs': ['cl_replacement_090'], 'func': cl_replacement_d2_090}


def cl_replacement_d2_091(cl_replacement_091):
    feature = _clean(cl_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_091'] = {'inputs': ['cl_replacement_091'], 'func': cl_replacement_d2_091}


def cl_replacement_d2_092(cl_replacement_092):
    feature = _clean(cl_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_092'] = {'inputs': ['cl_replacement_092'], 'func': cl_replacement_d2_092}


def cl_replacement_d2_093(cl_replacement_093):
    feature = _clean(cl_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_093'] = {'inputs': ['cl_replacement_093'], 'func': cl_replacement_d2_093}


def cl_replacement_d2_094(cl_replacement_094):
    feature = _clean(cl_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_094'] = {'inputs': ['cl_replacement_094'], 'func': cl_replacement_d2_094}


def cl_replacement_d2_095(cl_replacement_095):
    feature = _clean(cl_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_095'] = {'inputs': ['cl_replacement_095'], 'func': cl_replacement_d2_095}


def cl_replacement_d2_096(cl_replacement_096):
    feature = _clean(cl_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_096'] = {'inputs': ['cl_replacement_096'], 'func': cl_replacement_d2_096}


def cl_replacement_d2_097(cl_replacement_097):
    feature = _clean(cl_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_097'] = {'inputs': ['cl_replacement_097'], 'func': cl_replacement_d2_097}


def cl_replacement_d2_098(cl_replacement_098):
    feature = _clean(cl_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_098'] = {'inputs': ['cl_replacement_098'], 'func': cl_replacement_d2_098}


def cl_replacement_d2_099(cl_replacement_099):
    feature = _clean(cl_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_099'] = {'inputs': ['cl_replacement_099'], 'func': cl_replacement_d2_099}


def cl_replacement_d2_100(cl_replacement_100):
    feature = _clean(cl_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_100'] = {'inputs': ['cl_replacement_100'], 'func': cl_replacement_d2_100}


def cl_replacement_d2_101(cl_replacement_101):
    feature = _clean(cl_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_101'] = {'inputs': ['cl_replacement_101'], 'func': cl_replacement_d2_101}


def cl_replacement_d2_102(cl_replacement_102):
    feature = _clean(cl_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_102'] = {'inputs': ['cl_replacement_102'], 'func': cl_replacement_d2_102}


def cl_replacement_d2_103(cl_replacement_103):
    feature = _clean(cl_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_103'] = {'inputs': ['cl_replacement_103'], 'func': cl_replacement_d2_103}


def cl_replacement_d2_104(cl_replacement_104):
    feature = _clean(cl_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_104'] = {'inputs': ['cl_replacement_104'], 'func': cl_replacement_d2_104}


def cl_replacement_d2_105(cl_replacement_105):
    feature = _clean(cl_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_105'] = {'inputs': ['cl_replacement_105'], 'func': cl_replacement_d2_105}


def cl_replacement_d2_106(cl_replacement_106):
    feature = _clean(cl_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_106'] = {'inputs': ['cl_replacement_106'], 'func': cl_replacement_d2_106}


def cl_replacement_d2_107(cl_replacement_107):
    feature = _clean(cl_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_107'] = {'inputs': ['cl_replacement_107'], 'func': cl_replacement_d2_107}


def cl_replacement_d2_108(cl_replacement_108):
    feature = _clean(cl_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_108'] = {'inputs': ['cl_replacement_108'], 'func': cl_replacement_d2_108}


def cl_replacement_d2_109(cl_replacement_109):
    feature = _clean(cl_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_109'] = {'inputs': ['cl_replacement_109'], 'func': cl_replacement_d2_109}


def cl_replacement_d2_110(cl_replacement_110):
    feature = _clean(cl_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_110'] = {'inputs': ['cl_replacement_110'], 'func': cl_replacement_d2_110}


def cl_replacement_d2_111(cl_replacement_111):
    feature = _clean(cl_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_111'] = {'inputs': ['cl_replacement_111'], 'func': cl_replacement_d2_111}


def cl_replacement_d2_112(cl_replacement_112):
    feature = _clean(cl_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_112'] = {'inputs': ['cl_replacement_112'], 'func': cl_replacement_d2_112}


def cl_replacement_d2_113(cl_replacement_113):
    feature = _clean(cl_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_113'] = {'inputs': ['cl_replacement_113'], 'func': cl_replacement_d2_113}


def cl_replacement_d2_114(cl_replacement_114):
    feature = _clean(cl_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_114'] = {'inputs': ['cl_replacement_114'], 'func': cl_replacement_d2_114}


def cl_replacement_d2_115(cl_replacement_115):
    feature = _clean(cl_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_115'] = {'inputs': ['cl_replacement_115'], 'func': cl_replacement_d2_115}


def cl_replacement_d2_116(cl_replacement_116):
    feature = _clean(cl_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_116'] = {'inputs': ['cl_replacement_116'], 'func': cl_replacement_d2_116}


def cl_replacement_d2_117(cl_replacement_117):
    feature = _clean(cl_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_117'] = {'inputs': ['cl_replacement_117'], 'func': cl_replacement_d2_117}


def cl_replacement_d2_118(cl_replacement_118):
    feature = _clean(cl_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_118'] = {'inputs': ['cl_replacement_118'], 'func': cl_replacement_d2_118}


def cl_replacement_d2_119(cl_replacement_119):
    feature = _clean(cl_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_119'] = {'inputs': ['cl_replacement_119'], 'func': cl_replacement_d2_119}


def cl_replacement_d2_120(cl_replacement_120):
    feature = _clean(cl_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_120'] = {'inputs': ['cl_replacement_120'], 'func': cl_replacement_d2_120}


def cl_replacement_d2_121(cl_replacement_121):
    feature = _clean(cl_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_121'] = {'inputs': ['cl_replacement_121'], 'func': cl_replacement_d2_121}


def cl_replacement_d2_122(cl_replacement_122):
    feature = _clean(cl_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_122'] = {'inputs': ['cl_replacement_122'], 'func': cl_replacement_d2_122}


def cl_replacement_d2_123(cl_replacement_123):
    feature = _clean(cl_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_123'] = {'inputs': ['cl_replacement_123'], 'func': cl_replacement_d2_123}


def cl_replacement_d2_124(cl_replacement_124):
    feature = _clean(cl_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_124'] = {'inputs': ['cl_replacement_124'], 'func': cl_replacement_d2_124}


def cl_replacement_d2_125(cl_replacement_125):
    feature = _clean(cl_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_125'] = {'inputs': ['cl_replacement_125'], 'func': cl_replacement_d2_125}


def cl_replacement_d2_126(cl_replacement_126):
    feature = _clean(cl_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_126'] = {'inputs': ['cl_replacement_126'], 'func': cl_replacement_d2_126}


def cl_replacement_d2_127(cl_replacement_127):
    feature = _clean(cl_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_127'] = {'inputs': ['cl_replacement_127'], 'func': cl_replacement_d2_127}


def cl_replacement_d2_128(cl_replacement_128):
    feature = _clean(cl_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_128'] = {'inputs': ['cl_replacement_128'], 'func': cl_replacement_d2_128}


def cl_replacement_d2_129(cl_replacement_129):
    feature = _clean(cl_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_129'] = {'inputs': ['cl_replacement_129'], 'func': cl_replacement_d2_129}


def cl_replacement_d2_130(cl_replacement_130):
    feature = _clean(cl_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_130'] = {'inputs': ['cl_replacement_130'], 'func': cl_replacement_d2_130}


def cl_replacement_d2_131(cl_replacement_131):
    feature = _clean(cl_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_131'] = {'inputs': ['cl_replacement_131'], 'func': cl_replacement_d2_131}


def cl_replacement_d2_132(cl_replacement_132):
    feature = _clean(cl_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_132'] = {'inputs': ['cl_replacement_132'], 'func': cl_replacement_d2_132}


def cl_replacement_d2_133(cl_replacement_133):
    feature = _clean(cl_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_133'] = {'inputs': ['cl_replacement_133'], 'func': cl_replacement_d2_133}


def cl_replacement_d2_134(cl_replacement_134):
    feature = _clean(cl_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_134'] = {'inputs': ['cl_replacement_134'], 'func': cl_replacement_d2_134}


def cl_replacement_d2_135(cl_replacement_135):
    feature = _clean(cl_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_135'] = {'inputs': ['cl_replacement_135'], 'func': cl_replacement_d2_135}


def cl_replacement_d2_136(cl_replacement_136):
    feature = _clean(cl_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_136'] = {'inputs': ['cl_replacement_136'], 'func': cl_replacement_d2_136}


def cl_replacement_d2_137(cl_replacement_137):
    feature = _clean(cl_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_137'] = {'inputs': ['cl_replacement_137'], 'func': cl_replacement_d2_137}


def cl_replacement_d2_138(cl_replacement_138):
    feature = _clean(cl_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_138'] = {'inputs': ['cl_replacement_138'], 'func': cl_replacement_d2_138}


def cl_replacement_d2_139(cl_replacement_139):
    feature = _clean(cl_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_139'] = {'inputs': ['cl_replacement_139'], 'func': cl_replacement_d2_139}


def cl_replacement_d2_140(cl_replacement_140):
    feature = _clean(cl_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_140'] = {'inputs': ['cl_replacement_140'], 'func': cl_replacement_d2_140}


def cl_replacement_d2_141(cl_replacement_141):
    feature = _clean(cl_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_141'] = {'inputs': ['cl_replacement_141'], 'func': cl_replacement_d2_141}


def cl_replacement_d2_142(cl_replacement_142):
    feature = _clean(cl_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_142'] = {'inputs': ['cl_replacement_142'], 'func': cl_replacement_d2_142}


def cl_replacement_d2_143(cl_replacement_143):
    feature = _clean(cl_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_143'] = {'inputs': ['cl_replacement_143'], 'func': cl_replacement_d2_143}


def cl_replacement_d2_144(cl_replacement_144):
    feature = _clean(cl_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_144'] = {'inputs': ['cl_replacement_144'], 'func': cl_replacement_d2_144}


def cl_replacement_d2_145(cl_replacement_145):
    feature = _clean(cl_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_145'] = {'inputs': ['cl_replacement_145'], 'func': cl_replacement_d2_145}


def cl_replacement_d2_146(cl_replacement_146):
    feature = _clean(cl_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_146'] = {'inputs': ['cl_replacement_146'], 'func': cl_replacement_d2_146}


def cl_replacement_d2_147(cl_replacement_147):
    feature = _clean(cl_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_147'] = {'inputs': ['cl_replacement_147'], 'func': cl_replacement_d2_147}


def cl_replacement_d2_148(cl_replacement_148):
    feature = _clean(cl_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_148'] = {'inputs': ['cl_replacement_148'], 'func': cl_replacement_d2_148}


def cl_replacement_d2_149(cl_replacement_149):
    feature = _clean(cl_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_149'] = {'inputs': ['cl_replacement_149'], 'func': cl_replacement_d2_149}


def cl_replacement_d2_150(cl_replacement_150):
    feature = _clean(cl_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_150'] = {'inputs': ['cl_replacement_150'], 'func': cl_replacement_d2_150}


def cl_replacement_d2_151(cl_replacement_151):
    feature = _clean(cl_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_151'] = {'inputs': ['cl_replacement_151'], 'func': cl_replacement_d2_151}


def cl_replacement_d2_152(cl_replacement_152):
    feature = _clean(cl_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_152'] = {'inputs': ['cl_replacement_152'], 'func': cl_replacement_d2_152}


def cl_replacement_d2_153(cl_replacement_153):
    feature = _clean(cl_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_153'] = {'inputs': ['cl_replacement_153'], 'func': cl_replacement_d2_153}


def cl_replacement_d2_154(cl_replacement_154):
    feature = _clean(cl_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_154'] = {'inputs': ['cl_replacement_154'], 'func': cl_replacement_d2_154}


def cl_replacement_d2_155(cl_replacement_155):
    feature = _clean(cl_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_155'] = {'inputs': ['cl_replacement_155'], 'func': cl_replacement_d2_155}


def cl_replacement_d2_156(cl_replacement_156):
    feature = _clean(cl_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_156'] = {'inputs': ['cl_replacement_156'], 'func': cl_replacement_d2_156}


def cl_replacement_d2_157(cl_replacement_157):
    feature = _clean(cl_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_157'] = {'inputs': ['cl_replacement_157'], 'func': cl_replacement_d2_157}


def cl_replacement_d2_158(cl_replacement_158):
    feature = _clean(cl_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_158'] = {'inputs': ['cl_replacement_158'], 'func': cl_replacement_d2_158}


def cl_replacement_d2_159(cl_replacement_159):
    feature = _clean(cl_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_159'] = {'inputs': ['cl_replacement_159'], 'func': cl_replacement_d2_159}


def cl_replacement_d2_160(cl_replacement_160):
    feature = _clean(cl_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_160'] = {'inputs': ['cl_replacement_160'], 'func': cl_replacement_d2_160}


def cl_replacement_d2_161(cl_replacement_161):
    feature = _clean(cl_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_161'] = {'inputs': ['cl_replacement_161'], 'func': cl_replacement_d2_161}


def cl_replacement_d2_162(cl_replacement_162):
    feature = _clean(cl_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_162'] = {'inputs': ['cl_replacement_162'], 'func': cl_replacement_d2_162}


def cl_replacement_d2_163(cl_replacement_163):
    feature = _clean(cl_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_163'] = {'inputs': ['cl_replacement_163'], 'func': cl_replacement_d2_163}


def cl_replacement_d2_164(cl_replacement_164):
    feature = _clean(cl_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_164'] = {'inputs': ['cl_replacement_164'], 'func': cl_replacement_d2_164}


def cl_replacement_d2_165(cl_replacement_165):
    feature = _clean(cl_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_165'] = {'inputs': ['cl_replacement_165'], 'func': cl_replacement_d2_165}


def cl_replacement_d2_166(cl_replacement_166):
    feature = _clean(cl_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_166'] = {'inputs': ['cl_replacement_166'], 'func': cl_replacement_d2_166}


def cl_replacement_d2_167(cl_replacement_167):
    feature = _clean(cl_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_167'] = {'inputs': ['cl_replacement_167'], 'func': cl_replacement_d2_167}


def cl_replacement_d2_168(cl_replacement_168):
    feature = _clean(cl_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_168'] = {'inputs': ['cl_replacement_168'], 'func': cl_replacement_d2_168}


def cl_replacement_d2_169(cl_replacement_169):
    feature = _clean(cl_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_169'] = {'inputs': ['cl_replacement_169'], 'func': cl_replacement_d2_169}


def cl_replacement_d2_170(cl_replacement_170):
    feature = _clean(cl_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_170'] = {'inputs': ['cl_replacement_170'], 'func': cl_replacement_d2_170}


def cl_replacement_d2_171(cl_replacement_171):
    feature = _clean(cl_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_171'] = {'inputs': ['cl_replacement_171'], 'func': cl_replacement_d2_171}


def cl_replacement_d2_172(cl_replacement_172):
    feature = _clean(cl_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_172'] = {'inputs': ['cl_replacement_172'], 'func': cl_replacement_d2_172}


def cl_replacement_d2_173(cl_replacement_173):
    feature = _clean(cl_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_173'] = {'inputs': ['cl_replacement_173'], 'func': cl_replacement_d2_173}


def cl_replacement_d2_174(cl_replacement_174):
    feature = _clean(cl_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_174'] = {'inputs': ['cl_replacement_174'], 'func': cl_replacement_d2_174}


def cl_replacement_d2_175(cl_replacement_175):
    feature = _clean(cl_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
CL_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cl_replacement_d2_175'] = {'inputs': ['cl_replacement_175'], 'func': cl_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def clv_base_universe_d2_001_clv_002_range_expansion_10_002(clv_002_range_expansion_10_002):
    return _base_universe_d2(clv_002_range_expansion_10_002, 1)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_001_clv_002_range_expansion_10_002'] = {'inputs': ['clv_002_range_expansion_10_002'], 'func': clv_base_universe_d2_001_clv_002_range_expansion_10_002}


def clv_base_universe_d2_002_clv_004_close_location_42_004(clv_004_close_location_42_004):
    return _base_universe_d2(clv_004_close_location_42_004, 2)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_002_clv_004_close_location_42_004'] = {'inputs': ['clv_004_close_location_42_004'], 'func': clv_base_universe_d2_002_clv_004_close_location_42_004}


def clv_base_universe_d2_003_clv_005_atr_move_63_005(clv_005_atr_move_63_005):
    return _base_universe_d2(clv_005_atr_move_63_005, 3)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_003_clv_005_atr_move_63_005'] = {'inputs': ['clv_005_atr_move_63_005'], 'func': clv_base_universe_d2_003_clv_005_atr_move_63_005}


def clv_base_universe_d2_004_clv_008_range_expansion_189_008(clv_008_range_expansion_189_008):
    return _base_universe_d2(clv_008_range_expansion_189_008, 4)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_004_clv_008_range_expansion_189_008'] = {'inputs': ['clv_008_range_expansion_189_008'], 'func': clv_base_universe_d2_004_clv_008_range_expansion_189_008}


def clv_base_universe_d2_005_clv_010_close_location_378_010(clv_010_close_location_378_010):
    return _base_universe_d2(clv_010_close_location_378_010, 5)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_005_clv_010_close_location_378_010'] = {'inputs': ['clv_010_close_location_378_010'], 'func': clv_base_universe_d2_005_clv_010_close_location_378_010}


def clv_base_universe_d2_006_clv_011_atr_move_504_011(clv_011_atr_move_504_011):
    return _base_universe_d2(clv_011_atr_move_504_011, 6)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_006_clv_011_atr_move_504_011'] = {'inputs': ['clv_011_atr_move_504_011'], 'func': clv_base_universe_d2_006_clv_011_atr_move_504_011}


def clv_base_universe_d2_007_clv_014_range_expansion_1260_014(clv_014_range_expansion_1260_014):
    return _base_universe_d2(clv_014_range_expansion_1260_014, 7)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_007_clv_014_range_expansion_1260_014'] = {'inputs': ['clv_014_range_expansion_1260_014'], 'func': clv_base_universe_d2_007_clv_014_range_expansion_1260_014}


def clv_base_universe_d2_008_clv_016_close_location_5_016(clv_016_close_location_5_016):
    return _base_universe_d2(clv_016_close_location_5_016, 8)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_008_clv_016_close_location_5_016'] = {'inputs': ['clv_016_close_location_5_016'], 'func': clv_base_universe_d2_008_clv_016_close_location_5_016}


def clv_base_universe_d2_009_clv_017_atr_move_10_017(clv_017_atr_move_10_017):
    return _base_universe_d2(clv_017_atr_move_10_017, 9)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_009_clv_017_atr_move_10_017'] = {'inputs': ['clv_017_atr_move_10_017'], 'func': clv_base_universe_d2_009_clv_017_atr_move_10_017}


def clv_base_universe_d2_010_clv_020_range_expansion_63_020(clv_020_range_expansion_63_020):
    return _base_universe_d2(clv_020_range_expansion_63_020, 10)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_010_clv_020_range_expansion_63_020'] = {'inputs': ['clv_020_range_expansion_63_020'], 'func': clv_base_universe_d2_010_clv_020_range_expansion_63_020}


def clv_base_universe_d2_011_clv_022_close_location_126_022(clv_022_close_location_126_022):
    return _base_universe_d2(clv_022_close_location_126_022, 11)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_011_clv_022_close_location_126_022'] = {'inputs': ['clv_022_close_location_126_022'], 'func': clv_base_universe_d2_011_clv_022_close_location_126_022}


def clv_base_universe_d2_012_clv_023_atr_move_189_023(clv_023_atr_move_189_023):
    return _base_universe_d2(clv_023_atr_move_189_023, 12)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_012_clv_023_atr_move_189_023'] = {'inputs': ['clv_023_atr_move_189_023'], 'func': clv_base_universe_d2_012_clv_023_atr_move_189_023}


def clv_base_universe_d2_013_clv_026_range_expansion_504_026(clv_026_range_expansion_504_026):
    return _base_universe_d2(clv_026_range_expansion_504_026, 13)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_013_clv_026_range_expansion_504_026'] = {'inputs': ['clv_026_range_expansion_504_026'], 'func': clv_base_universe_d2_013_clv_026_range_expansion_504_026}


def clv_base_universe_d2_014_clv_028_close_location_1008_028(clv_028_close_location_1008_028):
    return _base_universe_d2(clv_028_close_location_1008_028, 14)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_014_clv_028_close_location_1008_028'] = {'inputs': ['clv_028_close_location_1008_028'], 'func': clv_base_universe_d2_014_clv_028_close_location_1008_028}


def clv_base_universe_d2_015_clv_029_atr_move_1260_029(clv_029_atr_move_1260_029):
    return _base_universe_d2(clv_029_atr_move_1260_029, 15)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_015_clv_029_atr_move_1260_029'] = {'inputs': ['clv_029_atr_move_1260_029'], 'func': clv_base_universe_d2_015_clv_029_atr_move_1260_029}


def clv_base_universe_d2_016_clv_basefill_001(clv_basefill_001):
    return _base_universe_d2(clv_basefill_001, 16)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_016_clv_basefill_001'] = {'inputs': ['clv_basefill_001'], 'func': clv_base_universe_d2_016_clv_basefill_001}


def clv_base_universe_d2_017_clv_basefill_003(clv_basefill_003):
    return _base_universe_d2(clv_basefill_003, 17)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_017_clv_basefill_003'] = {'inputs': ['clv_basefill_003'], 'func': clv_base_universe_d2_017_clv_basefill_003}


def clv_base_universe_d2_018_clv_basefill_006(clv_basefill_006):
    return _base_universe_d2(clv_basefill_006, 18)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_018_clv_basefill_006'] = {'inputs': ['clv_basefill_006'], 'func': clv_base_universe_d2_018_clv_basefill_006}


def clv_base_universe_d2_019_clv_basefill_007(clv_basefill_007):
    return _base_universe_d2(clv_basefill_007, 19)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_019_clv_basefill_007'] = {'inputs': ['clv_basefill_007'], 'func': clv_base_universe_d2_019_clv_basefill_007}


def clv_base_universe_d2_020_clv_basefill_009(clv_basefill_009):
    return _base_universe_d2(clv_basefill_009, 20)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_020_clv_basefill_009'] = {'inputs': ['clv_basefill_009'], 'func': clv_base_universe_d2_020_clv_basefill_009}


def clv_base_universe_d2_021_clv_basefill_012(clv_basefill_012):
    return _base_universe_d2(clv_basefill_012, 21)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_021_clv_basefill_012'] = {'inputs': ['clv_basefill_012'], 'func': clv_base_universe_d2_021_clv_basefill_012}


def clv_base_universe_d2_022_clv_basefill_013(clv_basefill_013):
    return _base_universe_d2(clv_basefill_013, 22)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_022_clv_basefill_013'] = {'inputs': ['clv_basefill_013'], 'func': clv_base_universe_d2_022_clv_basefill_013}


def clv_base_universe_d2_023_clv_basefill_015(clv_basefill_015):
    return _base_universe_d2(clv_basefill_015, 23)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_023_clv_basefill_015'] = {'inputs': ['clv_basefill_015'], 'func': clv_base_universe_d2_023_clv_basefill_015}


def clv_base_universe_d2_024_clv_basefill_018(clv_basefill_018):
    return _base_universe_d2(clv_basefill_018, 24)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_024_clv_basefill_018'] = {'inputs': ['clv_basefill_018'], 'func': clv_base_universe_d2_024_clv_basefill_018}


def clv_base_universe_d2_025_clv_basefill_019(clv_basefill_019):
    return _base_universe_d2(clv_basefill_019, 25)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_025_clv_basefill_019'] = {'inputs': ['clv_basefill_019'], 'func': clv_base_universe_d2_025_clv_basefill_019}


def clv_base_universe_d2_026_clv_basefill_021(clv_basefill_021):
    return _base_universe_d2(clv_basefill_021, 26)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_026_clv_basefill_021'] = {'inputs': ['clv_basefill_021'], 'func': clv_base_universe_d2_026_clv_basefill_021}


def clv_base_universe_d2_027_clv_basefill_024(clv_basefill_024):
    return _base_universe_d2(clv_basefill_024, 27)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_027_clv_basefill_024'] = {'inputs': ['clv_basefill_024'], 'func': clv_base_universe_d2_027_clv_basefill_024}


def clv_base_universe_d2_028_clv_basefill_025(clv_basefill_025):
    return _base_universe_d2(clv_basefill_025, 28)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_028_clv_basefill_025'] = {'inputs': ['clv_basefill_025'], 'func': clv_base_universe_d2_028_clv_basefill_025}


def clv_base_universe_d2_029_clv_basefill_027(clv_basefill_027):
    return _base_universe_d2(clv_basefill_027, 29)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_029_clv_basefill_027'] = {'inputs': ['clv_basefill_027'], 'func': clv_base_universe_d2_029_clv_basefill_027}


def clv_base_universe_d2_030_clv_basefill_030(clv_basefill_030):
    return _base_universe_d2(clv_basefill_030, 30)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_030_clv_basefill_030'] = {'inputs': ['clv_basefill_030'], 'func': clv_base_universe_d2_030_clv_basefill_030}


def clv_base_universe_d2_031_clv_basefill_031(clv_basefill_031):
    return _base_universe_d2(clv_basefill_031, 31)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_031_clv_basefill_031'] = {'inputs': ['clv_basefill_031'], 'func': clv_base_universe_d2_031_clv_basefill_031}


def clv_base_universe_d2_032_clv_basefill_032(clv_basefill_032):
    return _base_universe_d2(clv_basefill_032, 32)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_032_clv_basefill_032'] = {'inputs': ['clv_basefill_032'], 'func': clv_base_universe_d2_032_clv_basefill_032}


def clv_base_universe_d2_033_clv_basefill_033(clv_basefill_033):
    return _base_universe_d2(clv_basefill_033, 33)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_033_clv_basefill_033'] = {'inputs': ['clv_basefill_033'], 'func': clv_base_universe_d2_033_clv_basefill_033}


def clv_base_universe_d2_034_clv_basefill_034(clv_basefill_034):
    return _base_universe_d2(clv_basefill_034, 34)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_034_clv_basefill_034'] = {'inputs': ['clv_basefill_034'], 'func': clv_base_universe_d2_034_clv_basefill_034}


def clv_base_universe_d2_035_clv_basefill_035(clv_basefill_035):
    return _base_universe_d2(clv_basefill_035, 35)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_035_clv_basefill_035'] = {'inputs': ['clv_basefill_035'], 'func': clv_base_universe_d2_035_clv_basefill_035}


def clv_base_universe_d2_036_clv_basefill_036(clv_basefill_036):
    return _base_universe_d2(clv_basefill_036, 36)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_036_clv_basefill_036'] = {'inputs': ['clv_basefill_036'], 'func': clv_base_universe_d2_036_clv_basefill_036}


def clv_base_universe_d2_037_clv_basefill_037(clv_basefill_037):
    return _base_universe_d2(clv_basefill_037, 37)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_037_clv_basefill_037'] = {'inputs': ['clv_basefill_037'], 'func': clv_base_universe_d2_037_clv_basefill_037}


def clv_base_universe_d2_038_clv_basefill_038(clv_basefill_038):
    return _base_universe_d2(clv_basefill_038, 38)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_038_clv_basefill_038'] = {'inputs': ['clv_basefill_038'], 'func': clv_base_universe_d2_038_clv_basefill_038}


def clv_base_universe_d2_039_clv_basefill_039(clv_basefill_039):
    return _base_universe_d2(clv_basefill_039, 39)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_039_clv_basefill_039'] = {'inputs': ['clv_basefill_039'], 'func': clv_base_universe_d2_039_clv_basefill_039}


def clv_base_universe_d2_040_clv_basefill_040(clv_basefill_040):
    return _base_universe_d2(clv_basefill_040, 40)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_040_clv_basefill_040'] = {'inputs': ['clv_basefill_040'], 'func': clv_base_universe_d2_040_clv_basefill_040}


def clv_base_universe_d2_041_clv_basefill_041(clv_basefill_041):
    return _base_universe_d2(clv_basefill_041, 41)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_041_clv_basefill_041'] = {'inputs': ['clv_basefill_041'], 'func': clv_base_universe_d2_041_clv_basefill_041}


def clv_base_universe_d2_042_clv_basefill_042(clv_basefill_042):
    return _base_universe_d2(clv_basefill_042, 42)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_042_clv_basefill_042'] = {'inputs': ['clv_basefill_042'], 'func': clv_base_universe_d2_042_clv_basefill_042}


def clv_base_universe_d2_043_clv_basefill_043(clv_basefill_043):
    return _base_universe_d2(clv_basefill_043, 43)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_043_clv_basefill_043'] = {'inputs': ['clv_basefill_043'], 'func': clv_base_universe_d2_043_clv_basefill_043}


def clv_base_universe_d2_044_clv_basefill_044(clv_basefill_044):
    return _base_universe_d2(clv_basefill_044, 44)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_044_clv_basefill_044'] = {'inputs': ['clv_basefill_044'], 'func': clv_base_universe_d2_044_clv_basefill_044}


def clv_base_universe_d2_045_clv_basefill_045(clv_basefill_045):
    return _base_universe_d2(clv_basefill_045, 45)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_045_clv_basefill_045'] = {'inputs': ['clv_basefill_045'], 'func': clv_base_universe_d2_045_clv_basefill_045}


def clv_base_universe_d2_046_clv_basefill_046(clv_basefill_046):
    return _base_universe_d2(clv_basefill_046, 46)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_046_clv_basefill_046'] = {'inputs': ['clv_basefill_046'], 'func': clv_base_universe_d2_046_clv_basefill_046}


def clv_base_universe_d2_047_clv_basefill_047(clv_basefill_047):
    return _base_universe_d2(clv_basefill_047, 47)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_047_clv_basefill_047'] = {'inputs': ['clv_basefill_047'], 'func': clv_base_universe_d2_047_clv_basefill_047}


def clv_base_universe_d2_048_clv_basefill_048(clv_basefill_048):
    return _base_universe_d2(clv_basefill_048, 48)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_048_clv_basefill_048'] = {'inputs': ['clv_basefill_048'], 'func': clv_base_universe_d2_048_clv_basefill_048}


def clv_base_universe_d2_049_clv_basefill_049(clv_basefill_049):
    return _base_universe_d2(clv_basefill_049, 49)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_049_clv_basefill_049'] = {'inputs': ['clv_basefill_049'], 'func': clv_base_universe_d2_049_clv_basefill_049}


def clv_base_universe_d2_050_clv_basefill_050(clv_basefill_050):
    return _base_universe_d2(clv_basefill_050, 50)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_050_clv_basefill_050'] = {'inputs': ['clv_basefill_050'], 'func': clv_base_universe_d2_050_clv_basefill_050}


def clv_base_universe_d2_051_clv_basefill_051(clv_basefill_051):
    return _base_universe_d2(clv_basefill_051, 51)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_051_clv_basefill_051'] = {'inputs': ['clv_basefill_051'], 'func': clv_base_universe_d2_051_clv_basefill_051}


def clv_base_universe_d2_052_clv_basefill_052(clv_basefill_052):
    return _base_universe_d2(clv_basefill_052, 52)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_052_clv_basefill_052'] = {'inputs': ['clv_basefill_052'], 'func': clv_base_universe_d2_052_clv_basefill_052}


def clv_base_universe_d2_053_clv_basefill_053(clv_basefill_053):
    return _base_universe_d2(clv_basefill_053, 53)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_053_clv_basefill_053'] = {'inputs': ['clv_basefill_053'], 'func': clv_base_universe_d2_053_clv_basefill_053}


def clv_base_universe_d2_054_clv_basefill_054(clv_basefill_054):
    return _base_universe_d2(clv_basefill_054, 54)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_054_clv_basefill_054'] = {'inputs': ['clv_basefill_054'], 'func': clv_base_universe_d2_054_clv_basefill_054}


def clv_base_universe_d2_055_clv_basefill_055(clv_basefill_055):
    return _base_universe_d2(clv_basefill_055, 55)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_055_clv_basefill_055'] = {'inputs': ['clv_basefill_055'], 'func': clv_base_universe_d2_055_clv_basefill_055}


def clv_base_universe_d2_056_clv_basefill_056(clv_basefill_056):
    return _base_universe_d2(clv_basefill_056, 56)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_056_clv_basefill_056'] = {'inputs': ['clv_basefill_056'], 'func': clv_base_universe_d2_056_clv_basefill_056}


def clv_base_universe_d2_057_clv_basefill_057(clv_basefill_057):
    return _base_universe_d2(clv_basefill_057, 57)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_057_clv_basefill_057'] = {'inputs': ['clv_basefill_057'], 'func': clv_base_universe_d2_057_clv_basefill_057}


def clv_base_universe_d2_058_clv_basefill_058(clv_basefill_058):
    return _base_universe_d2(clv_basefill_058, 58)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_058_clv_basefill_058'] = {'inputs': ['clv_basefill_058'], 'func': clv_base_universe_d2_058_clv_basefill_058}


def clv_base_universe_d2_059_clv_basefill_059(clv_basefill_059):
    return _base_universe_d2(clv_basefill_059, 59)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_059_clv_basefill_059'] = {'inputs': ['clv_basefill_059'], 'func': clv_base_universe_d2_059_clv_basefill_059}


def clv_base_universe_d2_060_clv_basefill_060(clv_basefill_060):
    return _base_universe_d2(clv_basefill_060, 60)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_060_clv_basefill_060'] = {'inputs': ['clv_basefill_060'], 'func': clv_base_universe_d2_060_clv_basefill_060}


def clv_base_universe_d2_061_clv_basefill_061(clv_basefill_061):
    return _base_universe_d2(clv_basefill_061, 61)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_061_clv_basefill_061'] = {'inputs': ['clv_basefill_061'], 'func': clv_base_universe_d2_061_clv_basefill_061}


def clv_base_universe_d2_062_clv_basefill_062(clv_basefill_062):
    return _base_universe_d2(clv_basefill_062, 62)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_062_clv_basefill_062'] = {'inputs': ['clv_basefill_062'], 'func': clv_base_universe_d2_062_clv_basefill_062}


def clv_base_universe_d2_063_clv_basefill_063(clv_basefill_063):
    return _base_universe_d2(clv_basefill_063, 63)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_063_clv_basefill_063'] = {'inputs': ['clv_basefill_063'], 'func': clv_base_universe_d2_063_clv_basefill_063}


def clv_base_universe_d2_064_clv_basefill_064(clv_basefill_064):
    return _base_universe_d2(clv_basefill_064, 64)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_064_clv_basefill_064'] = {'inputs': ['clv_basefill_064'], 'func': clv_base_universe_d2_064_clv_basefill_064}


def clv_base_universe_d2_065_clv_basefill_065(clv_basefill_065):
    return _base_universe_d2(clv_basefill_065, 65)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_065_clv_basefill_065'] = {'inputs': ['clv_basefill_065'], 'func': clv_base_universe_d2_065_clv_basefill_065}


def clv_base_universe_d2_066_clv_basefill_066(clv_basefill_066):
    return _base_universe_d2(clv_basefill_066, 66)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_066_clv_basefill_066'] = {'inputs': ['clv_basefill_066'], 'func': clv_base_universe_d2_066_clv_basefill_066}


def clv_base_universe_d2_067_clv_basefill_067(clv_basefill_067):
    return _base_universe_d2(clv_basefill_067, 67)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_067_clv_basefill_067'] = {'inputs': ['clv_basefill_067'], 'func': clv_base_universe_d2_067_clv_basefill_067}


def clv_base_universe_d2_068_clv_basefill_068(clv_basefill_068):
    return _base_universe_d2(clv_basefill_068, 68)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_068_clv_basefill_068'] = {'inputs': ['clv_basefill_068'], 'func': clv_base_universe_d2_068_clv_basefill_068}


def clv_base_universe_d2_069_clv_basefill_069(clv_basefill_069):
    return _base_universe_d2(clv_basefill_069, 69)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_069_clv_basefill_069'] = {'inputs': ['clv_basefill_069'], 'func': clv_base_universe_d2_069_clv_basefill_069}


def clv_base_universe_d2_070_clv_basefill_070(clv_basefill_070):
    return _base_universe_d2(clv_basefill_070, 70)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_070_clv_basefill_070'] = {'inputs': ['clv_basefill_070'], 'func': clv_base_universe_d2_070_clv_basefill_070}


def clv_base_universe_d2_071_clv_basefill_071(clv_basefill_071):
    return _base_universe_d2(clv_basefill_071, 71)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_071_clv_basefill_071'] = {'inputs': ['clv_basefill_071'], 'func': clv_base_universe_d2_071_clv_basefill_071}


def clv_base_universe_d2_072_clv_basefill_072(clv_basefill_072):
    return _base_universe_d2(clv_basefill_072, 72)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_072_clv_basefill_072'] = {'inputs': ['clv_basefill_072'], 'func': clv_base_universe_d2_072_clv_basefill_072}


def clv_base_universe_d2_073_clv_basefill_073(clv_basefill_073):
    return _base_universe_d2(clv_basefill_073, 73)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_073_clv_basefill_073'] = {'inputs': ['clv_basefill_073'], 'func': clv_base_universe_d2_073_clv_basefill_073}


def clv_base_universe_d2_074_clv_basefill_074(clv_basefill_074):
    return _base_universe_d2(clv_basefill_074, 74)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_074_clv_basefill_074'] = {'inputs': ['clv_basefill_074'], 'func': clv_base_universe_d2_074_clv_basefill_074}


def clv_base_universe_d2_075_clv_basefill_075(clv_basefill_075):
    return _base_universe_d2(clv_basefill_075, 75)
CLV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['clv_base_universe_d2_075_clv_basefill_075'] = {'inputs': ['clv_basefill_075'], 'func': clv_base_universe_d2_075_clv_basefill_075}
