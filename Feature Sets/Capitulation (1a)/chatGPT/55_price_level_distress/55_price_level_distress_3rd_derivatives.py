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



def pld_001_amihud_illiquidity_accel_1(pld_001_amihud_illiquidity_roc_1):
    feature = _s(pld_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def pld_007_amihud_illiquidity_accel_5(pld_007_amihud_illiquidity_roc_5):
    feature = _s(pld_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def pld_013_amihud_illiquidity_accel_42(pld_013_amihud_illiquidity_roc_42):
    feature = _s(pld_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def pld_179_pld_019_amihud_illiquidity_42_019_accel_126(pld_154_pld_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(pld_154_pld_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def pld_180_pld_025_amihud_illiquidity_378_025_accel_378(pld_155_pld_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(pld_155_pld_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















PRICE_LEVEL_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    'pld_001_amihud_illiquidity_accel_1': {'inputs': ['pld_001_amihud_illiquidity_roc_1'], 'func': pld_001_amihud_illiquidity_accel_1},
    'pld_007_amihud_illiquidity_accel_5': {'inputs': ['pld_007_amihud_illiquidity_roc_5'], 'func': pld_007_amihud_illiquidity_accel_5},
    'pld_013_amihud_illiquidity_accel_42': {'inputs': ['pld_013_amihud_illiquidity_roc_42'], 'func': pld_013_amihud_illiquidity_accel_42},
    'pld_179_pld_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['pld_154_pld_019_amihud_illiquidity_42_019_roc_126'], 'func': pld_179_pld_019_amihud_illiquidity_42_019_accel_126},
    'pld_180_pld_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['pld_155_pld_025_amihud_illiquidity_378_025_roc_378'], 'func': pld_180_pld_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def pld_replacement_d3_001(pld_replacement_d2_001):
    feature = _clean(pld_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_001'] = {'inputs': ['pld_replacement_d2_001'], 'func': pld_replacement_d3_001}


def pld_replacement_d3_002(pld_replacement_d2_002):
    feature = _clean(pld_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_002'] = {'inputs': ['pld_replacement_d2_002'], 'func': pld_replacement_d3_002}


def pld_replacement_d3_003(pld_replacement_d2_003):
    feature = _clean(pld_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_003'] = {'inputs': ['pld_replacement_d2_003'], 'func': pld_replacement_d3_003}


def pld_replacement_d3_004(pld_replacement_d2_004):
    feature = _clean(pld_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_004'] = {'inputs': ['pld_replacement_d2_004'], 'func': pld_replacement_d3_004}


def pld_replacement_d3_005(pld_replacement_d2_005):
    feature = _clean(pld_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_005'] = {'inputs': ['pld_replacement_d2_005'], 'func': pld_replacement_d3_005}


def pld_replacement_d3_006(pld_replacement_d2_006):
    feature = _clean(pld_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_006'] = {'inputs': ['pld_replacement_d2_006'], 'func': pld_replacement_d3_006}


def pld_replacement_d3_007(pld_replacement_d2_007):
    feature = _clean(pld_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_007'] = {'inputs': ['pld_replacement_d2_007'], 'func': pld_replacement_d3_007}


def pld_replacement_d3_008(pld_replacement_d2_008):
    feature = _clean(pld_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_008'] = {'inputs': ['pld_replacement_d2_008'], 'func': pld_replacement_d3_008}


def pld_replacement_d3_009(pld_replacement_d2_009):
    feature = _clean(pld_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_009'] = {'inputs': ['pld_replacement_d2_009'], 'func': pld_replacement_d3_009}


def pld_replacement_d3_010(pld_replacement_d2_010):
    feature = _clean(pld_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_010'] = {'inputs': ['pld_replacement_d2_010'], 'func': pld_replacement_d3_010}


def pld_replacement_d3_011(pld_replacement_d2_011):
    feature = _clean(pld_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_011'] = {'inputs': ['pld_replacement_d2_011'], 'func': pld_replacement_d3_011}


def pld_replacement_d3_012(pld_replacement_d2_012):
    feature = _clean(pld_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_012'] = {'inputs': ['pld_replacement_d2_012'], 'func': pld_replacement_d3_012}


def pld_replacement_d3_013(pld_replacement_d2_013):
    feature = _clean(pld_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_013'] = {'inputs': ['pld_replacement_d2_013'], 'func': pld_replacement_d3_013}


def pld_replacement_d3_014(pld_replacement_d2_014):
    feature = _clean(pld_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_014'] = {'inputs': ['pld_replacement_d2_014'], 'func': pld_replacement_d3_014}


def pld_replacement_d3_015(pld_replacement_d2_015):
    feature = _clean(pld_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_015'] = {'inputs': ['pld_replacement_d2_015'], 'func': pld_replacement_d3_015}


def pld_replacement_d3_016(pld_replacement_d2_016):
    feature = _clean(pld_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_016'] = {'inputs': ['pld_replacement_d2_016'], 'func': pld_replacement_d3_016}


def pld_replacement_d3_017(pld_replacement_d2_017):
    feature = _clean(pld_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_017'] = {'inputs': ['pld_replacement_d2_017'], 'func': pld_replacement_d3_017}


def pld_replacement_d3_018(pld_replacement_d2_018):
    feature = _clean(pld_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_018'] = {'inputs': ['pld_replacement_d2_018'], 'func': pld_replacement_d3_018}


def pld_replacement_d3_019(pld_replacement_d2_019):
    feature = _clean(pld_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_019'] = {'inputs': ['pld_replacement_d2_019'], 'func': pld_replacement_d3_019}


def pld_replacement_d3_020(pld_replacement_d2_020):
    feature = _clean(pld_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_020'] = {'inputs': ['pld_replacement_d2_020'], 'func': pld_replacement_d3_020}


def pld_replacement_d3_021(pld_replacement_d2_021):
    feature = _clean(pld_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_021'] = {'inputs': ['pld_replacement_d2_021'], 'func': pld_replacement_d3_021}


def pld_replacement_d3_022(pld_replacement_d2_022):
    feature = _clean(pld_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_022'] = {'inputs': ['pld_replacement_d2_022'], 'func': pld_replacement_d3_022}


def pld_replacement_d3_023(pld_replacement_d2_023):
    feature = _clean(pld_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_023'] = {'inputs': ['pld_replacement_d2_023'], 'func': pld_replacement_d3_023}


def pld_replacement_d3_024(pld_replacement_d2_024):
    feature = _clean(pld_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_024'] = {'inputs': ['pld_replacement_d2_024'], 'func': pld_replacement_d3_024}


def pld_replacement_d3_025(pld_replacement_d2_025):
    feature = _clean(pld_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_025'] = {'inputs': ['pld_replacement_d2_025'], 'func': pld_replacement_d3_025}


def pld_replacement_d3_026(pld_replacement_d2_026):
    feature = _clean(pld_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_026'] = {'inputs': ['pld_replacement_d2_026'], 'func': pld_replacement_d3_026}


def pld_replacement_d3_027(pld_replacement_d2_027):
    feature = _clean(pld_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_027'] = {'inputs': ['pld_replacement_d2_027'], 'func': pld_replacement_d3_027}


def pld_replacement_d3_028(pld_replacement_d2_028):
    feature = _clean(pld_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_028'] = {'inputs': ['pld_replacement_d2_028'], 'func': pld_replacement_d3_028}


def pld_replacement_d3_029(pld_replacement_d2_029):
    feature = _clean(pld_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_029'] = {'inputs': ['pld_replacement_d2_029'], 'func': pld_replacement_d3_029}


def pld_replacement_d3_030(pld_replacement_d2_030):
    feature = _clean(pld_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_030'] = {'inputs': ['pld_replacement_d2_030'], 'func': pld_replacement_d3_030}


def pld_replacement_d3_031(pld_replacement_d2_031):
    feature = _clean(pld_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_031'] = {'inputs': ['pld_replacement_d2_031'], 'func': pld_replacement_d3_031}


def pld_replacement_d3_032(pld_replacement_d2_032):
    feature = _clean(pld_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_032'] = {'inputs': ['pld_replacement_d2_032'], 'func': pld_replacement_d3_032}


def pld_replacement_d3_033(pld_replacement_d2_033):
    feature = _clean(pld_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_033'] = {'inputs': ['pld_replacement_d2_033'], 'func': pld_replacement_d3_033}


def pld_replacement_d3_034(pld_replacement_d2_034):
    feature = _clean(pld_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_034'] = {'inputs': ['pld_replacement_d2_034'], 'func': pld_replacement_d3_034}


def pld_replacement_d3_035(pld_replacement_d2_035):
    feature = _clean(pld_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_035'] = {'inputs': ['pld_replacement_d2_035'], 'func': pld_replacement_d3_035}


def pld_replacement_d3_036(pld_replacement_d2_036):
    feature = _clean(pld_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_036'] = {'inputs': ['pld_replacement_d2_036'], 'func': pld_replacement_d3_036}


def pld_replacement_d3_037(pld_replacement_d2_037):
    feature = _clean(pld_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_037'] = {'inputs': ['pld_replacement_d2_037'], 'func': pld_replacement_d3_037}


def pld_replacement_d3_038(pld_replacement_d2_038):
    feature = _clean(pld_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_038'] = {'inputs': ['pld_replacement_d2_038'], 'func': pld_replacement_d3_038}


def pld_replacement_d3_039(pld_replacement_d2_039):
    feature = _clean(pld_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_039'] = {'inputs': ['pld_replacement_d2_039'], 'func': pld_replacement_d3_039}


def pld_replacement_d3_040(pld_replacement_d2_040):
    feature = _clean(pld_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_040'] = {'inputs': ['pld_replacement_d2_040'], 'func': pld_replacement_d3_040}


def pld_replacement_d3_041(pld_replacement_d2_041):
    feature = _clean(pld_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_041'] = {'inputs': ['pld_replacement_d2_041'], 'func': pld_replacement_d3_041}


def pld_replacement_d3_042(pld_replacement_d2_042):
    feature = _clean(pld_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_042'] = {'inputs': ['pld_replacement_d2_042'], 'func': pld_replacement_d3_042}


def pld_replacement_d3_043(pld_replacement_d2_043):
    feature = _clean(pld_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_043'] = {'inputs': ['pld_replacement_d2_043'], 'func': pld_replacement_d3_043}


def pld_replacement_d3_044(pld_replacement_d2_044):
    feature = _clean(pld_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_044'] = {'inputs': ['pld_replacement_d2_044'], 'func': pld_replacement_d3_044}


def pld_replacement_d3_045(pld_replacement_d2_045):
    feature = _clean(pld_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_045'] = {'inputs': ['pld_replacement_d2_045'], 'func': pld_replacement_d3_045}


def pld_replacement_d3_046(pld_replacement_d2_046):
    feature = _clean(pld_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_046'] = {'inputs': ['pld_replacement_d2_046'], 'func': pld_replacement_d3_046}


def pld_replacement_d3_047(pld_replacement_d2_047):
    feature = _clean(pld_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_047'] = {'inputs': ['pld_replacement_d2_047'], 'func': pld_replacement_d3_047}


def pld_replacement_d3_048(pld_replacement_d2_048):
    feature = _clean(pld_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_048'] = {'inputs': ['pld_replacement_d2_048'], 'func': pld_replacement_d3_048}


def pld_replacement_d3_049(pld_replacement_d2_049):
    feature = _clean(pld_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_049'] = {'inputs': ['pld_replacement_d2_049'], 'func': pld_replacement_d3_049}


def pld_replacement_d3_050(pld_replacement_d2_050):
    feature = _clean(pld_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_050'] = {'inputs': ['pld_replacement_d2_050'], 'func': pld_replacement_d3_050}


def pld_replacement_d3_051(pld_replacement_d2_051):
    feature = _clean(pld_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_051'] = {'inputs': ['pld_replacement_d2_051'], 'func': pld_replacement_d3_051}


def pld_replacement_d3_052(pld_replacement_d2_052):
    feature = _clean(pld_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_052'] = {'inputs': ['pld_replacement_d2_052'], 'func': pld_replacement_d3_052}


def pld_replacement_d3_053(pld_replacement_d2_053):
    feature = _clean(pld_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_053'] = {'inputs': ['pld_replacement_d2_053'], 'func': pld_replacement_d3_053}


def pld_replacement_d3_054(pld_replacement_d2_054):
    feature = _clean(pld_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_054'] = {'inputs': ['pld_replacement_d2_054'], 'func': pld_replacement_d3_054}


def pld_replacement_d3_055(pld_replacement_d2_055):
    feature = _clean(pld_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_055'] = {'inputs': ['pld_replacement_d2_055'], 'func': pld_replacement_d3_055}


def pld_replacement_d3_056(pld_replacement_d2_056):
    feature = _clean(pld_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_056'] = {'inputs': ['pld_replacement_d2_056'], 'func': pld_replacement_d3_056}


def pld_replacement_d3_057(pld_replacement_d2_057):
    feature = _clean(pld_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_057'] = {'inputs': ['pld_replacement_d2_057'], 'func': pld_replacement_d3_057}


def pld_replacement_d3_058(pld_replacement_d2_058):
    feature = _clean(pld_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_058'] = {'inputs': ['pld_replacement_d2_058'], 'func': pld_replacement_d3_058}


def pld_replacement_d3_059(pld_replacement_d2_059):
    feature = _clean(pld_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_059'] = {'inputs': ['pld_replacement_d2_059'], 'func': pld_replacement_d3_059}


def pld_replacement_d3_060(pld_replacement_d2_060):
    feature = _clean(pld_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_060'] = {'inputs': ['pld_replacement_d2_060'], 'func': pld_replacement_d3_060}


def pld_replacement_d3_061(pld_replacement_d2_061):
    feature = _clean(pld_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_061'] = {'inputs': ['pld_replacement_d2_061'], 'func': pld_replacement_d3_061}


def pld_replacement_d3_062(pld_replacement_d2_062):
    feature = _clean(pld_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_062'] = {'inputs': ['pld_replacement_d2_062'], 'func': pld_replacement_d3_062}


def pld_replacement_d3_063(pld_replacement_d2_063):
    feature = _clean(pld_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_063'] = {'inputs': ['pld_replacement_d2_063'], 'func': pld_replacement_d3_063}


def pld_replacement_d3_064(pld_replacement_d2_064):
    feature = _clean(pld_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_064'] = {'inputs': ['pld_replacement_d2_064'], 'func': pld_replacement_d3_064}


def pld_replacement_d3_065(pld_replacement_d2_065):
    feature = _clean(pld_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_065'] = {'inputs': ['pld_replacement_d2_065'], 'func': pld_replacement_d3_065}


def pld_replacement_d3_066(pld_replacement_d2_066):
    feature = _clean(pld_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_066'] = {'inputs': ['pld_replacement_d2_066'], 'func': pld_replacement_d3_066}


def pld_replacement_d3_067(pld_replacement_d2_067):
    feature = _clean(pld_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_067'] = {'inputs': ['pld_replacement_d2_067'], 'func': pld_replacement_d3_067}


def pld_replacement_d3_068(pld_replacement_d2_068):
    feature = _clean(pld_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_068'] = {'inputs': ['pld_replacement_d2_068'], 'func': pld_replacement_d3_068}


def pld_replacement_d3_069(pld_replacement_d2_069):
    feature = _clean(pld_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_069'] = {'inputs': ['pld_replacement_d2_069'], 'func': pld_replacement_d3_069}


def pld_replacement_d3_070(pld_replacement_d2_070):
    feature = _clean(pld_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_070'] = {'inputs': ['pld_replacement_d2_070'], 'func': pld_replacement_d3_070}


def pld_replacement_d3_071(pld_replacement_d2_071):
    feature = _clean(pld_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_071'] = {'inputs': ['pld_replacement_d2_071'], 'func': pld_replacement_d3_071}


def pld_replacement_d3_072(pld_replacement_d2_072):
    feature = _clean(pld_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_072'] = {'inputs': ['pld_replacement_d2_072'], 'func': pld_replacement_d3_072}


def pld_replacement_d3_073(pld_replacement_d2_073):
    feature = _clean(pld_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_073'] = {'inputs': ['pld_replacement_d2_073'], 'func': pld_replacement_d3_073}


def pld_replacement_d3_074(pld_replacement_d2_074):
    feature = _clean(pld_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_074'] = {'inputs': ['pld_replacement_d2_074'], 'func': pld_replacement_d3_074}


def pld_replacement_d3_075(pld_replacement_d2_075):
    feature = _clean(pld_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_075'] = {'inputs': ['pld_replacement_d2_075'], 'func': pld_replacement_d3_075}


def pld_replacement_d3_076(pld_replacement_d2_076):
    feature = _clean(pld_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_076'] = {'inputs': ['pld_replacement_d2_076'], 'func': pld_replacement_d3_076}


def pld_replacement_d3_077(pld_replacement_d2_077):
    feature = _clean(pld_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_077'] = {'inputs': ['pld_replacement_d2_077'], 'func': pld_replacement_d3_077}


def pld_replacement_d3_078(pld_replacement_d2_078):
    feature = _clean(pld_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_078'] = {'inputs': ['pld_replacement_d2_078'], 'func': pld_replacement_d3_078}


def pld_replacement_d3_079(pld_replacement_d2_079):
    feature = _clean(pld_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_079'] = {'inputs': ['pld_replacement_d2_079'], 'func': pld_replacement_d3_079}


def pld_replacement_d3_080(pld_replacement_d2_080):
    feature = _clean(pld_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_080'] = {'inputs': ['pld_replacement_d2_080'], 'func': pld_replacement_d3_080}


def pld_replacement_d3_081(pld_replacement_d2_081):
    feature = _clean(pld_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_081'] = {'inputs': ['pld_replacement_d2_081'], 'func': pld_replacement_d3_081}


def pld_replacement_d3_082(pld_replacement_d2_082):
    feature = _clean(pld_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_082'] = {'inputs': ['pld_replacement_d2_082'], 'func': pld_replacement_d3_082}


def pld_replacement_d3_083(pld_replacement_d2_083):
    feature = _clean(pld_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_083'] = {'inputs': ['pld_replacement_d2_083'], 'func': pld_replacement_d3_083}


def pld_replacement_d3_084(pld_replacement_d2_084):
    feature = _clean(pld_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_084'] = {'inputs': ['pld_replacement_d2_084'], 'func': pld_replacement_d3_084}


def pld_replacement_d3_085(pld_replacement_d2_085):
    feature = _clean(pld_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_085'] = {'inputs': ['pld_replacement_d2_085'], 'func': pld_replacement_d3_085}


def pld_replacement_d3_086(pld_replacement_d2_086):
    feature = _clean(pld_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_086'] = {'inputs': ['pld_replacement_d2_086'], 'func': pld_replacement_d3_086}


def pld_replacement_d3_087(pld_replacement_d2_087):
    feature = _clean(pld_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_087'] = {'inputs': ['pld_replacement_d2_087'], 'func': pld_replacement_d3_087}


def pld_replacement_d3_088(pld_replacement_d2_088):
    feature = _clean(pld_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_088'] = {'inputs': ['pld_replacement_d2_088'], 'func': pld_replacement_d3_088}


def pld_replacement_d3_089(pld_replacement_d2_089):
    feature = _clean(pld_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_089'] = {'inputs': ['pld_replacement_d2_089'], 'func': pld_replacement_d3_089}


def pld_replacement_d3_090(pld_replacement_d2_090):
    feature = _clean(pld_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_090'] = {'inputs': ['pld_replacement_d2_090'], 'func': pld_replacement_d3_090}


def pld_replacement_d3_091(pld_replacement_d2_091):
    feature = _clean(pld_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_091'] = {'inputs': ['pld_replacement_d2_091'], 'func': pld_replacement_d3_091}


def pld_replacement_d3_092(pld_replacement_d2_092):
    feature = _clean(pld_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_092'] = {'inputs': ['pld_replacement_d2_092'], 'func': pld_replacement_d3_092}


def pld_replacement_d3_093(pld_replacement_d2_093):
    feature = _clean(pld_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_093'] = {'inputs': ['pld_replacement_d2_093'], 'func': pld_replacement_d3_093}


def pld_replacement_d3_094(pld_replacement_d2_094):
    feature = _clean(pld_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_094'] = {'inputs': ['pld_replacement_d2_094'], 'func': pld_replacement_d3_094}


def pld_replacement_d3_095(pld_replacement_d2_095):
    feature = _clean(pld_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_095'] = {'inputs': ['pld_replacement_d2_095'], 'func': pld_replacement_d3_095}


def pld_replacement_d3_096(pld_replacement_d2_096):
    feature = _clean(pld_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_096'] = {'inputs': ['pld_replacement_d2_096'], 'func': pld_replacement_d3_096}


def pld_replacement_d3_097(pld_replacement_d2_097):
    feature = _clean(pld_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_097'] = {'inputs': ['pld_replacement_d2_097'], 'func': pld_replacement_d3_097}


def pld_replacement_d3_098(pld_replacement_d2_098):
    feature = _clean(pld_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_098'] = {'inputs': ['pld_replacement_d2_098'], 'func': pld_replacement_d3_098}


def pld_replacement_d3_099(pld_replacement_d2_099):
    feature = _clean(pld_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_099'] = {'inputs': ['pld_replacement_d2_099'], 'func': pld_replacement_d3_099}


def pld_replacement_d3_100(pld_replacement_d2_100):
    feature = _clean(pld_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_100'] = {'inputs': ['pld_replacement_d2_100'], 'func': pld_replacement_d3_100}


def pld_replacement_d3_101(pld_replacement_d2_101):
    feature = _clean(pld_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_101'] = {'inputs': ['pld_replacement_d2_101'], 'func': pld_replacement_d3_101}


def pld_replacement_d3_102(pld_replacement_d2_102):
    feature = _clean(pld_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_102'] = {'inputs': ['pld_replacement_d2_102'], 'func': pld_replacement_d3_102}


def pld_replacement_d3_103(pld_replacement_d2_103):
    feature = _clean(pld_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_103'] = {'inputs': ['pld_replacement_d2_103'], 'func': pld_replacement_d3_103}


def pld_replacement_d3_104(pld_replacement_d2_104):
    feature = _clean(pld_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_104'] = {'inputs': ['pld_replacement_d2_104'], 'func': pld_replacement_d3_104}


def pld_replacement_d3_105(pld_replacement_d2_105):
    feature = _clean(pld_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_105'] = {'inputs': ['pld_replacement_d2_105'], 'func': pld_replacement_d3_105}


def pld_replacement_d3_106(pld_replacement_d2_106):
    feature = _clean(pld_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_106'] = {'inputs': ['pld_replacement_d2_106'], 'func': pld_replacement_d3_106}


def pld_replacement_d3_107(pld_replacement_d2_107):
    feature = _clean(pld_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_107'] = {'inputs': ['pld_replacement_d2_107'], 'func': pld_replacement_d3_107}


def pld_replacement_d3_108(pld_replacement_d2_108):
    feature = _clean(pld_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_108'] = {'inputs': ['pld_replacement_d2_108'], 'func': pld_replacement_d3_108}


def pld_replacement_d3_109(pld_replacement_d2_109):
    feature = _clean(pld_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_109'] = {'inputs': ['pld_replacement_d2_109'], 'func': pld_replacement_d3_109}


def pld_replacement_d3_110(pld_replacement_d2_110):
    feature = _clean(pld_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_110'] = {'inputs': ['pld_replacement_d2_110'], 'func': pld_replacement_d3_110}


def pld_replacement_d3_111(pld_replacement_d2_111):
    feature = _clean(pld_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_111'] = {'inputs': ['pld_replacement_d2_111'], 'func': pld_replacement_d3_111}


def pld_replacement_d3_112(pld_replacement_d2_112):
    feature = _clean(pld_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_112'] = {'inputs': ['pld_replacement_d2_112'], 'func': pld_replacement_d3_112}


def pld_replacement_d3_113(pld_replacement_d2_113):
    feature = _clean(pld_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_113'] = {'inputs': ['pld_replacement_d2_113'], 'func': pld_replacement_d3_113}


def pld_replacement_d3_114(pld_replacement_d2_114):
    feature = _clean(pld_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_114'] = {'inputs': ['pld_replacement_d2_114'], 'func': pld_replacement_d3_114}


def pld_replacement_d3_115(pld_replacement_d2_115):
    feature = _clean(pld_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_115'] = {'inputs': ['pld_replacement_d2_115'], 'func': pld_replacement_d3_115}


def pld_replacement_d3_116(pld_replacement_d2_116):
    feature = _clean(pld_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_116'] = {'inputs': ['pld_replacement_d2_116'], 'func': pld_replacement_d3_116}


def pld_replacement_d3_117(pld_replacement_d2_117):
    feature = _clean(pld_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_117'] = {'inputs': ['pld_replacement_d2_117'], 'func': pld_replacement_d3_117}


def pld_replacement_d3_118(pld_replacement_d2_118):
    feature = _clean(pld_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_118'] = {'inputs': ['pld_replacement_d2_118'], 'func': pld_replacement_d3_118}


def pld_replacement_d3_119(pld_replacement_d2_119):
    feature = _clean(pld_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_119'] = {'inputs': ['pld_replacement_d2_119'], 'func': pld_replacement_d3_119}


def pld_replacement_d3_120(pld_replacement_d2_120):
    feature = _clean(pld_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_120'] = {'inputs': ['pld_replacement_d2_120'], 'func': pld_replacement_d3_120}


def pld_replacement_d3_121(pld_replacement_d2_121):
    feature = _clean(pld_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_121'] = {'inputs': ['pld_replacement_d2_121'], 'func': pld_replacement_d3_121}


def pld_replacement_d3_122(pld_replacement_d2_122):
    feature = _clean(pld_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_122'] = {'inputs': ['pld_replacement_d2_122'], 'func': pld_replacement_d3_122}


def pld_replacement_d3_123(pld_replacement_d2_123):
    feature = _clean(pld_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_123'] = {'inputs': ['pld_replacement_d2_123'], 'func': pld_replacement_d3_123}


def pld_replacement_d3_124(pld_replacement_d2_124):
    feature = _clean(pld_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_124'] = {'inputs': ['pld_replacement_d2_124'], 'func': pld_replacement_d3_124}


def pld_replacement_d3_125(pld_replacement_d2_125):
    feature = _clean(pld_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_125'] = {'inputs': ['pld_replacement_d2_125'], 'func': pld_replacement_d3_125}


def pld_replacement_d3_126(pld_replacement_d2_126):
    feature = _clean(pld_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_126'] = {'inputs': ['pld_replacement_d2_126'], 'func': pld_replacement_d3_126}


def pld_replacement_d3_127(pld_replacement_d2_127):
    feature = _clean(pld_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_127'] = {'inputs': ['pld_replacement_d2_127'], 'func': pld_replacement_d3_127}


def pld_replacement_d3_128(pld_replacement_d2_128):
    feature = _clean(pld_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_128'] = {'inputs': ['pld_replacement_d2_128'], 'func': pld_replacement_d3_128}


def pld_replacement_d3_129(pld_replacement_d2_129):
    feature = _clean(pld_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_129'] = {'inputs': ['pld_replacement_d2_129'], 'func': pld_replacement_d3_129}


def pld_replacement_d3_130(pld_replacement_d2_130):
    feature = _clean(pld_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_130'] = {'inputs': ['pld_replacement_d2_130'], 'func': pld_replacement_d3_130}


def pld_replacement_d3_131(pld_replacement_d2_131):
    feature = _clean(pld_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_131'] = {'inputs': ['pld_replacement_d2_131'], 'func': pld_replacement_d3_131}


def pld_replacement_d3_132(pld_replacement_d2_132):
    feature = _clean(pld_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_132'] = {'inputs': ['pld_replacement_d2_132'], 'func': pld_replacement_d3_132}


def pld_replacement_d3_133(pld_replacement_d2_133):
    feature = _clean(pld_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_133'] = {'inputs': ['pld_replacement_d2_133'], 'func': pld_replacement_d3_133}


def pld_replacement_d3_134(pld_replacement_d2_134):
    feature = _clean(pld_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_134'] = {'inputs': ['pld_replacement_d2_134'], 'func': pld_replacement_d3_134}


def pld_replacement_d3_135(pld_replacement_d2_135):
    feature = _clean(pld_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_135'] = {'inputs': ['pld_replacement_d2_135'], 'func': pld_replacement_d3_135}


def pld_replacement_d3_136(pld_replacement_d2_136):
    feature = _clean(pld_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_136'] = {'inputs': ['pld_replacement_d2_136'], 'func': pld_replacement_d3_136}


def pld_replacement_d3_137(pld_replacement_d2_137):
    feature = _clean(pld_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_137'] = {'inputs': ['pld_replacement_d2_137'], 'func': pld_replacement_d3_137}


def pld_replacement_d3_138(pld_replacement_d2_138):
    feature = _clean(pld_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_138'] = {'inputs': ['pld_replacement_d2_138'], 'func': pld_replacement_d3_138}


def pld_replacement_d3_139(pld_replacement_d2_139):
    feature = _clean(pld_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_139'] = {'inputs': ['pld_replacement_d2_139'], 'func': pld_replacement_d3_139}


def pld_replacement_d3_140(pld_replacement_d2_140):
    feature = _clean(pld_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_140'] = {'inputs': ['pld_replacement_d2_140'], 'func': pld_replacement_d3_140}


def pld_replacement_d3_141(pld_replacement_d2_141):
    feature = _clean(pld_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_141'] = {'inputs': ['pld_replacement_d2_141'], 'func': pld_replacement_d3_141}


def pld_replacement_d3_142(pld_replacement_d2_142):
    feature = _clean(pld_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_142'] = {'inputs': ['pld_replacement_d2_142'], 'func': pld_replacement_d3_142}


def pld_replacement_d3_143(pld_replacement_d2_143):
    feature = _clean(pld_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_143'] = {'inputs': ['pld_replacement_d2_143'], 'func': pld_replacement_d3_143}


def pld_replacement_d3_144(pld_replacement_d2_144):
    feature = _clean(pld_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_144'] = {'inputs': ['pld_replacement_d2_144'], 'func': pld_replacement_d3_144}


def pld_replacement_d3_145(pld_replacement_d2_145):
    feature = _clean(pld_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_145'] = {'inputs': ['pld_replacement_d2_145'], 'func': pld_replacement_d3_145}


def pld_replacement_d3_146(pld_replacement_d2_146):
    feature = _clean(pld_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_146'] = {'inputs': ['pld_replacement_d2_146'], 'func': pld_replacement_d3_146}


def pld_replacement_d3_147(pld_replacement_d2_147):
    feature = _clean(pld_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_147'] = {'inputs': ['pld_replacement_d2_147'], 'func': pld_replacement_d3_147}


def pld_replacement_d3_148(pld_replacement_d2_148):
    feature = _clean(pld_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_148'] = {'inputs': ['pld_replacement_d2_148'], 'func': pld_replacement_d3_148}


def pld_replacement_d3_149(pld_replacement_d2_149):
    feature = _clean(pld_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_149'] = {'inputs': ['pld_replacement_d2_149'], 'func': pld_replacement_d3_149}


def pld_replacement_d3_150(pld_replacement_d2_150):
    feature = _clean(pld_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_150'] = {'inputs': ['pld_replacement_d2_150'], 'func': pld_replacement_d3_150}


def pld_replacement_d3_151(pld_replacement_d2_151):
    feature = _clean(pld_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_151'] = {'inputs': ['pld_replacement_d2_151'], 'func': pld_replacement_d3_151}


def pld_replacement_d3_152(pld_replacement_d2_152):
    feature = _clean(pld_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_152'] = {'inputs': ['pld_replacement_d2_152'], 'func': pld_replacement_d3_152}


def pld_replacement_d3_153(pld_replacement_d2_153):
    feature = _clean(pld_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_153'] = {'inputs': ['pld_replacement_d2_153'], 'func': pld_replacement_d3_153}


def pld_replacement_d3_154(pld_replacement_d2_154):
    feature = _clean(pld_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_154'] = {'inputs': ['pld_replacement_d2_154'], 'func': pld_replacement_d3_154}


def pld_replacement_d3_155(pld_replacement_d2_155):
    feature = _clean(pld_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_155'] = {'inputs': ['pld_replacement_d2_155'], 'func': pld_replacement_d3_155}


def pld_replacement_d3_156(pld_replacement_d2_156):
    feature = _clean(pld_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_156'] = {'inputs': ['pld_replacement_d2_156'], 'func': pld_replacement_d3_156}


def pld_replacement_d3_157(pld_replacement_d2_157):
    feature = _clean(pld_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_157'] = {'inputs': ['pld_replacement_d2_157'], 'func': pld_replacement_d3_157}


def pld_replacement_d3_158(pld_replacement_d2_158):
    feature = _clean(pld_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_158'] = {'inputs': ['pld_replacement_d2_158'], 'func': pld_replacement_d3_158}


def pld_replacement_d3_159(pld_replacement_d2_159):
    feature = _clean(pld_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_159'] = {'inputs': ['pld_replacement_d2_159'], 'func': pld_replacement_d3_159}


def pld_replacement_d3_160(pld_replacement_d2_160):
    feature = _clean(pld_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_160'] = {'inputs': ['pld_replacement_d2_160'], 'func': pld_replacement_d3_160}


def pld_replacement_d3_161(pld_replacement_d2_161):
    feature = _clean(pld_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_161'] = {'inputs': ['pld_replacement_d2_161'], 'func': pld_replacement_d3_161}


def pld_replacement_d3_162(pld_replacement_d2_162):
    feature = _clean(pld_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_162'] = {'inputs': ['pld_replacement_d2_162'], 'func': pld_replacement_d3_162}


def pld_replacement_d3_163(pld_replacement_d2_163):
    feature = _clean(pld_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_163'] = {'inputs': ['pld_replacement_d2_163'], 'func': pld_replacement_d3_163}


def pld_replacement_d3_164(pld_replacement_d2_164):
    feature = _clean(pld_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_164'] = {'inputs': ['pld_replacement_d2_164'], 'func': pld_replacement_d3_164}


def pld_replacement_d3_165(pld_replacement_d2_165):
    feature = _clean(pld_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_165'] = {'inputs': ['pld_replacement_d2_165'], 'func': pld_replacement_d3_165}


def pld_replacement_d3_166(pld_replacement_d2_166):
    feature = _clean(pld_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_166'] = {'inputs': ['pld_replacement_d2_166'], 'func': pld_replacement_d3_166}


def pld_replacement_d3_167(pld_replacement_d2_167):
    feature = _clean(pld_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_167'] = {'inputs': ['pld_replacement_d2_167'], 'func': pld_replacement_d3_167}


def pld_replacement_d3_168(pld_replacement_d2_168):
    feature = _clean(pld_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_168'] = {'inputs': ['pld_replacement_d2_168'], 'func': pld_replacement_d3_168}


def pld_replacement_d3_169(pld_replacement_d2_169):
    feature = _clean(pld_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_169'] = {'inputs': ['pld_replacement_d2_169'], 'func': pld_replacement_d3_169}


def pld_replacement_d3_170(pld_replacement_d2_170):
    feature = _clean(pld_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
PLD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pld_replacement_d3_170'] = {'inputs': ['pld_replacement_d2_170'], 'func': pld_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pld_base_universe_d3_001_pld_002_zero_volume_frequency_10_002(pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002):
    return _base_universe_d3(pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002, 1)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_001_pld_002_zero_volume_frequency_10_002'] = {'inputs': ['pld_base_universe_d2_001_pld_002_zero_volume_frequency_10_002'], 'func': pld_base_universe_d3_001_pld_002_zero_volume_frequency_10_002}


def pld_base_universe_d3_002_pld_003_spread_proxy_21_003(pld_base_universe_d2_002_pld_003_spread_proxy_21_003):
    return _base_universe_d3(pld_base_universe_d2_002_pld_003_spread_proxy_21_003, 2)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_002_pld_003_spread_proxy_21_003'] = {'inputs': ['pld_base_universe_d2_002_pld_003_spread_proxy_21_003'], 'func': pld_base_universe_d3_002_pld_003_spread_proxy_21_003}


def pld_base_universe_d3_003_pld_004_trading_intensity_42_004(pld_base_universe_d2_003_pld_004_trading_intensity_42_004):
    return _base_universe_d3(pld_base_universe_d2_003_pld_004_trading_intensity_42_004, 3)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_003_pld_004_trading_intensity_42_004'] = {'inputs': ['pld_base_universe_d2_003_pld_004_trading_intensity_42_004'], 'func': pld_base_universe_d3_003_pld_004_trading_intensity_42_004}


def pld_base_universe_d3_004_pld_006_price_level_distress_84_006(pld_base_universe_d2_004_pld_006_price_level_distress_84_006):
    return _base_universe_d3(pld_base_universe_d2_004_pld_006_price_level_distress_84_006, 4)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_004_pld_006_price_level_distress_84_006'] = {'inputs': ['pld_base_universe_d2_004_pld_006_price_level_distress_84_006'], 'func': pld_base_universe_d3_004_pld_006_price_level_distress_84_006}


def pld_base_universe_d3_005_pld_008_zero_volume_frequency_189_008(pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008):
    return _base_universe_d3(pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008, 5)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_005_pld_008_zero_volume_frequency_189_008'] = {'inputs': ['pld_base_universe_d2_005_pld_008_zero_volume_frequency_189_008'], 'func': pld_base_universe_d3_005_pld_008_zero_volume_frequency_189_008}


def pld_base_universe_d3_006_pld_009_spread_proxy_252_009(pld_base_universe_d2_006_pld_009_spread_proxy_252_009):
    return _base_universe_d3(pld_base_universe_d2_006_pld_009_spread_proxy_252_009, 6)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_006_pld_009_spread_proxy_252_009'] = {'inputs': ['pld_base_universe_d2_006_pld_009_spread_proxy_252_009'], 'func': pld_base_universe_d3_006_pld_009_spread_proxy_252_009}


def pld_base_universe_d3_007_pld_010_trading_intensity_378_010(pld_base_universe_d2_007_pld_010_trading_intensity_378_010):
    return _base_universe_d3(pld_base_universe_d2_007_pld_010_trading_intensity_378_010, 7)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_007_pld_010_trading_intensity_378_010'] = {'inputs': ['pld_base_universe_d2_007_pld_010_trading_intensity_378_010'], 'func': pld_base_universe_d3_007_pld_010_trading_intensity_378_010}


def pld_base_universe_d3_008_pld_012_price_level_distress_756_012(pld_base_universe_d2_008_pld_012_price_level_distress_756_012):
    return _base_universe_d3(pld_base_universe_d2_008_pld_012_price_level_distress_756_012, 8)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_008_pld_012_price_level_distress_756_012'] = {'inputs': ['pld_base_universe_d2_008_pld_012_price_level_distress_756_012'], 'func': pld_base_universe_d3_008_pld_012_price_level_distress_756_012}


def pld_base_universe_d3_009_pld_014_zero_volume_frequency_1260_014(pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014, 9)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_009_pld_014_zero_volume_frequency_1260_014'] = {'inputs': ['pld_base_universe_d2_009_pld_014_zero_volume_frequency_1260_014'], 'func': pld_base_universe_d3_009_pld_014_zero_volume_frequency_1260_014}


def pld_base_universe_d3_010_pld_015_spread_proxy_1512_015(pld_base_universe_d2_010_pld_015_spread_proxy_1512_015):
    return _base_universe_d3(pld_base_universe_d2_010_pld_015_spread_proxy_1512_015, 10)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_010_pld_015_spread_proxy_1512_015'] = {'inputs': ['pld_base_universe_d2_010_pld_015_spread_proxy_1512_015'], 'func': pld_base_universe_d3_010_pld_015_spread_proxy_1512_015}


def pld_base_universe_d3_011_pld_016_trading_intensity_5_016(pld_base_universe_d2_011_pld_016_trading_intensity_5_016):
    return _base_universe_d3(pld_base_universe_d2_011_pld_016_trading_intensity_5_016, 11)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_011_pld_016_trading_intensity_5_016'] = {'inputs': ['pld_base_universe_d2_011_pld_016_trading_intensity_5_016'], 'func': pld_base_universe_d3_011_pld_016_trading_intensity_5_016}


def pld_base_universe_d3_012_pld_018_price_level_distress_21_018(pld_base_universe_d2_012_pld_018_price_level_distress_21_018):
    return _base_universe_d3(pld_base_universe_d2_012_pld_018_price_level_distress_21_018, 12)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_012_pld_018_price_level_distress_21_018'] = {'inputs': ['pld_base_universe_d2_012_pld_018_price_level_distress_21_018'], 'func': pld_base_universe_d3_012_pld_018_price_level_distress_21_018}


def pld_base_universe_d3_013_pld_020_zero_volume_frequency_63_020(pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020):
    return _base_universe_d3(pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020, 13)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_013_pld_020_zero_volume_frequency_63_020'] = {'inputs': ['pld_base_universe_d2_013_pld_020_zero_volume_frequency_63_020'], 'func': pld_base_universe_d3_013_pld_020_zero_volume_frequency_63_020}


def pld_base_universe_d3_014_pld_021_spread_proxy_84_021(pld_base_universe_d2_014_pld_021_spread_proxy_84_021):
    return _base_universe_d3(pld_base_universe_d2_014_pld_021_spread_proxy_84_021, 14)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_014_pld_021_spread_proxy_84_021'] = {'inputs': ['pld_base_universe_d2_014_pld_021_spread_proxy_84_021'], 'func': pld_base_universe_d3_014_pld_021_spread_proxy_84_021}


def pld_base_universe_d3_015_pld_022_trading_intensity_126_022(pld_base_universe_d2_015_pld_022_trading_intensity_126_022):
    return _base_universe_d3(pld_base_universe_d2_015_pld_022_trading_intensity_126_022, 15)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_015_pld_022_trading_intensity_126_022'] = {'inputs': ['pld_base_universe_d2_015_pld_022_trading_intensity_126_022'], 'func': pld_base_universe_d3_015_pld_022_trading_intensity_126_022}


def pld_base_universe_d3_016_pld_024_price_level_distress_252_024(pld_base_universe_d2_016_pld_024_price_level_distress_252_024):
    return _base_universe_d3(pld_base_universe_d2_016_pld_024_price_level_distress_252_024, 16)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_016_pld_024_price_level_distress_252_024'] = {'inputs': ['pld_base_universe_d2_016_pld_024_price_level_distress_252_024'], 'func': pld_base_universe_d3_016_pld_024_price_level_distress_252_024}


def pld_base_universe_d3_017_pld_026_zero_volume_frequency_504_026(pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026):
    return _base_universe_d3(pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026, 17)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_017_pld_026_zero_volume_frequency_504_026'] = {'inputs': ['pld_base_universe_d2_017_pld_026_zero_volume_frequency_504_026'], 'func': pld_base_universe_d3_017_pld_026_zero_volume_frequency_504_026}


def pld_base_universe_d3_018_pld_027_spread_proxy_756_027(pld_base_universe_d2_018_pld_027_spread_proxy_756_027):
    return _base_universe_d3(pld_base_universe_d2_018_pld_027_spread_proxy_756_027, 18)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_018_pld_027_spread_proxy_756_027'] = {'inputs': ['pld_base_universe_d2_018_pld_027_spread_proxy_756_027'], 'func': pld_base_universe_d3_018_pld_027_spread_proxy_756_027}


def pld_base_universe_d3_019_pld_028_trading_intensity_1008_028(pld_base_universe_d2_019_pld_028_trading_intensity_1008_028):
    return _base_universe_d3(pld_base_universe_d2_019_pld_028_trading_intensity_1008_028, 19)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_019_pld_028_trading_intensity_1008_028'] = {'inputs': ['pld_base_universe_d2_019_pld_028_trading_intensity_1008_028'], 'func': pld_base_universe_d3_019_pld_028_trading_intensity_1008_028}


def pld_base_universe_d3_020_pld_030_price_level_distress_1512_030(pld_base_universe_d2_020_pld_030_price_level_distress_1512_030):
    return _base_universe_d3(pld_base_universe_d2_020_pld_030_price_level_distress_1512_030, 20)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_020_pld_030_price_level_distress_1512_030'] = {'inputs': ['pld_base_universe_d2_020_pld_030_price_level_distress_1512_030'], 'func': pld_base_universe_d3_020_pld_030_price_level_distress_1512_030}


def pld_base_universe_d3_021_pld_basefill_001(pld_base_universe_d2_021_pld_basefill_001):
    return _base_universe_d3(pld_base_universe_d2_021_pld_basefill_001, 21)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_021_pld_basefill_001'] = {'inputs': ['pld_base_universe_d2_021_pld_basefill_001'], 'func': pld_base_universe_d3_021_pld_basefill_001}


def pld_base_universe_d3_022_pld_basefill_005(pld_base_universe_d2_022_pld_basefill_005):
    return _base_universe_d3(pld_base_universe_d2_022_pld_basefill_005, 22)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_022_pld_basefill_005'] = {'inputs': ['pld_base_universe_d2_022_pld_basefill_005'], 'func': pld_base_universe_d3_022_pld_basefill_005}


def pld_base_universe_d3_023_pld_basefill_007(pld_base_universe_d2_023_pld_basefill_007):
    return _base_universe_d3(pld_base_universe_d2_023_pld_basefill_007, 23)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_023_pld_basefill_007'] = {'inputs': ['pld_base_universe_d2_023_pld_basefill_007'], 'func': pld_base_universe_d3_023_pld_basefill_007}


def pld_base_universe_d3_024_pld_basefill_011(pld_base_universe_d2_024_pld_basefill_011):
    return _base_universe_d3(pld_base_universe_d2_024_pld_basefill_011, 24)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_024_pld_basefill_011'] = {'inputs': ['pld_base_universe_d2_024_pld_basefill_011'], 'func': pld_base_universe_d3_024_pld_basefill_011}


def pld_base_universe_d3_025_pld_basefill_013(pld_base_universe_d2_025_pld_basefill_013):
    return _base_universe_d3(pld_base_universe_d2_025_pld_basefill_013, 25)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_025_pld_basefill_013'] = {'inputs': ['pld_base_universe_d2_025_pld_basefill_013'], 'func': pld_base_universe_d3_025_pld_basefill_013}


def pld_base_universe_d3_026_pld_basefill_017(pld_base_universe_d2_026_pld_basefill_017):
    return _base_universe_d3(pld_base_universe_d2_026_pld_basefill_017, 26)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_026_pld_basefill_017'] = {'inputs': ['pld_base_universe_d2_026_pld_basefill_017'], 'func': pld_base_universe_d3_026_pld_basefill_017}


def pld_base_universe_d3_027_pld_basefill_019(pld_base_universe_d2_027_pld_basefill_019):
    return _base_universe_d3(pld_base_universe_d2_027_pld_basefill_019, 27)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_027_pld_basefill_019'] = {'inputs': ['pld_base_universe_d2_027_pld_basefill_019'], 'func': pld_base_universe_d3_027_pld_basefill_019}


def pld_base_universe_d3_028_pld_basefill_023(pld_base_universe_d2_028_pld_basefill_023):
    return _base_universe_d3(pld_base_universe_d2_028_pld_basefill_023, 28)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_028_pld_basefill_023'] = {'inputs': ['pld_base_universe_d2_028_pld_basefill_023'], 'func': pld_base_universe_d3_028_pld_basefill_023}


def pld_base_universe_d3_029_pld_basefill_025(pld_base_universe_d2_029_pld_basefill_025):
    return _base_universe_d3(pld_base_universe_d2_029_pld_basefill_025, 29)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_029_pld_basefill_025'] = {'inputs': ['pld_base_universe_d2_029_pld_basefill_025'], 'func': pld_base_universe_d3_029_pld_basefill_025}


def pld_base_universe_d3_030_pld_basefill_029(pld_base_universe_d2_030_pld_basefill_029):
    return _base_universe_d3(pld_base_universe_d2_030_pld_basefill_029, 30)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_030_pld_basefill_029'] = {'inputs': ['pld_base_universe_d2_030_pld_basefill_029'], 'func': pld_base_universe_d3_030_pld_basefill_029}


def pld_base_universe_d3_031_pld_basefill_031(pld_base_universe_d2_031_pld_basefill_031):
    return _base_universe_d3(pld_base_universe_d2_031_pld_basefill_031, 31)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_031_pld_basefill_031'] = {'inputs': ['pld_base_universe_d2_031_pld_basefill_031'], 'func': pld_base_universe_d3_031_pld_basefill_031}


def pld_base_universe_d3_032_pld_basefill_032(pld_base_universe_d2_032_pld_basefill_032):
    return _base_universe_d3(pld_base_universe_d2_032_pld_basefill_032, 32)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_032_pld_basefill_032'] = {'inputs': ['pld_base_universe_d2_032_pld_basefill_032'], 'func': pld_base_universe_d3_032_pld_basefill_032}


def pld_base_universe_d3_033_pld_basefill_033(pld_base_universe_d2_033_pld_basefill_033):
    return _base_universe_d3(pld_base_universe_d2_033_pld_basefill_033, 33)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_033_pld_basefill_033'] = {'inputs': ['pld_base_universe_d2_033_pld_basefill_033'], 'func': pld_base_universe_d3_033_pld_basefill_033}


def pld_base_universe_d3_034_pld_basefill_034(pld_base_universe_d2_034_pld_basefill_034):
    return _base_universe_d3(pld_base_universe_d2_034_pld_basefill_034, 34)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_034_pld_basefill_034'] = {'inputs': ['pld_base_universe_d2_034_pld_basefill_034'], 'func': pld_base_universe_d3_034_pld_basefill_034}


def pld_base_universe_d3_035_pld_basefill_035(pld_base_universe_d2_035_pld_basefill_035):
    return _base_universe_d3(pld_base_universe_d2_035_pld_basefill_035, 35)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_035_pld_basefill_035'] = {'inputs': ['pld_base_universe_d2_035_pld_basefill_035'], 'func': pld_base_universe_d3_035_pld_basefill_035}


def pld_base_universe_d3_036_pld_basefill_036(pld_base_universe_d2_036_pld_basefill_036):
    return _base_universe_d3(pld_base_universe_d2_036_pld_basefill_036, 36)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_036_pld_basefill_036'] = {'inputs': ['pld_base_universe_d2_036_pld_basefill_036'], 'func': pld_base_universe_d3_036_pld_basefill_036}


def pld_base_universe_d3_037_pld_basefill_037(pld_base_universe_d2_037_pld_basefill_037):
    return _base_universe_d3(pld_base_universe_d2_037_pld_basefill_037, 37)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_037_pld_basefill_037'] = {'inputs': ['pld_base_universe_d2_037_pld_basefill_037'], 'func': pld_base_universe_d3_037_pld_basefill_037}


def pld_base_universe_d3_038_pld_basefill_038(pld_base_universe_d2_038_pld_basefill_038):
    return _base_universe_d3(pld_base_universe_d2_038_pld_basefill_038, 38)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_038_pld_basefill_038'] = {'inputs': ['pld_base_universe_d2_038_pld_basefill_038'], 'func': pld_base_universe_d3_038_pld_basefill_038}


def pld_base_universe_d3_039_pld_basefill_039(pld_base_universe_d2_039_pld_basefill_039):
    return _base_universe_d3(pld_base_universe_d2_039_pld_basefill_039, 39)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_039_pld_basefill_039'] = {'inputs': ['pld_base_universe_d2_039_pld_basefill_039'], 'func': pld_base_universe_d3_039_pld_basefill_039}


def pld_base_universe_d3_040_pld_basefill_040(pld_base_universe_d2_040_pld_basefill_040):
    return _base_universe_d3(pld_base_universe_d2_040_pld_basefill_040, 40)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_040_pld_basefill_040'] = {'inputs': ['pld_base_universe_d2_040_pld_basefill_040'], 'func': pld_base_universe_d3_040_pld_basefill_040}


def pld_base_universe_d3_041_pld_basefill_041(pld_base_universe_d2_041_pld_basefill_041):
    return _base_universe_d3(pld_base_universe_d2_041_pld_basefill_041, 41)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_041_pld_basefill_041'] = {'inputs': ['pld_base_universe_d2_041_pld_basefill_041'], 'func': pld_base_universe_d3_041_pld_basefill_041}


def pld_base_universe_d3_042_pld_basefill_042(pld_base_universe_d2_042_pld_basefill_042):
    return _base_universe_d3(pld_base_universe_d2_042_pld_basefill_042, 42)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_042_pld_basefill_042'] = {'inputs': ['pld_base_universe_d2_042_pld_basefill_042'], 'func': pld_base_universe_d3_042_pld_basefill_042}


def pld_base_universe_d3_043_pld_basefill_043(pld_base_universe_d2_043_pld_basefill_043):
    return _base_universe_d3(pld_base_universe_d2_043_pld_basefill_043, 43)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_043_pld_basefill_043'] = {'inputs': ['pld_base_universe_d2_043_pld_basefill_043'], 'func': pld_base_universe_d3_043_pld_basefill_043}


def pld_base_universe_d3_044_pld_basefill_044(pld_base_universe_d2_044_pld_basefill_044):
    return _base_universe_d3(pld_base_universe_d2_044_pld_basefill_044, 44)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_044_pld_basefill_044'] = {'inputs': ['pld_base_universe_d2_044_pld_basefill_044'], 'func': pld_base_universe_d3_044_pld_basefill_044}


def pld_base_universe_d3_045_pld_basefill_045(pld_base_universe_d2_045_pld_basefill_045):
    return _base_universe_d3(pld_base_universe_d2_045_pld_basefill_045, 45)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_045_pld_basefill_045'] = {'inputs': ['pld_base_universe_d2_045_pld_basefill_045'], 'func': pld_base_universe_d3_045_pld_basefill_045}


def pld_base_universe_d3_046_pld_basefill_046(pld_base_universe_d2_046_pld_basefill_046):
    return _base_universe_d3(pld_base_universe_d2_046_pld_basefill_046, 46)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_046_pld_basefill_046'] = {'inputs': ['pld_base_universe_d2_046_pld_basefill_046'], 'func': pld_base_universe_d3_046_pld_basefill_046}


def pld_base_universe_d3_047_pld_basefill_047(pld_base_universe_d2_047_pld_basefill_047):
    return _base_universe_d3(pld_base_universe_d2_047_pld_basefill_047, 47)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_047_pld_basefill_047'] = {'inputs': ['pld_base_universe_d2_047_pld_basefill_047'], 'func': pld_base_universe_d3_047_pld_basefill_047}


def pld_base_universe_d3_048_pld_basefill_048(pld_base_universe_d2_048_pld_basefill_048):
    return _base_universe_d3(pld_base_universe_d2_048_pld_basefill_048, 48)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_048_pld_basefill_048'] = {'inputs': ['pld_base_universe_d2_048_pld_basefill_048'], 'func': pld_base_universe_d3_048_pld_basefill_048}


def pld_base_universe_d3_049_pld_basefill_049(pld_base_universe_d2_049_pld_basefill_049):
    return _base_universe_d3(pld_base_universe_d2_049_pld_basefill_049, 49)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_049_pld_basefill_049'] = {'inputs': ['pld_base_universe_d2_049_pld_basefill_049'], 'func': pld_base_universe_d3_049_pld_basefill_049}


def pld_base_universe_d3_050_pld_basefill_050(pld_base_universe_d2_050_pld_basefill_050):
    return _base_universe_d3(pld_base_universe_d2_050_pld_basefill_050, 50)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_050_pld_basefill_050'] = {'inputs': ['pld_base_universe_d2_050_pld_basefill_050'], 'func': pld_base_universe_d3_050_pld_basefill_050}


def pld_base_universe_d3_051_pld_basefill_051(pld_base_universe_d2_051_pld_basefill_051):
    return _base_universe_d3(pld_base_universe_d2_051_pld_basefill_051, 51)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_051_pld_basefill_051'] = {'inputs': ['pld_base_universe_d2_051_pld_basefill_051'], 'func': pld_base_universe_d3_051_pld_basefill_051}


def pld_base_universe_d3_052_pld_basefill_052(pld_base_universe_d2_052_pld_basefill_052):
    return _base_universe_d3(pld_base_universe_d2_052_pld_basefill_052, 52)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_052_pld_basefill_052'] = {'inputs': ['pld_base_universe_d2_052_pld_basefill_052'], 'func': pld_base_universe_d3_052_pld_basefill_052}


def pld_base_universe_d3_053_pld_basefill_053(pld_base_universe_d2_053_pld_basefill_053):
    return _base_universe_d3(pld_base_universe_d2_053_pld_basefill_053, 53)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_053_pld_basefill_053'] = {'inputs': ['pld_base_universe_d2_053_pld_basefill_053'], 'func': pld_base_universe_d3_053_pld_basefill_053}


def pld_base_universe_d3_054_pld_basefill_054(pld_base_universe_d2_054_pld_basefill_054):
    return _base_universe_d3(pld_base_universe_d2_054_pld_basefill_054, 54)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_054_pld_basefill_054'] = {'inputs': ['pld_base_universe_d2_054_pld_basefill_054'], 'func': pld_base_universe_d3_054_pld_basefill_054}


def pld_base_universe_d3_055_pld_basefill_055(pld_base_universe_d2_055_pld_basefill_055):
    return _base_universe_d3(pld_base_universe_d2_055_pld_basefill_055, 55)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_055_pld_basefill_055'] = {'inputs': ['pld_base_universe_d2_055_pld_basefill_055'], 'func': pld_base_universe_d3_055_pld_basefill_055}


def pld_base_universe_d3_056_pld_basefill_056(pld_base_universe_d2_056_pld_basefill_056):
    return _base_universe_d3(pld_base_universe_d2_056_pld_basefill_056, 56)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_056_pld_basefill_056'] = {'inputs': ['pld_base_universe_d2_056_pld_basefill_056'], 'func': pld_base_universe_d3_056_pld_basefill_056}


def pld_base_universe_d3_057_pld_basefill_057(pld_base_universe_d2_057_pld_basefill_057):
    return _base_universe_d3(pld_base_universe_d2_057_pld_basefill_057, 57)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_057_pld_basefill_057'] = {'inputs': ['pld_base_universe_d2_057_pld_basefill_057'], 'func': pld_base_universe_d3_057_pld_basefill_057}


def pld_base_universe_d3_058_pld_basefill_058(pld_base_universe_d2_058_pld_basefill_058):
    return _base_universe_d3(pld_base_universe_d2_058_pld_basefill_058, 58)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_058_pld_basefill_058'] = {'inputs': ['pld_base_universe_d2_058_pld_basefill_058'], 'func': pld_base_universe_d3_058_pld_basefill_058}


def pld_base_universe_d3_059_pld_basefill_059(pld_base_universe_d2_059_pld_basefill_059):
    return _base_universe_d3(pld_base_universe_d2_059_pld_basefill_059, 59)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_059_pld_basefill_059'] = {'inputs': ['pld_base_universe_d2_059_pld_basefill_059'], 'func': pld_base_universe_d3_059_pld_basefill_059}


def pld_base_universe_d3_060_pld_basefill_060(pld_base_universe_d2_060_pld_basefill_060):
    return _base_universe_d3(pld_base_universe_d2_060_pld_basefill_060, 60)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_060_pld_basefill_060'] = {'inputs': ['pld_base_universe_d2_060_pld_basefill_060'], 'func': pld_base_universe_d3_060_pld_basefill_060}


def pld_base_universe_d3_061_pld_basefill_061(pld_base_universe_d2_061_pld_basefill_061):
    return _base_universe_d3(pld_base_universe_d2_061_pld_basefill_061, 61)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_061_pld_basefill_061'] = {'inputs': ['pld_base_universe_d2_061_pld_basefill_061'], 'func': pld_base_universe_d3_061_pld_basefill_061}


def pld_base_universe_d3_062_pld_basefill_062(pld_base_universe_d2_062_pld_basefill_062):
    return _base_universe_d3(pld_base_universe_d2_062_pld_basefill_062, 62)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_062_pld_basefill_062'] = {'inputs': ['pld_base_universe_d2_062_pld_basefill_062'], 'func': pld_base_universe_d3_062_pld_basefill_062}


def pld_base_universe_d3_063_pld_basefill_063(pld_base_universe_d2_063_pld_basefill_063):
    return _base_universe_d3(pld_base_universe_d2_063_pld_basefill_063, 63)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_063_pld_basefill_063'] = {'inputs': ['pld_base_universe_d2_063_pld_basefill_063'], 'func': pld_base_universe_d3_063_pld_basefill_063}


def pld_base_universe_d3_064_pld_basefill_064(pld_base_universe_d2_064_pld_basefill_064):
    return _base_universe_d3(pld_base_universe_d2_064_pld_basefill_064, 64)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_064_pld_basefill_064'] = {'inputs': ['pld_base_universe_d2_064_pld_basefill_064'], 'func': pld_base_universe_d3_064_pld_basefill_064}


def pld_base_universe_d3_065_pld_basefill_065(pld_base_universe_d2_065_pld_basefill_065):
    return _base_universe_d3(pld_base_universe_d2_065_pld_basefill_065, 65)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_065_pld_basefill_065'] = {'inputs': ['pld_base_universe_d2_065_pld_basefill_065'], 'func': pld_base_universe_d3_065_pld_basefill_065}


def pld_base_universe_d3_066_pld_basefill_066(pld_base_universe_d2_066_pld_basefill_066):
    return _base_universe_d3(pld_base_universe_d2_066_pld_basefill_066, 66)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_066_pld_basefill_066'] = {'inputs': ['pld_base_universe_d2_066_pld_basefill_066'], 'func': pld_base_universe_d3_066_pld_basefill_066}


def pld_base_universe_d3_067_pld_basefill_067(pld_base_universe_d2_067_pld_basefill_067):
    return _base_universe_d3(pld_base_universe_d2_067_pld_basefill_067, 67)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_067_pld_basefill_067'] = {'inputs': ['pld_base_universe_d2_067_pld_basefill_067'], 'func': pld_base_universe_d3_067_pld_basefill_067}


def pld_base_universe_d3_068_pld_basefill_068(pld_base_universe_d2_068_pld_basefill_068):
    return _base_universe_d3(pld_base_universe_d2_068_pld_basefill_068, 68)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_068_pld_basefill_068'] = {'inputs': ['pld_base_universe_d2_068_pld_basefill_068'], 'func': pld_base_universe_d3_068_pld_basefill_068}


def pld_base_universe_d3_069_pld_basefill_069(pld_base_universe_d2_069_pld_basefill_069):
    return _base_universe_d3(pld_base_universe_d2_069_pld_basefill_069, 69)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_069_pld_basefill_069'] = {'inputs': ['pld_base_universe_d2_069_pld_basefill_069'], 'func': pld_base_universe_d3_069_pld_basefill_069}


def pld_base_universe_d3_070_pld_basefill_070(pld_base_universe_d2_070_pld_basefill_070):
    return _base_universe_d3(pld_base_universe_d2_070_pld_basefill_070, 70)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_070_pld_basefill_070'] = {'inputs': ['pld_base_universe_d2_070_pld_basefill_070'], 'func': pld_base_universe_d3_070_pld_basefill_070}


def pld_base_universe_d3_071_pld_basefill_071(pld_base_universe_d2_071_pld_basefill_071):
    return _base_universe_d3(pld_base_universe_d2_071_pld_basefill_071, 71)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_071_pld_basefill_071'] = {'inputs': ['pld_base_universe_d2_071_pld_basefill_071'], 'func': pld_base_universe_d3_071_pld_basefill_071}


def pld_base_universe_d3_072_pld_basefill_072(pld_base_universe_d2_072_pld_basefill_072):
    return _base_universe_d3(pld_base_universe_d2_072_pld_basefill_072, 72)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_072_pld_basefill_072'] = {'inputs': ['pld_base_universe_d2_072_pld_basefill_072'], 'func': pld_base_universe_d3_072_pld_basefill_072}


def pld_base_universe_d3_073_pld_basefill_073(pld_base_universe_d2_073_pld_basefill_073):
    return _base_universe_d3(pld_base_universe_d2_073_pld_basefill_073, 73)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_073_pld_basefill_073'] = {'inputs': ['pld_base_universe_d2_073_pld_basefill_073'], 'func': pld_base_universe_d3_073_pld_basefill_073}


def pld_base_universe_d3_074_pld_basefill_074(pld_base_universe_d2_074_pld_basefill_074):
    return _base_universe_d3(pld_base_universe_d2_074_pld_basefill_074, 74)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_074_pld_basefill_074'] = {'inputs': ['pld_base_universe_d2_074_pld_basefill_074'], 'func': pld_base_universe_d3_074_pld_basefill_074}


def pld_base_universe_d3_075_pld_basefill_075(pld_base_universe_d2_075_pld_basefill_075):
    return _base_universe_d3(pld_base_universe_d2_075_pld_basefill_075, 75)
PLD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pld_base_universe_d3_075_pld_basefill_075'] = {'inputs': ['pld_base_universe_d2_075_pld_basefill_075'], 'func': pld_base_universe_d3_075_pld_basefill_075}
