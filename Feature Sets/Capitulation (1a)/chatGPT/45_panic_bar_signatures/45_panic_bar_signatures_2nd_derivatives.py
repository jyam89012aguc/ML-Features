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



def pbs_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def pbs_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def pbs_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def pbs_154_pbs_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def pbs_155_pbs_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















PANIC_BAR_SIGNATURES_REGISTRY_2ND_DERIVATIVES = {
    'pbs_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': pbs_001_realized_vol_z_roc_1},
    'pbs_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': pbs_007_realized_vol_z_roc_5},
    'pbs_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': pbs_013_realized_vol_z_roc_42},
    'pbs_154_pbs_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': pbs_154_pbs_019_realized_vol_z_42_019_roc_126},
    'pbs_155_pbs_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': pbs_155_pbs_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def pbs_replacement_d2_001(pbs_replacement_001):
    feature = _clean(pbs_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_001'] = {'inputs': ['pbs_replacement_001'], 'func': pbs_replacement_d2_001}


def pbs_replacement_d2_002(pbs_replacement_002):
    feature = _clean(pbs_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_002'] = {'inputs': ['pbs_replacement_002'], 'func': pbs_replacement_d2_002}


def pbs_replacement_d2_003(pbs_replacement_003):
    feature = _clean(pbs_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_003'] = {'inputs': ['pbs_replacement_003'], 'func': pbs_replacement_d2_003}


def pbs_replacement_d2_004(pbs_replacement_004):
    feature = _clean(pbs_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_004'] = {'inputs': ['pbs_replacement_004'], 'func': pbs_replacement_d2_004}


def pbs_replacement_d2_005(pbs_replacement_005):
    feature = _clean(pbs_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_005'] = {'inputs': ['pbs_replacement_005'], 'func': pbs_replacement_d2_005}


def pbs_replacement_d2_006(pbs_replacement_006):
    feature = _clean(pbs_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_006'] = {'inputs': ['pbs_replacement_006'], 'func': pbs_replacement_d2_006}


def pbs_replacement_d2_007(pbs_replacement_007):
    feature = _clean(pbs_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_007'] = {'inputs': ['pbs_replacement_007'], 'func': pbs_replacement_d2_007}


def pbs_replacement_d2_008(pbs_replacement_008):
    feature = _clean(pbs_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_008'] = {'inputs': ['pbs_replacement_008'], 'func': pbs_replacement_d2_008}


def pbs_replacement_d2_009(pbs_replacement_009):
    feature = _clean(pbs_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_009'] = {'inputs': ['pbs_replacement_009'], 'func': pbs_replacement_d2_009}


def pbs_replacement_d2_010(pbs_replacement_010):
    feature = _clean(pbs_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_010'] = {'inputs': ['pbs_replacement_010'], 'func': pbs_replacement_d2_010}


def pbs_replacement_d2_011(pbs_replacement_011):
    feature = _clean(pbs_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_011'] = {'inputs': ['pbs_replacement_011'], 'func': pbs_replacement_d2_011}


def pbs_replacement_d2_012(pbs_replacement_012):
    feature = _clean(pbs_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_012'] = {'inputs': ['pbs_replacement_012'], 'func': pbs_replacement_d2_012}


def pbs_replacement_d2_013(pbs_replacement_013):
    feature = _clean(pbs_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_013'] = {'inputs': ['pbs_replacement_013'], 'func': pbs_replacement_d2_013}


def pbs_replacement_d2_014(pbs_replacement_014):
    feature = _clean(pbs_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_014'] = {'inputs': ['pbs_replacement_014'], 'func': pbs_replacement_d2_014}


def pbs_replacement_d2_015(pbs_replacement_015):
    feature = _clean(pbs_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_015'] = {'inputs': ['pbs_replacement_015'], 'func': pbs_replacement_d2_015}


def pbs_replacement_d2_016(pbs_replacement_016):
    feature = _clean(pbs_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_016'] = {'inputs': ['pbs_replacement_016'], 'func': pbs_replacement_d2_016}


def pbs_replacement_d2_017(pbs_replacement_017):
    feature = _clean(pbs_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_017'] = {'inputs': ['pbs_replacement_017'], 'func': pbs_replacement_d2_017}


def pbs_replacement_d2_018(pbs_replacement_018):
    feature = _clean(pbs_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_018'] = {'inputs': ['pbs_replacement_018'], 'func': pbs_replacement_d2_018}


def pbs_replacement_d2_019(pbs_replacement_019):
    feature = _clean(pbs_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_019'] = {'inputs': ['pbs_replacement_019'], 'func': pbs_replacement_d2_019}


def pbs_replacement_d2_020(pbs_replacement_020):
    feature = _clean(pbs_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_020'] = {'inputs': ['pbs_replacement_020'], 'func': pbs_replacement_d2_020}


def pbs_replacement_d2_021(pbs_replacement_021):
    feature = _clean(pbs_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_021'] = {'inputs': ['pbs_replacement_021'], 'func': pbs_replacement_d2_021}


def pbs_replacement_d2_022(pbs_replacement_022):
    feature = _clean(pbs_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_022'] = {'inputs': ['pbs_replacement_022'], 'func': pbs_replacement_d2_022}


def pbs_replacement_d2_023(pbs_replacement_023):
    feature = _clean(pbs_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_023'] = {'inputs': ['pbs_replacement_023'], 'func': pbs_replacement_d2_023}


def pbs_replacement_d2_024(pbs_replacement_024):
    feature = _clean(pbs_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_024'] = {'inputs': ['pbs_replacement_024'], 'func': pbs_replacement_d2_024}


def pbs_replacement_d2_025(pbs_replacement_025):
    feature = _clean(pbs_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_025'] = {'inputs': ['pbs_replacement_025'], 'func': pbs_replacement_d2_025}


def pbs_replacement_d2_026(pbs_replacement_026):
    feature = _clean(pbs_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_026'] = {'inputs': ['pbs_replacement_026'], 'func': pbs_replacement_d2_026}


def pbs_replacement_d2_027(pbs_replacement_027):
    feature = _clean(pbs_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_027'] = {'inputs': ['pbs_replacement_027'], 'func': pbs_replacement_d2_027}


def pbs_replacement_d2_028(pbs_replacement_028):
    feature = _clean(pbs_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_028'] = {'inputs': ['pbs_replacement_028'], 'func': pbs_replacement_d2_028}


def pbs_replacement_d2_029(pbs_replacement_029):
    feature = _clean(pbs_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_029'] = {'inputs': ['pbs_replacement_029'], 'func': pbs_replacement_d2_029}


def pbs_replacement_d2_030(pbs_replacement_030):
    feature = _clean(pbs_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_030'] = {'inputs': ['pbs_replacement_030'], 'func': pbs_replacement_d2_030}


def pbs_replacement_d2_031(pbs_replacement_031):
    feature = _clean(pbs_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_031'] = {'inputs': ['pbs_replacement_031'], 'func': pbs_replacement_d2_031}


def pbs_replacement_d2_032(pbs_replacement_032):
    feature = _clean(pbs_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_032'] = {'inputs': ['pbs_replacement_032'], 'func': pbs_replacement_d2_032}


def pbs_replacement_d2_033(pbs_replacement_033):
    feature = _clean(pbs_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_033'] = {'inputs': ['pbs_replacement_033'], 'func': pbs_replacement_d2_033}


def pbs_replacement_d2_034(pbs_replacement_034):
    feature = _clean(pbs_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_034'] = {'inputs': ['pbs_replacement_034'], 'func': pbs_replacement_d2_034}


def pbs_replacement_d2_035(pbs_replacement_035):
    feature = _clean(pbs_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_035'] = {'inputs': ['pbs_replacement_035'], 'func': pbs_replacement_d2_035}


def pbs_replacement_d2_036(pbs_replacement_036):
    feature = _clean(pbs_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_036'] = {'inputs': ['pbs_replacement_036'], 'func': pbs_replacement_d2_036}


def pbs_replacement_d2_037(pbs_replacement_037):
    feature = _clean(pbs_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_037'] = {'inputs': ['pbs_replacement_037'], 'func': pbs_replacement_d2_037}


def pbs_replacement_d2_038(pbs_replacement_038):
    feature = _clean(pbs_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_038'] = {'inputs': ['pbs_replacement_038'], 'func': pbs_replacement_d2_038}


def pbs_replacement_d2_039(pbs_replacement_039):
    feature = _clean(pbs_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_039'] = {'inputs': ['pbs_replacement_039'], 'func': pbs_replacement_d2_039}


def pbs_replacement_d2_040(pbs_replacement_040):
    feature = _clean(pbs_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_040'] = {'inputs': ['pbs_replacement_040'], 'func': pbs_replacement_d2_040}


def pbs_replacement_d2_041(pbs_replacement_041):
    feature = _clean(pbs_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_041'] = {'inputs': ['pbs_replacement_041'], 'func': pbs_replacement_d2_041}


def pbs_replacement_d2_042(pbs_replacement_042):
    feature = _clean(pbs_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_042'] = {'inputs': ['pbs_replacement_042'], 'func': pbs_replacement_d2_042}


def pbs_replacement_d2_043(pbs_replacement_043):
    feature = _clean(pbs_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_043'] = {'inputs': ['pbs_replacement_043'], 'func': pbs_replacement_d2_043}


def pbs_replacement_d2_044(pbs_replacement_044):
    feature = _clean(pbs_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_044'] = {'inputs': ['pbs_replacement_044'], 'func': pbs_replacement_d2_044}


def pbs_replacement_d2_045(pbs_replacement_045):
    feature = _clean(pbs_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_045'] = {'inputs': ['pbs_replacement_045'], 'func': pbs_replacement_d2_045}


def pbs_replacement_d2_046(pbs_replacement_046):
    feature = _clean(pbs_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_046'] = {'inputs': ['pbs_replacement_046'], 'func': pbs_replacement_d2_046}


def pbs_replacement_d2_047(pbs_replacement_047):
    feature = _clean(pbs_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_047'] = {'inputs': ['pbs_replacement_047'], 'func': pbs_replacement_d2_047}


def pbs_replacement_d2_048(pbs_replacement_048):
    feature = _clean(pbs_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_048'] = {'inputs': ['pbs_replacement_048'], 'func': pbs_replacement_d2_048}


def pbs_replacement_d2_049(pbs_replacement_049):
    feature = _clean(pbs_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_049'] = {'inputs': ['pbs_replacement_049'], 'func': pbs_replacement_d2_049}


def pbs_replacement_d2_050(pbs_replacement_050):
    feature = _clean(pbs_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_050'] = {'inputs': ['pbs_replacement_050'], 'func': pbs_replacement_d2_050}


def pbs_replacement_d2_051(pbs_replacement_051):
    feature = _clean(pbs_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_051'] = {'inputs': ['pbs_replacement_051'], 'func': pbs_replacement_d2_051}


def pbs_replacement_d2_052(pbs_replacement_052):
    feature = _clean(pbs_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_052'] = {'inputs': ['pbs_replacement_052'], 'func': pbs_replacement_d2_052}


def pbs_replacement_d2_053(pbs_replacement_053):
    feature = _clean(pbs_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_053'] = {'inputs': ['pbs_replacement_053'], 'func': pbs_replacement_d2_053}


def pbs_replacement_d2_054(pbs_replacement_054):
    feature = _clean(pbs_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_054'] = {'inputs': ['pbs_replacement_054'], 'func': pbs_replacement_d2_054}


def pbs_replacement_d2_055(pbs_replacement_055):
    feature = _clean(pbs_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_055'] = {'inputs': ['pbs_replacement_055'], 'func': pbs_replacement_d2_055}


def pbs_replacement_d2_056(pbs_replacement_056):
    feature = _clean(pbs_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_056'] = {'inputs': ['pbs_replacement_056'], 'func': pbs_replacement_d2_056}


def pbs_replacement_d2_057(pbs_replacement_057):
    feature = _clean(pbs_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_057'] = {'inputs': ['pbs_replacement_057'], 'func': pbs_replacement_d2_057}


def pbs_replacement_d2_058(pbs_replacement_058):
    feature = _clean(pbs_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_058'] = {'inputs': ['pbs_replacement_058'], 'func': pbs_replacement_d2_058}


def pbs_replacement_d2_059(pbs_replacement_059):
    feature = _clean(pbs_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_059'] = {'inputs': ['pbs_replacement_059'], 'func': pbs_replacement_d2_059}


def pbs_replacement_d2_060(pbs_replacement_060):
    feature = _clean(pbs_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_060'] = {'inputs': ['pbs_replacement_060'], 'func': pbs_replacement_d2_060}


def pbs_replacement_d2_061(pbs_replacement_061):
    feature = _clean(pbs_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_061'] = {'inputs': ['pbs_replacement_061'], 'func': pbs_replacement_d2_061}


def pbs_replacement_d2_062(pbs_replacement_062):
    feature = _clean(pbs_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_062'] = {'inputs': ['pbs_replacement_062'], 'func': pbs_replacement_d2_062}


def pbs_replacement_d2_063(pbs_replacement_063):
    feature = _clean(pbs_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_063'] = {'inputs': ['pbs_replacement_063'], 'func': pbs_replacement_d2_063}


def pbs_replacement_d2_064(pbs_replacement_064):
    feature = _clean(pbs_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_064'] = {'inputs': ['pbs_replacement_064'], 'func': pbs_replacement_d2_064}


def pbs_replacement_d2_065(pbs_replacement_065):
    feature = _clean(pbs_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_065'] = {'inputs': ['pbs_replacement_065'], 'func': pbs_replacement_d2_065}


def pbs_replacement_d2_066(pbs_replacement_066):
    feature = _clean(pbs_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_066'] = {'inputs': ['pbs_replacement_066'], 'func': pbs_replacement_d2_066}


def pbs_replacement_d2_067(pbs_replacement_067):
    feature = _clean(pbs_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_067'] = {'inputs': ['pbs_replacement_067'], 'func': pbs_replacement_d2_067}


def pbs_replacement_d2_068(pbs_replacement_068):
    feature = _clean(pbs_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_068'] = {'inputs': ['pbs_replacement_068'], 'func': pbs_replacement_d2_068}


def pbs_replacement_d2_069(pbs_replacement_069):
    feature = _clean(pbs_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_069'] = {'inputs': ['pbs_replacement_069'], 'func': pbs_replacement_d2_069}


def pbs_replacement_d2_070(pbs_replacement_070):
    feature = _clean(pbs_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_070'] = {'inputs': ['pbs_replacement_070'], 'func': pbs_replacement_d2_070}


def pbs_replacement_d2_071(pbs_replacement_071):
    feature = _clean(pbs_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_071'] = {'inputs': ['pbs_replacement_071'], 'func': pbs_replacement_d2_071}


def pbs_replacement_d2_072(pbs_replacement_072):
    feature = _clean(pbs_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_072'] = {'inputs': ['pbs_replacement_072'], 'func': pbs_replacement_d2_072}


def pbs_replacement_d2_073(pbs_replacement_073):
    feature = _clean(pbs_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_073'] = {'inputs': ['pbs_replacement_073'], 'func': pbs_replacement_d2_073}


def pbs_replacement_d2_074(pbs_replacement_074):
    feature = _clean(pbs_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_074'] = {'inputs': ['pbs_replacement_074'], 'func': pbs_replacement_d2_074}


def pbs_replacement_d2_075(pbs_replacement_075):
    feature = _clean(pbs_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_075'] = {'inputs': ['pbs_replacement_075'], 'func': pbs_replacement_d2_075}


def pbs_replacement_d2_076(pbs_replacement_076):
    feature = _clean(pbs_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_076'] = {'inputs': ['pbs_replacement_076'], 'func': pbs_replacement_d2_076}


def pbs_replacement_d2_077(pbs_replacement_077):
    feature = _clean(pbs_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_077'] = {'inputs': ['pbs_replacement_077'], 'func': pbs_replacement_d2_077}


def pbs_replacement_d2_078(pbs_replacement_078):
    feature = _clean(pbs_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_078'] = {'inputs': ['pbs_replacement_078'], 'func': pbs_replacement_d2_078}


def pbs_replacement_d2_079(pbs_replacement_079):
    feature = _clean(pbs_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_079'] = {'inputs': ['pbs_replacement_079'], 'func': pbs_replacement_d2_079}


def pbs_replacement_d2_080(pbs_replacement_080):
    feature = _clean(pbs_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_080'] = {'inputs': ['pbs_replacement_080'], 'func': pbs_replacement_d2_080}


def pbs_replacement_d2_081(pbs_replacement_081):
    feature = _clean(pbs_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_081'] = {'inputs': ['pbs_replacement_081'], 'func': pbs_replacement_d2_081}


def pbs_replacement_d2_082(pbs_replacement_082):
    feature = _clean(pbs_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_082'] = {'inputs': ['pbs_replacement_082'], 'func': pbs_replacement_d2_082}


def pbs_replacement_d2_083(pbs_replacement_083):
    feature = _clean(pbs_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_083'] = {'inputs': ['pbs_replacement_083'], 'func': pbs_replacement_d2_083}


def pbs_replacement_d2_084(pbs_replacement_084):
    feature = _clean(pbs_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_084'] = {'inputs': ['pbs_replacement_084'], 'func': pbs_replacement_d2_084}


def pbs_replacement_d2_085(pbs_replacement_085):
    feature = _clean(pbs_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_085'] = {'inputs': ['pbs_replacement_085'], 'func': pbs_replacement_d2_085}


def pbs_replacement_d2_086(pbs_replacement_086):
    feature = _clean(pbs_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_086'] = {'inputs': ['pbs_replacement_086'], 'func': pbs_replacement_d2_086}


def pbs_replacement_d2_087(pbs_replacement_087):
    feature = _clean(pbs_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_087'] = {'inputs': ['pbs_replacement_087'], 'func': pbs_replacement_d2_087}


def pbs_replacement_d2_088(pbs_replacement_088):
    feature = _clean(pbs_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_088'] = {'inputs': ['pbs_replacement_088'], 'func': pbs_replacement_d2_088}


def pbs_replacement_d2_089(pbs_replacement_089):
    feature = _clean(pbs_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_089'] = {'inputs': ['pbs_replacement_089'], 'func': pbs_replacement_d2_089}


def pbs_replacement_d2_090(pbs_replacement_090):
    feature = _clean(pbs_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_090'] = {'inputs': ['pbs_replacement_090'], 'func': pbs_replacement_d2_090}


def pbs_replacement_d2_091(pbs_replacement_091):
    feature = _clean(pbs_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_091'] = {'inputs': ['pbs_replacement_091'], 'func': pbs_replacement_d2_091}


def pbs_replacement_d2_092(pbs_replacement_092):
    feature = _clean(pbs_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_092'] = {'inputs': ['pbs_replacement_092'], 'func': pbs_replacement_d2_092}


def pbs_replacement_d2_093(pbs_replacement_093):
    feature = _clean(pbs_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_093'] = {'inputs': ['pbs_replacement_093'], 'func': pbs_replacement_d2_093}


def pbs_replacement_d2_094(pbs_replacement_094):
    feature = _clean(pbs_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_094'] = {'inputs': ['pbs_replacement_094'], 'func': pbs_replacement_d2_094}


def pbs_replacement_d2_095(pbs_replacement_095):
    feature = _clean(pbs_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_095'] = {'inputs': ['pbs_replacement_095'], 'func': pbs_replacement_d2_095}


def pbs_replacement_d2_096(pbs_replacement_096):
    feature = _clean(pbs_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_096'] = {'inputs': ['pbs_replacement_096'], 'func': pbs_replacement_d2_096}


def pbs_replacement_d2_097(pbs_replacement_097):
    feature = _clean(pbs_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_097'] = {'inputs': ['pbs_replacement_097'], 'func': pbs_replacement_d2_097}


def pbs_replacement_d2_098(pbs_replacement_098):
    feature = _clean(pbs_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_098'] = {'inputs': ['pbs_replacement_098'], 'func': pbs_replacement_d2_098}


def pbs_replacement_d2_099(pbs_replacement_099):
    feature = _clean(pbs_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_099'] = {'inputs': ['pbs_replacement_099'], 'func': pbs_replacement_d2_099}


def pbs_replacement_d2_100(pbs_replacement_100):
    feature = _clean(pbs_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_100'] = {'inputs': ['pbs_replacement_100'], 'func': pbs_replacement_d2_100}


def pbs_replacement_d2_101(pbs_replacement_101):
    feature = _clean(pbs_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_101'] = {'inputs': ['pbs_replacement_101'], 'func': pbs_replacement_d2_101}


def pbs_replacement_d2_102(pbs_replacement_102):
    feature = _clean(pbs_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_102'] = {'inputs': ['pbs_replacement_102'], 'func': pbs_replacement_d2_102}


def pbs_replacement_d2_103(pbs_replacement_103):
    feature = _clean(pbs_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_103'] = {'inputs': ['pbs_replacement_103'], 'func': pbs_replacement_d2_103}


def pbs_replacement_d2_104(pbs_replacement_104):
    feature = _clean(pbs_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_104'] = {'inputs': ['pbs_replacement_104'], 'func': pbs_replacement_d2_104}


def pbs_replacement_d2_105(pbs_replacement_105):
    feature = _clean(pbs_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_105'] = {'inputs': ['pbs_replacement_105'], 'func': pbs_replacement_d2_105}


def pbs_replacement_d2_106(pbs_replacement_106):
    feature = _clean(pbs_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_106'] = {'inputs': ['pbs_replacement_106'], 'func': pbs_replacement_d2_106}


def pbs_replacement_d2_107(pbs_replacement_107):
    feature = _clean(pbs_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_107'] = {'inputs': ['pbs_replacement_107'], 'func': pbs_replacement_d2_107}


def pbs_replacement_d2_108(pbs_replacement_108):
    feature = _clean(pbs_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_108'] = {'inputs': ['pbs_replacement_108'], 'func': pbs_replacement_d2_108}


def pbs_replacement_d2_109(pbs_replacement_109):
    feature = _clean(pbs_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_109'] = {'inputs': ['pbs_replacement_109'], 'func': pbs_replacement_d2_109}


def pbs_replacement_d2_110(pbs_replacement_110):
    feature = _clean(pbs_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_110'] = {'inputs': ['pbs_replacement_110'], 'func': pbs_replacement_d2_110}


def pbs_replacement_d2_111(pbs_replacement_111):
    feature = _clean(pbs_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_111'] = {'inputs': ['pbs_replacement_111'], 'func': pbs_replacement_d2_111}


def pbs_replacement_d2_112(pbs_replacement_112):
    feature = _clean(pbs_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_112'] = {'inputs': ['pbs_replacement_112'], 'func': pbs_replacement_d2_112}


def pbs_replacement_d2_113(pbs_replacement_113):
    feature = _clean(pbs_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_113'] = {'inputs': ['pbs_replacement_113'], 'func': pbs_replacement_d2_113}


def pbs_replacement_d2_114(pbs_replacement_114):
    feature = _clean(pbs_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_114'] = {'inputs': ['pbs_replacement_114'], 'func': pbs_replacement_d2_114}


def pbs_replacement_d2_115(pbs_replacement_115):
    feature = _clean(pbs_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_115'] = {'inputs': ['pbs_replacement_115'], 'func': pbs_replacement_d2_115}


def pbs_replacement_d2_116(pbs_replacement_116):
    feature = _clean(pbs_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_116'] = {'inputs': ['pbs_replacement_116'], 'func': pbs_replacement_d2_116}


def pbs_replacement_d2_117(pbs_replacement_117):
    feature = _clean(pbs_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_117'] = {'inputs': ['pbs_replacement_117'], 'func': pbs_replacement_d2_117}


def pbs_replacement_d2_118(pbs_replacement_118):
    feature = _clean(pbs_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_118'] = {'inputs': ['pbs_replacement_118'], 'func': pbs_replacement_d2_118}


def pbs_replacement_d2_119(pbs_replacement_119):
    feature = _clean(pbs_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_119'] = {'inputs': ['pbs_replacement_119'], 'func': pbs_replacement_d2_119}


def pbs_replacement_d2_120(pbs_replacement_120):
    feature = _clean(pbs_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_120'] = {'inputs': ['pbs_replacement_120'], 'func': pbs_replacement_d2_120}


def pbs_replacement_d2_121(pbs_replacement_121):
    feature = _clean(pbs_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_121'] = {'inputs': ['pbs_replacement_121'], 'func': pbs_replacement_d2_121}


def pbs_replacement_d2_122(pbs_replacement_122):
    feature = _clean(pbs_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_122'] = {'inputs': ['pbs_replacement_122'], 'func': pbs_replacement_d2_122}


def pbs_replacement_d2_123(pbs_replacement_123):
    feature = _clean(pbs_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_123'] = {'inputs': ['pbs_replacement_123'], 'func': pbs_replacement_d2_123}


def pbs_replacement_d2_124(pbs_replacement_124):
    feature = _clean(pbs_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_124'] = {'inputs': ['pbs_replacement_124'], 'func': pbs_replacement_d2_124}


def pbs_replacement_d2_125(pbs_replacement_125):
    feature = _clean(pbs_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_125'] = {'inputs': ['pbs_replacement_125'], 'func': pbs_replacement_d2_125}


def pbs_replacement_d2_126(pbs_replacement_126):
    feature = _clean(pbs_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_126'] = {'inputs': ['pbs_replacement_126'], 'func': pbs_replacement_d2_126}


def pbs_replacement_d2_127(pbs_replacement_127):
    feature = _clean(pbs_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_127'] = {'inputs': ['pbs_replacement_127'], 'func': pbs_replacement_d2_127}


def pbs_replacement_d2_128(pbs_replacement_128):
    feature = _clean(pbs_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_128'] = {'inputs': ['pbs_replacement_128'], 'func': pbs_replacement_d2_128}


def pbs_replacement_d2_129(pbs_replacement_129):
    feature = _clean(pbs_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_129'] = {'inputs': ['pbs_replacement_129'], 'func': pbs_replacement_d2_129}


def pbs_replacement_d2_130(pbs_replacement_130):
    feature = _clean(pbs_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_130'] = {'inputs': ['pbs_replacement_130'], 'func': pbs_replacement_d2_130}


def pbs_replacement_d2_131(pbs_replacement_131):
    feature = _clean(pbs_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_131'] = {'inputs': ['pbs_replacement_131'], 'func': pbs_replacement_d2_131}


def pbs_replacement_d2_132(pbs_replacement_132):
    feature = _clean(pbs_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_132'] = {'inputs': ['pbs_replacement_132'], 'func': pbs_replacement_d2_132}


def pbs_replacement_d2_133(pbs_replacement_133):
    feature = _clean(pbs_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_133'] = {'inputs': ['pbs_replacement_133'], 'func': pbs_replacement_d2_133}


def pbs_replacement_d2_134(pbs_replacement_134):
    feature = _clean(pbs_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_134'] = {'inputs': ['pbs_replacement_134'], 'func': pbs_replacement_d2_134}


def pbs_replacement_d2_135(pbs_replacement_135):
    feature = _clean(pbs_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_135'] = {'inputs': ['pbs_replacement_135'], 'func': pbs_replacement_d2_135}


def pbs_replacement_d2_136(pbs_replacement_136):
    feature = _clean(pbs_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_136'] = {'inputs': ['pbs_replacement_136'], 'func': pbs_replacement_d2_136}


def pbs_replacement_d2_137(pbs_replacement_137):
    feature = _clean(pbs_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_137'] = {'inputs': ['pbs_replacement_137'], 'func': pbs_replacement_d2_137}


def pbs_replacement_d2_138(pbs_replacement_138):
    feature = _clean(pbs_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_138'] = {'inputs': ['pbs_replacement_138'], 'func': pbs_replacement_d2_138}


def pbs_replacement_d2_139(pbs_replacement_139):
    feature = _clean(pbs_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_139'] = {'inputs': ['pbs_replacement_139'], 'func': pbs_replacement_d2_139}


def pbs_replacement_d2_140(pbs_replacement_140):
    feature = _clean(pbs_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_140'] = {'inputs': ['pbs_replacement_140'], 'func': pbs_replacement_d2_140}


def pbs_replacement_d2_141(pbs_replacement_141):
    feature = _clean(pbs_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_141'] = {'inputs': ['pbs_replacement_141'], 'func': pbs_replacement_d2_141}


def pbs_replacement_d2_142(pbs_replacement_142):
    feature = _clean(pbs_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_142'] = {'inputs': ['pbs_replacement_142'], 'func': pbs_replacement_d2_142}


def pbs_replacement_d2_143(pbs_replacement_143):
    feature = _clean(pbs_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_143'] = {'inputs': ['pbs_replacement_143'], 'func': pbs_replacement_d2_143}


def pbs_replacement_d2_144(pbs_replacement_144):
    feature = _clean(pbs_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_144'] = {'inputs': ['pbs_replacement_144'], 'func': pbs_replacement_d2_144}


def pbs_replacement_d2_145(pbs_replacement_145):
    feature = _clean(pbs_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_145'] = {'inputs': ['pbs_replacement_145'], 'func': pbs_replacement_d2_145}


def pbs_replacement_d2_146(pbs_replacement_146):
    feature = _clean(pbs_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_146'] = {'inputs': ['pbs_replacement_146'], 'func': pbs_replacement_d2_146}


def pbs_replacement_d2_147(pbs_replacement_147):
    feature = _clean(pbs_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_147'] = {'inputs': ['pbs_replacement_147'], 'func': pbs_replacement_d2_147}


def pbs_replacement_d2_148(pbs_replacement_148):
    feature = _clean(pbs_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_148'] = {'inputs': ['pbs_replacement_148'], 'func': pbs_replacement_d2_148}


def pbs_replacement_d2_149(pbs_replacement_149):
    feature = _clean(pbs_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_149'] = {'inputs': ['pbs_replacement_149'], 'func': pbs_replacement_d2_149}


def pbs_replacement_d2_150(pbs_replacement_150):
    feature = _clean(pbs_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_150'] = {'inputs': ['pbs_replacement_150'], 'func': pbs_replacement_d2_150}


def pbs_replacement_d2_151(pbs_replacement_151):
    feature = _clean(pbs_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_151'] = {'inputs': ['pbs_replacement_151'], 'func': pbs_replacement_d2_151}


def pbs_replacement_d2_152(pbs_replacement_152):
    feature = _clean(pbs_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_152'] = {'inputs': ['pbs_replacement_152'], 'func': pbs_replacement_d2_152}


def pbs_replacement_d2_153(pbs_replacement_153):
    feature = _clean(pbs_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_153'] = {'inputs': ['pbs_replacement_153'], 'func': pbs_replacement_d2_153}


def pbs_replacement_d2_154(pbs_replacement_154):
    feature = _clean(pbs_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_154'] = {'inputs': ['pbs_replacement_154'], 'func': pbs_replacement_d2_154}


def pbs_replacement_d2_155(pbs_replacement_155):
    feature = _clean(pbs_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_155'] = {'inputs': ['pbs_replacement_155'], 'func': pbs_replacement_d2_155}


def pbs_replacement_d2_156(pbs_replacement_156):
    feature = _clean(pbs_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_156'] = {'inputs': ['pbs_replacement_156'], 'func': pbs_replacement_d2_156}


def pbs_replacement_d2_157(pbs_replacement_157):
    feature = _clean(pbs_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_157'] = {'inputs': ['pbs_replacement_157'], 'func': pbs_replacement_d2_157}


def pbs_replacement_d2_158(pbs_replacement_158):
    feature = _clean(pbs_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_158'] = {'inputs': ['pbs_replacement_158'], 'func': pbs_replacement_d2_158}


def pbs_replacement_d2_159(pbs_replacement_159):
    feature = _clean(pbs_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_159'] = {'inputs': ['pbs_replacement_159'], 'func': pbs_replacement_d2_159}


def pbs_replacement_d2_160(pbs_replacement_160):
    feature = _clean(pbs_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_160'] = {'inputs': ['pbs_replacement_160'], 'func': pbs_replacement_d2_160}


def pbs_replacement_d2_161(pbs_replacement_161):
    feature = _clean(pbs_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_161'] = {'inputs': ['pbs_replacement_161'], 'func': pbs_replacement_d2_161}


def pbs_replacement_d2_162(pbs_replacement_162):
    feature = _clean(pbs_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_162'] = {'inputs': ['pbs_replacement_162'], 'func': pbs_replacement_d2_162}


def pbs_replacement_d2_163(pbs_replacement_163):
    feature = _clean(pbs_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_163'] = {'inputs': ['pbs_replacement_163'], 'func': pbs_replacement_d2_163}


def pbs_replacement_d2_164(pbs_replacement_164):
    feature = _clean(pbs_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_164'] = {'inputs': ['pbs_replacement_164'], 'func': pbs_replacement_d2_164}


def pbs_replacement_d2_165(pbs_replacement_165):
    feature = _clean(pbs_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_165'] = {'inputs': ['pbs_replacement_165'], 'func': pbs_replacement_d2_165}


def pbs_replacement_d2_166(pbs_replacement_166):
    feature = _clean(pbs_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_166'] = {'inputs': ['pbs_replacement_166'], 'func': pbs_replacement_d2_166}


def pbs_replacement_d2_167(pbs_replacement_167):
    feature = _clean(pbs_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_167'] = {'inputs': ['pbs_replacement_167'], 'func': pbs_replacement_d2_167}


def pbs_replacement_d2_168(pbs_replacement_168):
    feature = _clean(pbs_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_168'] = {'inputs': ['pbs_replacement_168'], 'func': pbs_replacement_d2_168}


def pbs_replacement_d2_169(pbs_replacement_169):
    feature = _clean(pbs_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_169'] = {'inputs': ['pbs_replacement_169'], 'func': pbs_replacement_d2_169}


def pbs_replacement_d2_170(pbs_replacement_170):
    feature = _clean(pbs_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_170'] = {'inputs': ['pbs_replacement_170'], 'func': pbs_replacement_d2_170}


def pbs_replacement_d2_171(pbs_replacement_171):
    feature = _clean(pbs_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_171'] = {'inputs': ['pbs_replacement_171'], 'func': pbs_replacement_d2_171}


def pbs_replacement_d2_172(pbs_replacement_172):
    feature = _clean(pbs_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_172'] = {'inputs': ['pbs_replacement_172'], 'func': pbs_replacement_d2_172}


def pbs_replacement_d2_173(pbs_replacement_173):
    feature = _clean(pbs_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_173'] = {'inputs': ['pbs_replacement_173'], 'func': pbs_replacement_d2_173}


def pbs_replacement_d2_174(pbs_replacement_174):
    feature = _clean(pbs_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_174'] = {'inputs': ['pbs_replacement_174'], 'func': pbs_replacement_d2_174}


def pbs_replacement_d2_175(pbs_replacement_175):
    feature = _clean(pbs_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
PBS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['pbs_replacement_d2_175'] = {'inputs': ['pbs_replacement_175'], 'func': pbs_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pbs_base_universe_d2_001_pbs_002_range_expansion_10_002(pbs_002_range_expansion_10_002):
    return _base_universe_d2(pbs_002_range_expansion_10_002, 1)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_001_pbs_002_range_expansion_10_002'] = {'inputs': ['pbs_002_range_expansion_10_002'], 'func': pbs_base_universe_d2_001_pbs_002_range_expansion_10_002}


def pbs_base_universe_d2_002_pbs_004_close_location_42_004(pbs_004_close_location_42_004):
    return _base_universe_d2(pbs_004_close_location_42_004, 2)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_002_pbs_004_close_location_42_004'] = {'inputs': ['pbs_004_close_location_42_004'], 'func': pbs_base_universe_d2_002_pbs_004_close_location_42_004}


def pbs_base_universe_d2_003_pbs_005_atr_move_63_005(pbs_005_atr_move_63_005):
    return _base_universe_d2(pbs_005_atr_move_63_005, 3)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_003_pbs_005_atr_move_63_005'] = {'inputs': ['pbs_005_atr_move_63_005'], 'func': pbs_base_universe_d2_003_pbs_005_atr_move_63_005}


def pbs_base_universe_d2_004_pbs_008_range_expansion_189_008(pbs_008_range_expansion_189_008):
    return _base_universe_d2(pbs_008_range_expansion_189_008, 4)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_004_pbs_008_range_expansion_189_008'] = {'inputs': ['pbs_008_range_expansion_189_008'], 'func': pbs_base_universe_d2_004_pbs_008_range_expansion_189_008}


def pbs_base_universe_d2_005_pbs_010_close_location_378_010(pbs_010_close_location_378_010):
    return _base_universe_d2(pbs_010_close_location_378_010, 5)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_005_pbs_010_close_location_378_010'] = {'inputs': ['pbs_010_close_location_378_010'], 'func': pbs_base_universe_d2_005_pbs_010_close_location_378_010}


def pbs_base_universe_d2_006_pbs_011_atr_move_504_011(pbs_011_atr_move_504_011):
    return _base_universe_d2(pbs_011_atr_move_504_011, 6)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_006_pbs_011_atr_move_504_011'] = {'inputs': ['pbs_011_atr_move_504_011'], 'func': pbs_base_universe_d2_006_pbs_011_atr_move_504_011}


def pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014(pbs_014_range_expansion_1260_014):
    return _base_universe_d2(pbs_014_range_expansion_1260_014, 7)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014'] = {'inputs': ['pbs_014_range_expansion_1260_014'], 'func': pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014}


def pbs_base_universe_d2_008_pbs_016_close_location_5_016(pbs_016_close_location_5_016):
    return _base_universe_d2(pbs_016_close_location_5_016, 8)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_008_pbs_016_close_location_5_016'] = {'inputs': ['pbs_016_close_location_5_016'], 'func': pbs_base_universe_d2_008_pbs_016_close_location_5_016}


def pbs_base_universe_d2_009_pbs_017_atr_move_10_017(pbs_017_atr_move_10_017):
    return _base_universe_d2(pbs_017_atr_move_10_017, 9)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_009_pbs_017_atr_move_10_017'] = {'inputs': ['pbs_017_atr_move_10_017'], 'func': pbs_base_universe_d2_009_pbs_017_atr_move_10_017}


def pbs_base_universe_d2_010_pbs_020_range_expansion_63_020(pbs_020_range_expansion_63_020):
    return _base_universe_d2(pbs_020_range_expansion_63_020, 10)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_010_pbs_020_range_expansion_63_020'] = {'inputs': ['pbs_020_range_expansion_63_020'], 'func': pbs_base_universe_d2_010_pbs_020_range_expansion_63_020}


def pbs_base_universe_d2_011_pbs_022_close_location_126_022(pbs_022_close_location_126_022):
    return _base_universe_d2(pbs_022_close_location_126_022, 11)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_011_pbs_022_close_location_126_022'] = {'inputs': ['pbs_022_close_location_126_022'], 'func': pbs_base_universe_d2_011_pbs_022_close_location_126_022}


def pbs_base_universe_d2_012_pbs_023_atr_move_189_023(pbs_023_atr_move_189_023):
    return _base_universe_d2(pbs_023_atr_move_189_023, 12)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_012_pbs_023_atr_move_189_023'] = {'inputs': ['pbs_023_atr_move_189_023'], 'func': pbs_base_universe_d2_012_pbs_023_atr_move_189_023}


def pbs_base_universe_d2_013_pbs_026_range_expansion_504_026(pbs_026_range_expansion_504_026):
    return _base_universe_d2(pbs_026_range_expansion_504_026, 13)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_013_pbs_026_range_expansion_504_026'] = {'inputs': ['pbs_026_range_expansion_504_026'], 'func': pbs_base_universe_d2_013_pbs_026_range_expansion_504_026}


def pbs_base_universe_d2_014_pbs_028_close_location_1008_028(pbs_028_close_location_1008_028):
    return _base_universe_d2(pbs_028_close_location_1008_028, 14)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_014_pbs_028_close_location_1008_028'] = {'inputs': ['pbs_028_close_location_1008_028'], 'func': pbs_base_universe_d2_014_pbs_028_close_location_1008_028}


def pbs_base_universe_d2_015_pbs_029_atr_move_1260_029(pbs_029_atr_move_1260_029):
    return _base_universe_d2(pbs_029_atr_move_1260_029, 15)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_015_pbs_029_atr_move_1260_029'] = {'inputs': ['pbs_029_atr_move_1260_029'], 'func': pbs_base_universe_d2_015_pbs_029_atr_move_1260_029}


def pbs_base_universe_d2_016_pbs_basefill_001(pbs_basefill_001):
    return _base_universe_d2(pbs_basefill_001, 16)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_016_pbs_basefill_001'] = {'inputs': ['pbs_basefill_001'], 'func': pbs_base_universe_d2_016_pbs_basefill_001}


def pbs_base_universe_d2_017_pbs_basefill_003(pbs_basefill_003):
    return _base_universe_d2(pbs_basefill_003, 17)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_017_pbs_basefill_003'] = {'inputs': ['pbs_basefill_003'], 'func': pbs_base_universe_d2_017_pbs_basefill_003}


def pbs_base_universe_d2_018_pbs_basefill_006(pbs_basefill_006):
    return _base_universe_d2(pbs_basefill_006, 18)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_018_pbs_basefill_006'] = {'inputs': ['pbs_basefill_006'], 'func': pbs_base_universe_d2_018_pbs_basefill_006}


def pbs_base_universe_d2_019_pbs_basefill_007(pbs_basefill_007):
    return _base_universe_d2(pbs_basefill_007, 19)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_019_pbs_basefill_007'] = {'inputs': ['pbs_basefill_007'], 'func': pbs_base_universe_d2_019_pbs_basefill_007}


def pbs_base_universe_d2_020_pbs_basefill_009(pbs_basefill_009):
    return _base_universe_d2(pbs_basefill_009, 20)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_020_pbs_basefill_009'] = {'inputs': ['pbs_basefill_009'], 'func': pbs_base_universe_d2_020_pbs_basefill_009}


def pbs_base_universe_d2_021_pbs_basefill_012(pbs_basefill_012):
    return _base_universe_d2(pbs_basefill_012, 21)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_021_pbs_basefill_012'] = {'inputs': ['pbs_basefill_012'], 'func': pbs_base_universe_d2_021_pbs_basefill_012}


def pbs_base_universe_d2_022_pbs_basefill_013(pbs_basefill_013):
    return _base_universe_d2(pbs_basefill_013, 22)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_022_pbs_basefill_013'] = {'inputs': ['pbs_basefill_013'], 'func': pbs_base_universe_d2_022_pbs_basefill_013}


def pbs_base_universe_d2_023_pbs_basefill_015(pbs_basefill_015):
    return _base_universe_d2(pbs_basefill_015, 23)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_023_pbs_basefill_015'] = {'inputs': ['pbs_basefill_015'], 'func': pbs_base_universe_d2_023_pbs_basefill_015}


def pbs_base_universe_d2_024_pbs_basefill_018(pbs_basefill_018):
    return _base_universe_d2(pbs_basefill_018, 24)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_024_pbs_basefill_018'] = {'inputs': ['pbs_basefill_018'], 'func': pbs_base_universe_d2_024_pbs_basefill_018}


def pbs_base_universe_d2_025_pbs_basefill_019(pbs_basefill_019):
    return _base_universe_d2(pbs_basefill_019, 25)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_025_pbs_basefill_019'] = {'inputs': ['pbs_basefill_019'], 'func': pbs_base_universe_d2_025_pbs_basefill_019}


def pbs_base_universe_d2_026_pbs_basefill_021(pbs_basefill_021):
    return _base_universe_d2(pbs_basefill_021, 26)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_026_pbs_basefill_021'] = {'inputs': ['pbs_basefill_021'], 'func': pbs_base_universe_d2_026_pbs_basefill_021}


def pbs_base_universe_d2_027_pbs_basefill_024(pbs_basefill_024):
    return _base_universe_d2(pbs_basefill_024, 27)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_027_pbs_basefill_024'] = {'inputs': ['pbs_basefill_024'], 'func': pbs_base_universe_d2_027_pbs_basefill_024}


def pbs_base_universe_d2_028_pbs_basefill_025(pbs_basefill_025):
    return _base_universe_d2(pbs_basefill_025, 28)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_028_pbs_basefill_025'] = {'inputs': ['pbs_basefill_025'], 'func': pbs_base_universe_d2_028_pbs_basefill_025}


def pbs_base_universe_d2_029_pbs_basefill_027(pbs_basefill_027):
    return _base_universe_d2(pbs_basefill_027, 29)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_029_pbs_basefill_027'] = {'inputs': ['pbs_basefill_027'], 'func': pbs_base_universe_d2_029_pbs_basefill_027}


def pbs_base_universe_d2_030_pbs_basefill_030(pbs_basefill_030):
    return _base_universe_d2(pbs_basefill_030, 30)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_030_pbs_basefill_030'] = {'inputs': ['pbs_basefill_030'], 'func': pbs_base_universe_d2_030_pbs_basefill_030}


def pbs_base_universe_d2_031_pbs_basefill_031(pbs_basefill_031):
    return _base_universe_d2(pbs_basefill_031, 31)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_031_pbs_basefill_031'] = {'inputs': ['pbs_basefill_031'], 'func': pbs_base_universe_d2_031_pbs_basefill_031}


def pbs_base_universe_d2_032_pbs_basefill_032(pbs_basefill_032):
    return _base_universe_d2(pbs_basefill_032, 32)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_032_pbs_basefill_032'] = {'inputs': ['pbs_basefill_032'], 'func': pbs_base_universe_d2_032_pbs_basefill_032}


def pbs_base_universe_d2_033_pbs_basefill_033(pbs_basefill_033):
    return _base_universe_d2(pbs_basefill_033, 33)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_033_pbs_basefill_033'] = {'inputs': ['pbs_basefill_033'], 'func': pbs_base_universe_d2_033_pbs_basefill_033}


def pbs_base_universe_d2_034_pbs_basefill_034(pbs_basefill_034):
    return _base_universe_d2(pbs_basefill_034, 34)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_034_pbs_basefill_034'] = {'inputs': ['pbs_basefill_034'], 'func': pbs_base_universe_d2_034_pbs_basefill_034}


def pbs_base_universe_d2_035_pbs_basefill_035(pbs_basefill_035):
    return _base_universe_d2(pbs_basefill_035, 35)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_035_pbs_basefill_035'] = {'inputs': ['pbs_basefill_035'], 'func': pbs_base_universe_d2_035_pbs_basefill_035}


def pbs_base_universe_d2_036_pbs_basefill_036(pbs_basefill_036):
    return _base_universe_d2(pbs_basefill_036, 36)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_036_pbs_basefill_036'] = {'inputs': ['pbs_basefill_036'], 'func': pbs_base_universe_d2_036_pbs_basefill_036}


def pbs_base_universe_d2_037_pbs_basefill_037(pbs_basefill_037):
    return _base_universe_d2(pbs_basefill_037, 37)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_037_pbs_basefill_037'] = {'inputs': ['pbs_basefill_037'], 'func': pbs_base_universe_d2_037_pbs_basefill_037}


def pbs_base_universe_d2_038_pbs_basefill_038(pbs_basefill_038):
    return _base_universe_d2(pbs_basefill_038, 38)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_038_pbs_basefill_038'] = {'inputs': ['pbs_basefill_038'], 'func': pbs_base_universe_d2_038_pbs_basefill_038}


def pbs_base_universe_d2_039_pbs_basefill_039(pbs_basefill_039):
    return _base_universe_d2(pbs_basefill_039, 39)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_039_pbs_basefill_039'] = {'inputs': ['pbs_basefill_039'], 'func': pbs_base_universe_d2_039_pbs_basefill_039}


def pbs_base_universe_d2_040_pbs_basefill_040(pbs_basefill_040):
    return _base_universe_d2(pbs_basefill_040, 40)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_040_pbs_basefill_040'] = {'inputs': ['pbs_basefill_040'], 'func': pbs_base_universe_d2_040_pbs_basefill_040}


def pbs_base_universe_d2_041_pbs_basefill_041(pbs_basefill_041):
    return _base_universe_d2(pbs_basefill_041, 41)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_041_pbs_basefill_041'] = {'inputs': ['pbs_basefill_041'], 'func': pbs_base_universe_d2_041_pbs_basefill_041}


def pbs_base_universe_d2_042_pbs_basefill_042(pbs_basefill_042):
    return _base_universe_d2(pbs_basefill_042, 42)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_042_pbs_basefill_042'] = {'inputs': ['pbs_basefill_042'], 'func': pbs_base_universe_d2_042_pbs_basefill_042}


def pbs_base_universe_d2_043_pbs_basefill_043(pbs_basefill_043):
    return _base_universe_d2(pbs_basefill_043, 43)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_043_pbs_basefill_043'] = {'inputs': ['pbs_basefill_043'], 'func': pbs_base_universe_d2_043_pbs_basefill_043}


def pbs_base_universe_d2_044_pbs_basefill_044(pbs_basefill_044):
    return _base_universe_d2(pbs_basefill_044, 44)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_044_pbs_basefill_044'] = {'inputs': ['pbs_basefill_044'], 'func': pbs_base_universe_d2_044_pbs_basefill_044}


def pbs_base_universe_d2_045_pbs_basefill_045(pbs_basefill_045):
    return _base_universe_d2(pbs_basefill_045, 45)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_045_pbs_basefill_045'] = {'inputs': ['pbs_basefill_045'], 'func': pbs_base_universe_d2_045_pbs_basefill_045}


def pbs_base_universe_d2_046_pbs_basefill_046(pbs_basefill_046):
    return _base_universe_d2(pbs_basefill_046, 46)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_046_pbs_basefill_046'] = {'inputs': ['pbs_basefill_046'], 'func': pbs_base_universe_d2_046_pbs_basefill_046}


def pbs_base_universe_d2_047_pbs_basefill_047(pbs_basefill_047):
    return _base_universe_d2(pbs_basefill_047, 47)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_047_pbs_basefill_047'] = {'inputs': ['pbs_basefill_047'], 'func': pbs_base_universe_d2_047_pbs_basefill_047}


def pbs_base_universe_d2_048_pbs_basefill_048(pbs_basefill_048):
    return _base_universe_d2(pbs_basefill_048, 48)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_048_pbs_basefill_048'] = {'inputs': ['pbs_basefill_048'], 'func': pbs_base_universe_d2_048_pbs_basefill_048}


def pbs_base_universe_d2_049_pbs_basefill_049(pbs_basefill_049):
    return _base_universe_d2(pbs_basefill_049, 49)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_049_pbs_basefill_049'] = {'inputs': ['pbs_basefill_049'], 'func': pbs_base_universe_d2_049_pbs_basefill_049}


def pbs_base_universe_d2_050_pbs_basefill_050(pbs_basefill_050):
    return _base_universe_d2(pbs_basefill_050, 50)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_050_pbs_basefill_050'] = {'inputs': ['pbs_basefill_050'], 'func': pbs_base_universe_d2_050_pbs_basefill_050}


def pbs_base_universe_d2_051_pbs_basefill_051(pbs_basefill_051):
    return _base_universe_d2(pbs_basefill_051, 51)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_051_pbs_basefill_051'] = {'inputs': ['pbs_basefill_051'], 'func': pbs_base_universe_d2_051_pbs_basefill_051}


def pbs_base_universe_d2_052_pbs_basefill_052(pbs_basefill_052):
    return _base_universe_d2(pbs_basefill_052, 52)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_052_pbs_basefill_052'] = {'inputs': ['pbs_basefill_052'], 'func': pbs_base_universe_d2_052_pbs_basefill_052}


def pbs_base_universe_d2_053_pbs_basefill_053(pbs_basefill_053):
    return _base_universe_d2(pbs_basefill_053, 53)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_053_pbs_basefill_053'] = {'inputs': ['pbs_basefill_053'], 'func': pbs_base_universe_d2_053_pbs_basefill_053}


def pbs_base_universe_d2_054_pbs_basefill_054(pbs_basefill_054):
    return _base_universe_d2(pbs_basefill_054, 54)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_054_pbs_basefill_054'] = {'inputs': ['pbs_basefill_054'], 'func': pbs_base_universe_d2_054_pbs_basefill_054}


def pbs_base_universe_d2_055_pbs_basefill_055(pbs_basefill_055):
    return _base_universe_d2(pbs_basefill_055, 55)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_055_pbs_basefill_055'] = {'inputs': ['pbs_basefill_055'], 'func': pbs_base_universe_d2_055_pbs_basefill_055}


def pbs_base_universe_d2_056_pbs_basefill_056(pbs_basefill_056):
    return _base_universe_d2(pbs_basefill_056, 56)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_056_pbs_basefill_056'] = {'inputs': ['pbs_basefill_056'], 'func': pbs_base_universe_d2_056_pbs_basefill_056}


def pbs_base_universe_d2_057_pbs_basefill_057(pbs_basefill_057):
    return _base_universe_d2(pbs_basefill_057, 57)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_057_pbs_basefill_057'] = {'inputs': ['pbs_basefill_057'], 'func': pbs_base_universe_d2_057_pbs_basefill_057}


def pbs_base_universe_d2_058_pbs_basefill_058(pbs_basefill_058):
    return _base_universe_d2(pbs_basefill_058, 58)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_058_pbs_basefill_058'] = {'inputs': ['pbs_basefill_058'], 'func': pbs_base_universe_d2_058_pbs_basefill_058}


def pbs_base_universe_d2_059_pbs_basefill_059(pbs_basefill_059):
    return _base_universe_d2(pbs_basefill_059, 59)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_059_pbs_basefill_059'] = {'inputs': ['pbs_basefill_059'], 'func': pbs_base_universe_d2_059_pbs_basefill_059}


def pbs_base_universe_d2_060_pbs_basefill_060(pbs_basefill_060):
    return _base_universe_d2(pbs_basefill_060, 60)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_060_pbs_basefill_060'] = {'inputs': ['pbs_basefill_060'], 'func': pbs_base_universe_d2_060_pbs_basefill_060}


def pbs_base_universe_d2_061_pbs_basefill_061(pbs_basefill_061):
    return _base_universe_d2(pbs_basefill_061, 61)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_061_pbs_basefill_061'] = {'inputs': ['pbs_basefill_061'], 'func': pbs_base_universe_d2_061_pbs_basefill_061}


def pbs_base_universe_d2_062_pbs_basefill_062(pbs_basefill_062):
    return _base_universe_d2(pbs_basefill_062, 62)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_062_pbs_basefill_062'] = {'inputs': ['pbs_basefill_062'], 'func': pbs_base_universe_d2_062_pbs_basefill_062}


def pbs_base_universe_d2_063_pbs_basefill_063(pbs_basefill_063):
    return _base_universe_d2(pbs_basefill_063, 63)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_063_pbs_basefill_063'] = {'inputs': ['pbs_basefill_063'], 'func': pbs_base_universe_d2_063_pbs_basefill_063}


def pbs_base_universe_d2_064_pbs_basefill_064(pbs_basefill_064):
    return _base_universe_d2(pbs_basefill_064, 64)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_064_pbs_basefill_064'] = {'inputs': ['pbs_basefill_064'], 'func': pbs_base_universe_d2_064_pbs_basefill_064}


def pbs_base_universe_d2_065_pbs_basefill_065(pbs_basefill_065):
    return _base_universe_d2(pbs_basefill_065, 65)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_065_pbs_basefill_065'] = {'inputs': ['pbs_basefill_065'], 'func': pbs_base_universe_d2_065_pbs_basefill_065}


def pbs_base_universe_d2_066_pbs_basefill_066(pbs_basefill_066):
    return _base_universe_d2(pbs_basefill_066, 66)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_066_pbs_basefill_066'] = {'inputs': ['pbs_basefill_066'], 'func': pbs_base_universe_d2_066_pbs_basefill_066}


def pbs_base_universe_d2_067_pbs_basefill_067(pbs_basefill_067):
    return _base_universe_d2(pbs_basefill_067, 67)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_067_pbs_basefill_067'] = {'inputs': ['pbs_basefill_067'], 'func': pbs_base_universe_d2_067_pbs_basefill_067}


def pbs_base_universe_d2_068_pbs_basefill_068(pbs_basefill_068):
    return _base_universe_d2(pbs_basefill_068, 68)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_068_pbs_basefill_068'] = {'inputs': ['pbs_basefill_068'], 'func': pbs_base_universe_d2_068_pbs_basefill_068}


def pbs_base_universe_d2_069_pbs_basefill_069(pbs_basefill_069):
    return _base_universe_d2(pbs_basefill_069, 69)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_069_pbs_basefill_069'] = {'inputs': ['pbs_basefill_069'], 'func': pbs_base_universe_d2_069_pbs_basefill_069}


def pbs_base_universe_d2_070_pbs_basefill_070(pbs_basefill_070):
    return _base_universe_d2(pbs_basefill_070, 70)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_070_pbs_basefill_070'] = {'inputs': ['pbs_basefill_070'], 'func': pbs_base_universe_d2_070_pbs_basefill_070}


def pbs_base_universe_d2_071_pbs_basefill_071(pbs_basefill_071):
    return _base_universe_d2(pbs_basefill_071, 71)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_071_pbs_basefill_071'] = {'inputs': ['pbs_basefill_071'], 'func': pbs_base_universe_d2_071_pbs_basefill_071}


def pbs_base_universe_d2_072_pbs_basefill_072(pbs_basefill_072):
    return _base_universe_d2(pbs_basefill_072, 72)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_072_pbs_basefill_072'] = {'inputs': ['pbs_basefill_072'], 'func': pbs_base_universe_d2_072_pbs_basefill_072}


def pbs_base_universe_d2_073_pbs_basefill_073(pbs_basefill_073):
    return _base_universe_d2(pbs_basefill_073, 73)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_073_pbs_basefill_073'] = {'inputs': ['pbs_basefill_073'], 'func': pbs_base_universe_d2_073_pbs_basefill_073}


def pbs_base_universe_d2_074_pbs_basefill_074(pbs_basefill_074):
    return _base_universe_d2(pbs_basefill_074, 74)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_074_pbs_basefill_074'] = {'inputs': ['pbs_basefill_074'], 'func': pbs_base_universe_d2_074_pbs_basefill_074}


def pbs_base_universe_d2_075_pbs_basefill_075(pbs_basefill_075):
    return _base_universe_d2(pbs_basefill_075, 75)
PBS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['pbs_base_universe_d2_075_pbs_basefill_075'] = {'inputs': ['pbs_basefill_075'], 'func': pbs_base_universe_d2_075_pbs_basefill_075}
