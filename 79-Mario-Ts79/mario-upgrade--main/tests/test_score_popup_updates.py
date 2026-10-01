import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')

import unittest

import pygame as pg

from source.states.level import Level


class ExpiringScore:
    def __init__(self):
        self.update_count = 0

    def update(self, score_list):
        self.update_count += 1
        score_list.remove(self)


class ScorePopupUpdateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pg.init()

    def test_all_expiring_popups_update_in_the_same_frame(self):
        level = Level.__new__(Level)
        first = ExpiringScore()
        second = ExpiringScore()
        level.moving_score_list = [first, second]

        level.update_moving_scores()

        self.assertEqual(first.update_count, 1)
        self.assertEqual(second.update_count, 1)
        self.assertEqual(level.moving_score_list, [])