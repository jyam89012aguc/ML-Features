import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


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



def evl_176_evl_001_netinc_decline_1_accel_1(evl_151_evl_001_netinc_decline_1_roc_1):
    feature = _s(evl_151_evl_001_netinc_decline_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def evl_177_evl_007_interest_coverage_stress_252_accel_42(evl_152_evl_007_interest_coverage_stress_252_roc_42):
    feature = _s(evl_152_evl_007_interest_coverage_stress_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def evl_178_evl_013_netinc_decline_1_accel_126(evl_153_evl_013_netinc_decline_1_roc_126):
    feature = _s(evl_153_evl_013_netinc_decline_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def evl_179_evl_019_interest_coverage_stress_84_accel_378(evl_154_evl_019_interest_coverage_stress_84_roc_378):
    feature = _s(evl_154_evl_019_interest_coverage_stress_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def evl_180_evl_025_netinc_decline_1_accel_4(evl_155_evl_025_netinc_decline_1_roc_4):
    feature = _s(evl_155_evl_025_netinc_decline_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















EARNINGS_VOLATILITY_REGISTRY_3RD_DERIVATIVES = {
    'evl_176_evl_001_netinc_decline_1_accel_1': {'inputs': ['evl_151_evl_001_netinc_decline_1_roc_1'], 'func': evl_176_evl_001_netinc_decline_1_accel_1},
    'evl_177_evl_007_interest_coverage_stress_252_accel_42': {'inputs': ['evl_152_evl_007_interest_coverage_stress_252_roc_42'], 'func': evl_177_evl_007_interest_coverage_stress_252_accel_42},
    'evl_178_evl_013_netinc_decline_1_accel_126': {'inputs': ['evl_153_evl_013_netinc_decline_1_roc_126'], 'func': evl_178_evl_013_netinc_decline_1_accel_126},
    'evl_179_evl_019_interest_coverage_stress_84_accel_378': {'inputs': ['evl_154_evl_019_interest_coverage_stress_84_roc_378'], 'func': evl_179_evl_019_interest_coverage_stress_84_accel_378},
    'evl_180_evl_025_netinc_decline_1_accel_4': {'inputs': ['evl_155_evl_025_netinc_decline_1_roc_4'], 'func': evl_180_evl_025_netinc_decline_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ev_replacement_d3_001(ev_replacement_d2_001):
    feature = _clean(ev_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_001'] = {'inputs': ['ev_replacement_d2_001'], 'func': ev_replacement_d3_001}


def ev_replacement_d3_002(ev_replacement_d2_002):
    feature = _clean(ev_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_002'] = {'inputs': ['ev_replacement_d2_002'], 'func': ev_replacement_d3_002}


def ev_replacement_d3_003(ev_replacement_d2_003):
    feature = _clean(ev_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_003'] = {'inputs': ['ev_replacement_d2_003'], 'func': ev_replacement_d3_003}


def ev_replacement_d3_004(ev_replacement_d2_004):
    feature = _clean(ev_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_004'] = {'inputs': ['ev_replacement_d2_004'], 'func': ev_replacement_d3_004}


def ev_replacement_d3_005(ev_replacement_d2_005):
    feature = _clean(ev_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_005'] = {'inputs': ['ev_replacement_d2_005'], 'func': ev_replacement_d3_005}


def ev_replacement_d3_006(ev_replacement_d2_006):
    feature = _clean(ev_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_006'] = {'inputs': ['ev_replacement_d2_006'], 'func': ev_replacement_d3_006}


def ev_replacement_d3_007(ev_replacement_d2_007):
    feature = _clean(ev_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_007'] = {'inputs': ['ev_replacement_d2_007'], 'func': ev_replacement_d3_007}


def ev_replacement_d3_008(ev_replacement_d2_008):
    feature = _clean(ev_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_008'] = {'inputs': ['ev_replacement_d2_008'], 'func': ev_replacement_d3_008}


def ev_replacement_d3_009(ev_replacement_d2_009):
    feature = _clean(ev_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_009'] = {'inputs': ['ev_replacement_d2_009'], 'func': ev_replacement_d3_009}


def ev_replacement_d3_010(ev_replacement_d2_010):
    feature = _clean(ev_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_010'] = {'inputs': ['ev_replacement_d2_010'], 'func': ev_replacement_d3_010}


def ev_replacement_d3_011(ev_replacement_d2_011):
    feature = _clean(ev_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_011'] = {'inputs': ['ev_replacement_d2_011'], 'func': ev_replacement_d3_011}


def ev_replacement_d3_012(ev_replacement_d2_012):
    feature = _clean(ev_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_012'] = {'inputs': ['ev_replacement_d2_012'], 'func': ev_replacement_d3_012}


def ev_replacement_d3_013(ev_replacement_d2_013):
    feature = _clean(ev_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_013'] = {'inputs': ['ev_replacement_d2_013'], 'func': ev_replacement_d3_013}


def ev_replacement_d3_014(ev_replacement_d2_014):
    feature = _clean(ev_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_014'] = {'inputs': ['ev_replacement_d2_014'], 'func': ev_replacement_d3_014}


def ev_replacement_d3_015(ev_replacement_d2_015):
    feature = _clean(ev_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_015'] = {'inputs': ['ev_replacement_d2_015'], 'func': ev_replacement_d3_015}


def ev_replacement_d3_016(ev_replacement_d2_016):
    feature = _clean(ev_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_016'] = {'inputs': ['ev_replacement_d2_016'], 'func': ev_replacement_d3_016}


def ev_replacement_d3_017(ev_replacement_d2_017):
    feature = _clean(ev_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_017'] = {'inputs': ['ev_replacement_d2_017'], 'func': ev_replacement_d3_017}


def ev_replacement_d3_018(ev_replacement_d2_018):
    feature = _clean(ev_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_018'] = {'inputs': ['ev_replacement_d2_018'], 'func': ev_replacement_d3_018}


def ev_replacement_d3_019(ev_replacement_d2_019):
    feature = _clean(ev_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_019'] = {'inputs': ['ev_replacement_d2_019'], 'func': ev_replacement_d3_019}


def ev_replacement_d3_020(ev_replacement_d2_020):
    feature = _clean(ev_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_020'] = {'inputs': ['ev_replacement_d2_020'], 'func': ev_replacement_d3_020}


def ev_replacement_d3_021(ev_replacement_d2_021):
    feature = _clean(ev_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_021'] = {'inputs': ['ev_replacement_d2_021'], 'func': ev_replacement_d3_021}


def ev_replacement_d3_022(ev_replacement_d2_022):
    feature = _clean(ev_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_022'] = {'inputs': ['ev_replacement_d2_022'], 'func': ev_replacement_d3_022}


def ev_replacement_d3_023(ev_replacement_d2_023):
    feature = _clean(ev_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_023'] = {'inputs': ['ev_replacement_d2_023'], 'func': ev_replacement_d3_023}


def ev_replacement_d3_024(ev_replacement_d2_024):
    feature = _clean(ev_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_024'] = {'inputs': ['ev_replacement_d2_024'], 'func': ev_replacement_d3_024}


def ev_replacement_d3_025(ev_replacement_d2_025):
    feature = _clean(ev_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_025'] = {'inputs': ['ev_replacement_d2_025'], 'func': ev_replacement_d3_025}


def ev_replacement_d3_026(ev_replacement_d2_026):
    feature = _clean(ev_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_026'] = {'inputs': ['ev_replacement_d2_026'], 'func': ev_replacement_d3_026}


def ev_replacement_d3_027(ev_replacement_d2_027):
    feature = _clean(ev_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_027'] = {'inputs': ['ev_replacement_d2_027'], 'func': ev_replacement_d3_027}


def ev_replacement_d3_028(ev_replacement_d2_028):
    feature = _clean(ev_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_028'] = {'inputs': ['ev_replacement_d2_028'], 'func': ev_replacement_d3_028}


def ev_replacement_d3_029(ev_replacement_d2_029):
    feature = _clean(ev_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_029'] = {'inputs': ['ev_replacement_d2_029'], 'func': ev_replacement_d3_029}


def ev_replacement_d3_030(ev_replacement_d2_030):
    feature = _clean(ev_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_030'] = {'inputs': ['ev_replacement_d2_030'], 'func': ev_replacement_d3_030}


def ev_replacement_d3_031(ev_replacement_d2_031):
    feature = _clean(ev_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_031'] = {'inputs': ['ev_replacement_d2_031'], 'func': ev_replacement_d3_031}


def ev_replacement_d3_032(ev_replacement_d2_032):
    feature = _clean(ev_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_032'] = {'inputs': ['ev_replacement_d2_032'], 'func': ev_replacement_d3_032}


def ev_replacement_d3_033(ev_replacement_d2_033):
    feature = _clean(ev_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_033'] = {'inputs': ['ev_replacement_d2_033'], 'func': ev_replacement_d3_033}


def ev_replacement_d3_034(ev_replacement_d2_034):
    feature = _clean(ev_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_034'] = {'inputs': ['ev_replacement_d2_034'], 'func': ev_replacement_d3_034}


def ev_replacement_d3_035(ev_replacement_d2_035):
    feature = _clean(ev_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_035'] = {'inputs': ['ev_replacement_d2_035'], 'func': ev_replacement_d3_035}


def ev_replacement_d3_036(ev_replacement_d2_036):
    feature = _clean(ev_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_036'] = {'inputs': ['ev_replacement_d2_036'], 'func': ev_replacement_d3_036}


def ev_replacement_d3_037(ev_replacement_d2_037):
    feature = _clean(ev_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_037'] = {'inputs': ['ev_replacement_d2_037'], 'func': ev_replacement_d3_037}


def ev_replacement_d3_038(ev_replacement_d2_038):
    feature = _clean(ev_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_038'] = {'inputs': ['ev_replacement_d2_038'], 'func': ev_replacement_d3_038}


def ev_replacement_d3_039(ev_replacement_d2_039):
    feature = _clean(ev_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_039'] = {'inputs': ['ev_replacement_d2_039'], 'func': ev_replacement_d3_039}


def ev_replacement_d3_040(ev_replacement_d2_040):
    feature = _clean(ev_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_040'] = {'inputs': ['ev_replacement_d2_040'], 'func': ev_replacement_d3_040}


def ev_replacement_d3_041(ev_replacement_d2_041):
    feature = _clean(ev_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_041'] = {'inputs': ['ev_replacement_d2_041'], 'func': ev_replacement_d3_041}


def ev_replacement_d3_042(ev_replacement_d2_042):
    feature = _clean(ev_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_042'] = {'inputs': ['ev_replacement_d2_042'], 'func': ev_replacement_d3_042}


def ev_replacement_d3_043(ev_replacement_d2_043):
    feature = _clean(ev_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_043'] = {'inputs': ['ev_replacement_d2_043'], 'func': ev_replacement_d3_043}


def ev_replacement_d3_044(ev_replacement_d2_044):
    feature = _clean(ev_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_044'] = {'inputs': ['ev_replacement_d2_044'], 'func': ev_replacement_d3_044}


def ev_replacement_d3_045(ev_replacement_d2_045):
    feature = _clean(ev_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_045'] = {'inputs': ['ev_replacement_d2_045'], 'func': ev_replacement_d3_045}


def ev_replacement_d3_046(ev_replacement_d2_046):
    feature = _clean(ev_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_046'] = {'inputs': ['ev_replacement_d2_046'], 'func': ev_replacement_d3_046}


def ev_replacement_d3_047(ev_replacement_d2_047):
    feature = _clean(ev_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_047'] = {'inputs': ['ev_replacement_d2_047'], 'func': ev_replacement_d3_047}


def ev_replacement_d3_048(ev_replacement_d2_048):
    feature = _clean(ev_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_048'] = {'inputs': ['ev_replacement_d2_048'], 'func': ev_replacement_d3_048}


def ev_replacement_d3_049(ev_replacement_d2_049):
    feature = _clean(ev_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_049'] = {'inputs': ['ev_replacement_d2_049'], 'func': ev_replacement_d3_049}


def ev_replacement_d3_050(ev_replacement_d2_050):
    feature = _clean(ev_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_050'] = {'inputs': ['ev_replacement_d2_050'], 'func': ev_replacement_d3_050}


def ev_replacement_d3_051(ev_replacement_d2_051):
    feature = _clean(ev_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_051'] = {'inputs': ['ev_replacement_d2_051'], 'func': ev_replacement_d3_051}


def ev_replacement_d3_052(ev_replacement_d2_052):
    feature = _clean(ev_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_052'] = {'inputs': ['ev_replacement_d2_052'], 'func': ev_replacement_d3_052}


def ev_replacement_d3_053(ev_replacement_d2_053):
    feature = _clean(ev_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_053'] = {'inputs': ['ev_replacement_d2_053'], 'func': ev_replacement_d3_053}


def ev_replacement_d3_054(ev_replacement_d2_054):
    feature = _clean(ev_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_054'] = {'inputs': ['ev_replacement_d2_054'], 'func': ev_replacement_d3_054}


def ev_replacement_d3_055(ev_replacement_d2_055):
    feature = _clean(ev_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_055'] = {'inputs': ['ev_replacement_d2_055'], 'func': ev_replacement_d3_055}


def ev_replacement_d3_056(ev_replacement_d2_056):
    feature = _clean(ev_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_056'] = {'inputs': ['ev_replacement_d2_056'], 'func': ev_replacement_d3_056}


def ev_replacement_d3_057(ev_replacement_d2_057):
    feature = _clean(ev_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_057'] = {'inputs': ['ev_replacement_d2_057'], 'func': ev_replacement_d3_057}


def ev_replacement_d3_058(ev_replacement_d2_058):
    feature = _clean(ev_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_058'] = {'inputs': ['ev_replacement_d2_058'], 'func': ev_replacement_d3_058}


def ev_replacement_d3_059(ev_replacement_d2_059):
    feature = _clean(ev_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_059'] = {'inputs': ['ev_replacement_d2_059'], 'func': ev_replacement_d3_059}


def ev_replacement_d3_060(ev_replacement_d2_060):
    feature = _clean(ev_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_060'] = {'inputs': ['ev_replacement_d2_060'], 'func': ev_replacement_d3_060}


def ev_replacement_d3_061(ev_replacement_d2_061):
    feature = _clean(ev_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_061'] = {'inputs': ['ev_replacement_d2_061'], 'func': ev_replacement_d3_061}


def ev_replacement_d3_062(ev_replacement_d2_062):
    feature = _clean(ev_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_062'] = {'inputs': ['ev_replacement_d2_062'], 'func': ev_replacement_d3_062}


def ev_replacement_d3_063(ev_replacement_d2_063):
    feature = _clean(ev_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_063'] = {'inputs': ['ev_replacement_d2_063'], 'func': ev_replacement_d3_063}


def ev_replacement_d3_064(ev_replacement_d2_064):
    feature = _clean(ev_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_064'] = {'inputs': ['ev_replacement_d2_064'], 'func': ev_replacement_d3_064}


def ev_replacement_d3_065(ev_replacement_d2_065):
    feature = _clean(ev_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_065'] = {'inputs': ['ev_replacement_d2_065'], 'func': ev_replacement_d3_065}


def ev_replacement_d3_066(ev_replacement_d2_066):
    feature = _clean(ev_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_066'] = {'inputs': ['ev_replacement_d2_066'], 'func': ev_replacement_d3_066}


def ev_replacement_d3_067(ev_replacement_d2_067):
    feature = _clean(ev_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_067'] = {'inputs': ['ev_replacement_d2_067'], 'func': ev_replacement_d3_067}


def ev_replacement_d3_068(ev_replacement_d2_068):
    feature = _clean(ev_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_068'] = {'inputs': ['ev_replacement_d2_068'], 'func': ev_replacement_d3_068}


def ev_replacement_d3_069(ev_replacement_d2_069):
    feature = _clean(ev_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_069'] = {'inputs': ['ev_replacement_d2_069'], 'func': ev_replacement_d3_069}


def ev_replacement_d3_070(ev_replacement_d2_070):
    feature = _clean(ev_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_070'] = {'inputs': ['ev_replacement_d2_070'], 'func': ev_replacement_d3_070}


def ev_replacement_d3_071(ev_replacement_d2_071):
    feature = _clean(ev_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_071'] = {'inputs': ['ev_replacement_d2_071'], 'func': ev_replacement_d3_071}


def ev_replacement_d3_072(ev_replacement_d2_072):
    feature = _clean(ev_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_072'] = {'inputs': ['ev_replacement_d2_072'], 'func': ev_replacement_d3_072}


def ev_replacement_d3_073(ev_replacement_d2_073):
    feature = _clean(ev_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_073'] = {'inputs': ['ev_replacement_d2_073'], 'func': ev_replacement_d3_073}


def ev_replacement_d3_074(ev_replacement_d2_074):
    feature = _clean(ev_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_074'] = {'inputs': ['ev_replacement_d2_074'], 'func': ev_replacement_d3_074}


def ev_replacement_d3_075(ev_replacement_d2_075):
    feature = _clean(ev_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_075'] = {'inputs': ['ev_replacement_d2_075'], 'func': ev_replacement_d3_075}


def ev_replacement_d3_076(ev_replacement_d2_076):
    feature = _clean(ev_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_076'] = {'inputs': ['ev_replacement_d2_076'], 'func': ev_replacement_d3_076}


def ev_replacement_d3_077(ev_replacement_d2_077):
    feature = _clean(ev_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_077'] = {'inputs': ['ev_replacement_d2_077'], 'func': ev_replacement_d3_077}


def ev_replacement_d3_078(ev_replacement_d2_078):
    feature = _clean(ev_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_078'] = {'inputs': ['ev_replacement_d2_078'], 'func': ev_replacement_d3_078}


def ev_replacement_d3_079(ev_replacement_d2_079):
    feature = _clean(ev_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_079'] = {'inputs': ['ev_replacement_d2_079'], 'func': ev_replacement_d3_079}


def ev_replacement_d3_080(ev_replacement_d2_080):
    feature = _clean(ev_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_080'] = {'inputs': ['ev_replacement_d2_080'], 'func': ev_replacement_d3_080}


def ev_replacement_d3_081(ev_replacement_d2_081):
    feature = _clean(ev_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_081'] = {'inputs': ['ev_replacement_d2_081'], 'func': ev_replacement_d3_081}


def ev_replacement_d3_082(ev_replacement_d2_082):
    feature = _clean(ev_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_082'] = {'inputs': ['ev_replacement_d2_082'], 'func': ev_replacement_d3_082}


def ev_replacement_d3_083(ev_replacement_d2_083):
    feature = _clean(ev_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_083'] = {'inputs': ['ev_replacement_d2_083'], 'func': ev_replacement_d3_083}


def ev_replacement_d3_084(ev_replacement_d2_084):
    feature = _clean(ev_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_084'] = {'inputs': ['ev_replacement_d2_084'], 'func': ev_replacement_d3_084}


def ev_replacement_d3_085(ev_replacement_d2_085):
    feature = _clean(ev_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_085'] = {'inputs': ['ev_replacement_d2_085'], 'func': ev_replacement_d3_085}


def ev_replacement_d3_086(ev_replacement_d2_086):
    feature = _clean(ev_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_086'] = {'inputs': ['ev_replacement_d2_086'], 'func': ev_replacement_d3_086}


def ev_replacement_d3_087(ev_replacement_d2_087):
    feature = _clean(ev_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_087'] = {'inputs': ['ev_replacement_d2_087'], 'func': ev_replacement_d3_087}


def ev_replacement_d3_088(ev_replacement_d2_088):
    feature = _clean(ev_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_088'] = {'inputs': ['ev_replacement_d2_088'], 'func': ev_replacement_d3_088}


def ev_replacement_d3_089(ev_replacement_d2_089):
    feature = _clean(ev_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_089'] = {'inputs': ['ev_replacement_d2_089'], 'func': ev_replacement_d3_089}


def ev_replacement_d3_090(ev_replacement_d2_090):
    feature = _clean(ev_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_090'] = {'inputs': ['ev_replacement_d2_090'], 'func': ev_replacement_d3_090}


def ev_replacement_d3_091(ev_replacement_d2_091):
    feature = _clean(ev_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_091'] = {'inputs': ['ev_replacement_d2_091'], 'func': ev_replacement_d3_091}


def ev_replacement_d3_092(ev_replacement_d2_092):
    feature = _clean(ev_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_092'] = {'inputs': ['ev_replacement_d2_092'], 'func': ev_replacement_d3_092}


def ev_replacement_d3_093(ev_replacement_d2_093):
    feature = _clean(ev_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_093'] = {'inputs': ['ev_replacement_d2_093'], 'func': ev_replacement_d3_093}


def ev_replacement_d3_094(ev_replacement_d2_094):
    feature = _clean(ev_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_094'] = {'inputs': ['ev_replacement_d2_094'], 'func': ev_replacement_d3_094}


def ev_replacement_d3_095(ev_replacement_d2_095):
    feature = _clean(ev_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_095'] = {'inputs': ['ev_replacement_d2_095'], 'func': ev_replacement_d3_095}


def ev_replacement_d3_096(ev_replacement_d2_096):
    feature = _clean(ev_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_096'] = {'inputs': ['ev_replacement_d2_096'], 'func': ev_replacement_d3_096}


def ev_replacement_d3_097(ev_replacement_d2_097):
    feature = _clean(ev_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_097'] = {'inputs': ['ev_replacement_d2_097'], 'func': ev_replacement_d3_097}


def ev_replacement_d3_098(ev_replacement_d2_098):
    feature = _clean(ev_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_098'] = {'inputs': ['ev_replacement_d2_098'], 'func': ev_replacement_d3_098}


def ev_replacement_d3_099(ev_replacement_d2_099):
    feature = _clean(ev_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_099'] = {'inputs': ['ev_replacement_d2_099'], 'func': ev_replacement_d3_099}


def ev_replacement_d3_100(ev_replacement_d2_100):
    feature = _clean(ev_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_100'] = {'inputs': ['ev_replacement_d2_100'], 'func': ev_replacement_d3_100}


def ev_replacement_d3_101(ev_replacement_d2_101):
    feature = _clean(ev_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_101'] = {'inputs': ['ev_replacement_d2_101'], 'func': ev_replacement_d3_101}


def ev_replacement_d3_102(ev_replacement_d2_102):
    feature = _clean(ev_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_102'] = {'inputs': ['ev_replacement_d2_102'], 'func': ev_replacement_d3_102}


def ev_replacement_d3_103(ev_replacement_d2_103):
    feature = _clean(ev_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_103'] = {'inputs': ['ev_replacement_d2_103'], 'func': ev_replacement_d3_103}


def ev_replacement_d3_104(ev_replacement_d2_104):
    feature = _clean(ev_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_104'] = {'inputs': ['ev_replacement_d2_104'], 'func': ev_replacement_d3_104}


def ev_replacement_d3_105(ev_replacement_d2_105):
    feature = _clean(ev_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_105'] = {'inputs': ['ev_replacement_d2_105'], 'func': ev_replacement_d3_105}


def ev_replacement_d3_106(ev_replacement_d2_106):
    feature = _clean(ev_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_106'] = {'inputs': ['ev_replacement_d2_106'], 'func': ev_replacement_d3_106}


def ev_replacement_d3_107(ev_replacement_d2_107):
    feature = _clean(ev_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_107'] = {'inputs': ['ev_replacement_d2_107'], 'func': ev_replacement_d3_107}


def ev_replacement_d3_108(ev_replacement_d2_108):
    feature = _clean(ev_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_108'] = {'inputs': ['ev_replacement_d2_108'], 'func': ev_replacement_d3_108}


def ev_replacement_d3_109(ev_replacement_d2_109):
    feature = _clean(ev_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_109'] = {'inputs': ['ev_replacement_d2_109'], 'func': ev_replacement_d3_109}


def ev_replacement_d3_110(ev_replacement_d2_110):
    feature = _clean(ev_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_110'] = {'inputs': ['ev_replacement_d2_110'], 'func': ev_replacement_d3_110}


def ev_replacement_d3_111(ev_replacement_d2_111):
    feature = _clean(ev_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_111'] = {'inputs': ['ev_replacement_d2_111'], 'func': ev_replacement_d3_111}


def ev_replacement_d3_112(ev_replacement_d2_112):
    feature = _clean(ev_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_112'] = {'inputs': ['ev_replacement_d2_112'], 'func': ev_replacement_d3_112}


def ev_replacement_d3_113(ev_replacement_d2_113):
    feature = _clean(ev_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_113'] = {'inputs': ['ev_replacement_d2_113'], 'func': ev_replacement_d3_113}


def ev_replacement_d3_114(ev_replacement_d2_114):
    feature = _clean(ev_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_114'] = {'inputs': ['ev_replacement_d2_114'], 'func': ev_replacement_d3_114}


def ev_replacement_d3_115(ev_replacement_d2_115):
    feature = _clean(ev_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_115'] = {'inputs': ['ev_replacement_d2_115'], 'func': ev_replacement_d3_115}


def ev_replacement_d3_116(ev_replacement_d2_116):
    feature = _clean(ev_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_116'] = {'inputs': ['ev_replacement_d2_116'], 'func': ev_replacement_d3_116}


def ev_replacement_d3_117(ev_replacement_d2_117):
    feature = _clean(ev_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_117'] = {'inputs': ['ev_replacement_d2_117'], 'func': ev_replacement_d3_117}


def ev_replacement_d3_118(ev_replacement_d2_118):
    feature = _clean(ev_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_118'] = {'inputs': ['ev_replacement_d2_118'], 'func': ev_replacement_d3_118}


def ev_replacement_d3_119(ev_replacement_d2_119):
    feature = _clean(ev_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_119'] = {'inputs': ['ev_replacement_d2_119'], 'func': ev_replacement_d3_119}


def ev_replacement_d3_120(ev_replacement_d2_120):
    feature = _clean(ev_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_120'] = {'inputs': ['ev_replacement_d2_120'], 'func': ev_replacement_d3_120}


def ev_replacement_d3_121(ev_replacement_d2_121):
    feature = _clean(ev_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_121'] = {'inputs': ['ev_replacement_d2_121'], 'func': ev_replacement_d3_121}


def ev_replacement_d3_122(ev_replacement_d2_122):
    feature = _clean(ev_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_122'] = {'inputs': ['ev_replacement_d2_122'], 'func': ev_replacement_d3_122}


def ev_replacement_d3_123(ev_replacement_d2_123):
    feature = _clean(ev_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_123'] = {'inputs': ['ev_replacement_d2_123'], 'func': ev_replacement_d3_123}


def ev_replacement_d3_124(ev_replacement_d2_124):
    feature = _clean(ev_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_124'] = {'inputs': ['ev_replacement_d2_124'], 'func': ev_replacement_d3_124}


def ev_replacement_d3_125(ev_replacement_d2_125):
    feature = _clean(ev_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_125'] = {'inputs': ['ev_replacement_d2_125'], 'func': ev_replacement_d3_125}


def ev_replacement_d3_126(ev_replacement_d2_126):
    feature = _clean(ev_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_126'] = {'inputs': ['ev_replacement_d2_126'], 'func': ev_replacement_d3_126}


def ev_replacement_d3_127(ev_replacement_d2_127):
    feature = _clean(ev_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_127'] = {'inputs': ['ev_replacement_d2_127'], 'func': ev_replacement_d3_127}


def ev_replacement_d3_128(ev_replacement_d2_128):
    feature = _clean(ev_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_128'] = {'inputs': ['ev_replacement_d2_128'], 'func': ev_replacement_d3_128}


def ev_replacement_d3_129(ev_replacement_d2_129):
    feature = _clean(ev_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_129'] = {'inputs': ['ev_replacement_d2_129'], 'func': ev_replacement_d3_129}


def ev_replacement_d3_130(ev_replacement_d2_130):
    feature = _clean(ev_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_130'] = {'inputs': ['ev_replacement_d2_130'], 'func': ev_replacement_d3_130}


def ev_replacement_d3_131(ev_replacement_d2_131):
    feature = _clean(ev_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_131'] = {'inputs': ['ev_replacement_d2_131'], 'func': ev_replacement_d3_131}


def ev_replacement_d3_132(ev_replacement_d2_132):
    feature = _clean(ev_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_132'] = {'inputs': ['ev_replacement_d2_132'], 'func': ev_replacement_d3_132}


def ev_replacement_d3_133(ev_replacement_d2_133):
    feature = _clean(ev_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_133'] = {'inputs': ['ev_replacement_d2_133'], 'func': ev_replacement_d3_133}


def ev_replacement_d3_134(ev_replacement_d2_134):
    feature = _clean(ev_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_134'] = {'inputs': ['ev_replacement_d2_134'], 'func': ev_replacement_d3_134}


def ev_replacement_d3_135(ev_replacement_d2_135):
    feature = _clean(ev_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_135'] = {'inputs': ['ev_replacement_d2_135'], 'func': ev_replacement_d3_135}


def ev_replacement_d3_136(ev_replacement_d2_136):
    feature = _clean(ev_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_136'] = {'inputs': ['ev_replacement_d2_136'], 'func': ev_replacement_d3_136}


def ev_replacement_d3_137(ev_replacement_d2_137):
    feature = _clean(ev_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_137'] = {'inputs': ['ev_replacement_d2_137'], 'func': ev_replacement_d3_137}


def ev_replacement_d3_138(ev_replacement_d2_138):
    feature = _clean(ev_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_138'] = {'inputs': ['ev_replacement_d2_138'], 'func': ev_replacement_d3_138}


def ev_replacement_d3_139(ev_replacement_d2_139):
    feature = _clean(ev_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_139'] = {'inputs': ['ev_replacement_d2_139'], 'func': ev_replacement_d3_139}


def ev_replacement_d3_140(ev_replacement_d2_140):
    feature = _clean(ev_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_140'] = {'inputs': ['ev_replacement_d2_140'], 'func': ev_replacement_d3_140}


def ev_replacement_d3_141(ev_replacement_d2_141):
    feature = _clean(ev_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_141'] = {'inputs': ['ev_replacement_d2_141'], 'func': ev_replacement_d3_141}


def ev_replacement_d3_142(ev_replacement_d2_142):
    feature = _clean(ev_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_142'] = {'inputs': ['ev_replacement_d2_142'], 'func': ev_replacement_d3_142}


def ev_replacement_d3_143(ev_replacement_d2_143):
    feature = _clean(ev_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_143'] = {'inputs': ['ev_replacement_d2_143'], 'func': ev_replacement_d3_143}


def ev_replacement_d3_144(ev_replacement_d2_144):
    feature = _clean(ev_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_144'] = {'inputs': ['ev_replacement_d2_144'], 'func': ev_replacement_d3_144}


def ev_replacement_d3_145(ev_replacement_d2_145):
    feature = _clean(ev_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_145'] = {'inputs': ['ev_replacement_d2_145'], 'func': ev_replacement_d3_145}


def ev_replacement_d3_146(ev_replacement_d2_146):
    feature = _clean(ev_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_146'] = {'inputs': ['ev_replacement_d2_146'], 'func': ev_replacement_d3_146}


def ev_replacement_d3_147(ev_replacement_d2_147):
    feature = _clean(ev_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_147'] = {'inputs': ['ev_replacement_d2_147'], 'func': ev_replacement_d3_147}


def ev_replacement_d3_148(ev_replacement_d2_148):
    feature = _clean(ev_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_148'] = {'inputs': ['ev_replacement_d2_148'], 'func': ev_replacement_d3_148}


def ev_replacement_d3_149(ev_replacement_d2_149):
    feature = _clean(ev_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_149'] = {'inputs': ['ev_replacement_d2_149'], 'func': ev_replacement_d3_149}


def ev_replacement_d3_150(ev_replacement_d2_150):
    feature = _clean(ev_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_150'] = {'inputs': ['ev_replacement_d2_150'], 'func': ev_replacement_d3_150}


def ev_replacement_d3_151(ev_replacement_d2_151):
    feature = _clean(ev_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_151'] = {'inputs': ['ev_replacement_d2_151'], 'func': ev_replacement_d3_151}


def ev_replacement_d3_152(ev_replacement_d2_152):
    feature = _clean(ev_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_152'] = {'inputs': ['ev_replacement_d2_152'], 'func': ev_replacement_d3_152}


def ev_replacement_d3_153(ev_replacement_d2_153):
    feature = _clean(ev_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_153'] = {'inputs': ['ev_replacement_d2_153'], 'func': ev_replacement_d3_153}


def ev_replacement_d3_154(ev_replacement_d2_154):
    feature = _clean(ev_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_154'] = {'inputs': ['ev_replacement_d2_154'], 'func': ev_replacement_d3_154}


def ev_replacement_d3_155(ev_replacement_d2_155):
    feature = _clean(ev_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_155'] = {'inputs': ['ev_replacement_d2_155'], 'func': ev_replacement_d3_155}


def ev_replacement_d3_156(ev_replacement_d2_156):
    feature = _clean(ev_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_156'] = {'inputs': ['ev_replacement_d2_156'], 'func': ev_replacement_d3_156}


def ev_replacement_d3_157(ev_replacement_d2_157):
    feature = _clean(ev_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_157'] = {'inputs': ['ev_replacement_d2_157'], 'func': ev_replacement_d3_157}


def ev_replacement_d3_158(ev_replacement_d2_158):
    feature = _clean(ev_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_158'] = {'inputs': ['ev_replacement_d2_158'], 'func': ev_replacement_d3_158}


def ev_replacement_d3_159(ev_replacement_d2_159):
    feature = _clean(ev_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_159'] = {'inputs': ['ev_replacement_d2_159'], 'func': ev_replacement_d3_159}


def ev_replacement_d3_160(ev_replacement_d2_160):
    feature = _clean(ev_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_160'] = {'inputs': ['ev_replacement_d2_160'], 'func': ev_replacement_d3_160}


def ev_replacement_d3_161(ev_replacement_d2_161):
    feature = _clean(ev_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_161'] = {'inputs': ['ev_replacement_d2_161'], 'func': ev_replacement_d3_161}


def ev_replacement_d3_162(ev_replacement_d2_162):
    feature = _clean(ev_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_162'] = {'inputs': ['ev_replacement_d2_162'], 'func': ev_replacement_d3_162}


def ev_replacement_d3_163(ev_replacement_d2_163):
    feature = _clean(ev_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_163'] = {'inputs': ['ev_replacement_d2_163'], 'func': ev_replacement_d3_163}


def ev_replacement_d3_164(ev_replacement_d2_164):
    feature = _clean(ev_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_164'] = {'inputs': ['ev_replacement_d2_164'], 'func': ev_replacement_d3_164}


def ev_replacement_d3_165(ev_replacement_d2_165):
    feature = _clean(ev_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_165'] = {'inputs': ['ev_replacement_d2_165'], 'func': ev_replacement_d3_165}


def ev_replacement_d3_166(ev_replacement_d2_166):
    feature = _clean(ev_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
EV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ev_replacement_d3_166'] = {'inputs': ['ev_replacement_d2_166'], 'func': ev_replacement_d3_166}


# Third-derivative extensions for repaired first-base features.
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def evl_base_universe_d3_001_evl_003_fcf_burn_to_cash_63(evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63):
    return _base_universe_d3(evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63, 1)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_001_evl_003_fcf_burn_to_cash_63'] = {'inputs': ['evl_base_universe_d2_001_evl_003_fcf_burn_to_cash_63'], 'func': evl_base_universe_d3_001_evl_003_fcf_burn_to_cash_63}


def evl_base_universe_d3_002_evl_004_debt_to_equity_84(evl_base_universe_d2_002_evl_004_debt_to_equity_84):
    return _base_universe_d3(evl_base_universe_d2_002_evl_004_debt_to_equity_84, 2)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_002_evl_004_debt_to_equity_84'] = {'inputs': ['evl_base_universe_d2_002_evl_004_debt_to_equity_84'], 'func': evl_base_universe_d3_002_evl_004_debt_to_equity_84}


def evl_base_universe_d3_003_evl_005_debt_to_assets_126(evl_base_universe_d2_003_evl_005_debt_to_assets_126):
    return _base_universe_d3(evl_base_universe_d2_003_evl_005_debt_to_assets_126, 3)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_003_evl_005_debt_to_assets_126'] = {'inputs': ['evl_base_universe_d2_003_evl_005_debt_to_assets_126'], 'func': evl_base_universe_d3_003_evl_005_debt_to_assets_126}


def evl_base_universe_d3_004_evl_012_accrual_gap_1260(evl_base_universe_d2_004_evl_012_accrual_gap_1260):
    return _base_universe_d3(evl_base_universe_d2_004_evl_012_accrual_gap_1260, 4)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_004_evl_012_accrual_gap_1260'] = {'inputs': ['evl_base_universe_d2_004_evl_012_accrual_gap_1260'], 'func': evl_base_universe_d3_004_evl_012_accrual_gap_1260}


def evl_base_universe_d3_005_evl_016_debt_to_equity_21(evl_base_universe_d2_005_evl_016_debt_to_equity_21):
    return _base_universe_d3(evl_base_universe_d2_005_evl_016_debt_to_equity_21, 5)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_005_evl_016_debt_to_equity_21'] = {'inputs': ['evl_base_universe_d2_005_evl_016_debt_to_equity_21'], 'func': evl_base_universe_d3_005_evl_016_debt_to_equity_21}


def evl_base_universe_d3_006_evl_017_debt_to_assets_42(evl_base_universe_d2_006_evl_017_debt_to_assets_42):
    return _base_universe_d3(evl_base_universe_d2_006_evl_017_debt_to_assets_42, 6)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_006_evl_017_debt_to_assets_42'] = {'inputs': ['evl_base_universe_d2_006_evl_017_debt_to_assets_42'], 'func': evl_base_universe_d3_006_evl_017_debt_to_assets_42}


def evl_base_universe_d3_007_evl_024_accrual_gap_504(evl_base_universe_d2_007_evl_024_accrual_gap_504):
    return _base_universe_d3(evl_base_universe_d2_007_evl_024_accrual_gap_504, 7)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_007_evl_024_accrual_gap_504'] = {'inputs': ['evl_base_universe_d2_007_evl_024_accrual_gap_504'], 'func': evl_base_universe_d3_007_evl_024_accrual_gap_504}


def evl_base_universe_d3_008_evl_027_fcf_burn_to_cash_1260(evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260):
    return _base_universe_d3(evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260, 8)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_008_evl_027_fcf_burn_to_cash_1260'] = {'inputs': ['evl_base_universe_d2_008_evl_027_fcf_burn_to_cash_1260'], 'func': evl_base_universe_d3_008_evl_027_fcf_burn_to_cash_1260}


def evl_base_universe_d3_009_evl_028_debt_to_equity_1512(evl_base_universe_d2_009_evl_028_debt_to_equity_1512):
    return _base_universe_d3(evl_base_universe_d2_009_evl_028_debt_to_equity_1512, 9)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_009_evl_028_debt_to_equity_1512'] = {'inputs': ['evl_base_universe_d2_009_evl_028_debt_to_equity_1512'], 'func': evl_base_universe_d3_009_evl_028_debt_to_equity_1512}


def evl_base_universe_d3_010_evl_029_debt_to_assets_63(evl_base_universe_d2_010_evl_029_debt_to_assets_63):
    return _base_universe_d3(evl_base_universe_d2_010_evl_029_debt_to_assets_63, 10)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_010_evl_029_debt_to_assets_63'] = {'inputs': ['evl_base_universe_d2_010_evl_029_debt_to_assets_63'], 'func': evl_base_universe_d3_010_evl_029_debt_to_assets_63}


def evl_base_universe_d3_011_evl_031_interest_coverage_stress_21(evl_base_universe_d2_011_evl_031_interest_coverage_stress_21):
    return _base_universe_d3(evl_base_universe_d2_011_evl_031_interest_coverage_stress_21, 11)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_011_evl_031_interest_coverage_stress_21'] = {'inputs': ['evl_base_universe_d2_011_evl_031_interest_coverage_stress_21'], 'func': evl_base_universe_d3_011_evl_031_interest_coverage_stress_21}


def evl_base_universe_d3_012_evl_036_accrual_gap_189(evl_base_universe_d2_012_evl_036_accrual_gap_189):
    return _base_universe_d3(evl_base_universe_d2_012_evl_036_accrual_gap_189, 12)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_012_evl_036_accrual_gap_189'] = {'inputs': ['evl_base_universe_d2_012_evl_036_accrual_gap_189'], 'func': evl_base_universe_d3_012_evl_036_accrual_gap_189}


def evl_base_universe_d3_013_evl_039_fcf_burn_to_cash_504(evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504):
    return _base_universe_d3(evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504, 13)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_013_evl_039_fcf_burn_to_cash_504'] = {'inputs': ['evl_base_universe_d2_013_evl_039_fcf_burn_to_cash_504'], 'func': evl_base_universe_d3_013_evl_039_fcf_burn_to_cash_504}


def evl_base_universe_d3_014_evl_040_debt_to_equity_756(evl_base_universe_d2_014_evl_040_debt_to_equity_756):
    return _base_universe_d3(evl_base_universe_d2_014_evl_040_debt_to_equity_756, 14)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_014_evl_040_debt_to_equity_756'] = {'inputs': ['evl_base_universe_d2_014_evl_040_debt_to_equity_756'], 'func': evl_base_universe_d3_014_evl_040_debt_to_equity_756}


def evl_base_universe_d3_015_evl_041_debt_to_assets_1008(evl_base_universe_d2_015_evl_041_debt_to_assets_1008):
    return _base_universe_d3(evl_base_universe_d2_015_evl_041_debt_to_assets_1008, 15)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_015_evl_041_debt_to_assets_1008'] = {'inputs': ['evl_base_universe_d2_015_evl_041_debt_to_assets_1008'], 'func': evl_base_universe_d3_015_evl_041_debt_to_assets_1008}


def evl_base_universe_d3_016_evl_043_interest_coverage_stress_1512(evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512):
    return _base_universe_d3(evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512, 16)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_016_evl_043_interest_coverage_stress_1512'] = {'inputs': ['evl_base_universe_d2_016_evl_043_interest_coverage_stress_1512'], 'func': evl_base_universe_d3_016_evl_043_interest_coverage_stress_1512}


def evl_base_universe_d3_017_evl_048_accrual_gap_63(evl_base_universe_d2_017_evl_048_accrual_gap_63):
    return _base_universe_d3(evl_base_universe_d2_017_evl_048_accrual_gap_63, 17)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_017_evl_048_accrual_gap_63'] = {'inputs': ['evl_base_universe_d2_017_evl_048_accrual_gap_63'], 'func': evl_base_universe_d3_017_evl_048_accrual_gap_63}


def evl_base_universe_d3_018_evl_051_fcf_burn_to_cash_189(evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189):
    return _base_universe_d3(evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189, 18)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_018_evl_051_fcf_burn_to_cash_189'] = {'inputs': ['evl_base_universe_d2_018_evl_051_fcf_burn_to_cash_189'], 'func': evl_base_universe_d3_018_evl_051_fcf_burn_to_cash_189}


def evl_base_universe_d3_019_evl_052_debt_to_equity_252(evl_base_universe_d2_019_evl_052_debt_to_equity_252):
    return _base_universe_d3(evl_base_universe_d2_019_evl_052_debt_to_equity_252, 19)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_019_evl_052_debt_to_equity_252'] = {'inputs': ['evl_base_universe_d2_019_evl_052_debt_to_equity_252'], 'func': evl_base_universe_d3_019_evl_052_debt_to_equity_252}


def evl_base_universe_d3_020_evl_053_debt_to_assets_378(evl_base_universe_d2_020_evl_053_debt_to_assets_378):
    return _base_universe_d3(evl_base_universe_d2_020_evl_053_debt_to_assets_378, 20)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_020_evl_053_debt_to_assets_378'] = {'inputs': ['evl_base_universe_d2_020_evl_053_debt_to_assets_378'], 'func': evl_base_universe_d3_020_evl_053_debt_to_assets_378}


def evl_base_universe_d3_021_evl_055_interest_coverage_stress_756(evl_base_universe_d2_021_evl_055_interest_coverage_stress_756):
    return _base_universe_d3(evl_base_universe_d2_021_evl_055_interest_coverage_stress_756, 21)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_021_evl_055_interest_coverage_stress_756'] = {'inputs': ['evl_base_universe_d2_021_evl_055_interest_coverage_stress_756'], 'func': evl_base_universe_d3_021_evl_055_interest_coverage_stress_756}


def evl_base_universe_d3_022_evl_060_accrual_gap_252(evl_base_universe_d2_022_evl_060_accrual_gap_252):
    return _base_universe_d3(evl_base_universe_d2_022_evl_060_accrual_gap_252, 22)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_022_evl_060_accrual_gap_252'] = {'inputs': ['evl_base_universe_d2_022_evl_060_accrual_gap_252'], 'func': evl_base_universe_d3_022_evl_060_accrual_gap_252}


def evl_base_universe_d3_023_evl_basefill_001(evl_base_universe_d2_023_evl_basefill_001):
    return _base_universe_d3(evl_base_universe_d2_023_evl_basefill_001, 23)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_023_evl_basefill_001'] = {'inputs': ['evl_base_universe_d2_023_evl_basefill_001'], 'func': evl_base_universe_d3_023_evl_basefill_001}


def evl_base_universe_d3_024_evl_basefill_002(evl_base_universe_d2_024_evl_basefill_002):
    return _base_universe_d3(evl_base_universe_d2_024_evl_basefill_002, 24)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_024_evl_basefill_002'] = {'inputs': ['evl_base_universe_d2_024_evl_basefill_002'], 'func': evl_base_universe_d3_024_evl_basefill_002}


def evl_base_universe_d3_025_evl_basefill_006(evl_base_universe_d2_025_evl_basefill_006):
    return _base_universe_d3(evl_base_universe_d2_025_evl_basefill_006, 25)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_025_evl_basefill_006'] = {'inputs': ['evl_base_universe_d2_025_evl_basefill_006'], 'func': evl_base_universe_d3_025_evl_basefill_006}


def evl_base_universe_d3_026_evl_basefill_008(evl_base_universe_d2_026_evl_basefill_008):
    return _base_universe_d3(evl_base_universe_d2_026_evl_basefill_008, 26)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_026_evl_basefill_008'] = {'inputs': ['evl_base_universe_d2_026_evl_basefill_008'], 'func': evl_base_universe_d3_026_evl_basefill_008}


def evl_base_universe_d3_027_evl_basefill_009(evl_base_universe_d2_027_evl_basefill_009):
    return _base_universe_d3(evl_base_universe_d2_027_evl_basefill_009, 27)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_027_evl_basefill_009'] = {'inputs': ['evl_base_universe_d2_027_evl_basefill_009'], 'func': evl_base_universe_d3_027_evl_basefill_009}


def evl_base_universe_d3_028_evl_basefill_010(evl_base_universe_d2_028_evl_basefill_010):
    return _base_universe_d3(evl_base_universe_d2_028_evl_basefill_010, 28)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_028_evl_basefill_010'] = {'inputs': ['evl_base_universe_d2_028_evl_basefill_010'], 'func': evl_base_universe_d3_028_evl_basefill_010}


def evl_base_universe_d3_029_evl_basefill_011(evl_base_universe_d2_029_evl_basefill_011):
    return _base_universe_d3(evl_base_universe_d2_029_evl_basefill_011, 29)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_029_evl_basefill_011'] = {'inputs': ['evl_base_universe_d2_029_evl_basefill_011'], 'func': evl_base_universe_d3_029_evl_basefill_011}


def evl_base_universe_d3_030_evl_basefill_013(evl_base_universe_d2_030_evl_basefill_013):
    return _base_universe_d3(evl_base_universe_d2_030_evl_basefill_013, 30)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_030_evl_basefill_013'] = {'inputs': ['evl_base_universe_d2_030_evl_basefill_013'], 'func': evl_base_universe_d3_030_evl_basefill_013}


def evl_base_universe_d3_031_evl_basefill_014(evl_base_universe_d2_031_evl_basefill_014):
    return _base_universe_d3(evl_base_universe_d2_031_evl_basefill_014, 31)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_031_evl_basefill_014'] = {'inputs': ['evl_base_universe_d2_031_evl_basefill_014'], 'func': evl_base_universe_d3_031_evl_basefill_014}


def evl_base_universe_d3_032_evl_basefill_015(evl_base_universe_d2_032_evl_basefill_015):
    return _base_universe_d3(evl_base_universe_d2_032_evl_basefill_015, 32)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_032_evl_basefill_015'] = {'inputs': ['evl_base_universe_d2_032_evl_basefill_015'], 'func': evl_base_universe_d3_032_evl_basefill_015}


def evl_base_universe_d3_033_evl_basefill_018(evl_base_universe_d2_033_evl_basefill_018):
    return _base_universe_d3(evl_base_universe_d2_033_evl_basefill_018, 33)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_033_evl_basefill_018'] = {'inputs': ['evl_base_universe_d2_033_evl_basefill_018'], 'func': evl_base_universe_d3_033_evl_basefill_018}


def evl_base_universe_d3_034_evl_basefill_020(evl_base_universe_d2_034_evl_basefill_020):
    return _base_universe_d3(evl_base_universe_d2_034_evl_basefill_020, 34)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_034_evl_basefill_020'] = {'inputs': ['evl_base_universe_d2_034_evl_basefill_020'], 'func': evl_base_universe_d3_034_evl_basefill_020}


def evl_base_universe_d3_035_evl_basefill_021(evl_base_universe_d2_035_evl_basefill_021):
    return _base_universe_d3(evl_base_universe_d2_035_evl_basefill_021, 35)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_035_evl_basefill_021'] = {'inputs': ['evl_base_universe_d2_035_evl_basefill_021'], 'func': evl_base_universe_d3_035_evl_basefill_021}


def evl_base_universe_d3_036_evl_basefill_022(evl_base_universe_d2_036_evl_basefill_022):
    return _base_universe_d3(evl_base_universe_d2_036_evl_basefill_022, 36)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_036_evl_basefill_022'] = {'inputs': ['evl_base_universe_d2_036_evl_basefill_022'], 'func': evl_base_universe_d3_036_evl_basefill_022}


def evl_base_universe_d3_037_evl_basefill_023(evl_base_universe_d2_037_evl_basefill_023):
    return _base_universe_d3(evl_base_universe_d2_037_evl_basefill_023, 37)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_037_evl_basefill_023'] = {'inputs': ['evl_base_universe_d2_037_evl_basefill_023'], 'func': evl_base_universe_d3_037_evl_basefill_023}


def evl_base_universe_d3_038_evl_basefill_025(evl_base_universe_d2_038_evl_basefill_025):
    return _base_universe_d3(evl_base_universe_d2_038_evl_basefill_025, 38)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_038_evl_basefill_025'] = {'inputs': ['evl_base_universe_d2_038_evl_basefill_025'], 'func': evl_base_universe_d3_038_evl_basefill_025}


def evl_base_universe_d3_039_evl_basefill_026(evl_base_universe_d2_039_evl_basefill_026):
    return _base_universe_d3(evl_base_universe_d2_039_evl_basefill_026, 39)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_039_evl_basefill_026'] = {'inputs': ['evl_base_universe_d2_039_evl_basefill_026'], 'func': evl_base_universe_d3_039_evl_basefill_026}


def evl_base_universe_d3_040_evl_basefill_030(evl_base_universe_d2_040_evl_basefill_030):
    return _base_universe_d3(evl_base_universe_d2_040_evl_basefill_030, 40)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_040_evl_basefill_030'] = {'inputs': ['evl_base_universe_d2_040_evl_basefill_030'], 'func': evl_base_universe_d3_040_evl_basefill_030}


def evl_base_universe_d3_041_evl_basefill_032(evl_base_universe_d2_041_evl_basefill_032):
    return _base_universe_d3(evl_base_universe_d2_041_evl_basefill_032, 41)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_041_evl_basefill_032'] = {'inputs': ['evl_base_universe_d2_041_evl_basefill_032'], 'func': evl_base_universe_d3_041_evl_basefill_032}


def evl_base_universe_d3_042_evl_basefill_033(evl_base_universe_d2_042_evl_basefill_033):
    return _base_universe_d3(evl_base_universe_d2_042_evl_basefill_033, 42)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_042_evl_basefill_033'] = {'inputs': ['evl_base_universe_d2_042_evl_basefill_033'], 'func': evl_base_universe_d3_042_evl_basefill_033}


def evl_base_universe_d3_043_evl_basefill_034(evl_base_universe_d2_043_evl_basefill_034):
    return _base_universe_d3(evl_base_universe_d2_043_evl_basefill_034, 43)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_043_evl_basefill_034'] = {'inputs': ['evl_base_universe_d2_043_evl_basefill_034'], 'func': evl_base_universe_d3_043_evl_basefill_034}


def evl_base_universe_d3_044_evl_basefill_035(evl_base_universe_d2_044_evl_basefill_035):
    return _base_universe_d3(evl_base_universe_d2_044_evl_basefill_035, 44)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_044_evl_basefill_035'] = {'inputs': ['evl_base_universe_d2_044_evl_basefill_035'], 'func': evl_base_universe_d3_044_evl_basefill_035}


def evl_base_universe_d3_045_evl_basefill_037(evl_base_universe_d2_045_evl_basefill_037):
    return _base_universe_d3(evl_base_universe_d2_045_evl_basefill_037, 45)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_045_evl_basefill_037'] = {'inputs': ['evl_base_universe_d2_045_evl_basefill_037'], 'func': evl_base_universe_d3_045_evl_basefill_037}


def evl_base_universe_d3_046_evl_basefill_038(evl_base_universe_d2_046_evl_basefill_038):
    return _base_universe_d3(evl_base_universe_d2_046_evl_basefill_038, 46)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_046_evl_basefill_038'] = {'inputs': ['evl_base_universe_d2_046_evl_basefill_038'], 'func': evl_base_universe_d3_046_evl_basefill_038}


def evl_base_universe_d3_047_evl_basefill_042(evl_base_universe_d2_047_evl_basefill_042):
    return _base_universe_d3(evl_base_universe_d2_047_evl_basefill_042, 47)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_047_evl_basefill_042'] = {'inputs': ['evl_base_universe_d2_047_evl_basefill_042'], 'func': evl_base_universe_d3_047_evl_basefill_042}


def evl_base_universe_d3_048_evl_basefill_044(evl_base_universe_d2_048_evl_basefill_044):
    return _base_universe_d3(evl_base_universe_d2_048_evl_basefill_044, 48)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_048_evl_basefill_044'] = {'inputs': ['evl_base_universe_d2_048_evl_basefill_044'], 'func': evl_base_universe_d3_048_evl_basefill_044}


def evl_base_universe_d3_049_evl_basefill_045(evl_base_universe_d2_049_evl_basefill_045):
    return _base_universe_d3(evl_base_universe_d2_049_evl_basefill_045, 49)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_049_evl_basefill_045'] = {'inputs': ['evl_base_universe_d2_049_evl_basefill_045'], 'func': evl_base_universe_d3_049_evl_basefill_045}


def evl_base_universe_d3_050_evl_basefill_046(evl_base_universe_d2_050_evl_basefill_046):
    return _base_universe_d3(evl_base_universe_d2_050_evl_basefill_046, 50)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_050_evl_basefill_046'] = {'inputs': ['evl_base_universe_d2_050_evl_basefill_046'], 'func': evl_base_universe_d3_050_evl_basefill_046}


def evl_base_universe_d3_051_evl_basefill_047(evl_base_universe_d2_051_evl_basefill_047):
    return _base_universe_d3(evl_base_universe_d2_051_evl_basefill_047, 51)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_051_evl_basefill_047'] = {'inputs': ['evl_base_universe_d2_051_evl_basefill_047'], 'func': evl_base_universe_d3_051_evl_basefill_047}


def evl_base_universe_d3_052_evl_basefill_049(evl_base_universe_d2_052_evl_basefill_049):
    return _base_universe_d3(evl_base_universe_d2_052_evl_basefill_049, 52)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_052_evl_basefill_049'] = {'inputs': ['evl_base_universe_d2_052_evl_basefill_049'], 'func': evl_base_universe_d3_052_evl_basefill_049}


def evl_base_universe_d3_053_evl_basefill_050(evl_base_universe_d2_053_evl_basefill_050):
    return _base_universe_d3(evl_base_universe_d2_053_evl_basefill_050, 53)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_053_evl_basefill_050'] = {'inputs': ['evl_base_universe_d2_053_evl_basefill_050'], 'func': evl_base_universe_d3_053_evl_basefill_050}


def evl_base_universe_d3_054_evl_basefill_054(evl_base_universe_d2_054_evl_basefill_054):
    return _base_universe_d3(evl_base_universe_d2_054_evl_basefill_054, 54)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_054_evl_basefill_054'] = {'inputs': ['evl_base_universe_d2_054_evl_basefill_054'], 'func': evl_base_universe_d3_054_evl_basefill_054}


def evl_base_universe_d3_055_evl_basefill_056(evl_base_universe_d2_055_evl_basefill_056):
    return _base_universe_d3(evl_base_universe_d2_055_evl_basefill_056, 55)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_055_evl_basefill_056'] = {'inputs': ['evl_base_universe_d2_055_evl_basefill_056'], 'func': evl_base_universe_d3_055_evl_basefill_056}


def evl_base_universe_d3_056_evl_basefill_057(evl_base_universe_d2_056_evl_basefill_057):
    return _base_universe_d3(evl_base_universe_d2_056_evl_basefill_057, 56)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_056_evl_basefill_057'] = {'inputs': ['evl_base_universe_d2_056_evl_basefill_057'], 'func': evl_base_universe_d3_056_evl_basefill_057}


def evl_base_universe_d3_057_evl_basefill_058(evl_base_universe_d2_057_evl_basefill_058):
    return _base_universe_d3(evl_base_universe_d2_057_evl_basefill_058, 57)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_057_evl_basefill_058'] = {'inputs': ['evl_base_universe_d2_057_evl_basefill_058'], 'func': evl_base_universe_d3_057_evl_basefill_058}


def evl_base_universe_d3_058_evl_basefill_059(evl_base_universe_d2_058_evl_basefill_059):
    return _base_universe_d3(evl_base_universe_d2_058_evl_basefill_059, 58)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_058_evl_basefill_059'] = {'inputs': ['evl_base_universe_d2_058_evl_basefill_059'], 'func': evl_base_universe_d3_058_evl_basefill_059}


def evl_base_universe_d3_059_evl_basefill_061(evl_base_universe_d2_059_evl_basefill_061):
    return _base_universe_d3(evl_base_universe_d2_059_evl_basefill_061, 59)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_059_evl_basefill_061'] = {'inputs': ['evl_base_universe_d2_059_evl_basefill_061'], 'func': evl_base_universe_d3_059_evl_basefill_061}


def evl_base_universe_d3_060_evl_basefill_062(evl_base_universe_d2_060_evl_basefill_062):
    return _base_universe_d3(evl_base_universe_d2_060_evl_basefill_062, 60)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_060_evl_basefill_062'] = {'inputs': ['evl_base_universe_d2_060_evl_basefill_062'], 'func': evl_base_universe_d3_060_evl_basefill_062}


def evl_base_universe_d3_061_evl_basefill_063(evl_base_universe_d2_061_evl_basefill_063):
    return _base_universe_d3(evl_base_universe_d2_061_evl_basefill_063, 61)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_061_evl_basefill_063'] = {'inputs': ['evl_base_universe_d2_061_evl_basefill_063'], 'func': evl_base_universe_d3_061_evl_basefill_063}


def evl_base_universe_d3_062_evl_basefill_064(evl_base_universe_d2_062_evl_basefill_064):
    return _base_universe_d3(evl_base_universe_d2_062_evl_basefill_064, 62)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_062_evl_basefill_064'] = {'inputs': ['evl_base_universe_d2_062_evl_basefill_064'], 'func': evl_base_universe_d3_062_evl_basefill_064}


def evl_base_universe_d3_063_evl_basefill_065(evl_base_universe_d2_063_evl_basefill_065):
    return _base_universe_d3(evl_base_universe_d2_063_evl_basefill_065, 63)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_063_evl_basefill_065'] = {'inputs': ['evl_base_universe_d2_063_evl_basefill_065'], 'func': evl_base_universe_d3_063_evl_basefill_065}


def evl_base_universe_d3_064_evl_basefill_066(evl_base_universe_d2_064_evl_basefill_066):
    return _base_universe_d3(evl_base_universe_d2_064_evl_basefill_066, 64)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_064_evl_basefill_066'] = {'inputs': ['evl_base_universe_d2_064_evl_basefill_066'], 'func': evl_base_universe_d3_064_evl_basefill_066}


def evl_base_universe_d3_065_evl_basefill_067(evl_base_universe_d2_065_evl_basefill_067):
    return _base_universe_d3(evl_base_universe_d2_065_evl_basefill_067, 65)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_065_evl_basefill_067'] = {'inputs': ['evl_base_universe_d2_065_evl_basefill_067'], 'func': evl_base_universe_d3_065_evl_basefill_067}


def evl_base_universe_d3_066_evl_basefill_068(evl_base_universe_d2_066_evl_basefill_068):
    return _base_universe_d3(evl_base_universe_d2_066_evl_basefill_068, 66)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_066_evl_basefill_068'] = {'inputs': ['evl_base_universe_d2_066_evl_basefill_068'], 'func': evl_base_universe_d3_066_evl_basefill_068}


def evl_base_universe_d3_067_evl_basefill_069(evl_base_universe_d2_067_evl_basefill_069):
    return _base_universe_d3(evl_base_universe_d2_067_evl_basefill_069, 67)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_067_evl_basefill_069'] = {'inputs': ['evl_base_universe_d2_067_evl_basefill_069'], 'func': evl_base_universe_d3_067_evl_basefill_069}


def evl_base_universe_d3_068_evl_basefill_070(evl_base_universe_d2_068_evl_basefill_070):
    return _base_universe_d3(evl_base_universe_d2_068_evl_basefill_070, 68)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_068_evl_basefill_070'] = {'inputs': ['evl_base_universe_d2_068_evl_basefill_070'], 'func': evl_base_universe_d3_068_evl_basefill_070}


def evl_base_universe_d3_069_evl_basefill_071(evl_base_universe_d2_069_evl_basefill_071):
    return _base_universe_d3(evl_base_universe_d2_069_evl_basefill_071, 69)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_069_evl_basefill_071'] = {'inputs': ['evl_base_universe_d2_069_evl_basefill_071'], 'func': evl_base_universe_d3_069_evl_basefill_071}


def evl_base_universe_d3_070_evl_basefill_072(evl_base_universe_d2_070_evl_basefill_072):
    return _base_universe_d3(evl_base_universe_d2_070_evl_basefill_072, 70)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_070_evl_basefill_072'] = {'inputs': ['evl_base_universe_d2_070_evl_basefill_072'], 'func': evl_base_universe_d3_070_evl_basefill_072}


def evl_base_universe_d3_071_evl_basefill_073(evl_base_universe_d2_071_evl_basefill_073):
    return _base_universe_d3(evl_base_universe_d2_071_evl_basefill_073, 71)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_071_evl_basefill_073'] = {'inputs': ['evl_base_universe_d2_071_evl_basefill_073'], 'func': evl_base_universe_d3_071_evl_basefill_073}


def evl_base_universe_d3_072_evl_basefill_074(evl_base_universe_d2_072_evl_basefill_074):
    return _base_universe_d3(evl_base_universe_d2_072_evl_basefill_074, 72)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_072_evl_basefill_074'] = {'inputs': ['evl_base_universe_d2_072_evl_basefill_074'], 'func': evl_base_universe_d3_072_evl_basefill_074}


def evl_base_universe_d3_073_evl_basefill_075(evl_base_universe_d2_073_evl_basefill_075):
    return _base_universe_d3(evl_base_universe_d2_073_evl_basefill_075, 73)
EVL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['evl_base_universe_d3_073_evl_basefill_075'] = {'inputs': ['evl_base_universe_d2_073_evl_basefill_075'], 'func': evl_base_universe_d3_073_evl_basefill_075}
