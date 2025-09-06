from dataclasses import dataclass
from typing import Tuple


@dataclass
class GamePositions:
    collect_2x_rewards: Tuple[int, int] = (1220, 522)
    collect_2x_rewards_confirm: Tuple[int, int] = (1272, 557)


@dataclass
class SettingsPositions:
    app: Tuple[int, int] = (1170, 535)
    search_bar: Tuple[int, int] = (1174, 191)
    date_time: Tuple[int, int] = (1168, 164)
    auto_toggle: Tuple[int, int] = (1400, 232)
    select_date: Tuple[int, int] = (1279, 300) 
    current_day: Tuple[int, int] = (1319, 400)  # CHANGE ON STARTUP
    change_day: Tuple[int, int] = (1239, 550)  # CHANGE ON STARTUP


@dataclass
class GeneralScreenPositions:
    exit_bar_bottom: Tuple[int, int] = (1284, 731)


@dataclass
class AppPositions:
    idle_miner_tycoon: Tuple[int, int] = (1168, 229)
    settings: Tuple[int, int] = SettingsPositions().app
