from nordic_energy_pool.models import Stat


def get_stats():
    all_stats = Stat.objects.all()

    daily = []
    accumulated = []
    total = 0
    for stat in all_stats:
        total += int(stat.miningRewards)
        accumulated.append({'date': stat.date, 'miningRewards': total})
        daily.append({'date': stat.date, 'miningRewards': stat.miningRewards})

    if len(daily) > 30:
        daily = daily[-30:]
        accumulated = accumulated[-30:]

    return daily, accumulated


def get_daily_rewards_per_date():
    stats = Stat.objects.all()
    return stats
