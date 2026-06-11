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



def idr_001_realized_vol_z_roc_1(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 1)).reindex(feature.index)

def idr_007_realized_vol_z_roc_5(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 5)).reindex(feature.index)

def idr_013_realized_vol_z_roc_42(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 42)).reindex(feature.index)

def idr_154_idr_019_realized_vol_z_42_019_roc_126(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 126)).reindex(feature.index)

def idr_155_idr_025_realized_vol_z_378_025_roc_378(close):
    rv = _s(close).pct_change().rolling(21).std()
    feature = _z(rv, 252)
    return (_roc(feature, 378)).reindex(feature.index)






















INTRADAY_RANGE_REGISTRY_2ND_DERIVATIVES = {
    'idr_001_realized_vol_z_roc_1': {'inputs': ['close'], 'func': idr_001_realized_vol_z_roc_1},
    'idr_007_realized_vol_z_roc_5': {'inputs': ['close'], 'func': idr_007_realized_vol_z_roc_5},
    'idr_013_realized_vol_z_roc_42': {'inputs': ['close'], 'func': idr_013_realized_vol_z_roc_42},
    'idr_154_idr_019_realized_vol_z_42_019_roc_126': {'inputs': ['close'], 'func': idr_154_idr_019_realized_vol_z_42_019_roc_126},
    'idr_155_idr_025_realized_vol_z_378_025_roc_378': {'inputs': ['close'], 'func': idr_155_idr_025_realized_vol_z_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ir_replacement_d2_001(ir_replacement_001):
    feature = _clean(ir_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_001'] = {'inputs': ['ir_replacement_001'], 'func': ir_replacement_d2_001}


def ir_replacement_d2_002(ir_replacement_002):
    feature = _clean(ir_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_002'] = {'inputs': ['ir_replacement_002'], 'func': ir_replacement_d2_002}


def ir_replacement_d2_003(ir_replacement_003):
    feature = _clean(ir_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_003'] = {'inputs': ['ir_replacement_003'], 'func': ir_replacement_d2_003}


def ir_replacement_d2_004(ir_replacement_004):
    feature = _clean(ir_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_004'] = {'inputs': ['ir_replacement_004'], 'func': ir_replacement_d2_004}


def ir_replacement_d2_005(ir_replacement_005):
    feature = _clean(ir_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_005'] = {'inputs': ['ir_replacement_005'], 'func': ir_replacement_d2_005}


def ir_replacement_d2_006(ir_replacement_006):
    feature = _clean(ir_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_006'] = {'inputs': ['ir_replacement_006'], 'func': ir_replacement_d2_006}


def ir_replacement_d2_007(ir_replacement_007):
    feature = _clean(ir_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_007'] = {'inputs': ['ir_replacement_007'], 'func': ir_replacement_d2_007}


def ir_replacement_d2_008(ir_replacement_008):
    feature = _clean(ir_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_008'] = {'inputs': ['ir_replacement_008'], 'func': ir_replacement_d2_008}


def ir_replacement_d2_009(ir_replacement_009):
    feature = _clean(ir_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_009'] = {'inputs': ['ir_replacement_009'], 'func': ir_replacement_d2_009}


def ir_replacement_d2_010(ir_replacement_010):
    feature = _clean(ir_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_010'] = {'inputs': ['ir_replacement_010'], 'func': ir_replacement_d2_010}


def ir_replacement_d2_011(ir_replacement_011):
    feature = _clean(ir_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_011'] = {'inputs': ['ir_replacement_011'], 'func': ir_replacement_d2_011}


def ir_replacement_d2_012(ir_replacement_012):
    feature = _clean(ir_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_012'] = {'inputs': ['ir_replacement_012'], 'func': ir_replacement_d2_012}


def ir_replacement_d2_013(ir_replacement_013):
    feature = _clean(ir_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_013'] = {'inputs': ['ir_replacement_013'], 'func': ir_replacement_d2_013}


def ir_replacement_d2_014(ir_replacement_014):
    feature = _clean(ir_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_014'] = {'inputs': ['ir_replacement_014'], 'func': ir_replacement_d2_014}


def ir_replacement_d2_015(ir_replacement_015):
    feature = _clean(ir_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_015'] = {'inputs': ['ir_replacement_015'], 'func': ir_replacement_d2_015}


def ir_replacement_d2_016(ir_replacement_016):
    feature = _clean(ir_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_016'] = {'inputs': ['ir_replacement_016'], 'func': ir_replacement_d2_016}


def ir_replacement_d2_017(ir_replacement_017):
    feature = _clean(ir_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_017'] = {'inputs': ['ir_replacement_017'], 'func': ir_replacement_d2_017}


def ir_replacement_d2_018(ir_replacement_018):
    feature = _clean(ir_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_018'] = {'inputs': ['ir_replacement_018'], 'func': ir_replacement_d2_018}


def ir_replacement_d2_019(ir_replacement_019):
    feature = _clean(ir_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_019'] = {'inputs': ['ir_replacement_019'], 'func': ir_replacement_d2_019}


def ir_replacement_d2_020(ir_replacement_020):
    feature = _clean(ir_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_020'] = {'inputs': ['ir_replacement_020'], 'func': ir_replacement_d2_020}


def ir_replacement_d2_021(ir_replacement_021):
    feature = _clean(ir_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_021'] = {'inputs': ['ir_replacement_021'], 'func': ir_replacement_d2_021}


def ir_replacement_d2_022(ir_replacement_022):
    feature = _clean(ir_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_022'] = {'inputs': ['ir_replacement_022'], 'func': ir_replacement_d2_022}


def ir_replacement_d2_023(ir_replacement_023):
    feature = _clean(ir_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_023'] = {'inputs': ['ir_replacement_023'], 'func': ir_replacement_d2_023}


def ir_replacement_d2_024(ir_replacement_024):
    feature = _clean(ir_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_024'] = {'inputs': ['ir_replacement_024'], 'func': ir_replacement_d2_024}


def ir_replacement_d2_025(ir_replacement_025):
    feature = _clean(ir_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_025'] = {'inputs': ['ir_replacement_025'], 'func': ir_replacement_d2_025}


def ir_replacement_d2_026(ir_replacement_026):
    feature = _clean(ir_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_026'] = {'inputs': ['ir_replacement_026'], 'func': ir_replacement_d2_026}


def ir_replacement_d2_027(ir_replacement_027):
    feature = _clean(ir_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_027'] = {'inputs': ['ir_replacement_027'], 'func': ir_replacement_d2_027}


def ir_replacement_d2_028(ir_replacement_028):
    feature = _clean(ir_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_028'] = {'inputs': ['ir_replacement_028'], 'func': ir_replacement_d2_028}


def ir_replacement_d2_029(ir_replacement_029):
    feature = _clean(ir_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_029'] = {'inputs': ['ir_replacement_029'], 'func': ir_replacement_d2_029}


def ir_replacement_d2_030(ir_replacement_030):
    feature = _clean(ir_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_030'] = {'inputs': ['ir_replacement_030'], 'func': ir_replacement_d2_030}


def ir_replacement_d2_031(ir_replacement_031):
    feature = _clean(ir_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_031'] = {'inputs': ['ir_replacement_031'], 'func': ir_replacement_d2_031}


def ir_replacement_d2_032(ir_replacement_032):
    feature = _clean(ir_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_032'] = {'inputs': ['ir_replacement_032'], 'func': ir_replacement_d2_032}


def ir_replacement_d2_033(ir_replacement_033):
    feature = _clean(ir_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_033'] = {'inputs': ['ir_replacement_033'], 'func': ir_replacement_d2_033}


def ir_replacement_d2_034(ir_replacement_034):
    feature = _clean(ir_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_034'] = {'inputs': ['ir_replacement_034'], 'func': ir_replacement_d2_034}


def ir_replacement_d2_035(ir_replacement_035):
    feature = _clean(ir_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_035'] = {'inputs': ['ir_replacement_035'], 'func': ir_replacement_d2_035}


def ir_replacement_d2_036(ir_replacement_036):
    feature = _clean(ir_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_036'] = {'inputs': ['ir_replacement_036'], 'func': ir_replacement_d2_036}


def ir_replacement_d2_037(ir_replacement_037):
    feature = _clean(ir_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_037'] = {'inputs': ['ir_replacement_037'], 'func': ir_replacement_d2_037}


def ir_replacement_d2_038(ir_replacement_038):
    feature = _clean(ir_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_038'] = {'inputs': ['ir_replacement_038'], 'func': ir_replacement_d2_038}


def ir_replacement_d2_039(ir_replacement_039):
    feature = _clean(ir_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_039'] = {'inputs': ['ir_replacement_039'], 'func': ir_replacement_d2_039}


def ir_replacement_d2_040(ir_replacement_040):
    feature = _clean(ir_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_040'] = {'inputs': ['ir_replacement_040'], 'func': ir_replacement_d2_040}


def ir_replacement_d2_041(ir_replacement_041):
    feature = _clean(ir_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_041'] = {'inputs': ['ir_replacement_041'], 'func': ir_replacement_d2_041}


def ir_replacement_d2_042(ir_replacement_042):
    feature = _clean(ir_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_042'] = {'inputs': ['ir_replacement_042'], 'func': ir_replacement_d2_042}


def ir_replacement_d2_043(ir_replacement_043):
    feature = _clean(ir_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_043'] = {'inputs': ['ir_replacement_043'], 'func': ir_replacement_d2_043}


def ir_replacement_d2_044(ir_replacement_044):
    feature = _clean(ir_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_044'] = {'inputs': ['ir_replacement_044'], 'func': ir_replacement_d2_044}


def ir_replacement_d2_045(ir_replacement_045):
    feature = _clean(ir_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_045'] = {'inputs': ['ir_replacement_045'], 'func': ir_replacement_d2_045}


def ir_replacement_d2_046(ir_replacement_046):
    feature = _clean(ir_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_046'] = {'inputs': ['ir_replacement_046'], 'func': ir_replacement_d2_046}


def ir_replacement_d2_047(ir_replacement_047):
    feature = _clean(ir_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_047'] = {'inputs': ['ir_replacement_047'], 'func': ir_replacement_d2_047}


def ir_replacement_d2_048(ir_replacement_048):
    feature = _clean(ir_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_048'] = {'inputs': ['ir_replacement_048'], 'func': ir_replacement_d2_048}


def ir_replacement_d2_049(ir_replacement_049):
    feature = _clean(ir_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_049'] = {'inputs': ['ir_replacement_049'], 'func': ir_replacement_d2_049}


def ir_replacement_d2_050(ir_replacement_050):
    feature = _clean(ir_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_050'] = {'inputs': ['ir_replacement_050'], 'func': ir_replacement_d2_050}


def ir_replacement_d2_051(ir_replacement_051):
    feature = _clean(ir_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_051'] = {'inputs': ['ir_replacement_051'], 'func': ir_replacement_d2_051}


def ir_replacement_d2_052(ir_replacement_052):
    feature = _clean(ir_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_052'] = {'inputs': ['ir_replacement_052'], 'func': ir_replacement_d2_052}


def ir_replacement_d2_053(ir_replacement_053):
    feature = _clean(ir_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_053'] = {'inputs': ['ir_replacement_053'], 'func': ir_replacement_d2_053}


def ir_replacement_d2_054(ir_replacement_054):
    feature = _clean(ir_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_054'] = {'inputs': ['ir_replacement_054'], 'func': ir_replacement_d2_054}


def ir_replacement_d2_055(ir_replacement_055):
    feature = _clean(ir_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_055'] = {'inputs': ['ir_replacement_055'], 'func': ir_replacement_d2_055}


def ir_replacement_d2_056(ir_replacement_056):
    feature = _clean(ir_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_056'] = {'inputs': ['ir_replacement_056'], 'func': ir_replacement_d2_056}


def ir_replacement_d2_057(ir_replacement_057):
    feature = _clean(ir_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_057'] = {'inputs': ['ir_replacement_057'], 'func': ir_replacement_d2_057}


def ir_replacement_d2_058(ir_replacement_058):
    feature = _clean(ir_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_058'] = {'inputs': ['ir_replacement_058'], 'func': ir_replacement_d2_058}


def ir_replacement_d2_059(ir_replacement_059):
    feature = _clean(ir_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_059'] = {'inputs': ['ir_replacement_059'], 'func': ir_replacement_d2_059}


def ir_replacement_d2_060(ir_replacement_060):
    feature = _clean(ir_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_060'] = {'inputs': ['ir_replacement_060'], 'func': ir_replacement_d2_060}


def ir_replacement_d2_061(ir_replacement_061):
    feature = _clean(ir_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_061'] = {'inputs': ['ir_replacement_061'], 'func': ir_replacement_d2_061}


def ir_replacement_d2_062(ir_replacement_062):
    feature = _clean(ir_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_062'] = {'inputs': ['ir_replacement_062'], 'func': ir_replacement_d2_062}


def ir_replacement_d2_063(ir_replacement_063):
    feature = _clean(ir_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_063'] = {'inputs': ['ir_replacement_063'], 'func': ir_replacement_d2_063}


def ir_replacement_d2_064(ir_replacement_064):
    feature = _clean(ir_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_064'] = {'inputs': ['ir_replacement_064'], 'func': ir_replacement_d2_064}


def ir_replacement_d2_065(ir_replacement_065):
    feature = _clean(ir_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_065'] = {'inputs': ['ir_replacement_065'], 'func': ir_replacement_d2_065}


def ir_replacement_d2_066(ir_replacement_066):
    feature = _clean(ir_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_066'] = {'inputs': ['ir_replacement_066'], 'func': ir_replacement_d2_066}


def ir_replacement_d2_067(ir_replacement_067):
    feature = _clean(ir_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_067'] = {'inputs': ['ir_replacement_067'], 'func': ir_replacement_d2_067}


def ir_replacement_d2_068(ir_replacement_068):
    feature = _clean(ir_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_068'] = {'inputs': ['ir_replacement_068'], 'func': ir_replacement_d2_068}


def ir_replacement_d2_069(ir_replacement_069):
    feature = _clean(ir_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_069'] = {'inputs': ['ir_replacement_069'], 'func': ir_replacement_d2_069}


def ir_replacement_d2_070(ir_replacement_070):
    feature = _clean(ir_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_070'] = {'inputs': ['ir_replacement_070'], 'func': ir_replacement_d2_070}


def ir_replacement_d2_071(ir_replacement_071):
    feature = _clean(ir_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_071'] = {'inputs': ['ir_replacement_071'], 'func': ir_replacement_d2_071}


def ir_replacement_d2_072(ir_replacement_072):
    feature = _clean(ir_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_072'] = {'inputs': ['ir_replacement_072'], 'func': ir_replacement_d2_072}


def ir_replacement_d2_073(ir_replacement_073):
    feature = _clean(ir_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_073'] = {'inputs': ['ir_replacement_073'], 'func': ir_replacement_d2_073}


def ir_replacement_d2_074(ir_replacement_074):
    feature = _clean(ir_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_074'] = {'inputs': ['ir_replacement_074'], 'func': ir_replacement_d2_074}


def ir_replacement_d2_075(ir_replacement_075):
    feature = _clean(ir_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_075'] = {'inputs': ['ir_replacement_075'], 'func': ir_replacement_d2_075}


def ir_replacement_d2_076(ir_replacement_076):
    feature = _clean(ir_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_076'] = {'inputs': ['ir_replacement_076'], 'func': ir_replacement_d2_076}


def ir_replacement_d2_077(ir_replacement_077):
    feature = _clean(ir_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_077'] = {'inputs': ['ir_replacement_077'], 'func': ir_replacement_d2_077}


def ir_replacement_d2_078(ir_replacement_078):
    feature = _clean(ir_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_078'] = {'inputs': ['ir_replacement_078'], 'func': ir_replacement_d2_078}


def ir_replacement_d2_079(ir_replacement_079):
    feature = _clean(ir_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_079'] = {'inputs': ['ir_replacement_079'], 'func': ir_replacement_d2_079}


def ir_replacement_d2_080(ir_replacement_080):
    feature = _clean(ir_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_080'] = {'inputs': ['ir_replacement_080'], 'func': ir_replacement_d2_080}


def ir_replacement_d2_081(ir_replacement_081):
    feature = _clean(ir_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_081'] = {'inputs': ['ir_replacement_081'], 'func': ir_replacement_d2_081}


def ir_replacement_d2_082(ir_replacement_082):
    feature = _clean(ir_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_082'] = {'inputs': ['ir_replacement_082'], 'func': ir_replacement_d2_082}


def ir_replacement_d2_083(ir_replacement_083):
    feature = _clean(ir_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_083'] = {'inputs': ['ir_replacement_083'], 'func': ir_replacement_d2_083}


def ir_replacement_d2_084(ir_replacement_084):
    feature = _clean(ir_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_084'] = {'inputs': ['ir_replacement_084'], 'func': ir_replacement_d2_084}


def ir_replacement_d2_085(ir_replacement_085):
    feature = _clean(ir_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_085'] = {'inputs': ['ir_replacement_085'], 'func': ir_replacement_d2_085}


def ir_replacement_d2_086(ir_replacement_086):
    feature = _clean(ir_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_086'] = {'inputs': ['ir_replacement_086'], 'func': ir_replacement_d2_086}


def ir_replacement_d2_087(ir_replacement_087):
    feature = _clean(ir_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_087'] = {'inputs': ['ir_replacement_087'], 'func': ir_replacement_d2_087}


def ir_replacement_d2_088(ir_replacement_088):
    feature = _clean(ir_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_088'] = {'inputs': ['ir_replacement_088'], 'func': ir_replacement_d2_088}


def ir_replacement_d2_089(ir_replacement_089):
    feature = _clean(ir_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_089'] = {'inputs': ['ir_replacement_089'], 'func': ir_replacement_d2_089}


def ir_replacement_d2_090(ir_replacement_090):
    feature = _clean(ir_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_090'] = {'inputs': ['ir_replacement_090'], 'func': ir_replacement_d2_090}


def ir_replacement_d2_091(ir_replacement_091):
    feature = _clean(ir_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_091'] = {'inputs': ['ir_replacement_091'], 'func': ir_replacement_d2_091}


def ir_replacement_d2_092(ir_replacement_092):
    feature = _clean(ir_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_092'] = {'inputs': ['ir_replacement_092'], 'func': ir_replacement_d2_092}


def ir_replacement_d2_093(ir_replacement_093):
    feature = _clean(ir_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_093'] = {'inputs': ['ir_replacement_093'], 'func': ir_replacement_d2_093}


def ir_replacement_d2_094(ir_replacement_094):
    feature = _clean(ir_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_094'] = {'inputs': ['ir_replacement_094'], 'func': ir_replacement_d2_094}


def ir_replacement_d2_095(ir_replacement_095):
    feature = _clean(ir_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_095'] = {'inputs': ['ir_replacement_095'], 'func': ir_replacement_d2_095}


def ir_replacement_d2_096(ir_replacement_096):
    feature = _clean(ir_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_096'] = {'inputs': ['ir_replacement_096'], 'func': ir_replacement_d2_096}


def ir_replacement_d2_097(ir_replacement_097):
    feature = _clean(ir_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_097'] = {'inputs': ['ir_replacement_097'], 'func': ir_replacement_d2_097}


def ir_replacement_d2_098(ir_replacement_098):
    feature = _clean(ir_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_098'] = {'inputs': ['ir_replacement_098'], 'func': ir_replacement_d2_098}


def ir_replacement_d2_099(ir_replacement_099):
    feature = _clean(ir_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_099'] = {'inputs': ['ir_replacement_099'], 'func': ir_replacement_d2_099}


def ir_replacement_d2_100(ir_replacement_100):
    feature = _clean(ir_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_100'] = {'inputs': ['ir_replacement_100'], 'func': ir_replacement_d2_100}


def ir_replacement_d2_101(ir_replacement_101):
    feature = _clean(ir_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_101'] = {'inputs': ['ir_replacement_101'], 'func': ir_replacement_d2_101}


def ir_replacement_d2_102(ir_replacement_102):
    feature = _clean(ir_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_102'] = {'inputs': ['ir_replacement_102'], 'func': ir_replacement_d2_102}


def ir_replacement_d2_103(ir_replacement_103):
    feature = _clean(ir_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_103'] = {'inputs': ['ir_replacement_103'], 'func': ir_replacement_d2_103}


def ir_replacement_d2_104(ir_replacement_104):
    feature = _clean(ir_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_104'] = {'inputs': ['ir_replacement_104'], 'func': ir_replacement_d2_104}


def ir_replacement_d2_105(ir_replacement_105):
    feature = _clean(ir_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_105'] = {'inputs': ['ir_replacement_105'], 'func': ir_replacement_d2_105}


def ir_replacement_d2_106(ir_replacement_106):
    feature = _clean(ir_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_106'] = {'inputs': ['ir_replacement_106'], 'func': ir_replacement_d2_106}


def ir_replacement_d2_107(ir_replacement_107):
    feature = _clean(ir_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_107'] = {'inputs': ['ir_replacement_107'], 'func': ir_replacement_d2_107}


def ir_replacement_d2_108(ir_replacement_108):
    feature = _clean(ir_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_108'] = {'inputs': ['ir_replacement_108'], 'func': ir_replacement_d2_108}


def ir_replacement_d2_109(ir_replacement_109):
    feature = _clean(ir_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_109'] = {'inputs': ['ir_replacement_109'], 'func': ir_replacement_d2_109}


def ir_replacement_d2_110(ir_replacement_110):
    feature = _clean(ir_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_110'] = {'inputs': ['ir_replacement_110'], 'func': ir_replacement_d2_110}


def ir_replacement_d2_111(ir_replacement_111):
    feature = _clean(ir_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_111'] = {'inputs': ['ir_replacement_111'], 'func': ir_replacement_d2_111}


def ir_replacement_d2_112(ir_replacement_112):
    feature = _clean(ir_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_112'] = {'inputs': ['ir_replacement_112'], 'func': ir_replacement_d2_112}


def ir_replacement_d2_113(ir_replacement_113):
    feature = _clean(ir_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_113'] = {'inputs': ['ir_replacement_113'], 'func': ir_replacement_d2_113}


def ir_replacement_d2_114(ir_replacement_114):
    feature = _clean(ir_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_114'] = {'inputs': ['ir_replacement_114'], 'func': ir_replacement_d2_114}


def ir_replacement_d2_115(ir_replacement_115):
    feature = _clean(ir_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_115'] = {'inputs': ['ir_replacement_115'], 'func': ir_replacement_d2_115}


def ir_replacement_d2_116(ir_replacement_116):
    feature = _clean(ir_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_116'] = {'inputs': ['ir_replacement_116'], 'func': ir_replacement_d2_116}


def ir_replacement_d2_117(ir_replacement_117):
    feature = _clean(ir_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_117'] = {'inputs': ['ir_replacement_117'], 'func': ir_replacement_d2_117}


def ir_replacement_d2_118(ir_replacement_118):
    feature = _clean(ir_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_118'] = {'inputs': ['ir_replacement_118'], 'func': ir_replacement_d2_118}


def ir_replacement_d2_119(ir_replacement_119):
    feature = _clean(ir_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_119'] = {'inputs': ['ir_replacement_119'], 'func': ir_replacement_d2_119}


def ir_replacement_d2_120(ir_replacement_120):
    feature = _clean(ir_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_120'] = {'inputs': ['ir_replacement_120'], 'func': ir_replacement_d2_120}


def ir_replacement_d2_121(ir_replacement_121):
    feature = _clean(ir_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_121'] = {'inputs': ['ir_replacement_121'], 'func': ir_replacement_d2_121}


def ir_replacement_d2_122(ir_replacement_122):
    feature = _clean(ir_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_122'] = {'inputs': ['ir_replacement_122'], 'func': ir_replacement_d2_122}


def ir_replacement_d2_123(ir_replacement_123):
    feature = _clean(ir_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_123'] = {'inputs': ['ir_replacement_123'], 'func': ir_replacement_d2_123}


def ir_replacement_d2_124(ir_replacement_124):
    feature = _clean(ir_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_124'] = {'inputs': ['ir_replacement_124'], 'func': ir_replacement_d2_124}


def ir_replacement_d2_125(ir_replacement_125):
    feature = _clean(ir_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_125'] = {'inputs': ['ir_replacement_125'], 'func': ir_replacement_d2_125}


def ir_replacement_d2_126(ir_replacement_126):
    feature = _clean(ir_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_126'] = {'inputs': ['ir_replacement_126'], 'func': ir_replacement_d2_126}


def ir_replacement_d2_127(ir_replacement_127):
    feature = _clean(ir_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_127'] = {'inputs': ['ir_replacement_127'], 'func': ir_replacement_d2_127}


def ir_replacement_d2_128(ir_replacement_128):
    feature = _clean(ir_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_128'] = {'inputs': ['ir_replacement_128'], 'func': ir_replacement_d2_128}


def ir_replacement_d2_129(ir_replacement_129):
    feature = _clean(ir_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_129'] = {'inputs': ['ir_replacement_129'], 'func': ir_replacement_d2_129}


def ir_replacement_d2_130(ir_replacement_130):
    feature = _clean(ir_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_130'] = {'inputs': ['ir_replacement_130'], 'func': ir_replacement_d2_130}


def ir_replacement_d2_131(ir_replacement_131):
    feature = _clean(ir_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_131'] = {'inputs': ['ir_replacement_131'], 'func': ir_replacement_d2_131}


def ir_replacement_d2_132(ir_replacement_132):
    feature = _clean(ir_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_132'] = {'inputs': ['ir_replacement_132'], 'func': ir_replacement_d2_132}


def ir_replacement_d2_133(ir_replacement_133):
    feature = _clean(ir_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_133'] = {'inputs': ['ir_replacement_133'], 'func': ir_replacement_d2_133}


def ir_replacement_d2_134(ir_replacement_134):
    feature = _clean(ir_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_134'] = {'inputs': ['ir_replacement_134'], 'func': ir_replacement_d2_134}


def ir_replacement_d2_135(ir_replacement_135):
    feature = _clean(ir_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_135'] = {'inputs': ['ir_replacement_135'], 'func': ir_replacement_d2_135}


def ir_replacement_d2_136(ir_replacement_136):
    feature = _clean(ir_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_136'] = {'inputs': ['ir_replacement_136'], 'func': ir_replacement_d2_136}


def ir_replacement_d2_137(ir_replacement_137):
    feature = _clean(ir_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_137'] = {'inputs': ['ir_replacement_137'], 'func': ir_replacement_d2_137}


def ir_replacement_d2_138(ir_replacement_138):
    feature = _clean(ir_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_138'] = {'inputs': ['ir_replacement_138'], 'func': ir_replacement_d2_138}


def ir_replacement_d2_139(ir_replacement_139):
    feature = _clean(ir_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_139'] = {'inputs': ['ir_replacement_139'], 'func': ir_replacement_d2_139}


def ir_replacement_d2_140(ir_replacement_140):
    feature = _clean(ir_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_140'] = {'inputs': ['ir_replacement_140'], 'func': ir_replacement_d2_140}


def ir_replacement_d2_141(ir_replacement_141):
    feature = _clean(ir_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_141'] = {'inputs': ['ir_replacement_141'], 'func': ir_replacement_d2_141}


def ir_replacement_d2_142(ir_replacement_142):
    feature = _clean(ir_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_142'] = {'inputs': ['ir_replacement_142'], 'func': ir_replacement_d2_142}


def ir_replacement_d2_143(ir_replacement_143):
    feature = _clean(ir_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_143'] = {'inputs': ['ir_replacement_143'], 'func': ir_replacement_d2_143}


def ir_replacement_d2_144(ir_replacement_144):
    feature = _clean(ir_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_144'] = {'inputs': ['ir_replacement_144'], 'func': ir_replacement_d2_144}


def ir_replacement_d2_145(ir_replacement_145):
    feature = _clean(ir_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_145'] = {'inputs': ['ir_replacement_145'], 'func': ir_replacement_d2_145}


def ir_replacement_d2_146(ir_replacement_146):
    feature = _clean(ir_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_146'] = {'inputs': ['ir_replacement_146'], 'func': ir_replacement_d2_146}


def ir_replacement_d2_147(ir_replacement_147):
    feature = _clean(ir_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_147'] = {'inputs': ['ir_replacement_147'], 'func': ir_replacement_d2_147}


def ir_replacement_d2_148(ir_replacement_148):
    feature = _clean(ir_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_148'] = {'inputs': ['ir_replacement_148'], 'func': ir_replacement_d2_148}


def ir_replacement_d2_149(ir_replacement_149):
    feature = _clean(ir_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_149'] = {'inputs': ['ir_replacement_149'], 'func': ir_replacement_d2_149}


def ir_replacement_d2_150(ir_replacement_150):
    feature = _clean(ir_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_150'] = {'inputs': ['ir_replacement_150'], 'func': ir_replacement_d2_150}


def ir_replacement_d2_151(ir_replacement_151):
    feature = _clean(ir_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_151'] = {'inputs': ['ir_replacement_151'], 'func': ir_replacement_d2_151}


def ir_replacement_d2_152(ir_replacement_152):
    feature = _clean(ir_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_152'] = {'inputs': ['ir_replacement_152'], 'func': ir_replacement_d2_152}


def ir_replacement_d2_153(ir_replacement_153):
    feature = _clean(ir_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_153'] = {'inputs': ['ir_replacement_153'], 'func': ir_replacement_d2_153}


def ir_replacement_d2_154(ir_replacement_154):
    feature = _clean(ir_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_154'] = {'inputs': ['ir_replacement_154'], 'func': ir_replacement_d2_154}


def ir_replacement_d2_155(ir_replacement_155):
    feature = _clean(ir_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_155'] = {'inputs': ['ir_replacement_155'], 'func': ir_replacement_d2_155}


def ir_replacement_d2_156(ir_replacement_156):
    feature = _clean(ir_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_156'] = {'inputs': ['ir_replacement_156'], 'func': ir_replacement_d2_156}


def ir_replacement_d2_157(ir_replacement_157):
    feature = _clean(ir_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_157'] = {'inputs': ['ir_replacement_157'], 'func': ir_replacement_d2_157}


def ir_replacement_d2_158(ir_replacement_158):
    feature = _clean(ir_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_158'] = {'inputs': ['ir_replacement_158'], 'func': ir_replacement_d2_158}


def ir_replacement_d2_159(ir_replacement_159):
    feature = _clean(ir_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_159'] = {'inputs': ['ir_replacement_159'], 'func': ir_replacement_d2_159}


def ir_replacement_d2_160(ir_replacement_160):
    feature = _clean(ir_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_160'] = {'inputs': ['ir_replacement_160'], 'func': ir_replacement_d2_160}


def ir_replacement_d2_161(ir_replacement_161):
    feature = _clean(ir_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_161'] = {'inputs': ['ir_replacement_161'], 'func': ir_replacement_d2_161}


def ir_replacement_d2_162(ir_replacement_162):
    feature = _clean(ir_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_162'] = {'inputs': ['ir_replacement_162'], 'func': ir_replacement_d2_162}


def ir_replacement_d2_163(ir_replacement_163):
    feature = _clean(ir_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_163'] = {'inputs': ['ir_replacement_163'], 'func': ir_replacement_d2_163}


def ir_replacement_d2_164(ir_replacement_164):
    feature = _clean(ir_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_164'] = {'inputs': ['ir_replacement_164'], 'func': ir_replacement_d2_164}


def ir_replacement_d2_165(ir_replacement_165):
    feature = _clean(ir_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_165'] = {'inputs': ['ir_replacement_165'], 'func': ir_replacement_d2_165}


def ir_replacement_d2_166(ir_replacement_166):
    feature = _clean(ir_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_166'] = {'inputs': ['ir_replacement_166'], 'func': ir_replacement_d2_166}


def ir_replacement_d2_167(ir_replacement_167):
    feature = _clean(ir_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_167'] = {'inputs': ['ir_replacement_167'], 'func': ir_replacement_d2_167}


def ir_replacement_d2_168(ir_replacement_168):
    feature = _clean(ir_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_168'] = {'inputs': ['ir_replacement_168'], 'func': ir_replacement_d2_168}


def ir_replacement_d2_169(ir_replacement_169):
    feature = _clean(ir_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_169'] = {'inputs': ['ir_replacement_169'], 'func': ir_replacement_d2_169}


def ir_replacement_d2_170(ir_replacement_170):
    feature = _clean(ir_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_170'] = {'inputs': ['ir_replacement_170'], 'func': ir_replacement_d2_170}


def ir_replacement_d2_171(ir_replacement_171):
    feature = _clean(ir_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_171'] = {'inputs': ['ir_replacement_171'], 'func': ir_replacement_d2_171}


def ir_replacement_d2_172(ir_replacement_172):
    feature = _clean(ir_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_172'] = {'inputs': ['ir_replacement_172'], 'func': ir_replacement_d2_172}


def ir_replacement_d2_173(ir_replacement_173):
    feature = _clean(ir_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_173'] = {'inputs': ['ir_replacement_173'], 'func': ir_replacement_d2_173}


def ir_replacement_d2_174(ir_replacement_174):
    feature = _clean(ir_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_174'] = {'inputs': ['ir_replacement_174'], 'func': ir_replacement_d2_174}


def ir_replacement_d2_175(ir_replacement_175):
    feature = _clean(ir_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
IR_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ir_replacement_d2_175'] = {'inputs': ['ir_replacement_175'], 'func': ir_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def idr_base_universe_d2_001_idr_002_range_expansion_10_002(idr_002_range_expansion_10_002):
    return _base_universe_d2(idr_002_range_expansion_10_002, 1)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_001_idr_002_range_expansion_10_002'] = {'inputs': ['idr_002_range_expansion_10_002'], 'func': idr_base_universe_d2_001_idr_002_range_expansion_10_002}


def idr_base_universe_d2_002_idr_004_close_location_42_004(idr_004_close_location_42_004):
    return _base_universe_d2(idr_004_close_location_42_004, 2)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_002_idr_004_close_location_42_004'] = {'inputs': ['idr_004_close_location_42_004'], 'func': idr_base_universe_d2_002_idr_004_close_location_42_004}


def idr_base_universe_d2_003_idr_005_atr_move_63_005(idr_005_atr_move_63_005):
    return _base_universe_d2(idr_005_atr_move_63_005, 3)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_003_idr_005_atr_move_63_005'] = {'inputs': ['idr_005_atr_move_63_005'], 'func': idr_base_universe_d2_003_idr_005_atr_move_63_005}


def idr_base_universe_d2_004_idr_008_range_expansion_189_008(idr_008_range_expansion_189_008):
    return _base_universe_d2(idr_008_range_expansion_189_008, 4)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_004_idr_008_range_expansion_189_008'] = {'inputs': ['idr_008_range_expansion_189_008'], 'func': idr_base_universe_d2_004_idr_008_range_expansion_189_008}


def idr_base_universe_d2_005_idr_010_close_location_378_010(idr_010_close_location_378_010):
    return _base_universe_d2(idr_010_close_location_378_010, 5)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_005_idr_010_close_location_378_010'] = {'inputs': ['idr_010_close_location_378_010'], 'func': idr_base_universe_d2_005_idr_010_close_location_378_010}


def idr_base_universe_d2_006_idr_011_atr_move_504_011(idr_011_atr_move_504_011):
    return _base_universe_d2(idr_011_atr_move_504_011, 6)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_006_idr_011_atr_move_504_011'] = {'inputs': ['idr_011_atr_move_504_011'], 'func': idr_base_universe_d2_006_idr_011_atr_move_504_011}


def idr_base_universe_d2_007_idr_014_range_expansion_1260_014(idr_014_range_expansion_1260_014):
    return _base_universe_d2(idr_014_range_expansion_1260_014, 7)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_007_idr_014_range_expansion_1260_014'] = {'inputs': ['idr_014_range_expansion_1260_014'], 'func': idr_base_universe_d2_007_idr_014_range_expansion_1260_014}


def idr_base_universe_d2_008_idr_016_close_location_5_016(idr_016_close_location_5_016):
    return _base_universe_d2(idr_016_close_location_5_016, 8)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_008_idr_016_close_location_5_016'] = {'inputs': ['idr_016_close_location_5_016'], 'func': idr_base_universe_d2_008_idr_016_close_location_5_016}


def idr_base_universe_d2_009_idr_017_atr_move_10_017(idr_017_atr_move_10_017):
    return _base_universe_d2(idr_017_atr_move_10_017, 9)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_009_idr_017_atr_move_10_017'] = {'inputs': ['idr_017_atr_move_10_017'], 'func': idr_base_universe_d2_009_idr_017_atr_move_10_017}


def idr_base_universe_d2_010_idr_020_range_expansion_63_020(idr_020_range_expansion_63_020):
    return _base_universe_d2(idr_020_range_expansion_63_020, 10)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_010_idr_020_range_expansion_63_020'] = {'inputs': ['idr_020_range_expansion_63_020'], 'func': idr_base_universe_d2_010_idr_020_range_expansion_63_020}


def idr_base_universe_d2_011_idr_022_close_location_126_022(idr_022_close_location_126_022):
    return _base_universe_d2(idr_022_close_location_126_022, 11)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_011_idr_022_close_location_126_022'] = {'inputs': ['idr_022_close_location_126_022'], 'func': idr_base_universe_d2_011_idr_022_close_location_126_022}


def idr_base_universe_d2_012_idr_023_atr_move_189_023(idr_023_atr_move_189_023):
    return _base_universe_d2(idr_023_atr_move_189_023, 12)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_012_idr_023_atr_move_189_023'] = {'inputs': ['idr_023_atr_move_189_023'], 'func': idr_base_universe_d2_012_idr_023_atr_move_189_023}


def idr_base_universe_d2_013_idr_026_range_expansion_504_026(idr_026_range_expansion_504_026):
    return _base_universe_d2(idr_026_range_expansion_504_026, 13)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_013_idr_026_range_expansion_504_026'] = {'inputs': ['idr_026_range_expansion_504_026'], 'func': idr_base_universe_d2_013_idr_026_range_expansion_504_026}


def idr_base_universe_d2_014_idr_028_close_location_1008_028(idr_028_close_location_1008_028):
    return _base_universe_d2(idr_028_close_location_1008_028, 14)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_014_idr_028_close_location_1008_028'] = {'inputs': ['idr_028_close_location_1008_028'], 'func': idr_base_universe_d2_014_idr_028_close_location_1008_028}


def idr_base_universe_d2_015_idr_029_atr_move_1260_029(idr_029_atr_move_1260_029):
    return _base_universe_d2(idr_029_atr_move_1260_029, 15)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_015_idr_029_atr_move_1260_029'] = {'inputs': ['idr_029_atr_move_1260_029'], 'func': idr_base_universe_d2_015_idr_029_atr_move_1260_029}


def idr_base_universe_d2_016_idr_basefill_001(idr_basefill_001):
    return _base_universe_d2(idr_basefill_001, 16)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_016_idr_basefill_001'] = {'inputs': ['idr_basefill_001'], 'func': idr_base_universe_d2_016_idr_basefill_001}


def idr_base_universe_d2_017_idr_basefill_003(idr_basefill_003):
    return _base_universe_d2(idr_basefill_003, 17)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_017_idr_basefill_003'] = {'inputs': ['idr_basefill_003'], 'func': idr_base_universe_d2_017_idr_basefill_003}


def idr_base_universe_d2_018_idr_basefill_006(idr_basefill_006):
    return _base_universe_d2(idr_basefill_006, 18)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_018_idr_basefill_006'] = {'inputs': ['idr_basefill_006'], 'func': idr_base_universe_d2_018_idr_basefill_006}


def idr_base_universe_d2_019_idr_basefill_007(idr_basefill_007):
    return _base_universe_d2(idr_basefill_007, 19)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_019_idr_basefill_007'] = {'inputs': ['idr_basefill_007'], 'func': idr_base_universe_d2_019_idr_basefill_007}


def idr_base_universe_d2_020_idr_basefill_009(idr_basefill_009):
    return _base_universe_d2(idr_basefill_009, 20)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_020_idr_basefill_009'] = {'inputs': ['idr_basefill_009'], 'func': idr_base_universe_d2_020_idr_basefill_009}


def idr_base_universe_d2_021_idr_basefill_012(idr_basefill_012):
    return _base_universe_d2(idr_basefill_012, 21)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_021_idr_basefill_012'] = {'inputs': ['idr_basefill_012'], 'func': idr_base_universe_d2_021_idr_basefill_012}


def idr_base_universe_d2_022_idr_basefill_013(idr_basefill_013):
    return _base_universe_d2(idr_basefill_013, 22)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_022_idr_basefill_013'] = {'inputs': ['idr_basefill_013'], 'func': idr_base_universe_d2_022_idr_basefill_013}


def idr_base_universe_d2_023_idr_basefill_015(idr_basefill_015):
    return _base_universe_d2(idr_basefill_015, 23)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_023_idr_basefill_015'] = {'inputs': ['idr_basefill_015'], 'func': idr_base_universe_d2_023_idr_basefill_015}


def idr_base_universe_d2_024_idr_basefill_018(idr_basefill_018):
    return _base_universe_d2(idr_basefill_018, 24)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_024_idr_basefill_018'] = {'inputs': ['idr_basefill_018'], 'func': idr_base_universe_d2_024_idr_basefill_018}


def idr_base_universe_d2_025_idr_basefill_019(idr_basefill_019):
    return _base_universe_d2(idr_basefill_019, 25)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_025_idr_basefill_019'] = {'inputs': ['idr_basefill_019'], 'func': idr_base_universe_d2_025_idr_basefill_019}


def idr_base_universe_d2_026_idr_basefill_021(idr_basefill_021):
    return _base_universe_d2(idr_basefill_021, 26)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_026_idr_basefill_021'] = {'inputs': ['idr_basefill_021'], 'func': idr_base_universe_d2_026_idr_basefill_021}


def idr_base_universe_d2_027_idr_basefill_024(idr_basefill_024):
    return _base_universe_d2(idr_basefill_024, 27)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_027_idr_basefill_024'] = {'inputs': ['idr_basefill_024'], 'func': idr_base_universe_d2_027_idr_basefill_024}


def idr_base_universe_d2_028_idr_basefill_025(idr_basefill_025):
    return _base_universe_d2(idr_basefill_025, 28)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_028_idr_basefill_025'] = {'inputs': ['idr_basefill_025'], 'func': idr_base_universe_d2_028_idr_basefill_025}


def idr_base_universe_d2_029_idr_basefill_027(idr_basefill_027):
    return _base_universe_d2(idr_basefill_027, 29)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_029_idr_basefill_027'] = {'inputs': ['idr_basefill_027'], 'func': idr_base_universe_d2_029_idr_basefill_027}


def idr_base_universe_d2_030_idr_basefill_030(idr_basefill_030):
    return _base_universe_d2(idr_basefill_030, 30)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_030_idr_basefill_030'] = {'inputs': ['idr_basefill_030'], 'func': idr_base_universe_d2_030_idr_basefill_030}


def idr_base_universe_d2_031_idr_basefill_031(idr_basefill_031):
    return _base_universe_d2(idr_basefill_031, 31)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_031_idr_basefill_031'] = {'inputs': ['idr_basefill_031'], 'func': idr_base_universe_d2_031_idr_basefill_031}


def idr_base_universe_d2_032_idr_basefill_032(idr_basefill_032):
    return _base_universe_d2(idr_basefill_032, 32)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_032_idr_basefill_032'] = {'inputs': ['idr_basefill_032'], 'func': idr_base_universe_d2_032_idr_basefill_032}


def idr_base_universe_d2_033_idr_basefill_033(idr_basefill_033):
    return _base_universe_d2(idr_basefill_033, 33)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_033_idr_basefill_033'] = {'inputs': ['idr_basefill_033'], 'func': idr_base_universe_d2_033_idr_basefill_033}


def idr_base_universe_d2_034_idr_basefill_034(idr_basefill_034):
    return _base_universe_d2(idr_basefill_034, 34)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_034_idr_basefill_034'] = {'inputs': ['idr_basefill_034'], 'func': idr_base_universe_d2_034_idr_basefill_034}


def idr_base_universe_d2_035_idr_basefill_035(idr_basefill_035):
    return _base_universe_d2(idr_basefill_035, 35)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_035_idr_basefill_035'] = {'inputs': ['idr_basefill_035'], 'func': idr_base_universe_d2_035_idr_basefill_035}


def idr_base_universe_d2_036_idr_basefill_036(idr_basefill_036):
    return _base_universe_d2(idr_basefill_036, 36)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_036_idr_basefill_036'] = {'inputs': ['idr_basefill_036'], 'func': idr_base_universe_d2_036_idr_basefill_036}


def idr_base_universe_d2_037_idr_basefill_037(idr_basefill_037):
    return _base_universe_d2(idr_basefill_037, 37)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_037_idr_basefill_037'] = {'inputs': ['idr_basefill_037'], 'func': idr_base_universe_d2_037_idr_basefill_037}


def idr_base_universe_d2_038_idr_basefill_038(idr_basefill_038):
    return _base_universe_d2(idr_basefill_038, 38)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_038_idr_basefill_038'] = {'inputs': ['idr_basefill_038'], 'func': idr_base_universe_d2_038_idr_basefill_038}


def idr_base_universe_d2_039_idr_basefill_039(idr_basefill_039):
    return _base_universe_d2(idr_basefill_039, 39)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_039_idr_basefill_039'] = {'inputs': ['idr_basefill_039'], 'func': idr_base_universe_d2_039_idr_basefill_039}


def idr_base_universe_d2_040_idr_basefill_040(idr_basefill_040):
    return _base_universe_d2(idr_basefill_040, 40)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_040_idr_basefill_040'] = {'inputs': ['idr_basefill_040'], 'func': idr_base_universe_d2_040_idr_basefill_040}


def idr_base_universe_d2_041_idr_basefill_041(idr_basefill_041):
    return _base_universe_d2(idr_basefill_041, 41)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_041_idr_basefill_041'] = {'inputs': ['idr_basefill_041'], 'func': idr_base_universe_d2_041_idr_basefill_041}


def idr_base_universe_d2_042_idr_basefill_042(idr_basefill_042):
    return _base_universe_d2(idr_basefill_042, 42)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_042_idr_basefill_042'] = {'inputs': ['idr_basefill_042'], 'func': idr_base_universe_d2_042_idr_basefill_042}


def idr_base_universe_d2_043_idr_basefill_043(idr_basefill_043):
    return _base_universe_d2(idr_basefill_043, 43)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_043_idr_basefill_043'] = {'inputs': ['idr_basefill_043'], 'func': idr_base_universe_d2_043_idr_basefill_043}


def idr_base_universe_d2_044_idr_basefill_044(idr_basefill_044):
    return _base_universe_d2(idr_basefill_044, 44)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_044_idr_basefill_044'] = {'inputs': ['idr_basefill_044'], 'func': idr_base_universe_d2_044_idr_basefill_044}


def idr_base_universe_d2_045_idr_basefill_045(idr_basefill_045):
    return _base_universe_d2(idr_basefill_045, 45)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_045_idr_basefill_045'] = {'inputs': ['idr_basefill_045'], 'func': idr_base_universe_d2_045_idr_basefill_045}


def idr_base_universe_d2_046_idr_basefill_046(idr_basefill_046):
    return _base_universe_d2(idr_basefill_046, 46)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_046_idr_basefill_046'] = {'inputs': ['idr_basefill_046'], 'func': idr_base_universe_d2_046_idr_basefill_046}


def idr_base_universe_d2_047_idr_basefill_047(idr_basefill_047):
    return _base_universe_d2(idr_basefill_047, 47)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_047_idr_basefill_047'] = {'inputs': ['idr_basefill_047'], 'func': idr_base_universe_d2_047_idr_basefill_047}


def idr_base_universe_d2_048_idr_basefill_048(idr_basefill_048):
    return _base_universe_d2(idr_basefill_048, 48)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_048_idr_basefill_048'] = {'inputs': ['idr_basefill_048'], 'func': idr_base_universe_d2_048_idr_basefill_048}


def idr_base_universe_d2_049_idr_basefill_049(idr_basefill_049):
    return _base_universe_d2(idr_basefill_049, 49)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_049_idr_basefill_049'] = {'inputs': ['idr_basefill_049'], 'func': idr_base_universe_d2_049_idr_basefill_049}


def idr_base_universe_d2_050_idr_basefill_050(idr_basefill_050):
    return _base_universe_d2(idr_basefill_050, 50)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_050_idr_basefill_050'] = {'inputs': ['idr_basefill_050'], 'func': idr_base_universe_d2_050_idr_basefill_050}


def idr_base_universe_d2_051_idr_basefill_051(idr_basefill_051):
    return _base_universe_d2(idr_basefill_051, 51)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_051_idr_basefill_051'] = {'inputs': ['idr_basefill_051'], 'func': idr_base_universe_d2_051_idr_basefill_051}


def idr_base_universe_d2_052_idr_basefill_052(idr_basefill_052):
    return _base_universe_d2(idr_basefill_052, 52)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_052_idr_basefill_052'] = {'inputs': ['idr_basefill_052'], 'func': idr_base_universe_d2_052_idr_basefill_052}


def idr_base_universe_d2_053_idr_basefill_053(idr_basefill_053):
    return _base_universe_d2(idr_basefill_053, 53)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_053_idr_basefill_053'] = {'inputs': ['idr_basefill_053'], 'func': idr_base_universe_d2_053_idr_basefill_053}


def idr_base_universe_d2_054_idr_basefill_054(idr_basefill_054):
    return _base_universe_d2(idr_basefill_054, 54)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_054_idr_basefill_054'] = {'inputs': ['idr_basefill_054'], 'func': idr_base_universe_d2_054_idr_basefill_054}


def idr_base_universe_d2_055_idr_basefill_055(idr_basefill_055):
    return _base_universe_d2(idr_basefill_055, 55)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_055_idr_basefill_055'] = {'inputs': ['idr_basefill_055'], 'func': idr_base_universe_d2_055_idr_basefill_055}


def idr_base_universe_d2_056_idr_basefill_056(idr_basefill_056):
    return _base_universe_d2(idr_basefill_056, 56)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_056_idr_basefill_056'] = {'inputs': ['idr_basefill_056'], 'func': idr_base_universe_d2_056_idr_basefill_056}


def idr_base_universe_d2_057_idr_basefill_057(idr_basefill_057):
    return _base_universe_d2(idr_basefill_057, 57)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_057_idr_basefill_057'] = {'inputs': ['idr_basefill_057'], 'func': idr_base_universe_d2_057_idr_basefill_057}


def idr_base_universe_d2_058_idr_basefill_058(idr_basefill_058):
    return _base_universe_d2(idr_basefill_058, 58)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_058_idr_basefill_058'] = {'inputs': ['idr_basefill_058'], 'func': idr_base_universe_d2_058_idr_basefill_058}


def idr_base_universe_d2_059_idr_basefill_059(idr_basefill_059):
    return _base_universe_d2(idr_basefill_059, 59)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_059_idr_basefill_059'] = {'inputs': ['idr_basefill_059'], 'func': idr_base_universe_d2_059_idr_basefill_059}


def idr_base_universe_d2_060_idr_basefill_060(idr_basefill_060):
    return _base_universe_d2(idr_basefill_060, 60)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_060_idr_basefill_060'] = {'inputs': ['idr_basefill_060'], 'func': idr_base_universe_d2_060_idr_basefill_060}


def idr_base_universe_d2_061_idr_basefill_061(idr_basefill_061):
    return _base_universe_d2(idr_basefill_061, 61)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_061_idr_basefill_061'] = {'inputs': ['idr_basefill_061'], 'func': idr_base_universe_d2_061_idr_basefill_061}


def idr_base_universe_d2_062_idr_basefill_062(idr_basefill_062):
    return _base_universe_d2(idr_basefill_062, 62)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_062_idr_basefill_062'] = {'inputs': ['idr_basefill_062'], 'func': idr_base_universe_d2_062_idr_basefill_062}


def idr_base_universe_d2_063_idr_basefill_063(idr_basefill_063):
    return _base_universe_d2(idr_basefill_063, 63)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_063_idr_basefill_063'] = {'inputs': ['idr_basefill_063'], 'func': idr_base_universe_d2_063_idr_basefill_063}


def idr_base_universe_d2_064_idr_basefill_064(idr_basefill_064):
    return _base_universe_d2(idr_basefill_064, 64)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_064_idr_basefill_064'] = {'inputs': ['idr_basefill_064'], 'func': idr_base_universe_d2_064_idr_basefill_064}


def idr_base_universe_d2_065_idr_basefill_065(idr_basefill_065):
    return _base_universe_d2(idr_basefill_065, 65)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_065_idr_basefill_065'] = {'inputs': ['idr_basefill_065'], 'func': idr_base_universe_d2_065_idr_basefill_065}


def idr_base_universe_d2_066_idr_basefill_066(idr_basefill_066):
    return _base_universe_d2(idr_basefill_066, 66)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_066_idr_basefill_066'] = {'inputs': ['idr_basefill_066'], 'func': idr_base_universe_d2_066_idr_basefill_066}


def idr_base_universe_d2_067_idr_basefill_067(idr_basefill_067):
    return _base_universe_d2(idr_basefill_067, 67)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_067_idr_basefill_067'] = {'inputs': ['idr_basefill_067'], 'func': idr_base_universe_d2_067_idr_basefill_067}


def idr_base_universe_d2_068_idr_basefill_068(idr_basefill_068):
    return _base_universe_d2(idr_basefill_068, 68)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_068_idr_basefill_068'] = {'inputs': ['idr_basefill_068'], 'func': idr_base_universe_d2_068_idr_basefill_068}


def idr_base_universe_d2_069_idr_basefill_069(idr_basefill_069):
    return _base_universe_d2(idr_basefill_069, 69)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_069_idr_basefill_069'] = {'inputs': ['idr_basefill_069'], 'func': idr_base_universe_d2_069_idr_basefill_069}


def idr_base_universe_d2_070_idr_basefill_070(idr_basefill_070):
    return _base_universe_d2(idr_basefill_070, 70)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_070_idr_basefill_070'] = {'inputs': ['idr_basefill_070'], 'func': idr_base_universe_d2_070_idr_basefill_070}


def idr_base_universe_d2_071_idr_basefill_071(idr_basefill_071):
    return _base_universe_d2(idr_basefill_071, 71)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_071_idr_basefill_071'] = {'inputs': ['idr_basefill_071'], 'func': idr_base_universe_d2_071_idr_basefill_071}


def idr_base_universe_d2_072_idr_basefill_072(idr_basefill_072):
    return _base_universe_d2(idr_basefill_072, 72)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_072_idr_basefill_072'] = {'inputs': ['idr_basefill_072'], 'func': idr_base_universe_d2_072_idr_basefill_072}


def idr_base_universe_d2_073_idr_basefill_073(idr_basefill_073):
    return _base_universe_d2(idr_basefill_073, 73)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_073_idr_basefill_073'] = {'inputs': ['idr_basefill_073'], 'func': idr_base_universe_d2_073_idr_basefill_073}


def idr_base_universe_d2_074_idr_basefill_074(idr_basefill_074):
    return _base_universe_d2(idr_basefill_074, 74)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_074_idr_basefill_074'] = {'inputs': ['idr_basefill_074'], 'func': idr_base_universe_d2_074_idr_basefill_074}


def idr_base_universe_d2_075_idr_basefill_075(idr_basefill_075):
    return _base_universe_d2(idr_basefill_075, 75)
IDR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['idr_base_universe_d2_075_idr_basefill_075'] = {'inputs': ['idr_basefill_075'], 'func': idr_base_universe_d2_075_idr_basefill_075}
