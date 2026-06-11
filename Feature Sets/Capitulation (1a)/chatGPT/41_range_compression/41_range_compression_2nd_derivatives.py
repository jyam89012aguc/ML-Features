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



def rcp_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def rcp_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def rcp_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def rcp_154_rcp_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def rcp_155_rcp_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















RANGE_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    'rcp_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': rcp_001_realized_vol_z_roc_1},
    'rcp_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': rcp_007_realized_vol_z_roc_5},
    'rcp_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': rcp_013_realized_vol_z_roc_42},
    'rcp_154_rcp_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': rcp_154_rcp_019_realized_vol_z_42_019_roc_126},
    'rcp_155_rcp_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': rcp_155_rcp_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def rc_replacement_d2_001(rc_replacement_001):
    feature = _clean(rc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_001'] = {'inputs': ['rc_replacement_001'], 'func': rc_replacement_d2_001}


def rc_replacement_d2_002(rc_replacement_002):
    feature = _clean(rc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_002'] = {'inputs': ['rc_replacement_002'], 'func': rc_replacement_d2_002}


def rc_replacement_d2_003(rc_replacement_003):
    feature = _clean(rc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_003'] = {'inputs': ['rc_replacement_003'], 'func': rc_replacement_d2_003}


def rc_replacement_d2_004(rc_replacement_004):
    feature = _clean(rc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_004'] = {'inputs': ['rc_replacement_004'], 'func': rc_replacement_d2_004}


def rc_replacement_d2_005(rc_replacement_005):
    feature = _clean(rc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_005'] = {'inputs': ['rc_replacement_005'], 'func': rc_replacement_d2_005}


def rc_replacement_d2_006(rc_replacement_006):
    feature = _clean(rc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_006'] = {'inputs': ['rc_replacement_006'], 'func': rc_replacement_d2_006}


def rc_replacement_d2_007(rc_replacement_007):
    feature = _clean(rc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_007'] = {'inputs': ['rc_replacement_007'], 'func': rc_replacement_d2_007}


def rc_replacement_d2_008(rc_replacement_008):
    feature = _clean(rc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_008'] = {'inputs': ['rc_replacement_008'], 'func': rc_replacement_d2_008}


def rc_replacement_d2_009(rc_replacement_009):
    feature = _clean(rc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_009'] = {'inputs': ['rc_replacement_009'], 'func': rc_replacement_d2_009}


def rc_replacement_d2_010(rc_replacement_010):
    feature = _clean(rc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_010'] = {'inputs': ['rc_replacement_010'], 'func': rc_replacement_d2_010}


def rc_replacement_d2_011(rc_replacement_011):
    feature = _clean(rc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_011'] = {'inputs': ['rc_replacement_011'], 'func': rc_replacement_d2_011}


def rc_replacement_d2_012(rc_replacement_012):
    feature = _clean(rc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_012'] = {'inputs': ['rc_replacement_012'], 'func': rc_replacement_d2_012}


def rc_replacement_d2_013(rc_replacement_013):
    feature = _clean(rc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_013'] = {'inputs': ['rc_replacement_013'], 'func': rc_replacement_d2_013}


def rc_replacement_d2_014(rc_replacement_014):
    feature = _clean(rc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_014'] = {'inputs': ['rc_replacement_014'], 'func': rc_replacement_d2_014}


def rc_replacement_d2_015(rc_replacement_015):
    feature = _clean(rc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_015'] = {'inputs': ['rc_replacement_015'], 'func': rc_replacement_d2_015}


def rc_replacement_d2_016(rc_replacement_016):
    feature = _clean(rc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_016'] = {'inputs': ['rc_replacement_016'], 'func': rc_replacement_d2_016}


def rc_replacement_d2_017(rc_replacement_017):
    feature = _clean(rc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_017'] = {'inputs': ['rc_replacement_017'], 'func': rc_replacement_d2_017}


def rc_replacement_d2_018(rc_replacement_018):
    feature = _clean(rc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_018'] = {'inputs': ['rc_replacement_018'], 'func': rc_replacement_d2_018}


def rc_replacement_d2_019(rc_replacement_019):
    feature = _clean(rc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_019'] = {'inputs': ['rc_replacement_019'], 'func': rc_replacement_d2_019}


def rc_replacement_d2_020(rc_replacement_020):
    feature = _clean(rc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_020'] = {'inputs': ['rc_replacement_020'], 'func': rc_replacement_d2_020}


def rc_replacement_d2_021(rc_replacement_021):
    feature = _clean(rc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_021'] = {'inputs': ['rc_replacement_021'], 'func': rc_replacement_d2_021}


def rc_replacement_d2_022(rc_replacement_022):
    feature = _clean(rc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_022'] = {'inputs': ['rc_replacement_022'], 'func': rc_replacement_d2_022}


def rc_replacement_d2_023(rc_replacement_023):
    feature = _clean(rc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_023'] = {'inputs': ['rc_replacement_023'], 'func': rc_replacement_d2_023}


def rc_replacement_d2_024(rc_replacement_024):
    feature = _clean(rc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_024'] = {'inputs': ['rc_replacement_024'], 'func': rc_replacement_d2_024}


def rc_replacement_d2_025(rc_replacement_025):
    feature = _clean(rc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_025'] = {'inputs': ['rc_replacement_025'], 'func': rc_replacement_d2_025}


def rc_replacement_d2_026(rc_replacement_026):
    feature = _clean(rc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_026'] = {'inputs': ['rc_replacement_026'], 'func': rc_replacement_d2_026}


def rc_replacement_d2_027(rc_replacement_027):
    feature = _clean(rc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_027'] = {'inputs': ['rc_replacement_027'], 'func': rc_replacement_d2_027}


def rc_replacement_d2_028(rc_replacement_028):
    feature = _clean(rc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_028'] = {'inputs': ['rc_replacement_028'], 'func': rc_replacement_d2_028}


def rc_replacement_d2_029(rc_replacement_029):
    feature = _clean(rc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_029'] = {'inputs': ['rc_replacement_029'], 'func': rc_replacement_d2_029}


def rc_replacement_d2_030(rc_replacement_030):
    feature = _clean(rc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_030'] = {'inputs': ['rc_replacement_030'], 'func': rc_replacement_d2_030}


def rc_replacement_d2_031(rc_replacement_031):
    feature = _clean(rc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_031'] = {'inputs': ['rc_replacement_031'], 'func': rc_replacement_d2_031}


def rc_replacement_d2_032(rc_replacement_032):
    feature = _clean(rc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_032'] = {'inputs': ['rc_replacement_032'], 'func': rc_replacement_d2_032}


def rc_replacement_d2_033(rc_replacement_033):
    feature = _clean(rc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_033'] = {'inputs': ['rc_replacement_033'], 'func': rc_replacement_d2_033}


def rc_replacement_d2_034(rc_replacement_034):
    feature = _clean(rc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_034'] = {'inputs': ['rc_replacement_034'], 'func': rc_replacement_d2_034}


def rc_replacement_d2_035(rc_replacement_035):
    feature = _clean(rc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_035'] = {'inputs': ['rc_replacement_035'], 'func': rc_replacement_d2_035}


def rc_replacement_d2_036(rc_replacement_036):
    feature = _clean(rc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_036'] = {'inputs': ['rc_replacement_036'], 'func': rc_replacement_d2_036}


def rc_replacement_d2_037(rc_replacement_037):
    feature = _clean(rc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_037'] = {'inputs': ['rc_replacement_037'], 'func': rc_replacement_d2_037}


def rc_replacement_d2_038(rc_replacement_038):
    feature = _clean(rc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_038'] = {'inputs': ['rc_replacement_038'], 'func': rc_replacement_d2_038}


def rc_replacement_d2_039(rc_replacement_039):
    feature = _clean(rc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_039'] = {'inputs': ['rc_replacement_039'], 'func': rc_replacement_d2_039}


def rc_replacement_d2_040(rc_replacement_040):
    feature = _clean(rc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_040'] = {'inputs': ['rc_replacement_040'], 'func': rc_replacement_d2_040}


def rc_replacement_d2_041(rc_replacement_041):
    feature = _clean(rc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_041'] = {'inputs': ['rc_replacement_041'], 'func': rc_replacement_d2_041}


def rc_replacement_d2_042(rc_replacement_042):
    feature = _clean(rc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_042'] = {'inputs': ['rc_replacement_042'], 'func': rc_replacement_d2_042}


def rc_replacement_d2_043(rc_replacement_043):
    feature = _clean(rc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_043'] = {'inputs': ['rc_replacement_043'], 'func': rc_replacement_d2_043}


def rc_replacement_d2_044(rc_replacement_044):
    feature = _clean(rc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_044'] = {'inputs': ['rc_replacement_044'], 'func': rc_replacement_d2_044}


def rc_replacement_d2_045(rc_replacement_045):
    feature = _clean(rc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_045'] = {'inputs': ['rc_replacement_045'], 'func': rc_replacement_d2_045}


def rc_replacement_d2_046(rc_replacement_046):
    feature = _clean(rc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_046'] = {'inputs': ['rc_replacement_046'], 'func': rc_replacement_d2_046}


def rc_replacement_d2_047(rc_replacement_047):
    feature = _clean(rc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_047'] = {'inputs': ['rc_replacement_047'], 'func': rc_replacement_d2_047}


def rc_replacement_d2_048(rc_replacement_048):
    feature = _clean(rc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_048'] = {'inputs': ['rc_replacement_048'], 'func': rc_replacement_d2_048}


def rc_replacement_d2_049(rc_replacement_049):
    feature = _clean(rc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_049'] = {'inputs': ['rc_replacement_049'], 'func': rc_replacement_d2_049}


def rc_replacement_d2_050(rc_replacement_050):
    feature = _clean(rc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_050'] = {'inputs': ['rc_replacement_050'], 'func': rc_replacement_d2_050}


def rc_replacement_d2_051(rc_replacement_051):
    feature = _clean(rc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_051'] = {'inputs': ['rc_replacement_051'], 'func': rc_replacement_d2_051}


def rc_replacement_d2_052(rc_replacement_052):
    feature = _clean(rc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_052'] = {'inputs': ['rc_replacement_052'], 'func': rc_replacement_d2_052}


def rc_replacement_d2_053(rc_replacement_053):
    feature = _clean(rc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_053'] = {'inputs': ['rc_replacement_053'], 'func': rc_replacement_d2_053}


def rc_replacement_d2_054(rc_replacement_054):
    feature = _clean(rc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_054'] = {'inputs': ['rc_replacement_054'], 'func': rc_replacement_d2_054}


def rc_replacement_d2_055(rc_replacement_055):
    feature = _clean(rc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_055'] = {'inputs': ['rc_replacement_055'], 'func': rc_replacement_d2_055}


def rc_replacement_d2_056(rc_replacement_056):
    feature = _clean(rc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_056'] = {'inputs': ['rc_replacement_056'], 'func': rc_replacement_d2_056}


def rc_replacement_d2_057(rc_replacement_057):
    feature = _clean(rc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_057'] = {'inputs': ['rc_replacement_057'], 'func': rc_replacement_d2_057}


def rc_replacement_d2_058(rc_replacement_058):
    feature = _clean(rc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_058'] = {'inputs': ['rc_replacement_058'], 'func': rc_replacement_d2_058}


def rc_replacement_d2_059(rc_replacement_059):
    feature = _clean(rc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_059'] = {'inputs': ['rc_replacement_059'], 'func': rc_replacement_d2_059}


def rc_replacement_d2_060(rc_replacement_060):
    feature = _clean(rc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_060'] = {'inputs': ['rc_replacement_060'], 'func': rc_replacement_d2_060}


def rc_replacement_d2_061(rc_replacement_061):
    feature = _clean(rc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_061'] = {'inputs': ['rc_replacement_061'], 'func': rc_replacement_d2_061}


def rc_replacement_d2_062(rc_replacement_062):
    feature = _clean(rc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_062'] = {'inputs': ['rc_replacement_062'], 'func': rc_replacement_d2_062}


def rc_replacement_d2_063(rc_replacement_063):
    feature = _clean(rc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_063'] = {'inputs': ['rc_replacement_063'], 'func': rc_replacement_d2_063}


def rc_replacement_d2_064(rc_replacement_064):
    feature = _clean(rc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_064'] = {'inputs': ['rc_replacement_064'], 'func': rc_replacement_d2_064}


def rc_replacement_d2_065(rc_replacement_065):
    feature = _clean(rc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_065'] = {'inputs': ['rc_replacement_065'], 'func': rc_replacement_d2_065}


def rc_replacement_d2_066(rc_replacement_066):
    feature = _clean(rc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_066'] = {'inputs': ['rc_replacement_066'], 'func': rc_replacement_d2_066}


def rc_replacement_d2_067(rc_replacement_067):
    feature = _clean(rc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_067'] = {'inputs': ['rc_replacement_067'], 'func': rc_replacement_d2_067}


def rc_replacement_d2_068(rc_replacement_068):
    feature = _clean(rc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_068'] = {'inputs': ['rc_replacement_068'], 'func': rc_replacement_d2_068}


def rc_replacement_d2_069(rc_replacement_069):
    feature = _clean(rc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_069'] = {'inputs': ['rc_replacement_069'], 'func': rc_replacement_d2_069}


def rc_replacement_d2_070(rc_replacement_070):
    feature = _clean(rc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_070'] = {'inputs': ['rc_replacement_070'], 'func': rc_replacement_d2_070}


def rc_replacement_d2_071(rc_replacement_071):
    feature = _clean(rc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_071'] = {'inputs': ['rc_replacement_071'], 'func': rc_replacement_d2_071}


def rc_replacement_d2_072(rc_replacement_072):
    feature = _clean(rc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_072'] = {'inputs': ['rc_replacement_072'], 'func': rc_replacement_d2_072}


def rc_replacement_d2_073(rc_replacement_073):
    feature = _clean(rc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_073'] = {'inputs': ['rc_replacement_073'], 'func': rc_replacement_d2_073}


def rc_replacement_d2_074(rc_replacement_074):
    feature = _clean(rc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_074'] = {'inputs': ['rc_replacement_074'], 'func': rc_replacement_d2_074}


def rc_replacement_d2_075(rc_replacement_075):
    feature = _clean(rc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_075'] = {'inputs': ['rc_replacement_075'], 'func': rc_replacement_d2_075}


def rc_replacement_d2_076(rc_replacement_076):
    feature = _clean(rc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_076'] = {'inputs': ['rc_replacement_076'], 'func': rc_replacement_d2_076}


def rc_replacement_d2_077(rc_replacement_077):
    feature = _clean(rc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_077'] = {'inputs': ['rc_replacement_077'], 'func': rc_replacement_d2_077}


def rc_replacement_d2_078(rc_replacement_078):
    feature = _clean(rc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_078'] = {'inputs': ['rc_replacement_078'], 'func': rc_replacement_d2_078}


def rc_replacement_d2_079(rc_replacement_079):
    feature = _clean(rc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_079'] = {'inputs': ['rc_replacement_079'], 'func': rc_replacement_d2_079}


def rc_replacement_d2_080(rc_replacement_080):
    feature = _clean(rc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_080'] = {'inputs': ['rc_replacement_080'], 'func': rc_replacement_d2_080}


def rc_replacement_d2_081(rc_replacement_081):
    feature = _clean(rc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_081'] = {'inputs': ['rc_replacement_081'], 'func': rc_replacement_d2_081}


def rc_replacement_d2_082(rc_replacement_082):
    feature = _clean(rc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_082'] = {'inputs': ['rc_replacement_082'], 'func': rc_replacement_d2_082}


def rc_replacement_d2_083(rc_replacement_083):
    feature = _clean(rc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_083'] = {'inputs': ['rc_replacement_083'], 'func': rc_replacement_d2_083}


def rc_replacement_d2_084(rc_replacement_084):
    feature = _clean(rc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_084'] = {'inputs': ['rc_replacement_084'], 'func': rc_replacement_d2_084}


def rc_replacement_d2_085(rc_replacement_085):
    feature = _clean(rc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_085'] = {'inputs': ['rc_replacement_085'], 'func': rc_replacement_d2_085}


def rc_replacement_d2_086(rc_replacement_086):
    feature = _clean(rc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_086'] = {'inputs': ['rc_replacement_086'], 'func': rc_replacement_d2_086}


def rc_replacement_d2_087(rc_replacement_087):
    feature = _clean(rc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_087'] = {'inputs': ['rc_replacement_087'], 'func': rc_replacement_d2_087}


def rc_replacement_d2_088(rc_replacement_088):
    feature = _clean(rc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_088'] = {'inputs': ['rc_replacement_088'], 'func': rc_replacement_d2_088}


def rc_replacement_d2_089(rc_replacement_089):
    feature = _clean(rc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_089'] = {'inputs': ['rc_replacement_089'], 'func': rc_replacement_d2_089}


def rc_replacement_d2_090(rc_replacement_090):
    feature = _clean(rc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_090'] = {'inputs': ['rc_replacement_090'], 'func': rc_replacement_d2_090}


def rc_replacement_d2_091(rc_replacement_091):
    feature = _clean(rc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_091'] = {'inputs': ['rc_replacement_091'], 'func': rc_replacement_d2_091}


def rc_replacement_d2_092(rc_replacement_092):
    feature = _clean(rc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_092'] = {'inputs': ['rc_replacement_092'], 'func': rc_replacement_d2_092}


def rc_replacement_d2_093(rc_replacement_093):
    feature = _clean(rc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_093'] = {'inputs': ['rc_replacement_093'], 'func': rc_replacement_d2_093}


def rc_replacement_d2_094(rc_replacement_094):
    feature = _clean(rc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_094'] = {'inputs': ['rc_replacement_094'], 'func': rc_replacement_d2_094}


def rc_replacement_d2_095(rc_replacement_095):
    feature = _clean(rc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_095'] = {'inputs': ['rc_replacement_095'], 'func': rc_replacement_d2_095}


def rc_replacement_d2_096(rc_replacement_096):
    feature = _clean(rc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_096'] = {'inputs': ['rc_replacement_096'], 'func': rc_replacement_d2_096}


def rc_replacement_d2_097(rc_replacement_097):
    feature = _clean(rc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_097'] = {'inputs': ['rc_replacement_097'], 'func': rc_replacement_d2_097}


def rc_replacement_d2_098(rc_replacement_098):
    feature = _clean(rc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_098'] = {'inputs': ['rc_replacement_098'], 'func': rc_replacement_d2_098}


def rc_replacement_d2_099(rc_replacement_099):
    feature = _clean(rc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_099'] = {'inputs': ['rc_replacement_099'], 'func': rc_replacement_d2_099}


def rc_replacement_d2_100(rc_replacement_100):
    feature = _clean(rc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_100'] = {'inputs': ['rc_replacement_100'], 'func': rc_replacement_d2_100}


def rc_replacement_d2_101(rc_replacement_101):
    feature = _clean(rc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_101'] = {'inputs': ['rc_replacement_101'], 'func': rc_replacement_d2_101}


def rc_replacement_d2_102(rc_replacement_102):
    feature = _clean(rc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_102'] = {'inputs': ['rc_replacement_102'], 'func': rc_replacement_d2_102}


def rc_replacement_d2_103(rc_replacement_103):
    feature = _clean(rc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_103'] = {'inputs': ['rc_replacement_103'], 'func': rc_replacement_d2_103}


def rc_replacement_d2_104(rc_replacement_104):
    feature = _clean(rc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_104'] = {'inputs': ['rc_replacement_104'], 'func': rc_replacement_d2_104}


def rc_replacement_d2_105(rc_replacement_105):
    feature = _clean(rc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_105'] = {'inputs': ['rc_replacement_105'], 'func': rc_replacement_d2_105}


def rc_replacement_d2_106(rc_replacement_106):
    feature = _clean(rc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_106'] = {'inputs': ['rc_replacement_106'], 'func': rc_replacement_d2_106}


def rc_replacement_d2_107(rc_replacement_107):
    feature = _clean(rc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_107'] = {'inputs': ['rc_replacement_107'], 'func': rc_replacement_d2_107}


def rc_replacement_d2_108(rc_replacement_108):
    feature = _clean(rc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_108'] = {'inputs': ['rc_replacement_108'], 'func': rc_replacement_d2_108}


def rc_replacement_d2_109(rc_replacement_109):
    feature = _clean(rc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_109'] = {'inputs': ['rc_replacement_109'], 'func': rc_replacement_d2_109}


def rc_replacement_d2_110(rc_replacement_110):
    feature = _clean(rc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_110'] = {'inputs': ['rc_replacement_110'], 'func': rc_replacement_d2_110}


def rc_replacement_d2_111(rc_replacement_111):
    feature = _clean(rc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_111'] = {'inputs': ['rc_replacement_111'], 'func': rc_replacement_d2_111}


def rc_replacement_d2_112(rc_replacement_112):
    feature = _clean(rc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_112'] = {'inputs': ['rc_replacement_112'], 'func': rc_replacement_d2_112}


def rc_replacement_d2_113(rc_replacement_113):
    feature = _clean(rc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_113'] = {'inputs': ['rc_replacement_113'], 'func': rc_replacement_d2_113}


def rc_replacement_d2_114(rc_replacement_114):
    feature = _clean(rc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_114'] = {'inputs': ['rc_replacement_114'], 'func': rc_replacement_d2_114}


def rc_replacement_d2_115(rc_replacement_115):
    feature = _clean(rc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_115'] = {'inputs': ['rc_replacement_115'], 'func': rc_replacement_d2_115}


def rc_replacement_d2_116(rc_replacement_116):
    feature = _clean(rc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_116'] = {'inputs': ['rc_replacement_116'], 'func': rc_replacement_d2_116}


def rc_replacement_d2_117(rc_replacement_117):
    feature = _clean(rc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_117'] = {'inputs': ['rc_replacement_117'], 'func': rc_replacement_d2_117}


def rc_replacement_d2_118(rc_replacement_118):
    feature = _clean(rc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_118'] = {'inputs': ['rc_replacement_118'], 'func': rc_replacement_d2_118}


def rc_replacement_d2_119(rc_replacement_119):
    feature = _clean(rc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_119'] = {'inputs': ['rc_replacement_119'], 'func': rc_replacement_d2_119}


def rc_replacement_d2_120(rc_replacement_120):
    feature = _clean(rc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_120'] = {'inputs': ['rc_replacement_120'], 'func': rc_replacement_d2_120}


def rc_replacement_d2_121(rc_replacement_121):
    feature = _clean(rc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_121'] = {'inputs': ['rc_replacement_121'], 'func': rc_replacement_d2_121}


def rc_replacement_d2_122(rc_replacement_122):
    feature = _clean(rc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_122'] = {'inputs': ['rc_replacement_122'], 'func': rc_replacement_d2_122}


def rc_replacement_d2_123(rc_replacement_123):
    feature = _clean(rc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_123'] = {'inputs': ['rc_replacement_123'], 'func': rc_replacement_d2_123}


def rc_replacement_d2_124(rc_replacement_124):
    feature = _clean(rc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_124'] = {'inputs': ['rc_replacement_124'], 'func': rc_replacement_d2_124}


def rc_replacement_d2_125(rc_replacement_125):
    feature = _clean(rc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_125'] = {'inputs': ['rc_replacement_125'], 'func': rc_replacement_d2_125}


def rc_replacement_d2_126(rc_replacement_126):
    feature = _clean(rc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_126'] = {'inputs': ['rc_replacement_126'], 'func': rc_replacement_d2_126}


def rc_replacement_d2_127(rc_replacement_127):
    feature = _clean(rc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_127'] = {'inputs': ['rc_replacement_127'], 'func': rc_replacement_d2_127}


def rc_replacement_d2_128(rc_replacement_128):
    feature = _clean(rc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_128'] = {'inputs': ['rc_replacement_128'], 'func': rc_replacement_d2_128}


def rc_replacement_d2_129(rc_replacement_129):
    feature = _clean(rc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_129'] = {'inputs': ['rc_replacement_129'], 'func': rc_replacement_d2_129}


def rc_replacement_d2_130(rc_replacement_130):
    feature = _clean(rc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_130'] = {'inputs': ['rc_replacement_130'], 'func': rc_replacement_d2_130}


def rc_replacement_d2_131(rc_replacement_131):
    feature = _clean(rc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_131'] = {'inputs': ['rc_replacement_131'], 'func': rc_replacement_d2_131}


def rc_replacement_d2_132(rc_replacement_132):
    feature = _clean(rc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_132'] = {'inputs': ['rc_replacement_132'], 'func': rc_replacement_d2_132}


def rc_replacement_d2_133(rc_replacement_133):
    feature = _clean(rc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_133'] = {'inputs': ['rc_replacement_133'], 'func': rc_replacement_d2_133}


def rc_replacement_d2_134(rc_replacement_134):
    feature = _clean(rc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_134'] = {'inputs': ['rc_replacement_134'], 'func': rc_replacement_d2_134}


def rc_replacement_d2_135(rc_replacement_135):
    feature = _clean(rc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_135'] = {'inputs': ['rc_replacement_135'], 'func': rc_replacement_d2_135}


def rc_replacement_d2_136(rc_replacement_136):
    feature = _clean(rc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_136'] = {'inputs': ['rc_replacement_136'], 'func': rc_replacement_d2_136}


def rc_replacement_d2_137(rc_replacement_137):
    feature = _clean(rc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_137'] = {'inputs': ['rc_replacement_137'], 'func': rc_replacement_d2_137}


def rc_replacement_d2_138(rc_replacement_138):
    feature = _clean(rc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_138'] = {'inputs': ['rc_replacement_138'], 'func': rc_replacement_d2_138}


def rc_replacement_d2_139(rc_replacement_139):
    feature = _clean(rc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_139'] = {'inputs': ['rc_replacement_139'], 'func': rc_replacement_d2_139}


def rc_replacement_d2_140(rc_replacement_140):
    feature = _clean(rc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_140'] = {'inputs': ['rc_replacement_140'], 'func': rc_replacement_d2_140}


def rc_replacement_d2_141(rc_replacement_141):
    feature = _clean(rc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_141'] = {'inputs': ['rc_replacement_141'], 'func': rc_replacement_d2_141}


def rc_replacement_d2_142(rc_replacement_142):
    feature = _clean(rc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_142'] = {'inputs': ['rc_replacement_142'], 'func': rc_replacement_d2_142}


def rc_replacement_d2_143(rc_replacement_143):
    feature = _clean(rc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_143'] = {'inputs': ['rc_replacement_143'], 'func': rc_replacement_d2_143}


def rc_replacement_d2_144(rc_replacement_144):
    feature = _clean(rc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_144'] = {'inputs': ['rc_replacement_144'], 'func': rc_replacement_d2_144}


def rc_replacement_d2_145(rc_replacement_145):
    feature = _clean(rc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_145'] = {'inputs': ['rc_replacement_145'], 'func': rc_replacement_d2_145}


def rc_replacement_d2_146(rc_replacement_146):
    feature = _clean(rc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_146'] = {'inputs': ['rc_replacement_146'], 'func': rc_replacement_d2_146}


def rc_replacement_d2_147(rc_replacement_147):
    feature = _clean(rc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_147'] = {'inputs': ['rc_replacement_147'], 'func': rc_replacement_d2_147}


def rc_replacement_d2_148(rc_replacement_148):
    feature = _clean(rc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_148'] = {'inputs': ['rc_replacement_148'], 'func': rc_replacement_d2_148}


def rc_replacement_d2_149(rc_replacement_149):
    feature = _clean(rc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_149'] = {'inputs': ['rc_replacement_149'], 'func': rc_replacement_d2_149}


def rc_replacement_d2_150(rc_replacement_150):
    feature = _clean(rc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_150'] = {'inputs': ['rc_replacement_150'], 'func': rc_replacement_d2_150}


def rc_replacement_d2_151(rc_replacement_151):
    feature = _clean(rc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_151'] = {'inputs': ['rc_replacement_151'], 'func': rc_replacement_d2_151}


def rc_replacement_d2_152(rc_replacement_152):
    feature = _clean(rc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_152'] = {'inputs': ['rc_replacement_152'], 'func': rc_replacement_d2_152}


def rc_replacement_d2_153(rc_replacement_153):
    feature = _clean(rc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_153'] = {'inputs': ['rc_replacement_153'], 'func': rc_replacement_d2_153}


def rc_replacement_d2_154(rc_replacement_154):
    feature = _clean(rc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_154'] = {'inputs': ['rc_replacement_154'], 'func': rc_replacement_d2_154}


def rc_replacement_d2_155(rc_replacement_155):
    feature = _clean(rc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_155'] = {'inputs': ['rc_replacement_155'], 'func': rc_replacement_d2_155}


def rc_replacement_d2_156(rc_replacement_156):
    feature = _clean(rc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_156'] = {'inputs': ['rc_replacement_156'], 'func': rc_replacement_d2_156}


def rc_replacement_d2_157(rc_replacement_157):
    feature = _clean(rc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_157'] = {'inputs': ['rc_replacement_157'], 'func': rc_replacement_d2_157}


def rc_replacement_d2_158(rc_replacement_158):
    feature = _clean(rc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_158'] = {'inputs': ['rc_replacement_158'], 'func': rc_replacement_d2_158}


def rc_replacement_d2_159(rc_replacement_159):
    feature = _clean(rc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_159'] = {'inputs': ['rc_replacement_159'], 'func': rc_replacement_d2_159}


def rc_replacement_d2_160(rc_replacement_160):
    feature = _clean(rc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_160'] = {'inputs': ['rc_replacement_160'], 'func': rc_replacement_d2_160}


def rc_replacement_d2_161(rc_replacement_161):
    feature = _clean(rc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_161'] = {'inputs': ['rc_replacement_161'], 'func': rc_replacement_d2_161}


def rc_replacement_d2_162(rc_replacement_162):
    feature = _clean(rc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_162'] = {'inputs': ['rc_replacement_162'], 'func': rc_replacement_d2_162}


def rc_replacement_d2_163(rc_replacement_163):
    feature = _clean(rc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_163'] = {'inputs': ['rc_replacement_163'], 'func': rc_replacement_d2_163}


def rc_replacement_d2_164(rc_replacement_164):
    feature = _clean(rc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_164'] = {'inputs': ['rc_replacement_164'], 'func': rc_replacement_d2_164}


def rc_replacement_d2_165(rc_replacement_165):
    feature = _clean(rc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_165'] = {'inputs': ['rc_replacement_165'], 'func': rc_replacement_d2_165}


def rc_replacement_d2_166(rc_replacement_166):
    feature = _clean(rc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_166'] = {'inputs': ['rc_replacement_166'], 'func': rc_replacement_d2_166}


def rc_replacement_d2_167(rc_replacement_167):
    feature = _clean(rc_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_167'] = {'inputs': ['rc_replacement_167'], 'func': rc_replacement_d2_167}


def rc_replacement_d2_168(rc_replacement_168):
    feature = _clean(rc_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_168'] = {'inputs': ['rc_replacement_168'], 'func': rc_replacement_d2_168}


def rc_replacement_d2_169(rc_replacement_169):
    feature = _clean(rc_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_169'] = {'inputs': ['rc_replacement_169'], 'func': rc_replacement_d2_169}


def rc_replacement_d2_170(rc_replacement_170):
    feature = _clean(rc_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_170'] = {'inputs': ['rc_replacement_170'], 'func': rc_replacement_d2_170}


def rc_replacement_d2_171(rc_replacement_171):
    feature = _clean(rc_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_171'] = {'inputs': ['rc_replacement_171'], 'func': rc_replacement_d2_171}


def rc_replacement_d2_172(rc_replacement_172):
    feature = _clean(rc_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_172'] = {'inputs': ['rc_replacement_172'], 'func': rc_replacement_d2_172}


def rc_replacement_d2_173(rc_replacement_173):
    feature = _clean(rc_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_173'] = {'inputs': ['rc_replacement_173'], 'func': rc_replacement_d2_173}


def rc_replacement_d2_174(rc_replacement_174):
    feature = _clean(rc_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_174'] = {'inputs': ['rc_replacement_174'], 'func': rc_replacement_d2_174}


def rc_replacement_d2_175(rc_replacement_175):
    feature = _clean(rc_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
RC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rc_replacement_d2_175'] = {'inputs': ['rc_replacement_175'], 'func': rc_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rcp_base_universe_d2_001_rcp_002_range_expansion_10_002(rcp_002_range_expansion_10_002):
    return _base_universe_d2(rcp_002_range_expansion_10_002, 1)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_001_rcp_002_range_expansion_10_002'] = {'inputs': ['rcp_002_range_expansion_10_002'], 'func': rcp_base_universe_d2_001_rcp_002_range_expansion_10_002}


def rcp_base_universe_d2_002_rcp_004_close_location_42_004(rcp_004_close_location_42_004):
    return _base_universe_d2(rcp_004_close_location_42_004, 2)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_002_rcp_004_close_location_42_004'] = {'inputs': ['rcp_004_close_location_42_004'], 'func': rcp_base_universe_d2_002_rcp_004_close_location_42_004}


def rcp_base_universe_d2_003_rcp_005_atr_move_63_005(rcp_005_atr_move_63_005):
    return _base_universe_d2(rcp_005_atr_move_63_005, 3)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_003_rcp_005_atr_move_63_005'] = {'inputs': ['rcp_005_atr_move_63_005'], 'func': rcp_base_universe_d2_003_rcp_005_atr_move_63_005}


def rcp_base_universe_d2_004_rcp_008_range_expansion_189_008(rcp_008_range_expansion_189_008):
    return _base_universe_d2(rcp_008_range_expansion_189_008, 4)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_004_rcp_008_range_expansion_189_008'] = {'inputs': ['rcp_008_range_expansion_189_008'], 'func': rcp_base_universe_d2_004_rcp_008_range_expansion_189_008}


def rcp_base_universe_d2_005_rcp_010_close_location_378_010(rcp_010_close_location_378_010):
    return _base_universe_d2(rcp_010_close_location_378_010, 5)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_005_rcp_010_close_location_378_010'] = {'inputs': ['rcp_010_close_location_378_010'], 'func': rcp_base_universe_d2_005_rcp_010_close_location_378_010}


def rcp_base_universe_d2_006_rcp_011_atr_move_504_011(rcp_011_atr_move_504_011):
    return _base_universe_d2(rcp_011_atr_move_504_011, 6)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_006_rcp_011_atr_move_504_011'] = {'inputs': ['rcp_011_atr_move_504_011'], 'func': rcp_base_universe_d2_006_rcp_011_atr_move_504_011}


def rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014(rcp_014_range_expansion_1260_014):
    return _base_universe_d2(rcp_014_range_expansion_1260_014, 7)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014'] = {'inputs': ['rcp_014_range_expansion_1260_014'], 'func': rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014}


def rcp_base_universe_d2_008_rcp_016_close_location_5_016(rcp_016_close_location_5_016):
    return _base_universe_d2(rcp_016_close_location_5_016, 8)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_008_rcp_016_close_location_5_016'] = {'inputs': ['rcp_016_close_location_5_016'], 'func': rcp_base_universe_d2_008_rcp_016_close_location_5_016}


def rcp_base_universe_d2_009_rcp_017_atr_move_10_017(rcp_017_atr_move_10_017):
    return _base_universe_d2(rcp_017_atr_move_10_017, 9)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_009_rcp_017_atr_move_10_017'] = {'inputs': ['rcp_017_atr_move_10_017'], 'func': rcp_base_universe_d2_009_rcp_017_atr_move_10_017}


def rcp_base_universe_d2_010_rcp_020_range_expansion_63_020(rcp_020_range_expansion_63_020):
    return _base_universe_d2(rcp_020_range_expansion_63_020, 10)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_010_rcp_020_range_expansion_63_020'] = {'inputs': ['rcp_020_range_expansion_63_020'], 'func': rcp_base_universe_d2_010_rcp_020_range_expansion_63_020}


def rcp_base_universe_d2_011_rcp_022_close_location_126_022(rcp_022_close_location_126_022):
    return _base_universe_d2(rcp_022_close_location_126_022, 11)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_011_rcp_022_close_location_126_022'] = {'inputs': ['rcp_022_close_location_126_022'], 'func': rcp_base_universe_d2_011_rcp_022_close_location_126_022}


def rcp_base_universe_d2_012_rcp_023_atr_move_189_023(rcp_023_atr_move_189_023):
    return _base_universe_d2(rcp_023_atr_move_189_023, 12)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_012_rcp_023_atr_move_189_023'] = {'inputs': ['rcp_023_atr_move_189_023'], 'func': rcp_base_universe_d2_012_rcp_023_atr_move_189_023}


def rcp_base_universe_d2_013_rcp_026_range_expansion_504_026(rcp_026_range_expansion_504_026):
    return _base_universe_d2(rcp_026_range_expansion_504_026, 13)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_013_rcp_026_range_expansion_504_026'] = {'inputs': ['rcp_026_range_expansion_504_026'], 'func': rcp_base_universe_d2_013_rcp_026_range_expansion_504_026}


def rcp_base_universe_d2_014_rcp_028_close_location_1008_028(rcp_028_close_location_1008_028):
    return _base_universe_d2(rcp_028_close_location_1008_028, 14)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_014_rcp_028_close_location_1008_028'] = {'inputs': ['rcp_028_close_location_1008_028'], 'func': rcp_base_universe_d2_014_rcp_028_close_location_1008_028}


def rcp_base_universe_d2_015_rcp_029_atr_move_1260_029(rcp_029_atr_move_1260_029):
    return _base_universe_d2(rcp_029_atr_move_1260_029, 15)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_015_rcp_029_atr_move_1260_029'] = {'inputs': ['rcp_029_atr_move_1260_029'], 'func': rcp_base_universe_d2_015_rcp_029_atr_move_1260_029}


def rcp_base_universe_d2_016_rcp_basefill_001(rcp_basefill_001):
    return _base_universe_d2(rcp_basefill_001, 16)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_016_rcp_basefill_001'] = {'inputs': ['rcp_basefill_001'], 'func': rcp_base_universe_d2_016_rcp_basefill_001}


def rcp_base_universe_d2_017_rcp_basefill_003(rcp_basefill_003):
    return _base_universe_d2(rcp_basefill_003, 17)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_017_rcp_basefill_003'] = {'inputs': ['rcp_basefill_003'], 'func': rcp_base_universe_d2_017_rcp_basefill_003}


def rcp_base_universe_d2_018_rcp_basefill_006(rcp_basefill_006):
    return _base_universe_d2(rcp_basefill_006, 18)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_018_rcp_basefill_006'] = {'inputs': ['rcp_basefill_006'], 'func': rcp_base_universe_d2_018_rcp_basefill_006}


def rcp_base_universe_d2_019_rcp_basefill_007(rcp_basefill_007):
    return _base_universe_d2(rcp_basefill_007, 19)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_019_rcp_basefill_007'] = {'inputs': ['rcp_basefill_007'], 'func': rcp_base_universe_d2_019_rcp_basefill_007}


def rcp_base_universe_d2_020_rcp_basefill_009(rcp_basefill_009):
    return _base_universe_d2(rcp_basefill_009, 20)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_020_rcp_basefill_009'] = {'inputs': ['rcp_basefill_009'], 'func': rcp_base_universe_d2_020_rcp_basefill_009}


def rcp_base_universe_d2_021_rcp_basefill_012(rcp_basefill_012):
    return _base_universe_d2(rcp_basefill_012, 21)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_021_rcp_basefill_012'] = {'inputs': ['rcp_basefill_012'], 'func': rcp_base_universe_d2_021_rcp_basefill_012}


def rcp_base_universe_d2_022_rcp_basefill_013(rcp_basefill_013):
    return _base_universe_d2(rcp_basefill_013, 22)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_022_rcp_basefill_013'] = {'inputs': ['rcp_basefill_013'], 'func': rcp_base_universe_d2_022_rcp_basefill_013}


def rcp_base_universe_d2_023_rcp_basefill_015(rcp_basefill_015):
    return _base_universe_d2(rcp_basefill_015, 23)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_023_rcp_basefill_015'] = {'inputs': ['rcp_basefill_015'], 'func': rcp_base_universe_d2_023_rcp_basefill_015}


def rcp_base_universe_d2_024_rcp_basefill_018(rcp_basefill_018):
    return _base_universe_d2(rcp_basefill_018, 24)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_024_rcp_basefill_018'] = {'inputs': ['rcp_basefill_018'], 'func': rcp_base_universe_d2_024_rcp_basefill_018}


def rcp_base_universe_d2_025_rcp_basefill_019(rcp_basefill_019):
    return _base_universe_d2(rcp_basefill_019, 25)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_025_rcp_basefill_019'] = {'inputs': ['rcp_basefill_019'], 'func': rcp_base_universe_d2_025_rcp_basefill_019}


def rcp_base_universe_d2_026_rcp_basefill_021(rcp_basefill_021):
    return _base_universe_d2(rcp_basefill_021, 26)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_026_rcp_basefill_021'] = {'inputs': ['rcp_basefill_021'], 'func': rcp_base_universe_d2_026_rcp_basefill_021}


def rcp_base_universe_d2_027_rcp_basefill_024(rcp_basefill_024):
    return _base_universe_d2(rcp_basefill_024, 27)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_027_rcp_basefill_024'] = {'inputs': ['rcp_basefill_024'], 'func': rcp_base_universe_d2_027_rcp_basefill_024}


def rcp_base_universe_d2_028_rcp_basefill_025(rcp_basefill_025):
    return _base_universe_d2(rcp_basefill_025, 28)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_028_rcp_basefill_025'] = {'inputs': ['rcp_basefill_025'], 'func': rcp_base_universe_d2_028_rcp_basefill_025}


def rcp_base_universe_d2_029_rcp_basefill_027(rcp_basefill_027):
    return _base_universe_d2(rcp_basefill_027, 29)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_029_rcp_basefill_027'] = {'inputs': ['rcp_basefill_027'], 'func': rcp_base_universe_d2_029_rcp_basefill_027}


def rcp_base_universe_d2_030_rcp_basefill_030(rcp_basefill_030):
    return _base_universe_d2(rcp_basefill_030, 30)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_030_rcp_basefill_030'] = {'inputs': ['rcp_basefill_030'], 'func': rcp_base_universe_d2_030_rcp_basefill_030}


def rcp_base_universe_d2_031_rcp_basefill_031(rcp_basefill_031):
    return _base_universe_d2(rcp_basefill_031, 31)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_031_rcp_basefill_031'] = {'inputs': ['rcp_basefill_031'], 'func': rcp_base_universe_d2_031_rcp_basefill_031}


def rcp_base_universe_d2_032_rcp_basefill_032(rcp_basefill_032):
    return _base_universe_d2(rcp_basefill_032, 32)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_032_rcp_basefill_032'] = {'inputs': ['rcp_basefill_032'], 'func': rcp_base_universe_d2_032_rcp_basefill_032}


def rcp_base_universe_d2_033_rcp_basefill_033(rcp_basefill_033):
    return _base_universe_d2(rcp_basefill_033, 33)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_033_rcp_basefill_033'] = {'inputs': ['rcp_basefill_033'], 'func': rcp_base_universe_d2_033_rcp_basefill_033}


def rcp_base_universe_d2_034_rcp_basefill_034(rcp_basefill_034):
    return _base_universe_d2(rcp_basefill_034, 34)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_034_rcp_basefill_034'] = {'inputs': ['rcp_basefill_034'], 'func': rcp_base_universe_d2_034_rcp_basefill_034}


def rcp_base_universe_d2_035_rcp_basefill_035(rcp_basefill_035):
    return _base_universe_d2(rcp_basefill_035, 35)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_035_rcp_basefill_035'] = {'inputs': ['rcp_basefill_035'], 'func': rcp_base_universe_d2_035_rcp_basefill_035}


def rcp_base_universe_d2_036_rcp_basefill_036(rcp_basefill_036):
    return _base_universe_d2(rcp_basefill_036, 36)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_036_rcp_basefill_036'] = {'inputs': ['rcp_basefill_036'], 'func': rcp_base_universe_d2_036_rcp_basefill_036}


def rcp_base_universe_d2_037_rcp_basefill_037(rcp_basefill_037):
    return _base_universe_d2(rcp_basefill_037, 37)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_037_rcp_basefill_037'] = {'inputs': ['rcp_basefill_037'], 'func': rcp_base_universe_d2_037_rcp_basefill_037}


def rcp_base_universe_d2_038_rcp_basefill_038(rcp_basefill_038):
    return _base_universe_d2(rcp_basefill_038, 38)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_038_rcp_basefill_038'] = {'inputs': ['rcp_basefill_038'], 'func': rcp_base_universe_d2_038_rcp_basefill_038}


def rcp_base_universe_d2_039_rcp_basefill_039(rcp_basefill_039):
    return _base_universe_d2(rcp_basefill_039, 39)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_039_rcp_basefill_039'] = {'inputs': ['rcp_basefill_039'], 'func': rcp_base_universe_d2_039_rcp_basefill_039}


def rcp_base_universe_d2_040_rcp_basefill_040(rcp_basefill_040):
    return _base_universe_d2(rcp_basefill_040, 40)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_040_rcp_basefill_040'] = {'inputs': ['rcp_basefill_040'], 'func': rcp_base_universe_d2_040_rcp_basefill_040}


def rcp_base_universe_d2_041_rcp_basefill_041(rcp_basefill_041):
    return _base_universe_d2(rcp_basefill_041, 41)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_041_rcp_basefill_041'] = {'inputs': ['rcp_basefill_041'], 'func': rcp_base_universe_d2_041_rcp_basefill_041}


def rcp_base_universe_d2_042_rcp_basefill_042(rcp_basefill_042):
    return _base_universe_d2(rcp_basefill_042, 42)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_042_rcp_basefill_042'] = {'inputs': ['rcp_basefill_042'], 'func': rcp_base_universe_d2_042_rcp_basefill_042}


def rcp_base_universe_d2_043_rcp_basefill_043(rcp_basefill_043):
    return _base_universe_d2(rcp_basefill_043, 43)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_043_rcp_basefill_043'] = {'inputs': ['rcp_basefill_043'], 'func': rcp_base_universe_d2_043_rcp_basefill_043}


def rcp_base_universe_d2_044_rcp_basefill_044(rcp_basefill_044):
    return _base_universe_d2(rcp_basefill_044, 44)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_044_rcp_basefill_044'] = {'inputs': ['rcp_basefill_044'], 'func': rcp_base_universe_d2_044_rcp_basefill_044}


def rcp_base_universe_d2_045_rcp_basefill_045(rcp_basefill_045):
    return _base_universe_d2(rcp_basefill_045, 45)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_045_rcp_basefill_045'] = {'inputs': ['rcp_basefill_045'], 'func': rcp_base_universe_d2_045_rcp_basefill_045}


def rcp_base_universe_d2_046_rcp_basefill_046(rcp_basefill_046):
    return _base_universe_d2(rcp_basefill_046, 46)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_046_rcp_basefill_046'] = {'inputs': ['rcp_basefill_046'], 'func': rcp_base_universe_d2_046_rcp_basefill_046}


def rcp_base_universe_d2_047_rcp_basefill_047(rcp_basefill_047):
    return _base_universe_d2(rcp_basefill_047, 47)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_047_rcp_basefill_047'] = {'inputs': ['rcp_basefill_047'], 'func': rcp_base_universe_d2_047_rcp_basefill_047}


def rcp_base_universe_d2_048_rcp_basefill_048(rcp_basefill_048):
    return _base_universe_d2(rcp_basefill_048, 48)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_048_rcp_basefill_048'] = {'inputs': ['rcp_basefill_048'], 'func': rcp_base_universe_d2_048_rcp_basefill_048}


def rcp_base_universe_d2_049_rcp_basefill_049(rcp_basefill_049):
    return _base_universe_d2(rcp_basefill_049, 49)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_049_rcp_basefill_049'] = {'inputs': ['rcp_basefill_049'], 'func': rcp_base_universe_d2_049_rcp_basefill_049}


def rcp_base_universe_d2_050_rcp_basefill_050(rcp_basefill_050):
    return _base_universe_d2(rcp_basefill_050, 50)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_050_rcp_basefill_050'] = {'inputs': ['rcp_basefill_050'], 'func': rcp_base_universe_d2_050_rcp_basefill_050}


def rcp_base_universe_d2_051_rcp_basefill_051(rcp_basefill_051):
    return _base_universe_d2(rcp_basefill_051, 51)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_051_rcp_basefill_051'] = {'inputs': ['rcp_basefill_051'], 'func': rcp_base_universe_d2_051_rcp_basefill_051}


def rcp_base_universe_d2_052_rcp_basefill_052(rcp_basefill_052):
    return _base_universe_d2(rcp_basefill_052, 52)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_052_rcp_basefill_052'] = {'inputs': ['rcp_basefill_052'], 'func': rcp_base_universe_d2_052_rcp_basefill_052}


def rcp_base_universe_d2_053_rcp_basefill_053(rcp_basefill_053):
    return _base_universe_d2(rcp_basefill_053, 53)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_053_rcp_basefill_053'] = {'inputs': ['rcp_basefill_053'], 'func': rcp_base_universe_d2_053_rcp_basefill_053}


def rcp_base_universe_d2_054_rcp_basefill_054(rcp_basefill_054):
    return _base_universe_d2(rcp_basefill_054, 54)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_054_rcp_basefill_054'] = {'inputs': ['rcp_basefill_054'], 'func': rcp_base_universe_d2_054_rcp_basefill_054}


def rcp_base_universe_d2_055_rcp_basefill_055(rcp_basefill_055):
    return _base_universe_d2(rcp_basefill_055, 55)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_055_rcp_basefill_055'] = {'inputs': ['rcp_basefill_055'], 'func': rcp_base_universe_d2_055_rcp_basefill_055}


def rcp_base_universe_d2_056_rcp_basefill_056(rcp_basefill_056):
    return _base_universe_d2(rcp_basefill_056, 56)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_056_rcp_basefill_056'] = {'inputs': ['rcp_basefill_056'], 'func': rcp_base_universe_d2_056_rcp_basefill_056}


def rcp_base_universe_d2_057_rcp_basefill_057(rcp_basefill_057):
    return _base_universe_d2(rcp_basefill_057, 57)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_057_rcp_basefill_057'] = {'inputs': ['rcp_basefill_057'], 'func': rcp_base_universe_d2_057_rcp_basefill_057}


def rcp_base_universe_d2_058_rcp_basefill_058(rcp_basefill_058):
    return _base_universe_d2(rcp_basefill_058, 58)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_058_rcp_basefill_058'] = {'inputs': ['rcp_basefill_058'], 'func': rcp_base_universe_d2_058_rcp_basefill_058}


def rcp_base_universe_d2_059_rcp_basefill_059(rcp_basefill_059):
    return _base_universe_d2(rcp_basefill_059, 59)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_059_rcp_basefill_059'] = {'inputs': ['rcp_basefill_059'], 'func': rcp_base_universe_d2_059_rcp_basefill_059}


def rcp_base_universe_d2_060_rcp_basefill_060(rcp_basefill_060):
    return _base_universe_d2(rcp_basefill_060, 60)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_060_rcp_basefill_060'] = {'inputs': ['rcp_basefill_060'], 'func': rcp_base_universe_d2_060_rcp_basefill_060}


def rcp_base_universe_d2_061_rcp_basefill_061(rcp_basefill_061):
    return _base_universe_d2(rcp_basefill_061, 61)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_061_rcp_basefill_061'] = {'inputs': ['rcp_basefill_061'], 'func': rcp_base_universe_d2_061_rcp_basefill_061}


def rcp_base_universe_d2_062_rcp_basefill_062(rcp_basefill_062):
    return _base_universe_d2(rcp_basefill_062, 62)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_062_rcp_basefill_062'] = {'inputs': ['rcp_basefill_062'], 'func': rcp_base_universe_d2_062_rcp_basefill_062}


def rcp_base_universe_d2_063_rcp_basefill_063(rcp_basefill_063):
    return _base_universe_d2(rcp_basefill_063, 63)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_063_rcp_basefill_063'] = {'inputs': ['rcp_basefill_063'], 'func': rcp_base_universe_d2_063_rcp_basefill_063}


def rcp_base_universe_d2_064_rcp_basefill_064(rcp_basefill_064):
    return _base_universe_d2(rcp_basefill_064, 64)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_064_rcp_basefill_064'] = {'inputs': ['rcp_basefill_064'], 'func': rcp_base_universe_d2_064_rcp_basefill_064}


def rcp_base_universe_d2_065_rcp_basefill_065(rcp_basefill_065):
    return _base_universe_d2(rcp_basefill_065, 65)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_065_rcp_basefill_065'] = {'inputs': ['rcp_basefill_065'], 'func': rcp_base_universe_d2_065_rcp_basefill_065}


def rcp_base_universe_d2_066_rcp_basefill_066(rcp_basefill_066):
    return _base_universe_d2(rcp_basefill_066, 66)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_066_rcp_basefill_066'] = {'inputs': ['rcp_basefill_066'], 'func': rcp_base_universe_d2_066_rcp_basefill_066}


def rcp_base_universe_d2_067_rcp_basefill_067(rcp_basefill_067):
    return _base_universe_d2(rcp_basefill_067, 67)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_067_rcp_basefill_067'] = {'inputs': ['rcp_basefill_067'], 'func': rcp_base_universe_d2_067_rcp_basefill_067}


def rcp_base_universe_d2_068_rcp_basefill_068(rcp_basefill_068):
    return _base_universe_d2(rcp_basefill_068, 68)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_068_rcp_basefill_068'] = {'inputs': ['rcp_basefill_068'], 'func': rcp_base_universe_d2_068_rcp_basefill_068}


def rcp_base_universe_d2_069_rcp_basefill_069(rcp_basefill_069):
    return _base_universe_d2(rcp_basefill_069, 69)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_069_rcp_basefill_069'] = {'inputs': ['rcp_basefill_069'], 'func': rcp_base_universe_d2_069_rcp_basefill_069}


def rcp_base_universe_d2_070_rcp_basefill_070(rcp_basefill_070):
    return _base_universe_d2(rcp_basefill_070, 70)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_070_rcp_basefill_070'] = {'inputs': ['rcp_basefill_070'], 'func': rcp_base_universe_d2_070_rcp_basefill_070}


def rcp_base_universe_d2_071_rcp_basefill_071(rcp_basefill_071):
    return _base_universe_d2(rcp_basefill_071, 71)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_071_rcp_basefill_071'] = {'inputs': ['rcp_basefill_071'], 'func': rcp_base_universe_d2_071_rcp_basefill_071}


def rcp_base_universe_d2_072_rcp_basefill_072(rcp_basefill_072):
    return _base_universe_d2(rcp_basefill_072, 72)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_072_rcp_basefill_072'] = {'inputs': ['rcp_basefill_072'], 'func': rcp_base_universe_d2_072_rcp_basefill_072}


def rcp_base_universe_d2_073_rcp_basefill_073(rcp_basefill_073):
    return _base_universe_d2(rcp_basefill_073, 73)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_073_rcp_basefill_073'] = {'inputs': ['rcp_basefill_073'], 'func': rcp_base_universe_d2_073_rcp_basefill_073}


def rcp_base_universe_d2_074_rcp_basefill_074(rcp_basefill_074):
    return _base_universe_d2(rcp_basefill_074, 74)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_074_rcp_basefill_074'] = {'inputs': ['rcp_basefill_074'], 'func': rcp_base_universe_d2_074_rcp_basefill_074}


def rcp_base_universe_d2_075_rcp_basefill_075(rcp_basefill_075):
    return _base_universe_d2(rcp_basefill_075, 75)
RCP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rcp_base_universe_d2_075_rcp_basefill_075'] = {'inputs': ['rcp_basefill_075'], 'func': rcp_base_universe_d2_075_rcp_basefill_075}
