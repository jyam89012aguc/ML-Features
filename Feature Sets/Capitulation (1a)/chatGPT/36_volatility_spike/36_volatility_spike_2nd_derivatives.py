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



def vsp_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def vsp_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def vsp_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def vsp_154_vsp_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def vsp_155_vsp_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLATILITY_SPIKE_REGISTRY_2ND_DERIVATIVES = {
    'vsp_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': vsp_001_realized_vol_z_roc_1},
    'vsp_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': vsp_007_realized_vol_z_roc_5},
    'vsp_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': vsp_013_realized_vol_z_roc_42},
    'vsp_154_vsp_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': vsp_154_vsp_019_realized_vol_z_42_019_roc_126},
    'vsp_155_vsp_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': vsp_155_vsp_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vs_replacement_d2_001(vs_replacement_001):
    feature = _clean(vs_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_001'] = {'inputs': ['vs_replacement_001'], 'func': vs_replacement_d2_001}


def vs_replacement_d2_002(vs_replacement_002):
    feature = _clean(vs_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_002'] = {'inputs': ['vs_replacement_002'], 'func': vs_replacement_d2_002}


def vs_replacement_d2_003(vs_replacement_003):
    feature = _clean(vs_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_003'] = {'inputs': ['vs_replacement_003'], 'func': vs_replacement_d2_003}


def vs_replacement_d2_004(vs_replacement_004):
    feature = _clean(vs_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_004'] = {'inputs': ['vs_replacement_004'], 'func': vs_replacement_d2_004}


def vs_replacement_d2_005(vs_replacement_005):
    feature = _clean(vs_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_005'] = {'inputs': ['vs_replacement_005'], 'func': vs_replacement_d2_005}


def vs_replacement_d2_006(vs_replacement_006):
    feature = _clean(vs_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_006'] = {'inputs': ['vs_replacement_006'], 'func': vs_replacement_d2_006}


def vs_replacement_d2_007(vs_replacement_007):
    feature = _clean(vs_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_007'] = {'inputs': ['vs_replacement_007'], 'func': vs_replacement_d2_007}


def vs_replacement_d2_008(vs_replacement_008):
    feature = _clean(vs_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_008'] = {'inputs': ['vs_replacement_008'], 'func': vs_replacement_d2_008}


def vs_replacement_d2_009(vs_replacement_009):
    feature = _clean(vs_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_009'] = {'inputs': ['vs_replacement_009'], 'func': vs_replacement_d2_009}


def vs_replacement_d2_010(vs_replacement_010):
    feature = _clean(vs_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_010'] = {'inputs': ['vs_replacement_010'], 'func': vs_replacement_d2_010}


def vs_replacement_d2_011(vs_replacement_011):
    feature = _clean(vs_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_011'] = {'inputs': ['vs_replacement_011'], 'func': vs_replacement_d2_011}


def vs_replacement_d2_012(vs_replacement_012):
    feature = _clean(vs_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_012'] = {'inputs': ['vs_replacement_012'], 'func': vs_replacement_d2_012}


def vs_replacement_d2_013(vs_replacement_013):
    feature = _clean(vs_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_013'] = {'inputs': ['vs_replacement_013'], 'func': vs_replacement_d2_013}


def vs_replacement_d2_014(vs_replacement_014):
    feature = _clean(vs_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_014'] = {'inputs': ['vs_replacement_014'], 'func': vs_replacement_d2_014}


def vs_replacement_d2_015(vs_replacement_015):
    feature = _clean(vs_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_015'] = {'inputs': ['vs_replacement_015'], 'func': vs_replacement_d2_015}


def vs_replacement_d2_016(vs_replacement_016):
    feature = _clean(vs_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_016'] = {'inputs': ['vs_replacement_016'], 'func': vs_replacement_d2_016}


def vs_replacement_d2_017(vs_replacement_017):
    feature = _clean(vs_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_017'] = {'inputs': ['vs_replacement_017'], 'func': vs_replacement_d2_017}


def vs_replacement_d2_018(vs_replacement_018):
    feature = _clean(vs_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_018'] = {'inputs': ['vs_replacement_018'], 'func': vs_replacement_d2_018}


def vs_replacement_d2_019(vs_replacement_019):
    feature = _clean(vs_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_019'] = {'inputs': ['vs_replacement_019'], 'func': vs_replacement_d2_019}


def vs_replacement_d2_020(vs_replacement_020):
    feature = _clean(vs_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_020'] = {'inputs': ['vs_replacement_020'], 'func': vs_replacement_d2_020}


def vs_replacement_d2_021(vs_replacement_021):
    feature = _clean(vs_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_021'] = {'inputs': ['vs_replacement_021'], 'func': vs_replacement_d2_021}


def vs_replacement_d2_022(vs_replacement_022):
    feature = _clean(vs_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_022'] = {'inputs': ['vs_replacement_022'], 'func': vs_replacement_d2_022}


def vs_replacement_d2_023(vs_replacement_023):
    feature = _clean(vs_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_023'] = {'inputs': ['vs_replacement_023'], 'func': vs_replacement_d2_023}


def vs_replacement_d2_024(vs_replacement_024):
    feature = _clean(vs_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_024'] = {'inputs': ['vs_replacement_024'], 'func': vs_replacement_d2_024}


def vs_replacement_d2_025(vs_replacement_025):
    feature = _clean(vs_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_025'] = {'inputs': ['vs_replacement_025'], 'func': vs_replacement_d2_025}


def vs_replacement_d2_026(vs_replacement_026):
    feature = _clean(vs_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_026'] = {'inputs': ['vs_replacement_026'], 'func': vs_replacement_d2_026}


def vs_replacement_d2_027(vs_replacement_027):
    feature = _clean(vs_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_027'] = {'inputs': ['vs_replacement_027'], 'func': vs_replacement_d2_027}


def vs_replacement_d2_028(vs_replacement_028):
    feature = _clean(vs_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_028'] = {'inputs': ['vs_replacement_028'], 'func': vs_replacement_d2_028}


def vs_replacement_d2_029(vs_replacement_029):
    feature = _clean(vs_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_029'] = {'inputs': ['vs_replacement_029'], 'func': vs_replacement_d2_029}


def vs_replacement_d2_030(vs_replacement_030):
    feature = _clean(vs_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_030'] = {'inputs': ['vs_replacement_030'], 'func': vs_replacement_d2_030}


def vs_replacement_d2_031(vs_replacement_031):
    feature = _clean(vs_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_031'] = {'inputs': ['vs_replacement_031'], 'func': vs_replacement_d2_031}


def vs_replacement_d2_032(vs_replacement_032):
    feature = _clean(vs_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_032'] = {'inputs': ['vs_replacement_032'], 'func': vs_replacement_d2_032}


def vs_replacement_d2_033(vs_replacement_033):
    feature = _clean(vs_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_033'] = {'inputs': ['vs_replacement_033'], 'func': vs_replacement_d2_033}


def vs_replacement_d2_034(vs_replacement_034):
    feature = _clean(vs_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_034'] = {'inputs': ['vs_replacement_034'], 'func': vs_replacement_d2_034}


def vs_replacement_d2_035(vs_replacement_035):
    feature = _clean(vs_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_035'] = {'inputs': ['vs_replacement_035'], 'func': vs_replacement_d2_035}


def vs_replacement_d2_036(vs_replacement_036):
    feature = _clean(vs_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_036'] = {'inputs': ['vs_replacement_036'], 'func': vs_replacement_d2_036}


def vs_replacement_d2_037(vs_replacement_037):
    feature = _clean(vs_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_037'] = {'inputs': ['vs_replacement_037'], 'func': vs_replacement_d2_037}


def vs_replacement_d2_038(vs_replacement_038):
    feature = _clean(vs_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_038'] = {'inputs': ['vs_replacement_038'], 'func': vs_replacement_d2_038}


def vs_replacement_d2_039(vs_replacement_039):
    feature = _clean(vs_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_039'] = {'inputs': ['vs_replacement_039'], 'func': vs_replacement_d2_039}


def vs_replacement_d2_040(vs_replacement_040):
    feature = _clean(vs_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_040'] = {'inputs': ['vs_replacement_040'], 'func': vs_replacement_d2_040}


def vs_replacement_d2_041(vs_replacement_041):
    feature = _clean(vs_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_041'] = {'inputs': ['vs_replacement_041'], 'func': vs_replacement_d2_041}


def vs_replacement_d2_042(vs_replacement_042):
    feature = _clean(vs_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_042'] = {'inputs': ['vs_replacement_042'], 'func': vs_replacement_d2_042}


def vs_replacement_d2_043(vs_replacement_043):
    feature = _clean(vs_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_043'] = {'inputs': ['vs_replacement_043'], 'func': vs_replacement_d2_043}


def vs_replacement_d2_044(vs_replacement_044):
    feature = _clean(vs_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_044'] = {'inputs': ['vs_replacement_044'], 'func': vs_replacement_d2_044}


def vs_replacement_d2_045(vs_replacement_045):
    feature = _clean(vs_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_045'] = {'inputs': ['vs_replacement_045'], 'func': vs_replacement_d2_045}


def vs_replacement_d2_046(vs_replacement_046):
    feature = _clean(vs_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_046'] = {'inputs': ['vs_replacement_046'], 'func': vs_replacement_d2_046}


def vs_replacement_d2_047(vs_replacement_047):
    feature = _clean(vs_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_047'] = {'inputs': ['vs_replacement_047'], 'func': vs_replacement_d2_047}


def vs_replacement_d2_048(vs_replacement_048):
    feature = _clean(vs_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_048'] = {'inputs': ['vs_replacement_048'], 'func': vs_replacement_d2_048}


def vs_replacement_d2_049(vs_replacement_049):
    feature = _clean(vs_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_049'] = {'inputs': ['vs_replacement_049'], 'func': vs_replacement_d2_049}


def vs_replacement_d2_050(vs_replacement_050):
    feature = _clean(vs_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_050'] = {'inputs': ['vs_replacement_050'], 'func': vs_replacement_d2_050}


def vs_replacement_d2_051(vs_replacement_051):
    feature = _clean(vs_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_051'] = {'inputs': ['vs_replacement_051'], 'func': vs_replacement_d2_051}


def vs_replacement_d2_052(vs_replacement_052):
    feature = _clean(vs_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_052'] = {'inputs': ['vs_replacement_052'], 'func': vs_replacement_d2_052}


def vs_replacement_d2_053(vs_replacement_053):
    feature = _clean(vs_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_053'] = {'inputs': ['vs_replacement_053'], 'func': vs_replacement_d2_053}


def vs_replacement_d2_054(vs_replacement_054):
    feature = _clean(vs_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_054'] = {'inputs': ['vs_replacement_054'], 'func': vs_replacement_d2_054}


def vs_replacement_d2_055(vs_replacement_055):
    feature = _clean(vs_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_055'] = {'inputs': ['vs_replacement_055'], 'func': vs_replacement_d2_055}


def vs_replacement_d2_056(vs_replacement_056):
    feature = _clean(vs_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_056'] = {'inputs': ['vs_replacement_056'], 'func': vs_replacement_d2_056}


def vs_replacement_d2_057(vs_replacement_057):
    feature = _clean(vs_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_057'] = {'inputs': ['vs_replacement_057'], 'func': vs_replacement_d2_057}


def vs_replacement_d2_058(vs_replacement_058):
    feature = _clean(vs_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_058'] = {'inputs': ['vs_replacement_058'], 'func': vs_replacement_d2_058}


def vs_replacement_d2_059(vs_replacement_059):
    feature = _clean(vs_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_059'] = {'inputs': ['vs_replacement_059'], 'func': vs_replacement_d2_059}


def vs_replacement_d2_060(vs_replacement_060):
    feature = _clean(vs_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_060'] = {'inputs': ['vs_replacement_060'], 'func': vs_replacement_d2_060}


def vs_replacement_d2_061(vs_replacement_061):
    feature = _clean(vs_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_061'] = {'inputs': ['vs_replacement_061'], 'func': vs_replacement_d2_061}


def vs_replacement_d2_062(vs_replacement_062):
    feature = _clean(vs_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_062'] = {'inputs': ['vs_replacement_062'], 'func': vs_replacement_d2_062}


def vs_replacement_d2_063(vs_replacement_063):
    feature = _clean(vs_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_063'] = {'inputs': ['vs_replacement_063'], 'func': vs_replacement_d2_063}


def vs_replacement_d2_064(vs_replacement_064):
    feature = _clean(vs_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_064'] = {'inputs': ['vs_replacement_064'], 'func': vs_replacement_d2_064}


def vs_replacement_d2_065(vs_replacement_065):
    feature = _clean(vs_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_065'] = {'inputs': ['vs_replacement_065'], 'func': vs_replacement_d2_065}


def vs_replacement_d2_066(vs_replacement_066):
    feature = _clean(vs_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_066'] = {'inputs': ['vs_replacement_066'], 'func': vs_replacement_d2_066}


def vs_replacement_d2_067(vs_replacement_067):
    feature = _clean(vs_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_067'] = {'inputs': ['vs_replacement_067'], 'func': vs_replacement_d2_067}


def vs_replacement_d2_068(vs_replacement_068):
    feature = _clean(vs_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_068'] = {'inputs': ['vs_replacement_068'], 'func': vs_replacement_d2_068}


def vs_replacement_d2_069(vs_replacement_069):
    feature = _clean(vs_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_069'] = {'inputs': ['vs_replacement_069'], 'func': vs_replacement_d2_069}


def vs_replacement_d2_070(vs_replacement_070):
    feature = _clean(vs_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_070'] = {'inputs': ['vs_replacement_070'], 'func': vs_replacement_d2_070}


def vs_replacement_d2_071(vs_replacement_071):
    feature = _clean(vs_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_071'] = {'inputs': ['vs_replacement_071'], 'func': vs_replacement_d2_071}


def vs_replacement_d2_072(vs_replacement_072):
    feature = _clean(vs_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_072'] = {'inputs': ['vs_replacement_072'], 'func': vs_replacement_d2_072}


def vs_replacement_d2_073(vs_replacement_073):
    feature = _clean(vs_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_073'] = {'inputs': ['vs_replacement_073'], 'func': vs_replacement_d2_073}


def vs_replacement_d2_074(vs_replacement_074):
    feature = _clean(vs_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_074'] = {'inputs': ['vs_replacement_074'], 'func': vs_replacement_d2_074}


def vs_replacement_d2_075(vs_replacement_075):
    feature = _clean(vs_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_075'] = {'inputs': ['vs_replacement_075'], 'func': vs_replacement_d2_075}


def vs_replacement_d2_076(vs_replacement_076):
    feature = _clean(vs_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_076'] = {'inputs': ['vs_replacement_076'], 'func': vs_replacement_d2_076}


def vs_replacement_d2_077(vs_replacement_077):
    feature = _clean(vs_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_077'] = {'inputs': ['vs_replacement_077'], 'func': vs_replacement_d2_077}


def vs_replacement_d2_078(vs_replacement_078):
    feature = _clean(vs_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_078'] = {'inputs': ['vs_replacement_078'], 'func': vs_replacement_d2_078}


def vs_replacement_d2_079(vs_replacement_079):
    feature = _clean(vs_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_079'] = {'inputs': ['vs_replacement_079'], 'func': vs_replacement_d2_079}


def vs_replacement_d2_080(vs_replacement_080):
    feature = _clean(vs_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_080'] = {'inputs': ['vs_replacement_080'], 'func': vs_replacement_d2_080}


def vs_replacement_d2_081(vs_replacement_081):
    feature = _clean(vs_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_081'] = {'inputs': ['vs_replacement_081'], 'func': vs_replacement_d2_081}


def vs_replacement_d2_082(vs_replacement_082):
    feature = _clean(vs_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_082'] = {'inputs': ['vs_replacement_082'], 'func': vs_replacement_d2_082}


def vs_replacement_d2_083(vs_replacement_083):
    feature = _clean(vs_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_083'] = {'inputs': ['vs_replacement_083'], 'func': vs_replacement_d2_083}


def vs_replacement_d2_084(vs_replacement_084):
    feature = _clean(vs_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_084'] = {'inputs': ['vs_replacement_084'], 'func': vs_replacement_d2_084}


def vs_replacement_d2_085(vs_replacement_085):
    feature = _clean(vs_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_085'] = {'inputs': ['vs_replacement_085'], 'func': vs_replacement_d2_085}


def vs_replacement_d2_086(vs_replacement_086):
    feature = _clean(vs_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_086'] = {'inputs': ['vs_replacement_086'], 'func': vs_replacement_d2_086}


def vs_replacement_d2_087(vs_replacement_087):
    feature = _clean(vs_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_087'] = {'inputs': ['vs_replacement_087'], 'func': vs_replacement_d2_087}


def vs_replacement_d2_088(vs_replacement_088):
    feature = _clean(vs_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_088'] = {'inputs': ['vs_replacement_088'], 'func': vs_replacement_d2_088}


def vs_replacement_d2_089(vs_replacement_089):
    feature = _clean(vs_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_089'] = {'inputs': ['vs_replacement_089'], 'func': vs_replacement_d2_089}


def vs_replacement_d2_090(vs_replacement_090):
    feature = _clean(vs_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_090'] = {'inputs': ['vs_replacement_090'], 'func': vs_replacement_d2_090}


def vs_replacement_d2_091(vs_replacement_091):
    feature = _clean(vs_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_091'] = {'inputs': ['vs_replacement_091'], 'func': vs_replacement_d2_091}


def vs_replacement_d2_092(vs_replacement_092):
    feature = _clean(vs_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_092'] = {'inputs': ['vs_replacement_092'], 'func': vs_replacement_d2_092}


def vs_replacement_d2_093(vs_replacement_093):
    feature = _clean(vs_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_093'] = {'inputs': ['vs_replacement_093'], 'func': vs_replacement_d2_093}


def vs_replacement_d2_094(vs_replacement_094):
    feature = _clean(vs_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_094'] = {'inputs': ['vs_replacement_094'], 'func': vs_replacement_d2_094}


def vs_replacement_d2_095(vs_replacement_095):
    feature = _clean(vs_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_095'] = {'inputs': ['vs_replacement_095'], 'func': vs_replacement_d2_095}


def vs_replacement_d2_096(vs_replacement_096):
    feature = _clean(vs_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_096'] = {'inputs': ['vs_replacement_096'], 'func': vs_replacement_d2_096}


def vs_replacement_d2_097(vs_replacement_097):
    feature = _clean(vs_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_097'] = {'inputs': ['vs_replacement_097'], 'func': vs_replacement_d2_097}


def vs_replacement_d2_098(vs_replacement_098):
    feature = _clean(vs_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_098'] = {'inputs': ['vs_replacement_098'], 'func': vs_replacement_d2_098}


def vs_replacement_d2_099(vs_replacement_099):
    feature = _clean(vs_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_099'] = {'inputs': ['vs_replacement_099'], 'func': vs_replacement_d2_099}


def vs_replacement_d2_100(vs_replacement_100):
    feature = _clean(vs_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_100'] = {'inputs': ['vs_replacement_100'], 'func': vs_replacement_d2_100}


def vs_replacement_d2_101(vs_replacement_101):
    feature = _clean(vs_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_101'] = {'inputs': ['vs_replacement_101'], 'func': vs_replacement_d2_101}


def vs_replacement_d2_102(vs_replacement_102):
    feature = _clean(vs_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_102'] = {'inputs': ['vs_replacement_102'], 'func': vs_replacement_d2_102}


def vs_replacement_d2_103(vs_replacement_103):
    feature = _clean(vs_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_103'] = {'inputs': ['vs_replacement_103'], 'func': vs_replacement_d2_103}


def vs_replacement_d2_104(vs_replacement_104):
    feature = _clean(vs_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_104'] = {'inputs': ['vs_replacement_104'], 'func': vs_replacement_d2_104}


def vs_replacement_d2_105(vs_replacement_105):
    feature = _clean(vs_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_105'] = {'inputs': ['vs_replacement_105'], 'func': vs_replacement_d2_105}


def vs_replacement_d2_106(vs_replacement_106):
    feature = _clean(vs_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_106'] = {'inputs': ['vs_replacement_106'], 'func': vs_replacement_d2_106}


def vs_replacement_d2_107(vs_replacement_107):
    feature = _clean(vs_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_107'] = {'inputs': ['vs_replacement_107'], 'func': vs_replacement_d2_107}


def vs_replacement_d2_108(vs_replacement_108):
    feature = _clean(vs_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_108'] = {'inputs': ['vs_replacement_108'], 'func': vs_replacement_d2_108}


def vs_replacement_d2_109(vs_replacement_109):
    feature = _clean(vs_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_109'] = {'inputs': ['vs_replacement_109'], 'func': vs_replacement_d2_109}


def vs_replacement_d2_110(vs_replacement_110):
    feature = _clean(vs_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_110'] = {'inputs': ['vs_replacement_110'], 'func': vs_replacement_d2_110}


def vs_replacement_d2_111(vs_replacement_111):
    feature = _clean(vs_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_111'] = {'inputs': ['vs_replacement_111'], 'func': vs_replacement_d2_111}


def vs_replacement_d2_112(vs_replacement_112):
    feature = _clean(vs_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_112'] = {'inputs': ['vs_replacement_112'], 'func': vs_replacement_d2_112}


def vs_replacement_d2_113(vs_replacement_113):
    feature = _clean(vs_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_113'] = {'inputs': ['vs_replacement_113'], 'func': vs_replacement_d2_113}


def vs_replacement_d2_114(vs_replacement_114):
    feature = _clean(vs_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_114'] = {'inputs': ['vs_replacement_114'], 'func': vs_replacement_d2_114}


def vs_replacement_d2_115(vs_replacement_115):
    feature = _clean(vs_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_115'] = {'inputs': ['vs_replacement_115'], 'func': vs_replacement_d2_115}


def vs_replacement_d2_116(vs_replacement_116):
    feature = _clean(vs_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_116'] = {'inputs': ['vs_replacement_116'], 'func': vs_replacement_d2_116}


def vs_replacement_d2_117(vs_replacement_117):
    feature = _clean(vs_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_117'] = {'inputs': ['vs_replacement_117'], 'func': vs_replacement_d2_117}


def vs_replacement_d2_118(vs_replacement_118):
    feature = _clean(vs_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_118'] = {'inputs': ['vs_replacement_118'], 'func': vs_replacement_d2_118}


def vs_replacement_d2_119(vs_replacement_119):
    feature = _clean(vs_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_119'] = {'inputs': ['vs_replacement_119'], 'func': vs_replacement_d2_119}


def vs_replacement_d2_120(vs_replacement_120):
    feature = _clean(vs_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_120'] = {'inputs': ['vs_replacement_120'], 'func': vs_replacement_d2_120}


def vs_replacement_d2_121(vs_replacement_121):
    feature = _clean(vs_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_121'] = {'inputs': ['vs_replacement_121'], 'func': vs_replacement_d2_121}


def vs_replacement_d2_122(vs_replacement_122):
    feature = _clean(vs_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_122'] = {'inputs': ['vs_replacement_122'], 'func': vs_replacement_d2_122}


def vs_replacement_d2_123(vs_replacement_123):
    feature = _clean(vs_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_123'] = {'inputs': ['vs_replacement_123'], 'func': vs_replacement_d2_123}


def vs_replacement_d2_124(vs_replacement_124):
    feature = _clean(vs_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_124'] = {'inputs': ['vs_replacement_124'], 'func': vs_replacement_d2_124}


def vs_replacement_d2_125(vs_replacement_125):
    feature = _clean(vs_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_125'] = {'inputs': ['vs_replacement_125'], 'func': vs_replacement_d2_125}


def vs_replacement_d2_126(vs_replacement_126):
    feature = _clean(vs_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_126'] = {'inputs': ['vs_replacement_126'], 'func': vs_replacement_d2_126}


def vs_replacement_d2_127(vs_replacement_127):
    feature = _clean(vs_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_127'] = {'inputs': ['vs_replacement_127'], 'func': vs_replacement_d2_127}


def vs_replacement_d2_128(vs_replacement_128):
    feature = _clean(vs_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_128'] = {'inputs': ['vs_replacement_128'], 'func': vs_replacement_d2_128}


def vs_replacement_d2_129(vs_replacement_129):
    feature = _clean(vs_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_129'] = {'inputs': ['vs_replacement_129'], 'func': vs_replacement_d2_129}


def vs_replacement_d2_130(vs_replacement_130):
    feature = _clean(vs_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_130'] = {'inputs': ['vs_replacement_130'], 'func': vs_replacement_d2_130}


def vs_replacement_d2_131(vs_replacement_131):
    feature = _clean(vs_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_131'] = {'inputs': ['vs_replacement_131'], 'func': vs_replacement_d2_131}


def vs_replacement_d2_132(vs_replacement_132):
    feature = _clean(vs_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_132'] = {'inputs': ['vs_replacement_132'], 'func': vs_replacement_d2_132}


def vs_replacement_d2_133(vs_replacement_133):
    feature = _clean(vs_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_133'] = {'inputs': ['vs_replacement_133'], 'func': vs_replacement_d2_133}


def vs_replacement_d2_134(vs_replacement_134):
    feature = _clean(vs_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_134'] = {'inputs': ['vs_replacement_134'], 'func': vs_replacement_d2_134}


def vs_replacement_d2_135(vs_replacement_135):
    feature = _clean(vs_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_135'] = {'inputs': ['vs_replacement_135'], 'func': vs_replacement_d2_135}


def vs_replacement_d2_136(vs_replacement_136):
    feature = _clean(vs_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_136'] = {'inputs': ['vs_replacement_136'], 'func': vs_replacement_d2_136}


def vs_replacement_d2_137(vs_replacement_137):
    feature = _clean(vs_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_137'] = {'inputs': ['vs_replacement_137'], 'func': vs_replacement_d2_137}


def vs_replacement_d2_138(vs_replacement_138):
    feature = _clean(vs_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_138'] = {'inputs': ['vs_replacement_138'], 'func': vs_replacement_d2_138}


def vs_replacement_d2_139(vs_replacement_139):
    feature = _clean(vs_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_139'] = {'inputs': ['vs_replacement_139'], 'func': vs_replacement_d2_139}


def vs_replacement_d2_140(vs_replacement_140):
    feature = _clean(vs_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_140'] = {'inputs': ['vs_replacement_140'], 'func': vs_replacement_d2_140}


def vs_replacement_d2_141(vs_replacement_141):
    feature = _clean(vs_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_141'] = {'inputs': ['vs_replacement_141'], 'func': vs_replacement_d2_141}


def vs_replacement_d2_142(vs_replacement_142):
    feature = _clean(vs_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_142'] = {'inputs': ['vs_replacement_142'], 'func': vs_replacement_d2_142}


def vs_replacement_d2_143(vs_replacement_143):
    feature = _clean(vs_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_143'] = {'inputs': ['vs_replacement_143'], 'func': vs_replacement_d2_143}


def vs_replacement_d2_144(vs_replacement_144):
    feature = _clean(vs_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_144'] = {'inputs': ['vs_replacement_144'], 'func': vs_replacement_d2_144}


def vs_replacement_d2_145(vs_replacement_145):
    feature = _clean(vs_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_145'] = {'inputs': ['vs_replacement_145'], 'func': vs_replacement_d2_145}


def vs_replacement_d2_146(vs_replacement_146):
    feature = _clean(vs_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_146'] = {'inputs': ['vs_replacement_146'], 'func': vs_replacement_d2_146}


def vs_replacement_d2_147(vs_replacement_147):
    feature = _clean(vs_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_147'] = {'inputs': ['vs_replacement_147'], 'func': vs_replacement_d2_147}


def vs_replacement_d2_148(vs_replacement_148):
    feature = _clean(vs_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_148'] = {'inputs': ['vs_replacement_148'], 'func': vs_replacement_d2_148}


def vs_replacement_d2_149(vs_replacement_149):
    feature = _clean(vs_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_149'] = {'inputs': ['vs_replacement_149'], 'func': vs_replacement_d2_149}


def vs_replacement_d2_150(vs_replacement_150):
    feature = _clean(vs_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_150'] = {'inputs': ['vs_replacement_150'], 'func': vs_replacement_d2_150}


def vs_replacement_d2_151(vs_replacement_151):
    feature = _clean(vs_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_151'] = {'inputs': ['vs_replacement_151'], 'func': vs_replacement_d2_151}


def vs_replacement_d2_152(vs_replacement_152):
    feature = _clean(vs_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_152'] = {'inputs': ['vs_replacement_152'], 'func': vs_replacement_d2_152}


def vs_replacement_d2_153(vs_replacement_153):
    feature = _clean(vs_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_153'] = {'inputs': ['vs_replacement_153'], 'func': vs_replacement_d2_153}


def vs_replacement_d2_154(vs_replacement_154):
    feature = _clean(vs_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_154'] = {'inputs': ['vs_replacement_154'], 'func': vs_replacement_d2_154}


def vs_replacement_d2_155(vs_replacement_155):
    feature = _clean(vs_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_155'] = {'inputs': ['vs_replacement_155'], 'func': vs_replacement_d2_155}


def vs_replacement_d2_156(vs_replacement_156):
    feature = _clean(vs_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_156'] = {'inputs': ['vs_replacement_156'], 'func': vs_replacement_d2_156}


def vs_replacement_d2_157(vs_replacement_157):
    feature = _clean(vs_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_157'] = {'inputs': ['vs_replacement_157'], 'func': vs_replacement_d2_157}


def vs_replacement_d2_158(vs_replacement_158):
    feature = _clean(vs_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_158'] = {'inputs': ['vs_replacement_158'], 'func': vs_replacement_d2_158}


def vs_replacement_d2_159(vs_replacement_159):
    feature = _clean(vs_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_159'] = {'inputs': ['vs_replacement_159'], 'func': vs_replacement_d2_159}


def vs_replacement_d2_160(vs_replacement_160):
    feature = _clean(vs_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_160'] = {'inputs': ['vs_replacement_160'], 'func': vs_replacement_d2_160}


def vs_replacement_d2_161(vs_replacement_161):
    feature = _clean(vs_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_161'] = {'inputs': ['vs_replacement_161'], 'func': vs_replacement_d2_161}


def vs_replacement_d2_162(vs_replacement_162):
    feature = _clean(vs_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_162'] = {'inputs': ['vs_replacement_162'], 'func': vs_replacement_d2_162}


def vs_replacement_d2_163(vs_replacement_163):
    feature = _clean(vs_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_163'] = {'inputs': ['vs_replacement_163'], 'func': vs_replacement_d2_163}


def vs_replacement_d2_164(vs_replacement_164):
    feature = _clean(vs_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_164'] = {'inputs': ['vs_replacement_164'], 'func': vs_replacement_d2_164}


def vs_replacement_d2_165(vs_replacement_165):
    feature = _clean(vs_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_165'] = {'inputs': ['vs_replacement_165'], 'func': vs_replacement_d2_165}


def vs_replacement_d2_166(vs_replacement_166):
    feature = _clean(vs_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_166'] = {'inputs': ['vs_replacement_166'], 'func': vs_replacement_d2_166}


def vs_replacement_d2_167(vs_replacement_167):
    feature = _clean(vs_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_167'] = {'inputs': ['vs_replacement_167'], 'func': vs_replacement_d2_167}


def vs_replacement_d2_168(vs_replacement_168):
    feature = _clean(vs_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_168'] = {'inputs': ['vs_replacement_168'], 'func': vs_replacement_d2_168}


def vs_replacement_d2_169(vs_replacement_169):
    feature = _clean(vs_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_169'] = {'inputs': ['vs_replacement_169'], 'func': vs_replacement_d2_169}


def vs_replacement_d2_170(vs_replacement_170):
    feature = _clean(vs_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_170'] = {'inputs': ['vs_replacement_170'], 'func': vs_replacement_d2_170}


def vs_replacement_d2_171(vs_replacement_171):
    feature = _clean(vs_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_171'] = {'inputs': ['vs_replacement_171'], 'func': vs_replacement_d2_171}


def vs_replacement_d2_172(vs_replacement_172):
    feature = _clean(vs_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_172'] = {'inputs': ['vs_replacement_172'], 'func': vs_replacement_d2_172}


def vs_replacement_d2_173(vs_replacement_173):
    feature = _clean(vs_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_173'] = {'inputs': ['vs_replacement_173'], 'func': vs_replacement_d2_173}


def vs_replacement_d2_174(vs_replacement_174):
    feature = _clean(vs_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_174'] = {'inputs': ['vs_replacement_174'], 'func': vs_replacement_d2_174}


def vs_replacement_d2_175(vs_replacement_175):
    feature = _clean(vs_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
VS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vs_replacement_d2_175'] = {'inputs': ['vs_replacement_175'], 'func': vs_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vsp_base_universe_d2_001_vsp_002_range_expansion_10_002(vsp_002_range_expansion_10_002):
    return _base_universe_d2(vsp_002_range_expansion_10_002, 1)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_001_vsp_002_range_expansion_10_002'] = {'inputs': ['vsp_002_range_expansion_10_002'], 'func': vsp_base_universe_d2_001_vsp_002_range_expansion_10_002}


def vsp_base_universe_d2_002_vsp_004_close_location_42_004(vsp_004_close_location_42_004):
    return _base_universe_d2(vsp_004_close_location_42_004, 2)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_002_vsp_004_close_location_42_004'] = {'inputs': ['vsp_004_close_location_42_004'], 'func': vsp_base_universe_d2_002_vsp_004_close_location_42_004}


def vsp_base_universe_d2_003_vsp_005_atr_move_63_005(vsp_005_atr_move_63_005):
    return _base_universe_d2(vsp_005_atr_move_63_005, 3)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_003_vsp_005_atr_move_63_005'] = {'inputs': ['vsp_005_atr_move_63_005'], 'func': vsp_base_universe_d2_003_vsp_005_atr_move_63_005}


def vsp_base_universe_d2_004_vsp_008_range_expansion_189_008(vsp_008_range_expansion_189_008):
    return _base_universe_d2(vsp_008_range_expansion_189_008, 4)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_004_vsp_008_range_expansion_189_008'] = {'inputs': ['vsp_008_range_expansion_189_008'], 'func': vsp_base_universe_d2_004_vsp_008_range_expansion_189_008}


def vsp_base_universe_d2_005_vsp_010_close_location_378_010(vsp_010_close_location_378_010):
    return _base_universe_d2(vsp_010_close_location_378_010, 5)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_005_vsp_010_close_location_378_010'] = {'inputs': ['vsp_010_close_location_378_010'], 'func': vsp_base_universe_d2_005_vsp_010_close_location_378_010}


def vsp_base_universe_d2_006_vsp_011_atr_move_504_011(vsp_011_atr_move_504_011):
    return _base_universe_d2(vsp_011_atr_move_504_011, 6)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_006_vsp_011_atr_move_504_011'] = {'inputs': ['vsp_011_atr_move_504_011'], 'func': vsp_base_universe_d2_006_vsp_011_atr_move_504_011}


def vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014(vsp_014_range_expansion_1260_014):
    return _base_universe_d2(vsp_014_range_expansion_1260_014, 7)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014'] = {'inputs': ['vsp_014_range_expansion_1260_014'], 'func': vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014}


def vsp_base_universe_d2_008_vsp_016_close_location_5_016(vsp_016_close_location_5_016):
    return _base_universe_d2(vsp_016_close_location_5_016, 8)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_008_vsp_016_close_location_5_016'] = {'inputs': ['vsp_016_close_location_5_016'], 'func': vsp_base_universe_d2_008_vsp_016_close_location_5_016}


def vsp_base_universe_d2_009_vsp_017_atr_move_10_017(vsp_017_atr_move_10_017):
    return _base_universe_d2(vsp_017_atr_move_10_017, 9)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_009_vsp_017_atr_move_10_017'] = {'inputs': ['vsp_017_atr_move_10_017'], 'func': vsp_base_universe_d2_009_vsp_017_atr_move_10_017}


def vsp_base_universe_d2_010_vsp_020_range_expansion_63_020(vsp_020_range_expansion_63_020):
    return _base_universe_d2(vsp_020_range_expansion_63_020, 10)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_010_vsp_020_range_expansion_63_020'] = {'inputs': ['vsp_020_range_expansion_63_020'], 'func': vsp_base_universe_d2_010_vsp_020_range_expansion_63_020}


def vsp_base_universe_d2_011_vsp_022_close_location_126_022(vsp_022_close_location_126_022):
    return _base_universe_d2(vsp_022_close_location_126_022, 11)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_011_vsp_022_close_location_126_022'] = {'inputs': ['vsp_022_close_location_126_022'], 'func': vsp_base_universe_d2_011_vsp_022_close_location_126_022}


def vsp_base_universe_d2_012_vsp_023_atr_move_189_023(vsp_023_atr_move_189_023):
    return _base_universe_d2(vsp_023_atr_move_189_023, 12)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_012_vsp_023_atr_move_189_023'] = {'inputs': ['vsp_023_atr_move_189_023'], 'func': vsp_base_universe_d2_012_vsp_023_atr_move_189_023}


def vsp_base_universe_d2_013_vsp_026_range_expansion_504_026(vsp_026_range_expansion_504_026):
    return _base_universe_d2(vsp_026_range_expansion_504_026, 13)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_013_vsp_026_range_expansion_504_026'] = {'inputs': ['vsp_026_range_expansion_504_026'], 'func': vsp_base_universe_d2_013_vsp_026_range_expansion_504_026}


def vsp_base_universe_d2_014_vsp_028_close_location_1008_028(vsp_028_close_location_1008_028):
    return _base_universe_d2(vsp_028_close_location_1008_028, 14)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_014_vsp_028_close_location_1008_028'] = {'inputs': ['vsp_028_close_location_1008_028'], 'func': vsp_base_universe_d2_014_vsp_028_close_location_1008_028}


def vsp_base_universe_d2_015_vsp_029_atr_move_1260_029(vsp_029_atr_move_1260_029):
    return _base_universe_d2(vsp_029_atr_move_1260_029, 15)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_015_vsp_029_atr_move_1260_029'] = {'inputs': ['vsp_029_atr_move_1260_029'], 'func': vsp_base_universe_d2_015_vsp_029_atr_move_1260_029}


def vsp_base_universe_d2_016_vsp_basefill_001(vsp_basefill_001):
    return _base_universe_d2(vsp_basefill_001, 16)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_016_vsp_basefill_001'] = {'inputs': ['vsp_basefill_001'], 'func': vsp_base_universe_d2_016_vsp_basefill_001}


def vsp_base_universe_d2_017_vsp_basefill_003(vsp_basefill_003):
    return _base_universe_d2(vsp_basefill_003, 17)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_017_vsp_basefill_003'] = {'inputs': ['vsp_basefill_003'], 'func': vsp_base_universe_d2_017_vsp_basefill_003}


def vsp_base_universe_d2_018_vsp_basefill_006(vsp_basefill_006):
    return _base_universe_d2(vsp_basefill_006, 18)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_018_vsp_basefill_006'] = {'inputs': ['vsp_basefill_006'], 'func': vsp_base_universe_d2_018_vsp_basefill_006}


def vsp_base_universe_d2_019_vsp_basefill_007(vsp_basefill_007):
    return _base_universe_d2(vsp_basefill_007, 19)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_019_vsp_basefill_007'] = {'inputs': ['vsp_basefill_007'], 'func': vsp_base_universe_d2_019_vsp_basefill_007}


def vsp_base_universe_d2_020_vsp_basefill_009(vsp_basefill_009):
    return _base_universe_d2(vsp_basefill_009, 20)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_020_vsp_basefill_009'] = {'inputs': ['vsp_basefill_009'], 'func': vsp_base_universe_d2_020_vsp_basefill_009}


def vsp_base_universe_d2_021_vsp_basefill_012(vsp_basefill_012):
    return _base_universe_d2(vsp_basefill_012, 21)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_021_vsp_basefill_012'] = {'inputs': ['vsp_basefill_012'], 'func': vsp_base_universe_d2_021_vsp_basefill_012}


def vsp_base_universe_d2_022_vsp_basefill_013(vsp_basefill_013):
    return _base_universe_d2(vsp_basefill_013, 22)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_022_vsp_basefill_013'] = {'inputs': ['vsp_basefill_013'], 'func': vsp_base_universe_d2_022_vsp_basefill_013}


def vsp_base_universe_d2_023_vsp_basefill_015(vsp_basefill_015):
    return _base_universe_d2(vsp_basefill_015, 23)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_023_vsp_basefill_015'] = {'inputs': ['vsp_basefill_015'], 'func': vsp_base_universe_d2_023_vsp_basefill_015}


def vsp_base_universe_d2_024_vsp_basefill_018(vsp_basefill_018):
    return _base_universe_d2(vsp_basefill_018, 24)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_024_vsp_basefill_018'] = {'inputs': ['vsp_basefill_018'], 'func': vsp_base_universe_d2_024_vsp_basefill_018}


def vsp_base_universe_d2_025_vsp_basefill_019(vsp_basefill_019):
    return _base_universe_d2(vsp_basefill_019, 25)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_025_vsp_basefill_019'] = {'inputs': ['vsp_basefill_019'], 'func': vsp_base_universe_d2_025_vsp_basefill_019}


def vsp_base_universe_d2_026_vsp_basefill_021(vsp_basefill_021):
    return _base_universe_d2(vsp_basefill_021, 26)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_026_vsp_basefill_021'] = {'inputs': ['vsp_basefill_021'], 'func': vsp_base_universe_d2_026_vsp_basefill_021}


def vsp_base_universe_d2_027_vsp_basefill_024(vsp_basefill_024):
    return _base_universe_d2(vsp_basefill_024, 27)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_027_vsp_basefill_024'] = {'inputs': ['vsp_basefill_024'], 'func': vsp_base_universe_d2_027_vsp_basefill_024}


def vsp_base_universe_d2_028_vsp_basefill_025(vsp_basefill_025):
    return _base_universe_d2(vsp_basefill_025, 28)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_028_vsp_basefill_025'] = {'inputs': ['vsp_basefill_025'], 'func': vsp_base_universe_d2_028_vsp_basefill_025}


def vsp_base_universe_d2_029_vsp_basefill_027(vsp_basefill_027):
    return _base_universe_d2(vsp_basefill_027, 29)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_029_vsp_basefill_027'] = {'inputs': ['vsp_basefill_027'], 'func': vsp_base_universe_d2_029_vsp_basefill_027}


def vsp_base_universe_d2_030_vsp_basefill_030(vsp_basefill_030):
    return _base_universe_d2(vsp_basefill_030, 30)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_030_vsp_basefill_030'] = {'inputs': ['vsp_basefill_030'], 'func': vsp_base_universe_d2_030_vsp_basefill_030}


def vsp_base_universe_d2_031_vsp_basefill_031(vsp_basefill_031):
    return _base_universe_d2(vsp_basefill_031, 31)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_031_vsp_basefill_031'] = {'inputs': ['vsp_basefill_031'], 'func': vsp_base_universe_d2_031_vsp_basefill_031}


def vsp_base_universe_d2_032_vsp_basefill_032(vsp_basefill_032):
    return _base_universe_d2(vsp_basefill_032, 32)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_032_vsp_basefill_032'] = {'inputs': ['vsp_basefill_032'], 'func': vsp_base_universe_d2_032_vsp_basefill_032}


def vsp_base_universe_d2_033_vsp_basefill_033(vsp_basefill_033):
    return _base_universe_d2(vsp_basefill_033, 33)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_033_vsp_basefill_033'] = {'inputs': ['vsp_basefill_033'], 'func': vsp_base_universe_d2_033_vsp_basefill_033}


def vsp_base_universe_d2_034_vsp_basefill_034(vsp_basefill_034):
    return _base_universe_d2(vsp_basefill_034, 34)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_034_vsp_basefill_034'] = {'inputs': ['vsp_basefill_034'], 'func': vsp_base_universe_d2_034_vsp_basefill_034}


def vsp_base_universe_d2_035_vsp_basefill_035(vsp_basefill_035):
    return _base_universe_d2(vsp_basefill_035, 35)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_035_vsp_basefill_035'] = {'inputs': ['vsp_basefill_035'], 'func': vsp_base_universe_d2_035_vsp_basefill_035}


def vsp_base_universe_d2_036_vsp_basefill_036(vsp_basefill_036):
    return _base_universe_d2(vsp_basefill_036, 36)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_036_vsp_basefill_036'] = {'inputs': ['vsp_basefill_036'], 'func': vsp_base_universe_d2_036_vsp_basefill_036}


def vsp_base_universe_d2_037_vsp_basefill_037(vsp_basefill_037):
    return _base_universe_d2(vsp_basefill_037, 37)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_037_vsp_basefill_037'] = {'inputs': ['vsp_basefill_037'], 'func': vsp_base_universe_d2_037_vsp_basefill_037}


def vsp_base_universe_d2_038_vsp_basefill_038(vsp_basefill_038):
    return _base_universe_d2(vsp_basefill_038, 38)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_038_vsp_basefill_038'] = {'inputs': ['vsp_basefill_038'], 'func': vsp_base_universe_d2_038_vsp_basefill_038}


def vsp_base_universe_d2_039_vsp_basefill_039(vsp_basefill_039):
    return _base_universe_d2(vsp_basefill_039, 39)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_039_vsp_basefill_039'] = {'inputs': ['vsp_basefill_039'], 'func': vsp_base_universe_d2_039_vsp_basefill_039}


def vsp_base_universe_d2_040_vsp_basefill_040(vsp_basefill_040):
    return _base_universe_d2(vsp_basefill_040, 40)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_040_vsp_basefill_040'] = {'inputs': ['vsp_basefill_040'], 'func': vsp_base_universe_d2_040_vsp_basefill_040}


def vsp_base_universe_d2_041_vsp_basefill_041(vsp_basefill_041):
    return _base_universe_d2(vsp_basefill_041, 41)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_041_vsp_basefill_041'] = {'inputs': ['vsp_basefill_041'], 'func': vsp_base_universe_d2_041_vsp_basefill_041}


def vsp_base_universe_d2_042_vsp_basefill_042(vsp_basefill_042):
    return _base_universe_d2(vsp_basefill_042, 42)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_042_vsp_basefill_042'] = {'inputs': ['vsp_basefill_042'], 'func': vsp_base_universe_d2_042_vsp_basefill_042}


def vsp_base_universe_d2_043_vsp_basefill_043(vsp_basefill_043):
    return _base_universe_d2(vsp_basefill_043, 43)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_043_vsp_basefill_043'] = {'inputs': ['vsp_basefill_043'], 'func': vsp_base_universe_d2_043_vsp_basefill_043}


def vsp_base_universe_d2_044_vsp_basefill_044(vsp_basefill_044):
    return _base_universe_d2(vsp_basefill_044, 44)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_044_vsp_basefill_044'] = {'inputs': ['vsp_basefill_044'], 'func': vsp_base_universe_d2_044_vsp_basefill_044}


def vsp_base_universe_d2_045_vsp_basefill_045(vsp_basefill_045):
    return _base_universe_d2(vsp_basefill_045, 45)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_045_vsp_basefill_045'] = {'inputs': ['vsp_basefill_045'], 'func': vsp_base_universe_d2_045_vsp_basefill_045}


def vsp_base_universe_d2_046_vsp_basefill_046(vsp_basefill_046):
    return _base_universe_d2(vsp_basefill_046, 46)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_046_vsp_basefill_046'] = {'inputs': ['vsp_basefill_046'], 'func': vsp_base_universe_d2_046_vsp_basefill_046}


def vsp_base_universe_d2_047_vsp_basefill_047(vsp_basefill_047):
    return _base_universe_d2(vsp_basefill_047, 47)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_047_vsp_basefill_047'] = {'inputs': ['vsp_basefill_047'], 'func': vsp_base_universe_d2_047_vsp_basefill_047}


def vsp_base_universe_d2_048_vsp_basefill_048(vsp_basefill_048):
    return _base_universe_d2(vsp_basefill_048, 48)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_048_vsp_basefill_048'] = {'inputs': ['vsp_basefill_048'], 'func': vsp_base_universe_d2_048_vsp_basefill_048}


def vsp_base_universe_d2_049_vsp_basefill_049(vsp_basefill_049):
    return _base_universe_d2(vsp_basefill_049, 49)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_049_vsp_basefill_049'] = {'inputs': ['vsp_basefill_049'], 'func': vsp_base_universe_d2_049_vsp_basefill_049}


def vsp_base_universe_d2_050_vsp_basefill_050(vsp_basefill_050):
    return _base_universe_d2(vsp_basefill_050, 50)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_050_vsp_basefill_050'] = {'inputs': ['vsp_basefill_050'], 'func': vsp_base_universe_d2_050_vsp_basefill_050}


def vsp_base_universe_d2_051_vsp_basefill_051(vsp_basefill_051):
    return _base_universe_d2(vsp_basefill_051, 51)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_051_vsp_basefill_051'] = {'inputs': ['vsp_basefill_051'], 'func': vsp_base_universe_d2_051_vsp_basefill_051}


def vsp_base_universe_d2_052_vsp_basefill_052(vsp_basefill_052):
    return _base_universe_d2(vsp_basefill_052, 52)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_052_vsp_basefill_052'] = {'inputs': ['vsp_basefill_052'], 'func': vsp_base_universe_d2_052_vsp_basefill_052}


def vsp_base_universe_d2_053_vsp_basefill_053(vsp_basefill_053):
    return _base_universe_d2(vsp_basefill_053, 53)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_053_vsp_basefill_053'] = {'inputs': ['vsp_basefill_053'], 'func': vsp_base_universe_d2_053_vsp_basefill_053}


def vsp_base_universe_d2_054_vsp_basefill_054(vsp_basefill_054):
    return _base_universe_d2(vsp_basefill_054, 54)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_054_vsp_basefill_054'] = {'inputs': ['vsp_basefill_054'], 'func': vsp_base_universe_d2_054_vsp_basefill_054}


def vsp_base_universe_d2_055_vsp_basefill_055(vsp_basefill_055):
    return _base_universe_d2(vsp_basefill_055, 55)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_055_vsp_basefill_055'] = {'inputs': ['vsp_basefill_055'], 'func': vsp_base_universe_d2_055_vsp_basefill_055}


def vsp_base_universe_d2_056_vsp_basefill_056(vsp_basefill_056):
    return _base_universe_d2(vsp_basefill_056, 56)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_056_vsp_basefill_056'] = {'inputs': ['vsp_basefill_056'], 'func': vsp_base_universe_d2_056_vsp_basefill_056}


def vsp_base_universe_d2_057_vsp_basefill_057(vsp_basefill_057):
    return _base_universe_d2(vsp_basefill_057, 57)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_057_vsp_basefill_057'] = {'inputs': ['vsp_basefill_057'], 'func': vsp_base_universe_d2_057_vsp_basefill_057}


def vsp_base_universe_d2_058_vsp_basefill_058(vsp_basefill_058):
    return _base_universe_d2(vsp_basefill_058, 58)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_058_vsp_basefill_058'] = {'inputs': ['vsp_basefill_058'], 'func': vsp_base_universe_d2_058_vsp_basefill_058}


def vsp_base_universe_d2_059_vsp_basefill_059(vsp_basefill_059):
    return _base_universe_d2(vsp_basefill_059, 59)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_059_vsp_basefill_059'] = {'inputs': ['vsp_basefill_059'], 'func': vsp_base_universe_d2_059_vsp_basefill_059}


def vsp_base_universe_d2_060_vsp_basefill_060(vsp_basefill_060):
    return _base_universe_d2(vsp_basefill_060, 60)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_060_vsp_basefill_060'] = {'inputs': ['vsp_basefill_060'], 'func': vsp_base_universe_d2_060_vsp_basefill_060}


def vsp_base_universe_d2_061_vsp_basefill_061(vsp_basefill_061):
    return _base_universe_d2(vsp_basefill_061, 61)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_061_vsp_basefill_061'] = {'inputs': ['vsp_basefill_061'], 'func': vsp_base_universe_d2_061_vsp_basefill_061}


def vsp_base_universe_d2_062_vsp_basefill_062(vsp_basefill_062):
    return _base_universe_d2(vsp_basefill_062, 62)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_062_vsp_basefill_062'] = {'inputs': ['vsp_basefill_062'], 'func': vsp_base_universe_d2_062_vsp_basefill_062}


def vsp_base_universe_d2_063_vsp_basefill_063(vsp_basefill_063):
    return _base_universe_d2(vsp_basefill_063, 63)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_063_vsp_basefill_063'] = {'inputs': ['vsp_basefill_063'], 'func': vsp_base_universe_d2_063_vsp_basefill_063}


def vsp_base_universe_d2_064_vsp_basefill_064(vsp_basefill_064):
    return _base_universe_d2(vsp_basefill_064, 64)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_064_vsp_basefill_064'] = {'inputs': ['vsp_basefill_064'], 'func': vsp_base_universe_d2_064_vsp_basefill_064}


def vsp_base_universe_d2_065_vsp_basefill_065(vsp_basefill_065):
    return _base_universe_d2(vsp_basefill_065, 65)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_065_vsp_basefill_065'] = {'inputs': ['vsp_basefill_065'], 'func': vsp_base_universe_d2_065_vsp_basefill_065}


def vsp_base_universe_d2_066_vsp_basefill_066(vsp_basefill_066):
    return _base_universe_d2(vsp_basefill_066, 66)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_066_vsp_basefill_066'] = {'inputs': ['vsp_basefill_066'], 'func': vsp_base_universe_d2_066_vsp_basefill_066}


def vsp_base_universe_d2_067_vsp_basefill_067(vsp_basefill_067):
    return _base_universe_d2(vsp_basefill_067, 67)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_067_vsp_basefill_067'] = {'inputs': ['vsp_basefill_067'], 'func': vsp_base_universe_d2_067_vsp_basefill_067}


def vsp_base_universe_d2_068_vsp_basefill_068(vsp_basefill_068):
    return _base_universe_d2(vsp_basefill_068, 68)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_068_vsp_basefill_068'] = {'inputs': ['vsp_basefill_068'], 'func': vsp_base_universe_d2_068_vsp_basefill_068}


def vsp_base_universe_d2_069_vsp_basefill_069(vsp_basefill_069):
    return _base_universe_d2(vsp_basefill_069, 69)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_069_vsp_basefill_069'] = {'inputs': ['vsp_basefill_069'], 'func': vsp_base_universe_d2_069_vsp_basefill_069}


def vsp_base_universe_d2_070_vsp_basefill_070(vsp_basefill_070):
    return _base_universe_d2(vsp_basefill_070, 70)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_070_vsp_basefill_070'] = {'inputs': ['vsp_basefill_070'], 'func': vsp_base_universe_d2_070_vsp_basefill_070}


def vsp_base_universe_d2_071_vsp_basefill_071(vsp_basefill_071):
    return _base_universe_d2(vsp_basefill_071, 71)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_071_vsp_basefill_071'] = {'inputs': ['vsp_basefill_071'], 'func': vsp_base_universe_d2_071_vsp_basefill_071}


def vsp_base_universe_d2_072_vsp_basefill_072(vsp_basefill_072):
    return _base_universe_d2(vsp_basefill_072, 72)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_072_vsp_basefill_072'] = {'inputs': ['vsp_basefill_072'], 'func': vsp_base_universe_d2_072_vsp_basefill_072}


def vsp_base_universe_d2_073_vsp_basefill_073(vsp_basefill_073):
    return _base_universe_d2(vsp_basefill_073, 73)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_073_vsp_basefill_073'] = {'inputs': ['vsp_basefill_073'], 'func': vsp_base_universe_d2_073_vsp_basefill_073}


def vsp_base_universe_d2_074_vsp_basefill_074(vsp_basefill_074):
    return _base_universe_d2(vsp_basefill_074, 74)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_074_vsp_basefill_074'] = {'inputs': ['vsp_basefill_074'], 'func': vsp_base_universe_d2_074_vsp_basefill_074}


def vsp_base_universe_d2_075_vsp_basefill_075(vsp_basefill_075):
    return _base_universe_d2(vsp_basefill_075, 75)
VSP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vsp_base_universe_d2_075_vsp_basefill_075'] = {'inputs': ['vsp_basefill_075'], 'func': vsp_base_universe_d2_075_vsp_basefill_075}
