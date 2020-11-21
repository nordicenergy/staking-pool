import datetime

from web3 import Web3, WebsocketProvider, HTTPProvider

from nordic_energy_pool.models import PendingRewardOrStakeIncrease
from nordic_energy_pool.settings import INFURA

PADDING_ZEROS = 1000000000000000000



def get_block_7_days_ago():
    w3 = Web3(HTTPProvider(INFURA))
    return w3.eth.getBlock('latest').number - 60000


def get_event_date(number):
    w3 = Web3(HTTPProvider(INFURA))
    block = w3.eth.getBlock(number)
    block_datetime = datetime.datetime.fromtimestamp(block.timestamp)
    return block_datetime


def get_user_events(wallet, pool):
    events = PendingRewardOrStakeIncrease.objects.filter(staker__iexact=wallet, staking_pool_contract=pool)
    return events


def get_user_rewards(wallet):
    today = datetime.date.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    pending_rewards = PendingRewardOrStakeIncrease.objects.filter(staker__iexact=wallet,
                                                                  date__gte=seven_days_ago).order_by('date')

    dates = {}
    for pending in pending_rewards:
        date = pending.date.date()
        total = int(pending.total) / PADDING_ZEROS
        if date in dates:
            dates[date] += total
        else:
            dates[date] = total

    ordered_dates = list(dates.keys())
    ordered_dates.sort()
    values = []
    new_dates = []

    for date in ordered_dates:
        values.append(dates[date])
        new_dates.append(date.strftime("%b %d"))

    return new_dates, values
