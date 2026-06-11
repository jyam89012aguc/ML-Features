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



def vif_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def vif_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def vif_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def vif_154_vif_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def vif_155_vif_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















VELOCITY_INFLECTION_REGISTRY_2ND_DERIVATIVES = {
    'vif_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': vif_001_return_decay_roc_1},
    'vif_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': vif_007_return_decay_roc_5},
    'vif_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': vif_013_return_decay_roc_42},
    'vif_154_vif_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': vif_154_vif_019_return_decay_42_019_roc_126},
    'vif_155_vif_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': vif_155_vif_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vi_replacement_d2_001(vi_replacement_001):
    feature = _clean(vi_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_001'] = {'inputs': ['vi_replacement_001'], 'func': vi_replacement_d2_001}


def vi_replacement_d2_002(vi_replacement_002):
    feature = _clean(vi_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_002'] = {'inputs': ['vi_replacement_002'], 'func': vi_replacement_d2_002}


def vi_replacement_d2_003(vi_replacement_003):
    feature = _clean(vi_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_003'] = {'inputs': ['vi_replacement_003'], 'func': vi_replacement_d2_003}


def vi_replacement_d2_004(vi_replacement_004):
    feature = _clean(vi_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_004'] = {'inputs': ['vi_replacement_004'], 'func': vi_replacement_d2_004}


def vi_replacement_d2_005(vi_replacement_005):
    feature = _clean(vi_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_005'] = {'inputs': ['vi_replacement_005'], 'func': vi_replacement_d2_005}


def vi_replacement_d2_006(vi_replacement_006):
    feature = _clean(vi_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_006'] = {'inputs': ['vi_replacement_006'], 'func': vi_replacement_d2_006}


def vi_replacement_d2_007(vi_replacement_007):
    feature = _clean(vi_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_007'] = {'inputs': ['vi_replacement_007'], 'func': vi_replacement_d2_007}


def vi_replacement_d2_008(vi_replacement_008):
    feature = _clean(vi_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_008'] = {'inputs': ['vi_replacement_008'], 'func': vi_replacement_d2_008}


def vi_replacement_d2_009(vi_replacement_009):
    feature = _clean(vi_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_009'] = {'inputs': ['vi_replacement_009'], 'func': vi_replacement_d2_009}


def vi_replacement_d2_010(vi_replacement_010):
    feature = _clean(vi_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_010'] = {'inputs': ['vi_replacement_010'], 'func': vi_replacement_d2_010}


def vi_replacement_d2_011(vi_replacement_011):
    feature = _clean(vi_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_011'] = {'inputs': ['vi_replacement_011'], 'func': vi_replacement_d2_011}


def vi_replacement_d2_012(vi_replacement_012):
    feature = _clean(vi_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_012'] = {'inputs': ['vi_replacement_012'], 'func': vi_replacement_d2_012}


def vi_replacement_d2_013(vi_replacement_013):
    feature = _clean(vi_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_013'] = {'inputs': ['vi_replacement_013'], 'func': vi_replacement_d2_013}


def vi_replacement_d2_014(vi_replacement_014):
    feature = _clean(vi_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_014'] = {'inputs': ['vi_replacement_014'], 'func': vi_replacement_d2_014}


def vi_replacement_d2_015(vi_replacement_015):
    feature = _clean(vi_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_015'] = {'inputs': ['vi_replacement_015'], 'func': vi_replacement_d2_015}


def vi_replacement_d2_016(vi_replacement_016):
    feature = _clean(vi_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_016'] = {'inputs': ['vi_replacement_016'], 'func': vi_replacement_d2_016}


def vi_replacement_d2_017(vi_replacement_017):
    feature = _clean(vi_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_017'] = {'inputs': ['vi_replacement_017'], 'func': vi_replacement_d2_017}


def vi_replacement_d2_018(vi_replacement_018):
    feature = _clean(vi_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_018'] = {'inputs': ['vi_replacement_018'], 'func': vi_replacement_d2_018}


def vi_replacement_d2_019(vi_replacement_019):
    feature = _clean(vi_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_019'] = {'inputs': ['vi_replacement_019'], 'func': vi_replacement_d2_019}


def vi_replacement_d2_020(vi_replacement_020):
    feature = _clean(vi_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_020'] = {'inputs': ['vi_replacement_020'], 'func': vi_replacement_d2_020}


def vi_replacement_d2_021(vi_replacement_021):
    feature = _clean(vi_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_021'] = {'inputs': ['vi_replacement_021'], 'func': vi_replacement_d2_021}


def vi_replacement_d2_022(vi_replacement_022):
    feature = _clean(vi_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_022'] = {'inputs': ['vi_replacement_022'], 'func': vi_replacement_d2_022}


def vi_replacement_d2_023(vi_replacement_023):
    feature = _clean(vi_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_023'] = {'inputs': ['vi_replacement_023'], 'func': vi_replacement_d2_023}


def vi_replacement_d2_024(vi_replacement_024):
    feature = _clean(vi_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_024'] = {'inputs': ['vi_replacement_024'], 'func': vi_replacement_d2_024}


def vi_replacement_d2_025(vi_replacement_025):
    feature = _clean(vi_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_025'] = {'inputs': ['vi_replacement_025'], 'func': vi_replacement_d2_025}


def vi_replacement_d2_026(vi_replacement_026):
    feature = _clean(vi_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_026'] = {'inputs': ['vi_replacement_026'], 'func': vi_replacement_d2_026}


def vi_replacement_d2_027(vi_replacement_027):
    feature = _clean(vi_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_027'] = {'inputs': ['vi_replacement_027'], 'func': vi_replacement_d2_027}


def vi_replacement_d2_028(vi_replacement_028):
    feature = _clean(vi_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_028'] = {'inputs': ['vi_replacement_028'], 'func': vi_replacement_d2_028}


def vi_replacement_d2_029(vi_replacement_029):
    feature = _clean(vi_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_029'] = {'inputs': ['vi_replacement_029'], 'func': vi_replacement_d2_029}


def vi_replacement_d2_030(vi_replacement_030):
    feature = _clean(vi_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_030'] = {'inputs': ['vi_replacement_030'], 'func': vi_replacement_d2_030}


def vi_replacement_d2_031(vi_replacement_031):
    feature = _clean(vi_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_031'] = {'inputs': ['vi_replacement_031'], 'func': vi_replacement_d2_031}


def vi_replacement_d2_032(vi_replacement_032):
    feature = _clean(vi_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_032'] = {'inputs': ['vi_replacement_032'], 'func': vi_replacement_d2_032}


def vi_replacement_d2_033(vi_replacement_033):
    feature = _clean(vi_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_033'] = {'inputs': ['vi_replacement_033'], 'func': vi_replacement_d2_033}


def vi_replacement_d2_034(vi_replacement_034):
    feature = _clean(vi_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_034'] = {'inputs': ['vi_replacement_034'], 'func': vi_replacement_d2_034}


def vi_replacement_d2_035(vi_replacement_035):
    feature = _clean(vi_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_035'] = {'inputs': ['vi_replacement_035'], 'func': vi_replacement_d2_035}


def vi_replacement_d2_036(vi_replacement_036):
    feature = _clean(vi_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_036'] = {'inputs': ['vi_replacement_036'], 'func': vi_replacement_d2_036}


def vi_replacement_d2_037(vi_replacement_037):
    feature = _clean(vi_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_037'] = {'inputs': ['vi_replacement_037'], 'func': vi_replacement_d2_037}


def vi_replacement_d2_038(vi_replacement_038):
    feature = _clean(vi_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_038'] = {'inputs': ['vi_replacement_038'], 'func': vi_replacement_d2_038}


def vi_replacement_d2_039(vi_replacement_039):
    feature = _clean(vi_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_039'] = {'inputs': ['vi_replacement_039'], 'func': vi_replacement_d2_039}


def vi_replacement_d2_040(vi_replacement_040):
    feature = _clean(vi_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_040'] = {'inputs': ['vi_replacement_040'], 'func': vi_replacement_d2_040}


def vi_replacement_d2_041(vi_replacement_041):
    feature = _clean(vi_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_041'] = {'inputs': ['vi_replacement_041'], 'func': vi_replacement_d2_041}


def vi_replacement_d2_042(vi_replacement_042):
    feature = _clean(vi_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_042'] = {'inputs': ['vi_replacement_042'], 'func': vi_replacement_d2_042}


def vi_replacement_d2_043(vi_replacement_043):
    feature = _clean(vi_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_043'] = {'inputs': ['vi_replacement_043'], 'func': vi_replacement_d2_043}


def vi_replacement_d2_044(vi_replacement_044):
    feature = _clean(vi_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_044'] = {'inputs': ['vi_replacement_044'], 'func': vi_replacement_d2_044}


def vi_replacement_d2_045(vi_replacement_045):
    feature = _clean(vi_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_045'] = {'inputs': ['vi_replacement_045'], 'func': vi_replacement_d2_045}


def vi_replacement_d2_046(vi_replacement_046):
    feature = _clean(vi_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_046'] = {'inputs': ['vi_replacement_046'], 'func': vi_replacement_d2_046}


def vi_replacement_d2_047(vi_replacement_047):
    feature = _clean(vi_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_047'] = {'inputs': ['vi_replacement_047'], 'func': vi_replacement_d2_047}


def vi_replacement_d2_048(vi_replacement_048):
    feature = _clean(vi_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_048'] = {'inputs': ['vi_replacement_048'], 'func': vi_replacement_d2_048}


def vi_replacement_d2_049(vi_replacement_049):
    feature = _clean(vi_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_049'] = {'inputs': ['vi_replacement_049'], 'func': vi_replacement_d2_049}


def vi_replacement_d2_050(vi_replacement_050):
    feature = _clean(vi_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_050'] = {'inputs': ['vi_replacement_050'], 'func': vi_replacement_d2_050}


def vi_replacement_d2_051(vi_replacement_051):
    feature = _clean(vi_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_051'] = {'inputs': ['vi_replacement_051'], 'func': vi_replacement_d2_051}


def vi_replacement_d2_052(vi_replacement_052):
    feature = _clean(vi_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_052'] = {'inputs': ['vi_replacement_052'], 'func': vi_replacement_d2_052}


def vi_replacement_d2_053(vi_replacement_053):
    feature = _clean(vi_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_053'] = {'inputs': ['vi_replacement_053'], 'func': vi_replacement_d2_053}


def vi_replacement_d2_054(vi_replacement_054):
    feature = _clean(vi_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_054'] = {'inputs': ['vi_replacement_054'], 'func': vi_replacement_d2_054}


def vi_replacement_d2_055(vi_replacement_055):
    feature = _clean(vi_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_055'] = {'inputs': ['vi_replacement_055'], 'func': vi_replacement_d2_055}


def vi_replacement_d2_056(vi_replacement_056):
    feature = _clean(vi_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_056'] = {'inputs': ['vi_replacement_056'], 'func': vi_replacement_d2_056}


def vi_replacement_d2_057(vi_replacement_057):
    feature = _clean(vi_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_057'] = {'inputs': ['vi_replacement_057'], 'func': vi_replacement_d2_057}


def vi_replacement_d2_058(vi_replacement_058):
    feature = _clean(vi_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_058'] = {'inputs': ['vi_replacement_058'], 'func': vi_replacement_d2_058}


def vi_replacement_d2_059(vi_replacement_059):
    feature = _clean(vi_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_059'] = {'inputs': ['vi_replacement_059'], 'func': vi_replacement_d2_059}


def vi_replacement_d2_060(vi_replacement_060):
    feature = _clean(vi_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_060'] = {'inputs': ['vi_replacement_060'], 'func': vi_replacement_d2_060}


def vi_replacement_d2_061(vi_replacement_061):
    feature = _clean(vi_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_061'] = {'inputs': ['vi_replacement_061'], 'func': vi_replacement_d2_061}


def vi_replacement_d2_062(vi_replacement_062):
    feature = _clean(vi_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_062'] = {'inputs': ['vi_replacement_062'], 'func': vi_replacement_d2_062}


def vi_replacement_d2_063(vi_replacement_063):
    feature = _clean(vi_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_063'] = {'inputs': ['vi_replacement_063'], 'func': vi_replacement_d2_063}


def vi_replacement_d2_064(vi_replacement_064):
    feature = _clean(vi_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_064'] = {'inputs': ['vi_replacement_064'], 'func': vi_replacement_d2_064}


def vi_replacement_d2_065(vi_replacement_065):
    feature = _clean(vi_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_065'] = {'inputs': ['vi_replacement_065'], 'func': vi_replacement_d2_065}


def vi_replacement_d2_066(vi_replacement_066):
    feature = _clean(vi_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_066'] = {'inputs': ['vi_replacement_066'], 'func': vi_replacement_d2_066}


def vi_replacement_d2_067(vi_replacement_067):
    feature = _clean(vi_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_067'] = {'inputs': ['vi_replacement_067'], 'func': vi_replacement_d2_067}


def vi_replacement_d2_068(vi_replacement_068):
    feature = _clean(vi_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_068'] = {'inputs': ['vi_replacement_068'], 'func': vi_replacement_d2_068}


def vi_replacement_d2_069(vi_replacement_069):
    feature = _clean(vi_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_069'] = {'inputs': ['vi_replacement_069'], 'func': vi_replacement_d2_069}


def vi_replacement_d2_070(vi_replacement_070):
    feature = _clean(vi_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_070'] = {'inputs': ['vi_replacement_070'], 'func': vi_replacement_d2_070}


def vi_replacement_d2_071(vi_replacement_071):
    feature = _clean(vi_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_071'] = {'inputs': ['vi_replacement_071'], 'func': vi_replacement_d2_071}


def vi_replacement_d2_072(vi_replacement_072):
    feature = _clean(vi_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_072'] = {'inputs': ['vi_replacement_072'], 'func': vi_replacement_d2_072}


def vi_replacement_d2_073(vi_replacement_073):
    feature = _clean(vi_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_073'] = {'inputs': ['vi_replacement_073'], 'func': vi_replacement_d2_073}


def vi_replacement_d2_074(vi_replacement_074):
    feature = _clean(vi_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_074'] = {'inputs': ['vi_replacement_074'], 'func': vi_replacement_d2_074}


def vi_replacement_d2_075(vi_replacement_075):
    feature = _clean(vi_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_075'] = {'inputs': ['vi_replacement_075'], 'func': vi_replacement_d2_075}


def vi_replacement_d2_076(vi_replacement_076):
    feature = _clean(vi_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_076'] = {'inputs': ['vi_replacement_076'], 'func': vi_replacement_d2_076}


def vi_replacement_d2_077(vi_replacement_077):
    feature = _clean(vi_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_077'] = {'inputs': ['vi_replacement_077'], 'func': vi_replacement_d2_077}


def vi_replacement_d2_078(vi_replacement_078):
    feature = _clean(vi_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_078'] = {'inputs': ['vi_replacement_078'], 'func': vi_replacement_d2_078}


def vi_replacement_d2_079(vi_replacement_079):
    feature = _clean(vi_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_079'] = {'inputs': ['vi_replacement_079'], 'func': vi_replacement_d2_079}


def vi_replacement_d2_080(vi_replacement_080):
    feature = _clean(vi_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_080'] = {'inputs': ['vi_replacement_080'], 'func': vi_replacement_d2_080}


def vi_replacement_d2_081(vi_replacement_081):
    feature = _clean(vi_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_081'] = {'inputs': ['vi_replacement_081'], 'func': vi_replacement_d2_081}


def vi_replacement_d2_082(vi_replacement_082):
    feature = _clean(vi_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_082'] = {'inputs': ['vi_replacement_082'], 'func': vi_replacement_d2_082}


def vi_replacement_d2_083(vi_replacement_083):
    feature = _clean(vi_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_083'] = {'inputs': ['vi_replacement_083'], 'func': vi_replacement_d2_083}


def vi_replacement_d2_084(vi_replacement_084):
    feature = _clean(vi_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_084'] = {'inputs': ['vi_replacement_084'], 'func': vi_replacement_d2_084}


def vi_replacement_d2_085(vi_replacement_085):
    feature = _clean(vi_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_085'] = {'inputs': ['vi_replacement_085'], 'func': vi_replacement_d2_085}


def vi_replacement_d2_086(vi_replacement_086):
    feature = _clean(vi_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_086'] = {'inputs': ['vi_replacement_086'], 'func': vi_replacement_d2_086}


def vi_replacement_d2_087(vi_replacement_087):
    feature = _clean(vi_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_087'] = {'inputs': ['vi_replacement_087'], 'func': vi_replacement_d2_087}


def vi_replacement_d2_088(vi_replacement_088):
    feature = _clean(vi_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_088'] = {'inputs': ['vi_replacement_088'], 'func': vi_replacement_d2_088}


def vi_replacement_d2_089(vi_replacement_089):
    feature = _clean(vi_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_089'] = {'inputs': ['vi_replacement_089'], 'func': vi_replacement_d2_089}


def vi_replacement_d2_090(vi_replacement_090):
    feature = _clean(vi_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_090'] = {'inputs': ['vi_replacement_090'], 'func': vi_replacement_d2_090}


def vi_replacement_d2_091(vi_replacement_091):
    feature = _clean(vi_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_091'] = {'inputs': ['vi_replacement_091'], 'func': vi_replacement_d2_091}


def vi_replacement_d2_092(vi_replacement_092):
    feature = _clean(vi_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_092'] = {'inputs': ['vi_replacement_092'], 'func': vi_replacement_d2_092}


def vi_replacement_d2_093(vi_replacement_093):
    feature = _clean(vi_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_093'] = {'inputs': ['vi_replacement_093'], 'func': vi_replacement_d2_093}


def vi_replacement_d2_094(vi_replacement_094):
    feature = _clean(vi_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_094'] = {'inputs': ['vi_replacement_094'], 'func': vi_replacement_d2_094}


def vi_replacement_d2_095(vi_replacement_095):
    feature = _clean(vi_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_095'] = {'inputs': ['vi_replacement_095'], 'func': vi_replacement_d2_095}


def vi_replacement_d2_096(vi_replacement_096):
    feature = _clean(vi_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_096'] = {'inputs': ['vi_replacement_096'], 'func': vi_replacement_d2_096}


def vi_replacement_d2_097(vi_replacement_097):
    feature = _clean(vi_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_097'] = {'inputs': ['vi_replacement_097'], 'func': vi_replacement_d2_097}


def vi_replacement_d2_098(vi_replacement_098):
    feature = _clean(vi_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_098'] = {'inputs': ['vi_replacement_098'], 'func': vi_replacement_d2_098}


def vi_replacement_d2_099(vi_replacement_099):
    feature = _clean(vi_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_099'] = {'inputs': ['vi_replacement_099'], 'func': vi_replacement_d2_099}


def vi_replacement_d2_100(vi_replacement_100):
    feature = _clean(vi_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_100'] = {'inputs': ['vi_replacement_100'], 'func': vi_replacement_d2_100}


def vi_replacement_d2_101(vi_replacement_101):
    feature = _clean(vi_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_101'] = {'inputs': ['vi_replacement_101'], 'func': vi_replacement_d2_101}


def vi_replacement_d2_102(vi_replacement_102):
    feature = _clean(vi_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_102'] = {'inputs': ['vi_replacement_102'], 'func': vi_replacement_d2_102}


def vi_replacement_d2_103(vi_replacement_103):
    feature = _clean(vi_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_103'] = {'inputs': ['vi_replacement_103'], 'func': vi_replacement_d2_103}


def vi_replacement_d2_104(vi_replacement_104):
    feature = _clean(vi_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_104'] = {'inputs': ['vi_replacement_104'], 'func': vi_replacement_d2_104}


def vi_replacement_d2_105(vi_replacement_105):
    feature = _clean(vi_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_105'] = {'inputs': ['vi_replacement_105'], 'func': vi_replacement_d2_105}


def vi_replacement_d2_106(vi_replacement_106):
    feature = _clean(vi_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_106'] = {'inputs': ['vi_replacement_106'], 'func': vi_replacement_d2_106}


def vi_replacement_d2_107(vi_replacement_107):
    feature = _clean(vi_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_107'] = {'inputs': ['vi_replacement_107'], 'func': vi_replacement_d2_107}


def vi_replacement_d2_108(vi_replacement_108):
    feature = _clean(vi_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_108'] = {'inputs': ['vi_replacement_108'], 'func': vi_replacement_d2_108}


def vi_replacement_d2_109(vi_replacement_109):
    feature = _clean(vi_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_109'] = {'inputs': ['vi_replacement_109'], 'func': vi_replacement_d2_109}


def vi_replacement_d2_110(vi_replacement_110):
    feature = _clean(vi_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_110'] = {'inputs': ['vi_replacement_110'], 'func': vi_replacement_d2_110}


def vi_replacement_d2_111(vi_replacement_111):
    feature = _clean(vi_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_111'] = {'inputs': ['vi_replacement_111'], 'func': vi_replacement_d2_111}


def vi_replacement_d2_112(vi_replacement_112):
    feature = _clean(vi_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_112'] = {'inputs': ['vi_replacement_112'], 'func': vi_replacement_d2_112}


def vi_replacement_d2_113(vi_replacement_113):
    feature = _clean(vi_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_113'] = {'inputs': ['vi_replacement_113'], 'func': vi_replacement_d2_113}


def vi_replacement_d2_114(vi_replacement_114):
    feature = _clean(vi_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_114'] = {'inputs': ['vi_replacement_114'], 'func': vi_replacement_d2_114}


def vi_replacement_d2_115(vi_replacement_115):
    feature = _clean(vi_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_115'] = {'inputs': ['vi_replacement_115'], 'func': vi_replacement_d2_115}


def vi_replacement_d2_116(vi_replacement_116):
    feature = _clean(vi_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_116'] = {'inputs': ['vi_replacement_116'], 'func': vi_replacement_d2_116}


def vi_replacement_d2_117(vi_replacement_117):
    feature = _clean(vi_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_117'] = {'inputs': ['vi_replacement_117'], 'func': vi_replacement_d2_117}


def vi_replacement_d2_118(vi_replacement_118):
    feature = _clean(vi_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_118'] = {'inputs': ['vi_replacement_118'], 'func': vi_replacement_d2_118}


def vi_replacement_d2_119(vi_replacement_119):
    feature = _clean(vi_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_119'] = {'inputs': ['vi_replacement_119'], 'func': vi_replacement_d2_119}


def vi_replacement_d2_120(vi_replacement_120):
    feature = _clean(vi_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_120'] = {'inputs': ['vi_replacement_120'], 'func': vi_replacement_d2_120}


def vi_replacement_d2_121(vi_replacement_121):
    feature = _clean(vi_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_121'] = {'inputs': ['vi_replacement_121'], 'func': vi_replacement_d2_121}


def vi_replacement_d2_122(vi_replacement_122):
    feature = _clean(vi_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_122'] = {'inputs': ['vi_replacement_122'], 'func': vi_replacement_d2_122}


def vi_replacement_d2_123(vi_replacement_123):
    feature = _clean(vi_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_123'] = {'inputs': ['vi_replacement_123'], 'func': vi_replacement_d2_123}


def vi_replacement_d2_124(vi_replacement_124):
    feature = _clean(vi_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_124'] = {'inputs': ['vi_replacement_124'], 'func': vi_replacement_d2_124}


def vi_replacement_d2_125(vi_replacement_125):
    feature = _clean(vi_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_125'] = {'inputs': ['vi_replacement_125'], 'func': vi_replacement_d2_125}


def vi_replacement_d2_126(vi_replacement_126):
    feature = _clean(vi_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_126'] = {'inputs': ['vi_replacement_126'], 'func': vi_replacement_d2_126}


def vi_replacement_d2_127(vi_replacement_127):
    feature = _clean(vi_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_127'] = {'inputs': ['vi_replacement_127'], 'func': vi_replacement_d2_127}


def vi_replacement_d2_128(vi_replacement_128):
    feature = _clean(vi_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_128'] = {'inputs': ['vi_replacement_128'], 'func': vi_replacement_d2_128}


def vi_replacement_d2_129(vi_replacement_129):
    feature = _clean(vi_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_129'] = {'inputs': ['vi_replacement_129'], 'func': vi_replacement_d2_129}


def vi_replacement_d2_130(vi_replacement_130):
    feature = _clean(vi_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_130'] = {'inputs': ['vi_replacement_130'], 'func': vi_replacement_d2_130}


def vi_replacement_d2_131(vi_replacement_131):
    feature = _clean(vi_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_131'] = {'inputs': ['vi_replacement_131'], 'func': vi_replacement_d2_131}


def vi_replacement_d2_132(vi_replacement_132):
    feature = _clean(vi_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_132'] = {'inputs': ['vi_replacement_132'], 'func': vi_replacement_d2_132}


def vi_replacement_d2_133(vi_replacement_133):
    feature = _clean(vi_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_133'] = {'inputs': ['vi_replacement_133'], 'func': vi_replacement_d2_133}


def vi_replacement_d2_134(vi_replacement_134):
    feature = _clean(vi_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_134'] = {'inputs': ['vi_replacement_134'], 'func': vi_replacement_d2_134}


def vi_replacement_d2_135(vi_replacement_135):
    feature = _clean(vi_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_135'] = {'inputs': ['vi_replacement_135'], 'func': vi_replacement_d2_135}


def vi_replacement_d2_136(vi_replacement_136):
    feature = _clean(vi_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_136'] = {'inputs': ['vi_replacement_136'], 'func': vi_replacement_d2_136}


def vi_replacement_d2_137(vi_replacement_137):
    feature = _clean(vi_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_137'] = {'inputs': ['vi_replacement_137'], 'func': vi_replacement_d2_137}


def vi_replacement_d2_138(vi_replacement_138):
    feature = _clean(vi_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_138'] = {'inputs': ['vi_replacement_138'], 'func': vi_replacement_d2_138}


def vi_replacement_d2_139(vi_replacement_139):
    feature = _clean(vi_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_139'] = {'inputs': ['vi_replacement_139'], 'func': vi_replacement_d2_139}


def vi_replacement_d2_140(vi_replacement_140):
    feature = _clean(vi_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_140'] = {'inputs': ['vi_replacement_140'], 'func': vi_replacement_d2_140}


def vi_replacement_d2_141(vi_replacement_141):
    feature = _clean(vi_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_141'] = {'inputs': ['vi_replacement_141'], 'func': vi_replacement_d2_141}


def vi_replacement_d2_142(vi_replacement_142):
    feature = _clean(vi_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_142'] = {'inputs': ['vi_replacement_142'], 'func': vi_replacement_d2_142}


def vi_replacement_d2_143(vi_replacement_143):
    feature = _clean(vi_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_143'] = {'inputs': ['vi_replacement_143'], 'func': vi_replacement_d2_143}


def vi_replacement_d2_144(vi_replacement_144):
    feature = _clean(vi_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_144'] = {'inputs': ['vi_replacement_144'], 'func': vi_replacement_d2_144}


def vi_replacement_d2_145(vi_replacement_145):
    feature = _clean(vi_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_145'] = {'inputs': ['vi_replacement_145'], 'func': vi_replacement_d2_145}


def vi_replacement_d2_146(vi_replacement_146):
    feature = _clean(vi_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_146'] = {'inputs': ['vi_replacement_146'], 'func': vi_replacement_d2_146}


def vi_replacement_d2_147(vi_replacement_147):
    feature = _clean(vi_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_147'] = {'inputs': ['vi_replacement_147'], 'func': vi_replacement_d2_147}


def vi_replacement_d2_148(vi_replacement_148):
    feature = _clean(vi_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_148'] = {'inputs': ['vi_replacement_148'], 'func': vi_replacement_d2_148}


def vi_replacement_d2_149(vi_replacement_149):
    feature = _clean(vi_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_149'] = {'inputs': ['vi_replacement_149'], 'func': vi_replacement_d2_149}


def vi_replacement_d2_150(vi_replacement_150):
    feature = _clean(vi_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_150'] = {'inputs': ['vi_replacement_150'], 'func': vi_replacement_d2_150}


def vi_replacement_d2_151(vi_replacement_151):
    feature = _clean(vi_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_151'] = {'inputs': ['vi_replacement_151'], 'func': vi_replacement_d2_151}


def vi_replacement_d2_152(vi_replacement_152):
    feature = _clean(vi_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_152'] = {'inputs': ['vi_replacement_152'], 'func': vi_replacement_d2_152}


def vi_replacement_d2_153(vi_replacement_153):
    feature = _clean(vi_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_153'] = {'inputs': ['vi_replacement_153'], 'func': vi_replacement_d2_153}


def vi_replacement_d2_154(vi_replacement_154):
    feature = _clean(vi_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_154'] = {'inputs': ['vi_replacement_154'], 'func': vi_replacement_d2_154}


def vi_replacement_d2_155(vi_replacement_155):
    feature = _clean(vi_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_155'] = {'inputs': ['vi_replacement_155'], 'func': vi_replacement_d2_155}


def vi_replacement_d2_156(vi_replacement_156):
    feature = _clean(vi_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_156'] = {'inputs': ['vi_replacement_156'], 'func': vi_replacement_d2_156}


def vi_replacement_d2_157(vi_replacement_157):
    feature = _clean(vi_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_157'] = {'inputs': ['vi_replacement_157'], 'func': vi_replacement_d2_157}


def vi_replacement_d2_158(vi_replacement_158):
    feature = _clean(vi_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_158'] = {'inputs': ['vi_replacement_158'], 'func': vi_replacement_d2_158}


def vi_replacement_d2_159(vi_replacement_159):
    feature = _clean(vi_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_159'] = {'inputs': ['vi_replacement_159'], 'func': vi_replacement_d2_159}


def vi_replacement_d2_160(vi_replacement_160):
    feature = _clean(vi_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_160'] = {'inputs': ['vi_replacement_160'], 'func': vi_replacement_d2_160}


def vi_replacement_d2_161(vi_replacement_161):
    feature = _clean(vi_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_161'] = {'inputs': ['vi_replacement_161'], 'func': vi_replacement_d2_161}


def vi_replacement_d2_162(vi_replacement_162):
    feature = _clean(vi_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_162'] = {'inputs': ['vi_replacement_162'], 'func': vi_replacement_d2_162}


def vi_replacement_d2_163(vi_replacement_163):
    feature = _clean(vi_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_163'] = {'inputs': ['vi_replacement_163'], 'func': vi_replacement_d2_163}


def vi_replacement_d2_164(vi_replacement_164):
    feature = _clean(vi_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_164'] = {'inputs': ['vi_replacement_164'], 'func': vi_replacement_d2_164}


def vi_replacement_d2_165(vi_replacement_165):
    feature = _clean(vi_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_165'] = {'inputs': ['vi_replacement_165'], 'func': vi_replacement_d2_165}


def vi_replacement_d2_166(vi_replacement_166):
    feature = _clean(vi_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_166'] = {'inputs': ['vi_replacement_166'], 'func': vi_replacement_d2_166}


def vi_replacement_d2_167(vi_replacement_167):
    feature = _clean(vi_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_167'] = {'inputs': ['vi_replacement_167'], 'func': vi_replacement_d2_167}


def vi_replacement_d2_168(vi_replacement_168):
    feature = _clean(vi_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_168'] = {'inputs': ['vi_replacement_168'], 'func': vi_replacement_d2_168}


def vi_replacement_d2_169(vi_replacement_169):
    feature = _clean(vi_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_169'] = {'inputs': ['vi_replacement_169'], 'func': vi_replacement_d2_169}


def vi_replacement_d2_170(vi_replacement_170):
    feature = _clean(vi_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_170'] = {'inputs': ['vi_replacement_170'], 'func': vi_replacement_d2_170}


def vi_replacement_d2_171(vi_replacement_171):
    feature = _clean(vi_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_171'] = {'inputs': ['vi_replacement_171'], 'func': vi_replacement_d2_171}


def vi_replacement_d2_172(vi_replacement_172):
    feature = _clean(vi_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_172'] = {'inputs': ['vi_replacement_172'], 'func': vi_replacement_d2_172}


def vi_replacement_d2_173(vi_replacement_173):
    feature = _clean(vi_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_173'] = {'inputs': ['vi_replacement_173'], 'func': vi_replacement_d2_173}


def vi_replacement_d2_174(vi_replacement_174):
    feature = _clean(vi_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_174'] = {'inputs': ['vi_replacement_174'], 'func': vi_replacement_d2_174}


def vi_replacement_d2_175(vi_replacement_175):
    feature = _clean(vi_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
VI_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vi_replacement_d2_175'] = {'inputs': ['vi_replacement_175'], 'func': vi_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vif_base_universe_d2_001_vif_003_loss_streak_21_003(vif_003_loss_streak_21_003):
    return _base_universe_d2(vif_003_loss_streak_21_003, 1)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_001_vif_003_loss_streak_21_003'] = {'inputs': ['vif_003_loss_streak_21_003'], 'func': vif_base_universe_d2_001_vif_003_loss_streak_21_003}


def vif_base_universe_d2_002_vif_004_ma_distance_42_004(vif_004_ma_distance_42_004):
    return _base_universe_d2(vif_004_ma_distance_42_004, 2)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_002_vif_004_ma_distance_42_004'] = {'inputs': ['vif_004_ma_distance_42_004'], 'func': vif_base_universe_d2_002_vif_004_ma_distance_42_004}


def vif_base_universe_d2_003_vif_005_stochastic_position_63_005(vif_005_stochastic_position_63_005):
    return _base_universe_d2(vif_005_stochastic_position_63_005, 3)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_003_vif_005_stochastic_position_63_005'] = {'inputs': ['vif_005_stochastic_position_63_005'], 'func': vif_base_universe_d2_003_vif_005_stochastic_position_63_005}


def vif_base_universe_d2_004_vif_009_loss_streak_252_009(vif_009_loss_streak_252_009):
    return _base_universe_d2(vif_009_loss_streak_252_009, 4)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_004_vif_009_loss_streak_252_009'] = {'inputs': ['vif_009_loss_streak_252_009'], 'func': vif_base_universe_d2_004_vif_009_loss_streak_252_009}


def vif_base_universe_d2_005_vif_010_ma_distance_378_010(vif_010_ma_distance_378_010):
    return _base_universe_d2(vif_010_ma_distance_378_010, 5)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_005_vif_010_ma_distance_378_010'] = {'inputs': ['vif_010_ma_distance_378_010'], 'func': vif_base_universe_d2_005_vif_010_ma_distance_378_010}


def vif_base_universe_d2_006_vif_011_stochastic_position_504_011(vif_011_stochastic_position_504_011):
    return _base_universe_d2(vif_011_stochastic_position_504_011, 6)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_006_vif_011_stochastic_position_504_011'] = {'inputs': ['vif_011_stochastic_position_504_011'], 'func': vif_base_universe_d2_006_vif_011_stochastic_position_504_011}


def vif_base_universe_d2_007_vif_015_loss_streak_1512_015(vif_015_loss_streak_1512_015):
    return _base_universe_d2(vif_015_loss_streak_1512_015, 7)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_007_vif_015_loss_streak_1512_015'] = {'inputs': ['vif_015_loss_streak_1512_015'], 'func': vif_base_universe_d2_007_vif_015_loss_streak_1512_015}


def vif_base_universe_d2_008_vif_016_ma_distance_5_016(vif_016_ma_distance_5_016):
    return _base_universe_d2(vif_016_ma_distance_5_016, 8)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_008_vif_016_ma_distance_5_016'] = {'inputs': ['vif_016_ma_distance_5_016'], 'func': vif_base_universe_d2_008_vif_016_ma_distance_5_016}


def vif_base_universe_d2_009_vif_017_stochastic_position_10_017(vif_017_stochastic_position_10_017):
    return _base_universe_d2(vif_017_stochastic_position_10_017, 9)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_009_vif_017_stochastic_position_10_017'] = {'inputs': ['vif_017_stochastic_position_10_017'], 'func': vif_base_universe_d2_009_vif_017_stochastic_position_10_017}


def vif_base_universe_d2_010_vif_021_loss_streak_84_021(vif_021_loss_streak_84_021):
    return _base_universe_d2(vif_021_loss_streak_84_021, 10)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_010_vif_021_loss_streak_84_021'] = {'inputs': ['vif_021_loss_streak_84_021'], 'func': vif_base_universe_d2_010_vif_021_loss_streak_84_021}


def vif_base_universe_d2_011_vif_022_ma_distance_126_022(vif_022_ma_distance_126_022):
    return _base_universe_d2(vif_022_ma_distance_126_022, 11)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_011_vif_022_ma_distance_126_022'] = {'inputs': ['vif_022_ma_distance_126_022'], 'func': vif_base_universe_d2_011_vif_022_ma_distance_126_022}


def vif_base_universe_d2_012_vif_023_stochastic_position_189_023(vif_023_stochastic_position_189_023):
    return _base_universe_d2(vif_023_stochastic_position_189_023, 12)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_012_vif_023_stochastic_position_189_023'] = {'inputs': ['vif_023_stochastic_position_189_023'], 'func': vif_base_universe_d2_012_vif_023_stochastic_position_189_023}


def vif_base_universe_d2_013_vif_027_loss_streak_756_027(vif_027_loss_streak_756_027):
    return _base_universe_d2(vif_027_loss_streak_756_027, 13)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_013_vif_027_loss_streak_756_027'] = {'inputs': ['vif_027_loss_streak_756_027'], 'func': vif_base_universe_d2_013_vif_027_loss_streak_756_027}


def vif_base_universe_d2_014_vif_028_ma_distance_1008_028(vif_028_ma_distance_1008_028):
    return _base_universe_d2(vif_028_ma_distance_1008_028, 14)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_014_vif_028_ma_distance_1008_028'] = {'inputs': ['vif_028_ma_distance_1008_028'], 'func': vif_base_universe_d2_014_vif_028_ma_distance_1008_028}


def vif_base_universe_d2_015_vif_029_stochastic_position_1260_029(vif_029_stochastic_position_1260_029):
    return _base_universe_d2(vif_029_stochastic_position_1260_029, 15)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_015_vif_029_stochastic_position_1260_029'] = {'inputs': ['vif_029_stochastic_position_1260_029'], 'func': vif_base_universe_d2_015_vif_029_stochastic_position_1260_029}


def vif_base_universe_d2_016_vif_basefill_001(vif_basefill_001):
    return _base_universe_d2(vif_basefill_001, 16)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_016_vif_basefill_001'] = {'inputs': ['vif_basefill_001'], 'func': vif_base_universe_d2_016_vif_basefill_001}


def vif_base_universe_d2_017_vif_basefill_002(vif_basefill_002):
    return _base_universe_d2(vif_basefill_002, 17)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_017_vif_basefill_002'] = {'inputs': ['vif_basefill_002'], 'func': vif_base_universe_d2_017_vif_basefill_002}


def vif_base_universe_d2_018_vif_basefill_006(vif_basefill_006):
    return _base_universe_d2(vif_basefill_006, 18)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_018_vif_basefill_006'] = {'inputs': ['vif_basefill_006'], 'func': vif_base_universe_d2_018_vif_basefill_006}


def vif_base_universe_d2_019_vif_basefill_007(vif_basefill_007):
    return _base_universe_d2(vif_basefill_007, 19)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_019_vif_basefill_007'] = {'inputs': ['vif_basefill_007'], 'func': vif_base_universe_d2_019_vif_basefill_007}


def vif_base_universe_d2_020_vif_basefill_008(vif_basefill_008):
    return _base_universe_d2(vif_basefill_008, 20)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_020_vif_basefill_008'] = {'inputs': ['vif_basefill_008'], 'func': vif_base_universe_d2_020_vif_basefill_008}


def vif_base_universe_d2_021_vif_basefill_012(vif_basefill_012):
    return _base_universe_d2(vif_basefill_012, 21)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_021_vif_basefill_012'] = {'inputs': ['vif_basefill_012'], 'func': vif_base_universe_d2_021_vif_basefill_012}


def vif_base_universe_d2_022_vif_basefill_013(vif_basefill_013):
    return _base_universe_d2(vif_basefill_013, 22)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_022_vif_basefill_013'] = {'inputs': ['vif_basefill_013'], 'func': vif_base_universe_d2_022_vif_basefill_013}


def vif_base_universe_d2_023_vif_basefill_014(vif_basefill_014):
    return _base_universe_d2(vif_basefill_014, 23)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_023_vif_basefill_014'] = {'inputs': ['vif_basefill_014'], 'func': vif_base_universe_d2_023_vif_basefill_014}


def vif_base_universe_d2_024_vif_basefill_018(vif_basefill_018):
    return _base_universe_d2(vif_basefill_018, 24)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_024_vif_basefill_018'] = {'inputs': ['vif_basefill_018'], 'func': vif_base_universe_d2_024_vif_basefill_018}


def vif_base_universe_d2_025_vif_basefill_019(vif_basefill_019):
    return _base_universe_d2(vif_basefill_019, 25)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_025_vif_basefill_019'] = {'inputs': ['vif_basefill_019'], 'func': vif_base_universe_d2_025_vif_basefill_019}


def vif_base_universe_d2_026_vif_basefill_020(vif_basefill_020):
    return _base_universe_d2(vif_basefill_020, 26)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_026_vif_basefill_020'] = {'inputs': ['vif_basefill_020'], 'func': vif_base_universe_d2_026_vif_basefill_020}


def vif_base_universe_d2_027_vif_basefill_024(vif_basefill_024):
    return _base_universe_d2(vif_basefill_024, 27)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_027_vif_basefill_024'] = {'inputs': ['vif_basefill_024'], 'func': vif_base_universe_d2_027_vif_basefill_024}


def vif_base_universe_d2_028_vif_basefill_025(vif_basefill_025):
    return _base_universe_d2(vif_basefill_025, 28)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_028_vif_basefill_025'] = {'inputs': ['vif_basefill_025'], 'func': vif_base_universe_d2_028_vif_basefill_025}


def vif_base_universe_d2_029_vif_basefill_026(vif_basefill_026):
    return _base_universe_d2(vif_basefill_026, 29)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_029_vif_basefill_026'] = {'inputs': ['vif_basefill_026'], 'func': vif_base_universe_d2_029_vif_basefill_026}


def vif_base_universe_d2_030_vif_basefill_030(vif_basefill_030):
    return _base_universe_d2(vif_basefill_030, 30)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_030_vif_basefill_030'] = {'inputs': ['vif_basefill_030'], 'func': vif_base_universe_d2_030_vif_basefill_030}


def vif_base_universe_d2_031_vif_basefill_031(vif_basefill_031):
    return _base_universe_d2(vif_basefill_031, 31)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_031_vif_basefill_031'] = {'inputs': ['vif_basefill_031'], 'func': vif_base_universe_d2_031_vif_basefill_031}


def vif_base_universe_d2_032_vif_basefill_032(vif_basefill_032):
    return _base_universe_d2(vif_basefill_032, 32)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_032_vif_basefill_032'] = {'inputs': ['vif_basefill_032'], 'func': vif_base_universe_d2_032_vif_basefill_032}


def vif_base_universe_d2_033_vif_basefill_033(vif_basefill_033):
    return _base_universe_d2(vif_basefill_033, 33)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_033_vif_basefill_033'] = {'inputs': ['vif_basefill_033'], 'func': vif_base_universe_d2_033_vif_basefill_033}


def vif_base_universe_d2_034_vif_basefill_034(vif_basefill_034):
    return _base_universe_d2(vif_basefill_034, 34)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_034_vif_basefill_034'] = {'inputs': ['vif_basefill_034'], 'func': vif_base_universe_d2_034_vif_basefill_034}


def vif_base_universe_d2_035_vif_basefill_035(vif_basefill_035):
    return _base_universe_d2(vif_basefill_035, 35)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_035_vif_basefill_035'] = {'inputs': ['vif_basefill_035'], 'func': vif_base_universe_d2_035_vif_basefill_035}


def vif_base_universe_d2_036_vif_basefill_036(vif_basefill_036):
    return _base_universe_d2(vif_basefill_036, 36)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_036_vif_basefill_036'] = {'inputs': ['vif_basefill_036'], 'func': vif_base_universe_d2_036_vif_basefill_036}


def vif_base_universe_d2_037_vif_basefill_037(vif_basefill_037):
    return _base_universe_d2(vif_basefill_037, 37)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_037_vif_basefill_037'] = {'inputs': ['vif_basefill_037'], 'func': vif_base_universe_d2_037_vif_basefill_037}


def vif_base_universe_d2_038_vif_basefill_038(vif_basefill_038):
    return _base_universe_d2(vif_basefill_038, 38)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_038_vif_basefill_038'] = {'inputs': ['vif_basefill_038'], 'func': vif_base_universe_d2_038_vif_basefill_038}


def vif_base_universe_d2_039_vif_basefill_039(vif_basefill_039):
    return _base_universe_d2(vif_basefill_039, 39)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_039_vif_basefill_039'] = {'inputs': ['vif_basefill_039'], 'func': vif_base_universe_d2_039_vif_basefill_039}


def vif_base_universe_d2_040_vif_basefill_040(vif_basefill_040):
    return _base_universe_d2(vif_basefill_040, 40)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_040_vif_basefill_040'] = {'inputs': ['vif_basefill_040'], 'func': vif_base_universe_d2_040_vif_basefill_040}


def vif_base_universe_d2_041_vif_basefill_041(vif_basefill_041):
    return _base_universe_d2(vif_basefill_041, 41)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_041_vif_basefill_041'] = {'inputs': ['vif_basefill_041'], 'func': vif_base_universe_d2_041_vif_basefill_041}


def vif_base_universe_d2_042_vif_basefill_042(vif_basefill_042):
    return _base_universe_d2(vif_basefill_042, 42)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_042_vif_basefill_042'] = {'inputs': ['vif_basefill_042'], 'func': vif_base_universe_d2_042_vif_basefill_042}


def vif_base_universe_d2_043_vif_basefill_043(vif_basefill_043):
    return _base_universe_d2(vif_basefill_043, 43)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_043_vif_basefill_043'] = {'inputs': ['vif_basefill_043'], 'func': vif_base_universe_d2_043_vif_basefill_043}


def vif_base_universe_d2_044_vif_basefill_044(vif_basefill_044):
    return _base_universe_d2(vif_basefill_044, 44)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_044_vif_basefill_044'] = {'inputs': ['vif_basefill_044'], 'func': vif_base_universe_d2_044_vif_basefill_044}


def vif_base_universe_d2_045_vif_basefill_045(vif_basefill_045):
    return _base_universe_d2(vif_basefill_045, 45)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_045_vif_basefill_045'] = {'inputs': ['vif_basefill_045'], 'func': vif_base_universe_d2_045_vif_basefill_045}


def vif_base_universe_d2_046_vif_basefill_046(vif_basefill_046):
    return _base_universe_d2(vif_basefill_046, 46)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_046_vif_basefill_046'] = {'inputs': ['vif_basefill_046'], 'func': vif_base_universe_d2_046_vif_basefill_046}


def vif_base_universe_d2_047_vif_basefill_047(vif_basefill_047):
    return _base_universe_d2(vif_basefill_047, 47)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_047_vif_basefill_047'] = {'inputs': ['vif_basefill_047'], 'func': vif_base_universe_d2_047_vif_basefill_047}


def vif_base_universe_d2_048_vif_basefill_048(vif_basefill_048):
    return _base_universe_d2(vif_basefill_048, 48)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_048_vif_basefill_048'] = {'inputs': ['vif_basefill_048'], 'func': vif_base_universe_d2_048_vif_basefill_048}


def vif_base_universe_d2_049_vif_basefill_049(vif_basefill_049):
    return _base_universe_d2(vif_basefill_049, 49)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_049_vif_basefill_049'] = {'inputs': ['vif_basefill_049'], 'func': vif_base_universe_d2_049_vif_basefill_049}


def vif_base_universe_d2_050_vif_basefill_050(vif_basefill_050):
    return _base_universe_d2(vif_basefill_050, 50)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_050_vif_basefill_050'] = {'inputs': ['vif_basefill_050'], 'func': vif_base_universe_d2_050_vif_basefill_050}


def vif_base_universe_d2_051_vif_basefill_051(vif_basefill_051):
    return _base_universe_d2(vif_basefill_051, 51)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_051_vif_basefill_051'] = {'inputs': ['vif_basefill_051'], 'func': vif_base_universe_d2_051_vif_basefill_051}


def vif_base_universe_d2_052_vif_basefill_052(vif_basefill_052):
    return _base_universe_d2(vif_basefill_052, 52)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_052_vif_basefill_052'] = {'inputs': ['vif_basefill_052'], 'func': vif_base_universe_d2_052_vif_basefill_052}


def vif_base_universe_d2_053_vif_basefill_053(vif_basefill_053):
    return _base_universe_d2(vif_basefill_053, 53)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_053_vif_basefill_053'] = {'inputs': ['vif_basefill_053'], 'func': vif_base_universe_d2_053_vif_basefill_053}


def vif_base_universe_d2_054_vif_basefill_054(vif_basefill_054):
    return _base_universe_d2(vif_basefill_054, 54)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_054_vif_basefill_054'] = {'inputs': ['vif_basefill_054'], 'func': vif_base_universe_d2_054_vif_basefill_054}


def vif_base_universe_d2_055_vif_basefill_055(vif_basefill_055):
    return _base_universe_d2(vif_basefill_055, 55)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_055_vif_basefill_055'] = {'inputs': ['vif_basefill_055'], 'func': vif_base_universe_d2_055_vif_basefill_055}


def vif_base_universe_d2_056_vif_basefill_056(vif_basefill_056):
    return _base_universe_d2(vif_basefill_056, 56)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_056_vif_basefill_056'] = {'inputs': ['vif_basefill_056'], 'func': vif_base_universe_d2_056_vif_basefill_056}


def vif_base_universe_d2_057_vif_basefill_057(vif_basefill_057):
    return _base_universe_d2(vif_basefill_057, 57)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_057_vif_basefill_057'] = {'inputs': ['vif_basefill_057'], 'func': vif_base_universe_d2_057_vif_basefill_057}


def vif_base_universe_d2_058_vif_basefill_058(vif_basefill_058):
    return _base_universe_d2(vif_basefill_058, 58)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_058_vif_basefill_058'] = {'inputs': ['vif_basefill_058'], 'func': vif_base_universe_d2_058_vif_basefill_058}


def vif_base_universe_d2_059_vif_basefill_059(vif_basefill_059):
    return _base_universe_d2(vif_basefill_059, 59)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_059_vif_basefill_059'] = {'inputs': ['vif_basefill_059'], 'func': vif_base_universe_d2_059_vif_basefill_059}


def vif_base_universe_d2_060_vif_basefill_060(vif_basefill_060):
    return _base_universe_d2(vif_basefill_060, 60)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_060_vif_basefill_060'] = {'inputs': ['vif_basefill_060'], 'func': vif_base_universe_d2_060_vif_basefill_060}


def vif_base_universe_d2_061_vif_basefill_061(vif_basefill_061):
    return _base_universe_d2(vif_basefill_061, 61)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_061_vif_basefill_061'] = {'inputs': ['vif_basefill_061'], 'func': vif_base_universe_d2_061_vif_basefill_061}


def vif_base_universe_d2_062_vif_basefill_062(vif_basefill_062):
    return _base_universe_d2(vif_basefill_062, 62)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_062_vif_basefill_062'] = {'inputs': ['vif_basefill_062'], 'func': vif_base_universe_d2_062_vif_basefill_062}


def vif_base_universe_d2_063_vif_basefill_063(vif_basefill_063):
    return _base_universe_d2(vif_basefill_063, 63)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_063_vif_basefill_063'] = {'inputs': ['vif_basefill_063'], 'func': vif_base_universe_d2_063_vif_basefill_063}


def vif_base_universe_d2_064_vif_basefill_064(vif_basefill_064):
    return _base_universe_d2(vif_basefill_064, 64)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_064_vif_basefill_064'] = {'inputs': ['vif_basefill_064'], 'func': vif_base_universe_d2_064_vif_basefill_064}


def vif_base_universe_d2_065_vif_basefill_065(vif_basefill_065):
    return _base_universe_d2(vif_basefill_065, 65)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_065_vif_basefill_065'] = {'inputs': ['vif_basefill_065'], 'func': vif_base_universe_d2_065_vif_basefill_065}


def vif_base_universe_d2_066_vif_basefill_066(vif_basefill_066):
    return _base_universe_d2(vif_basefill_066, 66)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_066_vif_basefill_066'] = {'inputs': ['vif_basefill_066'], 'func': vif_base_universe_d2_066_vif_basefill_066}


def vif_base_universe_d2_067_vif_basefill_067(vif_basefill_067):
    return _base_universe_d2(vif_basefill_067, 67)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_067_vif_basefill_067'] = {'inputs': ['vif_basefill_067'], 'func': vif_base_universe_d2_067_vif_basefill_067}


def vif_base_universe_d2_068_vif_basefill_068(vif_basefill_068):
    return _base_universe_d2(vif_basefill_068, 68)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_068_vif_basefill_068'] = {'inputs': ['vif_basefill_068'], 'func': vif_base_universe_d2_068_vif_basefill_068}


def vif_base_universe_d2_069_vif_basefill_069(vif_basefill_069):
    return _base_universe_d2(vif_basefill_069, 69)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_069_vif_basefill_069'] = {'inputs': ['vif_basefill_069'], 'func': vif_base_universe_d2_069_vif_basefill_069}


def vif_base_universe_d2_070_vif_basefill_070(vif_basefill_070):
    return _base_universe_d2(vif_basefill_070, 70)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_070_vif_basefill_070'] = {'inputs': ['vif_basefill_070'], 'func': vif_base_universe_d2_070_vif_basefill_070}


def vif_base_universe_d2_071_vif_basefill_071(vif_basefill_071):
    return _base_universe_d2(vif_basefill_071, 71)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_071_vif_basefill_071'] = {'inputs': ['vif_basefill_071'], 'func': vif_base_universe_d2_071_vif_basefill_071}


def vif_base_universe_d2_072_vif_basefill_072(vif_basefill_072):
    return _base_universe_d2(vif_basefill_072, 72)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_072_vif_basefill_072'] = {'inputs': ['vif_basefill_072'], 'func': vif_base_universe_d2_072_vif_basefill_072}


def vif_base_universe_d2_073_vif_basefill_073(vif_basefill_073):
    return _base_universe_d2(vif_basefill_073, 73)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_073_vif_basefill_073'] = {'inputs': ['vif_basefill_073'], 'func': vif_base_universe_d2_073_vif_basefill_073}


def vif_base_universe_d2_074_vif_basefill_074(vif_basefill_074):
    return _base_universe_d2(vif_basefill_074, 74)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_074_vif_basefill_074'] = {'inputs': ['vif_basefill_074'], 'func': vif_base_universe_d2_074_vif_basefill_074}


def vif_base_universe_d2_075_vif_basefill_075(vif_basefill_075):
    return _base_universe_d2(vif_basefill_075, 75)
VIF_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vif_base_universe_d2_075_vif_basefill_075'] = {'inputs': ['vif_basefill_075'], 'func': vif_base_universe_d2_075_vif_basefill_075}
