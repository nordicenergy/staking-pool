from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Stat(models.Model):
    date = models.DateField(unique=True)
    miningRewards = models.TextField()
    totalStaked = models.TextField()
    totalStakes = models.IntegerField()
    totalVesting = models.TextField()
    fromBlock = models.BigIntegerField(unique=True)
    upToBlock = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"


class PendingRewardOrStakeIncrease(models.Model):
    date = models.DateTimeField(timezone.now())
    total = models.TextField()
    compound = models.BooleanField(default=False)
    staker = models.TextField()
    stake_index = models.IntegerField()
    accredited_in_contract = models.BooleanField(default=False)
    staking_pool_contract = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Pending Reward or Stake Increase"
        verbose_name_plural = "Pending Rewards or Stake Increases"



