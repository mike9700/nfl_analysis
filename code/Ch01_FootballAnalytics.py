## Python
import pandas as pd
import nfl_data_py as nfl

pbp_py = nfl.import_pbp_data([2026])

# Fetch weekly stats for the 2023 season
#weekly_df = nfl.import_weekly_data([2023])
#print(weekly_df.head())

filter_crit = 'play_type == "pass" & air_yards.notnull()'

pbp_py_p = (
    pbp_py.query(filter_crit)
    .groupby(["passer_id", "passer"])
    .agg({"air_yards": ["count", "mean"]})
)

pbp_py_p.columns = list(map("_".join, pbp_py_p.columns.values))
sort_crit = "air_yards_count > 100"
print(
    pbp_py_p.query(sort_crit)\
        .sort_values(by="air_yards_mean", ascending=[False])\
            .to_string()
)

"""
**nfl_data_py** is a Python package that streamlines the importing
of a variety of different American football datasets. It also includes
tables to assist with the merging of datasets from various sources.

Functions
---------
import_pbp_data() - import play-by-play data
import_weekly_data() - import weekly player stats
import_seasonal_data() - import seasonal player stats
import_snap_counts() - import weekly snap count stats
import_ngs_data() - import NGS advanced analytics
import_qbr() - import QBR for NFL or college
import_seasonal_pfr() - import advanced stats from PFR on a seasonal basis
import_weekly_pfr() - import advanced stats from PFR on a weekly basis
import_officials() - import details on game officials
import_schedules() - import weekly teams schedules
import_seasonal_rosters() - import yearly team rosters
import_weekly_rosters() - import team rosters by week, including in-season updates
import_players() - import descriptive data for all players
import_depth_charts() - import team depth charts
import_injuries() - import team injury reports
import_ids() - import mapping of player ids for more major sites
import_contracts() - import contract data
import_win_totals() - import win total lines for teams
import_sc_lines() - import weekly betting lines for teams
import_draft_picks() - import draft pick history
import_draft_values() - import draft value models by pick
import_combine_data() - import combine stats
import_ftn_data() - import FTN charting data
see_pbp_cols() - return list of play-by-play columns
see_weekly_cols() - return list of weekly stat columns
import_team_desc() - import descriptive data for team viz
cache_pbp() - save pbp files locally to allow for faster loading
clean_nfl_data() - clean df by aligning common name diffs
"""