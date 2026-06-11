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



def tcl_001_amihud_illiquidity_accel_1(tcl_001_amihud_illiquidity_roc_1):
    feature = _s(tcl_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def tcl_007_amihud_illiquidity_accel_5(tcl_007_amihud_illiquidity_roc_5):
    feature = _s(tcl_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def tcl_013_amihud_illiquidity_accel_42(tcl_013_amihud_illiquidity_roc_42):
    feature = _s(tcl_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def tcl_179_tcl_019_amihud_illiquidity_42_019_accel_126(tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def tcl_180_tcl_025_amihud_illiquidity_378_025_accel_378(tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















TROUGH_CLUSTERING_REGISTRY_3RD_DERIVATIVES = {
    'tcl_001_amihud_illiquidity_accel_1': {'inputs': ['tcl_001_amihud_illiquidity_roc_1'], 'func': tcl_001_amihud_illiquidity_accel_1},
    'tcl_007_amihud_illiquidity_accel_5': {'inputs': ['tcl_007_amihud_illiquidity_roc_5'], 'func': tcl_007_amihud_illiquidity_accel_5},
    'tcl_013_amihud_illiquidity_accel_42': {'inputs': ['tcl_013_amihud_illiquidity_roc_42'], 'func': tcl_013_amihud_illiquidity_accel_42},
    'tcl_179_tcl_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126'], 'func': tcl_179_tcl_019_amihud_illiquidity_42_019_accel_126},
    'tcl_180_tcl_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378'], 'func': tcl_180_tcl_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def tc_replacement_d3_001(tc_replacement_d2_001):
    feature = _clean(tc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_001'] = {'inputs': ['tc_replacement_d2_001'], 'func': tc_replacement_d3_001}


def tc_replacement_d3_002(tc_replacement_d2_002):
    feature = _clean(tc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_002'] = {'inputs': ['tc_replacement_d2_002'], 'func': tc_replacement_d3_002}


def tc_replacement_d3_003(tc_replacement_d2_003):
    feature = _clean(tc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_003'] = {'inputs': ['tc_replacement_d2_003'], 'func': tc_replacement_d3_003}


def tc_replacement_d3_004(tc_replacement_d2_004):
    feature = _clean(tc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_004'] = {'inputs': ['tc_replacement_d2_004'], 'func': tc_replacement_d3_004}


def tc_replacement_d3_005(tc_replacement_d2_005):
    feature = _clean(tc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_005'] = {'inputs': ['tc_replacement_d2_005'], 'func': tc_replacement_d3_005}


def tc_replacement_d3_006(tc_replacement_d2_006):
    feature = _clean(tc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_006'] = {'inputs': ['tc_replacement_d2_006'], 'func': tc_replacement_d3_006}


def tc_replacement_d3_007(tc_replacement_d2_007):
    feature = _clean(tc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_007'] = {'inputs': ['tc_replacement_d2_007'], 'func': tc_replacement_d3_007}


def tc_replacement_d3_008(tc_replacement_d2_008):
    feature = _clean(tc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_008'] = {'inputs': ['tc_replacement_d2_008'], 'func': tc_replacement_d3_008}


def tc_replacement_d3_009(tc_replacement_d2_009):
    feature = _clean(tc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_009'] = {'inputs': ['tc_replacement_d2_009'], 'func': tc_replacement_d3_009}


def tc_replacement_d3_010(tc_replacement_d2_010):
    feature = _clean(tc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_010'] = {'inputs': ['tc_replacement_d2_010'], 'func': tc_replacement_d3_010}


def tc_replacement_d3_011(tc_replacement_d2_011):
    feature = _clean(tc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_011'] = {'inputs': ['tc_replacement_d2_011'], 'func': tc_replacement_d3_011}


def tc_replacement_d3_012(tc_replacement_d2_012):
    feature = _clean(tc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_012'] = {'inputs': ['tc_replacement_d2_012'], 'func': tc_replacement_d3_012}


def tc_replacement_d3_013(tc_replacement_d2_013):
    feature = _clean(tc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_013'] = {'inputs': ['tc_replacement_d2_013'], 'func': tc_replacement_d3_013}


def tc_replacement_d3_014(tc_replacement_d2_014):
    feature = _clean(tc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_014'] = {'inputs': ['tc_replacement_d2_014'], 'func': tc_replacement_d3_014}


def tc_replacement_d3_015(tc_replacement_d2_015):
    feature = _clean(tc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_015'] = {'inputs': ['tc_replacement_d2_015'], 'func': tc_replacement_d3_015}


def tc_replacement_d3_016(tc_replacement_d2_016):
    feature = _clean(tc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_016'] = {'inputs': ['tc_replacement_d2_016'], 'func': tc_replacement_d3_016}


def tc_replacement_d3_017(tc_replacement_d2_017):
    feature = _clean(tc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_017'] = {'inputs': ['tc_replacement_d2_017'], 'func': tc_replacement_d3_017}


def tc_replacement_d3_018(tc_replacement_d2_018):
    feature = _clean(tc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_018'] = {'inputs': ['tc_replacement_d2_018'], 'func': tc_replacement_d3_018}


def tc_replacement_d3_019(tc_replacement_d2_019):
    feature = _clean(tc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_019'] = {'inputs': ['tc_replacement_d2_019'], 'func': tc_replacement_d3_019}


def tc_replacement_d3_020(tc_replacement_d2_020):
    feature = _clean(tc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_020'] = {'inputs': ['tc_replacement_d2_020'], 'func': tc_replacement_d3_020}


def tc_replacement_d3_021(tc_replacement_d2_021):
    feature = _clean(tc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_021'] = {'inputs': ['tc_replacement_d2_021'], 'func': tc_replacement_d3_021}


def tc_replacement_d3_022(tc_replacement_d2_022):
    feature = _clean(tc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_022'] = {'inputs': ['tc_replacement_d2_022'], 'func': tc_replacement_d3_022}


def tc_replacement_d3_023(tc_replacement_d2_023):
    feature = _clean(tc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_023'] = {'inputs': ['tc_replacement_d2_023'], 'func': tc_replacement_d3_023}


def tc_replacement_d3_024(tc_replacement_d2_024):
    feature = _clean(tc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_024'] = {'inputs': ['tc_replacement_d2_024'], 'func': tc_replacement_d3_024}


def tc_replacement_d3_025(tc_replacement_d2_025):
    feature = _clean(tc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_025'] = {'inputs': ['tc_replacement_d2_025'], 'func': tc_replacement_d3_025}


def tc_replacement_d3_026(tc_replacement_d2_026):
    feature = _clean(tc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_026'] = {'inputs': ['tc_replacement_d2_026'], 'func': tc_replacement_d3_026}


def tc_replacement_d3_027(tc_replacement_d2_027):
    feature = _clean(tc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_027'] = {'inputs': ['tc_replacement_d2_027'], 'func': tc_replacement_d3_027}


def tc_replacement_d3_028(tc_replacement_d2_028):
    feature = _clean(tc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_028'] = {'inputs': ['tc_replacement_d2_028'], 'func': tc_replacement_d3_028}


def tc_replacement_d3_029(tc_replacement_d2_029):
    feature = _clean(tc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_029'] = {'inputs': ['tc_replacement_d2_029'], 'func': tc_replacement_d3_029}


def tc_replacement_d3_030(tc_replacement_d2_030):
    feature = _clean(tc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_030'] = {'inputs': ['tc_replacement_d2_030'], 'func': tc_replacement_d3_030}


def tc_replacement_d3_031(tc_replacement_d2_031):
    feature = _clean(tc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_031'] = {'inputs': ['tc_replacement_d2_031'], 'func': tc_replacement_d3_031}


def tc_replacement_d3_032(tc_replacement_d2_032):
    feature = _clean(tc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_032'] = {'inputs': ['tc_replacement_d2_032'], 'func': tc_replacement_d3_032}


def tc_replacement_d3_033(tc_replacement_d2_033):
    feature = _clean(tc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_033'] = {'inputs': ['tc_replacement_d2_033'], 'func': tc_replacement_d3_033}


def tc_replacement_d3_034(tc_replacement_d2_034):
    feature = _clean(tc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_034'] = {'inputs': ['tc_replacement_d2_034'], 'func': tc_replacement_d3_034}


def tc_replacement_d3_035(tc_replacement_d2_035):
    feature = _clean(tc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_035'] = {'inputs': ['tc_replacement_d2_035'], 'func': tc_replacement_d3_035}


def tc_replacement_d3_036(tc_replacement_d2_036):
    feature = _clean(tc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_036'] = {'inputs': ['tc_replacement_d2_036'], 'func': tc_replacement_d3_036}


def tc_replacement_d3_037(tc_replacement_d2_037):
    feature = _clean(tc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_037'] = {'inputs': ['tc_replacement_d2_037'], 'func': tc_replacement_d3_037}


def tc_replacement_d3_038(tc_replacement_d2_038):
    feature = _clean(tc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_038'] = {'inputs': ['tc_replacement_d2_038'], 'func': tc_replacement_d3_038}


def tc_replacement_d3_039(tc_replacement_d2_039):
    feature = _clean(tc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_039'] = {'inputs': ['tc_replacement_d2_039'], 'func': tc_replacement_d3_039}


def tc_replacement_d3_040(tc_replacement_d2_040):
    feature = _clean(tc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_040'] = {'inputs': ['tc_replacement_d2_040'], 'func': tc_replacement_d3_040}


def tc_replacement_d3_041(tc_replacement_d2_041):
    feature = _clean(tc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_041'] = {'inputs': ['tc_replacement_d2_041'], 'func': tc_replacement_d3_041}


def tc_replacement_d3_042(tc_replacement_d2_042):
    feature = _clean(tc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_042'] = {'inputs': ['tc_replacement_d2_042'], 'func': tc_replacement_d3_042}


def tc_replacement_d3_043(tc_replacement_d2_043):
    feature = _clean(tc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_043'] = {'inputs': ['tc_replacement_d2_043'], 'func': tc_replacement_d3_043}


def tc_replacement_d3_044(tc_replacement_d2_044):
    feature = _clean(tc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_044'] = {'inputs': ['tc_replacement_d2_044'], 'func': tc_replacement_d3_044}


def tc_replacement_d3_045(tc_replacement_d2_045):
    feature = _clean(tc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_045'] = {'inputs': ['tc_replacement_d2_045'], 'func': tc_replacement_d3_045}


def tc_replacement_d3_046(tc_replacement_d2_046):
    feature = _clean(tc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_046'] = {'inputs': ['tc_replacement_d2_046'], 'func': tc_replacement_d3_046}


def tc_replacement_d3_047(tc_replacement_d2_047):
    feature = _clean(tc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_047'] = {'inputs': ['tc_replacement_d2_047'], 'func': tc_replacement_d3_047}


def tc_replacement_d3_048(tc_replacement_d2_048):
    feature = _clean(tc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_048'] = {'inputs': ['tc_replacement_d2_048'], 'func': tc_replacement_d3_048}


def tc_replacement_d3_049(tc_replacement_d2_049):
    feature = _clean(tc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_049'] = {'inputs': ['tc_replacement_d2_049'], 'func': tc_replacement_d3_049}


def tc_replacement_d3_050(tc_replacement_d2_050):
    feature = _clean(tc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_050'] = {'inputs': ['tc_replacement_d2_050'], 'func': tc_replacement_d3_050}


def tc_replacement_d3_051(tc_replacement_d2_051):
    feature = _clean(tc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_051'] = {'inputs': ['tc_replacement_d2_051'], 'func': tc_replacement_d3_051}


def tc_replacement_d3_052(tc_replacement_d2_052):
    feature = _clean(tc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_052'] = {'inputs': ['tc_replacement_d2_052'], 'func': tc_replacement_d3_052}


def tc_replacement_d3_053(tc_replacement_d2_053):
    feature = _clean(tc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_053'] = {'inputs': ['tc_replacement_d2_053'], 'func': tc_replacement_d3_053}


def tc_replacement_d3_054(tc_replacement_d2_054):
    feature = _clean(tc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_054'] = {'inputs': ['tc_replacement_d2_054'], 'func': tc_replacement_d3_054}


def tc_replacement_d3_055(tc_replacement_d2_055):
    feature = _clean(tc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_055'] = {'inputs': ['tc_replacement_d2_055'], 'func': tc_replacement_d3_055}


def tc_replacement_d3_056(tc_replacement_d2_056):
    feature = _clean(tc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_056'] = {'inputs': ['tc_replacement_d2_056'], 'func': tc_replacement_d3_056}


def tc_replacement_d3_057(tc_replacement_d2_057):
    feature = _clean(tc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_057'] = {'inputs': ['tc_replacement_d2_057'], 'func': tc_replacement_d3_057}


def tc_replacement_d3_058(tc_replacement_d2_058):
    feature = _clean(tc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_058'] = {'inputs': ['tc_replacement_d2_058'], 'func': tc_replacement_d3_058}


def tc_replacement_d3_059(tc_replacement_d2_059):
    feature = _clean(tc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_059'] = {'inputs': ['tc_replacement_d2_059'], 'func': tc_replacement_d3_059}


def tc_replacement_d3_060(tc_replacement_d2_060):
    feature = _clean(tc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_060'] = {'inputs': ['tc_replacement_d2_060'], 'func': tc_replacement_d3_060}


def tc_replacement_d3_061(tc_replacement_d2_061):
    feature = _clean(tc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_061'] = {'inputs': ['tc_replacement_d2_061'], 'func': tc_replacement_d3_061}


def tc_replacement_d3_062(tc_replacement_d2_062):
    feature = _clean(tc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_062'] = {'inputs': ['tc_replacement_d2_062'], 'func': tc_replacement_d3_062}


def tc_replacement_d3_063(tc_replacement_d2_063):
    feature = _clean(tc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_063'] = {'inputs': ['tc_replacement_d2_063'], 'func': tc_replacement_d3_063}


def tc_replacement_d3_064(tc_replacement_d2_064):
    feature = _clean(tc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_064'] = {'inputs': ['tc_replacement_d2_064'], 'func': tc_replacement_d3_064}


def tc_replacement_d3_065(tc_replacement_d2_065):
    feature = _clean(tc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_065'] = {'inputs': ['tc_replacement_d2_065'], 'func': tc_replacement_d3_065}


def tc_replacement_d3_066(tc_replacement_d2_066):
    feature = _clean(tc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_066'] = {'inputs': ['tc_replacement_d2_066'], 'func': tc_replacement_d3_066}


def tc_replacement_d3_067(tc_replacement_d2_067):
    feature = _clean(tc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_067'] = {'inputs': ['tc_replacement_d2_067'], 'func': tc_replacement_d3_067}


def tc_replacement_d3_068(tc_replacement_d2_068):
    feature = _clean(tc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_068'] = {'inputs': ['tc_replacement_d2_068'], 'func': tc_replacement_d3_068}


def tc_replacement_d3_069(tc_replacement_d2_069):
    feature = _clean(tc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_069'] = {'inputs': ['tc_replacement_d2_069'], 'func': tc_replacement_d3_069}


def tc_replacement_d3_070(tc_replacement_d2_070):
    feature = _clean(tc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_070'] = {'inputs': ['tc_replacement_d2_070'], 'func': tc_replacement_d3_070}


def tc_replacement_d3_071(tc_replacement_d2_071):
    feature = _clean(tc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_071'] = {'inputs': ['tc_replacement_d2_071'], 'func': tc_replacement_d3_071}


def tc_replacement_d3_072(tc_replacement_d2_072):
    feature = _clean(tc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_072'] = {'inputs': ['tc_replacement_d2_072'], 'func': tc_replacement_d3_072}


def tc_replacement_d3_073(tc_replacement_d2_073):
    feature = _clean(tc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_073'] = {'inputs': ['tc_replacement_d2_073'], 'func': tc_replacement_d3_073}


def tc_replacement_d3_074(tc_replacement_d2_074):
    feature = _clean(tc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_074'] = {'inputs': ['tc_replacement_d2_074'], 'func': tc_replacement_d3_074}


def tc_replacement_d3_075(tc_replacement_d2_075):
    feature = _clean(tc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_075'] = {'inputs': ['tc_replacement_d2_075'], 'func': tc_replacement_d3_075}


def tc_replacement_d3_076(tc_replacement_d2_076):
    feature = _clean(tc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_076'] = {'inputs': ['tc_replacement_d2_076'], 'func': tc_replacement_d3_076}


def tc_replacement_d3_077(tc_replacement_d2_077):
    feature = _clean(tc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_077'] = {'inputs': ['tc_replacement_d2_077'], 'func': tc_replacement_d3_077}


def tc_replacement_d3_078(tc_replacement_d2_078):
    feature = _clean(tc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_078'] = {'inputs': ['tc_replacement_d2_078'], 'func': tc_replacement_d3_078}


def tc_replacement_d3_079(tc_replacement_d2_079):
    feature = _clean(tc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_079'] = {'inputs': ['tc_replacement_d2_079'], 'func': tc_replacement_d3_079}


def tc_replacement_d3_080(tc_replacement_d2_080):
    feature = _clean(tc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_080'] = {'inputs': ['tc_replacement_d2_080'], 'func': tc_replacement_d3_080}


def tc_replacement_d3_081(tc_replacement_d2_081):
    feature = _clean(tc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_081'] = {'inputs': ['tc_replacement_d2_081'], 'func': tc_replacement_d3_081}


def tc_replacement_d3_082(tc_replacement_d2_082):
    feature = _clean(tc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_082'] = {'inputs': ['tc_replacement_d2_082'], 'func': tc_replacement_d3_082}


def tc_replacement_d3_083(tc_replacement_d2_083):
    feature = _clean(tc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_083'] = {'inputs': ['tc_replacement_d2_083'], 'func': tc_replacement_d3_083}


def tc_replacement_d3_084(tc_replacement_d2_084):
    feature = _clean(tc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_084'] = {'inputs': ['tc_replacement_d2_084'], 'func': tc_replacement_d3_084}


def tc_replacement_d3_085(tc_replacement_d2_085):
    feature = _clean(tc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_085'] = {'inputs': ['tc_replacement_d2_085'], 'func': tc_replacement_d3_085}


def tc_replacement_d3_086(tc_replacement_d2_086):
    feature = _clean(tc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_086'] = {'inputs': ['tc_replacement_d2_086'], 'func': tc_replacement_d3_086}


def tc_replacement_d3_087(tc_replacement_d2_087):
    feature = _clean(tc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_087'] = {'inputs': ['tc_replacement_d2_087'], 'func': tc_replacement_d3_087}


def tc_replacement_d3_088(tc_replacement_d2_088):
    feature = _clean(tc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_088'] = {'inputs': ['tc_replacement_d2_088'], 'func': tc_replacement_d3_088}


def tc_replacement_d3_089(tc_replacement_d2_089):
    feature = _clean(tc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_089'] = {'inputs': ['tc_replacement_d2_089'], 'func': tc_replacement_d3_089}


def tc_replacement_d3_090(tc_replacement_d2_090):
    feature = _clean(tc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_090'] = {'inputs': ['tc_replacement_d2_090'], 'func': tc_replacement_d3_090}


def tc_replacement_d3_091(tc_replacement_d2_091):
    feature = _clean(tc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_091'] = {'inputs': ['tc_replacement_d2_091'], 'func': tc_replacement_d3_091}


def tc_replacement_d3_092(tc_replacement_d2_092):
    feature = _clean(tc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_092'] = {'inputs': ['tc_replacement_d2_092'], 'func': tc_replacement_d3_092}


def tc_replacement_d3_093(tc_replacement_d2_093):
    feature = _clean(tc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_093'] = {'inputs': ['tc_replacement_d2_093'], 'func': tc_replacement_d3_093}


def tc_replacement_d3_094(tc_replacement_d2_094):
    feature = _clean(tc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_094'] = {'inputs': ['tc_replacement_d2_094'], 'func': tc_replacement_d3_094}


def tc_replacement_d3_095(tc_replacement_d2_095):
    feature = _clean(tc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_095'] = {'inputs': ['tc_replacement_d2_095'], 'func': tc_replacement_d3_095}


def tc_replacement_d3_096(tc_replacement_d2_096):
    feature = _clean(tc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_096'] = {'inputs': ['tc_replacement_d2_096'], 'func': tc_replacement_d3_096}


def tc_replacement_d3_097(tc_replacement_d2_097):
    feature = _clean(tc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_097'] = {'inputs': ['tc_replacement_d2_097'], 'func': tc_replacement_d3_097}


def tc_replacement_d3_098(tc_replacement_d2_098):
    feature = _clean(tc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_098'] = {'inputs': ['tc_replacement_d2_098'], 'func': tc_replacement_d3_098}


def tc_replacement_d3_099(tc_replacement_d2_099):
    feature = _clean(tc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_099'] = {'inputs': ['tc_replacement_d2_099'], 'func': tc_replacement_d3_099}


def tc_replacement_d3_100(tc_replacement_d2_100):
    feature = _clean(tc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_100'] = {'inputs': ['tc_replacement_d2_100'], 'func': tc_replacement_d3_100}


def tc_replacement_d3_101(tc_replacement_d2_101):
    feature = _clean(tc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_101'] = {'inputs': ['tc_replacement_d2_101'], 'func': tc_replacement_d3_101}


def tc_replacement_d3_102(tc_replacement_d2_102):
    feature = _clean(tc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_102'] = {'inputs': ['tc_replacement_d2_102'], 'func': tc_replacement_d3_102}


def tc_replacement_d3_103(tc_replacement_d2_103):
    feature = _clean(tc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_103'] = {'inputs': ['tc_replacement_d2_103'], 'func': tc_replacement_d3_103}


def tc_replacement_d3_104(tc_replacement_d2_104):
    feature = _clean(tc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_104'] = {'inputs': ['tc_replacement_d2_104'], 'func': tc_replacement_d3_104}


def tc_replacement_d3_105(tc_replacement_d2_105):
    feature = _clean(tc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_105'] = {'inputs': ['tc_replacement_d2_105'], 'func': tc_replacement_d3_105}


def tc_replacement_d3_106(tc_replacement_d2_106):
    feature = _clean(tc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_106'] = {'inputs': ['tc_replacement_d2_106'], 'func': tc_replacement_d3_106}


def tc_replacement_d3_107(tc_replacement_d2_107):
    feature = _clean(tc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_107'] = {'inputs': ['tc_replacement_d2_107'], 'func': tc_replacement_d3_107}


def tc_replacement_d3_108(tc_replacement_d2_108):
    feature = _clean(tc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_108'] = {'inputs': ['tc_replacement_d2_108'], 'func': tc_replacement_d3_108}


def tc_replacement_d3_109(tc_replacement_d2_109):
    feature = _clean(tc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_109'] = {'inputs': ['tc_replacement_d2_109'], 'func': tc_replacement_d3_109}


def tc_replacement_d3_110(tc_replacement_d2_110):
    feature = _clean(tc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_110'] = {'inputs': ['tc_replacement_d2_110'], 'func': tc_replacement_d3_110}


def tc_replacement_d3_111(tc_replacement_d2_111):
    feature = _clean(tc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_111'] = {'inputs': ['tc_replacement_d2_111'], 'func': tc_replacement_d3_111}


def tc_replacement_d3_112(tc_replacement_d2_112):
    feature = _clean(tc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_112'] = {'inputs': ['tc_replacement_d2_112'], 'func': tc_replacement_d3_112}


def tc_replacement_d3_113(tc_replacement_d2_113):
    feature = _clean(tc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_113'] = {'inputs': ['tc_replacement_d2_113'], 'func': tc_replacement_d3_113}


def tc_replacement_d3_114(tc_replacement_d2_114):
    feature = _clean(tc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_114'] = {'inputs': ['tc_replacement_d2_114'], 'func': tc_replacement_d3_114}


def tc_replacement_d3_115(tc_replacement_d2_115):
    feature = _clean(tc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_115'] = {'inputs': ['tc_replacement_d2_115'], 'func': tc_replacement_d3_115}


def tc_replacement_d3_116(tc_replacement_d2_116):
    feature = _clean(tc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_116'] = {'inputs': ['tc_replacement_d2_116'], 'func': tc_replacement_d3_116}


def tc_replacement_d3_117(tc_replacement_d2_117):
    feature = _clean(tc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_117'] = {'inputs': ['tc_replacement_d2_117'], 'func': tc_replacement_d3_117}


def tc_replacement_d3_118(tc_replacement_d2_118):
    feature = _clean(tc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_118'] = {'inputs': ['tc_replacement_d2_118'], 'func': tc_replacement_d3_118}


def tc_replacement_d3_119(tc_replacement_d2_119):
    feature = _clean(tc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_119'] = {'inputs': ['tc_replacement_d2_119'], 'func': tc_replacement_d3_119}


def tc_replacement_d3_120(tc_replacement_d2_120):
    feature = _clean(tc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_120'] = {'inputs': ['tc_replacement_d2_120'], 'func': tc_replacement_d3_120}


def tc_replacement_d3_121(tc_replacement_d2_121):
    feature = _clean(tc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_121'] = {'inputs': ['tc_replacement_d2_121'], 'func': tc_replacement_d3_121}


def tc_replacement_d3_122(tc_replacement_d2_122):
    feature = _clean(tc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_122'] = {'inputs': ['tc_replacement_d2_122'], 'func': tc_replacement_d3_122}


def tc_replacement_d3_123(tc_replacement_d2_123):
    feature = _clean(tc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_123'] = {'inputs': ['tc_replacement_d2_123'], 'func': tc_replacement_d3_123}


def tc_replacement_d3_124(tc_replacement_d2_124):
    feature = _clean(tc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_124'] = {'inputs': ['tc_replacement_d2_124'], 'func': tc_replacement_d3_124}


def tc_replacement_d3_125(tc_replacement_d2_125):
    feature = _clean(tc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_125'] = {'inputs': ['tc_replacement_d2_125'], 'func': tc_replacement_d3_125}


def tc_replacement_d3_126(tc_replacement_d2_126):
    feature = _clean(tc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_126'] = {'inputs': ['tc_replacement_d2_126'], 'func': tc_replacement_d3_126}


def tc_replacement_d3_127(tc_replacement_d2_127):
    feature = _clean(tc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_127'] = {'inputs': ['tc_replacement_d2_127'], 'func': tc_replacement_d3_127}


def tc_replacement_d3_128(tc_replacement_d2_128):
    feature = _clean(tc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_128'] = {'inputs': ['tc_replacement_d2_128'], 'func': tc_replacement_d3_128}


def tc_replacement_d3_129(tc_replacement_d2_129):
    feature = _clean(tc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_129'] = {'inputs': ['tc_replacement_d2_129'], 'func': tc_replacement_d3_129}


def tc_replacement_d3_130(tc_replacement_d2_130):
    feature = _clean(tc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_130'] = {'inputs': ['tc_replacement_d2_130'], 'func': tc_replacement_d3_130}


def tc_replacement_d3_131(tc_replacement_d2_131):
    feature = _clean(tc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_131'] = {'inputs': ['tc_replacement_d2_131'], 'func': tc_replacement_d3_131}


def tc_replacement_d3_132(tc_replacement_d2_132):
    feature = _clean(tc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_132'] = {'inputs': ['tc_replacement_d2_132'], 'func': tc_replacement_d3_132}


def tc_replacement_d3_133(tc_replacement_d2_133):
    feature = _clean(tc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_133'] = {'inputs': ['tc_replacement_d2_133'], 'func': tc_replacement_d3_133}


def tc_replacement_d3_134(tc_replacement_d2_134):
    feature = _clean(tc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_134'] = {'inputs': ['tc_replacement_d2_134'], 'func': tc_replacement_d3_134}


def tc_replacement_d3_135(tc_replacement_d2_135):
    feature = _clean(tc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_135'] = {'inputs': ['tc_replacement_d2_135'], 'func': tc_replacement_d3_135}


def tc_replacement_d3_136(tc_replacement_d2_136):
    feature = _clean(tc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_136'] = {'inputs': ['tc_replacement_d2_136'], 'func': tc_replacement_d3_136}


def tc_replacement_d3_137(tc_replacement_d2_137):
    feature = _clean(tc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_137'] = {'inputs': ['tc_replacement_d2_137'], 'func': tc_replacement_d3_137}


def tc_replacement_d3_138(tc_replacement_d2_138):
    feature = _clean(tc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_138'] = {'inputs': ['tc_replacement_d2_138'], 'func': tc_replacement_d3_138}


def tc_replacement_d3_139(tc_replacement_d2_139):
    feature = _clean(tc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_139'] = {'inputs': ['tc_replacement_d2_139'], 'func': tc_replacement_d3_139}


def tc_replacement_d3_140(tc_replacement_d2_140):
    feature = _clean(tc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_140'] = {'inputs': ['tc_replacement_d2_140'], 'func': tc_replacement_d3_140}


def tc_replacement_d3_141(tc_replacement_d2_141):
    feature = _clean(tc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_141'] = {'inputs': ['tc_replacement_d2_141'], 'func': tc_replacement_d3_141}


def tc_replacement_d3_142(tc_replacement_d2_142):
    feature = _clean(tc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_142'] = {'inputs': ['tc_replacement_d2_142'], 'func': tc_replacement_d3_142}


def tc_replacement_d3_143(tc_replacement_d2_143):
    feature = _clean(tc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_143'] = {'inputs': ['tc_replacement_d2_143'], 'func': tc_replacement_d3_143}


def tc_replacement_d3_144(tc_replacement_d2_144):
    feature = _clean(tc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_144'] = {'inputs': ['tc_replacement_d2_144'], 'func': tc_replacement_d3_144}


def tc_replacement_d3_145(tc_replacement_d2_145):
    feature = _clean(tc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_145'] = {'inputs': ['tc_replacement_d2_145'], 'func': tc_replacement_d3_145}


def tc_replacement_d3_146(tc_replacement_d2_146):
    feature = _clean(tc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_146'] = {'inputs': ['tc_replacement_d2_146'], 'func': tc_replacement_d3_146}


def tc_replacement_d3_147(tc_replacement_d2_147):
    feature = _clean(tc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_147'] = {'inputs': ['tc_replacement_d2_147'], 'func': tc_replacement_d3_147}


def tc_replacement_d3_148(tc_replacement_d2_148):
    feature = _clean(tc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_148'] = {'inputs': ['tc_replacement_d2_148'], 'func': tc_replacement_d3_148}


def tc_replacement_d3_149(tc_replacement_d2_149):
    feature = _clean(tc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_149'] = {'inputs': ['tc_replacement_d2_149'], 'func': tc_replacement_d3_149}


def tc_replacement_d3_150(tc_replacement_d2_150):
    feature = _clean(tc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_150'] = {'inputs': ['tc_replacement_d2_150'], 'func': tc_replacement_d3_150}


def tc_replacement_d3_151(tc_replacement_d2_151):
    feature = _clean(tc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_151'] = {'inputs': ['tc_replacement_d2_151'], 'func': tc_replacement_d3_151}


def tc_replacement_d3_152(tc_replacement_d2_152):
    feature = _clean(tc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_152'] = {'inputs': ['tc_replacement_d2_152'], 'func': tc_replacement_d3_152}


def tc_replacement_d3_153(tc_replacement_d2_153):
    feature = _clean(tc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_153'] = {'inputs': ['tc_replacement_d2_153'], 'func': tc_replacement_d3_153}


def tc_replacement_d3_154(tc_replacement_d2_154):
    feature = _clean(tc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_154'] = {'inputs': ['tc_replacement_d2_154'], 'func': tc_replacement_d3_154}


def tc_replacement_d3_155(tc_replacement_d2_155):
    feature = _clean(tc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_155'] = {'inputs': ['tc_replacement_d2_155'], 'func': tc_replacement_d3_155}


def tc_replacement_d3_156(tc_replacement_d2_156):
    feature = _clean(tc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_156'] = {'inputs': ['tc_replacement_d2_156'], 'func': tc_replacement_d3_156}


def tc_replacement_d3_157(tc_replacement_d2_157):
    feature = _clean(tc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_157'] = {'inputs': ['tc_replacement_d2_157'], 'func': tc_replacement_d3_157}


def tc_replacement_d3_158(tc_replacement_d2_158):
    feature = _clean(tc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_158'] = {'inputs': ['tc_replacement_d2_158'], 'func': tc_replacement_d3_158}


def tc_replacement_d3_159(tc_replacement_d2_159):
    feature = _clean(tc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_159'] = {'inputs': ['tc_replacement_d2_159'], 'func': tc_replacement_d3_159}


def tc_replacement_d3_160(tc_replacement_d2_160):
    feature = _clean(tc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_160'] = {'inputs': ['tc_replacement_d2_160'], 'func': tc_replacement_d3_160}


def tc_replacement_d3_161(tc_replacement_d2_161):
    feature = _clean(tc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_161'] = {'inputs': ['tc_replacement_d2_161'], 'func': tc_replacement_d3_161}


def tc_replacement_d3_162(tc_replacement_d2_162):
    feature = _clean(tc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_162'] = {'inputs': ['tc_replacement_d2_162'], 'func': tc_replacement_d3_162}


def tc_replacement_d3_163(tc_replacement_d2_163):
    feature = _clean(tc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_163'] = {'inputs': ['tc_replacement_d2_163'], 'func': tc_replacement_d3_163}


def tc_replacement_d3_164(tc_replacement_d2_164):
    feature = _clean(tc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_164'] = {'inputs': ['tc_replacement_d2_164'], 'func': tc_replacement_d3_164}


def tc_replacement_d3_165(tc_replacement_d2_165):
    feature = _clean(tc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_165'] = {'inputs': ['tc_replacement_d2_165'], 'func': tc_replacement_d3_165}


def tc_replacement_d3_166(tc_replacement_d2_166):
    feature = _clean(tc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_166'] = {'inputs': ['tc_replacement_d2_166'], 'func': tc_replacement_d3_166}


def tc_replacement_d3_167(tc_replacement_d2_167):
    feature = _clean(tc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_167'] = {'inputs': ['tc_replacement_d2_167'], 'func': tc_replacement_d3_167}


def tc_replacement_d3_168(tc_replacement_d2_168):
    feature = _clean(tc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_168'] = {'inputs': ['tc_replacement_d2_168'], 'func': tc_replacement_d3_168}


def tc_replacement_d3_169(tc_replacement_d2_169):
    feature = _clean(tc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_169'] = {'inputs': ['tc_replacement_d2_169'], 'func': tc_replacement_d3_169}


def tc_replacement_d3_170(tc_replacement_d2_170):
    feature = _clean(tc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
TC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tc_replacement_d3_170'] = {'inputs': ['tc_replacement_d2_170'], 'func': tc_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tcl_base_universe_d3_001_tcl_002_zero_volume_frequency_10_002(tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002):
    return _base_universe_d3(tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002, 1)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_001_tcl_002_zero_volume_frequency_10_002'] = {'inputs': ['tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002'], 'func': tcl_base_universe_d3_001_tcl_002_zero_volume_frequency_10_002}


def tcl_base_universe_d3_002_tcl_003_spread_proxy_21_003(tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003):
    return _base_universe_d3(tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003, 2)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_002_tcl_003_spread_proxy_21_003'] = {'inputs': ['tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003'], 'func': tcl_base_universe_d3_002_tcl_003_spread_proxy_21_003}


def tcl_base_universe_d3_003_tcl_004_trading_intensity_42_004(tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004):
    return _base_universe_d3(tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004, 3)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_003_tcl_004_trading_intensity_42_004'] = {'inputs': ['tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004'], 'func': tcl_base_universe_d3_003_tcl_004_trading_intensity_42_004}


def tcl_base_universe_d3_004_tcl_006_price_level_distress_84_006(tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006):
    return _base_universe_d3(tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006, 4)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_004_tcl_006_price_level_distress_84_006'] = {'inputs': ['tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006'], 'func': tcl_base_universe_d3_004_tcl_006_price_level_distress_84_006}


def tcl_base_universe_d3_005_tcl_008_zero_volume_frequency_189_008(tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008):
    return _base_universe_d3(tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008, 5)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_005_tcl_008_zero_volume_frequency_189_008'] = {'inputs': ['tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008'], 'func': tcl_base_universe_d3_005_tcl_008_zero_volume_frequency_189_008}


def tcl_base_universe_d3_006_tcl_009_spread_proxy_252_009(tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009):
    return _base_universe_d3(tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009, 6)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_006_tcl_009_spread_proxy_252_009'] = {'inputs': ['tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009'], 'func': tcl_base_universe_d3_006_tcl_009_spread_proxy_252_009}


def tcl_base_universe_d3_007_tcl_010_trading_intensity_378_010(tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010):
    return _base_universe_d3(tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010, 7)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_007_tcl_010_trading_intensity_378_010'] = {'inputs': ['tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010'], 'func': tcl_base_universe_d3_007_tcl_010_trading_intensity_378_010}


def tcl_base_universe_d3_008_tcl_012_price_level_distress_756_012(tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012):
    return _base_universe_d3(tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012, 8)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_008_tcl_012_price_level_distress_756_012'] = {'inputs': ['tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012'], 'func': tcl_base_universe_d3_008_tcl_012_price_level_distress_756_012}


def tcl_base_universe_d3_009_tcl_014_zero_volume_frequency_1260_014(tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014, 9)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_009_tcl_014_zero_volume_frequency_1260_014'] = {'inputs': ['tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014'], 'func': tcl_base_universe_d3_009_tcl_014_zero_volume_frequency_1260_014}


def tcl_base_universe_d3_010_tcl_015_spread_proxy_1512_015(tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015):
    return _base_universe_d3(tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015, 10)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_010_tcl_015_spread_proxy_1512_015'] = {'inputs': ['tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015'], 'func': tcl_base_universe_d3_010_tcl_015_spread_proxy_1512_015}


def tcl_base_universe_d3_011_tcl_016_trading_intensity_5_016(tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016):
    return _base_universe_d3(tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016, 11)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_011_tcl_016_trading_intensity_5_016'] = {'inputs': ['tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016'], 'func': tcl_base_universe_d3_011_tcl_016_trading_intensity_5_016}


def tcl_base_universe_d3_012_tcl_018_price_level_distress_21_018(tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018):
    return _base_universe_d3(tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018, 12)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_012_tcl_018_price_level_distress_21_018'] = {'inputs': ['tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018'], 'func': tcl_base_universe_d3_012_tcl_018_price_level_distress_21_018}


def tcl_base_universe_d3_013_tcl_020_zero_volume_frequency_63_020(tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020):
    return _base_universe_d3(tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020, 13)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_013_tcl_020_zero_volume_frequency_63_020'] = {'inputs': ['tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020'], 'func': tcl_base_universe_d3_013_tcl_020_zero_volume_frequency_63_020}


def tcl_base_universe_d3_014_tcl_021_spread_proxy_84_021(tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021):
    return _base_universe_d3(tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021, 14)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_014_tcl_021_spread_proxy_84_021'] = {'inputs': ['tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021'], 'func': tcl_base_universe_d3_014_tcl_021_spread_proxy_84_021}


def tcl_base_universe_d3_015_tcl_022_trading_intensity_126_022(tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022):
    return _base_universe_d3(tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022, 15)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_015_tcl_022_trading_intensity_126_022'] = {'inputs': ['tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022'], 'func': tcl_base_universe_d3_015_tcl_022_trading_intensity_126_022}


def tcl_base_universe_d3_016_tcl_024_price_level_distress_252_024(tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024):
    return _base_universe_d3(tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024, 16)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_016_tcl_024_price_level_distress_252_024'] = {'inputs': ['tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024'], 'func': tcl_base_universe_d3_016_tcl_024_price_level_distress_252_024}


def tcl_base_universe_d3_017_tcl_026_zero_volume_frequency_504_026(tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026):
    return _base_universe_d3(tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026, 17)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_017_tcl_026_zero_volume_frequency_504_026'] = {'inputs': ['tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026'], 'func': tcl_base_universe_d3_017_tcl_026_zero_volume_frequency_504_026}


def tcl_base_universe_d3_018_tcl_027_spread_proxy_756_027(tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027):
    return _base_universe_d3(tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027, 18)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_018_tcl_027_spread_proxy_756_027'] = {'inputs': ['tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027'], 'func': tcl_base_universe_d3_018_tcl_027_spread_proxy_756_027}


def tcl_base_universe_d3_019_tcl_028_trading_intensity_1008_028(tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028):
    return _base_universe_d3(tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028, 19)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_019_tcl_028_trading_intensity_1008_028'] = {'inputs': ['tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028'], 'func': tcl_base_universe_d3_019_tcl_028_trading_intensity_1008_028}


def tcl_base_universe_d3_020_tcl_030_price_level_distress_1512_030(tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030):
    return _base_universe_d3(tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030, 20)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_020_tcl_030_price_level_distress_1512_030'] = {'inputs': ['tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030'], 'func': tcl_base_universe_d3_020_tcl_030_price_level_distress_1512_030}


def tcl_base_universe_d3_021_tcl_basefill_001(tcl_base_universe_d2_021_tcl_basefill_001):
    return _base_universe_d3(tcl_base_universe_d2_021_tcl_basefill_001, 21)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_021_tcl_basefill_001'] = {'inputs': ['tcl_base_universe_d2_021_tcl_basefill_001'], 'func': tcl_base_universe_d3_021_tcl_basefill_001}


def tcl_base_universe_d3_022_tcl_basefill_005(tcl_base_universe_d2_022_tcl_basefill_005):
    return _base_universe_d3(tcl_base_universe_d2_022_tcl_basefill_005, 22)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_022_tcl_basefill_005'] = {'inputs': ['tcl_base_universe_d2_022_tcl_basefill_005'], 'func': tcl_base_universe_d3_022_tcl_basefill_005}


def tcl_base_universe_d3_023_tcl_basefill_007(tcl_base_universe_d2_023_tcl_basefill_007):
    return _base_universe_d3(tcl_base_universe_d2_023_tcl_basefill_007, 23)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_023_tcl_basefill_007'] = {'inputs': ['tcl_base_universe_d2_023_tcl_basefill_007'], 'func': tcl_base_universe_d3_023_tcl_basefill_007}


def tcl_base_universe_d3_024_tcl_basefill_011(tcl_base_universe_d2_024_tcl_basefill_011):
    return _base_universe_d3(tcl_base_universe_d2_024_tcl_basefill_011, 24)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_024_tcl_basefill_011'] = {'inputs': ['tcl_base_universe_d2_024_tcl_basefill_011'], 'func': tcl_base_universe_d3_024_tcl_basefill_011}


def tcl_base_universe_d3_025_tcl_basefill_013(tcl_base_universe_d2_025_tcl_basefill_013):
    return _base_universe_d3(tcl_base_universe_d2_025_tcl_basefill_013, 25)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_025_tcl_basefill_013'] = {'inputs': ['tcl_base_universe_d2_025_tcl_basefill_013'], 'func': tcl_base_universe_d3_025_tcl_basefill_013}


def tcl_base_universe_d3_026_tcl_basefill_017(tcl_base_universe_d2_026_tcl_basefill_017):
    return _base_universe_d3(tcl_base_universe_d2_026_tcl_basefill_017, 26)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_026_tcl_basefill_017'] = {'inputs': ['tcl_base_universe_d2_026_tcl_basefill_017'], 'func': tcl_base_universe_d3_026_tcl_basefill_017}


def tcl_base_universe_d3_027_tcl_basefill_019(tcl_base_universe_d2_027_tcl_basefill_019):
    return _base_universe_d3(tcl_base_universe_d2_027_tcl_basefill_019, 27)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_027_tcl_basefill_019'] = {'inputs': ['tcl_base_universe_d2_027_tcl_basefill_019'], 'func': tcl_base_universe_d3_027_tcl_basefill_019}


def tcl_base_universe_d3_028_tcl_basefill_023(tcl_base_universe_d2_028_tcl_basefill_023):
    return _base_universe_d3(tcl_base_universe_d2_028_tcl_basefill_023, 28)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_028_tcl_basefill_023'] = {'inputs': ['tcl_base_universe_d2_028_tcl_basefill_023'], 'func': tcl_base_universe_d3_028_tcl_basefill_023}


def tcl_base_universe_d3_029_tcl_basefill_025(tcl_base_universe_d2_029_tcl_basefill_025):
    return _base_universe_d3(tcl_base_universe_d2_029_tcl_basefill_025, 29)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_029_tcl_basefill_025'] = {'inputs': ['tcl_base_universe_d2_029_tcl_basefill_025'], 'func': tcl_base_universe_d3_029_tcl_basefill_025}


def tcl_base_universe_d3_030_tcl_basefill_029(tcl_base_universe_d2_030_tcl_basefill_029):
    return _base_universe_d3(tcl_base_universe_d2_030_tcl_basefill_029, 30)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_030_tcl_basefill_029'] = {'inputs': ['tcl_base_universe_d2_030_tcl_basefill_029'], 'func': tcl_base_universe_d3_030_tcl_basefill_029}


def tcl_base_universe_d3_031_tcl_basefill_031(tcl_base_universe_d2_031_tcl_basefill_031):
    return _base_universe_d3(tcl_base_universe_d2_031_tcl_basefill_031, 31)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_031_tcl_basefill_031'] = {'inputs': ['tcl_base_universe_d2_031_tcl_basefill_031'], 'func': tcl_base_universe_d3_031_tcl_basefill_031}


def tcl_base_universe_d3_032_tcl_basefill_032(tcl_base_universe_d2_032_tcl_basefill_032):
    return _base_universe_d3(tcl_base_universe_d2_032_tcl_basefill_032, 32)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_032_tcl_basefill_032'] = {'inputs': ['tcl_base_universe_d2_032_tcl_basefill_032'], 'func': tcl_base_universe_d3_032_tcl_basefill_032}


def tcl_base_universe_d3_033_tcl_basefill_033(tcl_base_universe_d2_033_tcl_basefill_033):
    return _base_universe_d3(tcl_base_universe_d2_033_tcl_basefill_033, 33)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_033_tcl_basefill_033'] = {'inputs': ['tcl_base_universe_d2_033_tcl_basefill_033'], 'func': tcl_base_universe_d3_033_tcl_basefill_033}


def tcl_base_universe_d3_034_tcl_basefill_034(tcl_base_universe_d2_034_tcl_basefill_034):
    return _base_universe_d3(tcl_base_universe_d2_034_tcl_basefill_034, 34)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_034_tcl_basefill_034'] = {'inputs': ['tcl_base_universe_d2_034_tcl_basefill_034'], 'func': tcl_base_universe_d3_034_tcl_basefill_034}


def tcl_base_universe_d3_035_tcl_basefill_035(tcl_base_universe_d2_035_tcl_basefill_035):
    return _base_universe_d3(tcl_base_universe_d2_035_tcl_basefill_035, 35)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_035_tcl_basefill_035'] = {'inputs': ['tcl_base_universe_d2_035_tcl_basefill_035'], 'func': tcl_base_universe_d3_035_tcl_basefill_035}


def tcl_base_universe_d3_036_tcl_basefill_036(tcl_base_universe_d2_036_tcl_basefill_036):
    return _base_universe_d3(tcl_base_universe_d2_036_tcl_basefill_036, 36)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_036_tcl_basefill_036'] = {'inputs': ['tcl_base_universe_d2_036_tcl_basefill_036'], 'func': tcl_base_universe_d3_036_tcl_basefill_036}


def tcl_base_universe_d3_037_tcl_basefill_037(tcl_base_universe_d2_037_tcl_basefill_037):
    return _base_universe_d3(tcl_base_universe_d2_037_tcl_basefill_037, 37)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_037_tcl_basefill_037'] = {'inputs': ['tcl_base_universe_d2_037_tcl_basefill_037'], 'func': tcl_base_universe_d3_037_tcl_basefill_037}


def tcl_base_universe_d3_038_tcl_basefill_038(tcl_base_universe_d2_038_tcl_basefill_038):
    return _base_universe_d3(tcl_base_universe_d2_038_tcl_basefill_038, 38)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_038_tcl_basefill_038'] = {'inputs': ['tcl_base_universe_d2_038_tcl_basefill_038'], 'func': tcl_base_universe_d3_038_tcl_basefill_038}


def tcl_base_universe_d3_039_tcl_basefill_039(tcl_base_universe_d2_039_tcl_basefill_039):
    return _base_universe_d3(tcl_base_universe_d2_039_tcl_basefill_039, 39)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_039_tcl_basefill_039'] = {'inputs': ['tcl_base_universe_d2_039_tcl_basefill_039'], 'func': tcl_base_universe_d3_039_tcl_basefill_039}


def tcl_base_universe_d3_040_tcl_basefill_040(tcl_base_universe_d2_040_tcl_basefill_040):
    return _base_universe_d3(tcl_base_universe_d2_040_tcl_basefill_040, 40)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_040_tcl_basefill_040'] = {'inputs': ['tcl_base_universe_d2_040_tcl_basefill_040'], 'func': tcl_base_universe_d3_040_tcl_basefill_040}


def tcl_base_universe_d3_041_tcl_basefill_041(tcl_base_universe_d2_041_tcl_basefill_041):
    return _base_universe_d3(tcl_base_universe_d2_041_tcl_basefill_041, 41)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_041_tcl_basefill_041'] = {'inputs': ['tcl_base_universe_d2_041_tcl_basefill_041'], 'func': tcl_base_universe_d3_041_tcl_basefill_041}


def tcl_base_universe_d3_042_tcl_basefill_042(tcl_base_universe_d2_042_tcl_basefill_042):
    return _base_universe_d3(tcl_base_universe_d2_042_tcl_basefill_042, 42)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_042_tcl_basefill_042'] = {'inputs': ['tcl_base_universe_d2_042_tcl_basefill_042'], 'func': tcl_base_universe_d3_042_tcl_basefill_042}


def tcl_base_universe_d3_043_tcl_basefill_043(tcl_base_universe_d2_043_tcl_basefill_043):
    return _base_universe_d3(tcl_base_universe_d2_043_tcl_basefill_043, 43)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_043_tcl_basefill_043'] = {'inputs': ['tcl_base_universe_d2_043_tcl_basefill_043'], 'func': tcl_base_universe_d3_043_tcl_basefill_043}


def tcl_base_universe_d3_044_tcl_basefill_044(tcl_base_universe_d2_044_tcl_basefill_044):
    return _base_universe_d3(tcl_base_universe_d2_044_tcl_basefill_044, 44)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_044_tcl_basefill_044'] = {'inputs': ['tcl_base_universe_d2_044_tcl_basefill_044'], 'func': tcl_base_universe_d3_044_tcl_basefill_044}


def tcl_base_universe_d3_045_tcl_basefill_045(tcl_base_universe_d2_045_tcl_basefill_045):
    return _base_universe_d3(tcl_base_universe_d2_045_tcl_basefill_045, 45)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_045_tcl_basefill_045'] = {'inputs': ['tcl_base_universe_d2_045_tcl_basefill_045'], 'func': tcl_base_universe_d3_045_tcl_basefill_045}


def tcl_base_universe_d3_046_tcl_basefill_046(tcl_base_universe_d2_046_tcl_basefill_046):
    return _base_universe_d3(tcl_base_universe_d2_046_tcl_basefill_046, 46)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_046_tcl_basefill_046'] = {'inputs': ['tcl_base_universe_d2_046_tcl_basefill_046'], 'func': tcl_base_universe_d3_046_tcl_basefill_046}


def tcl_base_universe_d3_047_tcl_basefill_047(tcl_base_universe_d2_047_tcl_basefill_047):
    return _base_universe_d3(tcl_base_universe_d2_047_tcl_basefill_047, 47)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_047_tcl_basefill_047'] = {'inputs': ['tcl_base_universe_d2_047_tcl_basefill_047'], 'func': tcl_base_universe_d3_047_tcl_basefill_047}


def tcl_base_universe_d3_048_tcl_basefill_048(tcl_base_universe_d2_048_tcl_basefill_048):
    return _base_universe_d3(tcl_base_universe_d2_048_tcl_basefill_048, 48)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_048_tcl_basefill_048'] = {'inputs': ['tcl_base_universe_d2_048_tcl_basefill_048'], 'func': tcl_base_universe_d3_048_tcl_basefill_048}


def tcl_base_universe_d3_049_tcl_basefill_049(tcl_base_universe_d2_049_tcl_basefill_049):
    return _base_universe_d3(tcl_base_universe_d2_049_tcl_basefill_049, 49)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_049_tcl_basefill_049'] = {'inputs': ['tcl_base_universe_d2_049_tcl_basefill_049'], 'func': tcl_base_universe_d3_049_tcl_basefill_049}


def tcl_base_universe_d3_050_tcl_basefill_050(tcl_base_universe_d2_050_tcl_basefill_050):
    return _base_universe_d3(tcl_base_universe_d2_050_tcl_basefill_050, 50)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_050_tcl_basefill_050'] = {'inputs': ['tcl_base_universe_d2_050_tcl_basefill_050'], 'func': tcl_base_universe_d3_050_tcl_basefill_050}


def tcl_base_universe_d3_051_tcl_basefill_051(tcl_base_universe_d2_051_tcl_basefill_051):
    return _base_universe_d3(tcl_base_universe_d2_051_tcl_basefill_051, 51)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_051_tcl_basefill_051'] = {'inputs': ['tcl_base_universe_d2_051_tcl_basefill_051'], 'func': tcl_base_universe_d3_051_tcl_basefill_051}


def tcl_base_universe_d3_052_tcl_basefill_052(tcl_base_universe_d2_052_tcl_basefill_052):
    return _base_universe_d3(tcl_base_universe_d2_052_tcl_basefill_052, 52)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_052_tcl_basefill_052'] = {'inputs': ['tcl_base_universe_d2_052_tcl_basefill_052'], 'func': tcl_base_universe_d3_052_tcl_basefill_052}


def tcl_base_universe_d3_053_tcl_basefill_053(tcl_base_universe_d2_053_tcl_basefill_053):
    return _base_universe_d3(tcl_base_universe_d2_053_tcl_basefill_053, 53)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_053_tcl_basefill_053'] = {'inputs': ['tcl_base_universe_d2_053_tcl_basefill_053'], 'func': tcl_base_universe_d3_053_tcl_basefill_053}


def tcl_base_universe_d3_054_tcl_basefill_054(tcl_base_universe_d2_054_tcl_basefill_054):
    return _base_universe_d3(tcl_base_universe_d2_054_tcl_basefill_054, 54)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_054_tcl_basefill_054'] = {'inputs': ['tcl_base_universe_d2_054_tcl_basefill_054'], 'func': tcl_base_universe_d3_054_tcl_basefill_054}


def tcl_base_universe_d3_055_tcl_basefill_055(tcl_base_universe_d2_055_tcl_basefill_055):
    return _base_universe_d3(tcl_base_universe_d2_055_tcl_basefill_055, 55)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_055_tcl_basefill_055'] = {'inputs': ['tcl_base_universe_d2_055_tcl_basefill_055'], 'func': tcl_base_universe_d3_055_tcl_basefill_055}


def tcl_base_universe_d3_056_tcl_basefill_056(tcl_base_universe_d2_056_tcl_basefill_056):
    return _base_universe_d3(tcl_base_universe_d2_056_tcl_basefill_056, 56)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_056_tcl_basefill_056'] = {'inputs': ['tcl_base_universe_d2_056_tcl_basefill_056'], 'func': tcl_base_universe_d3_056_tcl_basefill_056}


def tcl_base_universe_d3_057_tcl_basefill_057(tcl_base_universe_d2_057_tcl_basefill_057):
    return _base_universe_d3(tcl_base_universe_d2_057_tcl_basefill_057, 57)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_057_tcl_basefill_057'] = {'inputs': ['tcl_base_universe_d2_057_tcl_basefill_057'], 'func': tcl_base_universe_d3_057_tcl_basefill_057}


def tcl_base_universe_d3_058_tcl_basefill_058(tcl_base_universe_d2_058_tcl_basefill_058):
    return _base_universe_d3(tcl_base_universe_d2_058_tcl_basefill_058, 58)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_058_tcl_basefill_058'] = {'inputs': ['tcl_base_universe_d2_058_tcl_basefill_058'], 'func': tcl_base_universe_d3_058_tcl_basefill_058}


def tcl_base_universe_d3_059_tcl_basefill_059(tcl_base_universe_d2_059_tcl_basefill_059):
    return _base_universe_d3(tcl_base_universe_d2_059_tcl_basefill_059, 59)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_059_tcl_basefill_059'] = {'inputs': ['tcl_base_universe_d2_059_tcl_basefill_059'], 'func': tcl_base_universe_d3_059_tcl_basefill_059}


def tcl_base_universe_d3_060_tcl_basefill_060(tcl_base_universe_d2_060_tcl_basefill_060):
    return _base_universe_d3(tcl_base_universe_d2_060_tcl_basefill_060, 60)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_060_tcl_basefill_060'] = {'inputs': ['tcl_base_universe_d2_060_tcl_basefill_060'], 'func': tcl_base_universe_d3_060_tcl_basefill_060}


def tcl_base_universe_d3_061_tcl_basefill_061(tcl_base_universe_d2_061_tcl_basefill_061):
    return _base_universe_d3(tcl_base_universe_d2_061_tcl_basefill_061, 61)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_061_tcl_basefill_061'] = {'inputs': ['tcl_base_universe_d2_061_tcl_basefill_061'], 'func': tcl_base_universe_d3_061_tcl_basefill_061}


def tcl_base_universe_d3_062_tcl_basefill_062(tcl_base_universe_d2_062_tcl_basefill_062):
    return _base_universe_d3(tcl_base_universe_d2_062_tcl_basefill_062, 62)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_062_tcl_basefill_062'] = {'inputs': ['tcl_base_universe_d2_062_tcl_basefill_062'], 'func': tcl_base_universe_d3_062_tcl_basefill_062}


def tcl_base_universe_d3_063_tcl_basefill_063(tcl_base_universe_d2_063_tcl_basefill_063):
    return _base_universe_d3(tcl_base_universe_d2_063_tcl_basefill_063, 63)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_063_tcl_basefill_063'] = {'inputs': ['tcl_base_universe_d2_063_tcl_basefill_063'], 'func': tcl_base_universe_d3_063_tcl_basefill_063}


def tcl_base_universe_d3_064_tcl_basefill_064(tcl_base_universe_d2_064_tcl_basefill_064):
    return _base_universe_d3(tcl_base_universe_d2_064_tcl_basefill_064, 64)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_064_tcl_basefill_064'] = {'inputs': ['tcl_base_universe_d2_064_tcl_basefill_064'], 'func': tcl_base_universe_d3_064_tcl_basefill_064}


def tcl_base_universe_d3_065_tcl_basefill_065(tcl_base_universe_d2_065_tcl_basefill_065):
    return _base_universe_d3(tcl_base_universe_d2_065_tcl_basefill_065, 65)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_065_tcl_basefill_065'] = {'inputs': ['tcl_base_universe_d2_065_tcl_basefill_065'], 'func': tcl_base_universe_d3_065_tcl_basefill_065}


def tcl_base_universe_d3_066_tcl_basefill_066(tcl_base_universe_d2_066_tcl_basefill_066):
    return _base_universe_d3(tcl_base_universe_d2_066_tcl_basefill_066, 66)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_066_tcl_basefill_066'] = {'inputs': ['tcl_base_universe_d2_066_tcl_basefill_066'], 'func': tcl_base_universe_d3_066_tcl_basefill_066}


def tcl_base_universe_d3_067_tcl_basefill_067(tcl_base_universe_d2_067_tcl_basefill_067):
    return _base_universe_d3(tcl_base_universe_d2_067_tcl_basefill_067, 67)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_067_tcl_basefill_067'] = {'inputs': ['tcl_base_universe_d2_067_tcl_basefill_067'], 'func': tcl_base_universe_d3_067_tcl_basefill_067}


def tcl_base_universe_d3_068_tcl_basefill_068(tcl_base_universe_d2_068_tcl_basefill_068):
    return _base_universe_d3(tcl_base_universe_d2_068_tcl_basefill_068, 68)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_068_tcl_basefill_068'] = {'inputs': ['tcl_base_universe_d2_068_tcl_basefill_068'], 'func': tcl_base_universe_d3_068_tcl_basefill_068}


def tcl_base_universe_d3_069_tcl_basefill_069(tcl_base_universe_d2_069_tcl_basefill_069):
    return _base_universe_d3(tcl_base_universe_d2_069_tcl_basefill_069, 69)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_069_tcl_basefill_069'] = {'inputs': ['tcl_base_universe_d2_069_tcl_basefill_069'], 'func': tcl_base_universe_d3_069_tcl_basefill_069}


def tcl_base_universe_d3_070_tcl_basefill_070(tcl_base_universe_d2_070_tcl_basefill_070):
    return _base_universe_d3(tcl_base_universe_d2_070_tcl_basefill_070, 70)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_070_tcl_basefill_070'] = {'inputs': ['tcl_base_universe_d2_070_tcl_basefill_070'], 'func': tcl_base_universe_d3_070_tcl_basefill_070}


def tcl_base_universe_d3_071_tcl_basefill_071(tcl_base_universe_d2_071_tcl_basefill_071):
    return _base_universe_d3(tcl_base_universe_d2_071_tcl_basefill_071, 71)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_071_tcl_basefill_071'] = {'inputs': ['tcl_base_universe_d2_071_tcl_basefill_071'], 'func': tcl_base_universe_d3_071_tcl_basefill_071}


def tcl_base_universe_d3_072_tcl_basefill_072(tcl_base_universe_d2_072_tcl_basefill_072):
    return _base_universe_d3(tcl_base_universe_d2_072_tcl_basefill_072, 72)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_072_tcl_basefill_072'] = {'inputs': ['tcl_base_universe_d2_072_tcl_basefill_072'], 'func': tcl_base_universe_d3_072_tcl_basefill_072}


def tcl_base_universe_d3_073_tcl_basefill_073(tcl_base_universe_d2_073_tcl_basefill_073):
    return _base_universe_d3(tcl_base_universe_d2_073_tcl_basefill_073, 73)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_073_tcl_basefill_073'] = {'inputs': ['tcl_base_universe_d2_073_tcl_basefill_073'], 'func': tcl_base_universe_d3_073_tcl_basefill_073}


def tcl_base_universe_d3_074_tcl_basefill_074(tcl_base_universe_d2_074_tcl_basefill_074):
    return _base_universe_d3(tcl_base_universe_d2_074_tcl_basefill_074, 74)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_074_tcl_basefill_074'] = {'inputs': ['tcl_base_universe_d2_074_tcl_basefill_074'], 'func': tcl_base_universe_d3_074_tcl_basefill_074}


def tcl_base_universe_d3_075_tcl_basefill_075(tcl_base_universe_d2_075_tcl_basefill_075):
    return _base_universe_d3(tcl_base_universe_d2_075_tcl_basefill_075, 75)
TCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tcl_base_universe_d3_075_tcl_basefill_075'] = {'inputs': ['tcl_base_universe_d2_075_tcl_basefill_075'], 'func': tcl_base_universe_d3_075_tcl_basefill_075}
