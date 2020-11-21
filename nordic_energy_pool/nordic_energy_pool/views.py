# -*- encoding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from nordic_energy_pool import settings
from nordic_energy_pool.ethereum import get_user_events, get_user_rewards, get_block_7_days_ago
from nordic_energy_pool.models import PendingRewardOrStakeIncrease
from nordic_energy_pool.stats import get_stats
from django.db.models import Sum
import time


def health(request):
    return HttpResponse("ok")


def index(request):
    return redirect('/pools/')


def pools(request):
    daily_rewards, accumulated = get_stats()
    return render(request, 'templates/pools.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS,
                                                    'contractAddress2': settings.nordic_energy_POOL_CONTRACT_ADDRESS_2,
                                                    'daily_rewards': daily_rewards,
                                                    'accumulated': accumulated
                                                    })


def deposit(request):
    return render(request, 'templates/deposit.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS,
                                                      'tokenAddress': settings.nordic_energy_TOKEN_CONTRACT_ADDRESS})


def deposit2(request):
    return render(request, 'templates/deposit.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS_2,
                                                      'tokenAddress': settings.nordic_energy_TOKEN_CONTRACT_ADDRESS})


def balances(request):
    return render(request, 'templates/balances.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS,
                                                       'contractAddress2': settings.nordic_energy_POOL_CONTRACT_ADDRESS_2})


def history(request):
    seven_days_ago = get_block_7_days_ago()
    return render(request, 'templates/history.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS,
                                                      'contractAddress2': settings.nordic_energy_POOL_CONTRACT_ADDRESS_2,
                                                      'seven_days_ago': seven_days_ago})


def faq(request):
    return render(request, 'templates/faq.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS})


def pool(request):
    return render(request, 'templates/pool.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS})


def pool2(request):
    return render(request, 'templates/pool.html', {'contractAddress': settings.nordic_energy_POOL_CONTRACT_ADDRESS_2})


def ajax_user_rewards(request, wallet):
    ordered_dates, values = get_user_rewards(wallet)
    return JsonResponse({'dates': ordered_dates, 'values': values})


def ajax_user_events(request, wallet, pool):
    events = get_user_events(wallet, pool)
    parsed = [{'event': "StakeIncreased" if e.compound else "PendingRewardsUpdated",
               'timestamp': time.mktime(e.date.timetuple()),
               'compound': e.compound,
               'total': e.total,
               'index': e.stake_index + 1} for e in events]
    return JsonResponse({'events': parsed})


def ajax_user_pending(request, wallet, index, pool):
    result = PendingRewardOrStakeIncrease.objects.filter(staker__iexact=wallet,
                                                         stake_index=index,
                                                         staking_pool_contract=pool,
                                                         accredited_in_contract=False).aggregate(Sum('total'))
    return JsonResponse({'total': result['total__sum']})
